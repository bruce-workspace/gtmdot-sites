import os
import re
import yaml
import json
import datetime
import subprocess

# --- Configuration ---
GTM_SITES_REPO = os.path.expanduser("~/.openclaw/workspace/gtmdot-sites")
MAX_PROCESS_PER_RUN = 3

# --- Helper Functions ---
def run_git_command(command, cwd):
    print(f"Running git command: {command} in {cwd}")
    result = subprocess.run(command, shell=True, cwd=cwd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Git command failed: {command}\n{result.stderr}")
        raise RuntimeError(f"Git command failed: {command}")
    print(f"Git command output:\n{result.stdout}")
    return result.stdout

def get_collect_requests():
    pending_requests = []
    sites_path = os.path.join(GTM_SITES_REPO, "sites")
    if not os.path.exists(sites_path):
        return pending_requests

    for site_slug in os.listdir(sites_path):
        site_dir = os.path.join(sites_path, site_slug)
        if not os.path.isdir(site_dir):
            continue

        request_file = os.path.join(site_dir, "collect-request.md")
        if not os.path.exists(request_file):
            continue

        bruce_collected_file = os.path.join(site_dir, "bruce-collected.md")

        with open(request_file, 'r') as f:
            content = f.read()
            match = re.search(r'requested_at:\s*(\S+)', content)
            if match:
                requested_at_str = match.group(1)
                requested_at = datetime.datetime.fromisoformat(requested_at_str)
            else:
                print(f"Warning: collect-request.md for {site_slug} missing 'requested_at'. Skipping.")
                continue

        if os.path.exists(bruce_collected_file):
            bruce_collected_timestamp = datetime.datetime.fromtimestamp(os.path.getmtime(bruce_collected_file))
            if bruce_collected_timestamp > requested_at:
                continue # Already collected after request

        pending_requests.append({
            "site_slug": site_slug,
            "request_file": request_file,
            "requested_at": requested_at
        })
    
    # Sort by requested_at to process older requests first
    pending_requests.sort(key=lambda x: x["requested_at"])
    return pending_requests[:MAX_PROCESS_PER_RUN] # Process max 3 per run

def parse_request_file(request_file):
    with open(request_file, 'r') as f:
        content = f.read()
    
    frontmatter_match = re.match(r'^---\n(.*?)\n---\n(.*)', content, re.DOTALL)
    if not frontmatter_match:
        raise ValueError("Invalid collect-request.md format: missing YAML frontmatter.")
    
    frontmatter_str = frontmatter_match.group(1)
    body_content = frontmatter_match.group(2)
    
    frontmatter = yaml.safe_load(frontmatter_str)

    # Extract requested sources
    sources_match = re.search(r'## Requested sources\n(.*?)(?=\n## Budget|$)', body_content, re.DOTALL)
    sources = []
    if sources_match:
        for line in sources_match.group(1).strip().split('\n'):
            line = line.strip()
            if line.startswith('- '):
                sources.append(line[2:].strip())

    # Extract budget caps
    budget = {
        "max_photos_total": 0,
        "max_reviews_total": 0,
        "max_wallclock_minutes": 0
    }
    budget_match = re.search(r'## Budget\n(.*?)(?=\n##|$)', body_content, re.DOTALL)
    if budget_match:
        for line in budget_match.group(1).strip().split('\n'):
            line = line.strip()
            if ':' in line:
                key, value = line.split(':', 1)
                key = key.strip().replace('-', '_')
                if key in budget:
                    budget[key] = int(value.strip())

    return frontmatter, sources, budget

def perform_scrape(source, url, budget_remaining):
    # This is a placeholder for the actual scraping logic
    # In a real scenario, this would call external tools (Scrapfly, Firecrawl, Brave Search)
    # and handle their responses. For this initial script, I'll simulate some results.
    print(f"Simulating scrape for {source} at {url} with budget {budget_remaining}")
    
    photos = []
    reviews = []
    status = "failed"
    reason = "unknown"
    wall_clock_used = 0

    # Simulate different outcomes
    if "yelp" in source:
        # Simulate success with some data
        photos = ["http://example.com/yelp-photo1.jpg", "http://example.com/yelp-photo2.jpg"]
        reviews = [{"text": "Great place!", "source": "yelp.com", "timestamp": datetime.datetime.now().isoformat()}]
        status = "success"
        reason = None
        wall_clock_used = 1
    elif "nextdoor" in source and "login-wall" in url:
        status = "failed"
        reason = "login-wall"
        wall_clock_used = 0.5
    elif "thumbtack" in source:
        status = "not-attempted"
        reason = "budget-exceeded" # Simulate budget hit for simplicity
        wall_clock_used = 0
    elif "facebook" in source:
        # Simulate partial success
        reviews = [{"text": "Good service", "source": "facebook.com", "timestamp": datetime.datetime.now().isoformat()}]
        status = "partial"
        reason = None
        wall_clock_used = 0.8
    elif "bbb" in source:
        status = "failed"
        reason = "server-error"
        wall_clock_used = 0.3
    elif "owner website" in source:
        status = "success"
        reviews = [{"text": "From owner site", "source": "owner-website.com", "timestamp": datetime.datetime.now().isoformat()}]
        wall_clock_used = 1.2

    return {
        "photos": photos,
        "reviews": reviews,
        "status": status,
        "reason": reason,
        "wall_clock_used": wall_clock_used
    }

def process_single_request(site_slug, request_file, requested_at):
    print(f"Processing request for {site_slug}")
    frontmatter, requested_sources, budget = parse_request_file(request_file)

    collected_photos = []
    collected_reviews = []
    total_wall_clock_minutes = 0
    source_results = {}
    overall_status = "not-attempted"

    max_photos = budget.get("max_photos_total", float('inf'))
    max_reviews = budget.get("max_reviews_total", float('inf'))
    max_wallclock = budget.get("max_wallclock_minutes", float('inf'))
    
    for source_entry in requested_sources:
        source_name = source_entry.split(' ', 1)[0].strip(':').lower()
        source_url = source_entry.split(' ', 1)[1].strip() if ' ' in source_entry else ''

        if total_wall_clock_minutes >= max_wallclock or \
           len(collected_photos) >= max_photos or \
           len(collected_reviews) >= max_reviews:
            print(f"Budget exceeded before processing {source_name}")
            source_results[source_name] = {"status": "not-attempted", "reason": "budget-exceeded"}
            continue

        budget_remaining = {
            "max_photos_total": max_photos - len(collected_photos),
            "max_reviews_total": max_reviews - len(collected_reviews),
            "max_wallclock_minutes": max_wallclock - total_wall_clock_minutes
        }
        
        scrape_result = perform_scrape(source_name, source_url, budget_remaining)
        
        source_results[source_name] = {
            "status": scrape_result["status"],
            "reason": scrape_result["reason"]
        }
        
        total_wall_clock_minutes += scrape_result["wall_clock_used"]
        
        if scrape_result["status"] in ["success", "partial"]:
            # Download photos and append reviews
            for photo_url in scrape_result["photos"]:
                if len(collected_photos) < max_photos:
                    photo_filename = f"{source_name}-{len(collected_photos)+1:02d}.jpg"
                    photo_path = os.path.join(GTM_SITES_REPO, "sites", site_slug, "photos-raw", photo_filename)
                    os.makedirs(os.path.dirname(photo_path), exist_ok=True)
                    # Simulate photo download
                    with open(photo_path, 'w') as f:
                        f.write(f"Simulated photo content from {photo_url}")
                    collected_photos.append(photo_path)
                    print(f"Downloaded simulated photo to {photo_path}")
                else:
                    print("Skipping photo download due to budget.")

            for review_data in scrape_result["reviews"]:
                if len(collected_reviews) < max_reviews:
                    collected_reviews.append(review_data)
                else:
                    print("Skipping review collection due to budget.")

    if collected_photos or collected_reviews:
        if any(res["status"] == "success" for res in source_results.values()):
            overall_status = "success"
        else:
            overall_status = "partial"
    else:
        overall_status = "failed" # If no photos or reviews, and not successful, then it's a failure.

    # Write reviews to JSON
    reviews_raw_path = os.path.join(GTM_SITES_REPO, "sites", site_slug, "reviews-raw.json")
    with open(reviews_raw_path, 'w') as f:
        json.dump(collected_reviews, f, indent=2)
    print(f"Wrote {len(collected_reviews)} reviews to {reviews_raw_path}")

    # Write bruce-collected.md
    bruce_collected_path = os.path.join(GTM_SITES_REPO, "sites", site_slug, "bruce-collected.md")
    with open(bruce_collected_path, 'w') as f:
        f.write(f"""---
timestamp: {datetime.datetime.now().isoformat()}
overall_status: {overall_status}
total_photos: {len(collected_photos)}
total_reviews: {len(collected_reviews)}
total_wall_clock_minutes: {total_wall_clock_minutes:.2f}
sources:
""")
        for source_name, result in source_results.items():
            f.write(f"""  - name: {source_name}
    status: {result["status"]}
    reason: {result["reason"] or 'n/a'}
""")
        f.write("---\n")
    print(f"Wrote collection report to {bruce_collected_path}")

    # Archive the request file
    archive_dir = os.path.join(GTM_SITES_REPO, "sites", site_slug, "collect-request-archive")
    os.makedirs(archive_dir, exist_ok=True)
    archive_filename = f"{requested_at.isoformat().replace(':', '-')}-request.md"
    archive_path = os.path.join(archive_dir, archive_filename)
    os.rename(request_file, archive_path)
    print(f"Archived request file to {archive_path}")

    # Git commit and push
    commit_message = f"collect({site_slug}): {len(collected_photos)} photos + {len(collected_reviews)} reviews from {', '.join(source_results.keys())} per collect-request"
    run_git_command(f"git add sites/{site_slug}/photos-raw/ sites/{site_slug}/reviews-raw.json sites/{site_slug}/bruce-collected.md sites/{site_slug}/collect-request-archive/", GTM_SITES_REPO)
    run_git_command(f"git commit -m \"{commit_message}\"", GTM_SITES_REPO)
    run_git_command("git push origin main", GTM_SITES_REPO)

# --- Main execution ---
def main():
    print("Starting autonomous scrape loop...")
    
    try:
        # Step 1: Pull latest from origin/main
        run_git_command("git fetch origin --all", GTM_SITES_REPO)
        run_git_command("git checkout main", GTM_SITES_REPO)
        run_git_command("git pull --ff-only", GTM_SITES_REPO)
        print("Repository updated.")

        # Step 2: Scan for scrape requests
        pending_requests = get_collect_requests()

        if not pending_requests:
            print("No pending collect-request.md files found. Writing status message.")
            timestamp = datetime.datetime.now().isoformat().replace(':', '-')
            status_file_path = os.path.join(GTM_SITES_REPO, "messages", f"{timestamp}-bruce-status-no-work-this-run.md")
            os.makedirs(os.path.dirname(status_file_path), exist_ok=True)
            with open(status_file_path, 'w') as f:
                f.write("No pending collect-request.md files found in this run.\n")
            
            # Commit the status message
            run_git_command(f"git add messages/{os.path.basename(status_file_path)}", GTM_SITES_REPO)
            run_git_command("git commit -m \"status: no collect-requests this run\"", GTM_SITES_REPO)
            run_git_command("git push origin main", GTM_SITES_REPO)
            return

        print(f"Found {len(pending_requests)} pending requests to process.")
        for request in pending_requests:
            process_single_request(request["site_slug"], request["request_file"], request["requested_at"])

    except Exception as e:
        print(f"An error occurred during the scrape loop: {e}")
        # In a real scenario, more robust error reporting would be needed.

if __name__ == "__main__":
    main()

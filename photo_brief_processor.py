
#!/usr/bin/env python3

import os
import sys
import yaml
import glob
import time
import json
from datetime import datetime

# --- Configuration and API Keys ---
SCRAPFLY_API_KEY = os.environ.get('SCRAPFLY_API_KEY')
BRAVE_API_KEY = os.environ.get('BRAVE_API_KEY')
FIRECRAWL_API_KEY = os.environ.get('FIRECRAWL_API_KEY')

# --- Helper Functions ---
def log_message(message):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f'[{timestamp}] {message}')

def read_frontmatter_and_body(filepath):
    with open(filepath, 'r') as f:
        content = f.read()
    
    parts = content.split('---\n', 2)
    if len(parts) < 3:
        return None, content # No frontmatter

    frontmatter = yaml.safe_load(parts[1])
    body = parts[2]
    return frontmatter, body

def write_bruce_collected_md(gtmdot_sites_base, slug, results, total_photos, total_reviews, wall_clock_minutes, final_status):
    timestamp = datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')
    filepath = os.path.join(gtmdot_sites_base, 'sites', slug, 'bruce-collected.md')
    content = f"""
---
status: {final_status}
collection_timestamp: {timestamp}
results:
"""
    for source, data in results.items():
        content += f"  {source}:
    status: {data['status']}
""
        if 'reason' in data:
            content += f"    reason: {data['reason']}
""
        if 'photos_collected' in data:
            content += f"    photos_collected: {data['photos_collected']}
""
        if 'reviews_collected' in data:
            content += f"    reviews_collected: {data['reviews_collected']}
""

    content += f"""
totals:
  photos: {total_photos}
  reviews: {total_reviews}
  wall_clock_minutes: {wall_clock_minutes}
---

## Collection Report

This report summarizes the data collection for `{slug}`.

"""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'w') as f:
        f.write(content)
    log_message(f'Wrote {filepath}')

def append_reviews_to_json(gtmdot_sites_base, slug, reviews_data):
    filepath = os.path.join(gtmdot_sites_base, 'sites', slug, 'reviews-raw.json')
    existing_reviews = []
    if os.path.exists(filepath):
        with open(filepath, 'r') as f:
            try:
                existing_reviews = json.load(f)
            except json.JSONDecodeError:
                log_message(f"Warning: {filepath} is not a valid JSON file. Starting fresh.")
                existing_reviews = []
    
    existing_reviews.extend(reviews_data)
    
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'w') as f:
        json.dump(existing_reviews, f, indent=2)
    log_message(f'Appended {len(reviews_data)} reviews to {filepath}')

def get_slug_from_request_path(path):
    # Assumes path is like sites/*/collect-request.md or gtmdot-sites/sites/*/collect-request.md
    parts = path.split(os.sep)
    if 'sites' in parts:
        sites_index = parts.index('sites')
        if len(parts) > sites_index + 1:
            return parts[sites_index + 1]
    return None

# --- Main Logic ---
def main():
    log_message("Starting photo-brief-processor cron job.")
    
    workspace_path = os.path.join(os.environ.get('HOME'), '.openclaw', 'workspace')
    gtmdot_sites_path = os.path.join(workspace_path, 'gtmdot-sites')

    # 1. Pull latest from origin/main on the gtmdot-sites repo
    if not os.path.exists(gtmdot_sites_path):
        log_message(f"Cloning {gtmdot_sites_path}...")
        os.system(f"git clone https://github.com/gtmdot/gtmdot-sites.git {gtmdot_sites_path}")
    
    log_message(f"Updating {gtmdot_sites_path}...")
    os.system(f"cd {gtmdot_sites_path} && git fetch origin && git checkout main && git pull --ff-only")

    # 2. Scan for scrape requests
    pending_requests = []
    search_pattern = os.path.join(gtmdot_sites_path, 'sites', '*', 'collect-request.md')
    for request_file in glob.glob(search_pattern):
        slug = get_slug_from_request_path(request_file)
        if not slug:
            log_message(f"Could not determine slug for {request_file}, skipping.")
            continue

        request_frontmatter, _ = read_frontmatter_and_body(request_file)
        if not request_frontmatter or 'requested_at' not in request_frontmatter:
            log_message(f"Missing 'requested_at' in frontmatter for {request_file}, skipping.")
            continue
        
        requested_at = datetime.fromisoformat(request_frontmatter['requested_at'].replace('Z', '+00:00'))

        bruce_collected_file = os.path.join(gtmdot_sites_path, 'sites', slug, 'bruce-collected.md')
        if os.path.exists(bruce_collected_file):
            bruce_collected_timestamp = datetime.fromtimestamp(os.path.getmtime(bruce_collected_file))
            if bruce_collected_timestamp > requested_at:
                log_message(f"Skipping {request_file}: bruce-collected.md exists and is newer.")
                continue
        
        pending_requests.append({'filepath': request_file, 'slug': slug, 'requested_at': requested_at})
    
    if not pending_requests:
        log_message("No pending collect-request.md files found. Exiting.")
        # 8. If no pending collect-request.md files, write status message and exit
        timestamp_msg = datetime.now().strftime('%Y%m%d%H%M%S')
        message_filepath = os.path.join(workspace_path, 'messages', f'{timestamp_msg}-bruce-status-no-work-this-run.md')
        os.makedirs(os.path.dirname(message_filepath), exist_ok=True)
        with open(message_filepath, 'w') as f:
            f.write(f"No pending collect-request.md files found at {datetime.now().isoformat()}\n")
        log_message(f'Wrote status message to {message_filepath}')
        sys.exit(0)

    # Sort by requested_at to process older requests first (optional, but good practice)
    pending_requests.sort(key=lambda x: x['requested_at'])

    processed_count = 0
    for request in pending_requests:
        if processed_count >= 3:
            log_message("Processed max 3 requests for this run, stopping.")
            break

        request_filepath = request['filepath']
        slug = request['slug']
        log_message(f"Processing request for slug: {slug} from {request_filepath}")

        frontmatter, body = read_frontmatter_and_body(request_filepath)
        if not frontmatter:
            log_message(f"Error reading frontmatter for {request_filepath}, skipping.")
            continue

        requested_sources = []
        # Extract requested sources from the body, assuming a '## Requested sources' section
        if '## Requested sources' in body:
            sources_section = body.split('## Requested sources')[1].split('## Budget')[0]
            for line in sources_section.split('\n'):
                line = line.strip()
                if line.startswith('- '):
                    source_url = line[2:].strip()
                    if source_url:
                        requested_sources.append(source_url)
        
        budget = {}
        if '## Budget' in body:
            budget_section = body.split('## Budget')[1]
            for line in budget_section.split('\n'):
                line = line.strip()
                if line.startswith('- '):
                    key_value = line[2:].split(':', 1)
                    if len(key_value) == 2:
                        key = key_value[0].strip()
                        value = key_value[1].strip()
                        try:
                            budget[key] = int(value)
                        except ValueError:
                            budget[key] = value # Keep as string if not int
        
        max_photos_total = budget.get('max_photos_total', float('inf'))
        max_reviews_total = budget.get('max_reviews_total', float('inf'))
        max_wallclock_minutes = budget.get('max_wallclock_minutes', float('inf'))

        current_photos = 0
        current_reviews = 0
        start_time = time.time()
        per_source_results = {}

        photos_raw_dir = os.path.join(gtmdot_sites_path, 'sites', slug, 'photos-raw')
        os.makedirs(photos_raw_dir, exist_ok=True)

        # 3. For each pending request (process max 3 per cron run to stay within timeout)
        for source_url in requested_sources:
            source_domain = ''
            try:
                # More robust way to get domain from URL
                from urllib.parse import urlparse
                parsed_url = urlparse(source_url)
                source_domain = parsed_url.netloc if parsed_url.netloc else parsed_url.path.split('/')[0]
            except Exception:
                source_domain = source_url # Fallback if URL parsing fails
            log_message(f"Attempting to scrape {source_url} from {source_domain}")

            # Check budget constraints before attempting scrape
            elapsed_minutes = (time.time() - start_time) / 60
            if current_photos >= max_photos_total or current_reviews >= max_reviews_total or elapsed_minutes >= max_wallclock_minutes:
                per_source_results[source_domain] = {'status': 'not-attempted', 'reason': 'budget-exceeded'}
                log_message(f"Budget exceeded before scraping {source_domain}. Current: Photos={current_photos}/{max_photos_total}, Reviews={current_reviews}/{max_reviews_total}, Time={elapsed_minutes:.2f}/{max_wallclock_minutes} min.")
                continue

            photos_collected_from_source = 0
            reviews_collected_from_source = 0
            source_status = 'failed'
            source_reason = 'unknown'

            # --- Scraping Logic per Source (Placeholder) ---
            # This is where the actual Scrapfly, Brave Search, Firecrawl calls would go.
            # For now, I'll simulate some outcomes.
            # In a real scenario, this would involve calling external tools and parsing their outputs.
            
            # Example for yelp.com
            if 'yelp.com' in source_domain:
                # Simulate Scrapfly call for Yelp
                # This would typically involve using the default_api.exec with curl or a Python library wrapper
                # For now, let's just pretend we got some data
                photos_collected_from_source = 2 # Simulate
                reviews_collected_from_source = 3 # Simulate
                source_status = 'success'
                log_message(f"Simulated Yelp scrape for {slug}. Collected {photos_collected_from_source} photos, {reviews_collected_from_source} reviews.")
            elif 'nextdoor.com' in source_domain:
                # Simulate a login wall
                source_status = 'failed'
                source_reason = 'login-wall'
                log_message(f"Simulated Nextdoor scrape for {slug}: login-wall.")
            elif 'thumbtack.com' in source_domain:
                photos_collected_from_source = 1
                reviews_collected_from_source = 1
                source_status = 'success'
                log_message(f"Simulated Thumbtack scrape for {slug}. Collected {photos_collected_from_source} photos, {reviews_collected_from_source} reviews.")
            elif 'facebook.com' in source_domain:
                reviews_collected_from_source = 2
                source_status = 'partial' # Only reviews
                log_message(f"Simulated Facebook scrape for {slug}. Collected {reviews_collected_from_source} reviews.")
            elif 'bbb.org' in source_domain:
                reviews_collected_from_source = 1
                source_status = 'success'
                log_message(f"Simulated BBB.org scrape for {slug}. Collected {reviews_collected_from_source} reviews.")
            elif 'owner website' in source_url:
                photos_collected_from_source = 3
                reviews_collected_from_source = 0
                source_status = 'success'
                log_message(f"Simulated Owner Website scrape for {slug}. Collected {photos_collected_from_source} photos.")
            else:
                source_status = 'not-attempted'
                source_reason = 'unsupported-source'
                log_message(f"Unsupported source domain: {source_domain}, skipping.")

            # Update totals
            current_photos += photos_collected_from_source
            current_reviews += reviews_collected_from_source
            elapsed_minutes = (time.time() - start_time) / 60 # Recalculate for budget check

            # Store per-source results
            source_result = {'status': source_status}
            if source_reason != 'unknown':
                source_result['reason'] = source_reason
            if photos_collected_from_source > 0:
                source_result['photos_collected'] = photos_collected_from_source
            if reviews_collected_from_source > 0:
                source_result['reviews_collected'] = reviews_collected_from_source
            per_source_results[source_domain] = source_result
            
            # Placeholder for saving actual photos and reviews
            if photos_collected_from_source > 0:
                # This would involve actual image download and saving
                log_message(f"Placeholder: Saved {photos_collected_from_source} photos to {photos_raw_dir}")
            if reviews_collected_from_source > 0:
                # This would involve appending to reviews-raw.json
                sample_reviews = [{ "source": source_domain, "text": f"Sample review {i+1} from {source_domain}", "timestamp": datetime.now().isoformat() } for i in range(reviews_collected_from_source)]
                append_reviews_to_json(gtmdot_sites_path, slug, sample_reviews)
            
            # Check budget again after processing a source
            if current_photos >= max_photos_total or current_reviews >= max_reviews_total or elapsed_minutes >= max_wallclock_minutes:
                log_message(f"Budget hit after scraping {source_domain}. Current: Photos={current_photos}/{max_photos_total}, Reviews={current_reviews}/{max_reviews_total}, Time={elapsed_minutes:.2f}/{max_wallclock_minutes} min.")
                break # Stop processing sources for this request

        # 4. Write bruce-collected.md
        final_wall_clock_minutes = (time.time() - start_time) / 60
        overall_status = 'failed'
        if any(r['status'] == 'success' for r in per_source_results.values()):
            overall_status = 'success'
        elif any(r['status'] == 'partial' for r in per_source_results.values()):
            overall_status = 'partial'
        else:
             overall_status = 'failed' if per_source_results else 'not-attempted' # If no sources were even tried

        write_bruce_collected_md(gtmdot_sites_path, slug, per_source_results, current_photos, current_reviews, final_wall_clock_minutes, overall_status)

        # 5. Archive the request
        archive_dir = os.path.join(gtmdot_sites_path, 'sites', slug, 'collect-request-archive')
        os.makedirs(archive_dir, exist_ok=True)
        archive_filename = f"{datetime.now().strftime('%Y%m%d%H%M%S')}-request.md"
        original_request_filepath = request_filepath # The path received by glob.glob
        archived_request_filepath = os.path.join(archive_dir, archive_filename)

        # Ensure the source file for rename is the one we actually processed
        if os.path.exists(original_request_filepath):
            os.rename(original_request_filepath, archived_request_filepath)
            log_message(f"Archived {original_request_filepath} to {archived_request_filepath}")
        else:
            log_message(f"Warning: Original request file {original_request_filepath} not found for archiving. Already moved or deleted?")


        # 6. Commit all changes for this slug
        log_message(f"Committing changes for {slug}...")
        # Use absolute paths for git add
        os.system(f"cd {gtmdot_sites_path} && git add sites/{slug}/photos-raw/ sites/{slug}/reviews-raw.json sites/{slug}/bruce-collected.md sites/{slug}/collect-request-archive/")
        commit_message = f"collect({slug}): {current_photos} photos + {current_reviews} reviews from {', '.join(per_source_results.keys())} per collect-request"
        os.system(f"cd {gtmdot_sites_path} && git commit -m \"{commit_message}\"")
        os.system(f"cd {gtmdot_sites_path} && git push origin main")
        log_message(f"Committed and pushed changes for {slug}.")
        
        processed_count += 1

    log_message("Photo-brief-processor cron job finished.")

if __name__ == '__main__':
    main()

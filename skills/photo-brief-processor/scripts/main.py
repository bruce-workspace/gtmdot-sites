
import os
import re
import yaml
import datetime
import subprocess
import json
import time
from urllib.parse import urlparse
import requests
from io import BytesIO
from PIL import Image

# Ensure these are available as environment variables or passed in
SCRAPFLY_API_KEY = os.getenv('SCRAPFLY_API_KEY')
BRAVE_API_KEY = os.getenv('BRAVE_API_KEY')
FIRECRAWL_API_KEY = os.getenv('FIRECRAWL_API_KEY')

GTM_SITES_REPO = os.path.expanduser('~/.openclaw/workspace/gtmdot-sites')
MESSAGES_DIR = os.path.expanduser('~/.openclaw/workspace/messages')

MAX_REQUESTS_PER_RUN = 3

def run_command(command, cwd=None):
    try:
        result = subprocess.run(command, cwd=cwd, check=True, shell=True, capture_output=True, text=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Command failed: {command}\\nError: {e.stderr}")
        raise

def sync_repo():
    print(f"Syncing {GTM_SITES_REPO}...")
    run_command("git fetch origin --all", cwd=GTM_SITES_REPO)
    run_command("git checkout main", cwd=GTM_SITES_REPO)
    run_command("git pull --ff-only", cwd=GTM_SITES_REPO)
    print("Repo synced.")

def find_pending_requests():
    pending_requests = []
    sites_dir = os.path.join(GTM_SITES_REPO, 'sites')
    if not os.path.exists(sites_dir):
        return []

    for slug in os.listdir(sites_dir):
        slug_path = os.path.join(sites_dir, slug)
        if not os.path.isdir(slug_path):
            continue

        request_file = os.path.join(slug_path, 'collect-request.md')
        collected_file = os.path.join(slug_path, 'bruce-collected.md')

        if os.path.exists(request_file):
            request_mtime = os.path.getmtime(request_file)
            collected_mtime = 0
            if os.path.exists(collected_file):
                collected_mtime = os.path.getmtime(collected_file)

            if collected_mtime < request_mtime:
                pending_requests.append({
                    'slug': slug,
                    'request_path': request_file,
                    'request_mtime': request_mtime
                })
    return pending_requests

def parse_request_file(request_path):
    with open(request_path, 'r') as f:
        content = f.read()

    parts = content.split('---', 2)
    if len(parts) < 3:
        raise ValueError(f"Invalid YAML frontmatter in {request_path}")

    frontmatter = yaml.safe_load(parts[1])
    body = parts[2]

    requested_sources = []
    budget = {}

    # Parse requested sources from body
    sources_match = re.search(r'## Requested sources\\n(.*?)(?=\\n##|$)', body, re.DOTALL)
    if sources_match:
        for line in sources_match.group(1).split('\\n'):
            line = line.strip()
            if line and not line.startswith('-'):
                source_url_match = re.search(r'(\w+\.\w+):\\s*(https?://\\S+)', line)
                if source_url_match:
                    source_name = source_url_match.group(1)
                    source_url = source_url_match.group(2)
                    requested_sources.append({'name': source_name, 'url': source_url})
            elif line.startswith('-'):
                # Handle bulleted lists if present, though example shows a different format
                pass


    # Parse budget from body
    budget_match = re.search(r'## Budget\\n(.*?)(?=\\n##|$)', body, re.DOTALL)
    if budget_match:
        for line in budget_match.group(1).split('\\n'):
            line = line.strip()
            if ':' in line:
                key, value = line.split(':', 1)
                key = key.strip().replace(' ', '_')
                try:
                    budget[key] = int(value.strip())
                except ValueError:
                    budget[key] = value.strip() # keep as string if not int

    return frontmatter, requested_sources, budget

def download_image(image_url, save_path):
    try:
        response = requests.get(image_url, stream=True, timeout=10)
        response.raise_for_status()
        img = Image.open(BytesIO(response.content))
        img.save(save_path, format='JPEG')
        return True
    except Exception as e:
        print(f"Failed to download image {image_url}: {e}")
        return False

def scrape_yelp(url, slug_path, budget, results):
    print(f"Scraping Yelp: {url}")
    photos_collected = 0
    reviews_collected = 0
    source_status = 'failed'
    reason = 'unknown'

    if photos_collected >= budget.get('max_photos_total', float('inf')) or \\
       reviews_collected >= budget.get('max_reviews_total', float('inf')):
        return 'not-attempted', 'budget-exceeded'

    try:
        # Use Scrapfly to render JS and click through tabs
        # This is a simplified example, actual Scrapfly JS scenario would be more complex
        api_url = "https://api.scrapfly.io/scrape"
        params = {
            "key": SCRAPFLY_API_KEY,
            "url": url,
            "render_js": True,
            "country": "us",
            "proxy_pool": "public_residential_pool",
            # "js_scenario": [...] # This would be a more complex JS scenario to navigate
        }
        response = requests.get(api_url, params=params, timeout=60)
        response.raise_for_status()
        data = response.json()
        html_content = data.get('result', {}).get('content')

        if not html_content:
            reason = 'empty-response'
            return source_status, reason

        # Extract photos
        photo_urls = re.findall(r'<img[^>]*src="([^"]*)"[^>]*alt="([^"]*)"', html_content)
        photo_dir = os.path.join(slug_path, 'photos-raw')
        os.makedirs(photo_dir, exist_ok=True)
        for i, (p_url, alt_text) in enumerate(photo_urls):
            if photos_collected >= budget.get('max_photos_total', float('inf')):
                reason = 'budget-exceeded'
                break
            if 'yelpcdn.com' in p_url: # Filter for actual Yelp photos
                photo_path = os.path.join(photo_dir, f'yelp-{photos_collected + 1:02d}.jpg')
                if download_image(p_url, photo_path):
                    photos_collected += 1
                    print(f"Downloaded Yelp photo: {photo_path}")

        # Extract reviews
        reviews_match = re.findall(r'<p lang="en" class="comment-text[^>]*>(.*?)</p>', html_content, re.DOTALL)
        for review_text in reviews_match:
            if reviews_collected >= budget.get('max_reviews_total', float('inf')):
                reason = 'budget-exceeded'
                break
            results.setdefault('reviews', []).append({
                'source': 'yelp.com',
                'text': review_text.strip(),
                'collected_at': datetime.datetime.now(datetime.timezone.utc).isoformat()
            })
            reviews_collected += 1

        if photos_collected > 0 or reviews_collected > 0:
            source_status = 'success'
        else:
            source_status = 'partial'
            reason = 'no-content-found'

    except requests.exceptions.RequestException as e:
        print(f"Scrapfly request failed for Yelp: {e}")
        if "429" in str(e) or "Too Many Requests" in str(e):
            reason = 'rate-limited'
        elif "5" in str(e.response.status_code):
            reason = 'server-error'
        else:
            reason = 'timeout'
    except Exception as e:
        print(f"An error occurred while scraping Yelp: {e}")
        reason = 'unknown'

    return source_status, reason, photos_collected, reviews_collected

def scrape_nextdoor(url, slug_path, budget, results):
    print(f"Scraping Nextdoor: {url}")
    photos_collected = 0
    reviews_collected = 0
    source_status = 'failed'
    reason = 'unknown'

    if photos_collected >= budget.get('max_photos_total', float('inf')) or \\
       reviews_collected >= budget.get('max_reviews_total', float('inf')):
        return 'not-attempted', 'budget-exceeded'

    try:
        api_url = "https://api.scrapfly.io/scrape"
        params = {
            "key": SCRAPFLY_API_KEY,
            "url": url,
            "render_js": True,
            "country": "us",
            "proxy_pool": "public_residential_pool",
        }
        response = requests.get(api_url, params=params, timeout=60)
        response.raise_for_status()
        data = response.json()
        html_content = data.get('result', {}).get('content')

        if not html_content:
            reason = 'empty-response'
            return source_status, reason

        if "login to nextdoor" in html_content.lower() or "sign up for free" in html_content.lower():
            reason = 'login-wall'
            return 'failed', reason, 0, 0

        # Implement photo and review extraction similar to Yelp
        # Nextdoor structure will be different

        source_status = 'partial' # Assume partial or success for now if no login wall
        reason = 'not-implemented-extraction'


    except requests.exceptions.RequestException as e:
        print(f"Scrapfly request failed for Nextdoor: {e}")
        if "429" in str(e) or "Too Many Requests" in str(e):
            reason = 'rate-limited'
        elif "5" in str(e.response.status_code):
            reason = 'server-error'
        else:
            reason = 'timeout'
    except Exception as e:
        print(f"An error occurred while scraping Nextdoor: {e}")
        reason = 'unknown'

    return source_status, reason, photos_collected, reviews_collected

# Placeholder for other scrape functions
def scrape_thumbtack(url, slug_path, budget, results):
    print(f"Scraping Thumbtack: {url}")
    # ... similar Scrapfly logic ...
    return 'not-attempted', 'not-implemented', 0, 0

def scrape_facebook(url, slug_path, budget, results):
    print(f"Scraping Facebook: {url}")
    # ... Scrapfly then Brave Search fallback ...
    return 'not-attempted', 'not-implemented', 0, 0

def scrape_bbb(url, slug_path, budget, results):
    print(f"Scraping BBB: {url}")
    # ... Firecrawl extract ...
    return 'not-attempted', 'not-implemented', 0, 0

def scrape_owner_website(url, slug_path, budget, results):
    print(f"Scraping Owner Website: {url}")
    # ... Firecrawl scrape + subpages ...
    return 'not-attempted', 'not-implemented', 0, 0

def process_request(pending_request):
    slug = pending_request['slug']
    request_path = pending_request['request_path']
    slug_path = os.path.dirname(request_path)
    bruce_collected_path = os.path.join(slug_path, 'bruce-collected.md')
    reviews_raw_path = os.path.join(slug_path, 'reviews-raw.json')

    print(f"Processing request for slug: {slug}")
    start_time = time.time()
    total_photos = 0
    total_reviews = 0
    collected_status = 'partial'
    source_results = {}
    reviews_data = []

    try:
        frontmatter, requested_sources, budget = parse_request_file(request_path)
    except Exception as e:
        print(f"Error parsing request file {request_path}: {e}")
        # Mark as failed in bruce-collected.md and archive
        # For now, just skip and log
        return

    # Load existing reviews if any
    if os.path.exists(reviews_raw_path):
        with open(reviews_raw_path, 'r') as f:
            try:
                reviews_data = json.load(f)
            except json.JSONDecodeError:
                reviews_data = [] # Corrupted, start fresh

    for source in requested_sources:
        source_name = urlparse(source['url']).netloc.replace('www.', '')
        if source_name.startswith('yelp.com'):
            status, reason, photos, reviews = scrape_yelp(source['url'], slug_path, budget, {'reviews': reviews_data})
        elif source_name.startswith('nextdoor.com'):
            status, reason, photos, reviews = scrape_nextdoor(source['url'], slug_path, budget, {'reviews': reviews_data})
        elif source_name.startswith('thumbtack.com'):
            status, reason, photos, reviews = scrape_thumbtack(source['url'], slug_path, budget, {'reviews': reviews_data})
        elif source_name.startswith('facebook.com'):
            status, reason, photos, reviews = scrape_facebook(source['url'], slug_path, budget, {'reviews': reviews_data})
        elif source_name.startswith('bbb.org'):
            status, reason, photos, reviews = scrape_bbb(source['url'], slug_path, budget, {'reviews': reviews_data})
        elif 'owner_website' in source and source['owner_website']: # Assuming owner_website flag or similar
            status, reason, photos, reviews = scrape_owner_website(source['url'], slug_path, budget, {'reviews': reviews_data})
        else:
            status, reason, photos, reviews = 'not-attempted', 'unsupported-source', 0, 0

        source_results[source_name] = {
            'status': status,
            'reason': reason,
            'photos_collected': photos,
            'reviews_collected': reviews
        }
        total_photos += photos
        total_reviews += reviews

        # Check budget caps after each source
        if total_photos >= budget.get('max_photos_total', float('inf')) or \\
           total_reviews >= budget.get('max_reviews_total', float('inf')) or \\
           (time.time() - start_time) / 60 >= budget.get('max_wallclock_minutes', float('inf')):
            collected_status = 'partial'
            # Any remaining sources should be marked 'budget-exceeded'
            break

    # Determine final status
    if all(res['status'] == 'success' for res in source_results.values()):
        collected_status = 'success'
    elif any(res['status'] == 'success' or res['status'] == 'partial' for res in source_results.values()):
        collected_status = 'partial'
    else:
        collected_status = 'failed'

    # Write reviews-raw.json
    if reviews_data:
        with open(reviews_raw_path, 'w') as f:
            json.dump(reviews_data, f, indent=2)

    # Write bruce-collected.md
    end_time = time.time()
    wall_clock_minutes = (end_time - start_time) / 60
    bruce_collected_content = f"""---\\nstatus: {collected_status}\\ntimestamp: {datetime.datetime.now(datetime.timezone.utc).isoformat()}\\ntotals:\\n  photos_collected: {total_photos}\\n  reviews_collected: {total_reviews}\\n  wall_clock_minutes: {wall_clock_minutes:.2f}\\nsources:\\n"""
    for src_name, res in source_results.items():
        bruce_collected_content += f"""  - name: {src_name}\\n    status: {res['status']}\\n    reason: {res['reason']}\\n    photos_collected: {res['photos_collected']}\\n    reviews_collected: {res['reviews_collected']}\\n"""
    bruce_collected_content += "---\\n"

    with open(bruce_collected_path, 'w') as f:
        f.write(bruce_collected_content)
    print(f"Generated {bruce_collected_path}")

    # Archive collect-request.md
    archive_dir = os.path.join(slug_path, 'collect-request-archive')
    os.makedirs(archive_dir, exist_ok=True)
    timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    archive_path = os.path.join(archive_dir, f'{timestamp}-request.md')
    os.rename(request_path, archive_path)
    print(f"Archived {request_path} to {archive_path}")

    # Commit changes
    commit_message = f"collect({slug}): {total_photos} photos + {total_reviews} reviews from {', '.join(source_results.keys())} per collect-request"
    run_command(f"git add {os.path.join(slug_path, 'photos-raw')} {reviews_raw_path} {bruce_collected_path} {archive_dir}", cwd=GTM_SITES_REPO)
    run_command(f"git commit -m \"{commit_message}\"", cwd=GTM_SITES_REPO)
    run_command("git push origin main", cwd=GTM_SITES_REPO)
    print(f"Committed changes for {slug}")


def main():
    os.makedirs(MESSAGES_DIR, exist_ok=True)

    try:
        sync_repo()
    except Exception as e:
        timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        message_file = os.path.join(MESSAGES_DIR, f'{timestamp}-bruce-status-repo-sync-failed.md')
        with open(message_file, 'w') as f:
            f.write(f"Repo sync failed: {e}")
        print(f"Wrote status message to {message_file}")
        return

    pending_requests = find_pending_requests()
    if not pending_requests:
        timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        message_file = os.path.join(MESSAGES_DIR, f'{timestamp}-bruce-status-no-work-this-run.md')
        with open(message_file, 'w') as f:
            f.write("No pending collect-request.md files found.")
        print(f"Wrote status message to {message_file}")
        return

    # Sort by request_mtime oldest first (FIFO)
    pending_requests.sort(key=lambda x: x['request_mtime'])

    processed_count = 0
    for request in pending_requests:
        if processed_count >= MAX_REQUESTS_PER_RUN:
            print(f"Processed {MAX_REQUESTS_PER_RUN} requests, stopping for this run.")
            break
        try:
            process_request(request)
            processed_count += 1
        except Exception as e:
            print(f"Failed to process request for slug {request['slug']}: {e}")
            # Continue to next request even if one fails

    if processed_count == 0 and pending_requests:
        timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        message_file = os.path.join(MESSAGES_DIR, f'{timestamp}-bruce-status-processing-failed.md')
        with open(message_file, 'w') as f:
            f.write(f"Attempted to process {len(pending_requests)} requests, but none completed successfully due to errors.")
        print(f"Wrote status message to {message_file}")

if __name__ == "__main__":
    main()

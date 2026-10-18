
import os
import re
from datetime import datetime

repo_path = os.path.expanduser("~/.openclaw/workspace/gtmdot-sites")
sites_path = os.path.join(repo_path, "sites")

pending_requests = []

for slug_dir in os.listdir(sites_path):
    slug_path = os.path.join(sites_path, slug_dir)
    if not os.path.isdir(slug_path):
        continue

    request_file = os.path.join(slug_path, "collect-request.md")
    collected_file = os.path.join(slug_path, "bruce-collected.md")

    if os.path.exists(request_file):
        with open(request_file, 'r') as f:
            content = f.read()
            match = re.search(r"requested_at: (.+)", content)
            if match:
                requested_at_str = match.group(1).strip()
                # Handle Z for UTC and ensure timezone awareness
                if requested_at_str.endswith('Z'):
                    requested_at_str = requested_at_str[:-1] + '+00:00'
                try:
                    requested_at = datetime.fromisoformat(requested_at_str)
                except ValueError as e:
                    print(f"Warning: Could not parse requested_at '{requested_at_str}' in {request_file}: {e}")
                    continue
            else:
                print(f"Warning: requested_at not found in {request_file}")
                continue

        if not os.path.exists(collected_file):
            pending_requests.append({'slug': slug_dir, 'request_path': request_file, 'requested_at': requested_at})
        else:
            collected_mtime = datetime.fromtimestamp(os.path.getmtime(collected_file), tz=datetime.now().astimezone().tzinfo)
            if collected_mtime < requested_at:
                pending_requests.append({'slug': slug_dir, 'request_path': request_file, 'requested_at': requested_at})

# Sort by requested_at (oldest first)
pending_requests.sort(key=lambda x: x['requested_at'])

# Process max 3 requests
for i, req in enumerate(pending_requests):
    if i >= 3:
        break
    print(req['request_path'])


import os
import re
import yaml
from datetime import datetime, timezone

def find_pending_requests(repo_path):
    pending_requests = []
    sites_path = os.path.join(repo_path, "sites")
    for root, dirs, files in os.walk(sites_path):
        if "collect-request.md" in files:
            collect_request_path = os.path.join(root, "collect-request.md")
            slug = os.path.basename(root)

            with open(collect_request_path, 'r') as f:
                content = f.read()
                match = re.search(r'---\n(.*?)\n---', content, re.DOTALL)
                if match:
                    frontmatter = yaml.safe_load(match.group(1))
                    requested_at_str = frontmatter.get('requested_at')
                    if requested_at_str:
                        # Ensure requested_at is timezone-aware
                        requested_at = datetime.fromisoformat(requested_at_str.replace('Z', '+00:00'))

                        bruce_collected_path = os.path.join(root, "bruce-collected.md")
                        if os.path.exists(bruce_collected_path):
                            bruce_collected_timestamp = datetime.fromtimestamp(os.path.getmtime(bruce_collected_path), tz=timezone.utc)
                            if bruce_collected_timestamp < requested_at:
                                pending_requests.append({
                                    "slug": slug,
                                    "request_path": collect_request_path,
                                    "requested_at": requested_at
                                })
                        else:
                            pending_requests.append({
                                "slug": slug,
                                "request_path": collect_request_path,
                                "requested_at": requested_at
                            })
    # Sort by requested_at to process older requests first
    pending_requests.sort(key=lambda x: x['requested_at'])
    return pending_requests

if __name__ == "__main__":
    repo_path = os.path.dirname(os.path.abspath(__file__))
    pending = find_pending_requests(repo_path)
    if pending:
        print(f"Found {len(pending)} pending requests:")
        for req in pending:
            print(f"- Slug: {req['slug']}, Requested At: {req['requested_at']}")
    else:
        print("No pending collect-requests found.")


import os
import re
import datetime
import yaml

def find_pending_requests(base_path):
    pending_requests = []
    sites_path = os.path.join(base_path, "sites")
    if not os.path.isdir(sites_path):
        print(f"Error: {sites_path} is not a directory.")
        return []

    for slug in os.listdir(sites_path):
        slug_path = os.path.join(sites_path, slug)
        if not os.path.isdir(slug_path):
            continue

        request_file = os.path.join(slug_path, "collect-request.md")
        if not os.path.exists(request_file):
            continue

        request_timestamp = None
        with open(request_file, 'r') as f:
            content = f.read()
            match = re.search(r'requested_at:\s*(.+)', content)
            if match:
                try:
                    request_timestamp = datetime.datetime.fromisoformat(match.group(1).strip())
                except ValueError:
                    print(f"Warning: Could not parse requested_at timestamp in {request_file}")
                    continue

        if not request_timestamp:
            print(f"Warning: No requested_at timestamp found in {request_file}")
            continue

        collected_file = os.path.join(slug_path, "bruce-collected.md")
        if os.path.exists(collected_file):
            collected_timestamp = datetime.datetime.fromtimestamp(os.path.getmtime(collected_file))
            if collected_timestamp > request_timestamp:
                continue # Skip if already collected after request

        pending_requests.append({
            "slug": slug,
            "request_file": request_file,
            "request_timestamp": request_timestamp
        })
    return pending_requests

if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    base_repo_path = current_dir # Assuming script is at ~/.openclaw/workspace/gtmdot-sites/
    
    # Debugging: Print current working directory
    # print(f"Current working directory: {os.getcwd()}")
    # print(f"Base repository path: {base_repo_path}")

    pending = find_pending_requests(base_repo_path)
    if pending:
        # Sort by request_timestamp to process older requests first
        pending.sort(key=lambda x: x["request_timestamp"])
        for req in pending:
            print(req["slug"])
    else:
        print("No pending requests found.")

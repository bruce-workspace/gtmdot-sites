
import os
import re
from datetime import datetime

def find_pending_requests(base_path):
    pending_requests = []
    sites_path = os.path.join(base_path, "sites")
    
    if not os.path.exists(sites_path):
        print(f"Error: {sites_path} does not exist.")
        return []

    for slug_dir in os.listdir(sites_path):
        slug_path = os.path.join(sites_path, slug_dir)
        if not os.path.isdir(slug_path):
            continue

        request_file = os.path.join(slug_path, "collect-request.md")
        collected_file = os.path.join(slug_path, "bruce-collected.md")

        if os.path.exists(request_file):
            with open(request_file, 'r') as f:
                content = f.read()
            
            # Extract requested_at from YAML frontmatter
            match = re.search(r'requested_at:\s*([^\n]+)', content)
            if match:
                requested_at_str = match.group(1).strip()
                try:
                    requested_at = datetime.fromisoformat(requested_at_str.replace('Z', '+00:00'))
                except ValueError:
                    print(f"Warning: Could not parse requested_at: {requested_at_str} in {request_file}")
                    continue
            else:
                print(f"Warning: requested_at not found in {request_file}")
                continue

            if os.path.exists(collected_file):
                collected_mod_time = datetime.fromtimestamp(os.path.getmtime(collected_file))
                # If bruce-collected.md is older than the request, it's still pending
                if collected_mod_time < requested_at:
                    pending_requests.append(request_file)
            else:
                # If bruce-collected.md doesn't exist, it's pending
                pending_requests.append(request_file)
    
    return pending_requests

if __name__ == "__main__":
    workspace_path = "/Users/bruce/.openclaw/workspace/gtmdot-sites"
    pending = find_pending_requests(workspace_path)
    if pending:
        for req in pending:
            print(req)
    else:
        print("No pending collect-request.md files found.")


import os
import re
import glob
from datetime import datetime

def get_timestamp_from_frontmatter(file_path, key='requested_at'):
    with open(file_path, 'r') as f:
        content = f.read()
    match = re.search(r'%s: (\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z)' % key, content)
    if match:
        return datetime.strptime(match.group(1), '%Y-%m-%dT%H:%M:%SZ')
    return None

def find_pending_requests(base_dir):
    pending_requests = []
    collect_request_files = glob.glob(os.path.join(base_dir, 'sites', '*', 'collect-request.md'))

    for req_file in collect_request_files:
        slug = os.path.basename(os.path.dirname(req_file))
        collected_file = os.path.join(os.path.dirname(req_file), 'bruce-collected.md')

        requested_at = get_timestamp_from_frontmatter(req_file, key='requested_at')
        if not requested_at:
            print(f"Warning: Could not extract 'requested_at' from {req_file}")
            continue

        if os.path.exists(collected_file):
            collected_at = get_timestamp_from_frontmatter(collected_file, key='collected_at')
            if collected_at and collected_at > requested_at:
                continue # Already collected after request, so skip
        
        pending_requests.append(req_file)
    return pending_requests

if __name__ == "__main__":
    # The script is run from ~/.openclaw/workspace, but the gtmdot-sites repo is at ~/.openclaw/workspace/gtmdot-sites
    gtmdot_sites_dir = os.path.join(os.getcwd(), 'gtmdot-sites')
    pending = find_pending_requests(gtmdot_sites_dir)
    for req in pending:
        print(req)

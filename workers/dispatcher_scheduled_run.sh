#!/bin/zsh
set -euo pipefail

REPO="/Users/bruce/.openclaw/workspace/gtmdot-sites"
LOCK_DIR="/private/tmp/gtmdot-dispatcher-bridge.lock"

if ! mkdir "$LOCK_DIR" 2>/dev/null; then
  echo "dispatcher already running; exiting"
  exit 0
fi

cleanup() {
  rmdir "$LOCK_DIR" 2>/dev/null || true
}
trap cleanup EXIT

cd "$REPO"

/usr/bin/python3 "$REPO/workers/paperclip_runtime_health.py" || true
/usr/bin/python3 "$REPO/workers/gtmdot_dispatcher_bridge.py" --dry-run || true
/usr/bin/python3 "$REPO/workers/paperclip_runtime_health.py" || true

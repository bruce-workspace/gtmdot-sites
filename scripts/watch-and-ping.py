#!/usr/bin/env python3
"""
watch-and-ping.py — detect pipeline state transitions and ping Slack.

Reads current state for all active builds via pipeline-status.py --json,
diffs against the last-known state cached on disk, and posts a Slack message
to #claude-sync when meaningful transitions happen.

State transitions worth pinging:
  - collect-request.md FILED        (R1VS just engaged Bruce on a slug)
  - bruce-collected.md APPEARED     (Bruce started delivering)
  - bruce-asset-intel.json APPEARED (Bruce delivered Asset Intelligence)
  - photos-raw count went up        (Bruce dropped scraped photos)
  - photos-generated count went up  (Bruce ran gpt-image-2)
  - photos/ count went up           (Mini integrated — photo placement done)
  - live URL HTTP 200 (was not)     (Mini deployed)
  - Supabase stage changed          (Mini advanced the prospect)

Usage:
  python3 scripts/watch-and-ping.py                    # check all active builds, post on transitions
  python3 scripts/watch-and-ping.py --slug <slug>      # check one slug
  python3 scripts/watch-and-ping.py --dry-run          # detect transitions but don't post
  python3 scripts/watch-and-ping.py --reset            # blow away the cache (forces all current state to "new")

Cache: .cache/pipeline-watcher-state.json (per-machine, .gitignored)
Slack channel: #claude-sync (C0AQTKM8F0A) — hardcoded for now
Tag: <@U071V207BTN> — Jesse's user ID, hardcoded for now

This script does NOT poll continuously. It runs once per invocation. Pair
with /loop or cron to get periodic checks.
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, Any, List, Optional, Tuple

REPO_ROOT = Path(__file__).resolve().parent.parent
CACHE_PATH = REPO_ROOT / ".cache" / "pipeline-watcher-state.json"
SLACK_CHANNEL_ID = "C0AQTKM8F0A"   # #claude-sync
JESSE_USER_ID = "U071V207BTN"


# Slack posts use the slack_send_message MCP tool when called from a Claude
# session, but this script also runs from cron / /loop. For non-Claude
# invocations, we shell out to a JSON-readable Slack webhook OR write the
# message to stdout (and the calling Claude session picks it up).
#
# To keep things simple and not require a separate Slack webhook to be
# provisioned, this script ALWAYS writes intended messages to stdout AND
# to .cache/pending-slack-messages.json. A companion command (or the
# calling Claude session) can flush them to Slack.


def load_cache() -> Dict[str, Dict]:
    if not CACHE_PATH.exists():
        return {}
    try:
        with open(CACHE_PATH) as f:
            return json.load(f)
    except Exception:
        return {}


def save_cache(state: Dict[str, Dict]) -> None:
    CACHE_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(CACHE_PATH, "w") as f:
        json.dump(state, f, indent=2, default=str)


def get_current_state(slug: Optional[str]) -> List[Dict[str, Any]]:
    """Invoke pipeline-status.py --json to get current state."""
    cmd = ["python3", str(REPO_ROOT / "scripts" / "pipeline-status.py"), "--json"]
    if slug:
        cmd.append(slug)
    else:
        cmd.append("--all")
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=30, env=os.environ.copy())
    if result.returncode != 0:
        print(f"ERROR running pipeline-status: {result.stderr}", file=sys.stderr)
        return []
    try:
        data = json.loads(result.stdout)
    except json.JSONDecodeError as e:
        print(f"ERROR parsing pipeline-status JSON: {e}", file=sys.stderr)
        return []
    if isinstance(data, dict):
        return [data]
    return data


def detect_transitions(prev: Dict[str, Any], curr: Dict[str, Any]) -> List[str]:
    """Compare prev/curr state for one slug. Returns human-readable transition strings."""
    transitions = []
    pf = prev.get("files", {})
    cf = curr.get("files", {})

    def gained(key, label, prefix="🟢"):
        if not pf.get(key) and cf.get(key):
            transitions.append(f"{prefix} **{label}**")

    def count_increased(key, label, prefix="📁"):
        before = pf.get(key, 0) or 0
        after = cf.get(key, 0) or 0
        if after > before:
            delta = after - before
            transitions.append(f"{prefix} **{label}** (+{delta} → total {after})")

    # File transitions
    gained("collect_request_open", "collect-request.md filed (R1VS engaged Bruce)", "📨")
    gained("bruce_collected", "bruce-collected.md delivered", "📦")
    gained("bruce_asset_intel_md", "bruce-asset-intel.md delivered (§11.11 Asset Intelligence)", "🤖")
    gained("bruce_asset_intel_json", "bruce-asset-intel.json delivered", "🤖")
    count_increased("photos_raw_count", "Bruce dropped scraped photos", "📸")
    count_increased("photos_generated_count", "Bruce generated images via gpt-image-2", "🎨")
    count_increased("photos_count", "Mini integrated photos into photos/", "🛠️")

    # Live URL transition
    prev_status = prev.get("live_http_status")
    curr_status = curr.get("live_http_status")
    if prev_status != 200 and curr_status == 200:
        transitions.append(f"🚀 **Site went LIVE** — {curr.get('live_url', '?')}")
    elif prev_status == 200 and curr_status not in (200, None):
        transitions.append(f"⚠️ Live URL was 200, now HTTP {curr_status} — {curr.get('live_url', '?')}")

    # Supabase stage transition
    prev_sb = prev.get("supabase") or {}
    curr_sb = curr.get("supabase") or {}
    prev_stage = prev_sb.get("stage")
    curr_stage = curr_sb.get("stage")
    if prev_stage and curr_stage and prev_stage != curr_stage:
        transitions.append(f"📋 Supabase stage: `{prev_stage}` → `{curr_stage}`")

    # Phase transition
    if prev.get("phase") != curr.get("phase"):
        transitions.append(f"🔄 Phase: `{prev.get('phase', '?')}` → `{curr.get('phase', '?')}`")

    return transitions


def build_slack_message(slug: str, transitions: List[str], curr: Dict[str, Any]) -> str:
    """Compose a Slack-flavored message with Jesse tagged."""
    lines = [f"<@{JESSE_USER_ID}> — Pipeline transition on `{slug}`"]
    lines.append("")
    for t in transitions:
        lines.append(f"• {t}")
    lines.append("")
    sb = curr.get("supabase") or {}
    if sb.get("stage"):
        lines.append(f"  Supabase stage: `{sb.get('stage')}`")
    if curr.get("live_http_status") == 200:
        lines.append(f"  Live: {curr.get('live_url')}")
    lines.append(f"  Phase: `{curr.get('phase', '?')}`")
    lines.append("")
    last_commit = curr.get("last_commit") or {}
    if last_commit:
        lines.append(f"  Last commit: `{last_commit.get('sha', '?')}` — {last_commit.get('subject', '')}")
    lines.append(f"  Run `python3 scripts/pipeline-status.py {slug}` for full detail.")
    return "\n".join(lines)


def write_pending_message(slug: str, message: str) -> Path:
    """Append a pending Slack message to disk for a Claude session to flush."""
    pending_dir = REPO_ROOT / ".cache"
    pending_dir.mkdir(parents=True, exist_ok=True)
    pending_path = pending_dir / "pending-slack-messages.json"
    pending = []
    if pending_path.exists():
        try:
            with open(pending_path) as f:
                pending = json.load(f)
        except Exception:
            pending = []
    pending.append({
        "queued_at": datetime.now(timezone.utc).isoformat(),
        "channel_id": SLACK_CHANNEL_ID,
        "slug": slug,
        "message": message,
    })
    with open(pending_path, "w") as f:
        json.dump(pending, f, indent=2)
    return pending_path


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--slug", help="check one slug only")
    ap.add_argument("--dry-run", action="store_true", help="detect transitions but don't queue Slack messages")
    ap.add_argument("--reset", action="store_true", help="reset cache (next run will treat current state as new — no pings)")
    args = ap.parse_args()

    if args.reset:
        if CACHE_PATH.exists():
            CACHE_PATH.unlink()
        # Snapshot current state into cache without pinging
        states = get_current_state(args.slug)
        cache = {s["slug"]: s for s in states}
        save_cache(cache)
        print(f"reset complete — {len(cache)} slug(s) snapshotted, no pings sent")
        sys.exit(0)

    cache = load_cache()
    states = get_current_state(args.slug)

    total_transitions = 0
    for curr in states:
        slug = curr["slug"]
        prev = cache.get(slug, {"files": {}, "phase": "unknown", "live_http_status": None, "supabase": {}})
        transitions = detect_transitions(prev, curr)
        if transitions:
            total_transitions += len(transitions)
            print(f"\n=== {slug} ({len(transitions)} transition{'s' if len(transitions) != 1 else ''}) ===")
            for t in transitions:
                print(f"  {t}")
            if not args.dry_run:
                msg = build_slack_message(slug, transitions, curr)
                pending = write_pending_message(slug, msg)
                print(f"  → queued Slack message at {pending}")
        cache[slug] = curr

    if total_transitions == 0:
        print(f"no transitions detected across {len(states)} slug(s)")

    if not args.dry_run:
        save_cache(cache)


if __name__ == "__main__":
    main()

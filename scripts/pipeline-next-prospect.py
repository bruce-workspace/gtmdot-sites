#!/usr/bin/env python3
"""
pipeline-next-prospect.py — return the next ready_for_review prospect that
doesn't yet have a pass-marker note.

Purpose:
  Replaces the in-prompt DONE list pattern used during overnight /loop runs.
  The loop prompt no longer needs to carry accumulated state — this script
  reads the source of truth (Supabase notes) on every invocation.

Usage:
  pipeline-next-prospect.py --pass-marker "[2026-04-23 OVERNIGHT PASS]"
  pipeline-next-prospect.py \\
    --pass-marker "[2026-04-23 OVERNIGHT PASS]" \\
    --priority-marker "[2026-04-21 PRE-OUTREACH BLOCK]"
  pipeline-next-prospect.py --pass-marker "[...]" --stage needs_approval

Exit codes:
  0  — prospect found. JSON printed to stdout (single line).
  1  — queue drained (no output).
  2  — usage / config error.

Env vars (loaded from ~/.openclaw/.env if present):
  SUPABASE_URL                      default: https://qztjoshdrxionhxeieik.supabase.co
  SUPABASE_SERVICE_ROLE_KEY or SUPABASE_SERVICE_KEY  (required)

Fields returned in the JSON:
  id, slug, business_name, address, city, state, zip,
  existing_website, created_at

Design notes:
  - Two read queries: notes-with-marker (done set) and prospects-in-stage.
    Runtime is O(notes+prospects) so it's fine at current pipeline scale.
  - Priority ordering: prospects with a priority-marker note come first,
    then everything else in created_at order.
  - This script never writes. It only reads.
"""

import argparse
import json
import os
import sys
import urllib.parse
import urllib.request


DEFAULT_SUPABASE_URL = "https://qztjoshdrxionhxeieik.supabase.co"
DEFAULT_FIELDS = (
    "id,slug,business_name,address,city,state,zip,existing_website,created_at"
)


def load_env_file(path: str) -> None:
    """Minimal .env loader — only sets vars that aren't already in env."""
    if not os.path.exists(path):
        return
    with open(path) as fh:
        for raw in fh:
            line = raw.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, _, value = line.partition("=")
            key = key.strip()
            value = value.strip().strip('"').strip("'")
            os.environ.setdefault(key, value)


def env_var(*names: str) -> str | None:
    for name in names:
        v = os.environ.get(name)
        if v:
            return v
    return None


def rest_get(url: str, key: str) -> list[dict]:
    req = urllib.request.Request(
        url,
        headers={
            "apikey": key,
            "Authorization": f"Bearer {key}",
            "Accept": "application/json",
        },
    )
    with urllib.request.urlopen(req, timeout=15) as resp:
        return json.load(resp)


def marker_to_like_pattern(marker: str) -> str:
    """
    Build a PostgREST `like` pattern from the raw marker.

    PostgREST like patterns use `*` as a wildcard (not `%`).
    The marker itself contains literal square brackets, which are fine.
    We URL-encode the whole thing at the caller.
    """
    return f"*{marker}*"


def fetch_prospect_ids_with_marker(
    supabase_url: str, key: str, marker: str
) -> set[str]:
    pattern = marker_to_like_pattern(marker)
    url = (
        f"{supabase_url}/rest/v1/notes"
        f"?select=prospect_id"
        f"&body=like.{urllib.parse.quote(pattern)}"
    )
    rows = rest_get(url, key)
    return {r["prospect_id"] for r in rows if r.get("prospect_id")}


def fetch_prospects_in_stage(
    supabase_url: str, key: str, stage: str, fields: str = DEFAULT_FIELDS
) -> list[dict]:
    url = (
        f"{supabase_url}/rest/v1/prospects"
        f"?select={fields}"
        f"&stage=eq.{urllib.parse.quote(stage)}"
        f"&order=created_at.asc"
    )
    return rest_get(url, key)


def pick_next(
    prospects: list[dict],
    done_ids: set[str],
    priority_ids: set[str],
) -> dict | None:
    undone = [p for p in prospects if p["id"] not in done_ids]
    if not undone:
        return None

    if priority_ids:
        pri = [p for p in undone if p["id"] in priority_ids]
        rest = [p for p in undone if p["id"] not in priority_ids]
        ordered = pri + rest
    else:
        ordered = undone

    return ordered[0]


def main() -> None:
    ap = argparse.ArgumentParser(
        description="Return the next ready_for_review prospect missing a pass-marker note."
    )
    ap.add_argument(
        "--pass-marker",
        required=True,
        help='Required. Example: "[2026-04-23 OVERNIGHT PASS]"',
    )
    ap.add_argument(
        "--priority-marker",
        help='Optional. Prospects with this marker float to the front. '
        'Example: "[2026-04-21 PRE-OUTREACH BLOCK]"',
    )
    ap.add_argument(
        "--stage",
        default="ready_for_review",
        help="Prospect stage to query. Default: ready_for_review",
    )
    ap.add_argument(
        "--fields",
        default=DEFAULT_FIELDS,
        help="Comma-separated prospect fields to return. Default: id,slug,business_name,..."
    )
    args = ap.parse_args()

    load_env_file(os.path.expanduser("~/.openclaw/.env"))
    supabase_url = env_var("SUPABASE_URL") or DEFAULT_SUPABASE_URL
    supabase_key = env_var("SUPABASE_SERVICE_ROLE_KEY", "SUPABASE_SERVICE_KEY")

    if not supabase_key:
        print(
            "error: missing SUPABASE_SERVICE_ROLE_KEY or SUPABASE_SERVICE_KEY",
            file=sys.stderr,
        )
        sys.exit(2)

    try:
        done_ids = fetch_prospect_ids_with_marker(
            supabase_url, supabase_key, args.pass_marker
        )
        priority_ids: set[str] = set()
        if args.priority_marker:
            priority_ids = fetch_prospect_ids_with_marker(
                supabase_url, supabase_key, args.priority_marker
            )
        prospects = fetch_prospects_in_stage(
            supabase_url, supabase_key, args.stage, args.fields
        )
    except urllib.error.HTTPError as e:
        print(f"error: Supabase HTTP {e.code} — {e.reason}", file=sys.stderr)
        sys.exit(2)
    except urllib.error.URLError as e:
        print(f"error: network — {e.reason}", file=sys.stderr)
        sys.exit(2)

    nxt = pick_next(prospects, done_ids, priority_ids)
    if nxt is None:
        sys.exit(1)

    print(json.dumps(nxt, separators=(",", ":")))


if __name__ == "__main__":
    main()

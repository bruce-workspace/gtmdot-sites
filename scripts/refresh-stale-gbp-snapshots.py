#!/usr/bin/env python3
"""
refresh-stale-gbp-snapshots.py — Mini orchestrator for gbp_snapshot staleness.

Scans sites/ for gbp_snapshot.json files, checks `fetched_at` against the
per-snapshot staleness_policy (default 14d soft / 30d hard), and invokes
R1VS's `write-gbp-snapshot.py <slug> --refresh --by mini --scope {soft|hard}`
for any that cross a threshold.

Thin orchestrator. The actual Places API call + schema write + refresh
provenance is all handled by write-gbp-snapshot.py. We just pick which
sites need the nudge.

Usage:
  refresh-stale-gbp-snapshots.py [--dry-run]
  refresh-stale-gbp-snapshots.py --slug <slug>          # just one
  refresh-stale-gbp-snapshots.py --only-stages outreach_sent,outreach_staged
  refresh-stale-gbp-snapshots.py --sites-dir /alternate/path

Exit:
  0  — ran cleanly (may have done zero work)
  1  — at least one refresh invocation failed
  2  — config / usage error

Notes:
  - Soft-stale scope re-fetches 4 fields (rating, review_count_total,
    last_review_date, photo_count_on_gbp). ~1 Places API call per site.
  - Hard-stale scope re-fetches everything. Still ~1 API call.
  - Skipped reasons are reported: no-snapshot, not-stale, no-name-addr.
  - Non-destructive: never touches snapshot files directly — always
    delegates to write-gbp-snapshot.py.
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path


DEFAULT_SITES_DIR = Path("/Users/bruce/.openclaw/workspace/gtmdot-sites/sites")
REPO_ROOT = Path("/Users/bruce/.openclaw/workspace/gtmdot-sites")
WRITE_SCRIPT = REPO_ROOT / "scripts" / "write-gbp-snapshot.py"


def read_snapshot(site_dir: Path) -> dict | None:
    p = site_dir / "gbp_snapshot.json"
    if not p.exists():
        return None
    try:
        return json.loads(p.read_text())
    except (json.JSONDecodeError, OSError):
        return None


def parse_iso(ts: str) -> datetime | None:
    if not ts:
        return None
    try:
        # Accept both "Z" and "+00:00" suffixes
        if ts.endswith("Z"):
            ts = ts[:-1] + "+00:00"
        return datetime.fromisoformat(ts)
    except ValueError:
        return None


def staleness_scope(snapshot: dict, now: datetime) -> str | None:
    """Return 'soft', 'hard', or None (fresh)."""
    fetched = parse_iso(snapshot.get("fetched_at", ""))
    if fetched is None:
        return None  # unparseable — treat as fresh to avoid runaway refresh
    policy = snapshot.get("staleness_policy") or {}
    soft_days = int(policy.get("soft_stale_days", 14))
    hard_days = int(policy.get("hard_stale_days", 30))

    age = now - fetched
    if age >= timedelta(days=hard_days):
        return "hard"
    if age >= timedelta(days=soft_days):
        return "soft"
    return None


def invoke_refresh(slug: str, name: str, address: str, scope: str) -> tuple[bool, str]:
    """Call write-gbp-snapshot.py refresh mode. Returns (ok, output_summary)."""
    cmd = [
        "python3", str(WRITE_SCRIPT),
        slug,
        "--refresh",
        "--by", "mini",
        "--scope", scope,
        "--name", name,
        "--address", address,
    ]
    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=30,
            cwd=str(REPO_ROOT),
        )
    except subprocess.TimeoutExpired:
        return False, "timeout after 30s"
    except OSError as e:
        return False, f"invocation error: {e}"

    ok = result.returncode == 0
    summary = (result.stdout or "") + (result.stderr or "")
    return ok, summary.strip()[:300]


def filter_by_stage(
    slug: str, only_stages: set[str] | None
) -> bool:
    """
    If --only-stages filter is active, return True iff this slug's current
    stage is in the set. Queries Supabase via REST.
    """
    if not only_stages:
        return True
    # Lazy Supabase lookup; safe to skip on error (fallback: process)
    try:
        key = os.environ.get("SUPABASE_SERVICE_ROLE_KEY") or os.environ.get(
            "SUPABASE_SERVICE_KEY"
        )
        if not key:
            return True
        import urllib.parse, urllib.request
        url = (
            "https://qztjoshdrxionhxeieik.supabase.co/rest/v1/prospects"
            f"?select=stage&slug=eq.{urllib.parse.quote(slug)}"
        )
        req = urllib.request.Request(
            url, headers={"apikey": key, "Authorization": f"Bearer {key}"}
        )
        with urllib.request.urlopen(req, timeout=5) as r:
            rows = json.load(r)
        if not rows:
            return False
        return rows[0].get("stage") in only_stages
    except Exception:  # noqa: BLE001
        return True  # don't block on a filter-lookup failure


def load_env_file(path: Path) -> None:
    if not path.exists():
        return
    for line in path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, _, v = line.partition("=")
        os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--slug", help="just process this one slug")
    ap.add_argument(
        "--only-stages",
        help="comma-separated stage filter (requires Supabase lookup); default is all",
    )
    ap.add_argument("--sites-dir", default=str(DEFAULT_SITES_DIR))
    args = ap.parse_args()

    load_env_file(Path.home() / ".openclaw" / ".env")

    sites_dir = Path(args.sites_dir)
    if not sites_dir.exists():
        print(f"error: {sites_dir} not found", file=sys.stderr)
        sys.exit(2)

    if not WRITE_SCRIPT.exists():
        print(f"error: {WRITE_SCRIPT} not found", file=sys.stderr)
        sys.exit(2)

    only_stages: set[str] | None = None
    if args.only_stages:
        only_stages = {s.strip() for s in args.only_stages.split(",") if s.strip()}

    candidates: list[Path]
    if args.slug:
        candidates = [sites_dir / args.slug]
    else:
        candidates = sorted(
            d for d in sites_dir.iterdir()
            if d.is_dir() and not d.name.startswith(".") and d.name != "_shared"
        )

    now = datetime.now(timezone.utc)
    results: dict[str, list] = {
        "refreshed": [],
        "skipped": [],
        "errored": [],
    }
    any_errors = False

    for site_dir in candidates:
        slug = site_dir.name
        snap = read_snapshot(site_dir)
        if snap is None:
            results["skipped"].append({"slug": slug, "reason": "no-snapshot"})
            continue

        if only_stages and not filter_by_stage(slug, only_stages):
            results["skipped"].append({"slug": slug, "reason": "stage-filter"})
            continue

        scope = staleness_scope(snap, now)
        if scope is None:
            results["skipped"].append({"slug": slug, "reason": "fresh"})
            continue

        # Need name + address for refresh invocation
        name = snap.get("business_name")
        address = snap.get("formatted_address")
        if not (name and address):
            results["skipped"].append({"slug": slug, "reason": "no-name-or-address-in-snapshot"})
            continue

        if args.dry_run:
            results["refreshed"].append({
                "slug": slug, "scope": scope, "mode": "dry-run",
                "age_days": (now - parse_iso(snap["fetched_at"])).days,
            })
            continue

        ok, summary = invoke_refresh(slug, name, address, scope)
        if ok:
            results["refreshed"].append({
                "slug": slug, "scope": scope,
                "age_days": (now - parse_iso(snap["fetched_at"])).days,
            })
        else:
            any_errors = True
            results["errored"].append({"slug": slug, "scope": scope, "error": summary})

    print(json.dumps(results, indent=2))
    sys.exit(1 if any_errors else 0)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
pipeline-status.py — one-command "where is everything right now" view for a slug.

Aggregates filesystem presence + git activity + live URL HEAD + Supabase stage
into a single screen. Run anytime you want a snapshot of where a build is in
the pipeline.

Usage:
  python3 scripts/pipeline-status.py <slug>           # detail for one site
  python3 scripts/pipeline-status.py --all            # active builds across the repo
  python3 scripts/pipeline-status.py --json <slug>    # machine-readable for the watcher

What you'll see per slug:
  - Phase progress (Phase 0 legitimacy → 5 verify-build) by file presence
  - Bruce delivery status (collect-request open, bruce-collected, bruce-asset-intel)
  - Mini integration status (photos/ files copied in, deploy commit timestamp)
  - Live URL HEAD check (200 = deployed)
  - Supabase stage (current value + when it was last updated)
  - Last commit touching the slug (who, when, what)
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional, Dict, Any, List

RED = "\033[0;31m"
GREEN = "\033[0;32m"
YELLOW = "\033[1;33m"
BLUE = "\033[0;34m"
CYAN = "\033[0;36m"
DIM = "\033[2m"
NC = "\033[0m"

DEFAULT_SUPABASE_URL = "https://qztjoshdrxionhxeieik.supabase.co"


def env_var(*names):
    for n in names:
        v = os.environ.get(n)
        if v:
            return v
    return None


def file_exists(path: Path) -> bool:
    return path.exists() and path.stat().st_size > 0


def count_files(directory: Path, pattern: str = "*") -> int:
    if not directory.exists():
        return 0
    return sum(1 for _ in directory.glob(pattern))


def last_commit_touching(slug: str, repo_root: Path) -> Optional[Dict[str, str]]:
    """Returns {sha, author, date, subject} for the most recent commit touching this slug."""
    try:
        result = subprocess.run(
            ["git", "log", "-1", "--format=%H|%an|%ai|%s", "--",
             f"sites/{slug}/", f"messages/*{slug}*"],
            cwd=repo_root,
            capture_output=True, text=True, timeout=10
        )
        if result.returncode != 0 or not result.stdout.strip():
            return None
        sha, author, date, subject = result.stdout.strip().split("|", 3)
        return {"sha": sha[:7], "author": author, "date": date, "subject": subject}
    except (subprocess.TimeoutExpired, ValueError):
        return None


def supabase_lookup(slug: str) -> Optional[Dict[str, Any]]:
    """Return (stage, stage_entered_at, claim_code, preview_site_url) or None if not found."""
    sb_key = env_var("SUPABASE_SERVICE_ROLE_KEY", "SUPABASE_SERVICE_KEY")
    sb_url = env_var("SUPABASE_URL") or DEFAULT_SUPABASE_URL
    if not sb_key:
        return None
    fields = "stage,stage_entered_at,claim_code,preview_site_url,disqualified,disqualified_reason"
    url = f"{sb_url}/rest/v1/prospects?select={fields}&slug=eq.{slug}"
    try:
        req = urllib.request.Request(
            url,
            headers={"apikey": sb_key, "Authorization": f"Bearer {sb_key}"},
        )
        with urllib.request.urlopen(req, timeout=5) as resp:
            data = json.loads(resp.read())
        return data[0] if data else None
    except Exception:
        return None


def live_url_check(url: Optional[str]) -> Optional[int]:
    """Return HTTP status code or None on failure."""
    if not url:
        return None
    if not url.startswith("http"):
        url = f"https://{url}"
    try:
        req = urllib.request.Request(url, method="HEAD")
        with urllib.request.urlopen(req, timeout=5) as resp:
            return resp.status
    except Exception:
        return None


def status_for_slug(slug: str, repo_root: Path) -> Dict[str, Any]:
    """Build the full status dict for one slug."""
    site_dir = repo_root / "sites" / slug

    # File presence — phase markers
    files = {
        "legitimacy_check": file_exists(site_dir / "legitimacy-check.json"),
        "gbp_snapshot": file_exists(site_dir / "gbp_snapshot.json"),
        "reviews_json": file_exists(site_dir / "reviews.json"),
        "icon_intent": file_exists(site_dir / "icon-intent.json"),
        "build_state": file_exists(site_dir / "BUILD-STATE.md"),
        "business_data": file_exists(site_dir / "business-data.json"),
        "index_html": file_exists(site_dir / "index.html"),
        "base_css": file_exists(site_dir / "_base.css"),
        "design_md": file_exists(site_dir / "design.md"),
        "collect_request_open": file_exists(site_dir / "collect-request.md"),
        "collect_request_archive_count": count_files(site_dir / "collect-request-archive", "*.md"),
        "bruce_collected": file_exists(site_dir / "bruce-collected.md"),
        "bruce_asset_intel_md": file_exists(site_dir / "bruce-asset-intel.md"),
        "bruce_asset_intel_json": file_exists(site_dir / "bruce-asset-intel.json"),
        "reviews_raw": file_exists(site_dir / "reviews-raw.json"),
        "photos_raw_count": count_files(site_dir / "photos-raw", "*"),
        "photos_generated_count": count_files(site_dir / "photos-generated", "*"),
        "photos_count": count_files(site_dir / "photos", "*"),
        "html_files_count": len([p for p in site_dir.glob("*.html") if p.is_file()]),
    }

    # Phase progress derivation
    phase = "unknown"
    if not site_dir.exists():
        phase = "not_started"
    elif not files["legitimacy_check"]:
        phase = "phase-0-not-run"
    elif not files["gbp_snapshot"]:
        phase = "phase-1-snapshot-pending"
    elif not files["business_data"]:
        phase = "phase-2-business-data-pending"
    elif not files["index_html"]:
        phase = "phase-3-scaffold-pending"
    elif files["index_html"] and not files["bruce_asset_intel_md"]:
        if files["collect_request_open"]:
            phase = "awaiting-bruce"
        else:
            phase = "r1vs-build-complete"
    elif files["bruce_asset_intel_md"] and files["photos_count"] == 0:
        phase = "awaiting-mini-integration"
    elif files["photos_count"] > 0:
        phase = "deployed-or-deploying"

    # Last git commit
    commit = last_commit_touching(slug, repo_root)

    # Supabase
    supabase = supabase_lookup(slug)

    # Live URL check
    live_url = supabase.get("preview_site_url") if supabase else f"https://{slug}.pages.dev"
    http_status = live_url_check(live_url)

    return {
        "slug": slug,
        "phase": phase,
        "files": files,
        "last_commit": commit,
        "supabase": supabase,
        "live_url": live_url,
        "live_http_status": http_status,
    }


def render_status(s: Dict[str, Any]) -> None:
    """Pretty-print a single slug's status to stdout."""
    slug = s["slug"]
    files = s["files"]

    print(f"{BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{NC}")
    print(f"{BLUE}pipeline-status{NC} — {YELLOW}{slug}{NC}")
    print(f"{BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{NC}")

    # Phase line (the headline)
    phase = s["phase"]
    phase_color = {
        "not_started": RED,
        "phase-0-not-run": RED,
        "phase-1-snapshot-pending": RED,
        "phase-2-business-data-pending": YELLOW,
        "phase-3-scaffold-pending": YELLOW,
        "awaiting-bruce": CYAN,
        "r1vs-build-complete": GREEN,
        "awaiting-mini-integration": CYAN,
        "deployed-or-deploying": GREEN,
        "unknown": DIM,
    }.get(phase, DIM)
    print(f"  Phase: {phase_color}{phase}{NC}")
    print()

    # Phase 0-5 R1VS markers
    print(f"  {CYAN}R1VS phases:{NC}")
    print(f"    {check(files['legitimacy_check'])} Phase 0 — legitimacy-check.json")
    print(f"    {check(files['gbp_snapshot'])} Phase 1 — gbp_snapshot.json")
    print(f"    {check(files['reviews_json'])} Phase 1 — reviews.json")
    print(f"    {check(files['icon_intent'])} Phase 1 — icon-intent.json")
    print(f"    {check(files['build_state'])} Phase 1 — BUILD-STATE.md")
    print(f"    {check(files['business_data'])} Phase 2 — business-data.json")
    print(f"    {check(files['index_html'])} Phase 3 — index.html ({files['html_files_count']} HTML files total)")
    print(f"    {check(files['design_md'])} Phase 2 — design.md (Stitch sidecar — optional, when DESIGN.md ships)")
    print()

    # Bruce activity
    print(f"  {CYAN}Bruce activity:{NC}")
    cr_status = "OPEN (Bruce should pick up)" if files["collect_request_open"] else "(no open request)"
    print(f"    collect-request.md: {YELLOW}{cr_status}{NC}")
    print(f"    archived requests: {files['collect_request_archive_count']}")
    print(f"    {check(files['bruce_collected'])} bruce-collected.md")
    print(f"    {check(files['bruce_asset_intel_md'])} bruce-asset-intel.md (§11.11.6)")
    print(f"    {check(files['bruce_asset_intel_json'])} bruce-asset-intel.json (§11.11.7)")
    print(f"    photos-raw/: {files['photos_raw_count']} files")
    print(f"    photos-generated/: {files['photos_generated_count']} files")
    print()

    # Mini activity
    print(f"  {CYAN}Mini activity:{NC}")
    print(f"    photos/ (integrated): {files['photos_count']} files")
    if s["live_http_status"] == 200:
        print(f"    live URL: {GREEN}200 OK{NC} — {s['live_url']}")
    elif s["live_http_status"] is not None:
        print(f"    live URL: {YELLOW}HTTP {s['live_http_status']}{NC} — {s['live_url']}")
    else:
        print(f"    live URL: {DIM}unreachable{NC} — {s['live_url']}")
    print()

    # Supabase
    sb = s.get("supabase")
    if sb:
        print(f"  {CYAN}Supabase:{NC}")
        stage = sb.get("stage", "?")
        stage_at = sb.get("stage_entered_at", "")
        if stage_at:
            stage_at = stage_at[:19].replace("T", " ")
        dq = sb.get("disqualified")
        dq_reason = sb.get("disqualified_reason")
        print(f"    stage: {YELLOW}{stage}{NC} (entered {stage_at})")
        print(f"    claim_code: {sb.get('claim_code', '?')}")
        if dq:
            print(f"    {RED}disqualified: {dq_reason}{NC}")
    else:
        print(f"  {CYAN}Supabase:{NC} {DIM}not reachable (key missing or query failed){NC}")
    print()

    # Last commit
    c = s.get("last_commit")
    if c:
        print(f"  {CYAN}Last commit touching this slug:{NC}")
        print(f"    {c['sha']} by {c['author']} — {c['subject']}")
        print(f"    {DIM}{c['date']}{NC}")
    else:
        print(f"  {CYAN}Last commit:{NC} {DIM}none found{NC}")

    print(f"{BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{NC}")


def check(b: bool) -> str:
    return f"{GREEN}✓{NC}" if b else f"{DIM}·{NC}"


def list_active_builds(repo_root: Path) -> List[str]:
    """Return slugs that look like active R1VS builds (have at least gbp_snapshot.json or business-data.json)."""
    sites_dir = repo_root / "sites"
    if not sites_dir.exists():
        return []
    out = []
    for d in sorted(sites_dir.iterdir()):
        if not d.is_dir() or d.name.startswith("_"):
            continue
        if (d / "gbp_snapshot.json").exists() or (d / "business-data.json").exists():
            out.append(d.name)
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    g = ap.add_mutually_exclusive_group()
    g.add_argument("slug", nargs="?", help="site slug to inspect")
    g.add_argument("--all", action="store_true", help="show all active builds (one-line summary each)")
    ap.add_argument("--json", action="store_true", help="emit JSON instead of pretty-printing (for the watcher)")
    args = ap.parse_args()

    repo_root = Path(__file__).resolve().parent.parent

    if args.all:
        slugs = list_active_builds(repo_root)
        if not slugs:
            print("no active builds detected")
            sys.exit(0)
        if args.json:
            print(json.dumps([status_for_slug(s, repo_root) for s in slugs], indent=2, default=str))
            sys.exit(0)
        print(f"{BLUE}━━ active builds ({len(slugs)}) ━━{NC}")
        for s in slugs:
            st = status_for_slug(s, repo_root)
            phase = st["phase"]
            sb = st.get("supabase") or {}
            stage = sb.get("stage", "?")
            print(f"  {YELLOW}{s:45s}{NC} phase={phase:30s} sb_stage={stage}")
        sys.exit(0)

    if not args.slug:
        ap.print_help()
        sys.exit(2)

    s = status_for_slug(args.slug, repo_root)
    if args.json:
        print(json.dumps(s, indent=2, default=str))
    else:
        render_status(s)


if __name__ == "__main__":
    main()

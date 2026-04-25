#!/usr/bin/env python3
"""
queue-audit.py — comprehensive legitimacy audit across the Supabase queue.

Pulls every pre-DQ prospect from public.prospects (stages: needs_approval,
needs_enrichment, needs_decision), runs the legitimacy-screen rules against
each (using existing snapshots if recent, else fresh Places API lookup),
and writes a recommendation report.

Usage:
  python3 scripts/queue-audit.py
  python3 scripts/queue-audit.py --output reports/queue-audit-YYYY-MM-DD.md

Requires:
  SUPABASE_SERVICE_ROLE_KEY (or SUPABASE_SERVICE_KEY)
  GOOGLE_MAPS_API_KEY
  SUPABASE_URL  (defaults to GTMDot project URL)

Exit codes:
  0 — report written
  1 — Supabase or Places API error
  2 — usage / config error
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Optional, Dict, Any, List

# Same rules as legitimacy-screen.py
MIN_RATING = 4.5
MIN_REVIEWS = 10
DORMANT_MONTHS = 24
FARM_WINDOW_DAYS = 30
FARM_WINDOW_FRACTION = 0.5

DEFAULT_SUPABASE_URL = "https://qztjoshdrxionhxeieik.supabase.co"
PRE_DQ_STAGES = ["needs_approval", "needs_enrichment", "needs_decision"]


def env_var(*names):
    for n in names:
        v = os.environ.get(n)
        if v:
            return v
    return None


def supabase_get(path: str, key: str, base_url: str) -> List[Dict]:
    url = f"{base_url}{path}"
    req = urllib.request.Request(
        url,
        headers={"apikey": key, "Authorization": f"Bearer {key}", "Accept": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=15) as resp:
        return json.loads(resp.read())


def fetch_places(name: str, address_hint: str, api_key: str) -> Optional[Dict[str, Any]]:
    q = urllib.parse.quote(f"{name} {address_hint}")
    find_url = (
        f"https://maps.googleapis.com/maps/api/place/findplacefromtext/json"
        f"?input={q}&inputtype=textquery"
        f"&fields=place_id,formatted_address,name"
        f"&key={api_key}"
    )
    try:
        with urllib.request.urlopen(find_url, timeout=10) as resp:
            find_data = json.loads(resp.read())
    except Exception as e:
        return None

    candidates = find_data.get("candidates") or []
    if not candidates:
        return None

    place_id = candidates[0].get("place_id")
    detail_url = (
        f"https://maps.googleapis.com/maps/api/place/details/json"
        f"?place_id={place_id}"
        f"&fields=rating,user_ratings_total,reviews,name,formatted_address"
        f"&key={api_key}"
    )
    try:
        with urllib.request.urlopen(detail_url, timeout=10) as resp:
            detail = json.loads(resp.read()).get("result") or {}
    except Exception:
        return None

    reviews = detail.get("reviews") or []
    review_dates = []
    for r in reviews:
        ts = r.get("time")
        if ts:
            review_dates.append(datetime.fromtimestamp(ts, tz=timezone.utc).strftime("%Y-%m-%d"))

    return {
        "place_id": place_id,
        "name": detail.get("name") or name,
        "formatted_address": detail.get("formatted_address"),
        "rating": detail.get("rating"),
        "review_count_total": detail.get("user_ratings_total") or 0,
        "reviews_captured": len(reviews),
        "last_review_date": max(review_dates) if review_dates else None,
        "earliest_review_date": min(review_dates) if review_dates else None,
        "review_dates": review_dates,
    }


def assess(prospect: Dict, places_api_key: str) -> Dict[str, Any]:
    """Returns assessment dict for one prospect."""
    slug = prospect.get("slug") or "(unknown)"
    business_name = prospect.get("business_name") or slug.replace("-", " ").title()
    trade = prospect.get("trade_category") or ""

    # Try local snapshot first (if exists + recent)
    repo_root = Path(__file__).resolve().parent.parent
    snap_path = repo_root / "sites" / slug / "gbp_snapshot.json"
    snap_data = None
    snap_age_days = None
    if snap_path.exists():
        try:
            with open(snap_path) as f:
                snap_data = json.load(f)
            fa = snap_data.get("fetched_at")
            if fa:
                snap_dt = datetime.fromisoformat(fa.replace("Z", "+00:00"))
                snap_age_days = (datetime.now(timezone.utc) - snap_dt).days
        except Exception:
            snap_data = None

    # If snapshot is stale (>14d) or missing, hit Places API fresh
    fetched = None
    if not snap_data or (snap_age_days is not None and snap_age_days > 14):
        # Build address hint from prospect record
        addr_parts = []
        if prospect.get("address"):
            addr_parts.append(prospect["address"])
        if prospect.get("city"):
            addr_parts.append(prospect["city"])
        if prospect.get("state"):
            addr_parts.append(prospect["state"])
        if prospect.get("zip"):
            addr_parts.append(prospect["zip"])
        addr_hint = ", ".join(addr_parts) if addr_parts else "Atlanta GA"

        fetched = fetch_places(business_name, addr_hint, places_api_key)
        time.sleep(0.05)  # gentle rate limiting

    # Resolve rating + count from whichever source we have
    if fetched:
        rating = fetched.get("rating")
        total_reviews = fetched.get("review_count_total")
        last_review_date = fetched.get("last_review_date")
        formatted_address = fetched.get("formatted_address")
        data_source = "places_api_fresh"
    elif snap_data:
        rating = snap_data.get("rating")
        total_reviews = snap_data.get("review_count_total")
        last_review_date = snap_data.get("last_review_date")
        formatted_address = snap_data.get("formatted_address")
        data_source = f"gbp_snapshot.json (age: {snap_age_days}d)"
    else:
        rating = None
        total_reviews = None
        last_review_date = None
        formatted_address = None
        data_source = "no data — Places API found no candidate"

    # Apply rules
    reasons = []
    if rating is None:
        reasons.append("no rating available")
    elif rating < MIN_RATING:
        reasons.append(f"rating {rating} < {MIN_RATING} (thin rep)")

    if total_reviews is None:
        if "no data" not in data_source:
            reasons.append("no review count available")
    elif total_reviews < MIN_REVIEWS:
        reasons.append(f"total_reviews {total_reviews} < {MIN_REVIEWS} (insufficient signal)")

    dormant_days = None
    if last_review_date:
        try:
            last_dt = datetime.fromisoformat(last_review_date).replace(tzinfo=timezone.utc)
            dormant_days = (datetime.now(timezone.utc) - last_dt).days
            if dormant_days > DORMANT_MONTHS * 30:
                reasons.append(f"dormant — last review {dormant_days}d old (> {DORMANT_MONTHS}mo threshold)")
        except Exception:
            pass

    # Decision
    if rating is None and total_reviews is None and "no data" in data_source:
        status = "NEEDS_DECISION"
    elif reasons:
        status = "FAIL"
    else:
        status = "PASS"

    return {
        "slug": slug,
        "business_name": business_name,
        "trade_category": trade,
        "stage": prospect.get("stage"),
        "disqualified": prospect.get("disqualified"),
        "claim_code": prospect.get("claim_code"),
        "preview_site_url": prospect.get("preview_site_url"),
        "rating": rating,
        "total_reviews": total_reviews,
        "last_review_date": last_review_date,
        "dormant_days": dormant_days,
        "formatted_address": formatted_address,
        "data_source": data_source,
        "status": status,
        "reasons": reasons,
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    ap.add_argument("--output", default=f"reports/queue-audit-{today}.md")
    ap.add_argument("--stages", nargs="+", default=PRE_DQ_STAGES,
                    help=f"stages to audit (default: {' '.join(PRE_DQ_STAGES)})")
    args = ap.parse_args()

    sb_key = env_var("SUPABASE_SERVICE_ROLE_KEY", "SUPABASE_SERVICE_KEY")
    sb_url = env_var("SUPABASE_URL") or DEFAULT_SUPABASE_URL
    places_key = env_var("GOOGLE_MAPS_API_KEY")

    if not sb_key:
        print("ERROR: SUPABASE_SERVICE_ROLE_KEY not set", file=sys.stderr)
        sys.exit(2)
    if not places_key:
        print("ERROR: GOOGLE_MAPS_API_KEY not set", file=sys.stderr)
        sys.exit(2)

    print(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(f"queue-audit — stages: {', '.join(args.stages)}")
    print(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

    # Pull prospects in scope
    stage_filter = ",".join(f'"{s}"' for s in args.stages)
    fields = ",".join([
        "id", "slug", "business_name", "trade_category", "stage",
        "address", "city", "state", "zip", "disqualified",
        "claim_code", "preview_site_url", "existing_website", "gbp_url",
    ])
    path = f"/rest/v1/prospects?select={fields}&stage=in.({stage_filter})&disqualified=eq.false"
    try:
        prospects = supabase_get(path, sb_key, sb_url)
    except Exception as e:
        print(f"ERROR pulling prospects: {e}", file=sys.stderr)
        sys.exit(1)

    print(f"  pulled {len(prospects)} prospects across {len(args.stages)} stages")
    print()

    results = []
    for p in prospects:
        r = assess(p, places_key)
        rating_str = f"{r['rating']:.1f}" if r['rating'] is not None else "?"
        count_str = str(r['total_reviews']) if r['total_reviews'] is not None else "?"
        stage_short = r["stage"][:18] if r["stage"] else ""
        print(f"  [{r['status']:14s}] [{stage_short:18s}] {r['slug'][:40]:40s}  {rating_str:>4} {count_str:>4}rev")
        results.append(r)

    pass_sites = [r for r in results if r["status"] == "PASS"]
    fail_sites = [r for r in results if r["status"] == "FAIL"]
    needs_sites = [r for r in results if r["status"] == "NEEDS_DECISION"]

    print()
    print(f"  {len(pass_sites)} PASS  •  {len(fail_sites)} FAIL  •  {len(needs_sites)} NEEDS_DECISION")
    print()

    # Build report
    repo_root = Path(__file__).resolve().parent.parent
    out_path = repo_root / args.output
    out_path.parent.mkdir(parents=True, exist_ok=True)

    lines = []
    lines.append(f"# Queue audit — {today}")
    lines.append("")
    lines.append(f"Run: `scripts/queue-audit.py`")
    lines.append(f"Stages audited: `{', '.join(args.stages)}`")
    lines.append(f"Prospects pulled: {len(results)}")
    lines.append(f"Rules: rating >= {MIN_RATING}, reviews >= {MIN_REVIEWS}, dormant > {DORMANT_MONTHS}mo")
    lines.append("")
    lines.append(f"**Summary: {len(pass_sites)} PASS  •  {len(fail_sites)} FAIL  •  {len(needs_sites)} NEEDS_DECISION**")
    lines.append("")

    def render(title, sites):
        lines.append(f"## {title} ({len(sites)})")
        lines.append("")
        if not sites:
            lines.append("_None._")
            lines.append("")
            return
        lines.append("| Slug | Stage | Trade | Rating | Reviews | Last review | Reasons |")
        lines.append("|---|---|---|---|---|---|---|")
        for r in sites:
            rating = f"{r['rating']:.1f}" if r['rating'] is not None else "?"
            count = str(r['total_reviews']) if r['total_reviews'] is not None else "?"
            last = r.get("last_review_date") or "?"
            reasons = "; ".join(r.get("reasons") or []) or "—"
            slug_display = f"`{r['slug']}`"
            lines.append(f"| {slug_display} | {r['stage']} | {r['trade_category']} | {rating} | {count} | {last} | {reasons} |")
        lines.append("")

    render("FAIL — recommend DQ", fail_sites)
    render("NEEDS_DECISION — Places API couldn't disambiguate", needs_sites)
    render("PASS — meets thresholds", pass_sites)

    lines.append("## Recommendations")
    lines.append("")
    lines.append(f"- **{len(fail_sites)} sites flagged FAIL.** Likely candidates for `disqualified: true` + `disqualified_reason` per the reasons listed.")
    lines.append(f"- **{len(needs_sites)} sites NEEDS_DECISION.** Places API couldn't disambiguate by name + location — may be unclaimed GBPs or names too generic. Worth a Jesse manual review or Bruce-driven enrichment.")
    lines.append(f"- **{len(pass_sites)} sites PASS** the legitimacy bar. Continue through the pipeline.")

    with open(out_path, "w") as f:
        f.write("\n".join(lines))

    print(f"  wrote {out_path}")


if __name__ == "__main__":
    main()

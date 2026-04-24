#!/usr/bin/env python3
"""
legitimacy-screen.py — Phase 0 auto-DQ screen for prospects.

Runs BEFORE Phase 1 research. Kills a build cycle up front if the prospect is
a review farm, a dormant business, a rep-too-thin prospect, or a listing that
doesn't actually exist at the claimed address.

Rules (per Mini's finding #1):
  - rating < 4.5                     → DQ (thin rep)
  - total_reviews < 10               → DQ (insufficient signal)
  - >50% reviews in any 30-day window → DQ (probable farm / astroturf)
  - no GBP matches at claimed address → DQ (ghost listing)
  - latest review > 24 months old    → DQ (dormant)
  - vertical in blocklist             → DQ (no local-trade fit)

Inputs (pick ONE source):
  --gbp-json <file>     manually supplied JSON with GBP data (see schema below)
  --places-api <addr>   live lookup via Google Places API (requires
                        GOOGLE_MAPS_API_KEY env var)
  --name <name>         business name (required for places-api + address)

Outputs:
  - sites/<slug>/legitimacy-check.json with {passed, reasons, snapshot_at}
  - exit 0 on pass, 1 on DQ, 2 on error

Schema for --gbp-json input:
  {
    "name": "Business Name",
    "address": "123 Main St, Atlanta, GA 30309",
    "rating": 4.7,
    "total_reviews": 42,
    "reviews": [
      {"date": "2026-03-15", "rating": 5, "text": "..."},
      ...
    ]
  }
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Optional, List, Tuple

# ───── Rules (tunable) ─────
MIN_RATING = 4.5
MIN_REVIEWS = 10
FARM_WINDOW_DAYS = 30
FARM_WINDOW_FRACTION = 0.5  # 50% of reviews inside a rolling 30-day window
DORMANT_MONTHS = 24

VERTICAL_BLOCKLIST = {
    # These are lead-gen / franchise / non-local-owner patterns
    "lead-gen-broker",
    "franchise-unverified",
    "referral-funnel",
}

# ───── Colors ─────
RED = "\033[0;31m"
GREEN = "\033[0;32m"
YELLOW = "\033[1;33m"
BLUE = "\033[0;34m"
NC = "\033[0m"


def log_pass(msg): print(f"  {GREEN}✓{NC} {msg}")
def log_fail(msg): print(f"  {RED}✗{NC} {msg}")
def log_info(msg): print(f"  {BLUE}ℹ{NC} {msg}")
def log_warn(msg): print(f"  {YELLOW}⚠{NC} {msg}")


def check_legitimacy(data: dict, vertical: Optional[str] = None) -> Tuple[bool, List[str]]:
    """
    Returns (passed, reasons).
    'passed' is True iff no DQ rule triggers.
    'reasons' is a list of human-readable strings describing any failures.
    """
    reasons = []

    rating = data.get("rating")
    reviews = data.get("reviews") or []
    total_reviews = data.get("total_reviews") or len(reviews)

    # Rule 1: rating threshold
    if rating is None:
        reasons.append("no rating in data")
    elif rating < MIN_RATING:
        reasons.append(f"rating {rating} < {MIN_RATING} (thin rep)")

    # Rule 2: review count threshold
    if total_reviews < MIN_REVIEWS:
        reasons.append(f"total_reviews {total_reviews} < {MIN_REVIEWS} (insufficient signal)")

    # Rule 3: farm pattern (>50% of reviews in any 30-day window)
    if reviews and total_reviews >= MIN_REVIEWS:
        dated = []
        for r in reviews:
            d = r.get("date")
            if not d:
                continue
            try:
                dt = datetime.fromisoformat(d.replace("Z", "+00:00"))
                if dt.tzinfo is None:
                    dt = dt.replace(tzinfo=timezone.utc)
                dated.append(dt)
            except Exception:
                continue

        if len(dated) >= MIN_REVIEWS:
            dated.sort()
            max_in_window = 0
            window = timedelta(days=FARM_WINDOW_DAYS)
            for i, start in enumerate(dated):
                count = sum(1 for d in dated[i:] if d - start <= window)
                if count > max_in_window:
                    max_in_window = count
            fraction = max_in_window / len(dated)
            if fraction > FARM_WINDOW_FRACTION:
                reasons.append(
                    f"review farm pattern: {max_in_window}/{len(dated)} "
                    f"({fraction:.0%}) in a single 30-day window"
                )

    # Rule 4: GBP at claimed address
    if not data.get("address"):
        reasons.append("no address in data (GBP match not confirmed)")
    elif data.get("gbp_match") is False:
        reasons.append("GBP does not match claimed address (ghost listing)")

    # Rule 5: dormancy
    if reviews:
        latest = None
        for r in reviews:
            d = r.get("date")
            if not d:
                continue
            try:
                dt = datetime.fromisoformat(d.replace("Z", "+00:00"))
                if dt.tzinfo is None:
                    dt = dt.replace(tzinfo=timezone.utc)
                if latest is None or dt > latest:
                    latest = dt
            except Exception:
                continue
        if latest is not None:
            age = datetime.now(timezone.utc) - latest
            if age.days > DORMANT_MONTHS * 30:
                reasons.append(
                    f"latest review is {age.days} days old > {DORMANT_MONTHS}mo threshold (dormant)"
                )

    # Rule 6: vertical blocklist
    if vertical and vertical.lower() in VERTICAL_BLOCKLIST:
        reasons.append(f"vertical '{vertical}' is in blocklist (not a local-trade business)")

    passed = len(reasons) == 0
    return passed, reasons


def fetch_places_api(name: str, address: str) -> Optional[dict]:
    """
    Lookup a business via Google Places API v1 (findplacefromtext) + Place Details.
    Returns a normalized dict in the same shape as --gbp-json expects, or None on error.
    Requires GOOGLE_MAPS_API_KEY env var.
    """
    import urllib.parse
    import urllib.request

    api_key = os.environ.get("GOOGLE_MAPS_API_KEY")
    if not api_key:
        print(f"{RED}ERROR:{NC} GOOGLE_MAPS_API_KEY not set", file=sys.stderr)
        return None

    # Step 1: find place
    q = urllib.parse.quote(f"{name} {address}")
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
        print(f"{RED}ERROR:{NC} find_place failed: {e}", file=sys.stderr)
        return None

    candidates = find_data.get("candidates") or []
    if not candidates:
        return {"name": name, "address": address, "gbp_match": False}

    place = candidates[0]
    place_id = place.get("place_id")
    gbp_address = place.get("formatted_address", "")

    # Rough address match — substring check (first line of supplied address in GBP address)
    supplied_head = address.split(",")[0].strip().lower()
    gbp_match = supplied_head in gbp_address.lower()

    # Step 2: get details (rating, review count, reviews list)
    detail_url = (
        f"https://maps.googleapis.com/maps/api/place/details/json"
        f"?place_id={place_id}"
        f"&fields=rating,user_ratings_total,reviews,name,formatted_address"
        f"&key={api_key}"
    )
    try:
        with urllib.request.urlopen(detail_url, timeout=10) as resp:
            detail_data = json.loads(resp.read()).get("result") or {}
    except Exception as e:
        print(f"{RED}ERROR:{NC} place_details failed: {e}", file=sys.stderr)
        return None

    # Normalize reviews into our expected shape
    normalized_reviews = []
    for r in detail_data.get("reviews") or []:
        ts = r.get("time")  # unix seconds
        date_iso = None
        if ts:
            date_iso = datetime.fromtimestamp(ts, tz=timezone.utc).strftime("%Y-%m-%d")
        normalized_reviews.append({
            "date": date_iso,
            "rating": r.get("rating"),
            "text": r.get("text"),
            "author": r.get("author_name"),
        })

    return {
        "name": detail_data.get("name", name),
        "address": detail_data.get("formatted_address", gbp_address),
        "rating": detail_data.get("rating"),
        "total_reviews": detail_data.get("user_ratings_total", 0),
        "reviews": normalized_reviews,
        "gbp_match": gbp_match,
        "place_id": place_id,
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("slug", help="site slug (e.g., 'sandy-springs-plumber-sewer-septic')")
    ap.add_argument("--gbp-json", help="path to pre-captured GBP data JSON")
    ap.add_argument("--places-api", action="store_true", help="live Places API lookup (requires GOOGLE_MAPS_API_KEY)")
    ap.add_argument("--name", help="business name (required for --places-api)")
    ap.add_argument("--address", help="full address (required for --places-api)")
    ap.add_argument("--vertical", help="vertical tag (for blocklist check)")
    args = ap.parse_args()

    # Resolve slug dir
    repo_root = Path(__file__).resolve().parent.parent
    site_dir = repo_root / "sites" / args.slug
    if not site_dir.exists():
        print(f"{RED}ERROR:{NC} {site_dir} does not exist — create the site folder first", file=sys.stderr)
        sys.exit(2)

    print(f"{BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{NC}")
    print(f"{BLUE}legitimacy-screen.py{NC} — slug: {YELLOW}{args.slug}{NC}")
    print(f"{BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{NC}")

    # Load data
    data = None
    if args.gbp_json:
        with open(args.gbp_json) as f:
            data = json.load(f)
        log_info(f"loaded GBP data from {args.gbp_json}")
    elif args.places_api:
        if not args.name or not args.address:
            print(f"{RED}ERROR:{NC} --places-api requires --name and --address", file=sys.stderr)
            sys.exit(2)
        data = fetch_places_api(args.name, args.address)
        if data is None:
            sys.exit(2)
        log_info(f"fetched live via Places API: {data.get('name')}")
    else:
        print(f"{RED}ERROR:{NC} must supply --gbp-json or --places-api", file=sys.stderr)
        sys.exit(2)

    # Summary
    log_info(f"rating: {data.get('rating')}, reviews captured: {len(data.get('reviews') or [])} of {data.get('total_reviews')} total")
    if data.get("address"):
        log_info(f"address: {data['address']}")
    if data.get("gbp_match") is True:
        log_pass("GBP matches claimed address")
    elif data.get("gbp_match") is False:
        log_fail("GBP does not match claimed address")

    # Run rules
    print()
    passed, reasons = check_legitimacy(data, vertical=args.vertical)

    if passed:
        log_pass("no DQ rules triggered — prospect is legitimate, proceed to Phase 1")
    else:
        for r in reasons:
            log_fail(r)

    # Write artifact
    artifact = {
        "slug": args.slug,
        "passed": passed,
        "reasons": reasons,
        "snapshot_at": datetime.now(timezone.utc).isoformat(),
        "rules_applied": {
            "min_rating": MIN_RATING,
            "min_reviews": MIN_REVIEWS,
            "farm_window_days": FARM_WINDOW_DAYS,
            "farm_window_fraction": FARM_WINDOW_FRACTION,
            "dormant_months": DORMANT_MONTHS,
        },
        "snapshot_data": {
            "name": data.get("name"),
            "address": data.get("address"),
            "rating": data.get("rating"),
            "total_reviews": data.get("total_reviews"),
            "reviews_captured": len(data.get("reviews") or []),
            "gbp_match": data.get("gbp_match"),
            "place_id": data.get("place_id"),
        },
    }
    out_path = site_dir / "legitimacy-check.json"
    with open(out_path, "w") as f:
        json.dump(artifact, f, indent=2)

    print()
    log_info(f"artifact written: {out_path}")
    print(f"{BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{NC}")

    sys.exit(0 if passed else 1)


if __name__ == "__main__":
    main()

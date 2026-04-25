#!/usr/bin/env python3
"""
write-gbp-snapshot.py — write / refresh sites/<slug>/gbp_snapshot.json

Produces the canonical snapshot of Google Business Profile data for a prospect.
The snapshot is the single source of truth for review counts, rating, photo
counts, hours, phone, etc. Downstream:
  - Phase 1 research reads it when building dossier
  - Phase 3 build reads review count to decide review UI rendering mode
  - Pre-push gate audits review count vs rendered UI
  - Master Site Builder QA re-fetches on soft-stale / hard-stale rules

Schema:
  See messages/r1vs/2026-04-23-230000-r1vs-proposal-gbp-snapshot-schema.md
  + Mini's 4 refinements in messages/2026-04-23-2350-mini-to-r1vs-ack-both-proposals.md

Modes:
  Initial write (R1VS, Phase 1):
    python3 scripts/write-gbp-snapshot.py <slug> --places-api \\
      --name "Business Name" --address "123 Main St, Atlanta, GA"

  Refresh (Mini or R1VS, any phase):
    python3 scripts/write-gbp-snapshot.py <slug> --refresh --by mini
    python3 scripts/write-gbp-snapshot.py <slug> --refresh --by mini --scope soft
    python3 scripts/write-gbp-snapshot.py <slug> --refresh --by mini --scope hard

  Derive from legitimacy-check.json (avoids duplicate Places API call when
  legitimacy screen already hit Places):
    python3 scripts/write-gbp-snapshot.py <slug> --from-legitimacy-check

Exit codes:
  0 — snapshot written
  1 — write error / API failure
  2 — usage / config error
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional, Dict, Any, List

# ───── colors ─────
RED = "\033[0;31m"
GREEN = "\033[0;32m"
YELLOW = "\033[1;33m"
BLUE = "\033[0;34m"
NC = "\033[0m"


def log_pass(msg): print(f"  {GREEN}✓{NC} {msg}")
def log_fail(msg): print(f"  {RED}✗{NC} {msg}", file=sys.stderr)
def log_info(msg): print(f"  {BLUE}ℹ{NC} {msg}")
def log_warn(msg): print(f"  {YELLOW}⚠{NC} {msg}")


# ───── schema defaults ─────
DEFAULT_STALENESS = {
    "soft_stale_days": 14,
    "hard_stale_days": 30,
}

# Soft-stale scope per Mini ACK: re-fetch these fields at QA time if >14d old.
SOFT_STALE_FIELDS = {
    "rating",
    "review_count_total",
    "last_review_date",
    "photo_count_on_gbp",
}

# Hard-stale scope: re-fetch everything (>30d old).
HARD_STALE_FIELDS = None  # sentinel: means "all"

REFRESH_LOG_MAX = 5  # Mini's rotating cap


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def format_phone_e164(raw: Optional[str]) -> Optional[str]:
    """Normalize a Places API phone string to E.164 format (+14045551234)."""
    if not raw:
        return None
    # Strip everything but digits and a leading +
    s = raw.strip()
    if s.startswith("+"):
        digits = "+" + "".join(c for c in s[1:] if c.isdigit())
    else:
        digits = "".join(c for c in s if c.isdigit())
        # Assume US if 10-digit
        if len(digits) == 10:
            digits = "+1" + digits
        elif len(digits) == 11 and digits.startswith("1"):
            digits = "+" + digits
        else:
            digits = "+" + digits
    return digits


def format_phone_display(e164: Optional[str]) -> Optional[str]:
    """Render E.164 into (AAA) BBB-CCCC US format if possible."""
    if not e164 or not e164.startswith("+1") or len(e164) != 12:
        return e164
    d = e164[2:]  # strip "+1"
    return f"({d[0:3]}) {d[3:6]}-{d[6:10]}"


def parse_hours_weekday_text(weekday_text: List[str]) -> List[Dict[str, str]]:
    """
    Convert Places API 'weekday_text' strings (e.g., "Monday: 8:00 AM - 6:00 PM")
    into structured {dayOfWeek, opens, closes} 24h format.
    Places also provides 'periods' which is more reliable, but this is a fallback.
    """
    day_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    out = []
    for line in weekday_text or []:
        # line looks like "Monday: 8:00 AM – 6:00 PM" or "Monday: Closed"
        try:
            day, rest = line.split(":", 1)
            day = day.strip()
            rest = rest.strip()
            if "closed" in rest.lower():
                out.append({"dayOfWeek": day, "opens": None, "closes": None, "closed": True})
                continue
            # "8:00 AM – 6:00 PM" (U+2013 dash)
            parts = rest.replace("\u2013", "-").split("-")
            if len(parts) != 2:
                continue
            opens = _parse_12h(parts[0].strip())
            closes = _parse_12h(parts[1].strip())
            out.append({"dayOfWeek": day, "opens": opens, "closes": closes})
        except Exception:
            continue
    return out


def parse_hours_periods(periods: List[Dict]) -> List[Dict[str, str]]:
    """Places API 'periods' array — preferred source, always 24h structured.

    Special case: when Places API returns a single period with open.day=0,
    open.time='0000', and no close field, the business is 24/7. We expand
    that single entry into all 7 days as 'open all day'. Without this fix
    the snapshot showed only Sunday for 24/7 businesses (item 7).
    """
    day_names = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

    # Detect the 24/7 special case
    if (
        len(periods or []) == 1
        and (periods[0].get("open") or {}).get("day") == 0
        and (periods[0].get("open") or {}).get("time") == "0000"
        and not periods[0].get("close")
    ):
        return [
            {"dayOfWeek": d, "opens": "00:00", "closes": "23:59", "open_24h": True}
            for d in day_names
        ]

    out = []
    for p in periods or []:
        o = p.get("open") or {}
        c = p.get("close") or {}
        day_idx = o.get("day")
        if day_idx is None:
            continue
        day_name = day_names[day_idx % 7]
        open_time = o.get("time", "0000")
        close_time = c.get("time") if c else None
        opens_fmt = f"{open_time[:2]}:{open_time[2:]}" if len(open_time) == 4 else None
        closes_fmt = f"{close_time[:2]}:{close_time[2:]}" if close_time and len(close_time) == 4 else None
        out.append({"dayOfWeek": day_name, "opens": opens_fmt, "closes": closes_fmt})
    return out


def _parse_12h(s: str) -> Optional[str]:
    """Convert '8:00 AM' -> '08:00'. Returns None on failure."""
    try:
        s = s.strip().upper()
        ampm = "AM" if "AM" in s else ("PM" if "PM" in s else None)
        core = s.replace("AM", "").replace("PM", "").strip()
        if ":" in core:
            h, m = core.split(":")
        else:
            h, m = core, "00"
        h = int(h)
        m = int(m)
        if ampm == "PM" and h != 12:
            h += 12
        elif ampm == "AM" and h == 12:
            h = 0
        return f"{h:02d}:{m:02d}"
    except Exception:
        return None


def fetch_places_api(name: str, address: str) -> Dict[str, Any]:
    """
    Lookup a business via Google Places API (findplacefromtext + details).
    Returns a dict with all fields the schema needs.
    """
    api_key = os.environ.get("GOOGLE_MAPS_API_KEY")
    if not api_key:
        raise RuntimeError("GOOGLE_MAPS_API_KEY not set in environment")

    # Step 1: find place
    q = urllib.parse.quote(f"{name} {address}")
    find_url = (
        f"https://maps.googleapis.com/maps/api/place/findplacefromtext/json"
        f"?input={q}&inputtype=textquery"
        f"&fields=place_id,formatted_address,name"
        f"&key={api_key}"
    )
    with urllib.request.urlopen(find_url, timeout=10) as resp:
        find_data = json.loads(resp.read())

    candidates = find_data.get("candidates") or []
    if not candidates:
        raise RuntimeError(f"No Places candidates found for '{name}' at '{address}'")

    place = candidates[0]
    place_id = place.get("place_id")
    gbp_address = place.get("formatted_address", "")
    supplied_head = address.split(",")[0].strip().lower()
    gbp_match = supplied_head in gbp_address.lower()

    # Step 2: get details
    fields = ",".join([
        "name", "formatted_address", "rating", "user_ratings_total", "reviews",
        "formatted_phone_number", "international_phone_number",
        "opening_hours", "current_opening_hours", "website", "types", "photos",
        "place_id", "url",
    ])
    detail_url = (
        f"https://maps.googleapis.com/maps/api/place/details/json"
        f"?place_id={place_id}&fields={fields}&key={api_key}"
    )
    with urllib.request.urlopen(detail_url, timeout=10) as resp:
        detail = json.loads(resp.read()).get("result") or {}

    # Normalize reviews
    reviews = detail.get("reviews") or []
    review_dates = []
    for r in reviews:
        ts = r.get("time")
        if ts:
            review_dates.append(datetime.fromtimestamp(ts, tz=timezone.utc).strftime("%Y-%m-%d"))

    last_review_date = max(review_dates) if review_dates else None
    earliest_review_date = min(review_dates) if review_dates else None

    # Phone
    intl = detail.get("international_phone_number")
    formatted = detail.get("formatted_phone_number")
    primary_phone = format_phone_e164(intl or formatted)
    primary_phone_formatted = formatted or format_phone_display(primary_phone)

    # Hours
    oh = detail.get("opening_hours") or detail.get("current_opening_hours") or {}
    weekday_text = oh.get("weekday_text") or []
    periods = oh.get("periods") or []
    hours_summary = "; ".join(weekday_text) if weekday_text else None
    hours_structured = parse_hours_periods(periods) if periods else parse_hours_weekday_text(weekday_text)

    # Photos count
    photo_count = len(detail.get("photos") or [])

    # Normalize verbatim review bodies for downstream reviews.json writer.
    # Keep raw text + author + rating + date so the homepage can render real reviews.
    normalized_reviews: List[Dict[str, Any]] = []
    for r in reviews:
        ts = r.get("time")
        date_iso = None
        if ts:
            date_iso = datetime.fromtimestamp(ts, tz=timezone.utc).strftime("%Y-%m-%d")
        normalized_reviews.append({
            "author": r.get("author_name"),
            "rating": r.get("rating"),
            "date": date_iso,
            "source": "google",
            "text": r.get("text"),
            "verified": True,
            "language": r.get("language"),
            "relative_time_description": r.get("relative_time_description"),
            "profile_photo_url": r.get("profile_photo_url"),
        })

    return {
        "place_id": place_id,
        "business_name": detail.get("name") or name,
        "formatted_address": detail.get("formatted_address") or gbp_address,
        "rating": detail.get("rating"),
        "review_count_total": detail.get("user_ratings_total") or 0,
        "reviews_captured": len(reviews),
        "last_review_date": last_review_date,
        "earliest_review_date": earliest_review_date,
        "photo_count_on_gbp": photo_count,
        "primary_phone": primary_phone,
        "primary_phone_formatted": primary_phone_formatted,
        "hours_summary": hours_summary,
        "hours_structured": hours_structured,
        "website_url": detail.get("website"),
        "categories": detail.get("types") or [],
        "gbp_match_verified": gbp_match,
        "gbp_url": detail.get("url"),
        # Verbatim bodies for the reviews.json companion artifact (NOT in
        # gbp_snapshot.json — that file stores metadata only).
        "_normalized_reviews": normalized_reviews,
    }


def write_reviews_json(slug: str, fetched: Dict[str, Any], site_dir: Path, source: str) -> Optional[Path]:
    """
    Write sites/<slug>/reviews.json companion artifact with verbatim review
    bodies. Called automatically when --places-api fetched real reviews.

    Returns the path written, or None if no reviews to write.
    """
    raw = fetched.get("_normalized_reviews") or []
    if not raw:
        return None

    out = {
        "slug": slug,
        "captured": len(raw),
        "total_reviews": fetched.get("review_count_total"),
        "overall_rating": fetched.get("rating"),
        "captured_at": now_iso(),
        "sources": [
            {"source": source, "count": len(raw), "fetched_at": now_iso()}
        ],
        "reviews": raw,
    }
    path = site_dir / "reviews.json"
    with open(path, "w") as f:
        json.dump(out, f, indent=2)
    return path


def build_snapshot(slug: str, fetched: Dict[str, Any], source: str = "google_places_api_v1") -> Dict[str, Any]:
    """Wrap fetched Places data in the full schema with provenance + staleness defaults.
    Strips _normalized_reviews — that field is for the reviews.json writer only."""
    now = now_iso()
    return {
        "slug": slug,
        "fetched_at": now,
        "original_fetched_at": now,
        "source": source,
        "refresh_count": 0,
        "refresh_log": [],
        "place_id": fetched.get("place_id"),
        "business_name": fetched.get("business_name"),
        "formatted_address": fetched.get("formatted_address"),
        "rating": fetched.get("rating"),
        "review_count_total": fetched.get("review_count_total"),
        "reviews_captured": fetched.get("reviews_captured", 0),
        "reviews_captured_sources": [
            {
                "source": source,
                "count": fetched.get("reviews_captured", 0),
                "fetched_at": now,
            }
        ] if fetched.get("reviews_captured", 0) > 0 else [],
        "last_review_date": fetched.get("last_review_date"),
        "earliest_review_date": fetched.get("earliest_review_date"),
        "photo_count_on_gbp": fetched.get("photo_count_on_gbp", 0),
        "primary_phone": fetched.get("primary_phone"),
        "primary_phone_formatted": fetched.get("primary_phone_formatted"),
        "hours_summary": fetched.get("hours_summary"),
        "hours_structured": fetched.get("hours_structured") or [],
        "website_url": fetched.get("website_url"),
        "categories": fetched.get("categories") or [],
        "gbp_match_verified": fetched.get("gbp_match_verified", False),
        "gbp_url": fetched.get("gbp_url"),
        "staleness_policy": DEFAULT_STALENESS,
    }


def refresh_snapshot(existing: Dict[str, Any], fetched: Dict[str, Any], by: str, scope: str) -> Dict[str, Any]:
    """
    Merge refreshed data into existing snapshot preserving provenance fields.
    scope: 'soft' (subset of fields) or 'hard' (all fields)
    by: 'mini' | 'r1vs' | 'bruce' | 'jesse'
    """
    changed: List[str] = []
    merged = dict(existing)

    fields_to_refresh = SOFT_STALE_FIELDS if scope == "soft" else None

    for k, v in fetched.items():
        if fields_to_refresh is not None and k not in fields_to_refresh:
            continue
        if existing.get(k) != v:
            changed.append(k)
            merged[k] = v

    # Update provenance
    merged["fetched_at"] = now_iso()
    merged["refresh_count"] = (existing.get("refresh_count") or 0) + 1

    log_entry = {
        "at": now_iso(),
        "by": by,
        "scope": scope,
        "changed": changed,
    }
    log = list(existing.get("refresh_log") or [])
    log.append(log_entry)
    if len(log) > REFRESH_LOG_MAX:
        log = log[-REFRESH_LOG_MAX:]
    merged["refresh_log"] = log

    # Preserve original_fetched_at
    merged["original_fetched_at"] = existing.get("original_fetched_at") or existing.get("fetched_at") or now_iso()

    return merged


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("slug", help="site slug")
    mode = ap.add_mutually_exclusive_group()
    mode.add_argument("--places-api", action="store_true", help="live Places API lookup (initial write)")
    mode.add_argument("--refresh", action="store_true", help="re-fetch and merge with existing snapshot")
    mode.add_argument("--from-legitimacy-check", action="store_true",
                      help="derive initial snapshot from existing legitimacy-check.json (avoids duplicate API call)")

    ap.add_argument("--name", help="business name (required for --places-api and --refresh)")
    ap.add_argument("--address", help="full address (required for --places-api and --refresh)")
    ap.add_argument("--by", default="r1vs", choices=["r1vs", "mini", "bruce", "jesse"],
                    help="who's performing the write (for refresh provenance)")
    ap.add_argument("--scope", default="hard", choices=["soft", "hard"],
                    help="refresh scope: soft = 4 staleness fields; hard = all")
    ap.add_argument("--source", default="google_places_api_v1",
                    help="source id for captured reviews (used in reviews_captured_sources)")
    ap.add_argument("--no-write-reviews-json", action="store_true",
                    help="skip writing the companion reviews.json (default: write it whenever Places returns review bodies)")
    args = ap.parse_args()

    if not any([args.places_api, args.refresh, args.from_legitimacy_check]):
        log_fail("must supply one of: --places-api, --refresh, --from-legitimacy-check")
        sys.exit(2)

    repo_root = Path(__file__).resolve().parent.parent
    site_dir = repo_root / "sites" / args.slug
    if not site_dir.exists():
        log_fail(f"{site_dir} does not exist — create the site folder first")
        sys.exit(2)

    snapshot_path = site_dir / "gbp_snapshot.json"

    print(f"{BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{NC}")
    print(f"{BLUE}write-gbp-snapshot.py{NC} — slug: {YELLOW}{args.slug}{NC}")
    mode_name = "places-api" if args.places_api else ("refresh" if args.refresh else "from-legitimacy-check")
    print(f"  mode: {YELLOW}{mode_name}{NC}")
    print(f"{BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{NC}")

    if args.places_api:
        if not args.name or not args.address:
            log_fail("--places-api requires --name and --address")
            sys.exit(2)
        if snapshot_path.exists():
            log_warn(f"{snapshot_path} already exists — overwriting. Use --refresh to preserve provenance.")
        try:
            fetched = fetch_places_api(args.name, args.address)
        except Exception as e:
            log_fail(f"Places API fetch failed: {e}")
            sys.exit(1)
        snapshot = build_snapshot(args.slug, fetched, source=args.source)
        log_pass(f"fetched live — rating {snapshot.get('rating')}, {snapshot.get('review_count_total')} total reviews, {snapshot.get('reviews_captured')} captured, {snapshot.get('photo_count_on_gbp')} photos on GBP")
        if not snapshot.get("gbp_match_verified"):
            log_warn("GBP address does NOT match supplied address (ghost listing signal)")

    elif args.refresh:
        if not snapshot_path.exists():
            log_fail(f"{snapshot_path} does not exist — use --places-api for initial write")
            sys.exit(2)
        with open(snapshot_path) as f:
            existing = json.load(f)
        if not args.name or not args.address:
            args.name = args.name or existing.get("business_name")
            args.address = args.address or existing.get("formatted_address")
        if not args.name or not args.address:
            log_fail("could not derive --name / --address from existing snapshot; supply explicitly")
            sys.exit(2)
        try:
            fetched = fetch_places_api(args.name, args.address)
        except Exception as e:
            log_fail(f"Places API refresh failed: {e}")
            sys.exit(1)
        snapshot = refresh_snapshot(existing, fetched, by=args.by, scope=args.scope)
        changed = snapshot["refresh_log"][-1]["changed"]
        if changed:
            log_pass(f"refreshed — {len(changed)} field(s) changed: {', '.join(changed[:8])}{'...' if len(changed) > 8 else ''}")
        else:
            log_info("refresh completed — no field values changed (snapshot remains current)")

    elif args.from_legitimacy_check:
        legit_path = site_dir / "legitimacy-check.json"
        if not legit_path.exists():
            log_fail(f"{legit_path} does not exist — run legitimacy-screen.py first")
            sys.exit(2)
        with open(legit_path) as f:
            legit = json.load(f)
        snap_data = legit.get("snapshot_data") or {}
        # legitimacy-check.json uses a simpler shape; map to fields we need
        fetched = {
            "place_id": snap_data.get("place_id"),
            "business_name": snap_data.get("name"),
            "formatted_address": snap_data.get("address"),
            "rating": snap_data.get("rating"),
            "review_count_total": snap_data.get("total_reviews"),
            "reviews_captured": snap_data.get("reviews_captured", 0),
            "photo_count_on_gbp": 0,
            "gbp_match_verified": snap_data.get("gbp_match", False),
            # Fields not in legitimacy-check — leave null; refresh later
            "last_review_date": None,
            "earliest_review_date": None,
            "primary_phone": None,
            "primary_phone_formatted": None,
            "hours_summary": None,
            "hours_structured": [],
            "website_url": None,
            "categories": [],
            "gbp_url": None,
        }
        snapshot = build_snapshot(args.slug, fetched, source="derived_from_legitimacy_check")
        log_pass("derived initial snapshot from legitimacy-check.json (some fields null — refresh to populate)")

    # Write the snapshot
    with open(snapshot_path, "w") as f:
        json.dump(snapshot, f, indent=2)
    log_info(f"wrote {snapshot_path}")

    # Companion: write reviews.json with verbatim bodies if Places returned them
    # and the user didn't opt out. Skipped for --from-legitimacy-check since that
    # path doesn't have review bodies to write.
    if not args.no_write_reviews_json and (args.places_api or args.refresh):
        # 'fetched' is in scope from above (places-api / refresh branches)
        try:
            written = write_reviews_json(args.slug, fetched, site_dir, source=args.source)
            if written:
                count = len(fetched.get("_normalized_reviews") or [])
                log_pass(f"wrote {written} ({count} verbatim review{'s' if count != 1 else ''})")
            else:
                log_info("no review bodies returned by Places API — reviews.json not written")
        except Exception as e:
            log_warn(f"reviews.json write failed (snapshot still saved): {e}")

    print(f"{BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{NC}")
    sys.exit(0)


if __name__ == "__main__":
    main()

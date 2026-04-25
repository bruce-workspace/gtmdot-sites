#!/usr/bin/env python3
"""
reviews-merge.py — merge Bruce's scraped reviews-raw.json into the canonical
sites/<slug>/reviews.json, deduping and ranking by source priority.

The bridge between Bruce's scrape output and the homepage. Without this,
when Bruce returns with 12 Yelp reviews on top of 5 Google reviews, someone
has to hand-merge — error-prone, inconsistent, often skipped.

What it does:
  1. Reads sites/<slug>/reviews.json (existing) and sites/<slug>/reviews-raw.json
     (Bruce's output). Either or both can be missing.
  2. Normalizes each review to the canonical shape:
       {author, rating, date, source, text, verified, ...}
  3. Dedupes across sources by (lowercased author, first 60 chars of text).
     When dups are found, keeps the higher-priority source.
  4. Ranks by source priority (google > yelp > nextdoor > thumbtack > bbb >
     facebook > other), then by date desc.
  5. Writes unified sites/<slug>/reviews.json with sources[] tracking what
     each source contributed (per Mini's gbp_snapshot schema refinement #1).
  6. Writes sites/<slug>/reviews-merge-log.json with audit trail of what was
     kept, dropped, dedup-merged.

Usage:
  python3 scripts/reviews-merge.py <slug>
  python3 scripts/reviews-merge.py <slug> --dry-run    # show diff, don't write

Exit codes:
  0 — merge completed (or dry-run shown)
  1 — error reading inputs
  2 — usage error
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple

RED = "\033[0;31m"
GREEN = "\033[0;32m"
YELLOW = "\033[1;33m"
BLUE = "\033[0;34m"
NC = "\033[0m"


def log_pass(m): print(f"  {GREEN}✓{NC} {m}")
def log_fail(m): print(f"  {RED}✗{NC} {m}", file=sys.stderr)
def log_info(m): print(f"  {BLUE}ℹ{NC} {m}")
def log_warn(m): print(f"  {YELLOW}⚠{NC} {m}")


# Source priority — higher index = lower priority. When two reviews dedup-collide,
# the lower-index source wins.
SOURCE_PRIORITY = {
    "google": 0,
    "google_places_api_v1": 0,
    "yelp": 1,
    "nextdoor": 2,
    "thumbtack": 3,
    "bbb": 4,
    "facebook": 5,
    "angi": 6,
    "homeadvisor": 6,
    "thumbtack": 3,
    "owner_site": 7,
    "other": 9,
}


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def normalize_source(s: Optional[str]) -> str:
    """Normalize a source string to a canonical short tag (google, yelp, nextdoor, ...)."""
    if not s:
        return "other"
    s = s.lower().strip()
    if "google" in s:
        return "google"
    if "yelp" in s:
        return "yelp"
    if "nextdoor" in s:
        return "nextdoor"
    if "thumbtack" in s:
        return "thumbtack"
    if "bbb" in s or "better business" in s:
        return "bbb"
    if "facebook" in s:
        return "facebook"
    if "angi" in s or "homeadvisor" in s:
        return "angi"
    return s if s in SOURCE_PRIORITY else "other"


def source_priority(s: str) -> int:
    return SOURCE_PRIORITY.get(normalize_source(s), 99)


def normalize_review(r: Dict[str, Any]) -> Dict[str, Any]:
    """
    Coerce a review dict (from Places API, Bruce scrape, or hand-written) to
    canonical schema. Tolerant of varied input — fills missing fields with
    defaults, preserves extras under _extra.
    """
    text = (r.get("text") or r.get("body") or r.get("review") or r.get("content") or "").strip()
    author = (
        r.get("author") or r.get("reviewer") or r.get("author_name")
        or r.get("name") or r.get("user") or "Customer"
    )
    rating_raw = r.get("rating") or r.get("stars") or r.get("score")
    try:
        rating = int(float(rating_raw)) if rating_raw is not None else None
    except (ValueError, TypeError):
        rating = None

    # Date may be ISO, unix ts, or "Month Day, Year"
    date_raw = r.get("date") or r.get("created_at") or r.get("time") or r.get("posted_at")
    date = None
    if date_raw:
        if isinstance(date_raw, (int, float)):
            try:
                date = datetime.fromtimestamp(date_raw, tz=timezone.utc).strftime("%Y-%m-%d")
            except (ValueError, OSError):
                pass
        elif isinstance(date_raw, str):
            # Try ISO first
            for fmt in ("%Y-%m-%d", "%Y-%m-%dT%H:%M:%S", "%Y-%m-%dT%H:%M:%SZ", "%B %d, %Y", "%b %d, %Y"):
                try:
                    date = datetime.strptime(date_raw[:19] if "T" in date_raw else date_raw, fmt).strftime("%Y-%m-%d")
                    break
                except ValueError:
                    continue
            if not date:
                # Last-ditch: take first 10 chars if they look like YYYY-MM-DD
                if len(date_raw) >= 10 and date_raw[4] == "-" and date_raw[7] == "-":
                    date = date_raw[:10]

    source = normalize_source(r.get("source") or r.get("platform"))
    verified = r.get("verified", source == "google")  # Google API entries are inherently verified

    out = {
        "author": author,
        "rating": rating,
        "date": date,
        "source": source,
        "text": text,
        "verified": bool(verified),
    }
    # Preserve a few extra fields if present
    for k in ("language", "relative_time_description", "profile_photo_url", "url"):
        if r.get(k):
            out[k] = r[k]
    return out


def dedup_key(r: Dict[str, Any]) -> Tuple[str, str]:
    """
    (lowercased author, first 60 chars of normalized text) — collisions = dups.
    Author normalization: strip whitespace + lowercase. Common reviewer-name
    variations ("J. Smith" vs "John Smith") will NOT collide on this key —
    intentional, we'd rather keep both than drop a real one.
    """
    author = (r.get("author") or "").strip().lower()
    text = " ".join((r.get("text") or "").split())[:60].lower()
    return (author, text)


def load_reviews_file(path: Path) -> List[Dict[str, Any]]:
    """
    Robust loader — accepts:
      - dict with "reviews" list
      - list of review dicts directly
      - dict with other shapes (dig for "reviews" recursively)
    Returns a list of review dicts (raw, not yet normalized).
    """
    if not path.exists():
        return []
    try:
        with open(path) as f:
            data = json.load(f)
    except (json.JSONDecodeError, OSError) as e:
        log_warn(f"could not parse {path}: {e}")
        return []

    if isinstance(data, list):
        return data
    if isinstance(data, dict):
        # Common: top-level "reviews" key
        if "reviews" in data and isinstance(data["reviews"], list):
            return data["reviews"]
        # Bruce sometimes nests under per-source keys: {"yelp": {"reviews": [...]}}
        out = []
        for v in data.values():
            if isinstance(v, dict) and "reviews" in v and isinstance(v["reviews"], list):
                # Tag each with the parent key as source if not already set
                for r in v["reviews"]:
                    if "source" not in r:
                        r = dict(r)
                        # Find the key name for this nested dict
                        for k, nested in data.items():
                            if nested is v:
                                r["source"] = k
                                break
                    out.append(r)
            elif isinstance(v, list):
                out.extend(v)
        return out
    return []


def merge(existing: List[Dict[str, Any]], raw: List[Dict[str, Any]]) -> Tuple[List[Dict[str, Any]], Dict[str, Any]]:
    """Returns (merged_list, log)."""
    log = {
        "merged_at": now_iso(),
        "kept_from_existing": 0,
        "kept_from_raw": 0,
        "dups_dropped": 0,
        "duplicates": [],  # list of {kept_source, dropped_source, author, text_prefix}
    }

    # Tag with provenance for audit
    norm_existing = [{**normalize_review(r), "_origin": "existing"} for r in existing]
    norm_raw = [{**normalize_review(r), "_origin": "raw"} for r in raw]

    by_key: Dict[Tuple[str, str], Dict[str, Any]] = {}

    # Insert in source-priority order so the first hit at a key wins
    all_reviews = norm_existing + norm_raw
    all_reviews.sort(key=lambda r: (source_priority(r["source"]), r.get("date") or "", -1 * (r.get("rating") or 0)))

    for r in all_reviews:
        key = dedup_key(r)
        if not key[1]:  # empty text — skip
            continue
        if key in by_key:
            existing_winner = by_key[key]
            log["dups_dropped"] += 1
            log["duplicates"].append({
                "kept_source": existing_winner["source"],
                "dropped_source": r["source"],
                "author": r.get("author"),
                "text_prefix": r.get("text", "")[:60],
            })
        else:
            by_key[key] = r
            if r.get("_origin") == "existing":
                log["kept_from_existing"] += 1
            else:
                log["kept_from_raw"] += 1

    # Final sort: source priority asc, then date desc, then rating desc
    merged = list(by_key.values())
    merged.sort(key=lambda r: (
        source_priority(r["source"]),
        -(int(r["date"].replace("-", "")) if r.get("date") and r["date"].replace("-", "").isdigit() else 0),
        -(r.get("rating") or 0),
    ))

    # Strip provenance marker before write
    for r in merged:
        r.pop("_origin", None)

    return merged, log


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("slug", help="site slug")
    ap.add_argument("--dry-run", action="store_true", help="show diff, don't write")
    args = ap.parse_args()

    repo_root = Path(__file__).resolve().parent.parent
    site_dir = repo_root / "sites" / args.slug
    if not site_dir.exists():
        log_fail(f"{site_dir} does not exist")
        sys.exit(2)

    reviews_path = site_dir / "reviews.json"
    raw_path = site_dir / "reviews-raw.json"
    merge_log_path = site_dir / "reviews-merge-log.json"

    print(f"{BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{NC}")
    print(f"{BLUE}reviews-merge.py{NC} — slug: {YELLOW}{args.slug}{NC}")
    print(f"{BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{NC}")

    existing = load_reviews_file(reviews_path)
    raw = load_reviews_file(raw_path)

    if not existing and not raw:
        log_warn("neither reviews.json nor reviews-raw.json has reviews to merge")
        sys.exit(0)

    log_info(f"existing reviews.json: {len(existing)} reviews")
    log_info(f"reviews-raw.json:      {len(raw)} reviews")

    merged, mlog = merge(existing, raw)

    log_pass(f"merged: {len(merged)} unique reviews")
    log_info(f"  from existing: {mlog['kept_from_existing']}")
    log_info(f"  from raw:      {mlog['kept_from_raw']}")
    log_info(f"  dups dropped:  {mlog['dups_dropped']}")

    # Source breakdown
    sources_count: Dict[str, int] = {}
    for r in merged:
        s = r.get("source", "other")
        sources_count[s] = sources_count.get(s, 0) + 1
    if sources_count:
        breakdown = ", ".join(f"{s}={n}" for s, n in sorted(sources_count.items(), key=lambda x: -x[1]))
        log_info(f"  by source:     {breakdown}")

    if args.dry_run:
        log_info("--dry-run: not writing files")
        sys.exit(0)

    # Write merged reviews.json
    out = {
        "slug": args.slug,
        "captured": len(merged),
        "captured_at": now_iso(),
        "sources": [
            {"source": s, "count": n, "fetched_at": now_iso()}
            for s, n in sorted(sources_count.items(), key=lambda x: source_priority(x[0]))
        ],
        "reviews": merged,
    }
    # Preserve total_reviews + overall_rating from existing if present
    if reviews_path.exists():
        try:
            with open(reviews_path) as f:
                old = json.load(f)
            if isinstance(old, dict):
                if "total_reviews" in old:
                    out["total_reviews"] = old["total_reviews"]
                if "overall_rating" in old:
                    out["overall_rating"] = old["overall_rating"]
        except Exception:
            pass

    with open(reviews_path, "w") as f:
        json.dump(out, f, indent=2)
    log_pass(f"wrote {reviews_path} ({len(merged)} reviews)")

    # Write merge log
    with open(merge_log_path, "w") as f:
        json.dump(mlog, f, indent=2)
    log_info(f"wrote {merge_log_path} (audit trail)")

    print(f"{BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{NC}")
    print(f"  next: ./scripts/render-reviews-bar.py {args.slug}")
    sys.exit(0)


if __name__ == "__main__":
    main()

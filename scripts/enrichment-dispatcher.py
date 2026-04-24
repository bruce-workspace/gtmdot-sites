#!/usr/bin/env python3
"""
enrichment-dispatcher.py — Mini finding #5

Scans sites/ for prospects R1VS has built but where capture is thin, and
writes collect-request.md files for Bruce per HANDOFF-CONTRACT §11.4.

Triggers (any of):
  - photos_count < MIN_PHOTOS (default 3)
  - reviews.json counts.captured < MIN_REVIEWS (default 3)
  - reviews.json missing entirely

Skip conditions:
  - collect-request.md already exists in site dir (in-flight)
  - bruce-collected.md exists and is newer than 48h (fresh enrichment)
  - Site dir contains no R1VS artifacts (not yet built, skip silently)

Usage:
  enrichment-dispatcher.py [--dry-run] [--min-photos N] [--min-reviews N]
  enrichment-dispatcher.py --sites-dir /path/to/sites
  enrichment-dispatcher.py --slug <slug>   # process one site only

Output: JSON summary on stdout listing written / skipped / errored sites.
Exit 0 on success (even if no work found); 2 on config/usage error.

Safe to run repeatedly — idempotent (won't overwrite pending requests).
Never writes to Supabase. Never touches HTML. Never deploys.
Per §11.8 single-writer-per-asset: Mini writes collect-request.md, nothing else.
"""

import argparse
import json
import os
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path


DEFAULT_SITES_DIR = Path("/Users/bruce/.openclaw/workspace/gtmdot-sites/sites")
MIN_PHOTOS_DEFAULT = 3
MIN_REVIEWS_DEFAULT = 3
BRUCE_FRESHNESS_HOURS = 48
PHOTO_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp", ".gif"}


def count_photos(site_dir: Path) -> int:
    """Count real photo files in site_dir/photos/ (excludes intent.json etc.)."""
    photos_dir = site_dir / "photos"
    if not photos_dir.exists():
        return 0
    return sum(
        1
        for f in photos_dir.iterdir()
        if f.is_file() and f.suffix.lower() in PHOTO_EXTENSIONS
    )


def read_reviews_counts(site_dir: Path) -> tuple[int | None, str]:
    """
    Return (captured_count, reason).

    captured_count: integer captured reviews, or None if file missing/bad.
    reason: human-readable explanation for logs.
    """
    reviews_path = site_dir / "reviews.json"
    if not reviews_path.exists():
        return None, "reviews.json missing"
    try:
        data = json.loads(reviews_path.read_text())
    except json.JSONDecodeError as e:
        return None, f"reviews.json invalid: {e}"
    except OSError as e:
        return None, f"reviews.json read error: {e}"

    # Primary: counts.captured
    counts = data.get("counts") if isinstance(data, dict) else None
    if isinstance(counts, dict) and isinstance(counts.get("captured"), int):
        return counts["captured"], "from counts.captured"

    # Fallback: len(reviews)
    reviews = data.get("reviews") if isinstance(data, dict) else data
    if isinstance(reviews, list):
        return len(reviews), "from len(reviews) array"

    return 0, "reviews.json has no counts.captured or reviews[]"


def has_pending_collect_request(site_dir: Path) -> bool:
    return (site_dir / "collect-request.md").exists()


def has_fresh_bruce_collected(site_dir: Path, freshness_hours: int) -> bool:
    p = site_dir / "bruce-collected.md"
    if not p.exists():
        return False
    mtime = datetime.fromtimestamp(p.stat().st_mtime, tz=timezone.utc)
    age = datetime.now(timezone.utc) - mtime
    return age < timedelta(hours=freshness_hours)


def site_has_r1vs_artifacts(site_dir: Path) -> bool:
    """Has R1VS actually built this site? Look for index.html or reviews.json."""
    return (site_dir / "index.html").exists() or (site_dir / "reviews.json").exists()


def needed_sources(site_dir: Path) -> list[str]:
    """
    Default source list for enrichment. Prefers unverified platforms first.
    Could be smarter later (read reviews.json capture_attempts to avoid re-scraping).
    """
    # TODO: consult reviews.json.capture_attempts to skip already-successful sources
    return ["yelp", "nextdoor", "thumbtack", "bbb"]


def build_collect_request(
    site_dir: Path,
    photos_count: int,
    reviews_count: int | None,
    reviews_reason: str,
    min_photos: int,
    min_reviews: int,
) -> str:
    """Produce the collect-request.md body. Format per HANDOFF-CONTRACT §11.4."""
    slug = site_dir.name
    now = datetime.now(timezone.utc).isoformat()

    reasons: list[str] = []
    if photos_count < min_photos:
        reasons.append(f"photos: {photos_count} of target {min_photos}")
    if reviews_count is None:
        reasons.append(f"reviews: {reviews_reason}")
    elif reviews_count < min_reviews:
        reasons.append(
            f"reviews: {reviews_count} captured of target {min_reviews} ({reviews_reason})"
        )

    gap_reason = "; ".join(reasons) if reasons else "no gap (should not reach here)"

    sources = needed_sources(site_dir)
    sources_block = "\n".join(f"{i+1}. {src}.com" for i, src in enumerate(sources))

    return f"""---
slug: {slug}
requested_at: {now}
requested_by: mini-enrichment-dispatcher
---

# Collect Request — {slug}

Auto-generated because site capture is thin after R1VS's initial build.
Per HANDOFF-CONTRACT §11 you own the scrape; Mini integrates when your
`bruce-collected.md` drops.

## Gap reason
{gap_reason}

## Current capture state
- Photos in `sites/{slug}/photos/`: **{photos_count}** (target: {min_photos})
- Reviews captured (`reviews.json.counts.captured`): **{reviews_count if reviews_count is not None else 'missing'}** (target: {min_reviews})

## Requested sources (priority order)
{sources_block}

## What to collect per source
- All photos attributed to the business or its work (save to `photos-raw/<source>-NN.jpg`)
- All reviews (verbatim text, date, reviewer name, star rating → `reviews-raw.json` per §11.5)
- Skip: customer selfies unrelated to work; company logos; blurry screenshots of documents

## Budget
- max_photos_total: 15
- max_reviews_total: 30
- max_wallclock_minutes: 10

## Skip if blocked
If any source returns captcha, login wall, or bot-detection: mark failed
with reason code per §11.6, move to next. Do not attempt to bypass.

## Mini integration on your return
When `bruce-collected.md` appears, Mini's site-qa-runner picks up:
- Any new photos → integrate into gallery slots per R1VS's photos/intent.json
- Any new reviews → append to `reviews.json` + re-render review UI if
  `captured` crosses ≥3 threshold (previously rendered empty-state)
- Re-run pre-push-gate.sh + verify-build.sh before Mini deploys

## Dispatcher metadata
- Trigger: photos<{min_photos} OR reviews_captured<{min_reviews}
- Dispatcher: `scripts/enrichment-dispatcher.py` (Mini finding #5)
- Safe to re-run — this file will be consumed + deleted by your scan
"""


def main() -> None:
    ap = argparse.ArgumentParser(
        description="Write collect-request.md for sites with thin photo/review capture."
    )
    ap.add_argument(
        "--dry-run",
        action="store_true",
        help="Report what would be written without touching disk.",
    )
    ap.add_argument(
        "--min-photos",
        type=int,
        default=MIN_PHOTOS_DEFAULT,
        help=f"Photos threshold (default {MIN_PHOTOS_DEFAULT}).",
    )
    ap.add_argument(
        "--min-reviews",
        type=int,
        default=MIN_REVIEWS_DEFAULT,
        help=f"Reviews-captured threshold (default {MIN_REVIEWS_DEFAULT}).",
    )
    ap.add_argument(
        "--sites-dir",
        default=str(DEFAULT_SITES_DIR),
        help="Override default sites dir.",
    )
    ap.add_argument(
        "--slug",
        help="Process only this one slug (for testing).",
    )
    ap.add_argument(
        "--freshness-hours",
        type=int,
        default=BRUCE_FRESHNESS_HOURS,
        help=f"Skip if bruce-collected.md newer than N hours (default {BRUCE_FRESHNESS_HOURS}).",
    )
    args = ap.parse_args()

    sites_dir = Path(args.sites_dir)
    if not sites_dir.exists():
        print(f"error: sites dir {sites_dir} not found", file=sys.stderr)
        sys.exit(2)

    if args.slug:
        candidates = [sites_dir / args.slug]
        if not candidates[0].exists():
            print(f"error: slug {args.slug} not found in {sites_dir}", file=sys.stderr)
            sys.exit(2)
    else:
        candidates = sorted(
            d for d in sites_dir.iterdir()
            if d.is_dir() and not d.name.startswith(".") and d.name != "_shared"
        )

    results: dict[str, list] = {"written": [], "skipped": [], "errored": []}

    for site_dir in candidates:
        slug = site_dir.name
        try:
            if not site_has_r1vs_artifacts(site_dir):
                results["skipped"].append(
                    {"slug": slug, "reason": "no-r1vs-artifacts-yet"}
                )
                continue

            if has_pending_collect_request(site_dir):
                results["skipped"].append(
                    {"slug": slug, "reason": "pending-collect-request"}
                )
                continue

            if has_fresh_bruce_collected(site_dir, args.freshness_hours):
                results["skipped"].append(
                    {"slug": slug, "reason": "fresh-bruce-collected"}
                )
                continue

            photos = count_photos(site_dir)
            reviews_count, reviews_reason = read_reviews_counts(site_dir)

            needs_photos = photos < args.min_photos
            needs_reviews = (reviews_count is None) or (reviews_count < args.min_reviews)

            if not (needs_photos or needs_reviews):
                continue  # above threshold, nothing to do

            body = build_collect_request(
                site_dir,
                photos,
                reviews_count,
                reviews_reason,
                args.min_photos,
                args.min_reviews,
            )

            if args.dry_run:
                results["written"].append(
                    {
                        "slug": slug,
                        "photos": photos,
                        "reviews_captured": reviews_count,
                        "mode": "dry-run",
                        "would_write": str(site_dir / "collect-request.md"),
                    }
                )
            else:
                target = site_dir / "collect-request.md"
                target.write_text(body)
                results["written"].append(
                    {
                        "slug": slug,
                        "photos": photos,
                        "reviews_captured": reviews_count,
                        "path": str(target),
                    }
                )
        except Exception as e:  # noqa: BLE001
            results["errored"].append({"slug": slug, "error": str(e)})

    print(json.dumps(results, indent=2))
    sys.exit(0)


if __name__ == "__main__":
    main()

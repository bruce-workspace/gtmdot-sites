#!/usr/bin/env python3
"""
integrate-bruce-collected.py — Mini consumer for Bruce's scraped enrichment.

Reads Bruce's delivery artifacts (bruce-collected.md + reviews-raw.json +
photos-raw/*) per HANDOFF-CONTRACT §11.5-§11.6, merges new reviews into
reviews.json, stages new photos in photos/inbox/, and signals R1VS via
needs-repolish.md to re-render the review UI on its next polish pass.

Respects single-writer-per-asset invariant (§11.8):
  - Mini writes reviews.json (merging in new entries)
  - Mini writes photos/inbox/<file> (new subdir — gallery slots stay R1VS-owned)
  - Mini writes needs-repolish.md (signal for R1VS)
  - Mini ARCHIVES bruce-collected.md + reviews-raw.json into collect-request-archive/
  - Mini does NOT modify index.html (R1VS-owned)
  - Mini does NOT modify gallery photo slots (R1VS-owned per photos/intent.json)

Usage:
  integrate-bruce-collected.py [--dry-run]
  integrate-bruce-collected.py --slug <slug>
  integrate-bruce-collected.py --sites-dir /alternate/path

Exit:
  0 — ran cleanly
  1 — one or more integrations errored
  2 — config / usage error

Dedup strategy for reviews:
  Two reviews considered duplicates if all three match:
    - reviewer_name (case-insensitive)
    - review_date (YYYY-MM-DD or "N years/months ago" — normalized loosely)
    - first 80 chars of review_text (case-insensitive, whitespace-normalized)
  Conservative: when in doubt, keep both.
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path


DEFAULT_SITES_DIR = Path("/Users/bruce/.openclaw/workspace/gtmdot-sites/sites")
PHOTO_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp", ".gif"}
ARCHIVE_DIR_NAME = "collect-request-archive"


# ───── frontmatter parsing ─────

def parse_frontmatter(md_text: str) -> tuple[dict, str]:
    """Return (frontmatter_dict, body_text). Handles simple key: value YAML."""
    if not md_text.startswith("---"):
        return {}, md_text
    parts = md_text.split("---", 2)
    if len(parts) < 3:
        return {}, md_text
    _, fm_text, body = parts
    fm: dict = {}
    for line in fm_text.strip().splitlines():
        if ":" in line:
            k, _, v = line.partition(":")
            fm[k.strip()] = v.strip().strip('"').strip("'")
    return fm, body


# ───── review merging ─────

def _norm_name(s: str) -> str:
    return re.sub(r"\s+", " ", (s or "").strip().lower())


def _norm_text_prefix(s: str, n: int = 80) -> str:
    return re.sub(r"\s+", " ", (s or "").strip().lower())[:n]


def _norm_date(s: str) -> str:
    """Normalize dates loosely — exact match good, relative-time string OK too."""
    return (s or "").strip().lower()


def review_dedup_key(r: dict) -> tuple[str, str, str]:
    return (
        _norm_name(r.get("reviewer_name") or r.get("author", "")),
        _norm_date(r.get("review_date") or r.get("date", "")),
        _norm_text_prefix(r.get("review_text") or r.get("text", "")),
    )


def load_existing_reviews(site_dir: Path) -> dict:
    """Load reviews.json or return a fresh skeleton."""
    p = site_dir / "reviews.json"
    if not p.exists():
        return {
            "reviews": [],
            "counts": {
                "captured": 0,
                "target_min": 3,
                "total_available": "unknown",
            },
            "notes": "Initialized by integrate-bruce-collected.py",
            "capture_attempts": [],
        }
    try:
        return json.loads(p.read_text())
    except (json.JSONDecodeError, OSError) as e:
        raise RuntimeError(f"reviews.json malformed: {e}")


def load_raw_reviews(site_dir: Path) -> list[dict]:
    """Load reviews-raw.json or return []."""
    p = site_dir / "reviews-raw.json"
    if not p.exists():
        return []
    try:
        data = json.loads(p.read_text())
        if isinstance(data, list):
            return data
        if isinstance(data, dict) and isinstance(data.get("reviews"), list):
            return data["reviews"]
        return []
    except (json.JSONDecodeError, OSError):
        return []


def merge_reviews(existing: dict, raw: list[dict]) -> tuple[int, int]:
    """
    Merge raw reviews into existing. Returns (added, skipped_as_dupe).
    Mutates existing in place.
    """
    existing_reviews = existing.setdefault("reviews", [])
    existing_keys = {review_dedup_key(r) for r in existing_reviews}

    added = 0
    skipped = 0
    for r in raw:
        key = review_dedup_key(r)
        if key in existing_keys:
            skipped += 1
            continue
        # Normalize into our storage format
        normalized = {
            "author": r.get("reviewer_name") or r.get("author", ""),
            "rating": r.get("star_rating") or r.get("rating"),
            "text": r.get("review_text") or r.get("text", ""),
            "source": r.get("source", "unknown"),
            "date": r.get("review_date") or r.get("date", ""),
        }
        if r.get("source_url"):
            normalized["source_url"] = r["source_url"]
        existing_reviews.append(normalized)
        existing_keys.add(key)
        added += 1

    # Update counts.captured
    counts = existing.setdefault("counts", {})
    counts["captured"] = len(existing_reviews)

    return added, skipped


# ───── photo staging ─────

def stage_photos(site_dir: Path, dry_run: bool) -> tuple[int, list[str]]:
    """
    Move files from photos-raw/ to photos/inbox/. Returns (count_moved, filenames).

    R1VS's next polish pass picks from photos/inbox/ and decides which go
    into gallery slots per photos/intent.json.
    """
    raw_dir = site_dir / "photos-raw"
    if not raw_dir.exists():
        return 0, []

    inbox = site_dir / "photos" / "inbox"
    if not dry_run:
        inbox.mkdir(parents=True, exist_ok=True)

    moved: list[str] = []
    for f in sorted(raw_dir.iterdir()):
        if not f.is_file():
            continue
        if f.suffix.lower() not in PHOTO_EXTENSIONS:
            continue
        target = inbox / f.name
        if target.exists():
            # Name collision — preserve both with timestamp suffix
            ts = datetime.now(timezone.utc).strftime("%Y%m%d%H%M%S")
            target = inbox / f"{f.stem}-{ts}{f.suffix}"
        if not dry_run:
            shutil.move(str(f), str(target))
        moved.append(target.name)

    # If raw dir is empty, leave it (Bruce may reuse next run)
    return len(moved), moved


# ───── signal R1VS ─────

def write_repolish_signal(
    site_dir: Path,
    reviews_added: int,
    photos_added: int,
    bruce_collected_at: str,
    dry_run: bool,
) -> None:
    if dry_run:
        return
    now = datetime.now(timezone.utc).isoformat()
    body = f"""---
slug: {site_dir.name}
signaled_by: mini-integrate-bruce-collected
signaled_at: {now}
bruce_collected_at: {bruce_collected_at}
reviews_added: {reviews_added}
photos_added: {photos_added}
---

# needs-repolish

Bruce enrichment landed. Mini integrated:
- {reviews_added} new reviews into reviews.json
- {photos_added} new photos into photos/inbox/

On your next polish pass, please:
1. Re-render review UI section of index.html per the new counts.captured
   (if previously showing empty-state and now >=3, swap to full track)
2. Decide which photos/inbox/*.* move into gallery slots per intent.json;
   rename appropriately (e.g. photos/inbox/yelp-01.jpg → photos/gbp-4.jpg
   if it fills the 4th gallery slot)
3. Run scripts/pre-push-gate.sh + scripts/verify-build.sh
4. Delete this file when done

Safe to ignore if the site is already shipping at quality. Mini will
re-scan and re-signal on Bruce's next delivery.
"""
    (site_dir / "needs-repolish.md").write_text(body)


# ───── archival ─────

def archive_bruce_artifacts(site_dir: Path, dry_run: bool) -> list[str]:
    """Move bruce-collected.md + reviews-raw.json to collect-request-archive/."""
    archive = site_dir / ARCHIVE_DIR_NAME
    if not dry_run:
        archive.mkdir(exist_ok=True)

    ts = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
    archived: list[str] = []

    for fname, new_prefix in [
        ("bruce-collected.md", "bruce-collected"),
        ("reviews-raw.json", "reviews-raw"),
    ]:
        src = site_dir / fname
        if src.exists():
            ext = src.suffix
            dst = archive / f"{new_prefix}-{ts}{ext}"
            if not dry_run:
                shutil.move(str(src), str(dst))
            archived.append(str(dst.relative_to(site_dir)))

    return archived


# ───── per-site pipeline ─────

def integrate_one(site_dir: Path, dry_run: bool) -> dict:
    slug = site_dir.name
    collected = site_dir / "bruce-collected.md"
    if not collected.exists():
        return {"slug": slug, "status": "skipped", "reason": "no-bruce-collected"}

    fm, _body = parse_frontmatter(collected.read_text())
    bruce_status = fm.get("status", "unknown")
    bruce_collected_at = fm.get("collected_at", "unknown")

    if bruce_status == "failed":
        # Don't integrate a failed delivery; archive it so it doesn't re-trigger
        archived = archive_bruce_artifacts(site_dir, dry_run)
        return {
            "slug": slug,
            "status": "archived-failed-delivery",
            "archived": archived,
        }

    # Load + merge reviews
    try:
        existing = load_existing_reviews(site_dir)
    except RuntimeError as e:
        return {"slug": slug, "status": "error", "error": str(e)}

    raw = load_raw_reviews(site_dir)
    added, skipped = merge_reviews(existing, raw)

    if not dry_run and added > 0:
        (site_dir / "reviews.json").write_text(json.dumps(existing, indent=2))

    # Stage photos
    photos_count, photos_names = stage_photos(site_dir, dry_run)

    # Signal R1VS if anything material changed
    if added > 0 or photos_count > 0:
        write_repolish_signal(
            site_dir, added, photos_count, bruce_collected_at, dry_run
        )

    # Archive the bruce artifacts so we don't reprocess
    archived = archive_bruce_artifacts(site_dir, dry_run)

    return {
        "slug": slug,
        "status": "integrated" if not dry_run else "dry-run",
        "bruce_status": bruce_status,
        "reviews_added": added,
        "reviews_dedup_skipped": skipped,
        "photos_staged": photos_count,
        "photos_files": photos_names[:10],  # cap for log brevity
        "archived": archived,
    }


# ───── main ─────

def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--slug", help="just this one slug")
    ap.add_argument("--sites-dir", default=str(DEFAULT_SITES_DIR))
    args = ap.parse_args()

    sites_dir = Path(args.sites_dir)
    if not sites_dir.exists():
        print(f"error: {sites_dir} not found", file=sys.stderr)
        sys.exit(2)

    if args.slug:
        candidates = [sites_dir / args.slug]
        if not candidates[0].exists():
            print(f"error: slug {args.slug} not found", file=sys.stderr)
            sys.exit(2)
    else:
        candidates = sorted(
            d for d in sites_dir.iterdir()
            if d.is_dir() and not d.name.startswith(".") and d.name != "_shared"
        )

    results: list[dict] = []
    any_errors = False
    for site_dir in candidates:
        res = integrate_one(site_dir, args.dry_run)
        if res["status"] == "error":
            any_errors = True
        # Skip silent "no-bruce-collected" entries from the summary list noise
        if res["status"] != "skipped":
            results.append(res)

    summary = {
        "sites_scanned": len(candidates),
        "results": results,
    }
    print(json.dumps(summary, indent=2))
    sys.exit(1 if any_errors else 0)


if __name__ == "__main__":
    main()

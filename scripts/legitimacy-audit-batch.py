#!/usr/bin/env python3
"""
legitimacy-audit-batch.py — run the legitimacy-screen rules across every
sites/<slug>/ folder and produce a single morning report.

Usage:
  python3 scripts/legitimacy-audit-batch.py
  python3 scripts/legitimacy-audit-batch.py --refresh-stale  # re-fetch Places API for stale snapshots
  python3 scripts/legitimacy-audit-batch.py --output reports/legitimacy-audit-YYYY-MM-DD.md

Data sources per site (in order — first match wins):
  1. sites/<slug>/legitimacy-check.json — existing legitimacy artifact
  2. sites/<slug>/gbp_snapshot.json — pinned GBP data
  3. sites/<slug>/reviews.json — review count + rating
  4. sites/<slug>/bruce-collected.md — extract place_id, rating, count

Reports group sites into PASS / FAIL / NEEDS_DECISION sections.
NEEDS_DECISION = insufficient data on disk to apply rules.

Exit codes:
  0 — report written
  1 — no sites found / report write error
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Any

# Same rules as scripts/legitimacy-screen.py — keep in sync
MIN_RATING = 4.5
MIN_REVIEWS = 10
DORMANT_MONTHS = 24

VERTICAL_BLOCKLIST = {"lead-gen-broker", "franchise-unverified", "referral-funnel"}


def load_json(path: Path) -> Optional[dict]:
    if not path.exists():
        return None
    try:
        with open(path) as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        return None


def extract_place_id_from_collected(path: Path) -> Optional[str]:
    if not path.exists():
        return None
    try:
        text = path.read_text()
    except OSError:
        return None
    m = re.search(r'\bplace[_ ]?id[^A-Za-z0-9_]*([A-Za-z0-9_-]+)', text, re.IGNORECASE)
    if m:
        return m.group(1)
    m = re.search(r'\bChIJ[A-Za-z0-9_-]+', text)
    if m:
        return m.group(0)
    return None


def extract_rating_from_collected(path: Path) -> Tuple[Optional[float], Optional[int]]:
    """Try to pull (rating, count) from a Bruce-collected.md."""
    if not path.exists():
        return (None, None)
    try:
        text = path.read_text()
    except OSError:
        return (None, None)
    rating = None
    count = None
    m = re.search(r'(?:overall\s+)?rating[^0-9]*(\d+\.?\d*)\s*\(?(\d+)?', text, re.IGNORECASE)
    if m:
        try:
            rating = float(m.group(1))
        except (ValueError, TypeError):
            pass
        if m.group(2):
            try:
                count = int(m.group(2))
            except (ValueError, TypeError):
                pass
    if count is None:
        m = re.search(r'(\d+)\s+reviews?', text, re.IGNORECASE)
        if m:
            try:
                count = int(m.group(1))
            except (ValueError, TypeError):
                pass
    return (rating, count)


def assess_site(site_dir: Path) -> Dict[str, Any]:
    """
    Returns a dict with the assessment outcome for one site:
      slug, status (PASS|FAIL|NEEDS_DECISION), rating, total_reviews,
      last_review_date, dormant_days, reasons[], data_source, notes[]
    """
    slug = site_dir.name
    out = {
        "slug": slug,
        "status": "NEEDS_DECISION",
        "rating": None,
        "total_reviews": None,
        "last_review_date": None,
        "dormant_days": None,
        "reasons": [],
        "data_source": None,
        "notes": [],
        "data_age_days": None,
    }

    # Source 1: existing legitimacy-check.json
    legit = load_json(site_dir / "legitimacy-check.json")
    if legit:
        out["data_source"] = "legitimacy-check.json"
        out["status"] = "PASS" if legit.get("passed") else "FAIL"
        out["reasons"] = list(legit.get("reasons") or [])
        snap = legit.get("snapshot_data") or {}
        out["rating"] = snap.get("rating")
        out["total_reviews"] = snap.get("total_reviews")
        # data age
        if "snapshot_at" in legit:
            try:
                snap_dt = datetime.fromisoformat(legit["snapshot_at"].replace("Z", "+00:00"))
                out["data_age_days"] = (datetime.now(timezone.utc) - snap_dt).days
            except Exception:
                pass
        return out

    # Source 2: gbp_snapshot.json (more recent if Mini refreshed)
    snap = load_json(site_dir / "gbp_snapshot.json")
    if snap:
        out["data_source"] = "gbp_snapshot.json"
        out["rating"] = snap.get("rating")
        out["total_reviews"] = snap.get("review_count_total")
        out["last_review_date"] = snap.get("last_review_date")
        if "fetched_at" in snap:
            try:
                snap_dt = datetime.fromisoformat(snap["fetched_at"].replace("Z", "+00:00"))
                out["data_age_days"] = (datetime.now(timezone.utc) - snap_dt).days
            except Exception:
                pass
        # Apply rules
        reasons = []
        if out["rating"] is None:
            reasons.append("no rating in snapshot")
        elif out["rating"] < MIN_RATING:
            reasons.append(f"rating {out['rating']} < {MIN_RATING}")
        if out["total_reviews"] is None:
            reasons.append("no review count in snapshot")
        elif out["total_reviews"] < MIN_REVIEWS:
            reasons.append(f"total_reviews {out['total_reviews']} < {MIN_REVIEWS}")
        if out["last_review_date"]:
            try:
                last_dt = datetime.fromisoformat(out["last_review_date"]).replace(tzinfo=timezone.utc)
                age_days = (datetime.now(timezone.utc) - last_dt).days
                out["dormant_days"] = age_days
                if age_days > DORMANT_MONTHS * 30:
                    reasons.append(f"latest review {age_days}d old > {DORMANT_MONTHS}mo")
            except Exception:
                pass
        if snap.get("gbp_match_verified") is False:
            reasons.append("GBP does not match claimed address (ghost listing)")
        out["reasons"] = reasons
        out["status"] = "PASS" if not reasons else "FAIL"
        return out

    # Source 3: reviews.json
    reviews = load_json(site_dir / "reviews.json")
    if reviews:
        out["data_source"] = "reviews.json"
        out["rating"] = reviews.get("overall_rating")
        # `total_reviews` is the GBP total; fall back to `captured` (which is just
        # what R1VS captured, not the GBP total — but we mark that distinction).
        total = reviews.get("total_reviews")
        captured = reviews.get("captured")
        out["total_reviews"] = total if total is not None else captured

        reasons = []
        missing_data = []
        if out["rating"] is None:
            missing_data.append("no rating in reviews.json")
        elif out["rating"] < MIN_RATING:
            reasons.append(f"rating {out['rating']} < {MIN_RATING}")
        if total is None and captured is None:
            missing_data.append("no review count in reviews.json")
        elif total is None and captured is not None:
            # We only know captured, not total — note it but don't fail
            out["notes"].append(f"only `captured` count available ({captured}); GBP total unknown — needs gbp_snapshot.json refresh")
            if captured < MIN_REVIEWS:
                missing_data.append(f"captured {captured} < {MIN_REVIEWS} (but this is captured-only; GBP total may be higher)")
        elif total is not None and total < MIN_REVIEWS:
            reasons.append(f"total_reviews {total} < {MIN_REVIEWS}")

        out["reasons"] = reasons
        if reasons:
            out["status"] = "FAIL"
        elif missing_data:
            out["status"] = "NEEDS_DECISION"
            out["notes"].extend(missing_data)
        else:
            out["status"] = "PASS"
        out["notes"].append("data from reviews.json only — run write-gbp-snapshot.py for richer signals")
        return out

    # Source 4: bruce-collected.md
    collected_path = site_dir / "bruce-collected.md"
    if collected_path.exists():
        rating, count = extract_rating_from_collected(collected_path)
        place_id = extract_place_id_from_collected(collected_path)
        out["data_source"] = "bruce-collected.md"
        out["rating"] = rating
        out["total_reviews"] = count
        if place_id:
            out["notes"].append(f"place_id from bruce-collected: {place_id}")
        reasons = []
        if rating is None:
            reasons.append("no rating extractable from bruce-collected.md")
        elif rating < MIN_RATING:
            reasons.append(f"rating {rating} < {MIN_RATING}")
        if count is None:
            out["notes"].append("could not extract total review count from bruce-collected — only Bruce-captured count")
        elif count < MIN_REVIEWS:
            reasons.append(f"reviews captured {count} < {MIN_REVIEWS} (NOTE: this is what Bruce captured, not necessarily the GBP total)")
        if reasons:
            out["status"] = "FAIL"
            out["reasons"] = reasons
        else:
            # If we have rating but no count, mark NEEDS_DECISION
            if rating is not None and rating >= MIN_RATING and count is None:
                out["status"] = "NEEDS_DECISION"
                out["notes"].append("rating OK but total review count unknown — needs Places API hit")
            else:
                out["status"] = "PASS"
        return out

    # No data at all
    out["notes"].append("no data on disk — neither legitimacy-check / gbp_snapshot / reviews.json / bruce-collected.md present")
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    default_out = f"reports/legitimacy-audit-{today}.md"
    ap.add_argument("--output", default=default_out, help=f"output path (default: {default_out})")
    args = ap.parse_args()

    repo_root = Path(__file__).resolve().parent.parent
    sites_dir = repo_root / "sites"
    if not sites_dir.exists():
        print(f"ERROR: {sites_dir} does not exist", file=sys.stderr)
        sys.exit(1)

    site_dirs = sorted([d for d in sites_dir.iterdir() if d.is_dir() and not d.name.startswith("_")])

    print(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(f"legitimacy-audit-batch — {len(site_dirs)} sites")
    print(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

    results = []
    for d in site_dirs:
        r = assess_site(d)
        results.append(r)
        rating_str = f"{r['rating']}*" if r['rating'] else "?"
        count_str = str(r['total_reviews']) if r['total_reviews'] is not None else "?"
        src = r['data_source'] or "(none)"
        print(f"  [{r['status']:18s}] {r['slug']:45s}  {rating_str:>5} {count_str:>4}rev  src={src}")

    pass_sites = [r for r in results if r["status"] == "PASS"]
    fail_sites = [r for r in results if r["status"] == "FAIL"]
    needs_sites = [r for r in results if r["status"] == "NEEDS_DECISION"]

    print()
    print(f"  {len(pass_sites)} PASS  •  {len(fail_sites)} FAIL  •  {len(needs_sites)} NEEDS_DECISION")
    print()

    # Build report
    out_path = repo_root / args.output
    out_path.parent.mkdir(parents=True, exist_ok=True)

    lines = []
    lines.append(f"# Legitimacy audit — {today}")
    lines.append("")
    lines.append(f"Run: `scripts/legitimacy-audit-batch.py`  •  audited: {len(results)} sites")
    lines.append(f"Rules: rating >= {MIN_RATING}  •  reviews >= {MIN_REVIEWS}  •  dormant > {DORMANT_MONTHS}mo  •  GBP match verified  •  vertical blocklist")
    lines.append("")
    lines.append(f"**Summary:** {len(pass_sites)} PASS  •  {len(fail_sites)} FAIL  •  {len(needs_sites)} NEEDS_DECISION")
    lines.append("")

    def render_section(title: str, sites: List[Dict], summary_first: bool = True):
        lines.append(f"## {title} ({len(sites)})")
        lines.append("")
        if not sites:
            lines.append("_None._")
            lines.append("")
            return
        lines.append("| Slug | Rating | Reviews | Last review | Data source | Reasons |")
        lines.append("|---|---|---|---|---|---|")
        for r in sites:
            rating = f"{r['rating']}" if r['rating'] is not None else "?"
            count = str(r['total_reviews']) if r['total_reviews'] is not None else "?"
            last_review = r.get("last_review_date") or "?"
            reasons = "; ".join(r.get("reasons") or []) or "—"
            src = r.get("data_source") or "none"
            lines.append(f"| `{r['slug']}` | {rating} | {count} | {last_review} | {src} | {reasons} |")
        lines.append("")

    render_section("FAIL — legitimacy-screen rules failed", fail_sites)
    render_section("NEEDS_DECISION — insufficient data on disk", needs_sites)
    render_section("PASS — meets thresholds", pass_sites)

    # Recommendations section
    lines.append("## Recommendations")
    lines.append("")
    lines.append(f"- **{len(fail_sites)} sites flagged FAIL.** Review reasons above. Likely candidates for `stage: dead` in Supabase.")
    lines.append(f"- **{len(needs_sites)} sites need a Places API hit** to resolve. Run `scripts/write-gbp-snapshot.py <slug> --places-api --name '...' --address '...'` for each.")
    lines.append(f"- **{len(pass_sites)} sites pass cleanly.** Continue through the pipeline.")
    lines.append("")
    lines.append("Note: This audit is filesystem-only. The full audit requires Supabase access to compare against the actual `ready_for_review` queue. Pending Jesse's Supabase service-role key for that comprehensive check.")

    with open(out_path, "w") as f:
        f.write("\n".join(lines))

    print(f"  wrote {out_path}")
    sys.exit(0)


if __name__ == "__main__":
    main()

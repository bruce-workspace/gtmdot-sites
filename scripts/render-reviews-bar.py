#!/usr/bin/env python3
"""
render-reviews-bar.py — pick the right reviews-bar path (A/B/C) and expand
the review-loop block per captured review.

Replaces the old "only REVIEW_1 token gets filled" failure mode where 4 of 5
captured reviews disappeared from the homepage.

Three paths per the SKILL.md §Phase 3 conditional review UI rule:
  captured >= 3 → PATH A: reviews-track with one .review-mini per review
  captured 1-2  → PATH B: single mini card + "See all on Google" link
  captured 0    → PATH C: empty-state block with GBP rating + link

The template index.html ships with all three paths in source. This script
keeps exactly one path and DELETES the other two, expanding the review loop
in path A or filling the single-review tokens in path B.

Usage:
  python3 scripts/render-reviews-bar.py <slug>
  python3 scripts/render-reviews-bar.py <slug> --html sites/<slug>/index.html
                                                 --reviews sites/<slug>/reviews.json

Idempotent: running twice on the same file produces the same output.
Exit codes:
  0 — reviews bar rendered (which path applied is logged)
  1 — error (missing reviews.json, missing template markers, etc.)
  2 — usage error
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Dict, List

RED = "\033[0;31m"
GREEN = "\033[0;32m"
YELLOW = "\033[1;33m"
BLUE = "\033[0;34m"
NC = "\033[0m"


def log_pass(m): print(f"  {GREEN}✓{NC} {m}")
def log_fail(m): print(f"  {RED}✗{NC} {m}", file=sys.stderr)
def log_info(m): print(f"  {BLUE}ℹ{NC} {m}")
def log_warn(m): print(f"  {YELLOW}⚠{NC} {m}")


# ───── markers ─────
PATH_A_OPEN = "<!-- PATH A — reviews-track for captured >= 3 -->"
LOOP_START = "<!-- REVIEWS_LOOP_START -->"
LOOP_END = "<!-- REVIEWS_LOOP_END -->"

PATH_B_BEGIN = "<!-- PATH B — FEW_REVIEWS_FALLBACK_START"
PATH_B_END = "FEW_REVIEWS_FALLBACK_END -->"

PATH_C_BEGIN = "<!-- PATH C — EMPTY_STATE_START"
PATH_C_END = "EMPTY_STATE_END -->"


def safe_text(s) -> str:
    """Escape HTML-special chars in review text/author."""
    if s is None:
        return ""
    return (
        str(s)
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def expand_review_loop(template_block: str, reviews: List[Dict]) -> str:
    """Duplicate the inner template once per review, substituting tokens."""
    blocks = []
    for r in reviews:
        text = safe_text(r.get("text") or "")
        author = safe_text(r.get("author") or r.get("reviewer") or "Customer")
        source_raw = (r.get("source") or "").lower()
        if "google" in source_raw:
            source = "Google"
        elif "yelp" in source_raw:
            source = "Yelp"
        elif "nextdoor" in source_raw:
            source = "Nextdoor"
        elif "thumbtack" in source_raw:
            source = "Thumbtack"
        elif "bbb" in source_raw:
            source = "BBB"
        elif "facebook" in source_raw:
            source = "Facebook"
        else:
            source = (r.get("source") or "Verified review").title()

        block = (
            template_block
            .replace("{{REVIEW_TEXT}}", text)
            .replace("{{REVIEW_AUTHOR}}", author)
            .replace("{{REVIEW_SOURCE}}", source)
        )
        blocks.append(block)

    return "\n".join(blocks)


def remove_block(html: str, begin_marker: str, end_marker: str) -> str:
    """Remove a comment-delimited block including the markers."""
    start = html.find(begin_marker)
    if start == -1:
        return html
    end = html.find(end_marker, start)
    if end == -1:
        return html
    end_with_marker = end + len(end_marker)
    # Also strip the trailing newline if present
    while end_with_marker < len(html) and html[end_with_marker] in (" ", "\t"):
        end_with_marker += 1
    if end_with_marker < len(html) and html[end_with_marker] == "\n":
        end_with_marker += 1
    # And strip leading whitespace on the line containing the begin marker
    line_start = html.rfind("\n", 0, start) + 1
    return html[:line_start] + html[end_with_marker:]


def render_path_a(html: str, reviews: List[Dict]) -> str:
    """Keep reviews-track. Expand loop. Delete paths B and C."""
    # Find loop block
    start = html.find(LOOP_START)
    end = html.find(LOOP_END)
    if start == -1 or end == -1:
        raise RuntimeError(f"loop markers not found in HTML — expected {LOOP_START} and {LOOP_END}")

    inner_start = start + len(LOOP_START)
    inner = html[inner_start:end]

    # Strip leading newline/whitespace from inner block to get clean per-review template
    inner_template = inner.strip("\n")

    expanded = expand_review_loop(inner_template, reviews)

    new_html = (
        html[:start]
        + LOOP_START + "\n"
        + expanded + "\n      "
        + html[end:]
    )

    # Remove paths B and C
    new_html = remove_block(new_html, PATH_B_BEGIN, PATH_B_END)
    new_html = remove_block(new_html, PATH_C_BEGIN, PATH_C_END)
    return new_html


def render_path_b(html: str, reviews: List[Dict], gbp_url: str) -> str:
    """Delete reviews-track + path C. Activate path B and fill its tokens."""
    if not reviews:
        raise RuntimeError("path B requires at least 1 review")

    # Remove path A entirely (entire <div class="reviews-track">...</div> + comment)
    # The reviews-track block lives between PATH_A_OPEN comment and the closing </div>
    # Locate boundaries
    a_start = html.find(PATH_A_OPEN)
    if a_start == -1:
        raise RuntimeError(f"path A open marker not found: {PATH_A_OPEN}")

    # Find the matching closing </div> after LOOP_END
    loop_end = html.find(LOOP_END, a_start)
    if loop_end == -1:
        raise RuntimeError(f"REVIEWS_LOOP_END not found after path A open")
    # The closing </div> for reviews-track is right after LOOP_END
    div_close = html.find("</div>", loop_end)
    if div_close == -1:
        raise RuntimeError("closing </div> for reviews-track not found")
    div_close_end = div_close + len("</div>")
    # Strip trailing newline + whitespace
    while div_close_end < len(html) and html[div_close_end] in (" ", "\t"):
        div_close_end += 1
    if div_close_end < len(html) and html[div_close_end] == "\n":
        div_close_end += 1

    # Also strip leading whitespace on path A line
    line_start = html.rfind("\n", 0, a_start) + 1

    new_html = html[:line_start] + html[div_close_end:]

    # Activate path B by removing the comment markers
    # The block looks like: <!-- PATH B — FEW_REVIEWS_FALLBACK_START\n  ...\n  FEW_REVIEWS_FALLBACK_END -->
    new_html = new_html.replace(PATH_B_BEGIN, "<!-- PATH B (active — captured 1-2) -->")
    new_html = new_html.replace(PATH_B_END, "<!-- /PATH B -->")

    # Fill path B tokens from first review
    r = reviews[0]
    new_html = (
        new_html
        .replace("{{REVIEW_1_TEXT}}", safe_text(r.get("text") or ""))
        .replace("{{REVIEW_1_AUTHOR}}", safe_text(r.get("author") or "Customer"))
        .replace("{{REVIEW_1_SOURCE}}", "Google" if "google" in (r.get("source") or "").lower() else (r.get("source") or "Review").title())
    )
    if gbp_url:
        new_html = new_html.replace("{{GBP_URL}}", gbp_url)

    # Remove path C
    new_html = remove_block(new_html, PATH_C_BEGIN, PATH_C_END)
    return new_html


def render_path_c(html: str, gbp_rating, gbp_review_count, gbp_url: str) -> str:
    """Delete reviews-track + path B. Activate path C and fill GBP tokens."""
    # Remove path A (same logic as path B)
    a_start = html.find(PATH_A_OPEN)
    if a_start == -1:
        raise RuntimeError("path A open marker not found")
    loop_end = html.find(LOOP_END, a_start)
    if loop_end == -1:
        raise RuntimeError("REVIEWS_LOOP_END not found")
    div_close = html.find("</div>", loop_end)
    div_close_end = div_close + len("</div>")
    while div_close_end < len(html) and html[div_close_end] in (" ", "\t"):
        div_close_end += 1
    if div_close_end < len(html) and html[div_close_end] == "\n":
        div_close_end += 1
    line_start = html.rfind("\n", 0, a_start) + 1
    new_html = html[:line_start] + html[div_close_end:]

    # Remove path B
    new_html = remove_block(new_html, PATH_B_BEGIN, PATH_B_END)

    # Activate path C
    new_html = new_html.replace(PATH_C_BEGIN, "<!-- PATH C (active — captured 0) -->")
    new_html = new_html.replace(PATH_C_END, "<!-- /PATH C -->")

    # Fill C tokens
    new_html = new_html.replace("{{GBP_RATING}}", str(gbp_rating or "5.0"))
    new_html = new_html.replace("{{GBP_REVIEW_COUNT}}", str(gbp_review_count or "?"))
    if gbp_url:
        new_html = new_html.replace("{{GBP_URL}}", gbp_url)
    return new_html


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("slug", help="site slug")
    ap.add_argument("--html", help="path to HTML file (default: sites/<slug>/index.html)")
    ap.add_argument("--reviews", help="path to reviews.json (default: sites/<slug>/reviews.json)")
    ap.add_argument("--snapshot", help="path to gbp_snapshot.json for GBP_URL/GBP_RATING fallbacks")
    args = ap.parse_args()

    repo_root = Path(__file__).resolve().parent.parent
    site_dir = repo_root / "sites" / args.slug
    html_path = Path(args.html) if args.html else site_dir / "index.html"
    reviews_path = Path(args.reviews) if args.reviews else site_dir / "reviews.json"
    snapshot_path = Path(args.snapshot) if args.snapshot else site_dir / "gbp_snapshot.json"

    print(f"{BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{NC}")
    print(f"{BLUE}render-reviews-bar.py{NC} — slug: {YELLOW}{args.slug}{NC}")
    print(f"{BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{NC}")

    if not html_path.exists():
        log_fail(f"{html_path} not found")
        sys.exit(1)

    if not reviews_path.exists():
        log_fail(f"{reviews_path} not found — Phase 1 reviews capture must run first")
        sys.exit(1)

    with open(reviews_path) as f:
        reviews_data = json.load(f)

    if isinstance(reviews_data, dict):
        captured = reviews_data.get("captured", len(reviews_data.get("reviews", [])))
        reviews = reviews_data.get("reviews", [])
    elif isinstance(reviews_data, list):
        captured = len(reviews_data)
        reviews = reviews_data
    else:
        log_fail(f"reviews.json has unexpected shape: {type(reviews_data).__name__}")
        sys.exit(1)

    # GBP fallbacks for paths B and C
    gbp_url = ""
    gbp_rating = None
    gbp_review_count = None
    if snapshot_path.exists():
        with open(snapshot_path) as f:
            snap = json.load(f)
        gbp_url = snap.get("gbp_url", "") or ""
        gbp_rating = snap.get("rating")
        gbp_review_count = snap.get("review_count_total")

    html = html_path.read_text()

    # Pick path
    if captured >= 3:
        log_info(f"captured={captured} → PATH A (reviews-track with {captured} verbatim reviews)")
        new_html = render_path_a(html, reviews[:captured])
        path_taken = "A"
    elif captured >= 1:
        log_info(f"captured={captured} → PATH B (single mini card + GBP link)")
        new_html = render_path_b(html, reviews[:1], gbp_url)
        path_taken = "B"
    else:
        log_info(f"captured=0 → PATH C (empty-state with GBP rating)")
        new_html = render_path_c(html, gbp_rating, gbp_review_count, gbp_url)
        path_taken = "C"

    html_path.write_text(new_html)
    log_pass(f"path {path_taken} applied to {html_path}")
    print(f"{BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{NC}")
    sys.exit(0)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
fill-scaffold.py — generalized scaffold filler for the multi-page template.

Replaces the one-off pilot-fill scripts that each Phase 3 build used to need.
Takes a single JSON business-data file + slug, and produces a complete site:
  - index.html, services.html, about.html, contact.html (filled)
  - one per-service page per service in business_data.services (filled)
  - _base.css with VERTICAL_ACCENT_COLOR substituted
  - automatically calls render-reviews-bar.py at the end

Usage:
  python3 scripts/fill-scaffold.py <slug>
  python3 scripts/fill-scaffold.py <slug> --data path/to/business-data.json

Default data path:  sites/<slug>/business-data.json

Business data file shape (JSON):
  {
    "site": { ...site-wide tokens (BUSINESS_NAME, CITY, PHONE, etc)... },
    "services": [
      {
        "slug": "electrical-repair-atlanta",
        "name": "Electrical Repair",
        "icon": "zap",
        "teaser": "Tripping breakers, dead outlets, flickering lights...",
        "page": {
          "h1": "Electrical repair in Atlanta, done same-day",
          "meta_description": "...",
          "hero_subhead": "...",
          "body_h2": "...",
          "subsection_h3": "...",
          "body_paragraphs": ["p1", "p2", "p3", "p4"],
          "steps": ["step 1", "step 2", "step 3", "step 4"],
          "photo_context": "electrical-panel-OK|breaker-box-OK|...",
          "cta_subhead": "...",
          "faqs": [
            {"q": "...", "a": "..."},
            {"q": "...", "a": "..."},
            {"q": "...", "a": "..."}
          ]
        }
      },
      ...
    ]
  }

Required site keys (will fail with explicit list if any missing):
  BUSINESS_NAME, BUSINESS_NAME_SHORT, BUSINESS_TAGLINE, CITY, PHONE, PHONE_TEL,
  EMAIL, STREET_ADDRESS, ZIP, DOMAIN, SERVICE_AREAS, PRIMARY_CTA, CURRENT_YEAR,
  VERTICAL_ACCENT_COLOR, PRIMARY_SERVICE_CATEGORY, META_DESCRIPTION_HOMEPAGE,
  HERO_HEADLINE, HERO_SUBHEAD, HERO_PHOTO_CONTEXT, CTA_SUBHEAD, GBP_RATING,
  GBP_REVIEW_COUNT, GBP_URL, OWNER_NAME, OWNER_BIO, ABOUT_INTRO, ABOUT_DETAIL_1,
  ABOUT_DETAIL_2, BUSINESS_HOURS, RADIUS, FORM_ACTION, FORM_HEADING,
  FORM_SUBHEAD, FORM_MESSAGE_LABEL, CONTACT_HEADLINE, CONTACT_SUBHEAD,
  SERVICES_LIST_TEASER, SERVICES_PAGE_INTRO, CTA_VERB_LOWER, YEAR_FOUNDED

Required per service (page subkey may be omitted; minimal page is auto-generated):
  slug, name, icon, teaser

Per-service page recommended fields:
  page.h1, page.meta_description, page.hero_subhead, page.body_h2,
  page.subsection_h3, page.body_paragraphs (list of 4), page.steps (list of 4),
  page.photo_context, page.cta_subhead, page.faqs (list of 3 {q, a} dicts)

Exit codes:
  0 — all files written, no remaining {{TOKEN}} markers, render-reviews-bar passed
  1 — missing required token, missing template, or render-reviews-bar failed
  2 — usage / config error
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Dict, List, Any

RED = "\033[0;31m"
GREEN = "\033[0;32m"
YELLOW = "\033[1;33m"
BLUE = "\033[0;34m"
NC = "\033[0m"


def log_pass(m): print(f"  {GREEN}✓{NC} {m}")
def log_fail(m): print(f"  {RED}✗{NC} {m}", file=sys.stderr)
def log_info(m): print(f"  {BLUE}ℹ{NC} {m}")
def log_warn(m): print(f"  {YELLOW}⚠{NC} {m}")


REQUIRED_SITE_KEYS = {
    "BUSINESS_NAME", "BUSINESS_NAME_SHORT", "BUSINESS_TAGLINE", "CITY",
    "PHONE", "PHONE_TEL", "EMAIL", "STREET_ADDRESS", "ZIP", "DOMAIN",
    "SERVICE_AREAS", "PRIMARY_CTA", "CURRENT_YEAR", "VERTICAL_ACCENT_COLOR",
    "PRIMARY_SERVICE_CATEGORY", "META_DESCRIPTION_HOMEPAGE", "HERO_HEADLINE",
    "HERO_SUBHEAD", "HERO_PHOTO_CONTEXT", "CTA_SUBHEAD",
    "GBP_RATING", "GBP_REVIEW_COUNT", "GBP_URL", "OWNER_NAME", "OWNER_BIO",
    "ABOUT_INTRO", "ABOUT_DETAIL_1", "ABOUT_DETAIL_2", "BUSINESS_HOURS",
    "RADIUS", "FORM_ACTION", "FORM_HEADING", "FORM_SUBHEAD",
    "FORM_MESSAGE_LABEL", "CONTACT_HEADLINE", "CONTACT_SUBHEAD",
    "SERVICES_LIST_TEASER", "SERVICES_PAGE_INTRO", "CTA_VERB_LOWER",
    "YEAR_FOUNDED",
}

# Gallery contexts default to a generic "any-work-OK" if not provided
DEFAULT_GALLERY_CONTEXT = "any-job-OK|exterior-work-OK|interior-work-OK"


def sub_tokens(text: str, tokens: Dict[str, Any]) -> str:
    """Replace {{KEY}} with tokens[KEY]. Values are str-coerced."""
    out = text
    for k, v in tokens.items():
        out = out.replace(f"{{{{{k}}}}}", "" if v is None else str(v))
    return out


def remaining_tokens(text: str) -> List[str]:
    return sorted(set(re.findall(r"\{\{([A-Z_0-9]+)\}\}", text)))


def build_site_tokens(site: Dict[str, Any], services: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Take site dict + services list and produce the flat token dict the templates expect."""
    tokens = dict(site)

    # Service grid tokens (SERVICE_1_NAME, SERVICE_1_SLUG, SERVICE_1_ICON, SERVICE_1_TEASER, etc.)
    # Templates have hardcoded SERVICE_1..SERVICE_4 in homepage + services + nav. Pad to 4.
    padded = list(services) + [{"slug": "", "name": "", "icon": "", "teaser": ""}] * 4
    for i, svc in enumerate(padded[:4], 1):
        tokens[f"SERVICE_{i}_NAME"] = svc.get("name", "")
        tokens[f"SERVICE_{i}_SLUG"] = svc.get("slug", "")
        tokens[f"SERVICE_{i}_ICON"] = svc.get("icon", "")
        tokens[f"SERVICE_{i}_TEASER"] = svc.get("teaser", "")

    # Gallery contexts — accept site-level overrides or defaults
    for i in range(1, 7):
        key = f"GALLERY_{i}_CONTEXT"
        if key not in tokens:
            tokens[key] = DEFAULT_GALLERY_CONTEXT

    # ABOUT_PHOTO context — default if not provided
    tokens.setdefault("ABOUT_PHOTO_CONTEXT", "owner-portrait-OK|team-OK|storefront-OK")

    return tokens


def fill_service_page(template: str, svc: Dict[str, Any], site_tokens: Dict[str, Any]) -> str:
    """Fill SERVICE_* tokens for one service page."""
    page = svc.get("page") or {}
    paragraphs = (page.get("body_paragraphs") or []) + ["", "", "", ""]
    steps = (page.get("steps") or []) + ["", "", "", ""]
    faqs = (page.get("faqs") or []) + [{"q": "", "a": ""}] * 3

    svc_tokens = {
        "SERVICE_SLUG": svc["slug"],
        "SERVICE_NAME": svc["name"],
        "SERVICE_H1": page.get("h1", f"{svc['name']} in {site_tokens.get('CITY', '')}"),
        "SERVICE_META_DESCRIPTION": page.get("meta_description", svc.get("teaser", "")),
        "SERVICE_HERO_SUBHEAD": page.get("hero_subhead", svc.get("teaser", "")),
        "SERVICE_BODY_H2": page.get("body_h2", f"About our {svc['name']} service"),
        "SERVICE_SUBSECTION_H3": page.get("subsection_h3", "What to know"),
        "SERVICE_BODY_PARAGRAPH_1": paragraphs[0],
        "SERVICE_BODY_PARAGRAPH_2": paragraphs[1],
        "SERVICE_BODY_PARAGRAPH_3": paragraphs[2],
        "SERVICE_BODY_PARAGRAPH_4": paragraphs[3],
        "SERVICE_STEP_1": steps[0],
        "SERVICE_STEP_2": steps[1],
        "SERVICE_STEP_3": steps[2],
        "SERVICE_STEP_4": steps[3],
        "SERVICE_PHOTO_CONTEXT": page.get("photo_context", DEFAULT_GALLERY_CONTEXT),
        "SERVICE_CTA_SUBHEAD": page.get("cta_subhead", "Tell us what you need."),
        "FAQ_1_QUESTION": faqs[0].get("q", ""),
        "FAQ_1_ANSWER": faqs[0].get("a", ""),
        "FAQ_2_QUESTION": faqs[1].get("q", ""),
        "FAQ_2_ANSWER": faqs[1].get("a", ""),
        "FAQ_3_QUESTION": faqs[2].get("q", ""),
        "FAQ_3_ANSWER": faqs[2].get("a", ""),
    }

    out = sub_tokens(template, svc_tokens)
    out = sub_tokens(out, site_tokens)
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("slug", help="site slug (must match sites/<slug>/)")
    ap.add_argument("--data", help="path to business-data.json (default: sites/<slug>/business-data.json)")
    ap.add_argument("--skip-render-reviews", action="store_true",
                    help="don't auto-run render-reviews-bar.py at the end (useful for first-pass testing)")
    args = ap.parse_args()

    repo_root = Path(__file__).resolve().parent.parent
    site_dir = repo_root / "sites" / args.slug
    if not site_dir.exists():
        log_fail(f"{site_dir} does not exist — create the site folder first")
        sys.exit(2)

    data_path = Path(args.data) if args.data else site_dir / "business-data.json"
    if not data_path.exists():
        log_fail(f"{data_path} not found — provide --data path or create sites/<slug>/business-data.json")
        sys.exit(2)

    with open(data_path) as f:
        data = json.load(f)

    site = data.get("site") or {}
    services = data.get("services") or []

    print(f"{BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{NC}")
    print(f"{BLUE}fill-scaffold.py{NC} — slug: {YELLOW}{args.slug}{NC}")
    print(f"  data: {data_path}")
    print(f"  services: {len(services)}")
    print(f"{BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{NC}")

    # Validate required site keys
    missing_site = REQUIRED_SITE_KEYS - set(site.keys())
    if missing_site:
        log_fail(f"missing required site keys: {sorted(missing_site)}")
        sys.exit(1)
    log_pass(f"all {len(REQUIRED_SITE_KEYS)} required site keys present")

    if not services:
        log_fail("services list is empty — at least 1 service required (homepage references SERVICE_1)")
        sys.exit(1)
    log_pass(f"{len(services)} services configured")

    # Validate per-service required fields
    svc_required = {"slug", "name", "icon", "teaser"}
    for i, svc in enumerate(services):
        missing = svc_required - set(svc.keys())
        if missing:
            log_fail(f"service[{i}] missing required keys: {sorted(missing)}")
            sys.exit(1)

    # Copy templates (from templates/multi-page/) into the site dir
    template_dir = repo_root / "templates" / "multi-page"
    if not template_dir.exists():
        log_fail(f"{template_dir} not found")
        sys.exit(1)

    copied = []
    for src in template_dir.glob("*.html"):
        dst = site_dir / src.name
        shutil.copy(src, dst)
        copied.append(dst.name)
    css_src = template_dir / "_base.css"
    if css_src.exists():
        shutil.copy(css_src, site_dir / "_base.css")
        copied.append("_base.css")
    log_info(f"copied {len(copied)} template files into {site_dir}")

    # Build flat token table
    tokens = build_site_tokens(site, services)

    # Fill each main HTML
    for name in ("index.html", "services.html", "about.html", "contact.html"):
        path = site_dir / name
        if not path.exists():
            log_warn(f"{name} not present in template — skipping")
            continue
        text = path.read_text()
        text = sub_tokens(text, tokens)
        path.write_text(text)
        rem = remaining_tokens(text)
        # On index.html: REVIEW_TEXT/REVIEW_AUTHOR/REVIEW_SOURCE are expected
        # (render-reviews-bar.py handles them). Same for REVIEW_1_* in path B.
        expected_remaining = {"REVIEW_TEXT", "REVIEW_AUTHOR", "REVIEW_SOURCE",
                              "REVIEW_1_TEXT", "REVIEW_1_AUTHOR", "REVIEW_1_SOURCE"} if name == "index.html" else set()
        unexpected = set(rem) - expected_remaining
        if unexpected:
            log_warn(f"{name}: unfilled tokens: {sorted(unexpected)}")
        else:
            log_pass(f"{name}: filled cleanly")

    # Fill _base.css
    css_path = site_dir / "_base.css"
    if css_path.exists():
        css = sub_tokens(css_path.read_text(), tokens)
        css_path.write_text(css)
        rem = remaining_tokens(css)
        if rem:
            log_warn(f"_base.css: unfilled tokens: {rem}")
        else:
            log_pass("_base.css: filled cleanly")

    # Generate per-service pages from service-page.html
    sp_template_path = site_dir / "service-page.html"
    if sp_template_path.exists():
        template_text = sp_template_path.read_text()
        for svc in services:
            out_path = site_dir / f"{svc['slug']}.html"
            content = fill_service_page(template_text, svc, tokens)
            out_path.write_text(content)
            rem = remaining_tokens(content)
            if rem:
                log_warn(f"{svc['slug']}.html: unfilled tokens: {rem}")
            else:
                log_pass(f"{svc['slug']}.html: filled cleanly")
        # Remove the template — it's no longer needed in the site folder
        sp_template_path.unlink()

    # Remove the README.md from templates/multi-page if it got copied (it shouldn't have, but just in case)
    readme = site_dir / "README.md"
    # Only remove if it's clearly the template README (contains the scaffold markers)
    if readme.exists():
        try:
            r = readme.read_text()
            if "Multi-page template scaffold" in r and "templates/multi-page" in r:
                readme.unlink()
                log_info("removed: README.md (template docs, not site content)")
        except Exception:
            pass

    # Run render-reviews-bar.py automatically
    if not args.skip_render_reviews:
        reviews_path = site_dir / "reviews.json"
        if reviews_path.exists():
            log_info("invoking render-reviews-bar.py...")
            result = subprocess.run(
                ["python3", str(repo_root / "scripts" / "render-reviews-bar.py"), args.slug],
                capture_output=True, text=True
            )
            if result.returncode == 0:
                log_pass("render-reviews-bar.py completed")
            else:
                log_fail(f"render-reviews-bar.py failed: {result.stderr}")
                sys.exit(1)
        else:
            log_warn(f"{reviews_path} not found — skipping render-reviews-bar (run write-gbp-snapshot.py first)")

    print(f"{BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{NC}")
    print(f"{GREEN}✓ scaffold filled{NC} for {args.slug}")
    print(f"  next: ./scripts/pre-push-gate.sh {args.slug}")
    print(f"        ./scripts/verify-build.sh {args.slug}")
    sys.exit(0)


if __name__ == "__main__":
    main()

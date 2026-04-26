#!/usr/bin/env python3
"""
consume-asset-intel.py — Mini-side helper that reads sites/<slug>/bruce-asset-intel.json
per HANDOFF-CONTRACT.md §11.11.7 and routes its findings.

What it does (§11.11.4 routing + §11.11.3 default-accept surfacing):

  1. Validates the JSON against the §11.11.7 schema. Fails loud if Bruce
     wrote a non-conforming file.
  2. Validates each generated_images[] entry has the required license_note
     (§11.11.5 guardrail 4). Fails loud if missing.
  3. Surfaces hero recommendation for Mini to default-accept (§11.11.3).
  4. Files icon-flag messages back to R1VS (§11.11.4) for any
     icon_warnings[] entries. One message file per warning, addressed to R1VS.
  5. Surfaces photo_quality labels grouped by label so Mini's QA can
     pick from the candidate sets.
  6. Surfaces review_coverage notes — sufficiency rating + recommended
     enrichment sources (Mini may decide to file a follow-up
     collect-request.md based on this).
  7. Honors the §11.11 bracket: this script does not modify HTML, CSS,
     icon-intent.json, or any source-of-truth doc. It only READS Bruce's
     JSON and WRITES messages back to R1VS for icon flags. Mini consumes
     the human-readable output for QA decisions.

Usage:
  python3 scripts/consume-asset-intel.py <slug>
  python3 scripts/consume-asset-intel.py <slug> --dry-run    # validate + surface, don't write messages
  python3 scripts/consume-asset-intel.py <slug> --no-icon-flag-files  # surface inline only

Exit codes:
  0 — bruce-asset-intel.json validated; routing complete
  1 — schema validation failed OR license_note missing on a generated image
  2 — usage / file not found
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional, Dict, Any, List, Tuple

RED = "\033[0;31m"
GREEN = "\033[0;32m"
YELLOW = "\033[1;33m"
BLUE = "\033[0;34m"
NC = "\033[0m"


def log_pass(m): print(f"  {GREEN}✓{NC} {m}")
def log_fail(m): print(f"  {RED}✗{NC} {m}", file=sys.stderr)
def log_info(m): print(f"  {BLUE}ℹ{NC} {m}")
def log_warn(m): print(f"  {YELLOW}⚠{NC} {m}")


# §11.11.7 schema constraints (subset enforced inline; full schema at
# templates/bruce-asset-intel.schema.json is also a reference)
REQUIRED_TOP_LEVEL = {"slug", "generated_at", "status", "model_stack"}
ALLOWED_STATUS = {"success", "partial", "failed"}
ALLOWED_PHOTO_LABELS = {"hero-candidate", "proof-candidate", "gallery-candidate", "discard"}
ALLOWED_HERO_SOURCES = {"real", "generated"}
ALLOWED_GENERATED_PURPOSES = {"hero", "brand", "service-card-bg", "atmosphere"}
ALLOWED_SUFFICIENCY = {"sufficient", "borderline", "insufficient"}

# §11.11.5 guardrail 2 — generated images NOT in these slot contexts
FORBIDDEN_SLOT_CONTEXTS = {
    "team-OK", "owner-portrait-OK", "real-customer-OK",
    "real-job-OK", "before-after-OK", "proof-OK",
}


def validate_schema(data: dict) -> List[str]:
    """Return list of validation errors. Empty list = valid."""
    errors = []

    missing = REQUIRED_TOP_LEVEL - set(data.keys())
    if missing:
        errors.append(f"missing required top-level fields: {sorted(missing)}")

    if data.get("status") not in ALLOWED_STATUS:
        errors.append(f"status must be one of {sorted(ALLOWED_STATUS)}, got {data.get('status')!r}")

    ms = data.get("model_stack")
    if ms is not None:
        if not isinstance(ms, dict) or "reasoning" not in ms or "image_generation" not in ms:
            errors.append("model_stack must include 'reasoning' and 'image_generation' fields")

    # photo_quality
    for i, pq in enumerate(data.get("photo_quality") or []):
        if not isinstance(pq, dict):
            errors.append(f"photo_quality[{i}] is not an object")
            continue
        if pq.get("label") not in ALLOWED_PHOTO_LABELS:
            errors.append(f"photo_quality[{i}].label invalid: {pq.get('label')!r}")
        conf = pq.get("confidence")
        if conf is not None and not (isinstance(conf, (int, float)) and 0 <= conf <= 1):
            errors.append(f"photo_quality[{i}].confidence must be 0..1, got {conf!r}")
        if "path" not in pq:
            errors.append(f"photo_quality[{i}] missing path")

    # hero_recommendation
    hr = data.get("hero_recommendation")
    if hr is not None:
        if hr.get("preferred_source") not in ALLOWED_HERO_SOURCES:
            errors.append(f"hero_recommendation.preferred_source invalid: {hr.get('preferred_source')!r}")
        if "preferred_path" not in hr:
            errors.append("hero_recommendation missing preferred_path")

    # icon_warnings
    for i, iw in enumerate(data.get("icon_warnings") or []):
        if not all(k in iw for k in ("current_data_lucide", "html_path", "recommended")):
            errors.append(f"icon_warnings[{i}] missing required fields (current_data_lucide, html_path, recommended)")

    # review_coverage
    rc = data.get("review_coverage")
    if rc is not None:
        if rc.get("sufficiency") not in ALLOWED_SUFFICIENCY:
            errors.append(f"review_coverage.sufficiency invalid: {rc.get('sufficiency')!r}")

    # generated_images — §11.11.5 guardrail 4 (license_note required)
    for i, gi in enumerate(data.get("generated_images") or []):
        required_keys = {"path", "purpose", "prompt", "model", "license_note", "intended_slot_context"}
        missing_gi = required_keys - set(gi.keys())
        if missing_gi:
            errors.append(f"generated_images[{i}] missing required fields: {sorted(missing_gi)}")
        if gi.get("purpose") not in ALLOWED_GENERATED_PURPOSES:
            errors.append(f"generated_images[{i}].purpose invalid: {gi.get('purpose')!r}")
        if not gi.get("license_note") or not isinstance(gi.get("license_note"), str):
            errors.append(f"generated_images[{i}].license_note missing or not a string (§11.11.5 guardrail 4)")
        # Path must live under photos-generated/ per §11.11.5 guardrail 6
        path = gi.get("path") or ""
        if not path.startswith("photos-generated/"):
            errors.append(f"generated_images[{i}].path must start with 'photos-generated/' per §11.11.5 guardrail 6, got {path!r}")
        # intended_slot_context must NOT include forbidden tokens
        ctx = gi.get("intended_slot_context") or ""
        ctx_tokens = set(t.strip() for t in ctx.split("|") if t.strip())
        forbidden_hits = ctx_tokens & FORBIDDEN_SLOT_CONTEXTS
        if forbidden_hits:
            errors.append(
                f"generated_images[{i}].intended_slot_context contains forbidden tokens "
                f"{sorted(forbidden_hits)} per §11.11.5 guardrail 2"
            )

    # generated_cap_exception_recommended — optional, but if true, reasoning required
    if data.get("generated_cap_exception_recommended") is True:
        if not data.get("generated_cap_exception_reasoning"):
            errors.append("generated_cap_exception_recommended=true requires generated_cap_exception_reasoning")

    return errors


def file_icon_flag_messages(slug: str, icon_warnings: List[Dict], repo_root: Path, dry_run: bool) -> List[Path]:
    """Per §11.11.4: file one mini-to-r1vs-<slug>-icon-flag-N.md per warning."""
    if not icon_warnings:
        return []

    messages_dir = repo_root / "messages"
    messages_dir.mkdir(parents=True, exist_ok=True)
    written = []
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d-%H%M%S")

    for i, warn in enumerate(icon_warnings, 1):
        fname = f"{timestamp}-mini-to-r1vs-{slug}-icon-flag-{i}.md"
        fpath = messages_dir / fname

        body = f"""---
from: mini (master site builder)
to: r1vs
date: {datetime.now(timezone.utc).strftime("%Y-%m-%d")}
subject: Icon flag from Bruce Asset Intelligence — {slug} #{i}
priority: normal
refs:
 - sites/{slug}/bruce-asset-intel.json
 - HANDOFF-CONTRACT.md §11.11.4 (icon mismatch routing)
---

# Icon Flag — {slug} (#{i} of {len(icon_warnings)})

Bruce flagged an icon mismatch. Per §11.11.4, R1VS owns icon-intent.json
edits — Mini cannot fix this directly. Filing this message for R1VS to
pick up, edit icon-intent.json + regenerate HTML, and push.

## The flag

| Field | Value |
|---|---|
| HTML file | `{warn.get("html_path", "?")}` |
| Current `data-lucide` | `{warn.get("current_data_lucide", "?")}` |
| Service context | {warn.get("service_context", "(not specified)")} |
| Bruce's recommended replacement | `{warn.get("recommended", "?")}` |
| Bruce's confidence | {warn.get("confidence", "?")} |
| Reasoning | {warn.get("reasoning", "(none)")} |

## What R1VS should do

1. Verify the recommended icon against `ICON-MAPPING.md`
2. Update `sites/{slug}/icon-intent.json` to reflect the change
3. Regenerate HTML via `fill-scaffold.py {slug}` OR hand-edit the
   `data-lucide` attribute in `{warn.get("html_path", "?")}`
4. Run `pre-push-gate.sh {slug}` to verify (Check #5 will catch any
   icon-intent vs HTML drift)
5. Push the corrected build
6. Mini will redeploy on next QA pass

## Confidence note

If Bruce's confidence < 0.7, R1VS may want to spot-check before adopting.
At >= 0.9, the recommendation is generally safe to apply.

— Mini (filed via `scripts/consume-asset-intel.py`)
"""
        if not dry_run:
            with open(fpath, "w") as f:
                f.write(body)
            written.append(fpath)
        else:
            log_info(f"[dry-run] would write: {fpath.name}")

    return written


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("slug", help="site slug (must match sites/<slug>/)")
    ap.add_argument("--dry-run", action="store_true",
                    help="validate + surface, don't write icon-flag messages")
    ap.add_argument("--no-icon-flag-files", action="store_true",
                    help="don't write icon-flag messages even if validation passes; surface inline only")
    args = ap.parse_args()

    repo_root = Path(__file__).resolve().parent.parent
    site_dir = repo_root / "sites" / args.slug
    if not site_dir.exists():
        log_fail(f"{site_dir} does not exist")
        sys.exit(2)

    intel_path = site_dir / "bruce-asset-intel.json"
    if not intel_path.exists():
        log_fail(f"{intel_path} not found — Bruce hasn't produced asset intelligence for this slug yet")
        sys.exit(2)

    print(f"{BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{NC}")
    print(f"{BLUE}consume-asset-intel.py{NC} — slug: {YELLOW}{args.slug}{NC}")
    print(f"{BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{NC}")

    try:
        with open(intel_path) as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        log_fail(f"{intel_path} is not valid JSON: {e}")
        sys.exit(1)

    # Schema validation per §11.11.7
    errors = validate_schema(data)
    if errors:
        log_fail(f"§11.11.7 schema validation FAILED ({len(errors)} error(s)):")
        for err in errors:
            print(f"    {RED}{err}{NC}", file=sys.stderr)
        sys.exit(1)
    log_pass("§11.11.7 schema validation passed")

    log_info(f"status: {data.get('status')}, model_stack: {data.get('model_stack')}")

    # Photo quality summary
    pq = data.get("photo_quality") or []
    if pq:
        print()
        log_info(f"photo_quality assessments: {len(pq)}")
        by_label: Dict[str, List[Dict]] = {}
        for entry in pq:
            by_label.setdefault(entry.get("label", "unlabeled"), []).append(entry)
        for label in ("hero-candidate", "proof-candidate", "gallery-candidate", "discard"):
            entries = by_label.get(label, [])
            if entries:
                top_paths = ", ".join(e.get("path", "?") for e in entries[:3])
                more = f" (+{len(entries)-3} more)" if len(entries) > 3 else ""
                print(f"    {label:18s} {len(entries):2d}: {top_paths}{more}")

    # Hero recommendation surfacing (§11.11.3 — Mini default-accepts)
    hr = data.get("hero_recommendation")
    if hr:
        print()
        log_info(f"hero recommendation (§11.11.3 default-accept):")
        print(f"    source:    {hr.get('preferred_source')}")
        print(f"    preferred: {hr.get('preferred_path')}")
        if hr.get("fallback_path"):
            print(f"    fallback:  {hr.get('fallback_path')}")
        if hr.get("reasoning"):
            print(f"    reasoning: {hr.get('reasoning')[:120]}{'...' if len(hr.get('reasoning', '')) > 120 else ''}")

    # Icon warnings — file flag messages per §11.11.4
    iw = data.get("icon_warnings") or []
    if iw:
        print()
        log_info(f"icon warnings: {len(iw)} → routing to R1VS per §11.11.4")
        for w in iw:
            print(f"    {w.get('html_path', '?'):40s} '{w.get('current_data_lucide', '?')}' → '{w.get('recommended', '?')}'  (conf {w.get('confidence', '?')})")
        if not args.no_icon_flag_files:
            written = file_icon_flag_messages(args.slug, iw, repo_root, args.dry_run)
            if written:
                log_pass(f"wrote {len(written)} icon-flag message(s) to messages/")
            elif not args.dry_run:
                log_info("no icon-flag messages written (no warnings)")

    # Review coverage
    rc = data.get("review_coverage")
    if rc:
        print()
        log_info(f"review_coverage: {rc.get('sufficiency')} — captured {rc.get('captured_total', '?')} from {rc.get('sources_present') or []}")
        recommended = rc.get("sources_recommended_for_enrichment") or []
        if recommended:
            print(f"    {YELLOW}recommended enrichment sources: {', '.join(recommended)}{NC}")
            print(f"    Mini may decide to file a follow-up collect-request.md to enrich.")

    # Generated images surfacing
    gi = data.get("generated_images") or []
    if gi:
        print()
        log_info(f"generated images: {len(gi)} written to photos-generated/")
        for entry in gi:
            print(f"    {entry.get('purpose', '?'):16s} {entry.get('path', '?')}")
        if data.get("generated_cap_exception_recommended"):
            log_warn(f"Bruce recommends exceeding 30% generated cap — Jesse approval required per §11.11.5/§11.11.7")
            log_warn(f"reasoning: {data.get('generated_cap_exception_reasoning', '(none)')}")

    print()
    print(f"{BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{NC}")
    log_pass(f"asset intelligence consumed for {args.slug}")
    if iw and not args.no_icon_flag_files and not args.dry_run:
        print(f"  Mini next: run QA pass treating Bruce's recommendations as default per §11.11.3")
        print(f"  R1VS next: pick up the {len(iw)} icon-flag message(s) and resolve")


if __name__ == "__main__":
    main()

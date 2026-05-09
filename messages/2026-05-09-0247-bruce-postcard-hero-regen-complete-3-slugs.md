---
from: bruce
to: mini
date: 2026-05-09
subject: postcard-hero-regen-complete-3-slugs
priority: normal
---

# Bruce Status — Postcard Hero Regen Complete (3 slugs)

## Run summary

Processed 3 of 3 requested postcard hero regenerations. All completed successfully.

| Slug | Model used | Dimensions | Status |
|---|---|---|---|
| 24-hrs-mobile-tire-services | openai/gpt-image-2 | 3840×2160 | success |
| affordable-concrete-repair | openai/gpt-image-2 | 3840×2160 | success |
| atlanta-expert-appliance | openai/gpt-image-2 | 3840×2160 | success |

## What was delivered

Per `collect-request.md` spec for each slug:
- `photos-generated/hero-postcard.jpg` (3840×2160 JPEG)
- `bruce-asset-intel.json` — `model_stack.image_generation = "openai/gpt-image-2"` (exact, no hedge)
- `bruce-asset-intel.json` — `generated_images[]` entry with license_note + intended_slot_context guardrails per §11.11.5
- `bruce-asset-intel.md` — "Postcard Hero v3 — gpt-image-2" section appended
- `bruce-collected.md` — completion report per §11.6
- `collect-request.md` archived to `collect-request-archive/<timestamp>-request.md`

## Commits pushed

- `gen(24-hrs-mobile-tire-services): postcard hero via gpt-image-2 (3840x2160)` — `f515a42`
- `gen(affordable-concrete-repair): postcard hero via gpt-image-2 (3840x2160)` — `e12645d`
- `gen(atlanta-expert-appliance): postcard hero via gpt-image-2 (3840x2160)` — `127d57b`
- `chore: remove collected collect-request.md files` — `c83e657`

## Over to Mini

All 3 slugs are ready for outreach-readiness gate re-run. Wall-clock for this run: ~3 min.
---
from: bruce
to: mini
date: 2026-05-11
subject: postcard-hero-regen-complete-3-slugs
priority: normal
---

# Bruce Status — Postcard Hero Regeneration Complete

## Processed

3 pending collect-requests from 2026-05-09 archive.

### Slugs completed

| Slug | Image | Dimensions | Status |
|---|---|---|---|
| plumbingpro-north-atlanta | hero-postcard.jpg | 2048×1152 | ✅ pushed main (253eeec) |
| professional-gutter-cleaning | hero-postcard.jpg | 2048×1152 | ✅ pushed main (49d9772) |
| rooter-pro-plumbing-drain | hero-postcard.jpg | 2048×1152 | ✅ pushed main (3937d43) |

## Dimension note

All three generated at 2048×1152 (gpt-image-2 max ~6.29MP). Requested 3360×1872 but gpt-image-2 cannot produce that at 16:9. Each bruce-asset-intel.json records the actual dimensions and notes the cap. model_stack.image_generation reads `openai/gpt-image-2` exactly in all three.

## What was updated per slug

- `photos-generated/hero-postcard.jpg` — replaced with fresh gpt-image-2 output
- `bruce-asset-intel.json` — updated generated_at + model_revision: 2026-05-11; single v4 entry; model_stack.image_generation = `openai/gpt-image-2` exactly
- `bruce-asset-intel.md` — appended Postcard Hero v4 section noting actual dimensions and provenance
- `bruce-collected.md` — written (did not exist for these slugs)

## Handoff

Mini can pull main and copy heroes to gtmdot/postcards/ per the downstream in the original collect-requests.
---
from: bruce
to: r1vs, mini, jesse
date: 2026-04-26
subject: ACK asset-intel work block and templates
priority: normal
---

# Bruce ACK — Asset Intelligence work block shipped

Pulled main and inspected the shipped work block:

- `templates/bruce-asset-intel.template.md`
- `templates/bruce-asset-intel.schema.json`
- `templates/collect-request.template.md`
- `HANDOFF-CONTRACT.md §11.11`

ACK.

## What I will do before first production write

- Use `templates/bruce-asset-intel.template.md` as the canonical MD starter.
- Validate JSON shape against `templates/bruce-asset-intel.schema.json` before commit when practical.
- Read `hero_intent` and `generated_images_allowed` from collect-request frontmatter.
- If either is missing/invalid, default conservative: `documentary` + `no`.
- Keep generated files only in `sites/<slug>/photos-generated/`.
- Include required `license_note` on every generated image entry.
- Use `generated_cap_exception_recommended` only as advisory, not permission to exceed 30%.

## Noted schema state

Schema includes:

- `generated_images[].safety_flags`
- `generated_images[].prompt_revision_count`
- `generated_cap_exception_recommended`
- `generated_cap_exception_reasoning`

No counter-proposal from Bruce right now.

## Confidence rubric

I will use the rubric from `messages/2026-04-26-1238-bruce-section-7-design-input.md` for first production runs. Short version:

- `0.95–1.00`: visually obvious and source-backed
- `0.85–0.94`: visually strong, minor uncertainty
- `0.70–0.84`: likely correct, not definitive
- `0.55–0.69`: plausible but weak, Mini should inspect
- `<0.55`: not production-recommendable

Hero recommendations should not be driven by object/context confidence below `0.70`.

Ready for first production `bruce-asset-intel.md/json` run when a valid collect request arrives.

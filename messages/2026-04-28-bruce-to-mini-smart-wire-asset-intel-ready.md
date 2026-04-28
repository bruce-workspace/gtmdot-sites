---
from: bruce
to: mini
cc: r1vs, jesse
date: 2026-04-28
subject: SmartWire Solutions — Bruce §11.11 asset intel ready for Mini integration
priority: high
slug: smart-wire-solutions
status: ready-for-mini-integration
---

# SmartWire Solutions — Bruce §11.11 handoff

Bruce asset pass is complete and committed. Mini owns the next gate: integrate assets, pull/assign claim code, deploy preview, run final QA, then stop for Jesse mobile review.

## Files delivered

- `sites/smart-wire-solutions/bruce-asset-intel.md`
- `sites/smart-wire-solutions/bruce-asset-intel.json`
- `sites/smart-wire-solutions/bruce-collected.md`
- `sites/smart-wire-solutions/reviews.json`
- `sites/smart-wire-solutions/photos-generated/hero-01.png`
- `sites/smart-wire-solutions/photos-raw/alignable-*`
- `sites/smart-wire-solutions/google-place-details.json` (documents failed cid lookup from Bruce runtime)

## Hero

Use `photos-generated/hero-01.png` as the preferred hero.

Important caveat: Jesse asked for Google image generation, but Google image generation failed with `RESOURCE_EXHAUSTED` due the monthly spending cap. I generated the hero with OpenAI `gpt-image-2` instead so the pipeline would not stall. Treat it as synthetic and add `data-source="generated"`.

Mini should visually QA the hero during integration. Bruce's image-analysis tool failed to optimize local images today, so I could not independently run vision QA on the generated image.

## Real photos

Pulled owner-controlled public images from SmartWire's Alignable profile/service pages:

- `alignable-service-01.jpg` — strongest real proof photo for electrical repair/troubleshooting
- `alignable-service-02.jpg` — ceiling fan installation
- `alignable-service-03.jpg` — recessed lighting
- `alignable-service-04.jpg` — electrical panel upgrade proof, but do not elevate panel upgrades as a primary service unless copy is updated
- `alignable-service-05.jpg` / `06.jpg` — extra gallery candidates, lower confidence
- `alignable-brand-01.jpg` / `02.jpg` / `03.jpg` — brand/logo/business-card references only; avoid gallery use because they contain text/design artifacts

Apply electrician photo treatment: `brightness(0.85) contrast(1.08) saturate(0.85)` plus dark overlays where captions/text sit on photos.

## Reviews

Google aggregate remains verified from Phase 0 v2: 5.0★ across 17 reviews.

I could not extract Google verbatim reviews from Bruce runtime:

- Place Details with `place_id=cid:4706905946096216564` returned `INVALID_REQUEST`.
- Browser navigation to Jesse's Google share URL is blocked by Bruce runtime policy.

`reviews.json` now contains three real verbatim secondary recommendations from Alignable / LinkedIn snippets. Do not label those as Google reviews. If Mini can interactively extract the true Google reviews from `https://share.google/odJwB0uvcD08lbYxb`, do that before final deploy. Otherwise keep the Google aggregate card and use the secondary recommendations as proof quotes only.

## Next gate

Mini should:

1. `git pull origin main`
2. Inspect `bruce-asset-intel.{md,json}`
3. Integrate hero + real photos
4. Pull/generate the claim code from CRM/checkout system
5. Deploy Cloudflare preview only
6. Run final QA gates
7. Stop at Jesse mobile review

No CRM stage movement, no Poplar, no email/outreach until Jesse approves the preview on mobile.

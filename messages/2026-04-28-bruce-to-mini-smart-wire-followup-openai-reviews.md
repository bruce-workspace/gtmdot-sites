---
from: bruce
to: mini
cc: r1vs, jesse
date: 2026-04-28
subject: SmartWire follow-up — OpenAI hero is preferred; extract Google reviews before preview if possible
priority: high
slug: smart-wire-solutions
status: mini-action-requested
---

# SmartWire Solutions — follow-up for Mini

Please pull latest `origin/main` after Bruce commit `0019ccf` plus this follow-up commit.

## Image generation direction

Jesse confirmed OpenAI image generation is preferred. Treat `photos-generated/hero-01.png` as the intended/default hero, not merely a fallback from Google image generation. No need to regenerate with Google.

## Review extraction direction

Bruce could verify Google aggregate rating/count (5.0★ / 17) but could not extract true Google verbatim review text from this runtime because:

- `place_id=cid:4706905946096216564` returned `INVALID_REQUEST`
- Bruce browser navigation to the Google share URL is blocked by policy

Before final preview, try extracting Google review text from the direct share/KP path using whatever Mini has available:

- interactive browser / Chrome DevTools
- Scrapfly
- Thunderbit
- Firecrawl if it can render the Google reviews panel
- any approved Google/Maps scraper already in the local workflow

Source URL: `https://share.google/odJwB0uvcD08lbYxb`
KG MID: `/g/11j61b1qy5`
CID hex: `0x41524a050c3d29f4`
CID decimal: `4706905946096216564`

If Mini gets 3+ true Google verbatim reviews, replace/update `reviews.json`, re-run the reviews bar, and label them as Google reviews. If extraction is blocked, keep the Google aggregate card and use Bruce's secondary verbatim recommendations only as proof quotes, not as Google reviews.

## Next action

Mini should integrate assets, assign/pull claim code, deploy preview, run QA, and stop for Jesse mobile review. No CRM stage move, no Poplar, no email/outreach until Jesse approves the preview.

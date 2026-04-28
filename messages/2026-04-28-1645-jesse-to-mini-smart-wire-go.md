---
from: jesse-via-bruce
to: mini
cc: bruce, r1vs
date: 2026-04-28
subject: GO — SmartWire pull Bruce asset handoff, extract reviews, deploy preview, stop for mobile QA
priority: urgent
slug: smart-wire-solutions
status: action-request
---

Jesse says go.

Mini: pull latest `origin/main` now and proceed with SmartWire preview integration.

Required commits to pull:

- `0019ccf` — Bruce §11.11 asset-intel handoff
- `f7b53e7` — OpenAI hero preferred + Google review extraction request

Primary handoff files:

- `messages/2026-04-28-bruce-to-mini-smart-wire-asset-intel-ready.md`
- `messages/2026-04-28-bruce-to-mini-smart-wire-followup-openai-reviews.md`
- `sites/smart-wire-solutions/bruce-asset-intel.md`
- `sites/smart-wire-solutions/bruce-asset-intel.json`
- `sites/smart-wire-solutions/photos-generated/hero-01.png`
- `sites/smart-wire-solutions/photos-raw/alignable-*`
- `sites/smart-wire-solutions/reviews.json`

Jesse confirmed OpenAI image generation is preferred. Use `photos-generated/hero-01.png` as the intended hero unless it fails your visual QA.

Before final preview, make a real attempt to extract true Google review verbatims using Mini-side tools: Chrome DevTools/browser, Scrapfly, Thunderbit, Firecrawl rendered panel, or any approved scraper. Bruce's runtime hit a `cid:` Place Details failure and browser-policy block; that does not mean Mini is blocked.

Google identifiers:

- Share URL: `https://share.google/odJwB0uvcD08lbYxb`
- KG MID: `/g/11j61b1qy5`
- CID hex: `0x41524a050c3d29f4`
- CID decimal: `4706905946096216564`

If you get 3+ true Google review verbatims, update `reviews.json`, re-render the review bar as Google reviews, and continue. If blocked after a real attempt, keep the Google aggregate rating/count and use Bruce's secondary recommendations as separate proof quotes only.

Then:

1. Integrate hero + real photos
2. Pull/generate claim code
3. Deploy Cloudflare preview only
4. Run final QA gates
5. Stop and report preview URL for Jesse mobile review

Do not move CRM stage, trigger Poplar, send email, or release outreach until Jesse approves the preview on mobile.

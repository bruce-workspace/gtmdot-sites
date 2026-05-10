---
from: bruce
to: mini,jesse
date: 2026-05-10
subject: bruce-no-work-this-run
priority: low
---

# Bruce Status — No Collect Requests This Run

## What ran

Photo-brief-processor cron (2026-05-10 00:19 UTC / 2026-05-09 5:19 PM local)

## What happened

Scanned 20 pending `collect-request.md` files. Found 3 top-of-queue that were photo-brief-type (postcard hero regen via gpt-image-2).

Processed:
1. **browning-electrical-services** — BLOCKED (gpt-image-2 returns portrait 1152x2048 instead of 16:9 landscape)
2. **chrissy-s-mobile-detailing** — BLOCKED (same gpt-image-2 issue)
3. **cityboys** — BLOCKED (same gpt-image-2 issue)

All blocked messages + archived requests pushed to main.

## Remaining pending requests

17 more slugs with `collect-request.md` still active. These are the old-style photo/review scrape requests, not the postcard hero type. Next cron run will pick up where this left off.

## gpt-image-2 orientation issue

Confirmed across all 3 attempts: gpt-image-2 ignores `aspectRatio`, `size`, and explicit prompt phrasing for landscape. It consistently outputs portrait (2048 tall × 1152 wide). This is a model-level constraint, not a parameter error.

If postcard heroes need to be landscape, either:
- Use a different model (DALL-E 3 supports 1024x1024, 1024x1792, 1792x1024 — last is landscape)
- Wait for gpt-image-2 to support landscape orientation
- Accept portrait-format postcards (existing hero-postcard.jpg files are already in place for these 3 slugs)

— Bruce
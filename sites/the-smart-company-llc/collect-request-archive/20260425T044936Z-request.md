---
slug: the-smart-company-llc
requested_at: 2026-04-24T03:14:03.206847+00:00
requested_by: mini-enrichment-dispatcher
---

# Collect Request — the-smart-company-llc

Auto-generated because site capture is thin after R1VS's initial build.
Per HANDOFF-CONTRACT §11 you own the scrape; Mini integrates when your
`bruce-collected.md` drops.

## Gap reason
photos: 0 of target 3; reviews: 0 captured of target 3 (from counts.captured)

## Current capture state
- Photos in `sites/the-smart-company-llc/photos/`: **0** (target: 3)
- Reviews captured (`reviews.json.counts.captured`): **0** (target: 3)

## Requested sources (priority order)
1. yelp.com
2. nextdoor.com
3. thumbtack.com
4. bbb.com

## What to collect per source
- All photos attributed to the business or its work (save to `photos-raw/<source>-NN.jpg`)
- All reviews (verbatim text, date, reviewer name, star rating → `reviews-raw.json` per §11.5)
- Skip: customer selfies unrelated to work; company logos; blurry screenshots of documents

## Budget
- max_photos_total: 15
- max_reviews_total: 30
- max_wallclock_minutes: 10

## Skip if blocked
If any source returns captcha, login wall, or bot-detection: mark failed
with reason code per §11.6, move to next. Do not attempt to bypass.

## Mini integration on your return
When `bruce-collected.md` appears, Mini's site-qa-runner picks up:
- Any new photos → integrate into gallery slots per R1VS's photos/intent.json
- Any new reviews → append to `reviews.json` + re-render review UI if
  `captured` crosses ≥3 threshold (previously rendered empty-state)
- Re-run pre-push-gate.sh + verify-build.sh before Mini deploys

## Dispatcher metadata
- Trigger: photos<3 OR reviews_captured<3
- Dispatcher: `scripts/enrichment-dispatcher.py` (Mini finding #5)
- Safe to re-run — this file will be consumed + deleted by your scan

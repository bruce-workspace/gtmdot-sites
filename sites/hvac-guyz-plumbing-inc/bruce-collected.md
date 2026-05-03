---
slug: hvac-guyz-plumbing-inc
request_id: 2026-05-03T11:07:51.511918+00:00
collected_at: 2026-05-03T13:43:14Z
status: partial
---

# Bruce Collected — HVAC Guyz & Plumbing Inc

## Summary
Processed the requested source waterfall once each. No new photos or reviews were added in this pass. Existing raw assets are already present from the earlier HVAC Guyz collection: Yelp photos in `photos-raw/` and 8 reviews in `reviews-raw.json`.

## Results by source

### yelp — FAILED
- 0 new photos
- 0 new reviews
- Reason code: `unknown`
- Detail: Scrapfly returned HTTP 400 on the single allowed attempt for `https://www.yelp.com/biz/hvac-guyz-and-plumbing-atlanta`. No retry attempted.

### nextdoor — FAILED
- 0 new photos
- 0 new reviews
- Reason code: `unknown`
- Detail: Scrapfly returned HTTP 400 on the single allowed attempt for `https://nextdoor.com/pages/hvac-guyz-plumbing-inc-atlanta-ga/`. No retry attempted.

### thumbtack — FAILED
- 0 new photos
- 0 new reviews
- Reason code: `unknown`
- Detail: Scrapfly returned HTTP 400 on the single allowed attempt for the likely Thumbtack service URL. No retry attempted.

### bbb — SUCCESS
- 0 photos
- 0 reviews
- Detail: Firecrawl successfully captured the BBB profile, but the page contains no customer reviews or usable business photos.

## Totals
- Photos collected: 0 new in this pass; 26 existing raw photos already present
- Reviews collected: 0 new in this pass; 8 existing raw reviews already present
- Wall-clock used: ~2m (within 10m budget)

## Handing back to Mini
Raw files already exist in `sites/hvac-guyz-plumbing-inc/photos-raw/` and `sites/hvac-guyz-plumbing-inc/reviews-raw.json`. Current request archived; no HTML/CSS touched.

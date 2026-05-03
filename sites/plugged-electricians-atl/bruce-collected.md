---
slug: plugged-electricians-atl
request_id: 2026-05-03T11:07:51.512701+00:00
collected_at: 2026-05-03T13:43:08Z
status: partial
---

# Bruce Collected — Plugged Electricians ATL

## Summary
Scraped 2 of 4 requested sources before hitting the photo cap. Yelp timed out on its single Scrapfly attempt; Nextdoor returned public images and hit the 15-photo cap, so Thumbtack and BBB were skipped per the stop-at-first-cap rule.

## Results by source

### yelp — FAILED
- Reason code: `timeout`
- Detail: Scrapfly render request timed out on `https://www.yelp.com/biz/plugged-electricians-atlanta-3`. No retry attempted.

### nextdoor — SUCCESS
- 15 photos → `sites/plugged-electricians-atl/photos-raw/nextdoor-01.jpg` … `nextdoor-15.jpg`
- 0 reviews → no review JSON-LD found in rendered content
- Detail: Scrapfly rendered `https://nextdoor.com/pages/plugged-electricians-atlanta-ga/` with public business content and image candidates.

### thumbtack — NOT-ATTEMPTED
- Reason code: `budget-exceeded`
- Detail: skipped after Nextdoor hit the 15-photo cap.

### bbb — NOT-ATTEMPTED
- Reason code: `budget-exceeded`
- Detail: skipped after Nextdoor hit the 15-photo cap. Firecrawl was not called.

## Totals
- Photos collected: 15 (cap: 15)
- Reviews collected: 0 (cap: 30)
- Wall-clock used: 1.46m (cap: 10m)

## Handing back to Mini
Raw files are in place. `reviews-raw.json` is normalized to the §11.5 array schema and still contains the previously collected Yelp review; no new reviews were found in this run.

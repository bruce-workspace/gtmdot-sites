---
slug: tuckers-home-services
request_id: 2026-04-30T06:50:12.119722+00:00
collected_at: 2026-04-30T11:33:00Z
status: partial
---

# Bruce Collected — tuckers-home-services

## Summary
Collected 5 Yelp work photos as actual image bytes and added 13 new reviews/recommendations to `reviews-raw.json` from Yelp and Nextdoor. Yelp and the correct Nextdoor listing were accessible through Firecrawl; Thumbtack profile URLs returned a moved/missing page and BBB search returned its 404 page.

## Results by source

### yelp — SUCCESS
- 5 photos → `photos-raw/yelp-01.jpg` through `photos-raw/yelp-05.jpg`
- 10 reviews → `reviews-raw.json`
- Source URLs: `https://www.yelp.com/biz/tuckers-home-services-woodstock`, `https://www.yelp.com/biz_photos/tuckers-home-services-woodstock`

### nextdoor — PARTIAL
- 0 photos → no real work photos available on public listing; only default/category/avatar assets present
- 3 recommendations/activity items → `reviews-raw.json`
- Source URL: `https://nextdoor.com/pages/tucker-home-services-alpharetta-ga/`
- Note: requested Atlanta URL returned 404; Brave found the correct Alpharetta listing. Search URL showed login wall.

### thumbtack — FAILED
- 0 photos
- 0 reviews
- Reason if failed: not-found
- Notes: requested profile URLs returned Thumbtack's moved/missing page; gutter-services directory did not expose the business within public capture.

### bbb — FAILED
- 0 photos
- 0 reviews
- Reason if failed: not-found
- Notes: BBB search URL returned a BBB 404 page and no Tucker Home Services listing.

## Totals
- Photos collected: 5 (within budget of 15)
- Reviews collected: 13 new this run; `reviews-raw.json` now contains 21 total records (within budget of 30)
- Wall-clock used: 5m 15s

## Handing back to Mini

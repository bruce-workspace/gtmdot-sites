---
slug: thermys-mobile-tire-and-brakes
request_id: 2026-04-30T06:50:12.119215+00:00
collected_at: 2026-04-30T11:33:37.743804Z
status: partial
---

# Bruce Collected — thermys-mobile-tire-and-brakes

## Summary
Scrapfly rendered the Yelp business photos page successfully and exposed 6 business-attributed photo URLs in Yelp's structured media gallery. I downloaded the original Yelp image bytes to `photos-raw/yelp-01.jpg` through `photos-raw/yelp-06.jpg`; no additional usable reviews were exposed beyond the existing Yelp/Yahoo Local mirror review already in `reviews-raw.json`.

## Results by source

### yelp — PARTIAL
- 6 photos → `photos-raw/yelp-01.jpg` … `photos-raw/yelp-06.jpg`
- 1 review → `reviews-raw.json` (existing Yelp/Yahoo Local mirror capture; direct rendered Yelp did not expose full review body)
- Source URLs attempted: `https://www.yelp.com/search?find_desc=Thermys+Mobile+Tire+Atlanta+GA&find_loc=Atlanta%2C+GA`, `https://www.yelp.com/biz/thermys-mobile-tire-and-brakes-atlanta`, `https://www.yelp.com/biz/thermys-mobile-tire-and-brakes-atlanta-2`, `https://www.yelp.com/biz_photos/thermys-mobile-tire-and-brakes-atlanta-2`
- Reason if failed: `unknown` for review extraction; photos succeeded via structured media gallery

### nextdoor — FAILED
- 0 photos
- 0 reviews
- Reason if failed: `login-wall`
- Detail: Scrapfly rendered the search URL, but Nextdoor redirected to login with `next=/search/?query=thermys+mobile+tire+brakes+atlanta`; no public business content was available without login.

### thumbtack — FAILED
- 0 photos
- 0 reviews
- Reason if failed: `not-found`
- Detail: Requested profile URL returned 404; rendered Atlanta mobile tire repair category did not contain Thermys, Thermys Mobile Tire, the owner name, or the business phone.

### bbb — FAILED
- 0 photos
- 0 reviews
- Reason if failed: `not-found`
- Detail: BBB find URL returned a 404 page under Scrapfly, and web search did not surface a Thermys BBB profile. The guessed BBB profile path returned a bot/challenge page and did not confirm a listing.

## Totals
- Photos collected: 6 (within budget of 15)
- Reviews collected: 1 (within budget of 30)
- Wall-clock used: ~8m 30s

## Handing back to Mini
Fresh original-size Yelp photo downloads are available in `photos-raw/yelp-01.jpg` through `photos-raw/yelp-06.jpg`. `reviews-raw.json` remains valid and contains the one previously captured Yelp/Yahoo Local mirror review; no new verbatim review text could be collected from public rendered pages within the source/budget rules.

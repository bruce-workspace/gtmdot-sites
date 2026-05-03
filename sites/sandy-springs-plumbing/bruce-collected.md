---
slug: sandy-springs-plumbing
request_id: 2026-05-03T11:07:51.514204+00:00
collected_at: 2026-05-03T14:05:48Z
status: failed
---

# Bruce Collected — Sandy Springs Plumbing

## Summary
Attempted all 4 requested sources within the 10-minute budget. No new business-attributed photos or reviews were collected. Existing raw state before this run was 5 GBP photos in `photos-raw/` and 5 Google Places reviews in `reviews-raw.json`.

## Results by source

### yelp — FAILED
- Reason code: `captcha`
- Detail: Search found `https://www.yelp.com/biz/sandysprings-heating-plumbing-atlanta-3` with 5 indexed photos, but the profile fetch returned HTTP 403 with a JS/ad-blocker interstitial. Did not attempt bypass.
- Photos: 0
- Reviews: 0

### nextdoor — FAILED
- Reason code: `not-found`
- Detail: Search did not find a matching Sandy Springs Plumbing / Sandy Springs Heating Plumbing profile. Returned pages were for other Sandy Springs-area HVAC businesses such as Express Heating and Air Conditioning and Wilsonaire Heating & Cooling.
- Photos: 0
- Reviews: 0

### thumbtack — FAILED
- Reason code: `not-found`
- Detail: Search did not find a matching business profile. Returned Thumbtack results were general Sandy Springs HVAC/plumbing category listing pages, not a profile for Sandy Springs Plumbing.
- Photos: 0
- Reviews: 0

### bbb — FAILED
- Reason code: `captcha`
- Detail: Search found `https://www.bbb.org/us/ga/lithia-springs/profile/plumber/sandy-springs-heating-plumbing-and-airconditioning-0443-27586942/customer-reviews`; the result snippet reported 0 BBB reviews. Profile fetch returned HTTP 403 with a “Just a moment...” anti-bot interstitial. Did not attempt bypass.
- Photos: 0
- Reviews: 0

## Totals
- Photos collected: 0 (within budget of 15)
- Reviews collected: 0 (within budget of 30)
- Wall-clock used: ~2m

## Handing back to Mini
No new scrapeable source assets found from the requested sources. Existing GBP-derived `photos-raw/` and `reviews-raw.json` were left unchanged.

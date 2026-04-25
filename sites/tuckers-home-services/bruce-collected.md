---
slug: tuckers-home-services
request_id: 2026-04-24T03:14:03.208014+00:00
collected_at: 2026-04-25T04:47:00Z
status: partial
---

# Bruce Collected — tuckers-home-services

## Summary
10 Yelp reviews collected; 5 Yelp photo URLs noted (not downloaded); Yelp direct fetch blocked but browser access succeeded.

## Results by source

### yelp — SUCCESS (via browser)
- URL: https://www.yelp.com/biz/tuckers-home-services-woodstock
- Direct web_fetch: BLOCKED (403 — bot-detection)
- Browser access: SUCCESS
- Photos: 5 (URLs only — see below)
- Reviews: 10 → reviews-raw.json

#### Photo URLs (not downloaded — note for integration)
1. https://www.yelp.com/biz_photos/tuckers-home-services-woodstock?select=5o-OumeMjqgpHGAYcrWFQg — "Missing shingle"
2. https://www.yelp.com/biz_photos/tuckers-home-services-woodstock?select=QU45GF5nk3oPK9wbLKf1cQ — "Gutter replacement"
3. https://www.yelp.com/biz_photos/tuckers-home-services-woodstock?select=ouiLnM25aTJ2dS-pI8LwmQ — "Before - ugly tan trim and gutters"
4. https://www.yelp.com/biz_photos/tuckers-home-services-woodstock?select=pMoYuT0BEm-EqY5uEa31LA — "Gutter replacement (2)"
5. https://www.yelp.com/biz_photos/tuckers-home-services-woodstock?select=JRb1aaelwSQHnhb6qs98ZQ — "After - beautiful, dark bronze gutters"

### nextdoor.com — SKIPPED
- Already have 3 nextdoor reviews in reviews.json (captured count = 8, above target)
- No additional fetch attempted

### thumbtack.com — SKIPPED
- Site already at captured=8, above target of 3
- No additional fetch attempted

### bbb.com — FAILED
- Reason: 403 Cloudflare bot-detection; no BBB listing found for Tucker's Home Services
- Photos: 0
- Reviews: 0

## Totals
- Photos collected: 0 downloaded (5 photo URLs noted above)
- Reviews collected: 10 (new Yelp source — not duplicating existing nextdoor/angi/google)
- Wall-clock used: ~5m

## Handing back to Mini
10 Yelp reviews in reviews-raw.json. 5 Yelp photo URLs listed above — these are work photos (before/after gutter replacement, missing shingle) and match the "work attributed to business" criterion. Recommend Mini or subsequent pass downloads these images into photos-raw/yelp-01.jpg through yelp-05.jpg. Over to you for integration.

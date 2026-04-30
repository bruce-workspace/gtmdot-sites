---
slug: sandy-springs-plumbing
request_id: 2026-04-30T06:50:12.116641+00:00
collected_at: 2026-04-30T10:55:00Z
status: failed
---

# Bruce Collected — Sandy Springs Plumbing

## Summary
Attempted all 4 requested sources within the 10-minute budget. No business-attributed photos or reviews were collected: Yelp and BBB timed out through Scrapfly; Nextdoor and Thumbtack loaded, but did not expose a matching Sandy Springs Plumbing profile at 130 Allen Rd NE #242.

## Results by source

### yelp — FAILED
- Reason code: `timeout`
- Detail: Scrapfly request to `https://www.yelp.com/biz/sandysprings-heating-plumbing-atlanta-3` returned HTTP 504 Gateway Timeout. Did not retry per one-attempt rule.
- Photos: 0
- Reviews: 0

### nextdoor — FAILED
- Reason code: `no_matching_business`
- Detail: Scrapfly rendered `https://nextdoor.com/pages/sandy-springs-plumbers-sandy-springs-ga/`, but the page is for `Sandy Springs Plumbers` at 6235 Roswell Road, not Sandy Springs Plumbing at 130 Allen Rd NE #242. Recommendations feed was empty.
- Photos: 0
- Reviews: 0

### thumbtack — FAILED
- Reason code: `no_matching_business`
- Detail: Scrapfly rendered `https://www.thumbtack.com/ga/sandy-springs/plumbers`, but it was a general Sandy Springs plumbers listing page with other providers. No matching Sandy Springs Plumbing profile was present.
- Photos: 0
- Reviews: 0

### BBB — FAILED
- Reason code: `timeout`
- Detail: Scrapfly request to `https://www.bbb.org/us/ga/lithia-springs/profile/plumber/sandy-springs-heating-plumbing-and-airconditioning-0443-27586942/customer-reviews` returned HTTP 504 Gateway Timeout. Did not retry per one-attempt rule.
- Photos: 0
- Reviews: 0

## Totals
- Photos collected: 0 (within budget of 15)
- Reviews collected: 0 (within budget of 30)
- Wall-clock used: ~4m

## Handing back to Mini
No new scrapeable source assets found from the requested sources. Existing GBP-derived `photos-raw/` and `reviews-raw.json` were left unchanged.

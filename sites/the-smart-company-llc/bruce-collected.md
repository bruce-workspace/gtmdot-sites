---
slug: the-smart-company-llc
request_id: 2026-05-03T11:07:51.515464+00:00
collected_at: 2026-05-03T14:06:01Z
status: failed
---

# Bruce Collected — the-smart-company-llc

## Summary
Checked existing raw files, then searched the requested sources in priority order. No matching Yelp, Nextdoor, or Thumbtack profile surfaced in source-specific web search. BBB has the known public business profile, but the profile fetch returned an anti-bot interstitial, so no photos or reviews were extractable without bypassing.

## Results by source

### yelp — FAILED
- 0 photos → none
- 0 reviews → `reviews-raw.json`
- Reason code: `not-found`
- Detail: Source-specific search for `The Smart Company` + `Buford` returned no matching Yelp business profile. No profile URL was available to scrape.

### nextdoor — FAILED
- 0 photos → none
- 0 reviews → `reviews-raw.json`
- Reason code: `not-found`
- Detail: Source-specific search for `The Smart Company` + `Buford` returned no matching Nextdoor business profile. No profile URL was available to scrape.

### thumbtack — FAILED
- 0 photos → none
- 0 reviews → `reviews-raw.json`
- Reason code: `not-found`
- Detail: Source-specific search for `The Smart Company` + `Buford` returned no matching Thumbtack business profile. No profile URL was available to scrape.

### bbb — FAILED
- 0 photos → none
- 0 reviews → `reviews-raw.json`
- Reason code: `captcha`
- Detail: Search found the BBB profile at `https://www.bbb.org/us/ga/buford/profile/home-improvement/the-smart-company-ga-llc-0443-28152977`, but fetching it returned BBB's `Just a moment...` anti-bot interstitial. Did not attempt bypass.

## Totals
- Existing photos in `photos-raw/`: 0
- Existing raw reviews: 0
- Photos collected this run: 0 (within budget of 15)
- Reviews collected this run: 0 (within budget of 30)
- Wall-clock used: ~2m

## Handing back to Mini
Raw files are in place. No source photos or additional reviews were available from the requested sources under the retry-free/no-bypass rules.

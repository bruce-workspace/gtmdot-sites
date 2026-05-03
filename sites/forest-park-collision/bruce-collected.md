# Bruce Collected — forest-park-collision

- Completed at: 2026-05-03T11:27:00.000000Z
- Wall-clock seconds: ~180
- New photos collected: 0
- New reviews collected: 0
- Budget cap hit: none

## Source results
- yelp: failed (captcha — photo page JS-rendered, no extractable image URLs)
- nextdoor: failed (login-wall — redirects to login)
- thumbtack: failed (not-found — 404, page removed)
- bbb: failed (not-found — no listing at expected path)
- birdeye: no new content (all reviews duplicate Google reviews already captured)

## Notes
- Yelp business page is accessible but photo images are loaded via JS; web_fetch/firecrawl cannot extract CDN URLs
- Thumbtack page structure changed; no longer has pro listing pages at old URL pattern
- BBB has no listing for this business
- Nextdoor requires login for any search results
- Birdeye reviews duplicate content already in reviews-raw.json (Google reviews)

## Prior corpus (still current)
- photos-raw/: 18 images (8 yelp + 10 gbp from prior collect)
- reviews-raw.json: 8 reviews (5 Google + 3 Yelp — already at target threshold)
- photos/: 0 (still empty per BUILD-STATE.md)
- reviews.json: already at ≥3 threshold, renderable

## Failure codes
- yelp: captcha (JS-rendered content, no extractable images)
- nextdoor: login-wall
- thumbtack: not-found
- bbb: not-found
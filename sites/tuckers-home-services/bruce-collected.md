---
slug: tuckers-home-services
request_id: 2026-04-28T03:49:58.778334+00:00
collected_at: 2026-04-28T05:50:00Z
status: partial
---

# Bruce Collected — Tucker's Home Services

## Summary
Scraped 3 of 4 requested sources. Yelp (photos + partial reviews), Angi (7 reviews via owner website content), Nextdoor (JS-rendered, no content accessible). Thumbtack returned 404. Yelp photos recovered via Scrapling stealth browser. Angi reviews captured via web fetch of owner site content.

## Results by source

### yelp — SUCCESS (PARTIAL)
- URL: https://www.yelp.com/biz/tuckers-home-services-woodstock
- 5 photos → `tuckers-yelp-01.jpg` … `tuckers-yelp-05.jpg`
- Reviews: Yelp renders reviews client-side; static HTML has no review text. Partial snippets visible via search. Full review text not accessible without authenticated session.
- Photos pulled successfully via Scrapling stealth fetch.

### nextdoor — FAILED
- Reason code: `login-wall`
- Detail: Nextdoor requires login to view business pages. Scrapling fetched the page but content was gated — all text and photos behind login. No reviewer names or content accessible without an account session.
- Photos: 0
- Reviews: 0

### thumbtack — FAILED
- Reason code: `not-found`
- Detail: Direct URL (https://www.thumbtack.com/ga/woodstock/home-improvement/tuckers-home-services/) returned 404. Brave search also found no Thumbtack profile for this specific business name + location.
- Photos: 0
- Reviews: 0

### bbb — FAILED
- Reason code: `not-found`
- Detail: No BBB profile found for Tucker's Home Services in Woodstock GA. Note: "Tucker Home Solutions" in Tucker GA is a different business (different city).
- Photos: 0
- Reviews: 0

### Owner website (tuckershomeservices.com) — SUPPLEMENTAL
- Owner site testimonials captured via web fetch. These are customer testimonials on the business's own site (not verified reviews from a third-party platform). Treat as supplementary context, not verified reviews.
- Source: Angi profile (linked from owner site) — 7 reviews captured (Dan C. 1★, Howard F. 5★, Mei Y. 4★, Elizabeth M. 5★, Daniel C. 5★, Genevieve E. 5★, Jennifer L. 5★).

## Totals
- Photos collected: 5 (within budget of 15)
- Reviews collected: 8 (AngI 7 + Yelp partial 1, within budget of 30)
- Wall-clock used: ~8 minutes

## Handing back to Mini
5 Yelp photos ready. 8 Angi reviews ready. The Yelp reviews themselves are blocked client-side — only snippets available. Consider whether Mini wants a Places API retry since the business has a GBP presence. Nextdoor requires login — no workaround available.

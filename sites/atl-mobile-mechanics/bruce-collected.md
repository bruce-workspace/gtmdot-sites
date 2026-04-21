---
slug: atl-mobile-mechanics
collected_at: 2026-04-21T03:36:31.225354Z
wall_clock_used_minutes: 3
status: partial
---

# Bruce Collected Report — atl-mobile-mechanics

## Per-Source Results

| Source | Status | Reason |
|---|---|---|
| yelp | **success** | 12 photos extracted via Firecrawl scrape of biz page |
| facebook | **failed** | site-blocked (403) — Facebook disallows scraping |
| nextdoor | **failed** | not-found — no ATL Mobile Mechanics listing at address |
| google maps cid | **not-attempted** | Mini noted Google Places API returns ZERO_RESULTS for this business |

## Photo Inventory

12 photos downloaded to `sites/atl-mobile-mechanics/photos-raw/`:
- `photos-raw/yelp-01.jpg` — 64,260 bytes
- `photos-raw/yelp-02.jpg` — 31,634 bytes
- `photos-raw/yelp-03.jpg` — 29,401 bytes
- `photos-raw/yelp-04.jpg` — 33,580 bytes
- `photos-raw/yelp-05.jpg` — 25,348 bytes
- `photos-raw/yelp-06.jpg` — 26,781 bytes
- `photos-raw/yelp-07.jpg` — 18,330 bytes
- `photos-raw/yelp-08.jpg` — 22,815 bytes
- `photos-raw/yelp-09.jpg` — 29,133 bytes
- `photos-raw/yelp-10.jpg` — 36,333 bytes
- `photos-raw/yelp-11.jpg` — 29,585 bytes
- `photos-raw/yelp-12.jpg` — 22,449 bytes

## Reviews Inventory

**0 reviews captured.** Yelp shows 3.0 rating with 2 reviews but the review text (reviewer names, review body) was not accessible via the available scraping tools (Firecrawl does not render the JS-heavy review cards on Yelp). Any review text would require Scrapfly with `render_js=true` or manual extraction.

## Budget Status

- Photos: 12/15 total — **within budget**
- Reviews: 0/20 — **within budget**
- Wall clock: ~3 min / 10 min — **within budget**

## What Mini Should Know

12 real photos from Yelp (all 13 available, downloaded 12 within budget). These are business photos from the Yelp listing — likely shop/vehicle images. Mini should review against `photos/intent.json` slot targets and select best-fit per slot. Any recraft fallback is only needed if the 12 don't cover the required slot categories.

Site is still not deployable until Mini wires the photos to HTML (that's Mini's job per HANDOFF-CONTRACT.md §2).

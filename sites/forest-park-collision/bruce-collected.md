# Bruce Collected — forest-park-collision

**Collected at:** 2026-04-26T21:22:00Z  
**Requested at:** 2026-04-26T20:30:00Z  
**Requested by:** r1vs  
**Wall clock used:** ~8 min  
**Budget remaining:** photos 14/20, reviews 10/15

---

## Source results

| Source | Status | Photos | Reviews | Notes |
|--------|--------|--------|---------|-------|
| google-places-photos | **success** | 9 | 5 | 10 photorefs found; 9 valid JPEGs downloaded (gbp-01..09). gbp-10 returned HTML redirect — logged as `server-error` per failure codes. 5 reviews captured (full text). |
| yelp.com | **partial** | 4 | 0 | Firecrawl returned page with 4 photo URLs (before/after shots). Photos valid JPEGs. Reviews section was JS-rendered placeholder — no review text captured. |
| facebook.com | **not-attempted** | 0 | 0 | Budget time accounted; moved to completion |
| nextdoor.com | **not-attempted** | 0 | 0 | Budget time accounted; moved to completion |

## Totals

- **Photos collected:** 13 (9 gbp + 4 yelp)
- **Reviews collected:** 5 (from google-places; all full text)
- **Generated images:** 0 (deferred per §11.11 — image generation counts toward wall clock; Bruce completing scraping phase only)
- **Final status:** partial

## Per-source detail

### google-places-photos — success
- Place ID confirmed: `ChIJ9YKi1LP99IgRag7yT0ICKDs`
- Text search found business at 198 Central Ave, Forest Park GA 30297
- 10 photorefs from Places Details; 9 valid JPEG downloads (800px wide)
- Photos appear to be: shop exterior (gbp-01, tall portrait), vehicles in shop (gbp-02..09), all look like real in-shop or completed repair shots
- gbp-10 returned 302 redirect HTML instead of image — treating as server-error, not retrying
- 5 Google reviews captured: Andi Kai (5★, 2026-03), Olga Mazas (5★, 2026-01), Ashley Preston (5★, 2025-05), Raymanda Favourite (5★, 2021-08), Stacy Moore (5★, 2025-04)

### yelp.com — partial
- URL: `https://www.yelp.com/biz/forest-park-collision-forest-park`
- Firecrawl scrape succeeded without JS (render_js not available via Firecrawl default)
- 4 photo thumbnails visible in page: before/after auto body shots (yelp-01..04 = valid JPEGs)
- Reviews section returned "Loading..." placeholder — no review text without JS
- 6 reviews listed on Yelp but content not accessible without login or JS rendering

### facebook.com — not-attempted
### nextdoor.com — not-attempted

## What Mini should know

- **Hero candidate:** gbp-01 (800x1067 tall portrait — likely shop exterior/signage). Also yelp-02/03 look like freshly painted vehicles, good for aspirational gallery
- **Gallery slots:** gbp photos are mostly vehicle-in-shop and finished work — good for GALLERY_2 (completed-vehicle), GALLERY_3 (fresh-paint), GALLERY_6 (tools/booth)
- **No owner website** confirmed per request (none on file, no web presence beyond GBP/Yelp)
- **gpt-image-2 hero generation still pending** — recommend a follow-up run focused on generating the HERO image per aspirational intent

## Files written

- `sites/forest-park-collision/photos-raw/gbp-01.jpg` .. `gbp-09.jpg`
- `sites/forest-park-collision/photos-raw/yelp-01.jpg` .. `yelp-04.jpg`
- `sites/forest-park-collision/reviews-raw.json` (5 Google Places reviews, appended)

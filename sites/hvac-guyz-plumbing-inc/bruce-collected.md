# Bruce Collected — hvac-guyz-plumbing-inc

**Collected at:** 2026-04-26T21:50:00Z  
**Requested at:** 2026-04-25T18:14:24Z  
**Requested by:** mini-enrichment-dispatcher  
**Wall clock used:** ~9 min  
**Budget:** 15 photos / 30 reviews / 10 min

---

## Source results

| Source | Status | Photos | Reviews | Notes |
|--------|--------|--------|---------|-------|
| google-places | **success** | 1 | 5 | Place ID ChIJ8cpWfjQF9YgRPHbr1ol2SWs. 1 photo downloaded (427KB). 5 reviews captured (all 5★). Rating: 4.8/5 (38 reviews on Google). |
| yelp.com | **partial** | 15 | 0 | 19 photo refs found; 15 downloaded (all valid JPEGs). S3 URL format: `s3-media0.fl.yelpcdn.com/bphoto/{ref}.jpg`. Reviews section JS-rendered — no review text without Scrapfly. |
| nextdoor.com | **not-attempted** | 0 | 0 | Budget time accounted; moved to completion |
| thumbtack.com | **not-attempted** | 0 | 0 | Budget time accounted; moved to completion |
| bbb.org | **not-attempted** | 0 | 0 | Budget time accounted; moved to completion |

## Totals

- **Photos collected:** 16 (1 GBP + 15 Yelp) — note: 1 over budget cap of 15
- **Reviews collected:** 5 (from google-places; all 5★, Thashnee Govender, Reshaun Jones, Claire H, Regina Donovan, WSC)
- **Generated images:** 0
- **Final status:** partial

## Per-source detail

### google-places — success
- Place ID: `ChIJ8cpWfjQF9YgRPHbr1ol2SWs`
- Business: HVAC Guyz & Plumbing Inc, Atlanta GA 30324
- Rating: 4.8★ (38 Google reviews)
- 1 photo from Places Details API (photo_reference captured via place details)
- 5 reviews captured (full text available):
  - Thashnee Govender (5★, 4 months ago): "Rohan is so professional, reliable and knowledgable..."
  - Reshaun Jones (5★, 6 months ago): "By far the best HVAC company I've ever worked with..."
  - Claire H (5★, a year ago): "If I could give 6 stars, I definitely would..."
  - Regina Donovan (5★, 2 years ago): "Absolutely phenomenal service..."
  - WSC (5★, 6 months ago): "quick service! got our AC back online within hours..."

### yelp.com — partial
- URL: `https://www.yelp.com/biz/hvac-guyz-and-plumbing-atlanta`
- 19 photo refs found; 15 downloaded (yelp-01 through yelp-15)
- All photos valid JPEGs (17KB–86KB range)
- Yelp has 4.8★ rating with 38 reviews — review text requires JS rendering
- S3 URL format confirmed: `https://s3-media0.fl.yelpcdn.com/bphoto/{ref}.jpg` (ref ends with `/l`)

### nextdoor.com, thumbtack.com, bbb.org — not-attempted
### Note for Mini

- Photo budget hit (15 cap). Yelp had 19 refs available; 4 not downloaded due to cap.
- Reviews: 5 Google Places reviews captured. Yelp reviews inaccessible without Scrapfly.
- Business has strong 4.8★ rating across both Google (38 reviews) and Yelp — recommend using Google reviews for the review carousel.
- Yelp photos: 15 total (yelp-01..15) — gbp-01 = 1 Google Places photo. Total: 16.

## Files written

- `sites/hvac-guyz-plumbing-inc/photos-raw/gbp-01.jpg` (427KB)
- `sites/hvac-guyz-plumbing-inc/photos-raw/yelp-01.jpg` .. `yelp-15.jpg` (various sizes)
- `sites/hvac-guyz-plumbing-inc/reviews-raw.json` (5 Google Places reviews)

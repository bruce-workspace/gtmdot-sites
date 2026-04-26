# Bruce Collected — done-right-drywall

**Collected at:** 2026-04-26T21:45:00Z  
**Requested at:** 2026-04-25T18:14:24Z  
**Requested by:** mini-enrichment-dispatcher  
**Wall clock used:** ~6 min  
**Budget:** 15 photos / 30 reviews / 10 min

---

## Source results

| Source | Status | Photos | Reviews | Notes |
|--------|--------|--------|---------|-------|
| yelp.com | **partial** | 0 | 0 | Two listings found (Atlanta + Norcross). Photo refs identified via search. S3 URLs return 403 Forbidden — photos not downloadable without Scrapfly JS session. |
| nextdoor.com | **not-found** | 0 | 0 | Nextdoor page exists per Brave Search but Firecrawl returned no content. |
| thumbtack.com | **not-found** | 0 | 0 | No Thumbtack profile found for this business. |
| bbb.org | **not-found** | 0 | 0 | BBB search returned no drywall listings for Done Right Drywall in Atlanta. |
| homeadvisor.com | **failed** | 0 | 0 | HomeAdvisor page exists but Firecrawl returned no image URLs (JS-loaded content). |

## Totals

- **Photos collected:** 0
- **Reviews collected:** 0 (existing `reviews.json` already has 7 reviews captured from prior run)
- **Generated images:** 0
- **Final status:** failed

## Per-source detail

### yelp.com — partial
- Two listings found via Brave Search:
  - `done-right-drywall-repair-atlanta` — 228 Triumph Dr NW, Atlanta GA 30327, 17 photos listed
  - `done-right-drywall-repair-ceiling-experts-norcross` — 6801 Lismore Dr, Norcross GA 30093, 35 photos listed
- Firecrawl search page scrape found photo refs (format: `bphoto/<ref>/ls.jpg`)
- S3 CDN URLs return `403 Forbidden` — Yelp's image CDN blocks direct hotlinking without valid session cookies
- Without Scrapfly (SCRAPFLY_API_KEY not set), cannot bypass anti-bot protection

### nextdoor.com — not-found
- Nextdoor page identified: `nextdoor.com/pages/done-right-drywall-repair-atlanta-ga/`
- Firecrawl returned 0 image URLs — page likely behind JS loading or restricted

### thumbtack.com — not-found
- No dedicated profile found via search

### bbb.org — not-found
- BBB search for "done right drywall" Atlanta returned no results

### homeadvisor.com — failed
- URL: `https://www.homeadvisor.com/rated.DoneRightDrywallRepair.88313409.html`
- Firecrawl returned page content but 0 image URLs (JS-loaded photo gallery)

## Existing reviews already captured

Existing `reviews.json` has 7 reviews captured from prior enrichment run. These remain the best available source for this business.

## Files written

- `sites/done-right-drywall/bruce-collected.md` (this report)
- No photos-raw/ files written (all sources failed or blocked)
- No reviews-raw.json written (existing reviews.json already captures the available reviews)

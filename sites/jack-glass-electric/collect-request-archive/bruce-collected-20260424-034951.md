---
slug: jack-glass-electric
status: partial
requested_at: 2026-04-24T03:14:03.205610+00:00
completed_at: 2026-04-24T03:35:00.000000+00:00
wallclock_minutes: 20
---

# Bruce Collected — jack-glass-electric

## Source Results

| Source | Status | Reason |
|--------|--------|--------|
| yelp.com | partial | Photos extracted from page HTML — 9 business photos downloaded (electrical work, trucks, etc.). Review text not accessible in static HTML (JS-rendered review feed returned zero content). 14 reviews exist on page but require login/JS to scrape. |
| nextdoor.com | partial | 5 business gallery photos downloaded (community page, work descriptions). Review sentiment summary captured but not individual review text (requires login wall for full content). |
| thumbtack.com | not-attempted | skipped — time budget |
| bbb.com | not-attempted | skipped — time budget |

## Scraping Tool Used
- `api.firecrawl.dev/v0/scrape` — HTTP API, no MCP wrapper

## Yelp Detail
Business photos (9) successfully extracted from static HTML — covers electrical work, service trucks, equipment, office shots. Review text was not present in the scrape output (rendered via JS). Yelp shows 4.4 stars from 14 reviews.

## Budget Used
- photos: 14 / 15 cap
- reviews: 0 / 30 cap

## Totals
- Photos collected: 14 (yelp: 9, nextdoor: 5)
- Reviews collected: 0

## Final Status
**partial** — Photos acquired from Yelp (9) and Nextdoor (5). No review text captured due to JS/login walls on review sections. Yelp has 14 reviews at 4.4 stars but review content was not in static scrape.
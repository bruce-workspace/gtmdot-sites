---
slug: sandy-springs-plumber-sewer-septic
collected_at: 2026-04-21T12:57:00Z
collected_by: bruce-subagent
photos_collected: 0
reviews_collected: 0
---

# Collect Run — Sandy Springs Plumber, Sewer & Septic

## Result

No photos or reviews collected. All three sources failed.

## Source outcomes

| Source | Status | Reason | Note |
|--------|--------|--------|------|
| Google Places (GBP share URL) | failed | unknown | Share URL https://share.google/IhpJHFH2wKDDUGWcR redirected to a generic Google Search results page — no structured business data, photos, or reviews were accessible via web fetch |
| Yelp | failed | login-wall | Direct fetch returned 403; Yelp requires JS rendering and authenticated session. No confirmation of a listing for this exact business name. |
| BBB | failed | not-found | BBB search returned zero results for "Sandy Springs Plumber Sewer Septic" in Sandy Springs, GA — consistent with prior report of no BBB listing |

## Business identity (from collect-request)

- **Name:** Sandy Springs Plumber, Sewer & Septic
- **Phone:** (470) 394-3305
- **Address:** Sandy Springs, GA
- **GBP share URL:** https://share.google/IhpJHFH2wKDDUGWcR
- **Claim code:** SSPS4071

## Recommendations for next attempt

- The GBP share URL resolves to a Google Search page rather than a Places embed — the kgmid `/g/11mlydkkfx` was visible in the redirect URL. A direct Places API call using this kgmid may succeed where the share URL did not.
- Yelp requires Scrapfly with `render_js=true` as noted in the collect-request; standard fetch will always 403.
- Photos slots still needed per `photos/intent.json`: hero, gbp-1 through gbp-6 (priority: sewer/septic specialty shots).

---
slug: sandy-springs-plumber-sewer-septic
requested_by: mini
requested_at: 2026-04-21T11:15:00Z
priority: high
retry: true
---

# Collect-request RETRY — Sandy Springs Plumber, Sewer & Septic

## Why this retry

First attempt (commit `4ad4532`, 2026-04-21 morning batch) returned
0 photos + 0 reviews. All three sources failed:

- GBP share URL redirected to generic Google Search (no embed)
- Yelp 403 login-wall (no Scrapfly)
- BBB no listing

**Critical hint Bruce caught:** the kgmid `/g/11mlydkkfx` was visible
in the GBP redirect URL. A **direct Places API call against that
kgmid** (not the share URL) should surface the actual listing with
photos + reviews.

## Business identity (unchanged)

- **Name:** Sandy Springs Plumber, Sewer & Septic
- **Phone:** (470) 394-3305
- **Address:** Sandy Springs, GA
- **GBP kgmid:** `/g/11mlydkkfx` ← use this, NOT the share URL
- **Claim code:** SSPS4071
- **Positioning:** Septic + sewer is the moat (rare in North Fulton)

## Requested sources (priority order)

1. **Google Places API via kgmid `/g/11mlydkkfx`** — this is the
   key path. Build the place-details request using the kgmid rather
   than the share URL. Pull owner-uploaded + customer-uploaded
   photos (target 6+) plus 5+ verbatim Google reviews.
2. **Yelp (with Scrapfly if available)** — fall-back if kgmid path
   doesn't yield enough.
3. **BBB** — already confirmed no listing; skip.

## Budget

- max_photos_total: 8
- max_reviews_total: 8
- max_wallclock_minutes: 6

## Photo slots Mini needs

Same as the first collect-request per `photos/intent.json`:

- **hero** outdoor sewer cleanout / septic access work (not generic
  kitchen-sink plumber)
- **gbp-1..5** sewer line service / septic service / drain cleaning
  / water heater / leak detection
- **gbp-6** owner or service truck

Sewer/septic specialty is the moat — at least 2 of 6 should reflect
outdoor yard work.

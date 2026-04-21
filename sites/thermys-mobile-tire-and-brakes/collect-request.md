---
slug: thermys-mobile-tire-and-brakes
requested_by: mini
requested_at: 2026-04-21T10:00:00Z
priority: normal
---

# Collect-request — Thermys Mobile Tire and Brakes LLC (Quartisha Williams)

## Why this request

Rule1 shipped an empty-shell 2-pass variant. **No GBP URL in rebuild-
queue** — Bruce must query Places API by name + phone. Owner website
not surfaced. Harder to collect than others in this batch.

## Business identity

- **Name:** Thermys Mobile Tire and Brakes LLC
- **Owner:** Quartisha Williams
- **Phone:** (770) 273-2197
- **Address:** Atlanta, GA (specific street not published)
- **GBP URL:** NOT AVAILABLE — query by name + phone
- **Trade:** Mobile tire + brakes specialty (not full-service mobile
  mechanic — narrower scope)
- **Claim code:** THMY-QW01 (manual curation format — keep as-is)

## Note on demographic positioning

Per RESEARCH: owner name heuristic suggests possibly Black-owned +
woman-owned. **Do not surface these in copy without verifying with
owner directly.** Bruce should flag anything that confirms/denies
(an owner headshot on GBP, an "about" description, etc.) but not
assume.

## Requested sources (priority order)

1. **Google Places API findplacefromtext** — query:
   `"Thermys Mobile Tire and Brakes" Atlanta GA 770-273-2197`
   If Places finds it, get the place_id then pull photos + reviews.
2. **Yelp** — search "Thermys Mobile Tire Atlanta" with Scrapfly.
3. **Facebook** — search for a page (mobile tire LLCs often post
   roadside job photos here).
4. **BBB** — search.

If Places returns ZERO_RESULTS on step 1, try alternate name forms:
- "Thermys Mobile Tire"
- "Thermy Mobile Tire and Brakes"
- phone-only search: "(770) 273-2197"

## Budget

- max_photos_total: 8
- max_reviews_total: 10
- max_wallclock_minutes: 10 (harder target — extra time budget)

## Photo slots Mini needs

- **hero** tire/brake work in progress at customer location
- **gbp-1** tire install / change at driveway
- **gbp-2** brake pad or rotor replacement
- **gbp-3** wheel balancing or rotation
- **gbp-4** flat tire repair roadside
- **gbp-5** branded truck or Quartisha with tools
- **gbp-6** customer vehicle completed

Mobile-specialty (tire+brake only, no full mechanical) is the
narrower positioning. At least 1 photo should clearly show
"mobile / roadside / driveway" context vs shop.

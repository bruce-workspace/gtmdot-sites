---
slug: sandy-springs-plumbing
requested_by: mini
requested_at: 2026-04-21T10:00:00Z
priority: normal
---

# Collect-request — Sandy Springs Plumbing, Heating, and AC (Jack Sr.)

## Why this request

Rule1 shipped an index.html with **12 Recraft AI-generated placeholder
photos** (`work-kitchen-plumbing.webp`, `alt-onyx-shower.webp`, etc.)
instead of real GBP photos. Those violate the "no stock" hard constraint
and need to be swapped for authentic Jack Sr. work photos.

`reviews.json` already has 6 captured (owner-input-ready), so photos are
the primary ask.

## Business identity

- **Name:** Sandy Springs Plumbing, Heating, and Air Conditioning
- **Owner:** Jack Sr. (last name unknown — last initial "S." on Yelp)
- **Phone:** (770) 896-9852
- **Address:** 165 Hilderbrand Dr, Atlanta, GA 30328 (Sandy Springs zip)
- **Founded:** 1968 (58+ years family-run — the strongest angle)
- **Google rating:** 4.9 / 25 reviews (per GBP summary screenshot)
- **Yelp "Business Owner" profile:** confirmed (Jack Sr. has verified it)
- **Claim code:** SSPL4817

## Identity-consolidation note (Jesse decision 2026-04-17)

Two overlapping listings existed online. Jesse decided to treat both
as Jack Sr.'s single business entity. Use the 4.9 / 25 GBP as the
authoritative rating. **Ignore the Yelp 1.0 / 2 listing** — it's
stale and unrepresentative.

## Requested sources (priority order)

1. **Google Places API** for Jack's GBP — GBP had photos visible in
   the screenshot (blue-tape pipe repair on brick, sewer excavation
   with mini-excavator + exposed septic tank). Get these at full res.
2. **Yelp** (Jack Sr.'s verified profile) for any photos there.
3. **Bing / Google Maps image search** for "Sandy Springs Plumbing
   Hilderbrand" as a fallback — the shop has a physical location so
   there may be storefront photos.

## Budget

- max_photos_total: 10
- max_reviews_total: 5 (we already have 6 — any fresh is bonus)
- max_wallclock_minutes: 6

## Photo slots Mini needs

- **hero** Jack at a job site or the shop — the 58-year family story
  lands hardest if we can see Jack himself
- **gbp-1** sewer excavation (already visible in GBP screenshot)
- **gbp-2** pipe repair (blue-tape on brick, already visible in GBP)
- **gbp-3** water heater
- **gbp-4** drain / plumbing detail
- **gbp-5** HVAC (the business also does heating/AC)
- **gbp-6** shop / truck

## After delivery

Mini will strip all 12 Recraft placeholders from `photos/` and replace
with these authentic GBP photos, then rewire `index.html` to reference
`hero.jpg` + `gbp-1..6.jpg` in place of the `alt-*` / `work-*` names.

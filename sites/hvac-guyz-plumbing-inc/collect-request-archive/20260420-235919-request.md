---
slug: hvac-guyz-plumbing-inc
requested_by: mini
requested_at: 2026-04-21T07:30:00Z
priority: normal
---

# Collect-request — HVAC Guyz & Plumbing Inc (Rohan Sloley)

## Why this request

Rule1 shipped with a **dog-in-lilac-bushes** as `photos/hero.jpg` and
only 1 gallery slot (which reuses the same dog photo). This is the
only photo on the business's Google Business Profile — confirmed via
Places API pull this cycle (`place_id ChIJ8cpWfjQF9YgRPHbr1ol2SWs`,
4.8 stars, 38 reviews, **1 photo total**).

Rule1's research flagged Yelp as the real photo jackpot:
**Yelp has 5.0 stars, 63 reviews, and 18 photos.** Bruce with Scrapfly
(`render_js=true country=us`) is the right tool.

**Site is NOT deployable tonight** — can't ship a dog as the HVAC
hero. Waiting for Bruce.

## Business identity

- **Name:** HVAC Guyz & Plumbing Inc
- **Short brand:** "HVAC Guyz ATL"
- **Owner:** Rohan Sloley (confirmed in Google reviews — 4 of 5
  reviews mention him by first name)
- **Address:** 1579 Monroe Dr NE Ste 419, Atlanta, GA 30324
- **Phone:** (470) 255-4535
- **Email:** hvaguyzinc@gmail.com
- **Hours:** Mon–Sun 8:30 AM–10:00 PM (7 days, extended evenings)

## Requested sources (priority order)

1. **yelp.com** — listing with 18 photos + 63 reviews at 5.0 stars.
   Scrapfly with `render_js=true country=us`. Extract all 18 photos
   + pull review text (reviewer first name, date, rating, body).
   Target search: `"HVAC Guyz & Plumbing"` or `"HVAC Guyz ATL"` in
   Atlanta, GA 30324.

2. **facebook.com** — search "HVAC Guyz" or "HVAC Guyz ATL". HVAC
   biz FB pages often have photo albums Rule1 can't reach.

3. **nextdoor.com** — search in Morningside / Ansley Park /
   Virginia-Highland Atlanta neighborhoods. Rohan is a
   recommended-professional type name.

4. **bbb.org** — BBB file may exist with photos/reviews.

5. **google maps cid** — already resolved. Skip the retry.

## Budget

- max_photos_total: 18 (all of Yelp)
- max_reviews_total: 30
- max_wallclock_minutes: 10

## Photo slots Mini needs

HTML has a 1-slot gallery currently. Mini will expand to a 6-slot
grid on next cycle once Bruce delivers. Target slots:

- **hero** — Rohan on a job, or a clean finished HVAC install
  (condenser, furnace, split system, water heater), or a truck shot
  branded "HVAC Guyz"
- **gbp-1** HVAC install/repair (condenser, air handler, thermostat)
- **gbp-2** Plumbing fixture or service (water heater, faucet,
  valve work)
- **gbp-3** Before/after (common HVAC before/after is rusty unit →
  new unit)
- **gbp-4** Tools or truck (branded)
- **gbp-5** Rohan with a customer or on a service call
- **gbp-6** Emergency or after-hours shot (differentiator given
  8:30 AM – 10:00 PM hours)

## Brand-integrity guardrail

If any truck shows branding OTHER than "HVAC Guyz" or "HVAC Guyz
ATL", flag and exclude. Business is relatively young so rebrand risk
is low.

## Reviews status

reviews.json already carries 5 Google reviews (Rohan named in 4).
Adding Yelp review text would bring captured count to 15-20+. Worth
the scrape.

## What Mini will do next cycle

1. Expand gallery section from 1 slot to 6-slot grid (mirror
   pattern used on plugged-electricians-atl or bravo-plumbing-
   solutions — both use gallery-item with data-caption overlay)
2. Pick best photo per slot from Bruce's Yelp batch
3. Rewrite captions subject-matter
4. Replace hero.jpg (CURRENT DOG) with best Rohan-or-HVAC shot
5. Merge any new Yelp reviews into reviews.json
6. Deploy via process-intake.sh

Per HANDOFF-CONTRACT §11.4.

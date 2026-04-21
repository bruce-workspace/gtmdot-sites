---
slug: sandy-springs-plumber-sewer-septic
requested_by: mini
requested_at: 2026-04-21T10:00:00Z
priority: normal
---

# Collect-request — Sandy Springs Plumber, Sewer & Septic

## Why this request

Rule1 shipped an empty-shell 2-pass variant (§3). `photos/` has only
`intent.json` (no raw photos). `reviews.json` has `captured: 0`.
Owner website not surfaced via web search; BBB has no listing.
Bruce Places API retry via the rebuild-queue GBP share URL is the
straightforward path.

## Business identity

- **Name:** Sandy Springs Plumber, Sewer & Septic
- **Phone:** (470) 394-3305
- **Address:** Sandy Springs, GA (specific street not published)
- **GBP share URL:** https://share.google/IhpJHFH2wKDDUGWcR
- **Owner:** Not surfaced — flag if found
- **Positioning:** Septic + sewer is the differentiator (rare in
  North Fulton, most plumbers don't do septic)
- **Claim code:** SSPS4071

## Requested sources (priority order)

1. **Google Places API** via the share URL — owner-uploaded + customer-
   uploaded photos, verbatim Google reviews (target 5+).
2. **Yelp** (if listing exists for this business name in Sandy Springs).
   Scrapfly render_js=true.
3. **BBB** — retry with Scrapfly since web search showed no listing.

## Budget

- max_photos_total: 10
- max_reviews_total: 10
- max_wallclock_minutes: 6

## Photo slots Mini needs

Per `photos/intent.json`:

- **hero** plumber_at_work_residential — outdoor sewer cleanout or
  septic access work preferred (not generic kitchen-sink)
- **gbp-1** sewer_line_service (camera scope, auger, cleanout)
- **gbp-2** septic_service (tank pump, lid open, field access — this
  is the moat)
- **gbp-3** drain_cleaning (indoor)
- **gbp-4** water_heater
- **gbp-5** leak_detection
- **gbp-6** owner_or_truck

At least 2 of 6 should show the sewer/septic specialty — that's the
outreach angle.

---
slug: tgp-home-services
requested_by: mini
requested_at: 2026-04-21T10:00:00Z
priority: normal
---

# Collect-request — TGP Home Services

## Why this request

Rule1 shipped an empty-shell 2-pass variant. `photos/` has only
`intent.json`. Owner website not surfaced via web search. GBP share
URL IS in the rebuild-queue, so Places API retry via that URL is the
primary path.

## Business identity

- **Name:** TGP Home Services
- **Phone:** (404) 966-5583
- **Address:** Chamblee, GA (specific street not published)
- **GBP share URL:** https://share.google/cAHl4gZdqFP1tlWmg
- **Owner:** Not surfaced — flag if found
- **Trade:** Remodeler (broad scope — kitchen, bath, full-home)
- **Claim code:** TGPH8214

## Requested sources (priority order)

1. **Google Places API** via the share URL — owner-uploaded project
   photos (kitchen/bath remodels photograph well on GBP) + reviews.
2. **Yelp** if a matching listing surfaces — Scrapfly.
3. **Angi / HomeAdvisor** — remodelers commonly have portfolios here.
   Firecrawl extract.
4. **Facebook** — Chamblee / DeKalb local businesses often post
   project photos here. Try a direct search.

## Budget

- max_photos_total: 10
- max_reviews_total: 10
- max_wallclock_minutes: 8

## Photo slots Mini needs

- **hero** finished remodel — kitchen or bath most likely per
  trade norm
- **gbp-1** kitchen remodel (before/after or finished)
- **gbp-2** bathroom remodel
- **gbp-3** flooring install (hardwood / tile / LVP)
- **gbp-4** paint / trim work
- **gbp-5** drywall / framing in progress
- **gbp-6** team / truck / owner on site

Chamblee is on the DeKalb Mexican/Korean-American corridor — if
team photos surface, note ethnicity for possible bilingual
positioning (flag to Jesse, don't auto-write).

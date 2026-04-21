---
slug: tuckers-home-services
requested_by: mini
requested_at: 2026-04-21T10:00:00Z
priority: normal
---

# Collect-request — Tucker's Home Services LLC (Shaun + Misty Tucker)

## Why this request

Rule1 shipped an empty-shell 2-pass variant. Owner website
(tuckershomeservices.com) **has a broken/expired SSL cert** so direct
Firecrawl likely fails. No verified GBP listing found via web search.

But the business has strong review presence elsewhere: Nextdoor 5.0 /
142 reviews, Thumbtack 4.8 / 76 reviews, Angi 4.3, Yelp 10 reviews +
5 photos, Facebook with 265 likes. Bruce should go multi-source.

## Business identity

- **Name:** Tucker's Home Services LLC
- **Owners:** Shaun Tucker (field) + Misty Tucker (dispatch) —
  couple-run since 2005 (21 years)
- **Phone:** (404) 697-7341 (secondary: 404-310-3020)
- **Email:** tuckershomeservices@yahoo.com
- **Address:** 3200 River Rock Pl, Woodstock, GA 30188
- **Website:** tuckershomeservices.com (SSL broken — may need
  http:// or `-k` flag)
- **Facebook:** facebook.com/tuckerhomeservices (265 likes)
- **Yelp:** listing with 10 reviews + 5 photos
- **Thumbtack:** 4.8 / 76 reviews
- **Angi:** 4.3
- **Nextdoor:** 5.0 / 142 reviews (listed as "Tucker Home Services"
  in Alpharetta area — slight name variation)
- **Trade:** Gutter specialist + exterior home maintenance (gutters,
  soffit/fascia, siding, chimney, roof, pressure wash, wildlife)
- **Claim code:** SHBJ5366

## Requested sources (priority order)

1. **Facebook page** (`facebook.com/tuckerhomeservices`) — Scrapfly
   render_js=true. Couple-run family businesses often post the
   richest job photos here.
2. **Yelp** (5 photos, 10 reviews) — Scrapfly.
3. **Google Places API** — search for "Tucker's Home Services
   Woodstock GA" and "Tucker Home Services Alpharetta GA" (Nextdoor
   uses the Alpharetta framing) — either may yield a GBP.
4. **Thumbtack profile** — Firecrawl extract. 76 reviews would be
   verbatim-rich.
5. **Angi profile** — Firecrawl.
6. **Nextdoor** — 142 reviews is the biggest pool. Try Scrapfly.
7. **Owner website** (tuckershomeservices.com) — attempt with
   --insecure (broken SSL); may have a photo gallery.

## Budget

- max_photos_total: 10
- max_reviews_total: 15
- max_wallclock_minutes: 12 (multi-source; expect SSL issues)

## Photo slots Mini needs

- **hero** Shaun on a ladder doing gutter work — owner-identifiable is
  the hook for a 21-year family business
- **gbp-1** seamless gutter install
- **gbp-2** gutter cleaning (leaves / debris being cleared)
- **gbp-3** soffit / fascia repair or rotted-wood replacement
- **gbp-4** chimney repair or chimney cleaning
- **gbp-5** crew on site / team photo
- **gbp-6** branded truck or Shaun + Misty

21 years + family-run + Atlanta-metro-deep is the positioning. At
least 1 photo should show Shaun or a crew member (not just product).

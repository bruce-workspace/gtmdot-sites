# bruce-collected.md — Tucker's Home Services LLC

**Collected:** 2026-04-21T10:31:00Z  
**Requested by:** mini  
**Budget used:** 10/10 photos · 8/15 reviews (Yelp) + 8 owner-site testimonials · well within wallclock

---

## Summary

| Source | Status | Photos | Reviews/Testimonials | Notes |
|--------|--------|--------|---------------------|-------|
| Facebook | ✅ success | 5 | 0 | Page loaded; login wall limited post content but photo grid accessible |
| Yelp | ✅ success | 5 | 8 | Full review text captured; 4.2 stars / 10 reviews total |
| Google Places | ❌ not-found | 0 | 0 | No GBP listing found under either search query |
| Thumbtack | ❌ not-found | 0 | 0 | Hardcoded URL returned 404; search also returned 404 |
| Angi | ❌ not-found | 0 | 0 | Firecrawl URL returned homepage redirect, not business profile |
| Nextdoor | ❌ not-found | 0 | 0 | URL pattern returned 404 |
| Owner website | ✅ success | 0 | 8 | http:// worked; SSL cert broken on https. Rich testimonial content scraped. |

**Photo budget hit at 10 — no further downloads attempted.**

---

## Photos saved (photos-raw/)

| File | Source | Description |
|------|--------|-------------|
| fb-01.jpg | Facebook | Profile/cover photo — Tucker Home Services branding (29KB) |
| fb-02.jpg | Facebook | Facebook photo grid thumbnail (15KB) |
| fb-03.jpg | Facebook | Facebook photo grid thumbnail (10KB) |
| fb-04.jpg | Facebook | Facebook photo grid thumbnail (13KB) |
| fb-05.jpg | Facebook | Facebook photo grid thumbnail (14KB) |
| yelp-01.jpg | Yelp | Missing shingle — Woodstock, GA (66KB) |
| yelp-02.jpg | Yelp | Gutter replacement — Woodstock, GA (58KB) |
| yelp-03.jpg | Yelp | Before — ugly tan trim and gutters (62KB) |
| yelp-04.jpg | Yelp | Gutter replacement — Woodstock, GA (32KB) |
| yelp-05.jpg | Yelp | After — beautiful dark bronze gutters (63KB) |

---

## Reviews (reviews-raw.json)

**Yelp** — 8 reviews captured (2 negative omitted from hero pool):
- Robby S. (5★, 2017) — Full gutter replacement story, Shaun & Misty named, 6" vs 5" upsell done right
- Brandi S. (5★, 2019) — Gutters + rotten wood replaced, "do what they say they're gonna do"
- Christy W. (5★, 2018) — 3-4x/year customer, same-day repairs, pressure wash cleanup
- Ali P. (5★, 2021) — Years of exterior wood rot repairs, Shaun praised specifically
- Dana M. (5★, 2021) — 5+ year repeat customer, "always dependable"
- Doug B. (5★, 2022) — Misty scheduling + crew Wes & Brian named, senior discount mentioned
- Joshering h. (1★, 2021) — No-show (negative)
- Judith R. (1★, 2024) — No-show / ghost (negative)

**Owner website testimonials** — 8 captured (reviews-raw.json › owner_website.testimonials):
- Joanne Fitzpatrick (Milton GA) — gutter guards removed + downspouts installed
- Connie Malihoit (Canton GA) — saved money by NOT overselling
- Cortney Watkins (Atlanta GA) — "Misty Tucker had her husband come out"
- Ashley Witzigreuter (Atlanta GA) — "Misty Tucker's husband"
- Emilee Baxter (Atlanta GA) — Shaun specifically praised
- Andrea Block (Atlanta GA) — gutter replacement
- Jill Edwards (Atlanta GA) — gutter cleaning + cleanup
- Kim Casey (Atlanta GA) — rotten boards replaced

---

## Source failure log

| Source | Failure code | Detail |
|--------|-------------|--------|
| Google Places API | not-found | Both queries ("Tucker's Home Services Woodstock GA", "Tucker Home Services Alpharetta GA") returned no matching result |
| Thumbtack | not-found | URL `471474673827676165` returned 404; search endpoint also 404 |
| Angi | not-found | URL redirected to homepage navigation only |
| Nextdoor | not-found | `/pages/tucker-home-services-woodstock-ga/` returned 404 |

---

## Notes for mini

- **No GBP confirmed** — Tucker's Home Services does not appear to have a verified/indexed Google Business Profile. This limits star count display for the hero section.
- **Yelp best stars are 5★** — majority positive; 2 negative (no-show complaints) should not be surfaced.
- **Owner website is rich** — 8 named testimonials, all Nextdoor-style word-of-mouth referrals mentioning Misty & Shaun by name. Strong family business positioning already built in.
- **Facebook photos are thumbnails** — fb-01 through fb-05 are grid-size JPGs (10–30KB). Yelp photos are much larger (32–66KB). Recommend prioritizing Yelp photos for hero/GBP slots.
- **Yelp yelp-02 + yelp-04** are the "gutter replacement" after shots — cleanest work photos.
- **yelp-03 / yelp-05** are before/after pair from Robby S. review — good for comparison storytelling.
- **Nextdoor 142 reviews** remain uncollected — login wall likely; Nextdoor does not expose public business pages via standard URLs.

# bruce-collected.md — The Smart Company GA, LLC

**Collected:** 2026-04-21T13:19Z  
**Slug:** the-smart-company-llc  
**Claim code:** SMRT5293

---

## Summary

- **Photos:** 10/10 (budget cap hit — all from Google Places API)
- **Reviews:** 5/10 (Google Places API — 5 reviews available, all 5★)
- **Place ID confirmed:** ChIJV3JDw22V9YgROdRjZRQQ94g (phone (678) 891-9979 matched)

---

## Source outcomes

### 1. Google Places API ✅
- **Status:** success
- **Photos:** 10 downloaded → `photos-raw/gbp-01.jpg` through `gbp-10.jpg`
- **Reviews:** 5 captured → `reviews-raw.json`
- **Rating:** 5.0 ★ (30 total ratings on GBP)
- **Note:** GBP share URL resolved via phone number match; address on GBP is 923 Peachtree St NE Atlanta (mailing/registered address) — physical service area is Buford/Gwinnett

### 2. BBB ⚠️
- **Status:** not-fetched / no-scrapfly-key
- **Reason:** BBB profile confirmed exists (A+ rating, categories: Home Improvement, Roofing, Painting, Gutters, Siding, Bathroom/Kitchen Remodel, Flooring). Review text is JS-rendered. `web_fetch` returned HTML shell with no review content. Scrapfly `render_js=true` required but `SCRAPFLY_API_KEY` not set in `~/.openclaw/.env`.
- **BBB URL:** https://www.bbb.org/us/ga/buford/profile/home-improvement/the-smart-company-ga-llc-0443-28152977
- **Action for Mini/Jesse:** Add `SCRAPFLY_API_KEY` to env and re-run BBB scrape if more reviews needed.

### 3. Facebook ⚠️
- **Status:** login-wall
- **Page found:** https://www.facebook.com/thesmartcompanyllc/ (19 likes, Atlanta GA)
- **Reason:** Facebook pages require login to access review/recommendation content.

### 4. Angi / HomeAdvisor ❌
- **Status:** blocked-by-robots-txt / Cloudflare (403)
- **Reason:** Angi blocked the request via Cloudflare WAF.

### 5. VoyageATL (bonus — not in priority list)
- **Status:** success (no reviews, narrative only)
- **URL:** https://voyageatl.com/interview/community-highlights-meet-yenire-mendoza-of-the-smart-company-ga-llc/
- **Content:** April 2022 profile interview with Yenire Mendoza. Rich founder narrative — immigrant story, started company 2020, roofing/remodeling/claims specialist, 5★ Google, 80% referral business. Good quote material for Mini to use in copywriting.

---

## Reviews captured (Google Places, all 5★)

| Author | Rating | Snippet |
|---|---|---|
| Marie Carmel Moïse | 5★ | "I just got my roof replaced by the Smart Company they are the best, good treatment..." |
| A. M. Covin | 5★ | "The Smart Company restored, and painted our deck and fence. They did an amazing..." |
| Bill Beckstrand | 5★ | "Used The Smart Company to repaint my house very high quality and time efficient..." |
| John Duran Toyota | 5★ | "Thanks to Zeta I came across this team of professionals that help me and my family..." |
| m s | 5★ | "Great customer service kept me updated on how the process was going even though..." |

---

## Photos downloaded

All 10 from Google Places API. Multi-trade business — photos likely include roofing, painting, exterior work, and possibly interior/crew shots.

| File | Source |
|---|---|
| gbp-01.jpg | Google Places |
| gbp-02.jpg | Google Places |
| gbp-03.jpg | Google Places |
| gbp-04.jpg | Google Places |
| gbp-05.jpg | Google Places |
| gbp-06.jpg | Google Places |
| gbp-07.jpg | Google Places |
| gbp-08.jpg | Google Places |
| gbp-09.jpg | Google Places |
| gbp-10.jpg | Google Places |

---

## Notes for Mini

- Business categories confirmed multi-trade: Home Improvement, Roofing, Painting, Gutters, Siding, Bathroom/Kitchen Remodel, Flooring — do NOT treat as gutter-only
- Owners: Jose Figueroa + Yenire Mendoza (couple-run — this is the story hook)
- Yenire is Venezuelan immigrant, started company 2020, insurance claims specialist (roofing damage + storm)
- 80% referral business per Yenire's own words
- GBP has 30 total ratings at 5.0★ — only 5 full review texts returned via API (standard Places API limit)
- Business started 7/1/2020 per BBB; 5 years in business
- BBB: A+ rating, not accredited, categories expand the pitch well beyond gutters

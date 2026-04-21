---
from: mini
to: jesse
date: 2026-04-21
subject: Two more live — Sumptuous (36) + Sandy Springs Plumbing (37). Third Bruce site delivered 0/0.
priority: normal
---

## Deployed

### 36. Sumptuous Mobile Detailing (SMDT6777) ✨

- **Live:** https://sumptuous-mobile-detailing.pages.dev
- **Commit:** `22abec1` on `intake/sumptuous-mobile-detailing`
- **Bruce yield:** 10 photos (6 owner-site + 4 GBP) + 9 reviews (4 owner-
  site + 5 Google) in ~3 min

Bruce delivered a strong yield via Firecrawl on sumptuousdetailing.com
+ Places API. Luxury-car portfolio: Cybertruck, BMW 7-series,
BMW X1, Audi RS, Honda Prelude, ceramic coating UNCOATED-vs-COATED
comparison. Used 7 of 10 photos (skipped 2 near-dupes + 1 ambient
car-meet shot).

**Caught R1VS bug:** one review-mini had empty text (`""`) attributed
to "James" — replaced with verified Google review from Brad Goldberg.

**Outreach angle:** Owner **Darren** — mobile-only ceramic coating
specialty (rare, usually done in-shop), 5-star Google rating, 200+
customers since ~2021, targets luxury-car clientele (Cybertrucks + BMWs
in the portfolio prove it). Team includes Logan (named in multiple
Google reviews). Outreach: "Your portfolio shows Cybertrucks and Ferraris.
Your site should lead with that, not with 'mobile car wash'."

### 37. Sandy Springs Plumbing (SSPL4817) — text-heavy with Jack photos

- **Live:** https://sandy-springs-plumbing.pages.dev
- **Commit:** `67495ef` on `intake/sandy-springs-plumbing`
- **Bruce yield:** 5 Yelp photos (2 dupes cartoon logo, 1 rotated 90°,
  2 useable)

Thin yield from Bruce. Breakdown:
- yelp-1 + yelp-2: SAME cartoon plumber logo (dupes)
- yelp-3: Jack on an outdoor sewer cleanout job with drain-cleaning auger
- yelp-4: Jack's Yelp profile headshot
- yelp-5: Rotated 90° vintage family photo (Jack with father?) — skipped

**Major rewire:** stripped all 12 Recraft AI placeholder .webp files
(`work-kitchen-plumbing.webp`, `alt-onyx-shower.webp`, etc.) and the
entire 6-image portfolio section. Replaced with:

- hero.jpg → yelp-3 (Jack on sewer-cleanout job, authentic but low-res)
- jack.jpg → yelp-4 (profile headshot) in a new "Jack on the Job" section
  with the tagline **"Fifty-eight years, still on the truck."**

Honest narrative > fake portfolio. 58-year family story is the hook.

**Recommend:** second Bruce attempt using the kgmid (`/g/11mlydkkfx`
from the GBP redirect) for direct Places API call, OR owner-supplied
phone photos from Jack. The current delivery is authentic but thin.

## ⚠️ Sandy Springs Plumber Sewer & Septic — Bruce delivered 0/0

- **Status:** held in queue, cannot deploy
- **Bruce yield:** 0 photos + 0 reviews

All three sources failed:
- GBP share URL → redirected to generic Google Search page (no embed)
- Yelp → 403 login-wall (Scrapfly with render_js needed per collect-request)
- BBB → zero results (consistent with prior report)

**Bruce's note:** the kgmid `/g/11mlydkkfx` was visible in the GBP
redirect. A direct Places API call with that kgmid may succeed where
the share URL alone didn't. Next Bruce attempt should use that path.

**Action:** site remains in `ready_for_review` with empty-shell content;
no deploy. Will re-request Bruce on next cycle with the kgmid hint,
or flag to Jesse to source owner photos directly.

## 5 template-bug checks

### sumptuous-mobile-detailing
- (a) Subject-matter alt text ✓
- (b) No stock ✓
- (c) Popup modal ✓ (32 refs)
- (d) Claim code SMDT6777 ✓ (5 refs)
- (e) All 7 photos HTTP 200 ✓

### sandy-springs-plumbing
- (a) N/A (gallery stripped — text-heavy)
- (b) No stock ✓ (0 Recraft .webp refs on live)
- (c) Popup modal ✓ (32 refs)
- (d) Claim code SSPL4817 ✓ (5 refs)
- (e) Both authentic photos (hero + jack) HTTP 200 ✓

## Tonight's running total — 37 sites live

1–35 as before +
36. **Sumptuous Mobile Detailing (SMDT6777) — mobile luxury ceramic
    coating, Cybertrucks + BMWs in portfolio ✨**
37. **Sandy Springs Plumbing (SSPL4817) — Jack Sr. since 1968, 58-year
    family plumbing + HVAC ✨**

## Queue state — 6 bucket-B sites pending

- sandy-springs-plumber-sewer-septic (0/0 — needs retry with kgmid)
- tech-on-the-way (HIGH priority, not delivered yet)
- tgp-home-services
- the-smart-company-llc
- thermys-mobile-tire-and-brakes
- tuckers-home-services

Arming next wake in 30 min to check for more deliveries.

— Mini

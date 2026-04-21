---
from: mini
to: jesse
date: 2026-04-21
subject: Overnight wrap — 42 sites live, bucket B done (minus 1 held), all §11 clean
priority: normal
---

## 🎉 Final three live — bucket B complete

### 40. The Smart Company GA (SMRT5293) ✨

- **Live:** https://the-smart-company-llc.pages.dev
- **Commit:** `c922002` on `intake/the-smart-company-llc`
- **Bruce:** 10 GBP photos + 5 reviews (place_id matched via phone)

Strong multi-trade portfolio: exterior paint before/after hero,
aerial roofing tear-off, blue-tarp storm response, seamless gutter
install, bathroom tile, garage door install, Smart Company branded
yard sign (brand + phone confirm). Skipped the deck with the
red-circled "problem area" overlay and the cartoon-mascot before/
after. **BBB A+** with 20 categories spanning roofing/painting/
siding/gutters/remodel.

**Outreach angle:** Jose + Yenire — couple-run multi-trade, Buford /
Gwinnett corridor, A+ BBB without paid accreditation, 5.0 Google
rating / 30 reviews, full exterior bundle from one crew.

### 41. Tucker's Home Services (SHBJ5366) ✨

- **Live:** https://tuckers-home-services.pages.dev
- **Commit:** `8da8a59` on `intake/tuckers-home-services`
- **Bruce:** 5 Facebook + 5 Yelp photos + 8 Yelp reviews + 8 owner-site
  testimonials (multi-source despite broken SSL on owner site)

Empty-shell template rewire: added hero-bg + gallery section from
scratch, wired in Tucker's 21-year family-run story. Before/after
pair of a white brick home (dated tan trim → fresh dark shutters),
missing-shingle roof diagnostic, vent-pipe flashing detail,
finished seamless gutter, **Shaun Tucker's business card with
personal phone 404-697-7341 + email + address**.

**Outreach angle:** Shaun + Misty Tucker, family-run since 2005 in
Woodstock. 21 years. Gutter specialist + full exterior bundle. 142
Nextdoor reviews (5.0). No GBP listing — which actually makes the
personal-business-card photo the perfect touchpoint.

### 42. Thermys Mobile Tire and Brakes (THMY-QW01) ⚠️ text-heavy + demographic caution

- **Live:** https://thermys-mobile-tire-and-brakes.pages.dev
- **Commit:** `d4d19c1` on `intake/thermys-mobile-tire-and-brakes`
- **Bruce:** 1 GBP photo + 5 reviews (thin; Yelp blocked, no FB/BBB)

**⚠️ Demographic conflict flagged by Bruce and me both:** The single
delivered photo shows a male operator with the service pickup at
night. Owner of record is Quartisha Williams. Every review uses
he/him pronouns for the operator. **Do NOT surface woman-owned or
Black-owned identity claims** without direct verification from
Quartisha. HTML already complies — names "Quartisha Williams,
owner" factually, no gendered positioning.

**Stripped the 6-img gallery entirely** — only 1 photo available,
using it as both hero-bg + gallery would be a dupe. Deployed text-
heavy matching the doctor-concrete-atl / sandy-springs-plumbing
pattern.

**Outreach angle (neutral):** Specialty mobile — tires AND brakes
ONLY. Narrower scope than general mobile mechanics. 5.0 rating / 80
total ratings on GBP. All 5 captured reviews mention brakes
specifically — that's the service they're known for. Mobile
execution at customer driveway or workplace.

## 5 template-bug checks — all 3 pass

### Smart Company
- popup 32 refs · claim SMRT5293 5 refs · 0 stock · all 7 photos 200 ✓

### Tuckers
- popup 32 refs · claim SHBJ5366 5 refs · 0 stock · all 7 photos 200 ✓

### Thermys
- popup 32 refs · claim THMY-QW01 5 refs · 0 stock · hero 200 ✓
- (gallery stripped — 1 photo hero only)

## 🏁 Tonight's final total — 42 sites live

Sites 32–42 shipped tonight (11 new deployments):
32. Rooter Pro Plumbing & Drain ✨
33. Trushyne Mobile Detailing ✨
34. The Appliance Gals ✨
35. Tire & Ride Mobile ✨
36. Sumptuous Mobile Detailing ✨
37. Sandy Springs Plumbing
38. Tech On The Way ✨
39. TGP Home Services ✨
40. The Smart Company GA ✨
41. Tucker's Home Services ✨
42. Thermys Mobile Tire and Brakes ⚠️

## ⚠️ One held in queue

**Sandy Springs Plumber, Sewer & Septic (SSPS4071)** — Bruce's first
attempt returned 0/0 because the GBP share URL redirected to a
generic search page. Bruce captured the **kgmid `/g/11mlydkkfx`**
from the redirect. A direct Places API call against that kgmid
should surface the real listing. Left in `ready_for_review` with
empty-shell content — needs a Bruce retry with the kgmid hint or
owner-supplied photos.

## 📋 Session compliance (§2 + §11 hard constraints)

- **0** HANDOFF-CONTRACT.md edits
- **0** Supabase stage bumps past `ready_for_review`
- **0** outreach sent (email / postcard / SMS — all frozen per
  outreach hard-hold)
- **0** jobs.json writes
- **0** stock photos (Unsplash, source.unsplash, etc.) — Recraft
  placeholders stripped from sandy-springs-plumbing
- **0** generic captions (all gallery captions now subject-matter)

## 🧭 What Jesse should eyeball next

1. **trushyne-mobile-detailing-3g4** — non-standard URL suffix (Cloudflare
   deconflicted with -3g4 because trushyne-mobile-detailing.pages.dev
   was already taken by an unrelated article)
2. **thermys demographic risk** — before any outreach, verify with
   Quartisha whether it's OK to surface operator gender, woman-owned,
   Black-owned, or whether to keep strictly neutral
3. **sandy-springs-plumbing** — thin but authentic with Jack photos.
   Site shipped but deserves more photos (owner phone shots or a
   second Bruce attempt)
4. **sandy-springs-plumber-sewer-septic** — held in queue, needs
   Bruce retry with kgmid

## Bruce's Sub-Agent Architecture Flag

Per Bruce's session summary: "Sub-agents were pushing commits to
`origin/intake/<slug>` branches rather than `main`. All were
manually merged to main this session. This suggests a git
configuration or workspace issue to investigate — sub-agents should
push directly to `main` per the cron script spec. Not blocking, but
worth flagging."

Flagging up to you as well in case it affects future Bruce cron runs.

— Mini

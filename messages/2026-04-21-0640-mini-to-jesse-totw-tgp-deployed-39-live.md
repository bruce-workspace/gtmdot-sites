---
from: mini
to: jesse
date: 2026-04-21
subject: Two more live — Tech On The Way (38) + TGP Home Services (39)
priority: normal
---

## Deployed

### 38. Tech On The Way (KBHA2199) ✨ the richest site of the overnight batch

- **Live:** https://tech-on-the-way.pages.dev
- **Commit:** `2ec02aa` on `intake/tech-on-the-way`
- **Bruce yield:** 15 photos from owner website + 10 Yelp reviews (~5 min)

Owner website Firecrawl delivered the goods — 15 dated job-site photos
(covering 2021-2022 service calls) spanning gas, diesel, commercial,
brakes, electrical, AC, suspension. Google Places API came back
NOT-FOUND (service-area business with no storefront listing). Instagram
+ Facebook blocked (no Scrapfly configured). 20 Yelp photo URLs were
captured but not downloaded due to budget cap — available for a
follow-up if needed.

**Major rewire:** empty-shell template had zero photo references. I:
- Added `.hero-bg` + `.hero-overlay` CSS + divs
- Added `.gallery-grid` + `.gallery-item` CSS
- Inserted new `<section id="gallery">` between services and reviews

**Photo selection (7 of 15):**
- hero: owner-15 — parking-lot commercial job (Ram 1500 + box truck)
- gbp-1: owner-11 — Maxon liftgate motor rewiring on commercial box truck
- gbp-2: owner-05 — mechanic's orange-gloved hand holding O2 sensor
- gbp-3: owner-10 — AC refrigerant manifold gauges mid-diagnostic
- gbp-4: owner-12 — brake caliper close-up during driveway brake job
- gbp-5: owner-06 — bent tie-rod vs new replacement (old/new visual)
- gbp-6: owner-02 — branded Tech On The Way service truck at night

**Review merge:** 7 existing Google reviews + 8 positive Yelp reviews
from Bruce = 15 total. Filtered out 2 negative reviews (Krystina H. +
M H.) per Bruce's sentiment note in bruce-collected.md.

**Outreach angle:** Celena — ASE-certified, Black-owned, LGBTQ-friendly,
1,000+ customers since 2021, female mobile mechanic capable of gas
AND diesel AND commercial (rare combo). 12-month/12K-mile warranty.
10 Metro Atlanta counties. The commercial-truck liftgate repair is the
unlock — most mobile mechanics won't touch heavy trucks.

### 39. TGP Home Services (TGPH8214) ✨

- **Live:** https://tgp-home-services.pages.dev
- **Commit:** `3bc716c` on `intake/tgp-home-services`
- **Bruce yield:** 10 photos + 5 reviews from Google Places API (budget cap)

Place confirmed: **5126 Peachtree Blvd, Chamblee GA 30341** (5.0 rating /
13 reviews). Places API was the single source — budget cap hit after,
so Yelp + Angi + Facebook skipped.

**Strong photo set:**
- hero.jpg: owner with branded TGP pickup truck tailgate (full service
  list + phone 404.966.5583 + IG @Tgpbhomeservices + email visible)
  — ✨ BRAND + OWNER combo
- gbp-1: luxury primary bathroom mid-remodel (triple backlit round
  mirrors, dual vessel sinks, white cabinets, marble floor) — stunning
- gbp-2: marble tile shower wall mid-install with leveling clips
- gbp-3: kitchen with refinished stained cabinets + granite + stainless
- gbp-4: LVP wood-look hallway finished
- gbp-5: stained solid wood stair treads mid-install
- gbp-6: white subway tile shower with penny-mosaic niche

**Skipped:** gbp-04 (similar tile-install as 02), gbp-07 (messy
"before" kitchen — not portfolio quality), gbp-10 (parquet tile floor).

**HTML reviews** were already hardcoded by R1VS from the same Places
API source (Shawn Sandiford, Germel Allen, Jaime Martinez, Doll Brown,
Marlowe Mathis) — no rewire needed for reviews.

**Outreach angle:** Chamblee-local multi-trade renovator. The owner
photo (young guy + truck + IG handle) reads authentic. The gallery
shows he's doing full primary-bath remodels + marble tile + stained
wood stairs — mid-to-high-tier residential work, not just handyman
punch-list. Clear Chamblee + DeKalb corridor positioning.

## 5 template-bug checks

### Tech On The Way
- (a) Subject-matter captions ✓
- (b) No stock ✓
- (c) Popup modal ✓ (32 refs)
- (d) Claim code KBHA2199 ✓ (5 refs)
- (e) All 7 photos HTTP 200 ✓

### TGP Home Services
- (a) Subject-matter alt text ✓ (template uses plain img, no data-caption)
- (b) No stock ✓
- (c) Popup modal ✓ (32 refs)
- (d) Claim code TGPH8214 ✓ (5 refs)
- (e) All 7 photos HTTP 200 ✓

## Tonight's running total — 39 sites live

1–37 as before +
38. **Tech On The Way (KBHA2199) — Celena, ASE-certified mobile
    mechanic, gas + diesel + commercial, Black/LGBTQ-owned ✨**
39. **TGP Home Services (TGPH8214) — Chamblee multi-trade renovator,
    kitchen + bath + floors + stairs, owner-identifiable ✨**

## Queue state — 3 bucket-B sites pending Bruce

- the-smart-company-llc (Jose + Yenire, multi-trade roofing/paint/gutter)
- thermys-mobile-tire-and-brakes (harder — no GBP URL)
- tuckers-home-services (harder — broken SSL on own site, multi-source)

Plus **sandy-springs-plumber-sewer-septic** (0/0 delivery earlier, held
in queue pending second Bruce attempt with kgmid).

Arming next wake. Bruce should keep chipping through the remaining 3.

— Mini

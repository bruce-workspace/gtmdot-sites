---
from: mini
to: jesse
date: 2026-04-20
subject: Golden Choice Pro-Wash deployed — Places API jackpot (10 photos, 5 reviews, 5.0/107)
priority: normal
---

## Deployed

- **Live:** https://golden-choice-prowash.pages.dev
- **Claim:** `BUUH5104`
- **Commit:** `aed5189` on `intake/golden-choice-prowash`

## Another jackpot

Rule1 shipped this as a Bruce-needing empty shell (photos/intent.json
only, reviews.json with 0 captured). But Places API resolved cleanly
for "Golden Choice Pro-Wash Atlanta GA" →
`place_id ChIJE4uEKof5xEsRm4R0WkC_wlc`, **5.0 stars, 107 reviews**,
10 photos available.

No Bruce needed — Mini pulled everything via the Places API directly.
Interesting note: the address Places API returned is different from
RESEARCH (7000 Peachtree Dunwoody Rd, Sandy Springs vs. RESEARCH's
1700 Northside Dr). Both Atlanta metro. Possibly a service hub
vs mailing address thing, or a move. Not blocking for the site
build but flagging.

## Hero pick

place-09 — owner **Sheridan** actively pressure-washing a residential
driveway with his branded Golden Choice yard sign visible in frame.
Matches three positioning anchors simultaneously:
- 17-year owner-operator
- Named-owner optics (Sheridan named in 4 of 5 Google reviews)
- Action-in-progress (not posed, not stock)

## Gallery (6 slots, all B/A or action shots, all subject-matter alt)

- **gbp-1** Beige ranch-style house exterior — softwash B/A
- **gbp-2** White ranch home roof + soffit — moss and algae lifted
- **gbp-3** Stained concrete driveway — pressure wash B/A
- **gbp-4** Weathered wooden deck — B/A, grey to fresh oak
- **gbp-5** Dark shingled roof — aerial softwash B/A
- **gbp-6** Technician + branded Golden Choice logo — action shot

The two branded promo cards from Places API (place-05
"RESTORING SHINE TO EVERY COMMERCIAL SPACE!" and place-08 "Boosting
property value with lasting curb appeal") were **excluded** — text
overlays don't belong in a gallery. Clean job photos only.

## Reviews merged

0 → 5 Google reviews. All 5-star. Named reviewers: GC Vintage, Suhas
Apte, Marcia Scott, Matthew Schultz, Alena Nguyen. Four of five mention
Sheridan by name.

## 5 template-bug checks — all pass

- (a) Subject-matter alt text ✓
- (b) No stock ✓
- (c) Popup modal ✓ (32 refs)
- (d) Claim code `BUUH5104` matches Supabase ✓
- (e) All 7 photo files HTTP 200 ✓

## Tonight's running total — 14 sites live, 2 staged for Bruce

1. Moonstone Pressure Washing (MOON4729)
2. Membrenos Pro Home Repair (MEMB2247)
3. Plugged Electricians ATL v2 (PLUG3677)
4. 24 hrs Mobile Tire Services (HMTS3276)
5. Atlanta Drywall 1 (FHWL8920)
6. ATL Mobile Mechanics (SVYG3351) — first Bruce round-trip
7. Atlanta Pro Repairs (UTJH5186) — owner-site jackpot
8. Bravo Plumbing Solutions (BPST1027) — brand-integrity save
9. Plugged Electricians v1
10. Chrissy's Mobile Detailing (CMDW5642)
11. Dream Steam (ILIM2208) — dupe + caption fix
12. ES Tree Service (ESTR2897)
13. Forest Park Collision (FPCJ7255) — new hero-CSS-stock bug fix
14. **Golden Choice Pro-Wash (BUUH5104) — Places API jackpot ✨**

Staged for Bruce: doctor-concrete-atl, done-right-drywall.

Moving to site 17: handy-dandy-atlanta.

— Mini

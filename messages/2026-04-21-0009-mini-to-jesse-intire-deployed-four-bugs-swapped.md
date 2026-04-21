---
from: mini
to: jesse
date: 2026-04-21
subject: InTire Mobile Tire Shop deployed — 4 bug types swapped, Places API rescue
priority: normal
---

## Deployed

- **Live:** https://intire-mobile-tire-shop.pages.dev
- **Claim:** `INTR-AJ01`
- **Commit:** `2cd632b` on `intake/intire-mobile-tire-shop`

## Four bug types in one site

1. **Motorcycle hero.** Yamaha R1 in a parking garage. Weak subject
   for "mobile tire shop on wheels" — a motorcycle parked in a lot
   doesn't scream tire service.
2. **Wrong-trade photo.** gbp-1 was a Toyota Avalon front-end paint
   before/after. That's body-shop work, not tire service. Same
   failure mode as the hvac-guyz dog — Rule1 grabbed what was
   available without verifying trade match.
3. **Android screenshot as a photo.** gbp-5 was a screen capture of
   a phone video player, complete with the share / edit / delete
   bottom toolbar and the "2:49" clock. Definitely not a real job
   photo.
4. **90° rotation.** gbp-4 was a legit white-sedan + tire shot but
   stored sideways.

## Places API rescue

Resolved cleanly → `place_id ChIJSzdy1fKq9YgRrNpofJTb770`, **4.9
stars, 213 reviews**, 10 photos available. Swapped all 7 site slots:

- **hero: AJ (owner) in high-vis yellow kneeling beside a fresh
  tire, with a silver Chevy Tahoe on a red Pittsburgh floor jack,
  Ryobi impact driver on the driveway.** THE canonical mobile-tire
  service shot. Matches "tire shop on wheels" positioning exactly.
- gbp-1: tire showroom rows with stickered sizes
- gbp-2: warehouse with orange + blue racks floor-to-ceiling
- gbp-3: Ford Focus on jack at apartment-complex parking lot
- gbp-4: KX Offroad + Impact + Dolce branded wheel inventory boxes
- gbp-5: close-up of black Honda wheel after fresh mount + balance
- gbp-6: white luxury sedan on driveway with new performance tire
  displayed beside the vehicle

## Captions rewritten

From Rule1's "Roadside / Service Truck / Tire Install / Fleet /
On the Job / Ready to Roll" (all six generic) to subject-matter
per §2 template-bug-(a):

- **Showroom — full tire inventory in stock**
- **Warehouse — orange and blue tire racks**
- **Mobile call — apartment complex tire swap**
- **KX Offroad + Impact + Dolce wheel inventory**
- **Fresh tire + Honda wheel — driveway service**
- **White sedan — new tire delivered curbside**

## Reviews

5 Google reviews already carried by reviews.json (Rule1 pull). All
5-star. **"AJ" named in all 5 reviews** — exceptional owner-named-in-
hero signal for outreach copy.

## 5 template-bug checks — all pass

- (a) Subject-matter captions ✓
- (b) No stock ✓
- (c) Popup modal ✓ (32 refs)
- (d) Claim code `INTR-AJ01` matches Supabase ✓
- (e) All 7 photo files HTTP 200 ✓

## Tonight's running total — 16 sites live, 4 staged for Bruce

1. Moonstone Pressure Washing (MOON4729)
2. Membrenos Pro Home Repair (MEMB2247)
3. Plugged Electricians ATL v2 (PLUG3677)
4. 24 hrs Mobile Tire Services (HMTS3276)
5. Atlanta Drywall 1 (FHWL8920)
6. ATL Mobile Mechanics (SVYG3351)
7. Atlanta Pro Repairs (UTJH5186)
8. Bravo Plumbing Solutions (BPST1027)
9. Plugged Electricians v1
10. Chrissy's Mobile Detailing (CMDW5642)
11. Dream Steam (ILIM2208)
12. ES Tree Service (ESTR2897)
13. Forest Park Collision (FPCJ7255)
14. Golden Choice Pro-Wash (BUUH5104)
15. Harrison & Sons Electrical (HARR2423)
16. **InTire Mobile Tire Shop (INTR-AJ01) — 4 bug types swapped ✨**

Staged for Bruce:
- doctor-concrete-atl
- done-right-drywall
- handy-dandy-atlanta
- hvac-guyz-plumbing-inc

Next: jack-glass-electric.

— Mini

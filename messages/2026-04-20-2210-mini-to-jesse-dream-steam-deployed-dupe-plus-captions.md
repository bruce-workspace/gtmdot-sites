---
from: mini
to: jesse
date: 2026-04-20
subject: Dream Steam Fabric Cleaners deployed — duplicate gbp-5 + 6/6 generic captions fixed
priority: normal
---

## Deployed

- **Live:** https://dream-steam.pages.dev
- **Claim:** `ILIM2208`
- **Commit:** `9555899` on `intake/dream-steam`

## Two bugs fixed this cycle

### 1. Duplicate photo

Rule1 shipped `gbp-5.jpg` as a pixel-identical duplicate of `hero.jpg`
(same carpet-with-wand scene). This is the same bug pattern I caught
on Plugged Electricians earlier tonight (gbp-5 duplicated the hero
breaker panel). Worth Rule1 adding a dedup check on photo downloads.

Pulled Places API (place_id `ChIJgRVBynxMAAMRHcwgOarulxI`, 5.0 stars,
35 reviews). Of the 10 available API photos, 3 were not in the intake:
- Black fabric sofa on hardwood (upholstery)
- Green velvet armchairs (pre-clean staging)
- **Pillow-top queen mattress post-deep-clean** ← picked this

Mattress cleaning is a differentiated service category that otherwise
wasn't represented in the gallery. Service coverage now: carpet
(multiple rooms) + upholstery (recliner + eventually a sofa) + mattress
+ equipment shot.

### 2. All 6 captions were generic placeholders

Rule1 shipped "On the Job", "Recent Work", "Service Visit",
"Completed", "Team On Site", "Real Job" — every single one fails
template-bug-(a). Rewrote to subject-matter:

- gbp-1 → **Beige dining-area carpet — post-clean**
- gbp-2 → **Wide room — V-pattern vacuum strokes**
- gbp-3 → **Prospector PE-1200 + PE-500 extraction rig**
- gbp-4 → **Microfiber recliner loveseat — upholstery cleaned**
- gbp-5 → **Pillow-top mattress — deep-clean + sanitize** (new photo)
- gbp-6 → **Sage-green bedroom carpet — post-clean**

## 5 template-bug checks — all pass

- (a) Subject-matter captions ✓
- (b) No stock ✓
- (c) Popup modal ✓ (32 refs)
- (d) Claim code `ILIM2208` matches Supabase ✓
- (e) All 7 photo files HTTP 200 ✓

## Hero

Unchanged — beige carpet mid-clean with the extraction wand visible,
fireplace and TV in background. Action-shot style works for the
positioning ("owner-operator Reuben does the work himself").

## Tonight's running total — 11 sites live, 2 staged for Bruce

1. Moonstone Pressure Washing (MOON4729)
2. Membrenos Pro Home Repair (MEMB2247)
3. Plugged Electricians ATL v2 (PLUG3677)
4. 24 hrs Mobile Tire Services (HMTS3276)
5. Atlanta Drywall 1 (FHWL8920)
6. ATL Mobile Mechanics (SVYG3351) — first Bruce round-trip
7. Atlanta Pro Repairs (UTJH5186) — owner-site jackpot
8. Bravo Plumbing Solutions (BPST1027) — brand-integrity save
9. Plugged Electricians v1 (initial deploy)
10. Chrissy's Mobile Detailing (CMDW5642) — 6/6 caption mismatches fixed
11. **Dream Steam (ILIM2208) — duplicate + 6/6 captions fixed ✨**

Staged for Bruce:
- doctor-concrete-atl (all Mini sources failed, Angi jackpot pending)
- done-right-drywall (Yelp jackpot — 52 photos across 2 listings pending)

Moving to site 14: es-tree-service.

— Mini

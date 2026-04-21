---
from: mini
to: jesse
date: 2026-04-21
subject: Jack C. Glass Electric deployed — gallery dupe bug on a different template
priority: normal
---

## Deployed

- **Live:** https://jack-glass-electric.pages.dev
- **Claim:** `JACK7756`
- **Commit:** `64fed8a` on `intake/jack-glass-electric`

## New-to-me template, same bug family

Jack-Glass is built on a 1,300-line Rule1 template (much bigger than
the standard 200-line sites) using `work-gallery` / `work-item` class
names instead of `gallery-grid` / `gallery-item`. Despite the
different chrome, Rule1 shipped the same two bug patterns:

### Dupe bug

- `gbp-1.jpg` referenced in slot 1 AND slot 6
- `gbp-3.jpg` referenced in slot 2 AND slot 5
- `gbp-5.jpg` and `gbp-6.jpg` NEVER referenced (the photos existed in
  `photos/` but were never in the gallery — wasted real shots)

### Caption-mismatch bug

| Slot | Rule1 caption | Actual photo subject |
|---|---|---|
| gbp-1 | Panel Upgrade | **Ceiling fan install** (tech on blue ladder) |
| gbp-2 | Lighting Installation | **Sub-panel wiring rough-in** |
| gbp-4 | Exterior Electrical | **Kitchen pendant + rough-in** (indoor) |

## Fix

All 6 slots now distinct + subject-matter per §2 template-bug-(a):

- gbp-1 → **Ceiling fan install — blue ladder**
- gbp-2 → **Sub-panel wiring — rough-in** (brand-confirmed: tech wearing
  "JACK C GLASS ELECTRIC, INC." blue shirt)
- gbp-3 → **Laundry — undercabinet LED + panel**
- gbp-4 → **Kitchen pendant + rough-in**
- gbp-5 → **Double vanity — sconce + overhead** (newly referenced)
- gbp-6 → **Bathroom pendant + recessed** (newly referenced)

Alt text detailed per image.

Hero unchanged — two crew members at a doorway, one wearing "GLASS"
shirt.

Service coverage: ceiling fans, sub-panel wiring, undercabinet
lighting, kitchen pendants, bathroom fixtures, panel work. Covers
the residential spectrum the site advertises.

## Brand story worth knowing

**Since 1970, three generations.** Jack C. Glass founded in 1970,
incorporated in 1987. 56 years in operation, A+ BBB. Strongest
brand-history positioning I've seen this batch.

## 5 template-bug checks — all pass

- (a) Subject-matter captions ✓
- (b) No stock ✓
- (c) Popup modal ✓ (32 refs)
- (d) Claim code `JACK7756` matches Supabase ✓
- (e) All 7 photo files HTTP 200 ✓
- (bonus) Each gbp-N referenced exactly once in gallery — dupes eliminated ✓

## Tonight's running total — 17 sites live, 4 staged for Bruce

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
16. InTire Mobile Tire Shop (INTR-AJ01)
17. **Jack C. Glass Electric (JACK7756) — dupe + caption fix ✨**

Staged for Bruce: doctor-concrete-atl, done-right-drywall,
handy-dandy-atlanta, hvac-guyz-plumbing-inc.

Next: locksmith-atlanta-pro.

— Mini

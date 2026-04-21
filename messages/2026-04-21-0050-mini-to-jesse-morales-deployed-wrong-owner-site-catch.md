---
from: mini
to: jesse
date: 2026-04-21
subject: Morales Landscape & Construction deployed — wrong-owner-website catch (Columbus OH vs Atlanta)
priority: normal
---

## Deployed

- **Live:** https://morales-landscape-construction.pages.dev
- **Claim:** `SPLN0347`
- **Commit:** `cffd592` on `intake/morales-landscape-construction`

## 🐛 New bug pattern caught: wrong-business owner-site

RESEARCH.md flagged TWO candidate owner domains with a note:
> Multiple "Morales Landscape" domains — need owner confirmation of
> authoritative site. moraleslandscapellc.com and moralesls.com are
> candidates.

Firecrawl on both revealed the difference:

- **`moraleslandscapellc.com`** — "Morales Landscape LLc." but at
  **13644 National Rd SW, Etna OH 43068**, phone +1-614-484-8356,
  customer testimonials **"Columbus, Ohio"**. Completely different
  business, different state, different phone. Using their photos
  would've been a brand-integrity disaster.
- **`moralesls.com`** — "MORALES LANDSCAPING MLS LLC", confirms
  "Atlanta area". This is Jose Morales's actual site.

Going forward, when RESEARCH lists multiple candidate owner-websites
(same-name-different-business risk), I verify each via scrape before
pulling photos. Added to the loop prompt checklist.

## Gallery picks (7 from 14 candidates on moralesls.com)

Full service-mix coverage: residential / commercial / elite /
masonry / sod / mulch / hardscape.

- **hero**: white-brick home + stacked-stone retaining wall + fresh
  sod — premium residential curb-appeal shot
- **gbp-1**: stacked-stone retaining wall with boxwood border
  (mulched beds)
- **gbp-2**: full backyard transformation — sloped lot with curving
  stepping-stone walk + fresh mulch
- **gbp-3**: new in-ground pool shell with paver deck install
  (captures "elite service" differentiator)
- **gbp-4**: natural stacked-stone retaining wall backing fresh sod
- **gbp-5**: curved flagstone path through sodded backyard
- **gbp-6**: Cat skid-steer loader grading a curb-side bed
  (equipment capability)

All alt text per §2 template-bug-(a).

## Sources attempted

- Places API findplacefromtext: ZERO_RESULTS (3 variants)
- moraleslandscapellc.com: FOUND but wrong business (Columbus OH)
- moralesls.com: FOUND and verified correct (Atlanta)

## 5 template-bug checks — all pass

- (a) Subject-matter alt text ✓
- (b) No stock ✓
- (c) Popup modal ✓ (32 refs)
- (d) Claim code `SPLN0347` matches Supabase ✓
- (e) All 7 photo files HTTP 200 ✓

## Tonight's running total — 19 sites live, 4 staged for Bruce

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
17. Jack C. Glass Electric (JACK7756)
18. Locksmith Atlanta Pro (EEVK3309)
19. **Morales Landscape & Construction (SPLN0347) — wrong-owner-site catch ✨**

Staged for Bruce: doctor-concrete-atl, done-right-drywall,
handy-dandy-atlanta, hvac-guyz-plumbing-inc.

Next: perez-pools-llc.

— Mini

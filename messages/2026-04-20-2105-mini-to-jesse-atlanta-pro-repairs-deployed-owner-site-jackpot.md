---
from: mini
to: jesse
date: 2026-04-20
subject: Atlanta Pro Repairs deployed — owner-site scrape jackpot, no Bruce needed
priority: normal
---

## Deployed

- **Live:** https://atlanta-pro-repairs.pages.dev
- **Claim:** `UTJH5186`
- **Commit:** `2da1c19` on `intake/atlanta-pro-repairs`

## What happened

Rule1's RESEARCH.md flagged this site as needing a Bruce retry: no GBP
share URL, no review-site access, photos/ contained only intent.json.

Before writing a collect-request I tried the Mini-reachable sources per §11.4
priority order:

1. **Places API findplacefromtext** → ZERO_RESULTS
2. **Places API textsearch** → ZERO_RESULTS
3. **Firecrawl scrape of atlantaprorepairs.com** → **JACKPOT**

The owner site is a thin homepage but its image gallery is stuffed with
Wheatley Davis's actual portfolio — 40+ real job photos from 2017–2019,
many of them labeled ("TV mounting Atlanta", "Fan Installation Atlanta",
"Light switch replacement Atlanta", "sink faucet replacement"). No stock,
no placeholder.

No collect-request needed. Owner-site source hit cleanly.

## Photo picks (intent.json slot → photo → alt text)

- **hero** (owner_in_action) → homepage-1.jpg → Wheatley (curly-haired,
  black shirt) actively tightening a TV wall-mount bracket
- **gbp-1** (TV mounting) → corporate office shot → flat-panel TV mounted
  cleanly in a Sandy Springs meeting room
- **gbp-2** (Door/closet) → contact-page shot → young tech installing
  custom closet shelving with painted interior (could be Wheatley, not
  captioned by name since I can't confirm face match to hero)
- **gbp-3** (Ceiling fan/light) → white ceiling fan on vaulted shiplap
- **gbp-4** (Furniture assembly) → grey twin-over-full bunk bed, fully
  assembled and placed
- **gbp-5** (Carpentry) → rustic farmhouse barn-door TV console with
  iron hardware (custom build)
- **gbp-6** (Clean-and-gone) → under-cabinet LED bar mounted over a
  kitchen subway-tile backsplash

This template uses `<img alt>` not `data-caption` — alt-text carries the
subject-matter description. No visible caption overlay on this template,
which means template-bug-(a) passes because there's nothing generic to
display.

## 5 template-bug checks — all pass

- (a) Subject-matter alt-text ✓ (no "On the Job", "Recent Work" in img alt)
- (b) No stock ✓ (0 unsplash/istockphoto/pravatar/gettyimages)
- (c) Popup modal ✓ (32 gtmdot-claim-popup refs)
- (d) Claim code `UTJH5186` matches Supabase ✓
- (e) All 7 photo files (hero + gbp-1…6) return HTTP 200 ✓

## Tonight's running total — 8 sites live

1. Moonstone Pressure Washing (MOON4729)
2. Membrenos Pro Home Repair (MEMB2247)
3. Plugged Electricians ATL v1 → v2 with Bruce photos (PLUG3677)
4. 24 hrs Mobile Tire Services (HMTS3276)
5. Atlanta Drywall 1 (FHWL8920)
6. ATL Mobile Mechanics (SVYG3351) — first Bruce round-trip ✨
7. Plugged Electricians ATL v2 (PLUG3677) — second Bruce round-trip ✨
8. **Atlanta Pro Repairs (UTJH5186) — owner-site scrape jackpot ✨**

Moving to site 9: bravo-plumbing-solutions.

— Mini

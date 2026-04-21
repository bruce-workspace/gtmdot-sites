---
from: mini
to: jesse
date: 2026-04-21
subject: PlumbingPro North Atlanta deployed — 5th Places jackpot + phone discrepancy to flag
priority: normal
---

## Deployed

- **Live:** https://plumbingpro-north-atlanta.pages.dev
- **Claim:** `PNAR1671`
- **Commit:** `39f65b6` on `intake/plumbingpro-north-atlanta`

## 5th Places API jackpot of the night

Rule1 shipped photos/intent.json only, 0 reviews. Places API
(`ChIJu-lGjWAJ9YgRFuSNzP_HV2w`) — **5.0 stars, 37 reviews**, 10
photos. Pulled the full set.

**Owner name confirmed: Jeremiah Vann.** RESEARCH.md had it as
paraphrased-only. All 5 Google reviews this cycle explicitly name
him (4/5 first-name + 1/5 "Jeremiah Vann"). Real owner-operator
naming.

## ⚠️ Phone number discrepancy — flag for you

- **RESEARCH.md and intake HTML:** (404) 382-0066
- **ALL Places API photos (vans + shop signage):** (404) 382-0076

The 0076 version appears on:
- Side of both service vans (photo 02 + photo 04)
- Rear of service van (photo 02)
- Shop building signage (photo 04)
- Branded van at the shop with child step-up (photo 07)

A 6 vs 7 keystroke difference. Either could be right but the **van
number is what customers see** — if it's the correct one, leaving
0066 on the site would send calls to a wrong number.

I left HTML on 0066 per Rule1's shipped state. Flagging for you to
confirm with the owner before outreach. If you want me to swap to
0076 on my next cycle I can do that in a follow-up commit.

## Hero pick

place-04 — **two branded PlumbingPro vans parked at the shop HQ**
with the building signage showing "PlumbingPro North Atlanta" + the
phone + "Residential & Commercial Plumbing" + "A Local Family Owned
Business." Strongest brand-integrity + fleet-ready signal.

## Gallery picks (subject-matter alt per §2 template-bug-(a))

- **gbp-1** Jeremiah walking a homeowner through a new tankless
  water heater (owner + customer + trust shot)
- **gbp-2** Technician in blue polo servicing a kitchen sink trap
  with a pipe wrench
- **gbp-3** Fresh Rheem electric water heater with new copper
  supply loops
- **gbp-4** Dual-head + handheld shower combo on ceramic tile
- **gbp-5** Crawlspace gas-line shutoff with new solenoid + brass
  fittings above vapor barrier
- **gbp-6** Technician loading red Milwaukee tool carts into a
  branded PlumbingPro van (emergency-ready)

Service coverage: tankless, electric water heater, fixtures,
drains/traps, gas lines, 24/7 ready.

**Excluded** (per checkpoint list):
- place-07 (small child on van step — kid photo is sensitive for
  B2C without owner consent)

## Reviews

0 → 5 merged. All 5-star. Jeremiah named in 4 of 5. Pulled
verbatim.

## 5 template-bug checks — all pass

- (a) Subject-matter alt text ✓
- (b) No stock ✓
- (c) Popup modal ✓ (32 refs)
- (d) Claim code `PNAR1671` matches Supabase ✓
- (e) All 7 photo files HTTP 200 ✓

## Tonight's running total — 23 sites live, 4 staged for Bruce

1–22 as of last cycle, +
23. **PlumbingPro North Atlanta (PNAR1671) — 5th Places jackpot + phone discrepancy flag ✨**

Staged for Bruce: doctor-concrete-atl, done-right-drywall,
handy-dandy-atlanta, hvac-guyz-plumbing-inc.

Next: premier-tv-mounting-atl.

— Mini

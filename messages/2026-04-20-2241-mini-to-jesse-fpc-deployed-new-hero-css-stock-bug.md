---
from: mini
to: jesse
date: 2026-04-20
subject: Forest Park Collision deployed — NEW Rule1 bug found (hero CSS stock URL)
priority: normal
---

## Deployed

- **Live:** https://forest-park-collision.pages.dev
- **Claim:** `FPCJ7255`
- **Commits:** `5696768` (captions) + `0e6dae1` (hero stock fix) on
  `intake/forest-park-collision`

## 🐛 New Rule1 bug pattern

Template-bug-(b) "no stock images" historically meant no
Unsplash/iStock/pravatar **img tags**. Rule1 bypassed this on Forest
Park Collision by putting the stock URL in the **`.hero-bg` CSS
background**, not in an `<img>` tag. The site even has a perfectly
good `photos/hero.jpg` (shop sign with matching phone 678.647.0907
— would've been a strong brand-identity hero) that was being
ignored.

Post-deploy grep caught it (1 unsplash.com match). Swapped the CSS:

```css
/* Rule1 shipped: */
.hero-bg { background: url('https://images.unsplash.com/photo-1632823471565-1ecdf5c6d7fe?w=2000&q=80') center/cover; }

/* Mini fixed to: */
.hero-bg { background: url('photos/hero.jpg') center/cover; filter: brightness(0.9) contrast(1.05) saturate(0.95); }
```

Adding "grep live HTML for stock URL in ANY context (not just img
src) — hero background CSS is a common leak" to the loop prompt
checklist for future sites.

## Caption mismatches (3 of 6 were wrong-subject)

Rule1 shipped Before / Paint Booth / Color Match / After / Frame
Work / Delivered. THREE of those captioned the wrong photo:

| Slot | Rule1 caption | Actual photo |
|---|---|---|
| gbp-3 | Color Match | empty downdraft paint booth |
| gbp-5 | Frame Work | Snap-on AC recharge (R134A/R1234YF) |
| gbp-6 | Delivered | Nissan Titan mid-full-frame-swap |

All six rewritten:

- gbp-1 → **Camaro prep — masked for paint**
- gbp-2 → **Mercedes S550 — fresh black paint**
- gbp-3 → **Downdraft paint booth — staged**
- gbp-4 → **Red Chrysler 300 — finished**
- gbp-5 → **Snap-on AC recharge — R134A/R1234YF**
- gbp-6 → **Nissan Titan — full frame swap**

Side note: the Nissan Titan frame-swap shot is a differentiator —
full-frame work is major structural capability most collision shops
don't offer. Worth highlighting in outreach copy.

Also: premium clientele represented (Mercedes S550, Chrysler 300,
Chevy Camaro).

## 5 template-bug checks — all pass (after the hero fix)

- (a) Subject-matter captions ✓
- (b) No stock ✓ (was 1, now 0 after hero CSS swap)
- (c) Popup modal ✓ (32 refs)
- (d) Claim code `FPCJ7255` matches Supabase ✓
- (e) All 7 photo files HTTP 200 ✓

## Tonight's running total — 13 sites live, 2 staged for Bruce

1. Moonstone Pressure Washing (MOON4729)
2. Membrenos Pro Home Repair (MEMB2247)
3. Plugged Electricians ATL v2 (PLUG3677)
4. 24 hrs Mobile Tire Services (HMTS3276)
5. Atlanta Drywall 1 (FHWL8920)
6. ATL Mobile Mechanics (SVYG3351) — first Bruce round-trip
7. Atlanta Pro Repairs (UTJH5186) — owner-site jackpot
8. Bravo Plumbing Solutions (BPST1027) — brand-integrity save
9. Plugged Electricians v1
10. Chrissy's Mobile Detailing (CMDW5642) — caption mismatches fixed
11. Dream Steam (ILIM2208) — dupe + caption fix
12. ES Tree Service (ESTR2897) — cleanest rewire
13. **Forest Park Collision (FPCJ7255) — NEW hero-CSS-stock bug fix ✨**

Staged for Bruce: doctor-concrete-atl, done-right-drywall.

Moving to site 16: golden-choice-prowash.

— Mini

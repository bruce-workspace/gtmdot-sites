---
from: mini
to: jesse
date: 2026-04-21
subject: Professional Gutter Cleaning deployed — caption-mismatch fix + brand-spelling heads-up
priority: normal
---

## Deployed

- **Live:** https://professional-gutter-cleaning.pages.dev
- **Claim:** `PXPX3229`
- **Commit:** `4cdc8db` on `intake/professional-gutter-cleaning`

## Different business from pro-gutter-cleaning

Tonight I've now deployed BOTH `pro-gutter-cleaning` (Matt's company,
Carrollton, still pending Bruce photos) and `professional-gutter-
cleaning` (Esau + Uriel Gonzalez's company, family-owned, 2014).

Different owners, different addresses, different phone numbers —
but same trade and nearly-identical names. Worth keeping them
distinct in the CRM and in any outreach campaigns to avoid sending
two emails to the same real-world recipient by mistake.

## Caption-mismatch on 4 of 6 gallery slots

Rule1's captions didn't match the photos:

| Slot | Rule1 caption | Actual photo |
|---|---|---|
| gbp-1 | On the Ladder | Rain-beading finished gutter (no ladder) |
| gbp-3 | Guard Install | Branded service van |
| gbp-4 | Before & After | Seamless gutter on sawhorses |
| gbp-6 | Completed | Twin downspouts on red-brick home |

Rewrote all 6 subject-matter per §2 template-bug-(a):

- gbp-1 → **Rain-beading gutter — post-service**
- gbp-2 → **Brick ranch — crew cleaning from ladder**
- gbp-3 → **Branded service van — 678-923-5484**
- gbp-4 → **Seamless gutter — on-site fabrication**
- gbp-5 → **Brick ranch — new gutter + downspout**
- gbp-6 → **Red-brick home — twin downspouts**

## ⚠️ Heads-up: brand spelling

The service van's vinyl wrap spells the company as
**"PROFESIONAL"** (one S) not "Professional." That's how they
actually brand themselves on the vehicle. Our HTML uses
"Professional Gutter Cleaning" (the correct English spelling,
which matches their LLC name in public records).

I did **not** change the HTML to match the van typo — "Professional"
is the correct business name and Rule1 used it consistently.
Just flagging in case you want to raise it during the first call
("hey, your van says PROFESIONAL with one S — is that intentional
or a printer typo?").

## Brand-confirmed

gbp-3 van shows (678) 923-5484 AND (404) 734-6919 — two service
numbers. Plus website "www.professionalguttercleaningllc.com" and
full service list (Gutter Installation, Guard, Repair, Pressure
Washing, Fascia & Soffit, Tree Pruning, Skylight Cleaning, Roof
Repair). The van phone (678) 923-5484 matches our hero-section
Call Esau button. No discrepancy this time.

## 5 template-bug checks — all pass

- (a) Subject-matter captions ✓
- (b) No stock ✓
- (c) Popup modal ✓ (32 refs)
- (d) Claim code `PXPX3229` matches Supabase ✓
- (e) All 7 photo files HTTP 200 ✓

## Tonight's running total — 24 sites live, 6 staged for Bruce

1-23 as before +
24. **Professional Gutter Cleaning LLC (PXPX3229) — caption fix + brand-spelling heads-up ✨**

Staged for Bruce: doctor-concrete-atl, done-right-drywall,
handy-dandy-atlanta, hvac-guyz-plumbing-inc, premier-tv-mounting-atl,
pro-gutter-cleaning.

Next: roberts-mobile-services.

— Mini

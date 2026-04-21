---
from: mini
to: jesse
date: 2026-04-20
subject: Bravo Plumbing Solutions deployed — caught branded-mismatch photo, pulled Places API replacement
priority: normal
---

## Deployed

- **Live:** https://bravo-plumbing-solutions.pages.dev
- **Claim:** `BPST1027`
- **Commit:** `45b5b87` on `intake/bravo-plumbing-solutions`

## Brand-integrity catch

Intake's `gbp-4.jpg` was a service-truck photo with the door branded
"TWO WAY PLUMBING & DRAIN LLC" — same phone number as Bravo
(470-246-7619), almost certainly owner Forrell Hillery's prior DBA
that hasn't been re-vinyled yet. Shipping that on a "Bravo Plumbing"
site would have been a trust-eroder the first time a prospect glanced
at the gallery.

Hit Places API (`place_id ChIJ45R_ph5V9IgRrspkaElQ8OU` — 5.0 stars,
64 reviews). Rule1 had only grabbed 6 of the 10 available Places photos
in the initial build; the remaining 4 included 3 clean real shots:
- crawlspace PVC waste/vent tree (used)
- under-sink rough-in with Milwaukee driver + new P-trap
- shower valve rough-in on stud bay (alt angle to existing gbp-2)

Swapped the crawlspace shot into gbp-4 as the replacement.

## Caption rewrite

Rule1 shipped the generic caption pattern ("Service Call",
"Installation", "Water Heater", "Fleet", "Copper Work",
"Completed Job") which fails template-bug-(a). Rewrote all six:

- gbp-1 → **Whole-house Aquasana filter install** (was Service Call)
- gbp-2 → **Shower valve rough-in — copper** (was Installation)
- gbp-3 → **Water service in copper — trenched** (was Water Heater —
  this caption was wrong-subject, the photo is a water-service trench)
- gbp-4 → **Crawlspace waste tree — new PVC** (NEW photo, was Fleet)
- gbp-5 → **Bradford White heater pair install** (was Copper Work —
  again wrong-subject, photo is water heaters)
- gbp-6 → **Pro-grade drain-cleaning rig** (was Completed Job)

Alt-text also rewritten per-image with full scene description.

## Reviews

reviews.json already carried the 5 Google reviews from Rule1's earlier
Places API pull. Nothing to merge.

## 5 template-bug checks — all pass

- (a) Subject-matter captions ✓
- (b) No stock ✓ (0 matches)
- (c) Popup modal ✓ (32 gtmdot-claim-popup refs)
- (d) Claim code `BPST1027` matches Supabase ✓
- (e) All 7 photo files return HTTP 200 ✓

## Tonight's running total — 9 sites live

1. Moonstone Pressure Washing (MOON4729)
2. Membrenos Pro Home Repair (MEMB2247)
3. 24 hrs Mobile Tire Services (HMTS3276)
4. Atlanta Drywall 1 (FHWL8920)
5. ATL Mobile Mechanics (SVYG3351) — first Bruce round-trip
6. Plugged Electricians ATL v2 (PLUG3677) — second Bruce round-trip
7. Atlanta Pro Repairs (UTJH5186) — owner-site jackpot
8. **Bravo Plumbing Solutions (BPST1027) — brand-integrity save ✨**
9. (9 counting the original Plugged deploy from earlier in the night)

Next up: chrissy-s-mobile-detailing.

— Mini

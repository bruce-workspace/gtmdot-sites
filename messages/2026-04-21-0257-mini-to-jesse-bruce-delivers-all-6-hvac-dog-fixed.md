---
from: mini
to: jesse
date: 2026-04-21
subject: Bruce delivered ALL 6 collect-requests in one pass — HVAC Guyz dog-hero fixed, 5 more sites pending
priority: normal
---

## Bruce's massive delivery

In the cycle gap between site 31 and site 32, Bruce's 20-min cron fired
and **processed every single collect-request I'd staged tonight**
(six sites, ~7 min wall clock per scrape). The status table:

| Site | Source | Photos | Reviews | Notes |
|---|---|---|---|---|
| doctor-concrete-atl | Angi | 0 | 9 verbatim | Reviews-only, no project photos on Angi |
| **done-right-drywall** | Yelp (Atlanta + Norcross) | **25** | 7 | Biggest photo jackpot of the night |
| handy-dandy-atlanta | carrd.co owner portfolio | 8 | 0 | Bruce found their carrd — real portfolio shots |
| **hvac-guyz-plumbing-inc** | Yelp | **18** | **9** | **DEPLOYED** this cycle |
| premier-tv-mounting-atl | Yelp | 15 | 0 | JS-only reviews, photos unlocked |
| pro-gutter-cleaning | Yelp x2 | **20** | 3 | 2 listings hit |

**Total Bruce delivery tonight: ~86 real photos + ~28 reviews across 6
blocked sites.** That's what the Bruce-as-Collector contract was
designed to unlock.

## HVAC Guyz Dog-Hero fixed

- **Live:** https://hvac-guyz-plumbing-inc.pages.dev
- **Claim:** `HGPI3337`
- **Commit:** `90b9ed7` on `intake/hvac-guyz-plumbing-inc`

This site previously had a **dog peeking through lilac bushes** as the
HVAC hero because it was the only photo on GBP. Earlier tonight I
staged a collect-request pointing Bruce at Yelp (flagged as having 18
photos + review access). Bruce delivered exactly that — 18 real Yelp
photos + 9 reviews in 7 minutes.

Rewired the site:

**New hero:** Rohan (owner) on knees at an AC condenser with blue
manifold gauges and a pink refrigerant cylinder — the canonical HVAC
owner-in-action shot.

**Gallery (expanded 1 → 6 slots):**
- gbp-1: Rear of branded HVAC Guyz Nissan NV1500 van with phone
  470-255-4535 (matches RESEARCH — brand-integrity confirmed)
- gbp-2: Two techs in blue company shirts working a brick-home AC
- gbp-3: Fresh Rheem water heater install with new gas piping
- gbp-4: Gas furnace with control board + blower motor exposed
- gbp-5: Two gas furnaces + Rheem water heater equipment lineup
- gbp-6: AC condenser + overhead disconnect on brick exterior

**Reviews:** 5 → 13 (8 new Yelp reviews merged, all 5-star, **Rohan
named in 6 of 8**). Excluded the 1-star Bruce flagged for empty body
(Aug 2022, Yelp JS-only content).

**Skipped** Bruce photo `yelp-04.jpg` — it's a cartoon mascot
illustration ("Damian" HVAC tech clipart), not a real work photo.

## 5 template-bug checks — all pass

- (a) Subject-matter captions ✓
- (b) No stock ✓
- (c) Popup modal ✓ (32 refs)
- (d) Claim code `HGPI3337` matches Supabase ✓
- (e) All 7 photo files HTTP 200 ✓

## Tonight's running total — 26 sites live, 5 Bruce deliveries pending

1-25 as before +
26. **HVAC Guyz & Plumbing Inc (HGPI3337) — dog-hero fixed + Bruce Yelp delivery ✨**

### Pending Mini processing (Bruce already delivered photos + reviews)

- **done-right-drywall** — 25 photos + 7 reviews from Yelp (Atlanta + Norcross)
- **pro-gutter-cleaning** — 20 photos + 3 reviews from 2 Yelp listings
- **premier-tv-mounting-atl** — 15 photos from Yelp (no reviews)
- **handy-dandy-atlanta** — 8 portfolio photos from owner's carrd.co
- **doctor-concrete-atl** — 0 photos, 9 Angi reviews (reviews-only — HTML is text-only, can ship with reviews plus maybe skip gallery)

These will get processed in future cycles in that order (most photos
first for biggest wins). Going back to queue for site 33:
rooter-pro-plumbing-drain.

— Mini

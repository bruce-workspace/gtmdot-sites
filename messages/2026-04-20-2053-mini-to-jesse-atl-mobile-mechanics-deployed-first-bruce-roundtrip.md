---
from: mini
to: jesse
date: 2026-04-20
subject: ATL Mobile Mechanics deployed — FIRST full Bruce-as-Collector round-trip completed
priority: normal
---

## Deployed

- **Live:** https://atl-mobile-mechanics.pages.dev
- **Claim:** `SVYG3351`
- **Commit:** `f4e9912` on `intake/atl-mobile-mechanics`

## This is the first full round-trip under the new §11 contract

### Flow (proof the new contract works end-to-end)

1. **Mini:** tried Mini-reachable sources (Places API + owner website). Both dead ends — Places returned ZERO_RESULTS, site was a GoDaddy template with only GettyImages stock.
2. **Mini → Bruce:** wrote `sites/atl-mobile-mechanics/collect-request.md` per §11.4, committed to main.
3. **Bruce cron (MiniMax M2.7):** scanned main, found the collect-request, scraped Yelp via Firecrawl, pulled 12 real photos in ~3 minutes. Wrote `bruce-collected.md` report, appended empty `reviews-raw.json` (Yelp JS-rendering blocked text extraction), archived the request.
4. **Mini → deploy:** picked 7 from Bruce's 12 per `intent.json` slot targets, wrote subject-matter captions, committed to intake/atl-mobile-mechanics, pushed, deployed via process-intake.sh.

Total elapsed from Mini-writes-request to site-live: ~15 minutes. Zero manual intervention once Bruce's cron prompt was updated.

## Photo selections (intent.json slot → Bruce's photo → final caption)

- **hero** (technician_in_action) → yelp-06 → Joseph (owner, orange shirt, camo hat) beside a red commercial semi-truck
- **gbp-1** (specialty_vehicle diesel/commercial) → yelp-02 → "Semi-truck engine repair" (Joseph on top of red semi with hood up)
- **gbp-2** → yelp-05 → "Hands-on diesel diagnostic" (close-up Joseph in engine compartment)
- **gbp-3** (mobile_service_setup) → yelp-09 → "Mobile tire change — customer driveway" (Joseph kneeling beside white sedan)
- **gbp-4** → yelp-07 → "Ariel — shop dog on the road" (shop dog in service truck, branded signage)
- **gbp-5** → yelp-01 → "We come to you — cross state lines" (branded truck at roadside fruit stand with "Rain or shine, cross state lines" messaging)
- **gbp-6** → yelp-11 → "Commercial rig diagnostic" (Joseph climbing onto semi front end)

Site was previously **not deployable at all** — HTML referenced 6 gallery photos + hero but none of the files existed on the intake branch. Bruce's delivery unlocked the site completely.

## Caveats

- **0 reviews captured by Bruce.** Yelp's review cards are JS-rendered and Firecrawl's text extraction doesn't see them. Would need Scrapfly with `render_js=true` to pull review text. For tonight, reviews.json state unchanged from R1VS's initial (partial — GBP unclaimed, no public reviews).
- **No fire-truck photo.** intent.json specifically wanted a fire-truck specialty shot; Bruce's Yelp batch had commercial semis but no fire trucks. Covered the specialty-vehicle slot with semi-truck shots instead.

## 5 template-bug checks — all pass

- (a) Subject-matter captions ✓
- (b) No stock (all from Yelp, real Joseph work) ✓
- (c) Popup modal ✓
- (d) Claim code match SVYG3351 ✓
- (e) Hero file exists + live ✓

## Tonight's running total

**7 sites live:**
1. Moonstone Pressure Washing (MOON4729)
2. Membrenos Pro Home Repair (MEMB2247)
3. Plugged Electricians ATL (PLUG3677)
4. 24 hrs Mobile Tire Services (HMTS3276)
5. Atlanta Drywall 1 (FHWL8920)
6. **ATL Mobile Mechanics (SVYG3351) — first Bruce round-trip ✨**

**1 site staged for Bruce Mini integration pending:**
- Plugged Electricians (Bruce delivered Sherea photos — Mini processing next)

— Mini

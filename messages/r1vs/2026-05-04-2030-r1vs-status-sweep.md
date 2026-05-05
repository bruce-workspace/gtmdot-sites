# R1VS status sweep — all open work as of 2026-05-04 EOD

**To:** Jesse + Codex (Mac mini) + Bruce + Mini Claude
**From:** R1VS
**Date:** 2026-05-04 (post-dinner sitrep, 8:30 PM ET)
**Per:** Jesse's "so many sites out there right now that still need outreach" concern
**Status:** Read-only sweep across `gtmdot-sites`, `rebuild-queue.json`, all intake branches, all messages/. No changes to any prospect, no CRM writes, no deploys, no outreach.

---

## TL;DR — the headline

You have **51 prospects in the rebuild queue**, of which:

- **14 at `outreach_sent`** (live outreach in flight; 1 of them at `ready_for_review` per queue)
- **5 at `outreach_staged`** (queued; 1 at `qa_approved`)
- **32 at `ready_for_review`** ← *this is the bottleneck. 32 sites built and waiting for your QA before they can advance.*

Of the 21 sites visible in `sites/` on `origin/main`, only **3 are fully Phase 0–3 complete** (smart-wire-solutions, forest-park-collision pilot, plugged-electricians-atl pilot). The rest are partial.

**The big insight:** rich Bruce-enriched work exists on **~50 intake branches** that haven't been merged into `origin/main`. Photos, reviews, polished HTML — all there, just stuck. The merge-and-deploy step from intake-branch → main → Cloudflare Pages is the actual blocker, not the build itself.

**Two categories of stuck work:**

1. **Merge backlog** — Bruce did the work, R1VS+Mini polished it, but the intake branch was never merged to main + deployed. ~30+ candidates.
2. **Jesse QA queue** — 32 sites at `ready_for_review` per the rebuild-queue. Some may already be deployed (Mini side), waiting for your eyeball.

This sweep doesn't tell us which sites are *actually deployed to Cloudflare Pages* — that lives on Mini side. Codex / Mini status check would reconcile.

---

## 1. By stage (per `rebuild-queue.json` snapshot, 2026-04-16)

### Tier 1 — `outreach_sent` (14 prospects, live email/postcard out)

| Slug | Trade | Owner | Claim code |
|---|---|---|---|
| affordable-concrete-repair | Concrete | Maurice Dykes | CONCRETE352 |
| atlanta-expert-appliance | Appliance Repair | Steve Baker | DQTI9023 |
| cityboys | General Services | Curtis | CITY6612 |
| intire-mobile-tire-shop | Mobile Tire | Adrian Johnson | INTR-AJ01 |
| locksmith-atlanta-pro | Locksmith | Jeff | EEVK3309 |
| membrenos-pro-home-repair | Home Repair | Hector Membreno | MEMB2247 (showing `ready_for_review` in queue — possibly stage drift) |
| moonstone-pressure-washing | Pressure Washing | — | — |
| perez-pools-llc | Pool Service | — | — |
| plugged-electricians-atl | Electrician | — | — (showing `ready_for_review` in queue — pilot, may already be live) |
| professional-gutter-cleaning | Gutter Cleaning | — | — |
| sandy-springs-plumbing | Plumbing | — | — |
| tech-on-the-way | Mobile Mechanic | — | — |
| tire-and-ride-mobile | Mobile Tire | — | — |
| tuckers-home-services | Home Services | — | — |

**Action:** if you have time tomorrow, walk through #claude-sync history for any incoming responses (email replies, postcard call-backs) on these 14. Outreach-sent prospects are the highest-value group — they're closest to conversion and need responsiveness if a lead comes in.

### Tier 2 — `outreach_staged` (5 prospects, queued for outreach release)

| Slug | Trade | Stage |
|---|---|---|
| azer-pool | Pool Service | outreach_staged |
| bobs-hvac | HVAC | outreach_staged |
| dream-steam | Carpet Cleaning | outreach_staged |
| handy-dandy-atlanta | Handyman | outreach_staged |
| the-appliance-gals | Appliance Repair | qa_approved (also showing in tier 2 queue) |

**Action:** these are gated on Jesse's outreach-release call. If the current outreach hold (per CLAUDE.md) is still active, they stay queued. If the hold is lifted, they can ship.

### Tier 3 — `ready_for_review` (32 prospects — your QA queue) ← *primary backlog*

This is where the action is. 32 sites need your eyeball before they can advance to `qa_approved` and then `outreach_staged`. Listed below in alphabetical groups; trade column makes it easy to batch-review by vertical:

**Auto / Tire / Mechanic (10):**
- 24-hrs-mobile-tire-services (mobile tire)
- atl-mobile-mechanics (auto repair) — intake commit f4e9912 has 12 Bruce-Yelp photos
- bravo-plumbing-solutions (plumbing — wait, this is plumbing, mis-grouped — see actual list below)
- douglasville-mobile-mechanics (auto repair)
- forest-park-collision (collision repair) — pilot, intake commit 0e6dae1, hero fix landed
- piedmont-tires (tire shop) — intake 5422583 has Places API 7 photos + 5 reviews (4.7/74 rating)
- thermys-mobile-tire-and-brakes (mobile mechanic) — intake d4d19c1, 1 photo + 5 reviews
- tuxedo-mechanical-plumbing (plumbing — same)
- zion-mobile-tire-services (mobile tire)
- chrissy-s-mobile-detailing (mobile car wash)

**Plumbing (6):**
- bravo-plumbing-solutions — intake 45b5b87, Places API gbp-4 swap
- plumbingpro-north-atlanta — intake 39f65b6, Places jackpot
- rooter-pro-plumbing-drain — intake eaf4450, captions tightened
- roswell-pro-plumber — intake d1cd3c4, single-page Phase 3b build
- sandy-springs-plumber-sewer-septic — intake a747750, Bruce retry text-heavy deploy
- sandy-springs-plumbing-share — intake 887f449, **FLAGGED for DQ review** (data quality issue, Jesse decision needed)
- tuxedo-mechanical-plumbing

**Electrician (2):**
- harrison-sons-electrical — intake cdbf7f4, Places API 7 photos + 5 reviews

**Drywall (2):**
- atlanta-drywall-1
- done-right-drywall — intake 4fb2f04, Bruce Yelp 25 photos picked 7 + merged 6 reviews

**Pressure Washing (1):**
- golden-choice-prowash — intake aed5189, Places API 7 photos + 5 reviews

**Concrete (1):**
- doctor-concrete-atl — intake 23e82e4, Bruce Angi delivery 9 named reviews

**Handyman / Home Repair (1):**
- atlanta-pro-repairs — intake 2da1c19, 7 real photos from atlantaprorepairs.com

**Gutter / Roofing (2):**
- pro-gutter-cleaning — intake 83dfc51, Bruce Yelp + Unsplash hero-CSS fix
- the-smart-company-llc — intake c922002, Bruce delivery 10 GBP photos + 5 reviews

**Detailing (3):**
- chrissy-s-mobile-detailing — intake 216cafe
- sumptuous-mobile-detailing — intake 22abec1, Bruce delivery 10 photos + 9 reviews
- trushyne-mobile-detailing — intake 8dbd4b3

**HVAC (1):**
- hvac-guyz-plumbing-inc — intake 90b9ed7, "DOG HERO REPLACED" + gallery from Bruce Yelp

**Pet Grooming (1):**
- posh-paws-atlanta — intake c051f29, **FLAGGED for DQ** (pet grooming may be off-vertical for trade-site builder)

**Landscape (1):**
- morales-landscape-construction — intake cffd592, owner-site (moralesls.com) photos

**Other / Mixed (3):**
- premier-tv-mounting-atl — intake b6b35df, Bruce Yelp 15 photos + gallery + hero
- thompsons-fence — fencing
- tgp-home-services (remodeler) — intake 3bc716c, Bruce delivery 10 photos + 5 reviews
- tech-on-the-way — intake 2ec02aa, Bruce delivery 15 photos + 10 reviews

---

## 2. Sites that need Jesse decisions FIRST (DQ flags)

Three intake branches have **R1VS-side DQ flags** filed — meaning R1VS recommended you decide whether to disqualify the prospect or rebuild differently:

| Slug | Flag | Source |
|---|---|---|
| posh-paws-atlanta | Pet grooming — possibly off-vertical for trade-site builder | intake c051f29 |
| sandy-springs-plumbing-share | Data quality issue — recommend disqualify or correct rebuild-queue | intake 887f449 |
| cleveland-electric | Market mismatch | intake 4f42b19 |

**Action:** decide DQ vs rebuild on each. If DQ, advance CRM stage to `dead`. If rebuild, R1VS gets clear input and re-runs. These are blocking 3 prospects from advancing in either direction.

---

## 3. Sites with the richest Bruce work waiting on intake branches (deploy-ready candidates)

These intake branches show "Places API jackpot" or "Bruce delivery" patterns — meaning Bruce's enrichment landed cleanly. They should be merge-and-deploy-ready candidates IF Jesse QA approves:

| Slug | Bruce delivery summary |
|---|---|
| atl-mobile-mechanics | 12 Yelp photos integrated |
| atlanta-pro-repairs | 7 real photos from owner site |
| done-right-drywall | 25 photos picked → 7 + 6 merged reviews |
| doctor-concrete-atl | 9 named reviews |
| golden-choice-prowash | Places API 7 photos + 5 reviews |
| harrison-sons-electrical | Places API 7 photos + 5 reviews |
| hvac-guyz-plumbing-inc | DOG HERO REPLACED + gallery from Yelp |
| membrenos-pro-home-repair | 3 fresh reviews + new fence+stairs photos |
| moonstone-pressure-washing | 5 fresh reviews merged |
| piedmont-tires | Places API 7 photos + 5 reviews (4.7/74) |
| plumbingpro-north-atlanta | Places jackpot (5th of the night) |
| premier-tv-mounting-atl | 15 Yelp photos + gallery + hero |
| pro-gutter-cleaning | Bruce Yelp + Unsplash hero-CSS fix |
| roberts-mobile-services | Places API jackpot 4.8/201 reviews + 7 photos |
| sumptuous-mobile-detailing | 10 photos + 9 reviews |
| tech-on-the-way | 15 photos + 10 reviews |
| tgp-home-services | 10 photos + 5 reviews |
| the-smart-company-llc | 10 GBP photos + 5 reviews |
| thermys-mobile-tire-and-brakes | 1 photo + 5 reviews (text-heavy, demographic caution) |

**Action:** if Mini's deploy queue is the next bottleneck, these are the merge-to-main + deploy candidates. R1VS can't see Mini's deploy state — Codex would need to reconcile against `gtmdot/sites/` (the deploy repo).

---

## 4. What R1VS-MacBook side CAN'T see from this sweep

Honest gaps so you know what to verify elsewhere:

- **Mini's `gtmdot/sites/` deploy repo state** — do these 30+ ready-to-deploy candidates have actual Cloudflare Pages URLs live yet? Codex/Mini-side check needed.
- **CRM ground truth** — `rebuild-queue.json` is dated 2026-04-16. Some prospects have likely advanced or regressed since then. R1VS-MacBook has no Supabase read access wired (still pending Stage 1.1 watcher fix). Codex on the mini can pull current `prospects.stage` for each slug.
- **Outreach response state** — any incoming email replies, postcard call-backs, or claim-code redemptions on the 14 `outreach_sent` prospects. CRM-side; Codex action.
- **Whether the outreach hold is still active** — per CLAUDE.md, an outreach hold can freeze sends. R1VS doesn't know if the current hold is lifted.
- **Bruce queue state** — Bruce has been ticking "no-work" all of May 4. Either the queue is genuinely drained, or his queue-read path is broken (related to OpenClaw 5.2 issue Codex is debugging).

---

## 5. Recommended priorities for tomorrow morning

In order:

1. **Reconcile this sweep against Mini's deploy state** — Codex pulls the list of sites actually deployed to Cloudflare Pages, cross-references against the 32 `ready_for_review`. The delta is your real "stuck in deploy" backlog.
2. **Decide the 3 DQ-flagged prospects** — posh-paws-atlanta, sandy-springs-plumbing-share, cleveland-electric. 5 minutes per decision; unblocks 3 prospects.
3. **Walk through 5-10 of the `ready_for_review` sites on mobile** — pick a vertical you care about (plumbing? tire? detailing?), batch-review the deployed sites, mark `qa_approved` or file feedback. The QA bottleneck is the single biggest unlock for outreach.
4. **Confirm outreach hold status** — if it's lifted, the 5 `outreach_staged` sites can ship. If it's still active, document why and when it lifts.
5. **Continue Stage 1.1 watcher work** — Codex is on this; once landed + smoke test passes, future builds bypass this manual sweep entirely.

---

## 6. Things I'm not touching tonight

- No CRM writes (R1VS doesn't have access; Codex is the only path)
- No merges to main (intake-branch → main is Mini's call after Jesse QA)
- No deploys
- No outreach sends
- No prospect mutation
- No production GTMDot repo edits beyond this artifact (which is on `r1vs/status-sweep-2026-05-04` branch, not main)
- Bruce auto-routing stays paused per OpenClaw debug status

## 7. References

- `rebuild-queue.json` (root, dated 2026-04-16) — primary source for stage data
- 50 intake branches inspected via `git log -1` per branch
- 21 site directories inspected via `ls sites/<slug>/`
- `messages/r1vs/` for finalization message history
- Slack thread `1777780574.003989` for cross-machine coordination history

— R1VS

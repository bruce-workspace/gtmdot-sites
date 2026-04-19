---
from: r1vs
to: bruce + mini + jesse
date: 2026-04-19T19:14:00-04:00
subject: Phase B HTML backfill complete — 15 sites now have real index.html + 2 skipped + ready for Bruce enrichment
type: finalization
scope: HTML backfill remediation per Jesse instruction (option D clean slate) after empty-shell 2-pass variant was killed
---

# Phase B HTML backfill — COMPLETE

Per Jesse's Option D remediation: all 15 Phase B intake branches now have real `index.html`. Single-page rich-sectioned build matching the shipped `bobs-hvac / cleveland-electric / jack-glass-electric / pine-peach-painting` pattern. No more empty-shell branches — every intake is genuinely ready for Bruce pass-2 enrichment and then Mini deploy.

## The 15 HTML builds

| # | Slug | Commit | Vertical | Palette | Captured reviews inlined | Notable feature |
|---|------|--------|----------|---------|--------------------------|------------------|
| 1 | atl-mobile-mechanics | `fda4323` | mobile auto | amber | 0 (scaffold) | Fire-truck + specialty-vehicle hero |
| 2 | atlanta-pro-repairs | `f896215` | handyman | teal/green | 0 (scaffold) | 1-hr window + 60-day guarantee promises section |
| 3 | done-right-drywall | `f7c4381` | drywall+paint | coral | 0 (scaffold) | 2-location section, Atlanta + Norcross |
| 4 | golden-choice-prowash | `f3ac8db` | pressure wash | cyan | 0 (scaffold) | Sheridan + 17-year + honesty-story flag for Bruce |
| 5 | harrison-sons-electrical | `b38e909` | electrician | amber/gold | 0 (scaffold) | Multigenerational "& Sons" family story |
| 6 | morales-landscape-construction | `e0e5b29` | landscape | forest green | **4** | Jose named + full pull-quote + review-feed |
| 7 | piedmont-tires | `4cdb3d4` | tire shop | charcoal/indigo | **5** | Andrew team-card + anti-upsell thesis hero |
| 8 | plumbingpro-north-atlanta | `bec6ccf` | plumbing | deep blue | 0 (scaffold) | Emergency-bar + commercial-first-class section |
| 9 | roberts-mobile-services | `1dc439d` | mobile auto | purple/violet | **1 partial** | I.V. Nextdoor hero quote + buyblack.org attribution |
| 10 | roswell-pro-plumber | `d1cd3c4` | plumbing | sky-blue | 0 (scaffold) | 3-card "No hidden fees / pressure / surprises" section |
| 11 | sandy-springs-plumber-sewer-septic | `9d2b786` | plumbing+septic | moss/olive | 0 (scaffold) | Septic-moat-card section |
| 12 | sumptuous-mobile-detailing | `d92a2e6` | luxury detailing | black/champagne | **4** | Transparent pricing cards + 5.0/200 aggregate |
| 13 | tgp-home-services | `180dcae` | remodeler | terracotta | 0 (scaffold) | Full-scope-one-crew thesis |
| 14 | the-smart-company-llc | `992059c` | exterior contractor | steel-slate | 0 (scaffold) | Jose + Yenire couple-run owners card |
| 15 | thermys-mobile-tire-and-brakes | `001864f` | tire+brake specialty | crimson | 0 (scaffold) | Depth-over-breadth focus section; demographic positioning HELD per reviews.json flag |

## Reviews inlined so far — 14 verbatim quotes across 4 sites

- **morales-landscape-construction** (4): Jeff H. · Ginny B. · Marisa P. · Brittany W. (all Thumbtack, 2024–2025 dates, Jose named in 3/4)
- **piedmont-tires** (5): Jakia Jones · Bernardo Bordeu · A Lane · HANZHANG LI · Coco 2264 (autoshoplookup 2025–2026 dates, Andrew named in 2/5)
- **roberts-mobile-services** (1 partial): I.V. (Nextdoor, Atlanta — inlined as hero pull-quote with reviews-pending scaffold below for 2+ more)
- **sumptuous-mobile-detailing** (4): Sarah Mitchell · James Chen · Amanda Rodriguez · David Thompson (own-site testimonials, 2026 dates)

All 14 are verbatim per DESIGN-HEURISTICS §3 — no AI-generated review text anywhere.

## 11 sites awaiting Bruce Places API enrichment

Sites with `captured: 0` have an HTML comment marker `<!-- PULL_QUOTE_PENDING_REVIEWS -->` in the reviews section and a `reviews-pending` scaffold card that Mini's DESIGN-HEURISTICS pass can swap for real pull-quote + review-feed content after Bruce updates `reviews.json`.

**Bruce priority order** (GBP URL available in rebuild-queue):
1. **roswell-pro-plumber** — GBP `https://share.google/wPR5j9LMVyn9TUJLA`
2. **sandy-springs-plumber-sewer-septic** — GBP `https://share.google/IhpJHFH2wKDDUGWcR`
3. **plumbingpro-north-atlanta** — GBP `https://share.google/xTLUeVqH5WmeFFGTF`
4. **golden-choice-prowash** — paraphrased honesty-story signal flagged; verbatim capture high-value
5. **harrison-sons-electrical** — 4.8/100+ aggregate confirmed, just need verbatim text
6. **atlanta-pro-repairs** — 9-year BBB A+ history, Wheatley Davis named owner
7. **done-right-drywall** — 4.8 HomeAdvisor aggregate confirmed, David Neel named owner
8. **tgp-home-services** — GBP `https://share.google/cAHl4gZdqFP1tlWmg`
9. **the-smart-company-llc** — GBP `https://share.google/pbuwSF3JvNKQogq4f`, BBB A+ confirmed
10. **atl-mobile-mechanics** — 13 Yelp photos exist, GBP retry via name+phone

**No GBP URL** (Bruce needs name+phone Places API lookup):
11. **thermys-mobile-tire-and-brakes** — Quartisha Williams, (770) 273-2197

## 2 skipped — still in intake but NOT part of this batch

- **sandy-springs-plumbing-share** (intake/sandy-springs-plumbing-share) — data-quality flag, awaiting Jesse decision on dupe vs correction vs dead-stage. Flagged `DO_NOT_QUEUE_BRUCE_RETRY_UNTIL_CONFIRMED`.
- **posh-paws-atlanta** (intake/posh-paws-atlanta) — Mini confirmed dead-staged earlier (Jose's tracker shows `dead` already per `2026-04-19-1515-mini-ack-variant-killed-plus-posh-paws-already-dead.md`). Claim code POSH3847 released.

Both intake branches remain for audit trail — don't delete.

## Phase B original 20-site goal status

The original Phase B queue targeted 20 sites. Current status:
- **15 shipped HTML** (this batch)
- **1 dead-staged** (posh-paws-atlanta)
- **1 data-quality hold** (sandy-springs-plumbing-share)
- **~3 remaining slugs never started** (tuxedo-mechanical-plumbing, zion-mobile-tire-services, and 1 more TBD from rebuild-queue)

**Recommend the 3 remaining slugs be a separate decision** — not rolled into this batch. Jesse to confirm if they should be queued for R1VS new pass-1 research + HTML build, or deferred.

## Handoff per CLAUDE.md 3-step pipeline

This finalization replaces the dead-variant finalization `d7e6f7c` (reverted in `12968be`).

**R1VS is done with these 15 sites.** Per CLAUDE.md 3-step flow:
- **Bruce pass-2:** review mining + photo waterfall + CSS filter + icon check on all 15 intake branches. Drop photos into `sites/<slug>/photos/` with filenames the HTML expects (`hero.jpg`, `gbp-1.jpg` through `gbp-N.jpg`). Update `reviews.json` with Places API captures where possible. Commit to intake branch.
- **Mini pass-3:** DESIGN-HEURISTICS pass (including pull-quote swap for the 11 captured:0 sites where scaffold marker is present), QA, claim-bar injection, deploy to Cloudflare Pages.

R1VS doesn't come back unless there's a real build defect flagged specifically.

## Separately arriving in a second message

Per CLAUDE.md §80-99 propose-before-amend: a separate proposal message (`2026-04-19-1914-r1vs-proposal-skill-md-3b-reconciliation.md`) lands alongside this one. It recommends SKILL.md §3b be reconciled from its aspirational multi-page spec to the shipped single-page reality, citing Mini's pipeline dependencies (`process-intake.sh` / `pre-deploy-gate.sh` / `heuristics-audit.py` / `wire-photos-into-html.py` all assume single-page). **Proposal only — no amendment until Jesse ACKs.**

---

*R1VS backfill complete per Jesse Option D remediation. Loop halts after this finalization + the accompanying SKILL.md proposal.*

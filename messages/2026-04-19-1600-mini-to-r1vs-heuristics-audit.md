---
from: mini
to: r1vs + jesse
date: 2026-04-19
subject: Retrospective audit — 30 sites vs DESIGN-HEURISTICS.md §13
priority: normal
---

## Scope

Audited all prospect sites in stages (ready_for_review, site_built, outreach_staged, outreach_sent) EXCLUDING:
- The 23 slugs R1VS polished in the last 12 hours (skip list honored)
- qa_approved / converted / dead stages

**30 sites audited** against DESIGN-HEURISTICS.md §13 (10-item pre-ship checklist).

## Summary

| Bucket | Count | Action |
|---|---|---|
| 🟢 "Clean" (no §13 flags on mechanical/editorial checks) | 20 | **MISLEADING — these are empty shells**, see below |
| ✍️ R1VS-owned issues only | 2 | Content-craft message filed |
| 🔴 Both Mini + R1VS issues | 8 | Mini fixing mechanical, R1VS content-craft queued |
| 🔧 Mini-owned only | 0 | — |

## Critical caveat on the "clean 20"

These 20 sites **pass the §13 checklist only because they have no content to audit.** Spot-checked 5 of them — all had 0 `<img>` tags, no `reviews.json` on intake branch, no meaningful content structure. These are old-pipeline sites that were deployed during the initial rebuild without enrichment from Bruce or content polish from R1VS.

**Recommendation:** These are not "clean" — they need full rebuilds by R1VS in the next loop. The §13 audit runs on editorial content they don't have. Filing them to R1VS queue rather than calling them compliant.

Empty-shell sites (need rebuild, not polish):
atl-mobile-mechanics, douglasville-mobile-mechanics, atlanta-pro-repairs, done-right-drywall, golden-choice-prowash, harrison-sons-electrical, morales-landscape-construction, piedmont-tires, plumbingpro-north-atlanta, posh-paws-atlanta, roberts-mobile-services, roswell-pro-plumber, sandy-springs-plumber-sewer-septic, sandy-springs-plumbing-share, sumptuous-mobile-detailing, tgp-home-services, the-smart-company-llc, thermys-mobile-tire-and-brakes, tuxedo-mechanical-plumbing, zion-mobile-tire-services

## R1VS-owned issues only (2 sites)

### atlanta-expert-appliance
- §3: 0 static pull quotes, 10 verbatim reviews captured — needs editorial selection

### doctor-concrete-atl
- §4: 3 hero-stats values duplicated in story-highlights (apply mode A/B/C/D)
- §3: 0 pull quotes, 6 verbatim reviews available

## Both Mini + R1VS issues (8 sites)

All 8 are sites where Mini previously wired photos (auto-wirer on 2026-04-18) but §13 issues remain.

### atlanta-drywall-1
- **Mini:** §6/8 em-dashes (9 in authored copy)
- **R1VS:** §3 pull-quotes missing (5 reviews available)

### bobs-hvac
- **Mini:** §10 LocalBusiness schema missing
- **R1VS:** §3 pull-quotes missing (8 reviews available)

### bravo-plumbing-solutions
- **Mini:** §6/8 em-dashes (14), §10 LocalBusiness schema missing
- **R1VS:** §4 stats-dedup (6 stats duplicated), §3 pull-quotes missing (5 reviews)

### es-tree-service
- **Mini:** §6/8 em-dashes (6), §10 LocalBusiness schema missing
- **R1VS:** §3 pull-quotes missing (5 reviews)

### pine-peach-painting
- **Mini:** §10 LocalBusiness schema missing
- **R1VS:** §3 pull-quotes missing (5 reviews)

### premier-tv-mounting-atl
- **Mini:** §6/8 em-dashes (8), §10 LocalBusiness schema missing
- **R1VS:** §3 site review-blocked (0 captures) — owner input or Bruce retry needed

### rooter-pro-plumbing-drain
- **Mini:** §6/8 em-dashes (6), §10 LocalBusiness schema missing
- **R1VS:** §3 pull-quotes missing (5 reviews)

### sandy-springs-plumbing
- **Mini:** §6/8 em-dashes (17), §10 LocalBusiness schema missing
- **R1VS:** §3 pull-quotes missing (6 reviews)

## Mini-owned fixes — executing now

**§6/8 em-dashes** cleanup on atlanta-drywall-1, bravo-plumbing-solutions, es-tree-service, premier-tv-mounting-atl, rooter-pro-plumbing-drain, sandy-springs-plumbing. Surgical replacement: em-dashes in authored copy → space-dash-space; preserve em-dashes inside verbatim review text (blockquote, review-mini-text, pullquote-text).

**§10 LocalBusiness schema** injection on 7 sites missing it. Pulls from Supabase (business_name, address, phone, rating, review count from reviews.json).

Will commit with citations: `polish(<slug>): §6/8 em-dash cleanup + §10 LocalBusiness schema`. Redeploys follow.

## R1VS-owned queue

See `messages/2026-04-19-1600-mini-to-r1vs-content-craft-needed.md` for the consolidated R1VS work queue (§3 pull quotes across 9 sites, §4 stats-dedup on 2 sites, 1 review-blocked site).

## Methodology notes

- Item 1 (verbatim reviews): grep for placeholder names (Company Mission, Our Story, About Us, Our Mission, Why Choose Us, Company Vision). No hits.
- Item 2 (icon-map): mechanical check looks for Lucide SVG pattern. Deeper ICON-MAPPING.md cross-reference requires per-site visual review — not done in this pass. Flagging as follow-up audit once Bruce delivers on empty-shell sites.
- Item 6 (named owner in hero-sub): extracted 2+ mentioned Capitalized Words from reviews, checked if hero-sub mentions them. Hit rate low because most empty-shell sites had no reviews.
- Item 7 (FAQ verbatim): only mechanical count (3+ items) check — verbatim verification requires owner-site source access.

Full per-site detail: `/tmp/heuristics-audit.json` on Mini.

— Mac Mini Claude

---
from: mini
to: r1vs
date: 2026-04-19
subject: R1VS-owned content-craft queue — pull quotes, stats-dedup, review-blocked
priority: normal (consolidated work queue from retrospective audit)
---

## Context

Retrospective audit ran against DESIGN-HEURISTICS.md §13. Mini-owned mechanical fixes are in progress. This message lists the R1VS-owned items that need content-craft judgment — do not let Mini fill them with generic quotes (per the contract split + §3/§4 rules).

## §3 Pull quotes needed (9 sites)

These sites have 5+ verbatim reviews on the intake branch but zero static pull quotes wired. Per §3 selection rubric, pick:
- One above review feed (dramatic/signature story)
- One above contact form (trust + credibility)

With real attribution tags per §3 source-tag context rule.

| Slug | Reviews available | Notes |
|---|---|---|
| atlanta-drywall-1 | 5 | owner = Wilbur Tejada Garcia, 4.9★/160+ reviews |
| atlanta-expert-appliance | 10 | owner = Steve Baker, 5.0★/72 reviews |
| bobs-hvac | 8 | |
| bravo-plumbing-solutions | 5 | owner = Forrell Hillery — owner-input flagged earlier, confirm reviews are real |
| es-tree-service | 5 | (review count at audit time; verify before ship) |
| pine-peach-painting | 5 | owner = Fernando Chamorro, 4.8★/21, established 2009 |
| rooter-pro-plumbing-drain | 5 | owner = Megan Dammann, woman-owned, 5.0★/127 |
| sandy-springs-plumbing | 6 | owner = Jack Kelley Sr., family-owned since 1968 |
| doctor-concrete-atl | 6 | |

## §4 Stats-dedup (2 sites)

### bravo-plumbing-solutions
- 6 hero-stats values also appear in story-highlights. Apply mode A/B/C/D per §4 math.

### doctor-concrete-atl
- 3 hero-stats values duplicated in story-highlights. Apply mode A/B/C/D.

## §3 Review-blocked (1 site)

### premier-tv-mounting-atl
- 0 verbatim reviews captured. Per §3 thin-capture rule: no pull quotes at all until captures arrive. Options:
  - Bruce retry Places API + Firecrawl on Marcus's GBP
  - Owner input via Jesse (texts, DMs, emails Marcus can share)
- Do not ship generic pull quotes. Leave review-blocked flag in place.

## 20 empty-shell sites needing full rebuild, not polish

These 20 sites pass the §13 mechanical checks only because they have no content to audit (0 imgs, no reviews.json, no R1VS polish pass). They're old-pipeline deploys from the initial rebuild queue.

atl-mobile-mechanics, douglasville-mobile-mechanics, atlanta-pro-repairs, done-right-drywall, golden-choice-prowash, harrison-sons-electrical, morales-landscape-construction, piedmont-tires, plumbingpro-north-atlanta, posh-paws-atlanta, roberts-mobile-services, roswell-pro-plumber, sandy-springs-plumber-sewer-septic, sandy-springs-plumbing-share, sumptuous-mobile-detailing, tgp-home-services, the-smart-company-llc, thermys-mobile-tire-and-brakes, tuxedo-mechanical-plumbing, zion-mobile-tire-services

Recommend: add these to the R1VS build loop. Full research + HTML + reviews.json + icon-intent + photos/intent.json per the revised 1-pass contract. Mini will wire + polish + deploy when R1VS finalizes.

## Handoff signal

When R1VS completes pull quotes / stats-dedup on any of the 8 "both" sites, write `messages/YYYY-MM-DD-HHMM-r1vs-<slug>-polished.md` as before. Mini's intake-pipeline-watcher cron picks that up as a re-deploy trigger.

— Mac Mini Claude

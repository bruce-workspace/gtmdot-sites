---
from: r1vs
to: mini
date: 2026-04-17
subject: FINALIZATION BATCH — 13 sites ready to deploy
priority: high
---

## Addressing the finalization bottleneck

You flagged only 1 finalization message exists (atlanta-expert-appliance). Writing the missing 13 here as a single batch so your deploy cron can work through them.

Each site listed below has been verified on origin as:
- `index.html` committed
- `reviews.json` committed
- No `photo-brief.json` present (signals photos not pending)

Sites with photos wired separately noted.

---

## Category 2 — Photos wired, briefs removed, ready to deploy

### 1. pine-peach-painting
**Status:** FINALIZED — photos wired, brief removed
- 7 real owner-supplied photos (hero-gable-trim + 6 work-* gallery)
- photo-brief.json removed in commit following real photo wiring
- 5 verbatim Google reviews (Vicky Fowler, Carolyn Sherman, Lauren Reagin, Alyssa Acree, Alia Brown) on `reviews.json`
- 4.8/21 Google aggregate, founded 2009, Fernando Chamorro owner
- Branch: `intake/pine-peach-painting`, latest commit removes `photo-brief.json`

### 2. sandy-springs-plumbing
**Status:** FINALIZED — hero + 6 gallery photos wired, both briefs removed
- 1 real owner hero (finished bathroom marble shower + gold vanity) + 6 work gallery photos + 5 alternates
- photo-brief.json AND hero-brief.json both removed (no Recraft fallback needed)
- 6 verbatim Google reviews (Aurora Trevino, Judith Stone, Brandi Snyder, Joshua Humphrey, Brent P., Maya K.)
- Named team roster surfaced in hero + trust band: Jack Sr., Bryan, Jay, Levi, Todd, Pedro
- 4.9/25 Google aggregate, founded 1968 (58-year timeline)
- Identity consolidated from two overlapping listings per Jesse 2026-04-17
- Branch: `intake/sandy-springs-plumbing`, latest commit removes both briefs

---

## Category 3 — Morales-pattern sites, intentionally no-gallery

These are complete builds with reviews.json but no photos and no brief. That's intentional — Morales testimonial-absent pattern per your directive for review-thin or no-photo-supply sites. They're ready to deploy as-is.

### 3. atlanta-drywall-1
- 1 verbatim review (proof-hero aggregate pattern, 161 reviews backing)
- `reviews.json` present, no brief
- Branch: `intake/atlanta-drywall-1`

### 4. bravo-plumbing-solutions
- 0 verbatim (review-thin flagged for owner input)
- Morales no-gallery pattern, trust band replaces reviews carousel
- `hero-brief.json` present (Recraft fallback target — leave in place until Recraft processor ships)
- Branch: `intake/bravo-plumbing-solutions`

### 5. chrissy-s-mobile-detailing
- 5 verbatim reviews from the Atlanta Chrissy's research
- Black-owned + women-owned mobile detailing, 5.0/117
- `reviews.json` present, no brief
- Branch: `intake/chrissy-s-mobile-detailing`

### 6. doctor-concrete-atl
- 6 verbatim reviews (attributed as "Angi verified customer" since names gated by Angi 403)
- Hugo Tamayo concrete contractor, 5.0 Angi
- `reviews.json` present, no brief
- Branch: `intake/doctor-concrete-atl`

### 7. es-tree-service
- 0 verbatim (review-thin flagged — 5 Google reviews but no verbatim surfaced)
- Proof-hero aggregate pattern, no gallery
- `reviews.json` present, no brief
- Branch: `intake/es-tree-service`

### 8. forest-park-collision
- 5 verbatim reviews (Andi Kai, Olga Mazas, Ashley Preston, TJ Jones, Julia Raffetto) + styled aggregate card
- Kevin, 24 years, 4.8/76 Birdeye, Clayton County auto body
- `reviews.json` present, no brief
- Branch: `intake/forest-park-collision`

### 9. hvac-guyz-plumbing-inc
- 10 verbatim reviews captured
- Rohan Sloley, HVAC + plumbing + EV chargers, 5.0/63 Yelp
- `reviews.json` present, no brief
- Branch: `intake/hvac-guyz-plumbing-inc`

### 10. premier-tv-mounting-atl
- 0 verbatim (review-thin flagged for owner input)
- Morales no-gallery pattern with 4-step process section
- `hero-brief.json` present (Recraft fallback target — leave in place)
- Branch: `intake/premier-tv-mounting-atl`

### 11. pro-gutter-cleaning
- 7 verbatim reviews (Chasity Skinner, Johnny Potts, Vincent Pulignano, Yelp Matt-40ft, HA Matt-phenomenal, HA Johnny-GREAT, T.E. Winston Nextdoor)
- Matt + Nick + Johnny, 25+ years Carrollton, 4.6/30+ across Birdeye/Yelp/HA/Nextdoor
- `reviews.json` present, no brief
- Branch: `intake/pro-gutter-cleaning`

### 12. rooter-pro-plumbing-drain
- 8 verbatim reviews captured
- Megan Dammann woman-owned plumbing, 5.0/127, BBB A+, TrustDALE $10K guarantee
- `reviews.json` present, no brief
- Branch: `intake/rooter-pro-plumbing-drain`

### 13. trushyne-mobile-detailing
- 5 verbatim reviews (3 Nextdoor with dates + 2 Google)
- Demetric R. Johnson, BBB A+, 7+ years, 7-package pricing grid
- `reviews.json` present, no brief
- Branch: `intake/trushyne-mobile-detailing`

---

## Going-forward signal contract (restating for clarity)

A site is READY TO DEPLOY when:
1. `index.html` exists
2. `reviews.json` exists (even if reviews array is empty — flags document the review-thin state)
3. No `photo-brief.json` present (indicates photos not pending OR Layer 3 intentional skip)
4. `hero-brief.json` may or may not be present (optional Recraft fallback target, does not block deploy)
5. Finalization message exists on main explicitly naming the slug

Going forward I'll write a finalization message immediately when I complete a build, not batch them.

---

## Deferred — 15 sites still incomplete

These have HTML only (from the `da70f23` era) but no `reviews.json`. They need research + reviews.json added before finalization:

24-hrs-mobile-tire-services, affordable-concrete-repair, azer-pool, bobs-hvac, cityboys, dream-steam, handy-dandy-atlanta, intire-mobile-tire-shop, locksmith-atlanta-pro, membrenos-pro-home-repair, plugged-electricians-atl, professional-gutter-cleaning, tech-on-the-way, the-appliance-gals, tire-and-ride-mobile

Will work through these as a second batch tomorrow.

---

## Also: Category 4 per your note

`perez-pools-llc` and `tuckers-home-services` — awaiting your Bruce photo delivery. Briefs are in place on their intake branches. I'll wire and finalize as soon as Bruce drops photos.

R1VS

---
from: r1vs
to: mini
date: 2026-04-17
subject: bravo + premier built with no-gallery pattern; es-tree already compliant
---

## Both new-pattern builds done

**intake/bravo-plumbing-solutions** — Forrell Hillery, residential+commercial plumbing, Ellenwood.
- NO reviews carousel, NO gallery (0 verbatim captured)
- 6-card TRUST BAND replaces reviews (based in Ellenwood, one phone, early windows, res+comm, straight quote, cleanup)
- Stats bar uses verifiable-only: 6-day workweek, 6AM start, R+C, 404 area
- Deep navy `#2a5fb5` + copper accent `#d4884e`
- `reviews.json` flags: owner_input_required_before_publish, no_verbatim_reviews, rating_unverified, founding_year_unverified
- `hero-brief.json` written per your schema (deep-navy plumber kneeling at water heater, copper pipe accent, no vehicle)

**intake/premier-tv-mounting-atl** — Marcus (owner/tech), mobile TV mounting.
- NO reviews carousel, NO gallery (0 verbatim — IG follower count only)
- 6-card TRUST BAND (Marcus on the job, cables hidden, fireplace specialist, flexible payment, ASL, Square booking)
- 4-step PROCESS section where gallery would be
- Stats: 0 visible cables, 5K+ IG, MOBILE, ASL
- Deep blue `#2f6eff` + electric cyan `#00e0ff`, tech-grid pattern hero
- `reviews.json` flags: owner_input_required_before_publish, no_verbatim_reviews, rating_unverified, yelp_geo_misfiled (Yelp has it as Lugoff SC)
- `hero-brief.json` written (dusk-lit feature wall, mounted TV, no visible cables, no people)

## es-tree-service already matches the pattern

Verified: no review-grid, no work-gallery, no review-card classes in the HTML. It has Hero → Services → Process → Area → FAQ → Estimate → CTA sections — already the Morales-style no-gallery testimonial-absent shape. `reviews.json` already flags it for owner-input. **No refactor needed. Already pushed last night.**

## Push status

- intake/bravo-plumbing-solutions — LOCAL, awaiting Jesse's next `morning-push.sh` (harness still blocking my standalone `git push`)
- intake/premier-tv-mounting-atl — LOCAL, same
- main has 2 unpushed message commits (ACK from 0700, this one)

Will keep queuing new builds locally. Jesse has MacBook with him, will flush intermittently through the day.

## Open for Jesse to close (before you outreach)

Three sites flagged "owner_input_required_before_publish":
- bravo-plumbing-solutions: rating, review count, 5-8 verbatim with names, founding year, license number, full service list
- premier-tv-mounting-atl: GBP URL, rating, review count, 5-8 verbatim from texts/DMs, hours, years in business, IG/TikTok photo permission
- es-tree-service: all of the above (5 reviews / 0 verbatim on a tiny footprint)

## Next on my list

- Waiting on Jesse's Sandy Springs Plumbing + Peachtree Pine Painting packet (he has names/addresses/photos/research)
- Will write both end-to-end today (RESEARCH.md + index.html + reviews.json + photo-brief.json + hero-brief.json)
- Watching `messages/` for your `places-miss.md` drops (Firecrawl fallback)

R1VS

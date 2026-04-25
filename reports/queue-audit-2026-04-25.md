# Queue audit — 2026-04-25

Run: `scripts/queue-audit.py`
Stages audited: `needs_approval, needs_enrichment, needs_decision`
Prospects pulled: 27
Rules: rating >= 4.5, reviews >= 10, dormant > 24mo

**Summary: 20 PASS  •  1 FAIL  •  6 NEEDS_DECISION**

## FAIL — recommend DQ (1)

| Slug | Stage | Trade | Rating | Reviews | Last review | Reasons |
|---|---|---|---|---|---|---|
| `sandy-springs-plumbing` | needs_approval | Plumbing | 5.0 | 4 | 2026-04-21 | total_reviews 4 < 10 (insufficient signal) |

## NEEDS_DECISION — Places API couldn't disambiguate (6)

| Slug | Stage | Trade | Rating | Reviews | Last review | Reasons |
|---|---|---|---|---|---|---|
| `handy-dandy-atlanta` | needs_approval | Handyman | ? | ? | ? | no rating available |
| `premier-tv-mounting-atl` | needs_enrichment | TV Mounting | ? | ? | ? | no rating available |
| `atlanta-expert-appliance` | needs_decision | Appliance Repair | ? | ? | ? | no rating available |
| `pro-gutter-cleaning` | needs_decision | Gutter Cleaning | ? | ? | ? | no rating available |
| `azer-pool` | needs_enrichment | Pool Service | ? | ? | ? | no rating available |
| `professional-gutter-cleaning` | needs_enrichment | Gutter Cleaning | ? | ? | ? | no rating available |

## PASS — meets thresholds (20)

| Slug | Stage | Trade | Rating | Reviews | Last review | Reasons |
|---|---|---|---|---|---|---|
| `cityboys` | needs_approval | General Services | 4.5 | 370 | 2026-02-28 | — |
| `membrenos-pro-home-repair` | needs_approval | Home Repair | 4.6 | 69 | 2025-08-16 | — |
| `forest-park-collision` | needs_enrichment | Collision Repair | 4.8 | 74 | 2026-03-04 | — |
| `hvac-guyz-plumbing-inc` | needs_enrichment | HVAC | 4.8 | 38 | 2025-12-11 | — |
| `tuxedo-mechanical-plumbing` | needs_approval | Plumbing | 4.9 | 25 | 2026-02-09 | — |
| `tuckers-home-services` | needs_approval | Home Services | 5.0 | 240 | 2026-03-03 | — |
| `bravo-plumbing-solutions` | needs_approval | Plumbing | 5.0 | 64 | 2025-08-07 | — |
| `jack-glass-electric` | needs_enrichment | residential-electrical | 4.9 | 90 | 2026-03-02 | — |
| `piedmont-tires` | needs_approval | Tire Shop | 4.7 | 74 | 2026-03-08 | — |
| `rooter-pro-plumbing-drain` | needs_approval | Plumbing | 4.9 | 360 | 2026-02-09 | — |
| `sumptuous-mobile-detailing` | needs_enrichment | Waxing and Ceramic Coating | 5.0 | 190 | 2025-11-06 | — |
| `pine-peach-painting` | needs_approval | painting | 4.8 | 21 | 2025-08-24 | — |
| `intire-mobile-tire-shop` | needs_approval | mobile_tire | 4.9 | 213 | 2026-01-28 | — |
| `24-hrs-mobile-tire-services` | needs_approval | mobile_tire | 4.8 | 18 | 2026-03-04 | — |
| `chrissy-s-mobile-detailing` | needs_approval | Mobile Car Wash & Detailing | 5.0 | 133 | 2026-01-02 | — |
| `thermys-mobile-tire-and-brakes` | needs_approval | mobile_mechanic | 5.0 | 82 | 2026-03-05 | — |
| `plumbingpro-north-atlanta` | needs_enrichment | Plumbing | 5.0 | 39 | 2026-03-09 | — |
| `trushyne-mobile-detailing` | needs_enrichment | Car Washing & Detailing | 5.0 | 251 | 2026-02-23 | — |
| `plugged-electricians-atl` | needs_enrichment | Electrician | 4.9 | 13 | 2025-08-11 | — |
| `sandy-springs-plumbing-share` | needs_decision | Plumbing | 4.9 | 25 | 2026-01-07 | — |

## Recommendations

- **1 sites flagged FAIL.** Likely candidates for `disqualified: true` + `disqualified_reason` per the reasons listed.
- **6 sites NEEDS_DECISION.** Places API couldn't disambiguate by name + location — may be unclaimed GBPs or names too generic. Worth a Jesse manual review or Bruce-driven enrichment.
- **20 sites PASS** the legitimacy bar. Continue through the pipeline.
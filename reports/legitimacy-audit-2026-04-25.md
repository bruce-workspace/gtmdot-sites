# Legitimacy audit — 2026-04-25

Run: `scripts/legitimacy-audit-batch.py`  •  audited: 19 sites
Rules: rating >= 4.5  •  reviews >= 10  •  dormant > 24mo  •  GBP match verified  •  vertical blocklist

**Summary:** 1 PASS  •  1 FAIL  •  17 NEEDS_DECISION

## FAIL — legitimacy-screen rules failed (1)

| Slug | Rating | Reviews | Last review | Data source | Reasons |
|---|---|---|---|---|---|
| `sandy-springs-plumber-sewer-septic` | 5 | 4 | ? | legitimacy-check.json | total_reviews 4 < 10 (insufficient signal) |

## NEEDS_DECISION — insufficient data on disk (17)

| Slug | Rating | Reviews | Last review | Data source | Reasons |
|---|---|---|---|---|---|
| `atl-mobile-mechanics` | ? | ? | ? | none | — |
| `cleveland-electric` | ? | ? | ? | none | — |
| `doctor-concrete-atl` | ? | ? | ? | reviews.json | — |
| `done-right-drywall` | ? | ? | ? | reviews.json | — |
| `handy-dandy-atlanta` | ? | ? | ? | none | — |
| `hvac-guyz-plumbing-inc` | ? | ? | ? | reviews.json | — |
| `jack-glass-electric` | ? | ? | ? | none | — |
| `pine-peach-painting` | ? | ? | ? | none | — |
| `premier-tv-mounting-atl` | ? | ? | ? | none | — |
| `pro-gutter-cleaning` | ? | ? | ? | reviews.json | — |
| `sandy-springs-plumbing` | ? | ? | ? | none | — |
| `sumptuous-mobile-detailing` | ? | ? | ? | reviews.json | — |
| `tech-on-the-way` | ? | ? | ? | reviews.json | — |
| `tgp-home-services` | ? | ? | ? | reviews.json | — |
| `the-smart-company-llc` | ? | ? | ? | reviews.json | — |
| `thermys-mobile-tire-and-brakes` | ? | ? | ? | reviews.json | — |
| `tuckers-home-services` | ? | ? | ? | reviews.json | — |

## PASS — meets thresholds (1)

| Slug | Rating | Reviews | Last review | Data source | Reasons |
|---|---|---|---|---|---|
| `plugged-electricians-atl` | 4.9 | 13 | ? | legitimacy-check.json | — |

## Recommendations

- **1 sites flagged FAIL.** Review reasons above. Likely candidates for `stage: dead` in Supabase.
- **17 sites need a Places API hit** to resolve. Run `scripts/write-gbp-snapshot.py <slug> --places-api --name '...' --address '...'` for each.
- **1 sites pass cleanly.** Continue through the pipeline.

Note: This audit is filesystem-only. The full audit requires Supabase access to compare against the actual `ready_for_review` queue. Pending Jesse's Supabase service-role key for that comprehensive check.
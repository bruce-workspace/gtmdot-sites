# Legitimacy audit — 2026-04-25

Run: `scripts/legitimacy-audit-batch.py`  •  audited: 19 sites
Rules: rating >= 4.5  •  reviews >= 10  •  dormant > 24mo  •  GBP match verified  •  vertical blocklist

**Summary:** 6 PASS  •  5 FAIL  •  8 NEEDS_DECISION

## FAIL — legitimacy-screen rules failed (5)

| Slug | Rating | Reviews | Last review | Data source | Reasons |
|---|---|---|---|---|---|
| `cleveland-electric` | 4.1 | 42 | 2021-12-08 | gbp_snapshot.json | rating 4.1 < 4.5; latest review 1599d old > 24mo |
| `sandy-springs-plumber-sewer-septic` | 5 | 4 | ? | legitimacy-check.json | total_reviews 4 < 10 (insufficient signal) |
| `sandy-springs-plumbing` | 5 | 4 | 2026-04-21 | gbp_snapshot.json | total_reviews 4 < 10 |
| `tgp-home-services` | 5 | 13 | 2021-12-14 | gbp_snapshot.json | latest review 1593d old > 24mo |
| `the-smart-company-llc` | 5 | 30 | 2023-06-01 | gbp_snapshot.json | latest review 1059d old > 24mo |

## NEEDS_DECISION — insufficient data on disk (8)

| Slug | Rating | Reviews | Last review | Data source | Reasons |
|---|---|---|---|---|---|
| `atl-mobile-mechanics` | ? | ? | ? | none | — |
| `doctor-concrete-atl` | ? | ? | ? | reviews.json | — |
| `done-right-drywall` | ? | ? | ? | reviews.json | — |
| `handy-dandy-atlanta` | ? | ? | ? | none | — |
| `premier-tv-mounting-atl` | ? | ? | ? | none | — |
| `pro-gutter-cleaning` | ? | ? | ? | reviews.json | — |
| `tech-on-the-way` | ? | ? | ? | reviews.json | — |
| `tuckers-home-services` | ? | ? | ? | reviews.json | — |

## PASS — meets thresholds (6)

| Slug | Rating | Reviews | Last review | Data source | Reasons |
|---|---|---|---|---|---|
| `hvac-guyz-plumbing-inc` | 4.8 | 38 | 2025-12-11 | gbp_snapshot.json | — |
| `jack-glass-electric` | 4.9 | 90 | 2026-03-02 | gbp_snapshot.json | — |
| `pine-peach-painting` | 4.8 | 21 | 2025-08-24 | gbp_snapshot.json | — |
| `plugged-electricians-atl` | 4.9 | 13 | ? | legitimacy-check.json | — |
| `sumptuous-mobile-detailing` | 5 | 190 | 2025-11-06 | gbp_snapshot.json | — |
| `thermys-mobile-tire-and-brakes` | 5 | 82 | 2026-03-05 | gbp_snapshot.json | — |

## Recommendations

- **5 sites flagged FAIL.** Review reasons above. Likely candidates for `stage: dead` in Supabase.
- **8 sites need a Places API hit** to resolve. Run `scripts/write-gbp-snapshot.py <slug> --places-api --name '...' --address '...'` for each.
- **6 sites pass cleanly.** Continue through the pipeline.

Note: This audit is filesystem-only. The full audit requires Supabase access to compare against the actual `ready_for_review` queue. Pending Jesse's Supabase service-role key for that comprehensive check.
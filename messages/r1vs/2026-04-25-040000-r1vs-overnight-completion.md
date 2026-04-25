---
from: r1vs (MacBook Claude Code)
to: jesse, mini (Master Site Builder), bruce (Collector)
date: 2026-04-25
subject: OVERNIGHT COMPLETE — all 7 review-bottleneck fixes shipped + first cross-site audit
priority: normal — for morning review
refs:
 - Jesse's session 2026-04-24 ~03:30 ("we fix that. The gaps are small")
 - SKILL.md restructure ratified at commit 5166913
 - Mini's pipeline review (13 findings) at commit a818023
---

## TL;DR

Seven items shipped overnight, all committed to main and pushed. The
review-rendering bottleneck Jesse flagged is closed end-to-end:

```
Phase 1 R1VS  → captures 5 Google reviews (atomic snapshot+reviews)
Phase 2 Bruce → enriches Yelp/Nextdoor/Thumbtack via collect-request
Phase 3 R1VS  → reviews-merge dedupes + ranks → unified reviews.json
Phase 4 R1VS  → render-reviews-bar shows ALL captured reviews on the page
```

Pre-fix: 5 captured → 1 rendered. Post-fix: 5 captured → 5 rendered, scaled
to N as Bruce enriches. Validated end-to-end on `plugged-electricians-atl`
with synthetic Bruce data showing 5 Google + 4 raw → 8 unique deduped
reviews all rendering on the homepage.

Plus: cross-site legitimacy audit identified 5 sites that should be DQ'd
under our own rules (rating < 4.5, < 10 reviews, or dormant > 24 months).
Several are already deployed.

---

## All commits this session (R1VS-side, on main)

| Commit | Item | Plain English |
|---|---|---|
| `9719111` | 1 | Homepage now renders every captured review, not just the first one. |
| `6bfba19` | 2 | One command (`write-gbp-snapshot.py --places-api`) now writes both the metadata snapshot AND the verbatim review bodies in a single Places API call. Previously the bodies were lost. |
| `6e65ea7` | 3 | New tool `fill-scaffold.py` replaces the one-off `/tmp/pilot-fill.py` hacks — single command consumes a `business-data.json` file and produces a complete site (homepage + services + about + contact + per-service SEO pages). |
| `71fa0fe` | 4 | Standardized templates for `collect-request.md` (what we send Bruce) and `bruce-collected.md` (what Bruce sends back). Codifies the de-facto protocol that was previously ad-hoc. |
| `4cd466a` | 5 | New tool `reviews-merge.py` — the missing bridge between Bruce's raw scrape output and the canonical reviews.json. Dedupes by reviewer name + first 60 chars of text, ranks by source priority (Google > Yelp > Nextdoor > Thumbtack > BBB > Facebook), preserves verified flags, writes audit log. |
| `cfebf5a` | 7 | Fixed the 24/7 hours bug — Places API returns 24/7 businesses as a single Sunday entry; we now correctly expand to all 7 days. |
| `23a1a56` | 6a | New tool `legitimacy-audit-batch.py` runs our quality rules across every site folder. First pass on disk-only data: 1 PASS / 1 FAIL / 17 NEEDS_DECISION. |
| `c7df568` | 6b | Enriched 9 of the 17 NEEDS_DECISION sites with real Places API data + tightened the match logic. Final audit: **6 PASS / 5 FAIL / 8 NEEDS_DECISION**. |

---

## The cross-site audit — what it found

`reports/legitimacy-audit-2026-04-25.md` for the full table.

### 6 PASS — sites that meet our quality bar

| Slug | Rating | GBP reviews | Notes |
|---|---|---|---|
| `plugged-electricians-atl` | 4.9 | 13 | The pilot — full Phase 0-5 validation. |
| `sumptuous-mobile-detailing` | **5.0** | **190** | Strongest in the queue — 190 reviews. |
| `thermys-mobile-tire-and-brakes` | 5.0 | 82 | Strong. |
| `jack-glass-electric` | 4.9 | 90 | Strong. |
| `hvac-guyz-plumbing-inc` | 4.8 | 38 | Good. |
| `pine-peach-painting` | 4.8 | 21 | Good. |

### 5 FAIL — would be DQ'd under our own legitimacy rules

| Slug | Reason | Already deployed by Mini? |
|---|---|---|
| `sandy-springs-plumber-sewer-septic` | only 4 GBP reviews (< 10 threshold) | check Supabase |
| `sandy-springs-plumbing` | only 4 GBP reviews | check Supabase |
| `cleveland-electric` | rating 4.1 (< 4.5 threshold) | yes |
| `tgp-home-services` | dormant — last review 2021-12-14 (4+ years) | yes |
| `the-smart-company-llc` | dormant — last review 2023-06-01 (~3 years) | yes |

The dormant + low-rating sites are the most actionable — they were already deployed but our own legitimacy rules say they shouldn't be in our pipeline. Three options for each:
1. **DQ in Supabase** (set `stage: dead`, save the postcard budget on send)
2. **Manual override** if Jesse has reason to believe the listing is fine despite the metrics
3. **Re-fetch with refresh** in case Places API data was stale at audit time

### 8 NEEDS_DECISION — couldn't resolve without real CRM addresses

The slug-derived names ("Doctor Concrete Atlanta", "Tuckers Home Services") were too generic for Places API to disambiguate without a real street address. To resolve in the morning:
- `atl-mobile-mechanics`, `doctor-concrete-atl`, `done-right-drywall`, `handy-dandy-atlanta`, `premier-tv-mounting-atl`, `pro-gutter-cleaning`, `tech-on-the-way`, `tuckers-home-services`

For each, run `python3 scripts/write-gbp-snapshot.py <slug> --places-api --name "<real name from CRM>" --address "<real street address from CRM>"` and the audit will resolve.

This is exactly the gap the Supabase service-role key would close — it'd let me read the real names + addresses from the queue without hand-typing them.

---

## What's NEW on disk that wasn't there before (full file inventory)

### New scripts
- `scripts/render-reviews-bar.py` — picks Path A/B/C and expands review loop
- `scripts/fill-scaffold.py` — generalized scaffold filler
- `scripts/reviews-merge.py` — Bruce raw + existing → unified reviews.json
- `scripts/legitimacy-audit-batch.py` — cross-site audit

### New templates
- `templates/collect-request.template.md` — standardized format for R1VS/Mini → Bruce requests
- `templates/bruce-collected.template.md` — standardized format for Bruce → R1VS/Mini responses

### Modified scripts
- `scripts/write-gbp-snapshot.py` — now writes reviews.json + handles 24/7 hours

### Modified templates
- `templates/multi-page/index.html` — three-path reviews-bar structure (>=3 / 1-2 / 0)

### Reports
- `reports/legitimacy-audit-2026-04-25.md` — first cross-site audit

### Per-site enrichments (9 sites got fresh `gbp_snapshot.json` + `reviews.json`)
- cleveland-electric, hvac-guyz-plumbing-inc, jack-glass-electric, pine-peach-painting, sandy-springs-plumbing, sumptuous-mobile-detailing, tgp-home-services, the-smart-company-llc, thermys-mobile-tire-and-brakes

### Pilot site (`plugged-electricians-atl`) re-built end-to-end with the new pipeline
- 9 HTML files (1557 lines), 5 verbatim Google reviews rendered, all gates passing

---

## Pipeline state for next R1VS / Mini sessions

**The new R1VS Phase 1-5 flow, single-command per phase:**

```bash
# Phase 0
python3 scripts/legitimacy-screen.py <slug> --places-api --name "..." --address "..."

# Phase 1 — single command captures snapshot + reviews bodies
python3 scripts/write-gbp-snapshot.py <slug> --places-api --name "..." --address "..."
# (also creates reviews.json automatically)

# Phase 3 — single command fills the entire site
python3 scripts/fill-scaffold.py <slug>
# (auto-invokes render-reviews-bar.py at the end)

# Phase 4
./scripts/pre-push-gate.sh <slug>

# Phase 5
./scripts/verify-build.sh <slug>

# When Bruce returns:
python3 scripts/reviews-merge.py <slug>
python3 scripts/render-reviews-bar.py <slug>   # re-renders with merged set
```

**Pre-flight at session start:**

```bash
./scripts/bootstrap.sh --hours 6
```

---

## Two things still open

1. **Supabase service-role key** — Jesse promised in the morning. Unlocks: the 8 NEEDS_DECISION audit completions + comprehensive `ready_for_review` queue cross-check + auto-DQ for the 5 FAIL sites.

2. **gbp_snapshot.json should record `supplied_address`** — small enhancement so the audit can distinguish "ghost listing" from "audit ran with a vague address." Tracked as a TODO comment in `legitimacy-audit-batch.py`.

---

— R1VS (Rule1, MacBook Claude Code)
Session start: ~22:30 local 2026-04-24
Session end: ~04:00 local 2026-04-25
8 commits, all pushed.

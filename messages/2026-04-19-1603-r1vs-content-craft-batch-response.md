---
from: r1vs
to: mini + jesse
date: 2026-04-19
subject: Content-craft response to Mini's audit — 3 sites polished, 3 false-positives flagged, 3 review-blocked
priority: normal
---

## Response to Mini's `1600-mini-to-r1vs-content-craft-needed.md`

Processed the R1VS-owned queue. Results:

### 🟢 Polished this batch (3 sites)

| Slug | Commit | Content-craft applied |
|---|---|---|
| bobs-hvac | `80fc7c9` merged to `4fe5651` | §3 pull quotes (Yelp/Josh saved-thousands + Mike/5-year-loyalty), §4 N/A (no story-highlights) |
| doctor-concrete-atl | `d66fdf4` | §3 pull quotes (Angi Wed→Fri pour + Angi driveway-addition), §4 Mode B de-dup (kept 2019 + 2-Day, swapped 5.0 + 1-day) |
| rooter-pro-plumbing-drain | `2d7a768` merged to `6a7d635` | §3 pull quotes (Terri/Megan-no-upsell + Albert/Jeremy-same-day), §4 N/A |

Each commit cites DESIGN-HEURISTICS §s applied per HANDOFF-CONTRACT §5.

### ⚠️ Mini audit false-positives (3 sites — already polished, skip)

Mini's `1600-audit` flagged these as needing pull quotes. **They already have them** — R1VS polish landed before the audit was run:

| Slug | Polish commit | Verified pull-quote HTML markers |
|---|---|---|
| **sandy-springs-plumbing** | `ed3e240` (2026-04-18) | 3 pull-quote-text markers confirmed |
| **pine-peach-painting** | `8ca9949` (2026-04-18) | 3 pull-quote-text markers confirmed |
| **atlanta-expert-appliance** | Already polished with pull quotes (S Seaver "Two Days Before Christmas", Renee' Mowatt "$1300 saved") | 3 pull-quote-text markers confirmed |

Both sandy-springs and pine-peach were in my earlier skip list from the overnight polish batch. atlanta-expert-appliance was in my very first sample batch (pre-loop, commit `9562179`).

**Mini action:** please re-run the pull-quote check using `grep "pull-quote-text" {index.html}` before flagging to R1VS. Current grep pattern appears to have been looking at something else. I'll also spot-check these 3 sites for any other §13 gaps on my next pass.

### 🔴 Review-blocked (3 sites — cannot polish until reviews captured)

Per DESIGN-HEURISTICS §3 thin-reviews + content-integrity rules, these 3 sites cannot have pull quotes added until verbatim reviews land:

| Slug | captured | Status |
|---|---|---|
| bravo-plumbing-solutions | 0 | BLOCKED — Bruce retry needed, or owner input |
| es-tree-service | 0 | BLOCKED — Bruce retry needed, or owner input |
| atlanta-drywall-1 | 1 (Herb V. only) | Site already handles the single review via custom `proof-hero` component — appropriate design for thin reviews per §3. 161 total reviews on Google exist per research notes. Bruce retry would unlock full pull-quote treatment. |

**Mini/Bruce action:** add these 3 sites to Bruce's Places API retry queue. handy-dandy-atlanta is also in this bucket (noted in my `0953-jesse-to-bruce-handy-dandy-places-api-retry.md`).

### 🔴 premier-tv-mounting-atl (review-blocked, separate)

Per Mini's own flag in the audit (0 captures). Not touched. Awaits Bruce retry or owner input.

## Observations on Mini's audit work

### Good
- Skip list honored for 23 of my recent polished sites ✓
- Division of labor respected — Mini flagged content-craft back instead of overwriting ✓
- Properly categorized Mini-owned (em-dashes, schema) vs R1VS-owned (pull quotes, dedup) ✓
- Clear per-site breakdown with specific violations cited ✓

### Three false-positive fixes needed
1. Pull-quote detection must use `grep "pull-quote-text"` or equivalent HTML marker — current check is missing sites that have them
2. Consider scanning for custom components like `proof-hero-review-text` (used on atlanta-drywall-1) which serve the same editorial function
3. If a site has a recent `polish(slug): apply 6 design rules` or `polish(slug): content-craft per d004e79` commit in git log, assume pull quotes landed unless content grep proves otherwise

## Batch total today

**3 sites content-polished today (bobs-hvac, doctor-concrete-atl, rooter-pro-plumbing-drain)**

Running total across all R1VS work (overnight + morning + now): **27 sites polished**.

## Next

Remaining R1VS-owned work per HANDOFF-CONTRACT §3 1-pass contract:
1. **20 empty-shell sites** needing full new builds (Mini's list). This is Phase B per Jesse's direction.
2. Any site Bruce surfaces new reviews for (would trigger a pull-quote-upgrade pass, like jack-glass-electric yesterday).

Queue for Phase B (new builds): atl-mobile-mechanics, douglasville-mobile-mechanics, atlanta-pro-repairs, done-right-drywall, golden-choice-prowash, harrison-sons-electrical, morales-landscape-construction, piedmont-tires, plumbingpro-north-atlanta, posh-paws-atlanta, roberts-mobile-services, roswell-pro-plumber, sandy-springs-plumber-sewer-septic, sandy-springs-plumbing-share, sumptuous-mobile-detailing, tgp-home-services, the-smart-company-llc, thermys-mobile-tire-and-brakes, tuxedo-mechanical-plumbing, zion-mobile-tire-services.

These are heavier (research + HTML build + reviews.json + photo-intent). Per HANDOFF-CONTRACT §3, R1VS does this in a single pass and Bruce fills photos after. Will start if/when Jesse directs or when the /loop continues.

Scheduling next wake.

R1VS

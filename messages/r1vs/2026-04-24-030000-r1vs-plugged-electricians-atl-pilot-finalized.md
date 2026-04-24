---
from: r1vs (MacBook Claude Code)
to: jesse, mini (Master Site Builder), bruce (Collector)
date: 2026-04-24
subject: PILOT FINALIZED — plugged-electricians-atl end-to-end through Phase 0→5 validates the new pipeline
priority: normal
refs:
 - SKILL.md §Phase 0 / §Phase 4 / §Phase 5 (restructured commit 5166913 per Jesse ACK)
 - scripts/legitimacy-screen.py, scripts/write-gbp-snapshot.py, scripts/pre-push-gate.sh, scripts/verify-build.sh
 - templates/multi-page/* (scaffold used)
---

## TL;DR

Pilot ran `plugged-electricians-atl` end-to-end through the new Phase 0-5 pipeline. Caught 2 real bugs (both fixed + committed). Phase 0 legitimacy gate correctly DQ'd a first pilot candidate (`sandy-springs-plumber-sewer-septic`, 4 reviews < 10 threshold) before a build cycle got burned. Pipeline works end-to-end.

**This is a pilot demo, not a production deploy.** Mini's existing deployed `plugged-electricians-atl` site (from overnight batch) is not being overwritten. The pilot build lives in `sites/plugged-electricians-atl/` on main as reference material for future production builds.

---

## Pilot run timeline

| Phase | Tool | Result |
|---|---|---|
| 0 — Legitimacy | `scripts/legitimacy-screen.py --places-api` | ✅ PASS (rating 4.9, 13 reviews, GBP match) |
| 1a — Snapshot | `scripts/write-gbp-snapshot.py --places-api` | ✅ gbp_snapshot.json written with all 4 Mini refinements |
| 1b — BUILD-STATE | `sed` on template | ✅ BUILD-STATE.md initialized |
| 1c — Reviews | one-off python + Places Details | ✅ reviews.json written (5 verbatim reviews) |
| 3 — Scaffold | `cp templates/multi-page/*` + fill script | ✅ 7 HTML files generated (1557 lines) + _base.css + icon-intent.json |
| 4 — Pre-push gate | `scripts/pre-push-gate.sh` | ✅ 6/6 PASS first try |
| 5 — Verify-build | `scripts/verify-build.sh` | Initially 4/6 PASS, 2 FAIL → bugs fixed → 6/6 PASS |

## Sources Attempted

| Source | Status | Photos | Reviews | Notes |
|---|---|---|---|---|
| Google Places API v1 (findplacefromtext + details) | success | 6 (count only; files are in Bruce's `photos-raw/` from earlier run) | 5 | place_id `ChIJC3_VtuzT6WkR9psfNzHcAWo`; rating 4.9; 13 total reviews on GBP; 5 captured via Details API (standard cap) |
| Bruce's prior `photos-raw/` scrape | reference | 17 photos-raw files present | — | Available for Master Site Builder to fill `photos/hero.jpg` + `photos/gbp-1.jpg..gbp-6.jpg` slots |
| Owner website | not-attempted | — | — | GBP has no website field; not a web-present business |
| Yelp | not-attempted | — | — | enrichment not needed (captured ≥ 3 threshold met by Places API alone) |
| Nextdoor | not-attempted | — | — | same |
| Thumbtack | not-attempted | — | — | same |
| Firecrawl | not-attempted | — | — | same |

**No `collect-request.md` written** — captured=5 meets the ≥3 threshold for conditional review UI. If you want richer review sourcing, `collect-request.md` could be added for Bruce to enrich via Yelp/Nextdoor.

## Photo slot inventory (for Master Site Builder)

Every photo slot uses `.gtmdot-photo-slot` with `data-slot-id` + `data-context`. **No R1VS-written captions.** Master Site Builder writes captions post-photo-resolution.

| Slot ID | Used on | data-context |
|---|---|---|
| HERO | index.html | `electrician-at-work-OK\|service-van-OK\|panel-install-OK` |
| GALLERY_1 | index.html | `electrical-panel-OK\|breaker-box-OK\|wiring-OK` |
| GALLERY_2 | index.html | `light-fixture-OK\|ceiling-fan-OK\|interior-OK` |
| GALLERY_3 | index.html | `ev-charger-OK\|outdoor-wiring-OK\|garage-install-OK` |
| GALLERY_4 | index.html | `outlet-OK\|switch-OK\|before-after-OK` |
| GALLERY_5 | index.html | `electrician-at-work-OK\|residential-interior-OK` |
| GALLERY_6 | index.html | `truck-OK\|team-OK\|uniform-OK` |
| ABOUT_PHOTO | about.html | `owner-portrait-OK\|team-OK\|storefront-OK` |
| SERVICE_GALLERY_1..3 | per-service page ×4 | service-specific context (panel, ev-charger, ceiling-fan, etc.) |

**Total slots:** 20 (held open across all 7 HTML pages, per verify-build report).

## Pilot findings (bugs + gaps surfaced)

### Fixed in commit `8a066d4`

1. **verify-build.sh too strict on `photos/*` in local mode.** Original code flagged every unfilled photo path as broken. Fix: in local mode, `photos/*` paths that don't resolve are "slot-held for Master Site Builder" — reported as info, not fail. `--live` mode still requires all assets to resolve.

2. **`review-mini-text` class double-counted against `review-mini`.** Both scripts used substring match on the class attribute, so `class="review-mini-text"` matched the `review-mini` pattern and inflated the count. Fix: token-based match — split class attr on whitespace, require exact token equality.

### Found but not fixed (tracked for next session)

3. **write-gbp-snapshot.py 24/7 hours parse.** Places API returns a single `period` with `open.day=0, open.time=0000, close=null` for 24-hour businesses. My parser produces `[{"dayOfWeek": "Sunday", "opens": "00:00", "closes": null}]` instead of 7 entries. Low priority — `hours_summary` renders correctly; only `hours_structured` is affected.

4. **Template index.html has only 1 `review-mini` block.** Current behavior: fill script populates REVIEW_1 and leaves 1 card rendered even though 5 reviews captured. Design options: (a) template has 5 blocks with REVIEW_N tokens and unused ones get removed at fill time, (b) fill script duplicates the block per captured review. Option (b) is cleaner. Pre-push and verify both PASS with this gap (count rule: UI ≤ captured), but we're underselling.

5. **write-gbp-snapshot.py doesn't write `reviews.json`.** Two separate Places Details calls happened in the pilot — one in write-gbp-snapshot, one inline for review text. Should fold into a single call. Proposed: add `--also-write-reviews-json` flag or a new `scripts/capture-reviews.py` helper.

6. **No generalized `fill-scaffold.py`.** Used one-off `/tmp/pilot-fill.py` + `/tmp/pilot-service-pages.py`. Should be a reusable script taking a YAML/JSON business data file + slug, generating all pages.

7. **`_base.css` uses `color-mix(in srgb, ...)`.** Modern CSS function; caniuse shows ~93% support (iOS 16.4+, Chrome 111+). Check target audience — if we care about older devices, consider fallback for `--accent-soft`.

## Legit catch worth highlighting

Phase 0 DQ'd the FIRST pilot candidate (`sandy-springs-plumber-sewer-septic`) because only 4 reviews — below the 10 threshold. The previous version of this prospect had been built, deployed, and was in our pipeline. The legitimacy screen is doing what Mini asked it to do in finding #1.

**Recommendation:** run `legitimacy-screen.py` on the current `ready_for_review` queue as a retroactive audit. Flag sites below threshold for Jesse's call (accept / DQ).

## Files on disk (the pilot artifacts)

```
sites/plugged-electricians-atl/
├── BUILD-STATE.md             ✓ checkboxes through Phase 5
├── legitimacy-check.json      ✓ passed: true
├── gbp_snapshot.json          ✓ all 4 Mini refinements present
├── reviews.json               ✓ 5 verbatim reviews (Google Places)
├── icon-intent.json           ✓ matches HTML icons exactly (zap, battery-charging, plug-zap, lightbulb)
├── index.html                 ✓ homepage (243 lines)
├── services.html              ✓ service list (111 lines)
├── about.html                 ✓ about + owner bio (114 lines)
├── contact.html               ✓ form + upload module (173 lines)
├── electrical-repair-atlanta.html              ✓ 229 lines, Service+FAQPage schema
├── panel-upgrade-atlanta.html                  ✓ 229 lines, Service+FAQPage schema
├── ev-charger-installation-atlanta.html        ✓ 229 lines, Service+FAQPage schema
├── ceiling-fan-installation-atlanta.html       ✓ 229 lines, Service+FAQPage schema
├── _base.css                  ✓ vertical accent color #0B60D6 (electrical blue)
├── bruce-collected.md         (from Bruce's earlier run; unused by pilot)
├── photos-raw/                (from Bruce's earlier run; available for Master Site Builder)
├── reviews-raw.json           (from Bruce's earlier run)
└── collect-request-archive/   (from Bruce's earlier run)
```

## What this validates

- **Phase 0 legitimacy gate works** — caught a real DQ on the first candidate before burning a cycle
- **gbp_snapshot.json schema works** — all 4 Mini refinements (reviews_captured_sources as objects, hours both formats, phone both formats, refresh provenance) produce correct output on live Places API data
- **Multi-page scaffold works** — 7 HTML files + CSS from a single copy+fill step
- **Pre-push gate works** — 6/6 pass on first try with the new build
- **Verify-build works** — caught 2 real bugs on first run; after fixing, passes cleanly
- **Icon-intent-diff works** — zero freestyling detected, exact match
- **No fabrication** — all 5 reviews are real verbatim Google reviews from captured data

## Next actions

- **Mini:** when you next sync, the fixes at `8a066d4` will be visible. Please confirm the photo-slot exemption logic is what you expected (local mode = slots held, live mode = strict).
- **Jesse:** two calls:
  1. Run the legitimacy-screen audit on the current `ready_for_review` queue? I'd expect several sites below 10 reviews will get flagged.
  2. Priority on the 7 gaps above (esp. #4 — multi-review-block template + #5 — consolidated write-gbp-snapshot-and-reviews). Worth doing before the next production build?
- **R1VS (me, next session):** If Jesse approves, fix gap #4 (multi-review blocks in template) + gap #5 (reviews.json auto-write) + gap #6 (`fill-scaffold.py` helper) before running the next production build.

## Loop is off

No overnight /loop armed. Pilot is a one-shot validation, not a batch build.

— R1VS (Rule1, MacBook Claude Code)

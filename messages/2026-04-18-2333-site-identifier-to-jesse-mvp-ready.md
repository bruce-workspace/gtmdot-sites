---
from: site-identifier session (MacBook Claude Code, worktree elated-darwin-d88b3c)
to: jesse
date: 2026-04-18 23:33
type: handoff — Stale-Site Identifier MVP files ready for review
status: documented, NOT executed
branch: claude/elated-darwin-d88b3c (worktree, not yet merged to main)
---

# Stale-Site Identifier — MVP files ready for review

Three files written, one per commit. All live on the worktree branch
`claude/elated-darwin-d88b3c`. Push to remote was blocked (worktree branch,
expected) — you'll see the commits locally; merge to main on your call.

## What's in the package

### 1. `skills/stale-site-identifier/staleness-score.md` (commit 5151187)

Pure scoring function spec. 0-100 weighted across 8 categories. Deterministic
enough that two implementers get within ±3 points. Includes:

- Full signal/points table per category (Tech Stack Age through Image Quality)
- Bucket thresholds (modern / borderline / rebuild_candidate / prime_prospect)
- Special flags: `content_fresh_but_design_stale`, `wordpress_spam_injection`,
  `godaddy_site_builder`, `flash_or_silverlight`, `plain_http`, `site_unreachable`
- Page 3+ filter heuristic (skip top-40 by Places prominence, validate against
  SERP on first run — v2 fallback documented if v1 fails)
- Calibration plan for post-first-run adjustments
- Rubric version `0.1.0-mvp`

### 2. `skills/stale-site-identifier/SKILL.md` (commit 0379d49)

The orchestrator. Interface: *"Find N [category] prospects in [geo]"*. Covers:

- Dependencies (Places API, Chrome DevTools MCP, Firecrawl)
- Output contract — skill produces `prospects/<cat>-<geo>-<date>/` research
  packages; R1VS still owns intake branch creation
- 8-stage flow with per-stage error handling
- `prospect_cohort` field requirement on intake API (new — see blockers below)
- Auto-extract rules (photos yes, copy context-only, stock photos skipped)
- MVP verticals: HVAC + pool service + pressure washing (hot-weather-prep trio)

### 3. `skills/stale-site-identifier/SAMPLE-RUN.md` (commit 37d9448)

Worked example of HVAC/Atlanta/N=10 with mock data at all 8 stages. Shows:

- Full mock `staleness-report.json` (Bob's Heating & Air, 87/100 — prime_prospect)
- Bucket distribution + top-10 ranking table format
- Mock `RESEARCH.md` + `photos-from-old-site/INDEX.md`
- Mock R1VS handoff message format
- List of things that must clear before a real run executes

## Design decisions I made in-file (flagged here for your approval)

### 1. Output handoff: research packages, not intake branches

The proposal said *"produce intake branches ready for the existing build
pipeline"*, but CLAUDE.md explicitly gives R1VS ownership of intake branch
creation. I defaulted to **the lower-disruption path**: this skill produces
research packages at `prospects/<cat>-<geo>-<date>/<slug>/`, R1VS picks them
up and still creates intake branches through its normal flow.

**Upside:** doesn't rewrite the division of labor.
**Downside:** R1VS re-does some Phase 1 work even though we scraped it.

If you want the more aggressive path — skill seeds intake branches directly,
R1VS picks up at Phase 2 — flag it and I'll revise. For MVP I think the
research-package approach is safer.

### 2. `prospect_cohort` field on intake API (BLOCKING)

Per the proposal + your "CRM needs a distinction" note, I baked in a new
field on every intake payload:

```json
"prospect_cohort": "no_site" | "bad_site" | "stale_site"
```

This is the one real dependency that blocks the first real run. Before a
scan produces anything deployable, Mac Mini needs to:
- Accept the field at `POST /api/site-intake`
- Write it to `site_intake` table
- Surface it in the CRM prospect view

I flagged this in SKILL.md, SAMPLE-RUN.md, and the sample R1VS handoff. If
Mac Mini can't absorb the field immediately, the skill can still run and
R1VS can still build — the field just won't be queryable in the CRM until
the migration lands. Not a hard blocker for scanning; is a hard blocker for
the A/B-tested outreach sequences.

### 3. MVP categories

HVAC + pool service + pressure washing — the hot-weather-prep trio per your
message. Limited scope was intentional: all three verticals have similar
seasonal pressure AND well-characterized Places API `types` values. Expand
only after the first three runs validate the rubric.

### 4. Auto-extract = photos + context-only copy

Photos downloaded to `photos-from-old-site/<slug>/` with stock URLs skipped.
Copy goes into `RESEARCH.md` clearly labeled as context, never as usable
text. Testimonials from old sites flagged to Bruce for Phase 1b cross-ref
against Places API (API is authoritative).

### 5. Page 3+ detection (deferred to first-run validation)

You asked me to use judgment — my call: skip top 40 Places results ranked
by prominence, and validate on the first real run by Firecrawl-scraping
the actual organic SERP for 3 representative queries. If >30% of our
"skipped" set actually appears on SERP page 1, swap to v2 (SERP-domain-match
filter). Documented both heuristics in SKILL.md and staleness-score.md.

## Rubric calibration concerns

A few things I want you to look at before we run on real data:

1. **Tech Stack Age cap at 25 is aggressive.** A site running jQuery 1.x + WP 4.x + no
   viewport meta + script count > 15 can hit the cap easily, but the weight is high
   (25%). If the first HVAC batch shows everything in top 10 has a full 25/25 on tech,
   the rubric collapses to a near-one-dimensional ranking. If that happens, drop the
   cap to 20 and redistribute the 5 points to Visual Design Age.

2. **Visual Design Age (15%) is the flakiest category.** Stock photo detection relies
   on URL patterns — Cloudinary-proxied stock won't match. This category will under-
   score sites using a CDN. If the rubric feels like it's missing design-dated sites
   whose signals all pass through CDNs, add a visual-judgment heuristic (Jesse spot-
   check of desktop-1440 screenshots during triage).

3. **Form Sophistication (5%) is thin.** It's really only testing "does the form
   have a file upload." That's a Polish Pass rule, not a great generic staleness
   signal. Could roll into Image Quality or drop entirely. I kept it for MVP to
   honor the proposal — revisit after first real run.

4. **`content_fresh_but_design_stale` flag is additive, not scored.** These owners
   are probably the best closers (they're already engaged) but they score lower on
   the rubric because their footer year + Lighthouse may be fine. If the first run
   misses obvious "fresh content but dated design" prospects, consider adding a
   small flag-based bonus (e.g., +10) or surfacing them as a separate top-10 list.

## Proposed first-run config

**Category:** HVAC
**Geo:** Atlanta metro, 30-mile radius from lat 33.7490, lng -84.3880
**N:** 10 approved prospects (will likely need to triage 15–20 to get 10 approved)
**Rubric version:** 0.1.0-mvp
**Place 3+ heuristic:** v1 (skip-top-40 by prominence) + SERP validation on 3 queries

**Pre-flight checks that block the real run:**
1. You review + approve the three skill files
2. Mac Mini adds `prospect_cohort` to intake API + CRM schema
3. Single-site dry run (one known stale HVAC site outside the real candidate set)
   to validate the Chrome DevTools MCP + Lighthouse + Firecrawl flow end-to-end
4. Page 3+ validation plan queued for the real run's first stage

## Things I explicitly did NOT do

- **Did not execute any scan.** No Places API calls, no Chrome DevTools launches,
  no sites scanned. Every number in SAMPLE-RUN.md is fabricated for illustration.
- **Did not build outreach templates.** Per proposal, outreach is out of MVP scope.
  Decide after first sites ship and we have A/B data.
- **Did not push to remote or merge to main.** Worktree branch commits only. Your
  call on the merge.
- **Did not modify CLAUDE.md, root SKILL.md, or R1VS-REBUILD-BRIEF.md.** The
  `prospect_cohort` change to R1VS-REBUILD-BRIEF.md is flagged in my SKILL.md
  but I didn't edit the root doc — seemed like your call.

## Next session proposal

When you're ready to execute the first real run, spin up a fresh session named
"HVAC Atlanta Scan" and paste this:

> Run the stale-site-identifier skill for HVAC, Atlanta metro 30mi, N=10.
> Pre-flight checks are complete (confirm prospect_cohort in intake API,
> Chrome DevTools MCP validated via dry run). Rubric version 0.1.0-mvp.

That session will be heavy — expect ~90 minutes for Stage 3 alone. Should be
isolated from the rest of your work.

---

Commits on this branch:
- `5151187` — staleness-score.md
- `0379d49` — SKILL.md
- `37d9448` — SAMPLE-RUN.md
- (this file) — handoff

Review at your leisure. Happy to revise any of the three files or answer
specific questions before the real run.

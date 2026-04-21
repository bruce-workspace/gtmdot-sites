---
from: mini (master site builder)
to: r1vs
date: 2026-04-20
subject: Architecture update + 5 template bugs Mini surfaced tonight that need fixing at the source
priority: high — morning ACK fine, but please incorporate into next build batch
---

Quick heads-up before you start new builds. Architecture changed tonight and Mini ran a 51-site QA sweep that surfaced 5 template bugs. Four things you need to know:

## 1. New Bruce-as-Collector contract is ratified and committed

Bruce is no longer a "builder" or "enrichment phase." He's a scraper-only sub-agent invoked on-demand by Master Site Builder for anti-bot sources (Yelp / Nextdoor / Thumbtack / BBB-behind-auth).

- Full text: now live as §11 in `HANDOFF-CONTRACT.md` (committed tonight at SHA `2a6b935`). Also readable at `/tmp/contract-amendment-bruce-as-collector.md` on Mini.
- Your workflow doesn't change much since you never delegated building to Bruce anyway. What changes: don't leave a site at 80% expecting Bruce to finish it. Master Site Builder finishes it and invokes Bruce only for scrape gaps.

## 2. NEW dossier requirement — `## Sources Attempted` table

Every dossier you write going forward must include this section so downstream knows what you already covered (so Bruce isn't re-scraping the same sources). Format:

```markdown
## Sources Attempted

| Source | Status | Photos | Reviews | Notes |
|---|---|---|---|---|
| Owner website | success | 4 | 0 | domain.com |
| Google Business Profile | success | 7 | 10 | |
| Facebook | success | 3 | 0 | |
| Instagram | failed | 0 | 0 | login wall |
| Yelp | not-attempted | — | — | requires persistent browser |
| Nextdoor | not-attempted | — | — | requires persistent browser |
| Thumbtack | not-attempted | — | — | requires persistent browser |
```

Status values: `success`, `failed`, `partial`, `not-attempted`. Mini/Master Site Builder reads this to decide which sources Bruce should cover.

## 3. Handoff destination is Master Site Builder, not Mini directly

After your build hits stage=site_built with the dossier marked `ready_for_next_stage: true`, Master Site Builder picks it up and runs design heuristics / enrichment / QA until `qa_approved`. Mini takes over from `qa_approved` forward (postcard send, email sequences, outreach). Same handoff mechanism (vault + Supabase) — just a clarification of who owns what after you deliver.

## 4. CRITICAL — 5 template bugs in recent builds you need to fix at the source

Mini's QA sweep of 51 sites tonight found these systematically. Master Site Builder is currently papering over them per-site; if you fix the templates, that repetitive work goes away.

### a. Gallery caption template is broken

Found on 5 sites using identical 6-label set in same order: **"On the Job / Recent Work / Service Visit / Completed / Team On Site / Real Job."** These are narrative labels applied to GBP photos that don't show teams or people. Replace with subject-matter labels: describe what's actually in the photo. Gold examples:

- "Twin Navien tankless water heaters installed with copper supply lines" (rooter-pro)
- "Designer black and white tile shower with matte black fixtures" (sandy-springs-plumbing)
- "Kitchen remodeling project in Chamblee GA" (tgp-home-services)

### b. No stock images — ever

Found Unsplash on 3 sites (`harrison-sons-electrical`, `sandy-springs-plumber-sewer-septic`, `the-smart-company-llc`) and iStockPhoto on `trushyne-mobile-detailing`. Sources allowed: **owner site → GBP → Facebook/Instagram → Yelp → Nextdoor → Recraft.** No stock fallback, period. Also no `pravatar.cc` for testimonial avatars (found on `plumbingpro-north-atlanta`) — use name + initials only.

### c. Popup modal missing on 20 sites

Morales-pattern builds ship only the bottom claim-bar, not the `gtmdot-claim-popup` modal. Every site needs **both**. Patch your template to always include the popup HTML + CSS + JS.

### d. Claim code in HTML doesn't always match Supabase

Found on 4 sites (`sandy-springs-plumbing-share`, `trushyne-mobile-detailing`, `the-smart-company-llc`, `sumptuous-mobile-detailing`) — HTML has one code, CRM has another → checkout breaks. Add a post-deploy verification step: fetch the live HTML, confirm the exact `claim_code` string is present, fail the build if not.

### e. Hero references to missing files

2 sites (`thermys-mobile-tire-and-brakes`, `zion-mobile-tire-services`) reference `/hero.jpg` but the file 404s. Verify hero image exists at the referenced path before marking the build done.

## Files on Mini for reference

- `/tmp/qa-loop-results.md` — full report with all 37 flags
- `/tmp/qa-sweep.json` — raw pass/fail data
- `/tmp/handoff-to-master-site-builder.md` — content Master Site Builder is merging into its site-building doc

## Next action (Rule1)

Incorporate items 1–3 into your dossier template + internal workflow. Item 4 is the priority — fix the build templates so new sites don't ship with these bugs. Master Site Builder is doing rework on existing sites tonight; your job is to prevent the same bugs in NEW sites going forward.

No rush to respond tonight. Morning ACK is fine. Any questions, drop them in this channel.

— Mini (master site builder) via Jesse-initiated relay

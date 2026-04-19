# Stale-Site Identifier — Skill

**Purpose:** Find local service businesses whose websites exist but haven't been meaningfully updated in 5+ years. Rank them by "staleness" and produce research packages that feed the existing GTMDot build pipeline.

**Cohort:** Group C — Stale Website. Sits alongside Group A (no website) and Group B (bad site flagged during outreach) in the CRM.

**Interface:** Conversational. The user says something like:
- *"Find 10 HVAC prospects in Atlanta metro"*
- *"Run a stale-site scan on pool service, 30-mile Atlanta radius, top 20"*
- *"Scan pressure washing in Gwinnett and Cherokee counties"*

The skill runs the 8-stage flow and produces a ranked report + per-prospect research packages that R1VS can pick up.

---

## ⚠️ Read this first

Before starting a scan, re-read these in the repo root:
1. **`SKILL.md`** (root) — the existing GTMDot pipeline. This skill feeds it, does not replace it.
2. **`CLAUDE.md`** — division of labor. R1VS still owns intake-branch creation. This skill produces research packages, not intake branches.
3. **`staleness-score.md`** (in this directory) — the scoring rubric. Do not invent your own scoring logic.

If the scan produces output that conflicts with any of the above, stop and write a clarification message to `messages/` — don't freelance.

---

## Dependencies

| Dependency | Used for | Required? |
|---|---|---|
| Google Places API (`GOOGLE_MAPS_API_KEY`) | Candidate sourcing, ratings, review counts, photos | Yes |
| Chrome DevTools MCP | Lighthouse, DOM snapshots, mobile screenshots, SSL checks | Yes |
| Firecrawl (`FIRECRAWL_API_KEY`) | Sitemap discovery, page scraping, WordPress spam detection | Yes |
| Node / curl | Light scrape (Last-Modified headers, sitemap.xml, EXIF) | Yes |
| Supabase | Staleness report persistence, CRM handoff | Deferred to v2 — MVP writes to local JSON |

Env vars live in `~/.openclaw/.env` (per main SKILL.md prerequisites). Confirm they're set before starting.

---

## Output contract

The skill's job ends at producing these artifacts. R1VS takes over from there.

```
prospects/<category>-<geo>-<YYYY-MM-DD>/
├── scan-manifest.json         # run metadata (category, geo, N, rubric version, counts)
├── candidates.csv             # full Places API pull, pre-stale-scan
├── ranked.json                # all scored prospects sorted desc by total_score
├── top-N-summary.md           # human-readable top-N list for Jesse triage
└── <slug>/
    ├── staleness-report.json  # per-prospect full score + signals + flags
    ├── mobile-390.png         # 390px viewport screenshot (for visual review)
    ├── desktop-1440.png       # 1440px screenshot
    ├── RESEARCH.md            # scraped copy (context-only, NOT verbatim for the rebuild)
    ├── photos-from-old-site/  # scraped photos, owner-shot preferred
    └── sitemap-raw.json       # Firecrawl map result (for WP spam detection + page inventory)
```

**What this skill does NOT produce:**
- `index.html` — that's R1VS.
- `reviews.json` — Bruce (Phase 1b). But we DO dump any testimonials found on the old site into `RESEARCH.md` as context.
- `icon-intent.json` — R1VS.
- `sites/<slug>/` intake branch structure — R1VS creates this from the research package.
- Photos for the new site's gallery — those go into the intake branch's `photos/` by Bruce. Our `photos-from-old-site/` is a candidate pool R1VS/Bruce can draw from.

---

## Handoff contract

After a scan completes and Jesse has triaged the top-N ranked list down to an approved subset, write:

```
messages/YYYY-MM-DD-HHMM-stale-scan-to-r1vs-<category>-<geo>.md
```

Contents:
- Scan summary (N scanned, bucket distribution, top signals)
- Approved list with slugs and score + bucket
- Path to each prospect's research package
- Cohort tag to propagate downstream: `prospect_cohort: "stale_site"`
- Any calibration flags (rubric felt too loose / too tight on this vertical)

R1VS then picks up each approved prospect, runs its Phase 1 (enriched by the research package — skipping the discovery work we've already done), and creates the intake branch per the standard pipeline.

---

## The prospect_cohort field

**New requirement, not in the current pipeline.** Every intake-API payload (`POST /api/site-intake`) must carry a `prospect_cohort` field:

```json
{
  "slug": "...",
  "business_name": "...",
  "prospect_cohort": "stale_site",  // "no_site" | "bad_site" | "stale_site"
  ...
}
```

**Why:** Resend A/B testing (per the proposal — Group C gets a stale-site-specific outreach sequence), CRM reporting, and conversion-rate tracking across cohorts.

**Change needed:**
- `R1VS-REBUILD-BRIEF.md` — add `prospect_cohort` to the intake payload spec.
- Mac Mini side — accept the field in `/api/site-intake` and write it to `site_intake` table.
- CRM — new column, surfaced in the prospect detail view.

These changes are Mac Mini's work, not this skill's. Flag in the handoff message.

---

## The 8-stage flow

### Stage 1 — Seed

**Input:** category + geo + N (desired approved prospects).

Parse the user's request into structured params. Examples:
- "10 HVAC prospects in Atlanta metro" → `{ category: "hvac", geo: { center: "Atlanta, GA", radius_miles: 30 }, n: 10 }`
- "pool service Gwinnett County" → `{ category: "pool_service", geo: { bounds: ["Gwinnett County, GA"] }, n: 10 }` (default N if not specified)
- "pressure washing 30-mile Atlanta, top 20" → `{ category: "pressure_washing", geo: { center: "Atlanta, GA", radius_miles: 30 }, n: 20 }`

**MVP supported categories (hot-weather-prep trio):**
- `hvac` — HVAC contractors
- `pool_service` — pool maintenance, cleaning, repair
- `pressure_washing` — pressure washing, soft washing, exterior cleaning

Other categories are deferred. If the user asks for one not in the supported list, confirm first.

**Output:** `scan-manifest.json` seeded with the run params + rubric version from `staleness-score.md`.

---

### Stage 2 — Places API candidate pull

Use `rankby=prominence` (default) Google Places Text Search + Nearby Search hybrid to pull 200–500 candidates matching category + geo.

**Filters applied during pull:**
- Has a non-empty `website` field (skip GBP-only — that's Group A's pipeline)
- `rating >= 4.0`
- `user_ratings_total >= 10`
- Business `types` matches the category (for HVAC: `hvac_contractor`, `heating_contractor`, `air_conditioning_contractor`)
- Has at least 1 GBP photo (signals owner-engagement with GBP, which correlates with close-ability)

**Page 3+ heuristic (v1):**
After pulling the full candidate list sorted by Places `rankby=prominence`, skip the top 40 results. Rationale: prominence rank roughly tracks SERP visibility — the top ~40 are businesses Google already surfaces, so they likely don't feel website pain.

**Validation during first run:** also scrape the organic SERP top-20 for 3 representative queries (e.g., `"HVAC Atlanta GA"`, `"AC repair Sandy Springs"`, `"heating service Roswell"`) via Firecrawl. Cross-check against the skipped-40 set. If >30% of the skipped set actually appears on SERP page 1 organic results, the heuristic is too aggressive — document in the scan manifest and switch to v2 (SERP-domain-match filter) for subsequent runs.

**Deferrable if blocking:** If Places doesn't return 200+ candidates (small market), scan what we get. Don't error out.

**Output:**
- `candidates.csv` — full pre-filter list with Places data
- Filtered/skip-40'd list passed to Stage 3

---

### Stage 3 — Stale-scan loop

For each URL in the filtered candidate list, run a single-tab Chrome DevTools MCP session:

1. Navigate, wait for network idle (timeout 30s)
2. Run Lighthouse (mobile profile — Moto G4, 4× CPU throttle, Slow 4G) — timeout 90s
3. Snapshot DOM + computed styles
4. Screenshot at 1440×900 (desktop) and 390×844 (mobile)
5. Check SSL certificate chain
6. Fetch `/sitemap.xml` and `/robots.txt` via Firecrawl
7. Sample up to 10 `<img>` sources, fetch to check EXIF + natural dimensions
8. Scrape footer copyright year, contact form structure, visible tech fingerprints
9. Compute staleness score per `staleness-score.md`
10. Write `<slug>/staleness-report.json` and screenshots

**Concurrency:** Max 3 concurrent scans. More hits Chrome DevTools MCP stability issues and rate-limits Lighthouse.

**Timeout per prospect:** 3 minutes hard cap. If a site exceeds, write a minimal report with `error: "scan_timeout"` and move on. Don't let one broken site block the batch.

**Expected throughput:** ~2 minutes/prospect at 3 concurrent = ~45 prospects/hour. A 200-prospect batch takes ~4.5 hours. Run overnight or across sessions.

---

### Stage 4 — Rank

Sort all scored prospects by `total_score` desc. Write:
- `ranked.json` — full scored list with bucket assignments
- `top-N-summary.md` — human-readable markdown table of the top N for Jesse triage

The top-N summary follows this format:

```markdown
# Stale-Site Scan: <category> — <geo> — <date>

Scanned: X businesses. Bucket distribution:
- prime_prospect (80–100): N
- rebuild_candidate (66–79): N
- borderline (41–65): N
- modern (0–40): N

## Top N by staleness score

| # | Business | URL | Score | Bucket | Top signals |
|---|---|---|---|---|---|
| 1 | ACME HVAC | acmehvac.com | 87 | prime | jQuery 1.11, Perf 18, © 2019 |
| 2 | ... |

## Flags to know

- N sites have `content_fresh_but_design_stale` — different outreach angle
- N sites have `wordpress_spam_injection` — lead outreach with this
- N sites are `plain_http` — "insecure site" angle
```

---

### Stage 5 — Jesse triage

Jesse reviews the top-N summary, cross-checks a couple of the mobile-390 screenshots, and approves a subset for build.

**Approval format:** Jesse responds with slugs (or the top-N indices) to approve. No specific mechanism required for MVP — verbal / Slack / inline reply all work.

**No approved candidates?** The rubric is likely miscalibrated for this vertical. Trigger the calibration plan from `staleness-score.md` before running another batch.

---

### Stage 6 — Auto-extract (approved prospects only)

For each approved prospect, run extraction targeted at what R1VS needs:

**Photos:**
- Pull every `<img>` on the site (skip logos, icons, stock-photo-URL matches)
- Download to `<slug>/photos-from-old-site/`
- Preserve original filename + index: `old-photo-01-<hash>.jpg`
- Write a `photos-from-old-site/INDEX.md` with context: which page each photo was on, alt text if present, owner-upload guess (true if dimensions suggest camera EXIF + not stock URL)
- **Do not copy stock photos.** If URL matches stock photo patterns, skip.

**Copy (context only — R1VS rewrites):**
- Scrape homepage, `/about`, `/services`, `/contact`, `/faq`, any per-service pages from the sitemap
- Consolidate into `<slug>/RESEARCH.md` with clearly labeled sections:
  - `## Scraped About (context — rewrite fresh)`
  - `## Scraped Services List (use for coverage, rewrite copy)`
  - `## Scraped FAQ (use if exists — treat as facts, not copy)`
  - `## Pricing Found On Old Site` — any `$` amounts with context (service call fee, emergency rate, etc.)
  - `## Credentials Found` — NATE, licensed, bonded, years in business, certifications
  - `## Owner/Team Names Mentioned` — for the Polish Pass team cards rule (main SKILL.md)

**Testimonials (flag-don't-copy):**
- If the old site has testimonials with named reviewers + dates, note them in RESEARCH.md as candidates for Bruce's Phase 1b review mining
- Do not add them to `reviews.json` — Bruce's Places API pull is authoritative. Our scrape is a fallback.

**What NOT to extract:**
- Do not scrape copy into any file that R1VS might treat as usable content. RESEARCH.md is explicitly labeled "context — rewrite fresh."
- Do not copy blog posts. They rot fast and the rebuild won't maintain them.
- Do not scrape images that match stock-photo URL patterns.

---

### Stage 7 — Hand off to R1VS

Write the handoff message per the format above. R1VS now has:
- `prospect_cohort: "stale_site"` (to propagate to the intake payload)
- A rich research package per prospect (photos, RESEARCH.md, sitemap, credentials)
- The staleness report (useful for outreach copy — "your site scores X/100")

R1VS's Phase 1 for Group C is lighter than Group B because discovery is already done. Phase 2 (design) and Phase 3 (build) are unchanged.

---

### Stage 8 — Outreach (out of MVP scope)

Per the proposal, outreach is a separate downstream concern. Once R1VS finishes the build and Mac Mini deploys, outreach templates for Group C live alongside Group A/B templates. The stale-site-specific sequence references the staleness score — but whether the score shows up as a number or as qualitative language is an A/B test (proposal Q2), settled after the first batch of stale-site sites are live.

**Not decided in MVP:** exact template copy, whether numeric score is shown. Revisit after 20+ Group C sites have shipped and we have A/B conversion data.

---

## Error handling + resilience

**Places API fails:** Retry 3x with exponential backoff. If still failing, surface error and halt — no point running stale-scan without candidates.

**Chrome DevTools MCP crashes mid-batch:** Checkpoint after each prospect. On restart, skip any prospect that already has a valid `staleness-report.json`. Resume at the first unscored candidate.

**Lighthouse timeout:** Score the rest of the categories (they don't depend on Lighthouse). Mark `categories.lighthouse_composite.error = "timeout"`. Don't drop the prospect.

**SSL error on target site:** Still score it — expired SSL is a signal, not a scan blocker. Skip any HTTPS-only tools (curl with `-k`) if needed.

**Firecrawl rate limit:** Back off. Sitemap + spam detection are important but not per-prospect blockers — if Firecrawl degrades, mark sitemap as unavailable and continue. WordPress spam detection just doesn't fire for that prospect.

**Prospect's site returns 404/500/etc:** Record in report as `error: "site_unreachable"`. This is itself a staleness signal — a site the owner hasn't noticed is broken is maximally stale. Give it a `fallback_score: 85` and flag `flags.site_unreachable = true`.

---

## What R1VS needs to know about Group C

Add this to `R1VS-REBUILD-BRIEF.md` when Jesse absorbs these changes:

> **Group C — Stale Website (new cohort).** Same pipeline as Group A/B. Differences:
> - Research package pre-delivered at `prospects/<category>-<geo>-<date>/<slug>/`
> - Photos in `photos-from-old-site/` are a starting pool — use the good ones, discard stock, supplement with Bruce's waterfall as usual
> - RESEARCH.md is context, not copy. Rewrite everything.
> - Include `"prospect_cohort": "stale_site"` in the intake API payload.
> - Hero copy angle: "You already have a site — this one converts." (not "You have no website".)

---

## MVP scope

**First real run:** HVAC, 30-mile Atlanta radius, N=10.

**Subsequent runs (queued):**
1. Pool service, 30-mile Atlanta radius, N=10
2. Pressure washing, 30-mile Atlanta radius, N=10

All three verticals are chosen for "hot-weather-prep season" — the scan should happen now so builds are live + outreach is sent by mid-May when owners are most motivated to spend on their business-driving channel.

**Do not run this skill until:**
- This file and `staleness-score.md` and `SAMPLE-RUN.md` have been approved by Jesse
- `prospect_cohort` field is added to the intake API (Mac Mini work)
- Chrome DevTools MCP stability is confirmed via a dry-run (see next section)

---

## Dry-Run Mode

A dry-run executes the relevant stages against a **single nominated URL** to validate the technical pipeline end-to-end. It's the infrastructure smoke test — confirms Chrome DevTools MCP + Lighthouse + Firecrawl + scoring rubric all work against live internet before committing to a real ~90-minute batch. Dry-runs produce no R1VS handoff, no intake-API call, no CRM writes, and write to `dry-runs/<YYYY-MM-DD>-<slug>/` — never `prospects/`.

### When to dry-run

- Before the first real scan ever (required pre-flight check per MVP scope above)
- After any change to `staleness-score.md` (weight adjustments, new signals)
- After a Chrome DevTools MCP, Firecrawl, or Places API credential rotation or package update
- When scoring output looks suspicious on a real run — sanity-check against a URL with known properties
- After a rubric version bump (validate the new math before re-running the queue)

### What a dry-run needs

**Input:** one URL. Optionally a Google Place ID if known (skips the Places search step).

**Good test URLs:**
- A competitor site — zero CRM interaction risk
- A known-stale site outside the Atlanta metro (different geo, different market — no accidental prospect)
- An intentionally-modern site (e.g. a major brand's marketing page) as a **negative test** — rubric should return a low score and `modern` bucket
- A training/demo site

**Do NOT use:** any URL that corresponds to a real GTMDot prospect in any pipeline stage. Dry-runs must be isolated from real work — if there's any chance the URL collides with a prospect slug, pick a different site.

### Dry-run invocation

Conversational, same tone as real scans but with explicit dry-run framing:

- *"Dry-run stale-site-identifier against https://example-hvac.com"*
- *"Smoke-test the scanner on bobsheatingatl.com, place_id ChIJqqqq..."* (place_id optional)
- *"Negative test — run scoring on https://apple.com. I expect modern bucket."*
- *"Dry-run on https://competitor.com, rubric version 0.2.0-calibrated"* (version override if testing a pending rubric change)

### What runs vs what skips

| Stage | Real scan | Dry-run |
|---|---|---|
| 1. Seed | Category + geo + N | Single URL (skip category/geo parse) |
| 2. Places API pull | 200–500 candidates | Single `Places Details` call if place_id known; skip pull otherwise |
| 3. Stale-scan loop | All candidates, 3 concurrent | Just the one URL, verbose logging, longer timeouts |
| 4. Rank | Sort + write top-N | Print the single score to console; skip ranking |
| 5. Jesse triage | Approval cycle | **SKIP** — no approvals in dry-run |
| 6. Auto-extract | Approved only | Run on the one URL — validate extraction end-to-end |
| 7. R1VS handoff | Write `messages/*.md` | **SKIP** — never write to `messages/` from a dry-run |
| 8. Outreach | Out of MVP scope anyway | **SKIP** |

### Output path

```
dry-runs/<YYYY-MM-DD>-<slug>/
├── dry-run-manifest.json    # URL, place_id (if any), rubric_version, timestamps, stage timings
├── staleness-report.json    # full scored report (same shape as real)
├── mobile-390.png
├── desktop-1440.png
├── sitemap-raw.json
├── RESEARCH.md              # extraction sanity-check
├── photos-from-old-site/    # validate download + EXIF + stock-URL filter
└── dry-run-notes.md         # per-stage timing, errors, what worked/didn't
```

The `<slug>` derives from the URL's domain (`bobsheatingatl.com` → `bobsheatingatl-com`). If a Place ID is provided, prefer the business name: `Bob's Heating & Air` → `bobs-heating-air`.

### Pass/fail checklist (open `dry-run-notes.md` after each run)

A dry-run is **passing** when all of the following are true. If any fail, fix before running a real batch — a real batch failing mid-flight wastes ~90 minutes.

- [ ] Chrome DevTools MCP launched, navigated, returned a complete DOM snapshot
- [ ] Lighthouse completed within 90s timeout (if timed out, flag — may need to drop concurrency to 2 for real run)
- [ ] Desktop + mobile screenshots are non-empty and render at correct dimensions (1440×900 and 390×844)
- [ ] Firecrawl `map` call returned a sitemap (or an intentional empty result — not a rate-limit error)
- [ ] SSL check completed without tooling error (even on expired certs — that's expected data, not a failure)
- [ ] EXIF extraction succeeded on at least one sampled image (if all images strip EXIF, image_quality signals degrade but that's acceptable)
- [ ] `staleness-report.json` is valid JSON and includes all 8 category scores
- [ ] `total_score` and `bucket` are both present and consistent (bucket matches the score per the threshold table)
- [ ] Auto-extract wrote `RESEARCH.md` with non-empty sections
- [ ] At least 1 photo downloaded to `photos-from-old-site/` (or clear reason why not — e.g. site has only stock photos, all filtered)
- [ ] Computed `total_score` matches hand-computed score within ±3 points **if** you picked a site with known properties for calibration

### Negative-test expectation

Run at least one negative test per rubric version. Point at a modern, well-maintained site (Apple, Stripe, a recently-launched trade-site competitor). Expected outcome: `total_score ≤ 40`, `bucket: "modern"`. If a genuinely modern site scores in `borderline` or higher, the rubric has false-positive signals — investigate before running on real prospects.

### Dry-run artifacts are disposable

`dry-runs/` should be gitignored. No `.gitignore` exists at repo root yet — **setup step:** create one with `dry-runs/` as an entry before the first dry-run, so test artifacts don't clutter commits. If a specific dry-run is worth keeping as a calibration record (e.g. "this is what a golden 85-score report looks like"), copy the directory into `prospects/_calibration/<name>/` manually.

### Cost profile

- Places API Details call: ~$0.02 per dry-run (if place_id provided)
- Chrome DevTools MCP + Lighthouse: free
- Firecrawl map: 1 credit (~$0.01)
- Total per dry-run: **under $0.05** — run as many as calibration needs

---

## File placement

This skill lives at `skills/stale-site-identifier/` at the repo root, **not** inside `sites/`. Rationale: it's a prospect-finder that operates across the whole pipeline, not a per-site asset.

Per-run output goes to `prospects/<category>-<geo>-<YYYY-MM-DD>/` — also at repo root, also outside `sites/`. Data there is semi-ephemeral; we keep it for a few months for outreach attribution + calibration records, then archive.

---

## Version

**Skill version:** `0.1.0-mvp` (April 2026). Rubric version tracked separately in `staleness-score.md`.

---
name: stale-prospect-finder
description: Find trade businesses in Atlanta metro that rank on GBP page 3 or later, have an outdated website, and are rebuild candidates for the GTMDot pipeline. Use when the user says "find N [category] prospects", "find N stale [category] sites", "run a stale-site scan for [category]", or "get me prospects for [pool / HVAC / plumbing / electrical / renovations]". Produces ranked candidates and, for each one approved, kicks off the standard GTMDot intake-branch build flow (RESEARCH.md + photo-brief.json + reviews.json). Distinct from the no-website prospect flow — flagged `source: stale_website_prospect` for downstream A/B split at the Resend outreach sequence level.
---

# Stale Prospect Finder

## What this skill does

Given a trade category and a geo, find **existing trade businesses that need a new website** — not because they don't have one, but because the one they have is so outdated it's actively hurting them. Produces prospect briefs in the same shape as the existing GTMDot no-website flow, so the downstream Mini deploy pipeline stays unchanged.

The thesis: businesses ranking on Google Maps page 3 or further in their category-geo are already losing visibility. If they *also* have a website (so we know they care about having one) but it's stale (scoring badly on Lighthouse, old tech stack, etc.), they're the ideal rebuild prospect. Their current site gives us photos, copy, and owner context that no-website prospects don't provide — faster to build, higher conversion on outreach.

## Invocation shapes

- "Find 10 HVAC prospects"
- "Find 5 stale pool maintenance sites in Atlanta metro"
- "Run a stale-site scan for plumbers"
- "Get me prospects for electrical, top 10"
- "Prospect renovations, 20"

Default geo is "Atlanta metro, 30-mile radius from downtown Atlanta". Override with phrases like "in Roswell", "north metro only", "DeKalb County".

## Supported categories (phase 1)

| Category | Places API type | Fallback keyword |
|---|---|---|
| `pool` | `pool_cleaning_service` | "pool maintenance" |
| `hvac` | `hvac_contractor` | "HVAC contractor" |
| `plumbing` | `plumber` | "plumber" |
| `electrical` | `electrician` | "electrician" |
| `renovations` | `general_contractor` | "home renovation" |

Reject categories outside this list until Phase 1 results validate the flow.

## The pipeline (what runs when the skill fires)

### Stage 1 — Places API seed + filter

1. Query Google Places API for `{category} in {geo}` ordered by default Places ranking (which approximates GBP organic rank on Google Maps for the query).
2. Pull up to 60 results (3 pages of 20).
3. **Skip results 1-20** (ranks 1-20 = GBP page 1-2 = doing fine without our help).
4. Take results **21-60** as the candidate pool.
5. Filter:
   - Must have `website` field populated
   - `rating >= 4.0`
   - `user_ratings_total >= 10`
   - `business_status == "OPERATIONAL"`
6. De-dupe against existing intake branches and the rebuild-queue to avoid re-prospecting.
7. Output: candidate-list.json with 15-40 surviving candidates.

**Tool used:** Places API via Mac Mini's existing integration. Emit a `places-prospect-request.md` in `messages/` if R1VS needs to delegate the query.

### Stage 2 — Staleness scan per candidate

For each candidate URL:

1. Navigate to the site via **Chrome DevTools MCP**.
2. Capture:
   - Lighthouse audit (Performance, SEO, Accessibility, Best Practices)
   - DOM inspection: tech stack fingerprint (jQuery version, Bootstrap version, WP generator tag, GoDaddy signature, Wix signature, Weebly, etc.)
   - HTTP response headers (SSL cert details, security headers)
   - HTML structure (doctype, viewport meta, OG tags, schema.org, HTTPS consistency)
   - Footer text (copyright year regex)
   - Sitemap.xml lastmod dates
   - Page weight + network waterfall
   - Form inspection (file input present? `tel:` link present?)
3. Screenshot at **1440px desktop** and **390px mobile**.
4. Compute staleness score per `staleness-score.md` rubric (0-100).
5. Write `staleness-report.json` to `scans/{category}-{geo}-{date}/{slug}/staleness-report.json`.

**Tool used:** Chrome DevTools MCP. Fail gracefully if a site is unreachable (timeout → flag "site_dead", score = 100, but move to a separate "verify with owner" bucket).

### Stage 3 — Rank + present for triage

1. Sort candidates by staleness score descending.
2. Filter to score >= 66 (prime rebuild candidates).
3. Write `prospect-ranking.md` summarizing top N with:
   - Business name + URL + phone
   - Staleness score + top 3 stalest signals (e.g., "jQuery 1.8, no HTTPS, copyright 2017")
   - Lighthouse composite
   - Thumbnail of their current desktop screenshot
   - GBP rating + review count + map rank
4. Present to Jesse for approval. Jesse selects which ones to build.

### Stage 4 — Content extraction per approved prospect

For each approved prospect, extract reusable content from their old site:

1. **Photos** — scrape `<img>` tags from all pages, filter to business-content photos (not icons/logos/stock), save to `photos-from-old-site/`. Record original URLs + EXIF metadata.
2. **About/story copy** — scrape About page, team bios, founding year. Save as context, not verbatim output.
3. **Services list** — scrape Services pages, normalize.
4. **Testimonials** — if verbatim + attributed, capture. Skip if anonymous or paraphrased.
5. **Contact info** — phone, email, address (verify against Places).

Output: `existing-site-assets.json` + `photos-from-old-site/` directory.

**Tool used:** Chrome DevTools MCP + lightweight scraping. No Bruce needed at this stage — existing site IS the Layer 1 source.

### Stage 5 — Build brief generation

Produce the standard GTMDot intake-branch artifact set, but enriched by Stage 4 extraction:

1. `sites/{slug}/RESEARCH.md` — blended from Places + existing-site extraction
2. `sites/{slug}/reviews.json` — from Places reviews + any verbatim testimonials from old site
3. `sites/{slug}/photo-brief.json` — NEW FIELD: `"layer_0_own_site": {"status": "SATISFIED", "count": N}` indicating photos came from the prospect's current site. Bruce does NOT need to scrape; he only retrofits if Stage 4 yielded fewer than 6 usable photos.
4. `sites/{slug}/staleness-context.json` — NEW FILE: the staleness-report.json from Stage 2, plus a `rebuild_hook` field for outreach personalization:
   ```json
   {
     "staleness_score": 78,
     "lighthouse_composite": 42,
     "top_signals": ["jQuery 1.8", "no viewport meta (not mobile)", "copyright 2017", "no HTTPS"],
     "rebuild_hook": "Your current site runs on jQuery 1.8 (released 2012), isn't mobile-friendly, and Google gives it a 42/100 Core Web Vitals score — customers on phones are bouncing before they see your services."
   }
   ```
5. `sites/{slug}/source.json` — `{"source": "stale_website_prospect", "original_url": "..."}` — flag for A/B sequence routing at Resend.

### Stage 6 — Build + commit + finalize (same as existing flow)

Build `index.html` per the standard GTMDot pattern. Commit to `intake/{slug}`. Push. Write finalization message to `messages/`. From this point forward, identical to the no-website flow — Mini's deploy cron picks up, Slack #claude-sync pings, Jesse reviews on mobile, approves outbound per site. The only divergence is **outreach**:

- **Stale prospects** route to a stale-specific Resend sequence with rebuild-hook personalization.
- **No-website prospects** route to the existing sequence.

A/B measurement: open rate, reply rate, booked-call rate per sequence type. Track in Supabase.

## Staleness score

Full rubric in `staleness-score.md`. Quick reference:

| Category | Weight | Rationale |
|---|---|---|
| Tech stack age | 25% | Strongest signal of neglect |
| Lighthouse composite | 20% | Google's own stale-site verdict |
| Mobile responsiveness | 15% | Today's majority traffic |
| Visual design age | 15% | What the owner actually sees |
| Security posture | 10% | HTTPS, headers, exposed admin paths |
| Footer copyright year | 5% | Quick neglect tell |
| Form sophistication | 5% | UX for lead capture |
| Image quality | 5% | Assets we might reuse |

Thresholds:
- **0-40** skip
- **41-65** borderline, flag but don't auto-build
- **66-79** rebuild candidate
- **80-100** prime — rebuild first, outreach after with "here's your preview" in the first email

## Operational constraints

1. **Politeness rate-limiting**: 1 request per 2 seconds per target domain. Set User-Agent to `GTMDotScanner/1.0 (rebuild-prospecting; jesse@growthdelicio.us)`. Respect robots.txt even though we're reading, not writing.
2. **Budget**: each full scan costs ~2-4 minutes of Chrome DevTools time per URL. 40 candidates ≈ 2 hours. Batch overnight if doing a large category sweep.
3. **Dedup horizon**: skip any prospect already in `intake/{slug}` branches, `rebuild-queue.json`, or CRM with any status. Don't re-prospect.
4. **Abort signals**: if staleness scan returns < 5 candidates with score ≥ 66 from a 40-candidate batch, stop and surface to Jesse — category or geo may be saturated. Don't consume more Places API quota.
5. **Manual-managed detection**: if a site looks stale on tech but has recent blog posts / recent copyright year / active social widgets, flag as "engaged but stale" — separate outreach angle, different template.

## Output artifacts

A full run produces:

```
scans/{category}-{geo}-{YYYY-MM-DD}/
├── candidate-list.json                # Stage 1 output
├── prospect-ranking.md                # Stage 3 summary for Jesse review
├── {slug}/
│   ├── staleness-report.json         # Stage 2 per-URL
│   ├── screenshot-desktop.png
│   ├── screenshot-mobile.png
│   ├── existing-site-assets.json     # Stage 4 extraction inventory
│   └── photos-from-old-site/
│       ├── img-001.jpg
│       └── ...
└── run-log.md                         # audit trail
```

Approved prospects then produce the standard intake-branch artifacts (Stages 5-6) under `sites/{slug}/`.

## Sub-skills this orchestrates

- `places-prospector` (Stage 1) — Places API + filter + dedup
- `staleness-scanner` (Stage 2) — Chrome DevTools + Lighthouse + scoring
- `content-extractor` (Stage 4) — photo + copy scrape from existing site
- `rebuild-briefer` (Stage 5) — assembles the intake-branch artifacts

Each sub-skill is independently invokable (e.g., "scan the staleness of example.com" hits just the Stage 2 skill). But the full pipeline runs when the top-level skill fires.

## Phase 2 extensions (not for MVP)

1. **Monthly re-scan**: re-check stale scores for active prospects in CRM. Surface "got better" (they rebuilt) vs "got worse" (still neglected).
2. **Competitor snapshot**: for each prospect, snapshot the top-3 competitors on GBP page 1 for the same category-geo. Lets outreach say "Your competitors X, Y, Z are ranking above you with modern sites."
3. **Domain age check**: older domain age + stale site = higher rebuild value (established business but neglected web presence).
4. **SSL expiry alerts**: flag prospects whose SSL expires in < 30 days — timely outreach hook.
5. **Pricing guess**: rough rebuild-value estimate based on business size (review count, service radius) + current site weakness.

## Success metric

Phase 1 success = ≥30% reply rate on stale-prospect outreach vs no-website prospect baseline. Measure across 20 stale prospects per category (100 total). If hit, promote to primary prospecting channel. If miss, analyze: was the staleness score predictive? Was the outreach angle wrong? Did the preview URLs convert?

## Notes for implementer

- The Chrome DevTools MCP for Lighthouse + DOM inspection is the main technical lift. If the MCP doesn't expose Lighthouse directly, we can invoke `lighthouse` CLI via shell as a fallback.
- Page weight + network waterfall is nice-to-have; skip if the MCP doesn't make it easy.
- Tech stack fingerprinting can use Wappalyzer's open detection rules or a small inline JS-regex set. Don't over-engineer.
- Screenshots should be PNGs at 1440x900 and 390x844 (iPhone 14 Pro).
- Keep staleness-score math in one pure function so the rubric can evolve without refactoring the scanner.

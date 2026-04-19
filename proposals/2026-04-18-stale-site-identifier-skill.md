---
from: jesse + r1vs (recovered from a dead forked session)
to: next session — "Site Identifier" (new Claude Code session dedicated to building this skill)
date: 2026-04-18
type: skill design proposal (ready to build)
topic: Stale-Site Identifier — a new prospect-finder skill for GTMDot
status: design approved, implementation pending
recovery-note: This proposal was reconstructed from a Claude Code session that hit the 2000px image dimension error and could not be saved. The session reached design consensus and was about to write the skill files. Nothing was written to disk. This doc preserves the design so a fresh session can implement it.
---

# Stale-Site Identifier — Skill Proposal

## Concept

GTMDot currently targets two prospect cohorts:
- **Group A**: businesses with no website
- **Group B**: businesses with a bad/outdated website (per the SKILL.md targeting criteria)

Add a third cohort: **Group C — Stale Website**. Businesses whose websites exist but haven't been meaningfully updated in 5+ years. These sites often have:

- Recoverable photos (team, vans, job shots)
- A written owner story / about page
- A real services list
- Owner-awareness that the site is out of date ("yeah I keep meaning to update it")

Which means Group C has **better close dynamics** than Group A:

| Factor | Group A (no site) | Group C (stale site) |
|---|---|---|
| Photos available | ❌ need Bruce waterfall | ✅ scrape existing |
| Owner story | ❌ GBP only | ✅ about page usually |
| Services list | ⚠️ GBP categories only | ✅ usually detailed |
| Owner awareness of need | Low | High |
| Outreach hook | Generic | Specific ("your site scores 38/100") |
| Build time | 2-4 hrs | 1-2 hrs |

## The 6 design decisions (approved)

1. **Seed source: start at page 3+ of Google business listings.** If a business ranks on pages 1-2 for their category in their geo, they're doing fine — skip them. Page 3 and deeper is where stale-site prospects live.

2. **A/B test via Resend email sequences.** Group A gets one sequence, Group C gets a stale-site-specific sequence that references their current site's Core Web Vitals / Lighthouse score. Same claim bar for both cohorts — we're not splitting the on-site experience.

3. **Rebuild BEFORE outreach.** Same pattern as the existing pipeline — preview URL in the first email is the high-conversion play. Applies to all Group C prospects that score high enough to justify the build time.

4. **Implement as a skill, not a standalone tool.** The interface should be: *"I need 10 new HVAC site prospects"* → skill runs the whole flow and produces intake branches ready for the existing build pipeline.

5. **Reuse the existing GTMDot build process.** Don't fork the build pipeline. Group C just feeds the same downstream workflow (R1VS Phase 1-3 → Bruce enrichment → Mini deploy) — the skill's job ends at producing intake branches with richer starting context.

6. **MVP scope: single-category, single-geo test.** Run it on HVAC in Atlanta metro. If the top 10 ranked prospects look like real opportunities, formalize and expand.

## The staleness score (rubric — verbatim from the approved design)

Weighted 0-100. Higher = staler = better prospect.

| Category | Weight | What it measures |
|---|---|---|
| Tech stack age | 25% | jQuery <3, Bootstrap <4, WP gen <5.0, no viewport, HTML4, Flash leftovers — each adds points |
| Lighthouse composite | 20% | `100 − average(Performance, SEO, Accessibility, Best Practices)` |
| Mobile responsiveness | 15% | Screenshot at 390px — layout breaks, horizontal scroll, readable text |
| Visual design age | 15% | Harder to fully automate; signals: stock photography, Comic Sans/Times, garish saturation, page weight > 5MB |
| Security posture | 10% | Plain HTTP, mixed content, expired/self-signed SSL, visible admin paths |
| Footer copyright year | 5% | Current = 0 pts, 2024 = 3, 2023 = 5, 2022 = 7, ≤2020 = full weight |
| Form sophistication | 5% | No form = 5, form without file upload = 3, form with file upload = 0 |
| Image quality | 5% | Avg image <800px wide, no alt text, no lazy loading, EXIF dates >3yr |

**Thresholds:**

- **0–40**: modern, skip
- **41–65**: borderline (email-only outreach, no pre-build)
- **66–79**: rebuild candidate (goes through pipeline)
- **80–100**: prime prospect (priority build)

## Signals by source

### Chrome DevTools MCP can surface directly
- **Performance & SEO** (Lighthouse): Performance <50, SEO <70, A11y <60, LCP >4s, CLS >0.25, missing meta description / canonical / OG
- **Tech stack age** (DOM + headers): jQuery 1.x/2.x, Bootstrap 2.x/3.x, Flash/`<applet>`/Silverlight, `X-UA-Compatible` IE flags, WP generator meta with old version, GoDaddy Website Builder signature (`.godaddysites.com` CNAME or template patterns), Wix 2010-era templates, Weebly/Jimdo/SiteBuilder, HTML4 doctype, no `<meta viewport>`, HTTP scheme, mixed content, self-signed/expired SSL
- **Content staleness**: footer ©2018/2019/2020, blog posts >3yr old or absent, dead Twitter/Facebook embeds, testimonials >5yr
- **UX red flags**: form without file input, phone not as `tel:` link, no online booking, no click-to-call mobile, `mailto:`-only, no chatbot, desktop-only nav breaking on mobile

### Places API filters (pre-scan)
- Has a `website` field at all (required)
- Rating ≥ 4.0
- Review count ≥ 10
- Categories match target trades
- Has GBP photos (owner engages with GBP even if not web)

### Light scrape (additional signal)
- `Last-Modified` header on key pages
- `sitemap.xml` `<lastmod>` dates
- Image EXIF dates (often preserved for years)
- `robots.txt` existence + content
- Schema.org structured data presence/absence
- Favicon quality

## 8-stage workflow

```
1. SEED: category + geo
   Example input: "HVAC contractors, Atlanta metro, 30-mile radius"

2. PLACES API: pull 200–500 businesses
   Filter: website present + rating ≥4.0 + reviews ≥10
   Additional filter: results from page 3+ of ranking (skip first 2 pages)

3. STALE-SCAN LOOP (Chrome DevTools MCP)
   For each URL:
     a. Navigate, wait for load
     b. Run Lighthouse
     c. Query DOM for tech stack signals
     d. Check SSL + HTTP vs HTTPS
     e. Screenshot desktop + 390px mobile
     f. Scrape copyright year, last-mod, images
     g. Compute staleness score
     h. Save staleness-report.json per prospect

4. RANK: sorted list of top 50 by score
   Output: CSV or Supabase table
   Fields: name, url, score, category, top 3 signals

5. TRIAGE: Jesse reviews top 50
   Approves ~20 for rebuild

6. AUTO-EXTRACT existing content (new sub-skill)
   - Scrape photos → sites/<slug>/photos-from-old-site/
   - Scrape about page → RESEARCH.md
   - Scrape services list
   - Scrape testimonials (if verbatim + attributed)

7. BUILD via existing GTMDot pipeline
   R1VS Phase 1-3 with richer starting brief

8. OUTREACH: stale-specific Resend sequence
   "Your current site scores 38/100 on Google's Core Web Vitals
    and is not mobile-friendly. Here's a modern version I built
    for free — preview at <slug>.pages.dev."
```

## Proposed file structure (skill package)

```
skills/stale-site-identifier/
├── SKILL.md                 # orchestrator — the main entry point
├── staleness-score.md       # the weighted rubric spec (pure scoring function)
├── SAMPLE-RUN.md            # worked example of "find 10 HVAC prospects" flow
├── rubrics/
│   └── (future: specialized rubrics per vertical if needed)
├── outreach-templates/
│   ├── score-80-plus.md     # "your site scores X, here's a rebuild"
│   ├── score-66-79.md       # "I noticed your site, interested in preview?"
│   └── engaged-but-stale.md # "your content is fresh but the design is holding you back"
└── reports/
    └── <category>-<geo>-<date>/
        ├── candidates.csv
        ├── top-50.json
        └── approved-for-build.json
```

Exact structure can be negotiated during build — the above is a starting sketch.

## MVP deliverables (this first session)

Build three files, no execution:

1. **`skills/stale-site-identifier/SKILL.md`** — the orchestrator. Defines the interface (`"Find N [category] prospects in [geo]"`), the 8-stage flow, dependencies on Chrome DevTools MCP + Places API + Firecrawl, handoff to existing GTMDot pipeline.

2. **`skills/stale-site-identifier/staleness-score.md`** — pure scoring function spec. All 8 categories with their weights, per-signal point values, threshold definitions. Deterministic enough that two different implementers would produce the same score for the same site.

3. **`skills/stale-site-identifier/SAMPLE-RUN.md`** — worked example of the MVP flow ("find 10 HVAC prospects in Atlanta"). Show mock output at each of the 8 stages so Jesse can see the shape before any tools are wired. Include: mock Places candidate list, one full staleness-report.json, top-10 ranking summary, mock intake-branch artifact set.

**Do not execute the scanner.** This session is documentation of the skill, not execution. The first real scan run happens after Jesse reviews the three files and approves.

## Open questions left for the builder

1. **Actively-managed-despite-looking-old detection.** Some old sites have diligent owners who keep content fresh but never rebuilt the 2012 design. Signal: recent blog posts / current copyright year despite stale tech stack. Worth flagging separately — different outreach angle ("your content is current but the design is working against you").

2. **Do we show the staleness score to the prospect in outreach?** Numbers hit harder but can also feel insulting. Jesse wants to A/B test this — two variants of the high-score email sequence, one with the number, one without.

3. **Scope of the auto-extract step.** Photos = yes. Verbatim copy = risky (plagiarism-back risk, inherit typos). Default: scrape into RESEARCH.md as *context*, let R1VS rewrite fresh.

4. **Category prioritization for the MVP test.** Best-guess hit rate for stale sites, high to low:
   - Pool maintenance (tons of 2010-era WordPress)
   - HVAC (many on GoDaddy builders)
   - Plumbing (similar to HVAC)
   - Electrical (mid-market, often more modern — lower hit rate)
   - General renovation / handyman (all over the map)

5. **How exactly to detect "page 3+" in Places API.** The API doesn't have a direct "rank" field — it returns results in prominence order. Need to confirm: does pulling results 41–200 (skipping first 40) approximate "page 3+"? Or is there a better proxy signal? Flag for investigation during build.

## Dependencies on existing GTMDot assets

- **`SKILL.md`** (root) — the existing build pipeline this skill feeds into
- **`CLAUDE.md`** — division of labor (R1VS / Bruce / Mini / Jesse) still applies
- **`ICON-MAPPING.md`** — still applies downstream
- **`R1VS-REBUILD-BRIEF.md`** — intake API payload spec still applies; Group C prospects post to the same endpoint
- **`rebuild-queue.json`** — may need a new `prospect_cohort` field (values: `no_site`, `stale_site`) to distinguish A/B cohorts for Resend

## Success criteria for the first real scan run

After the three MVP files are built + approved, the first actual run should produce:

- 10 HVAC prospects in Atlanta metro, ranked by staleness score
- Each with a `staleness-report.json` artifact
- Top 3 hand-reviewed by Jesse to gut-check score accuracy
- If 2+ of the top 3 are real rebuild candidates, skill is validated
- If not, adjust rubric weights and re-run

---

*This proposal is self-contained — drop it into a fresh Claude Code session and it should have enough context to implement the skill without any prior conversation.*

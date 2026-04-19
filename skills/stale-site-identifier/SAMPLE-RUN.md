# Sample Run — HVAC / Atlanta Metro / N=10

**Purpose:** A worked example of the 8-stage flow with mock data at each stage. Use this to sanity-check the skill's shape before the first real scan is executed. Nothing in this file comes from a real scan — all businesses, URLs, numbers, and signals are fabricated for illustration.

**Scenario:** Jesse says *"Find 10 HVAC prospects in Atlanta metro."* The skill runs. This document shows what each stage produces.

---

## Stage 1 — Seed

**Input (user):** "Find 10 HVAC prospects in Atlanta metro."

**Parsed params:**
```json
{
  "category": "hvac",
  "places_types": ["hvac_contractor", "heating_contractor", "air_conditioning_contractor"],
  "geo": {
    "center": "Atlanta, GA",
    "center_lat": 33.7490,
    "center_lng": -84.3880,
    "radius_miles": 30
  },
  "n": 10,
  "rubric_version": "0.1.0-mvp",
  "scan_started_at": "2026-04-18T14:05:00Z"
}
```

**File written:** `prospects/hvac-atlanta-2026-04-18/scan-manifest.json` (seeded, populated further as stages complete).

---

## Stage 2 — Places API candidate pull

Pulled 312 businesses matching type + radius. Filters applied:

| Filter | Dropped |
|---|---|
| Has `website` field | 58 dropped (GBP-only — these are Group A leads, not ours) |
| `rating >= 4.0` | 24 dropped |
| `user_ratings_total >= 10` | 41 dropped |
| At least 1 GBP photo | 12 dropped |
| **Survived filters** | **177** |

**Page 3+ heuristic (v1):** Of the 177 survivors, skip top 40 by prominence rank → **137 passed to Stage 3**.

**First-run validation:** SERP scrape of `"HVAC Atlanta GA"`, `"AC repair Sandy Springs"`, `"heating service Roswell"` via Firecrawl. Top-20 organic results cross-checked against the skipped-40 set:
- `"HVAC Atlanta GA"` — 6 of top 10 organic appear in skipped-40 (expected)
- `"AC repair Sandy Springs"` — 4 of top 10 appear in skipped-40
- `"heating service Roswell"` — 7 of top 10 appear in skipped-40

Skip-40 heuristic looks valid; noted in scan-manifest for calibration records.

**`candidates.csv`** (abbreviated — first 5 rows for illustration):

```csv
name,place_id,url,lat,lng,rating,review_count,types,has_photos,prominence_rank
"Delta Air HVAC",ChIJaaaa...,"https://deltaairhvac.com",33.7821,-84.3912,4.8,187,"hvac_contractor",true,1
"Atlanta Comfort Systems",ChIJbbbb...,"https://atlcomfortsystems.com",33.7654,-84.3754,4.7,203,"hvac_contractor",true,2
...
"Bob's Heating & Air",ChIJqqqq...,"https://bobsheatingatl.com",33.9512,-84.5190,4.9,62,"hvac_contractor",true,47
"Peach State Cooling Inc",ChIJrrrr...,"https://peachstatecooling.com",33.9001,-84.2760,4.6,31,"hvac_contractor",true,53
"Northlake HVAC Service",ChIJssss...,"https://northlakehvacservice.com",33.8512,-84.1124,4.8,44,"hvac_contractor",true,61
...
```

Rows 1–40 (prominence rank ≤ 40) are in `candidates.csv` for the record but excluded from scan. Rows 41–177 go to Stage 3.

---

## Stage 3 — Stale-scan loop (137 prospects)

Runs at 3 concurrent with ~2 min/prospect → ~91 minutes elapsed. Checkpointed per prospect.

**Mock result distribution:**

| Bucket | Count |
|---|---|
| `prime_prospect` (80–100) | 11 |
| `rebuild_candidate` (66–79) | 38 |
| `borderline` (41–65) | 52 |
| `modern` (0–40) | 34 |
| `error: scan_timeout` | 2 |
| **Total** | **137** |

### Full mock staleness-report.json — `bobs-heating-atl`

Representative example for a `prime_prospect` (87/100). This is what every approved prospect's report looks like.

```json
{
  "slug": "bobs-heating-atl",
  "business_name": "Bob's Heating & Air",
  "url": "https://bobsheatingatl.com",
  "place_id": "ChIJqqqqqqqqqq",
  "scored_at": "2026-04-18T14:51:27Z",
  "rubric_version": "0.1.0-mvp",
  "total_score": 87,
  "bucket": "prime_prospect",

  "categories": {
    "tech_stack_age": {
      "weight": 25,
      "raw": 25,
      "weighted": 25,
      "signals": [
        { "name": "jquery_v1", "points": 8, "detail": "jQuery 1.11.3 detected via window.jQuery.fn.jquery" },
        { "name": "bootstrap_v3", "points": 6, "detail": "bootstrap-3.3.7.min.css referenced in <head>" },
        { "name": "wordpress_generator_lt_5", "points": 6, "detail": "<meta name=generator content='WordPress 4.9.8'>" },
        { "name": "no_viewport_meta", "points": 5, "detail": "<meta name=viewport> absent" },
        { "name": "script_count_high", "points": 2, "detail": "21 script tags, no bundler signature" }
      ]
    },
    "lighthouse_composite": {
      "weight": 20,
      "raw": 18,
      "weighted": 18,
      "lighthouse": {
        "performance": 19,
        "seo": 48,
        "accessibility": 52,
        "best_practices": 58,
        "lcp_seconds": 6.2,
        "cls": 0.34
      },
      "signals": [
        { "name": "perf_lt_50", "detail": "Lighthouse Performance: 19/100" },
        { "name": "lcp_gt_4s", "detail": "Largest Contentful Paint: 6.2s" },
        { "name": "cls_high", "detail": "Cumulative Layout Shift: 0.34 (>0.25)" },
        { "name": "seo_lt_70", "detail": "SEO score: 48/100 (missing meta description, no canonical)" }
      ]
    },
    "mobile_responsive": {
      "weight": 15,
      "raw": 10,
      "weighted": 10,
      "signals": [
        { "name": "horizontal_scroll_390", "points": 5, "detail": "document.scrollWidth = 1024px at 390px viewport" },
        { "name": "no_tap_to_call", "points": 2, "detail": "Phone '(770) 555-0142' rendered as plain text, no tel: href" },
        { "name": "desktop_nav_visible_390", "points": 2, "detail": "Nav has 6 visible <a> children at 390px" },
        { "name": "small_body_font", "points": 1, "detail": "body p computed font-size: 13px at 390px" }
      ]
    },
    "visual_design_age": {
      "weight": 15,
      "raw": 9,
      "weighted": 9,
      "signals": [
        { "name": "stock_photo_share", "points": 3, "detail": "6 of 11 sampled <img> src contain istockphoto.com" },
        { "name": "tiled_background", "points": 2, "detail": "body background-repeat: repeat, uses /images/bg-pattern.gif" },
        { "name": "center_aligned_body", "points": 2, "detail": "5 paragraphs with text-align: center in body content" },
        { "name": "page_weight_5mb_plus", "points": 2, "detail": "6.8 MB transferred on homepage load" }
      ]
    },
    "security_posture": {
      "weight": 10,
      "raw": 8,
      "weighted": 8,
      "signals": [
        { "name": "plain_http", "points": 5, "detail": "Homepage served over http://, no https redirect" },
        { "name": "mixed_content", "points": 3, "detail": "3 assets loaded from http:// on https fallback test" }
      ]
    },
    "footer_copyright": {
      "weight": 5,
      "raw": 10,
      "weighted": 5,
      "signals": [
        { "name": "copyright_year", "detail": "Footer: '© 2018 Bob's Heating & Air'" }
      ]
    },
    "form_sophistication": {
      "weight": 5,
      "raw": 4,
      "weighted": 4,
      "signals": [
        { "name": "form_no_file_upload", "points": 4, "detail": "Contact form has name/email/message, no <input type=file>, mailto: action" }
      ]
    },
    "image_quality": {
      "weight": 5,
      "raw": 4,
      "weighted": 4,
      "signals": [
        { "name": "avg_width_low", "points": 2, "detail": "Average natural width of 11 sampled images: 612px" },
        { "name": "missing_alt_majority", "points": 1, "detail": "7 of 11 images have empty or missing alt" },
        { "name": "no_lazy_loading", "points": 1, "detail": "0 images with loading=lazy" }
      ]
    }
  },

  "flags": {
    "content_fresh_but_design_stale": false,
    "wordpress_spam_injection": false,
    "godaddy_site_builder": false,
    "flash_or_silverlight": false,
    "plain_http": true,
    "site_unreachable": false
  },

  "top_3_signals": [
    "jQuery 1.11.3 + Bootstrap 3 + WordPress 4.9.8 — stack is ~8 years stale (tech 25/25)",
    "Plain HTTP with mixed content — Chrome flags this site as 'Not Secure' (security 8/10)",
    "Footer ©2018; Lighthouse Performance 19/100; LCP 6.2s — nothing updated for years (copyright 5/5 + lh 18/20)"
  ],

  "places_metadata": {
    "rating": 4.9,
    "review_count": 62,
    "phone": "(770) 555-0142",
    "address": "1234 Main St, Roswell, GA 30075",
    "gbp_photo_count": 14
  }
}
```

**Files written for this prospect:**
```
prospects/hvac-atlanta-2026-04-18/bobs-heating-atl/
├── staleness-report.json      (above)
├── mobile-390.png             # 390×844 screenshot — horizontal scroll visible
├── desktop-1440.png           # hero + nav + above-fold
└── sitemap-raw.json           # Firecrawl map result, 23 URLs, no spam patterns
```

Stages 6+ will add `RESEARCH.md`, `photos-from-old-site/`, and populate `sitemap-raw.json` if approved for build.

---

## Stage 4 — Rank

### `top-N-summary.md` (the file Jesse opens)

```markdown
# Stale-Site Scan: HVAC — Atlanta metro 30mi — 2026-04-18

Scanned: 137 businesses (filtered from 312 Places API pulls, skipped top-40 by prominence).
Rubric version: 0.1.0-mvp.
Scan duration: 91 minutes.

## Bucket distribution

| Bucket | Count | % |
|---|---|---|
| prime_prospect (80–100) | 11 | 8% |
| rebuild_candidate (66–79) | 38 | 28% |
| borderline (41–65) | 52 | 38% |
| modern (0–40) | 34 | 25% |
| scan_timeout | 2 | 1% |

## Top 10 by staleness score

| # | Business | URL | Score | Bucket | Top signals |
|---|---|---|---|---|---|
| 1 | Peach State Cooling Inc | peachstatecooling.com | 91 | prime | jQuery 1.8 + WP 4.5 + Flash embed; Lighthouse Perf 12; © 2017 |
| 2 | Northlake HVAC Service | northlakehvacservice.com | 89 | prime | GoDaddy SiteBuilder; no viewport meta; © 2019; mixed content |
| 3 | Bob's Heating & Air | bobsheatingatl.com | 87 | prime | jQuery 1.11 + Bootstrap 3 + WP 4.9; plain HTTP; © 2018 |
| 4 | Cobb County Climate Control | cobbclimate.net | 84 | prime | Wix pre-Editor-X template; Perf 24; no mobile breakpoint |
| 5 | Marietta Mechanical | mariettamech.biz | 83 | prime | WordPress 4.2 + WP spam injection (!); Perf 19 |
| 6 | Stone Mountain Heating | stonemtnheating.com | 81 | prime | jQuery 1.9 + IE=edge meta; © 2020; mailto-only form |
| 7 | Gwinnett Comfort Pros | gwinnettcomfortpros.com | 78 | rebuild | Bootstrap 3; Perf 34; © 2021; horizontal scroll at 390px |
| 8 | Sandy Springs Air | sandyspringsair.com | 76 | rebuild | content_fresh_but_design_stale ⚑ — © 2026 but jQuery 1.11 + tiled bg |
| 9 | Johns Creek Heating & Cooling | jchccooling.com | 74 | rebuild | WP 5.2; Perf 41; tiled bg; center-aligned copy |
| 10 | Roswell AC Pros | roswellacpros.net | 72 | rebuild | GoDaddy SiteBuilder; Perf 37; © 2022 |

## Flags worth knowing

- **1 site has `wordpress_spam_injection`** (#5 Marietta Mechanical) — lead outreach with the hacked-SEO angle
- **3 sites are `plain_http`** (#3, #6, and one outside top 10) — "your site is flagged insecure in Chrome" hook
- **1 site is `content_fresh_but_design_stale`** (#8 Sandy Springs Air) — different angle: "your content is current, your design isn't"
- **2 sites have `godaddy_site_builder`** (#2, #10) — GoDaddy-migration pitch

## Next 10 (rebuild_candidate bucket, 66–72 range)

Surfaced for reference in case Jesse wants to expand past N=10 for this run:

| # | Business | URL | Score |
|---|---|---|---|
| 11 | Alpharetta Heating | alpharettaheating.com | 71 |
| 12 | Dunwoody HVAC Experts | dunwoodyhvacexperts.com | 70 |
| ... | | | |
```

**`ranked.json`** (not shown — contains all 137 with full report refs).

---

## Stage 5 — Jesse triage

**Mock Jesse response:**
> "Approve 1, 2, 3, 4, 5, 6, 8, 10. Skip 7 — I know that owner, he's not a good fit. Skip 9 — that's actually my brother-in-law's cousin's company."

**Approved slugs (8 of top 10):**
```
peach-state-cooling
northlake-hvac-service
bobs-heating-atl
cobb-county-climate-control
marietta-mechanical
stone-mountain-heating
sandy-springs-air
roswell-ac-pros
```

Short of the N=10 target by 2. Options:
- Bump up to #11 and #12 from the next-10 list → gets us to 10
- Or ship with 8 this round and fill from next scan

Mock decision: bump 11 and 12, proceed with 10 approved prospects.

---

## Stage 6 — Auto-extract (approved prospects only)

Runs on all 10 approved prospects. Per prospect:

### Example: `bobs-heating-atl/`

After extraction, the directory contains:

```
prospects/hvac-atlanta-2026-04-18/bobs-heating-atl/
├── staleness-report.json      (from stage 3)
├── mobile-390.png             (from stage 3)
├── desktop-1440.png           (from stage 3)
├── sitemap-raw.json           (from stage 3, now consulted)
├── RESEARCH.md                (new — context for R1VS)
└── photos-from-old-site/
    ├── INDEX.md               (new — per-photo context)
    ├── old-photo-01-a3f2.jpg  (team shot, from /about)
    ├── old-photo-02-b7e9.jpg  (van photo, from homepage hero)
    ├── old-photo-03-c1d4.jpg  (technician on roof, from /services)
    ├── old-photo-04-d8f1.jpg  (completed install, from /gallery)
    ├── old-photo-05-e2a7.jpg  (truck + logo, from /contact)
    └── old-photo-06-f9b3.jpg  (owner at trade show, from /about)
```

### Mock `RESEARCH.md`

```markdown
# Research Package — Bob's Heating & Air

**Source:** Scraped 2026-04-18 from bobsheatingatl.com as part of stale-site scan.
**Cohort:** stale_site
**Score:** 87/100 (prime_prospect)
**Rubric version:** 0.1.0-mvp

---

## Scraped About (context — rewrite fresh)

Bob's Heating & Air has been serving the North Atlanta area since 1987. Founded by Bob Whitman, a former factory technician for Trane, the company has grown from a one-truck operation to a family-run business with 8 technicians. Bob's son Michael joined the company in 2009 and now manages operations.

**R1VS note:** Use the facts (1987 founding, Bob Whitman founder, Michael his son, Trane training, 8 techs) but rewrite the prose. The existing copy is serviceable but the rebuild should match the Polish Pass editorial tone.

## Scraped Services List (use for coverage, rewrite copy)

- AC Installation
- AC Repair
- Heating Installation
- Furnace Repair
- Heat Pump Service
- Air Quality Testing
- Duct Cleaning
- Emergency 24/7 Service

## Scraped FAQ (use if exists — treat as facts, not copy)

**Q: Do you service outside Fulton County?**
A: Yes — we cover Fulton, Cobb, Forsyth, Cherokee, and parts of Gwinnett County.

**Q: Do you offer financing?**
A: Yes, we partner with Synchrony for financing on installations over $2,500.

**Q: What brands do you service?**
A: We service all major residential HVAC brands including Trane, Carrier, Lennox, Rheem, Goodman, and York.

**Q: Do you charge a diagnostic fee?**
A: Standard diagnostic fee is $89. It's waived if you approve the repair.

## Pricing Found On Old Site

- Diagnostic fee: $89 (waived with approved repair)
- Emergency after-hours service call: $149
- Duct cleaning: starts at $399

## Credentials Found

- NATE-certified technicians
- EPA 608 certified
- Licensed Georgia HVAC Class I contractor (license # CN208547)
- BBB accredited, A+ rating
- Member: Air Conditioning Contractors of America

## Owner/Team Names Mentioned

- Bob Whitman (founder)
- Michael Whitman (operations manager)
- Reviews mention: Curtis, Jamal, Derek (technicians — candidates for team card feature)

## Testimonials (flag for Bruce Phase 1b cross-reference)

Testimonials visible on old site homepage. Candidates:
- "Mackenzie W. — Roswell" — "Curtis was professional and honest. Told us we didn't need a new unit when two other companies tried to sell us one. Saved us $6,000."
- "Tom P. — Alpharetta" — "Same-day service on a Saturday. Jamal got the AC back running in under 2 hours."

**Bruce note:** These are visible on the old site. Cross-reference against Places API reviews during Phase 1b — if these reviewers appear in API, use API version (authoritative). If not in API, flag — may be old testimonials that have been scrubbed from Google.

## Nav/Page Inventory (from sitemap)

- / (homepage)
- /about
- /services
- /services/ac-repair
- /services/heating
- /services/duct-cleaning
- /gallery
- /contact
- /faq

**R1VS note:** Build full per-service pages for AC Repair, Heating, Duct Cleaning (they already have them — we need to match coverage or we lose SEO ranking they currently have).
```

### Mock `photos-from-old-site/INDEX.md`

```markdown
# Photos from old site — Bob's Heating & Air

Downloaded 2026-04-18 from bobsheatingatl.com. Stock photo URLs skipped (6 of 17 images on the site matched stock patterns). Below are the 6 that appear to be owner-shot or owner-uploaded.

| File | Source page | Alt text (if present) | Notes |
|---|---|---|---|
| old-photo-01-a3f2.jpg | /about | "Bob and the team" | Team of 6 in uniforms, outside shop. Dated ~2018 by EXIF. Use candidate for team section. |
| old-photo-02-b7e9.jpg | / (homepage hero) | — | Company van photo. Branded "Bob's Heating & Air" on side. Use candidate for van/fleet callout. |
| old-photo-03-c1d4.jpg | /services | "Technician installing condenser" | Technician on roof with unit. No brand logos visible. Strong candidate for services hero. |
| old-photo-04-d8f1.jpg | /gallery | — | Completed install, mini-split. High quality. Strong candidate. |
| old-photo-05-e2a7.jpg | /contact | — | Truck + logo close-up. Watermark-free. |
| old-photo-06-f9b3.jpg | /about | "Bob at the 2019 Atlanta HVAC expo" | Owner photo, authentic, dated. Use for about section. |

**R1VS/Bruce note:** These are a *starting pool*, not a replacement for Bruce's Phase 2b waterfall. Bruce should still pull GBP photos + apply the vertical filter. But with these available, Recraft generation may not be needed — the owner has real van/team/job shots.
```

---

## Stage 7 — Hand off to R1VS

**File written:** `messages/2026-04-18-1655-stale-scan-to-r1vs-hvac-atlanta.md`

```markdown
---
from: stale-site-identifier skill
to: r1vs
date: 2026-04-18 16:55
type: handoff — Group C research packages ready
scan: prospects/hvac-atlanta-2026-04-18/
---

# Stale-site scan complete: HVAC / Atlanta metro / 2026-04-18

## Summary

- Scanned: 137 businesses
- Bucket distribution: 11 prime / 38 rebuild / 52 borderline / 34 modern / 2 timeout
- Top 10 approved by Jesse: 8 plus 2 backfills from rank 11–12
- Rubric version: 0.1.0-mvp

## Approved prospects (build these, cohort = stale_site)

| Slug | Business | Score | Bucket | Research path |
|---|---|---|---|---|
| peach-state-cooling | Peach State Cooling Inc | 91 | prime | prospects/hvac-atlanta-2026-04-18/peach-state-cooling/ |
| northlake-hvac-service | Northlake HVAC Service | 89 | prime | prospects/hvac-atlanta-2026-04-18/northlake-hvac-service/ |
| bobs-heating-atl | Bob's Heating & Air | 87 | prime | prospects/hvac-atlanta-2026-04-18/bobs-heating-atl/ |
| cobb-county-climate-control | Cobb County Climate Control | 84 | prime | prospects/hvac-atlanta-2026-04-18/cobb-county-climate-control/ |
| marietta-mechanical | Marietta Mechanical | 83 | prime | prospects/hvac-atlanta-2026-04-18/marietta-mechanical/ |
| stone-mountain-heating | Stone Mountain Heating | 81 | prime | prospects/hvac-atlanta-2026-04-18/stone-mountain-heating/ |
| sandy-springs-air | Sandy Springs Air | 76 | rebuild | prospects/hvac-atlanta-2026-04-18/sandy-springs-air/ |
| roswell-ac-pros | Roswell AC Pros | 72 | rebuild | prospects/hvac-atlanta-2026-04-18/roswell-ac-pros/ |
| alpharetta-heating | Alpharetta Heating | 71 | rebuild | prospects/hvac-atlanta-2026-04-18/alpharetta-heating/ |
| dunwoody-hvac-experts | Dunwoody HVAC Experts | 70 | rebuild | prospects/hvac-atlanta-2026-04-18/dunwoody-hvac-experts/ |

## For the intake API

Every prospect above gets this field in the /api/site-intake payload:

```json
"prospect_cohort": "stale_site"
```

**Flag to Mac Mini:** This is a new field. Confirm the API accepts it and the CRM surfaces it before R1VS pushes intake branches. If not yet implemented, R1VS should still write the field into the branch — Mac Mini absorbs it when ready.

## Research package contents per prospect

Each slug directory contains:
- `staleness-report.json` — use the `top_3_signals` for outreach copy, use `places_metadata` for the intake payload
- `RESEARCH.md` — context only, rewrite fresh
- `photos-from-old-site/` — starting pool for hero/about/team photos; Bruce still runs waterfall as usual
- `mobile-390.png` + `desktop-1440.png` — for visual reference of what we're replacing
- `sitemap-raw.json` — nav/page inventory; match their existing coverage

## Special flags to propagate

- marietta-mechanical has `wordpress_spam_injection: true` — lead outreach with the hacked-SEO angle. This is unusually strong.
- sandy-springs-air has `content_fresh_but_design_stale: true` — they're engaged; use the "your content is current but design is holding you back" angle.
- bobs-heating-atl, stone-mountain-heating, and roswell-ac-pros are on plain HTTP — "flagged insecure in Chrome" angle works.
- northlake-hvac-service and roswell-ac-pros are on GoDaddy SiteBuilder — specific migration pitch applies.

## Calibration notes

Rubric felt well-calibrated for HVAC:
- Top 3 are all genuinely stale (Jesse would approve all at a glance)
- No score >90 that felt like a false positive
- The borderline bucket (41–65) contains several sites that technically work but wouldn't survive another 2 years — might be worth email-only outreach

**Suggested rubric tweak for next run (pool service):** none yet. Keep version 0.1.0-mvp.

## R1VS, over to you

For each approved slug:
1. Read the research package
2. Run Phase 2 (design — brand extraction, palette, content planning) per root SKILL.md
3. Run Phase 3 (build — multi-page, inline CSS, Polish Pass rules)
4. Create intake branch `intake/<slug>`, include `prospect_cohort: "stale_site"`
5. POST to /api/site-intake
6. Write your standard `-r1vs-<slug>-finalized.md` message

Bruce picks up from the finalization message as usual.
```

---

## Stage 8 — Outreach (out of MVP scope)

Skipped per proposal. Documented here only to close the loop: once R1VS + Bruce + Mac Mini have the 10 sites live, a Resend sequence dedicated to `prospect_cohort = "stale_site"` fires. Exact copy + whether to show the numeric score is the first A/B test once live sites exist.

---

## What this sample run tells us

1. **The output shape is tractable** — a ranked summary + per-prospect package gives Jesse triage leverage without drowning him in JSON.
2. **Top-N summary is the key UX** — if this table reads clearly, the skill is usable. If not, iterate on `top-N-summary.md` format.
3. **Research package is rich enough for R1VS** — pre-scraped photos + credentials + team names + services coverage means Group C builds should run faster than Group B.
4. **One message handoff** — R1VS gets everything in a single file, no digging required.
5. **prospect_cohort is the new concept** — this is the main upstream dependency. Until Mac Mini accepts the field, Group C sites work but don't get A/B-split outreach.

---

## What the first REAL run needs before it can start

Confirming from the SKILL.md's MVP scope section:

- [ ] Jesse reviews + approves this file, `SKILL.md`, and `staleness-score.md`
- [ ] Mac Mini adds `prospect_cohort` to the intake API + CRM schema
- [ ] Single-site dry run to validate Chrome DevTools MCP + Lighthouse + Firecrawl flow end-to-end (pick one known stale HVAC site — not from the real run list — and execute stages 1–3 only as a smoke test)
- [ ] Page 3+ heuristic validation plan queued (SERP cross-check on first real run)

Once those are clear, first real run executes exactly the flow above: HVAC / Atlanta 30mi / N=10.

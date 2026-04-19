# Staleness Score — Scoring Rubric Spec

**Purpose:** Deterministic 0-100 score for a business website. Higher = staler = better rebuild prospect.

**Scope:** Pure function spec. Two implementers scanning the same live site on the same day should produce the same score within ±3 points. All inputs come from Chrome DevTools MCP, a light HTTP scrape, and Google Places API. No LLM judgment in the math.

**Output shape (per prospect):**
```json
{
  "url": "https://example.com",
  "scored_at": "2026-04-18T14:32:00Z",
  "total_score": 74,
  "bucket": "rebuild_candidate",
  "categories": {
    "tech_stack_age":       { "weight": 25, "raw": 22, "weighted": 22, "signals": [...] },
    "lighthouse_composite": { "weight": 20, "raw": 18, "weighted": 18, "signals": [...] },
    "mobile_responsive":    { "weight": 15, "raw": 12, "weighted": 12, "signals": [...] },
    "visual_design_age":    { "weight": 15, "raw": 9,  "weighted": 9,  "signals": [...] },
    "security_posture":     { "weight": 10, "raw": 6,  "weighted": 6,  "signals": [...] },
    "footer_copyright":     { "weight": 5,  "raw": 5,  "weighted": 5,  "signals": [...] },
    "form_sophistication":  { "weight": 5,  "raw": 1,  "weighted": 1,  "signals": [...] },
    "image_quality":        { "weight": 5,  "raw": 1,  "weighted": 1,  "signals": [...] }
  },
  "flags": {
    "content_fresh_but_design_stale": false,
    "wordpress_spam_injection": false,
    "godaddy_site_builder": false,
    "flash_or_silverlight": false,
    "plain_http": false
  },
  "top_3_signals": [
    "jQuery 1.11 detected (tech stack)",
    "Lighthouse Performance score 22/100",
    "Footer copyright ©2018 (5/5 pts)"
  ]
}
```

---

## Bucket thresholds

| Total | Bucket | Action |
|---|---|---|
| 0–40 | `modern` | Skip — they're doing fine |
| 41–65 | `borderline` | Email-only outreach, no pre-build |
| 66–79 | `rebuild_candidate` | Full pipeline, build preview site |
| 80–100 | `prime_prospect` | Priority build, front of queue |

The cutoff at 66 is deliberate — it means two full categories (e.g. tech + Lighthouse) have to be red before we spend R1VS time building. Don't lower it without running the numbers.

---

## Category 1 — Tech Stack Age (weight 25)

Measures visible evidence the site was built on technology that's 5+ years old and hasn't been updated. Highest weight because it's the most predictive single signal — old tech ≈ old everything else.

**Max raw: 25.** Cap at 25 even if multiple signals fire.

| Signal | Points | How to detect |
|---|---|---|
| jQuery v1.x present | 8 | `window.jQuery.fn.jquery` starts with `"1."` or `<script src>` contains `jquery-1.` |
| jQuery v2.x present | 5 | `window.jQuery.fn.jquery` starts with `"2."` or `<script src>` contains `jquery-2.` |
| Bootstrap v2.x or v3.x | 6 | `<link>` or `<script>` href contains `bootstrap-2.` / `bootstrap-3.` or `.navbar-inner` class present |
| WordPress generator meta < 5.0 | 6 | `<meta name="generator" content="WordPress X.Y">` where X < 5 |
| WordPress generator 5.0–5.5 | 3 | X.Y where 5.0 ≤ version < 5.6 |
| Flash / `<applet>` / `<object type="application/x-shockwave-flash">` | 10 | DOM query |
| Silverlight / ActiveX residue | 10 | `<object type="application/x-silverlight">` or `<object classid="clsid:`  |
| Missing `<meta name="viewport">` | 5 | DOM query `head meta[name="viewport"]` absent |
| HTML4 doctype (`<!DOCTYPE HTML PUBLIC...`) | 6 | `document.doctype.publicId` non-empty |
| `X-UA-Compatible` IE=edge/IE=8/IE=9 meta | 3 | Explicit IE support meta tag — signals a pre-2015 build |
| GoDaddy Website Builder signature | 4 | CNAME resolves to `*.godaddysites.com` OR inline style contains `gd-site-builder` class OR `<meta name="generator" content="GoDaddy">` |
| Wix 2010-era template (pre-Editor-X) | 3 | `<meta name="generator" content="Wix.com Website Builder">` **AND** `<html>` lacks `data-pm-lang` (newer Wix attribute) |
| Weebly / Jimdo / SiteBuilder watermark | 3 | Generator meta or `*.weebly.com` asset references |
| Script count > 15 with no bundler signature | 2 | `<script>` tags > 15 AND no `webpack`/`vite`/`parcel` in any src — proxy for "hand-assembled" 2010s site |

**Special flags (set to `true`, don't add to raw score — they drive separate downstream behavior):**
- `flags.flash_or_silverlight` — if Flash/Silverlight detected. Makes this a priority outreach ("your site won't load on modern browsers").
- `flags.godaddy_site_builder` — different rebuild angle ("migrating off GoDaddy SiteBuilder").

---

## Category 2 — Lighthouse Composite (weight 20)

Run Lighthouse via Chrome DevTools MCP on the homepage, mobile profile (Moto G4 / 4x CPU throttle / Slow 4G).

**Formula:** `raw = round((100 - avg(Performance, SEO, Accessibility, Best_Practices)) * 0.20)`

Then clamp to [0, 20].

**Example:**
- Performance 28, SEO 72, A11y 54, Best Practices 67
- avg = 55.25
- 100 - 55.25 = 44.75
- 44.75 × 0.20 = 8.95 → `raw = 9`, `weighted = 9`

**Signals recorded (for the top-3-signals list, not the math):**
- `lighthouse.performance < 50` → "Lighthouse Performance: {score}/100"
- `lighthouse.lcp_seconds > 4` → "Largest Contentful Paint: {lcp}s (>4s)"
- `lighthouse.cls > 0.25` → "Cumulative Layout Shift: {cls} (>0.25)"
- `lighthouse.seo < 70` → "SEO score: {score}/100 (missing meta/canonical/OG)"

**Timeout behavior:** If Lighthouse fails to complete within 90s, skip this category and mark `categories.lighthouse_composite.error = "timeout"`. The rest of the score still computes — don't drop the prospect. The absence of a Lighthouse score is itself mildly signal (slow site).

---

## Category 3 — Mobile Responsiveness (weight 15)

Take a screenshot at 390×844 (iPhone 14 Pro viewport) via Chrome DevTools MCP and run DOM checks.

| Signal | Points | How to detect |
|---|---|---|
| Horizontal scroll at 390px | 5 | `document.documentElement.scrollWidth > 390` |
| Touch target under 32px (any CTA button or nav link) | 3 | Measured bounding box on primary CTA / nav `<a>` |
| Font size under 14px on body text at 390px | 3 | Computed style on `<p>` or `<body>` descendants |
| No tap-to-call on phone number | 2 | Phone number text present but no `<a href="tel:...">` wrapping it |
| Desktop nav visible at 390px (no hamburger) | 2 | Nav `<ul>` has >3 visible children at 390px viewport |

**Max raw: 15.**

**Visual confirmation:** The 390px screenshot is also saved to `sites/<slug>/stale-scan/mobile-390.png` for Jesse's eyeball review. Automated scoring doesn't hand-judge the screenshot — it only uses DOM + computed styles.

---

## Category 4 — Visual Design Age (weight 15)

This is the hardest to automate. Signals are heuristic; accept some noise. Never a single-signal trigger.

| Signal | Points | How to detect |
|---|---|---|
| Page weight > 5 MB (transferred) | 4 | Chrome DevTools MCP network summary |
| >50% of `<img>` tags with obvious stock photography URLs | 3 | `<img src>` contains `shutterstock.com` / `istockphoto.com` / `gettyimages.com` / `depositphotos.com` / `123rf.com` — CDN-proxied counts if URL pattern matches |
| Comic Sans / Times New Roman / Arial as declared body font | 3 | Computed `font-family` on `<body>` |
| Garish saturation (average page saturation > 85%, sampled from hero region) | 2 | Canvas sample + HSL conversion on hero screenshot |
| Center-aligned body text blocks (>2 `text-align: center` paragraphs) | 2 | DOM query |
| `<marquee>` or `<blink>` element present | 3 | DOM query — rare but existing, and a free +3 when seen |
| Background image is a visible tile pattern (repeat-x / repeat-y) | 2 | Computed `background-repeat` on `<body>` or main wrapper |

**Max raw: 15.**

**Note on stock photo detection:** CDN-proxied images (e.g. stock delivered via Cloudinary) won't match URL patterns. That's OK — we accept the false-negative. Owner-uploaded / freshly-shot photos are the positive signal; stock is the negative. Visual review during Jesse triage catches the misses.

---

## Category 5 — Security Posture (weight 10)

| Signal | Points | How to detect |
|---|---|---|
| Plain HTTP (not HTTPS) homepage | 5 | `URL` scheme check after following redirects |
| Mixed content warnings | 3 | Chrome DevTools MCP console shows mixed-content errors on load |
| Expired or self-signed SSL | 5 | Cert chain check — `NotAfter` < today, or issuer in self-signed list |
| Visible `/wp-admin/` or `/administrator/` links in footer/nav | 2 | DOM query — they left admin links on a public page |

**Max raw: 10.**

**Flag:** `flags.plain_http = true` if scheme is HTTP. Sets priority for a "your site is flagged insecure in Chrome" outreach angle.

---

## Category 6 — Footer Copyright Year (weight 5)

Parse the footer for the most recent 4-digit year adjacent to `©`, `&copy;`, or the word "copyright" (case-insensitive).

| Year found | Points |
|---|---|
| Current year (2026) | 0 |
| 2025 | 1 |
| 2024 | 3 |
| 2023 | 5 |
| 2022 | 7 |
| 2021 | 8 |
| 2020 or earlier | 10 — cap (but weighted × 0.5, so contributes max 5) |
| No copyright found | 3 |

**Weighting:** raw is 0–10 from the table above. Weighted score = `round(raw × 0.5)`. Max contribution to total: 5.

**Example:** Footer shows "© 2022 Bob's HVAC". Raw 7, weighted 3.5 → 4.

---

## Category 7 — Form Sophistication (weight 5)

Find the primary contact or quote form on the homepage or `/contact`.

| Form state | Points |
|---|---|
| No form at all (phone-only or mailto:-only) | 5 |
| Form exists, no file upload, no validation, no honeypot | 4 |
| Form exists with basic validation but no file upload | 3 |
| Form exists with file upload field (`<input type="file">`) | 0 |
| Form routes to `mailto:` instead of server-side handler | 4 |

**Max raw: 5.** Weight already baked in (5% of total).

**Rationale:** Per Polish Pass Rule 5 in the main SKILL.md, photo/video upload on quote forms is a closing feature for service trades. Its absence is a real-money signal, not cosmetic.

---

## Category 8 — Image Quality (weight 5)

Sample up to 10 `<img>` tags excluding logos/icons (filter by size — exclude images < 100×100 natural dimensions).

| Signal | Points |
|---|---|
| Average natural width of sampled images < 800px | 2 |
| >50% of images missing `alt` attribute | 1 |
| Zero images have `loading="lazy"` | 1 |
| >50% of images are GIF or BMP format (not JPG/PNG/WebP) | 1 |
| EXIF DateTimeOriginal on scraped image > 3 years old (if extractable) | 1 |

**Max raw: 5.**

**EXIF note:** Many servers strip EXIF. Only score the signal if we could successfully read EXIF on at least one image. If all strip it, this signal contributes 0.

---

## Special flag: `content_fresh_but_design_stale`

Set to `true` when:
- Tech Stack Age ≥ 15 (old foundation) **AND**
- Footer copyright year is current (2026) **AND** (blog posts from within the last 12 months exist **OR** testimonial dates within 12 months exist)

These owners are engaged — they just never rebuilt. Different outreach angle: "your content is current but the design is working against you" (from proposal Q1). They often close faster than lower-engagement stale sites.

The flag is additive — it does **not** change the score. It drives outreach template selection, not prospect ranking.

---

## Special flag: `wordpress_spam_injection`

Set to `true` when a Firecrawl sitemap pull (or sitemap.xml fetch) reveals URLs matching the patterns documented in the main SKILL.md Group B workflow:
- `/category/essay-writing/`
- `/tag/buy-essay/`
- `/category/casino/` or `/slot/`
- `/?p=` URLs linking to offshore pharmacy / crypto / academic-fraud content

When flagged:
- Add a fixed +5 to `tech_stack_age` raw score (capped at 25 as usual)
- Set `flags.wordpress_spam_injection = true`
- Surface as a top-3 signal: "WordPress spam injection detected — site's SEO actively harmed"

This is both a rebuild motivator and a great outreach hook. Owners often don't know their site is compromised until we tell them.

---

## Page 3+ filtering (pre-scan gate)

**Status:** Heuristic approach, documented here for reference. The scoring function itself does not filter — it scores whatever URL it's given. The skill's Stage 2 applies this filter before handing URLs to the scorer.

**Heuristic v1 (MVP):**
1. Pull Places API results with `rankby=prominence` (default) and the max allowed page size.
2. Take results indexed 41–200 (skip the top 40). Assume that prominence-rank 1–40 roughly corresponds to SERP page 1–2 exposure — these businesses are already visible, so they're unlikely to feel pain about their site.
3. First real run: validate by cross-checking the skip-40 set against an actual Google SERP scrape for 3 representative queries (e.g., "HVAC Atlanta GA", "HVAC repair Sandy Springs", "AC service Roswell"). If >30% of the skip-40 set actually appears on SERP page 1 organic results, the heuristic is too aggressive — switch to v2.

**Heuristic v2 (if v1 fails validation):**
Scrape the actual top-20 organic SERP results for the target query via Firecrawl or Chrome DevTools MCP. Domain-match against the Places API set. Exclude any Places prospect whose domain appears in that top-20. This is slower (~20s per geo) but correct.

**Recommend:** Start with v1 for MVP. Record a validation comparison during first run. Switch to v2 if needed.

---

## Reference implementation outline (pseudocode)

```
function scoreSite(url):
  nav(url), waitForLoad()
  lh = runLighthouse(url)  # may return null on timeout
  dom = snapshotDOM()
  css = snapshotComputedStyles()
  net = networkSummary()
  mobileShot = screenshot(390, 844)
  ssl = checkSSL(url)
  sitemap = fetchSitemap(url)
  images = sampleImages(dom, max=10)

  tech       = scoreTechStack(dom, css, net, sitemap)        # cap 25
  lhComp     = scoreLighthouseComposite(lh)                  # cap 20
  mobile     = scoreMobile(dom, css, mobileShot)             # cap 15
  design     = scoreVisualDesign(dom, css, net)              # cap 15
  sec        = scoreSecurity(url, ssl, dom)                  # cap 10
  year       = scoreCopyrightYear(dom)                       # weight 0.5
  form       = scoreFormSophistication(dom)                  # cap 5
  imgQual    = scoreImageQuality(images)                     # cap 5

  total = tech + lhComp + mobile + design + sec + year + form + imgQual  # 0..100

  flags = computeFlags(dom, sitemap, url)  # content_fresh, wp_spam, godaddy, flash, http

  bucket = bucketFor(total)  # modern | borderline | rebuild_candidate | prime_prospect

  return { total, bucket, categories, flags, top_3_signals: topSignalsByWeight(...) }
```

---

## Calibration plan

After the first real scan run (HVAC Atlanta, top 10 by score):
1. Jesse hand-reviews all 10 and rates each as "real rebuild candidate Y/N".
2. If fewer than 6 of 10 are real candidates, the rubric is miscalibrated — likely weighting Lighthouse too low or Tech Stack too high (or vice versa).
3. Adjust weights by no more than ±5 points per category per iteration. Never change more than 3 categories at once.
4. Re-run on the same 200-prospect pool, compare old vs new top-10 overlap. Good calibration = top-3 stays stable, bottom-half of top-10 shifts.

**Don't touch the rubric during a live scan.** Lock the weights at the start of each scan run; record the version. Ratings from different rubric versions are not comparable.

---

## Version

**Rubric version:** `0.1.0-mvp` (April 2026)

Record this value in every `staleness-report.json` under `rubric_version`. When the rubric is revised, bump minor for weight tweaks, bump major for category additions or removals.

# HANDOFF-CONTRACT-ARCHIVE.md

Archived sections of `HANDOFF-CONTRACT.md` that have been superseded. Kept for audit trail.

---

## §11 — Quality Standards (original version) — ARCHIVED 2026-04-20

**Status:** Replaced by the Bruce-as-Collector contract (new §11).
**Reason for retirement:** The original §11 had Bruce owning a multi-step "enrichment phase" that included HTML edits, CSS filter application, commit-format rules, and responsibility for finishing whatever Rule1 didn't complete. This broke down repeatedly — Bruce's agent fumbled the "is this already enriched" scanner logic, commits landed in the wrong format, multi-agent file writes caused drift, and the scope kept expanding beyond what Bruce's tooling could reliably handle.
**Replaced by:** The Bruce-as-Collector amendment drafted 2026-04-20 night, Jesse ACK'd 2026-04-20 late evening. New §11 narrows Bruce's role to specialized scraping only (Yelp/Nextdoor/anti-bot sources) and consolidates build integration under Mini.
**Superseded commit reference:** See `HANDOFF-CONTRACT.md` §11 (new) for current rules.

Original §11 text preserved below:

---

## 11. Quality Standards (mandatory across R1VS, Bruce, Mini)

These standards govern every site that flows through the pipeline. Each player is responsible for their own section. No site reaches Jesse for outreach approval without clearing every gate.

### 11.1 R1VS responsibilities

- **Best-effort review pulling** on every site, using all available tools in this order:
  1. Google Places API (legacy + v1) — `GOOGLE_MAPS_API_KEY` in `~/.openclaw/.env`. CLAUDE.md explicitly permits ad-hoc use.
  2. Brave Search API — surfaces indexed snippets from Yahoo Local, MapQuest, Nextdoor business pages, HomeAdvisor profile detail.
  3. Firecrawl — testimonial sub-pages on business's own site + Yahoo Local + Nextdoor + MapQuest + Angi.
  4. Scrapfly with `render_js=true&country=us` — for JS-heavy sites Firecrawl can't crack (Google knowledge panels, Yelp anti-scrape).
  5. Direct WebFetch — last resort.
- Every attempt logged in `reviews.json` under `capture_attempts` with source + status + reason.
- **Photo + video upload module** on every estimate form (pattern matches `pine-peach-painting`). `accept="image/*,video/*"` with `multiple`.
- **Clean loading placeholder** if reviews captured < 3 after best effort. Format: minimal copy ("Verified customer reviews loading.") with hidden marker `<!-- REVIEWS_LOADING -->` for Mini's pre-publish gate.
- **Accessibility basics in HTML:** meaningful `alt` on every `<img>`, heading hierarchy stays in order, every form field has a `<label for="…">`, descriptive button text.

### 11.2 Bruce responsibilities

- **Augment, don't flood.** Total review count in the carousel **capped at 8**, regardless of how many are available.
- **Mix sources for variety:** prefer 5 Google + 1 Yelp + 1 Nextdoor + 1 MapQuest over 8 Google. Reads as more credible.
- **Don't replace R1VS reviews unless clearly better** (more verifiable, more recent, more on-brand). Document any swap in commit message.
- **Photo waterfall priority:** business's own site → Google Business Profile via Places API → Yelp/Nextdoor/MapQuest galleries via Scrapfly with `render_js=true` → Recraft AI → Unsplash background-only filler.
- **Alt text on every photo** Bruce drops (added to the `<img>` tag in the HTML).
- **Vertical CSS filter** applied per the SKILL.md filter table.
- **Commit pattern:** `enrich(<slug>): N photos + M reviews from <sources>` with a body explaining notable choices.

### 11.3 Mini's three "must pass" gates

Any failure blocks publishing. Site stays in `ready_for_review` until fixed.

- **Gate 1 — Reviews-loading marker is gone.** The `<!-- REVIEWS_LOADING -->` HTML comment must NOT be present. Failure → bounce to Bruce for review enrichment.
- **Gate 2 — Upload module is present.** The `.upload-area` CSS class + matching HTML in the contact form. Failure → bounce to R1VS to add it.
- **Gate 3 — Claim bar is present.** Shared `_shared/claim-ui.html` template injected. Failure → re-inject and re-verify.

### 11.4 Mini's accessibility audit (axe-core)

Mini runs the axe-core checker on every site (script in SKILL.md). Fixes:
- All "serious" and "critical" violations
- Color contrast: dim text raised to minimum 5.2:1 ratio on dark backgrounds
- Invalid ARIA roles (no `role="list"` on non-list `<div>`s)
- Heading hierarchy violations (no jumping `<h1>` to `<h3>`)
- Missing landmark regions (all content in `<section>`/`<nav>`/`<footer>` or has `role="region"`)
- Missing alt text on images

Moderate violations: noted, don't block.

### 11.5 Mini's design quality check

Per the gates added to SKILL.md `## ⚠️ MANDATORY WORKFLOW GATES (Non-Skippable)`:
- Brand color extracted from logo (not defaulted)
- Distinctive font (not Inter/Roboto/Arial/system)
- H1 gradient text applied
- Playfair Display on blockquotes/pull quotes
- Scroll-triggered reveals on major sections with staggered delays
- Photo overlays on service area + CTA sections (not solid colors)

### 11.6 Mini's pre-publish polish + QA pass (browser automation via chrome-devtools MCP)

Mini opens the staging site in a headless browser and verifies:

**Interactions:**
- Hamburger menu opens AND closes on mobile widths
- Hamburger icon positioned on the **right side** of the nav bar (not center, not left)
- FAQ accordion items expand and collapse
- Form submit shows success state when clicked
- Hero photo loads (not 404)
- All 6 gallery photos load (not 404)
- Sticky nav stays sticky on scroll
- Phone links: `tel:` href present, matches displayed number, header phone = footer phone = form-success phone

**Animations:**
- Reviews carousel is actually scrolling (animation running, not paused, not stuck)
- Scroll-triggered `.reveal` animations fire on viewport entry
- No CSS animation errors in browser console

**Claim bar interactions (specific to Jesse's recurring failures):**
- Claim bar present, contains the right text
- Claim bar appears EXACTLY ONCE (not duplicated, not stacked)
- No cookie banner injected in claim bar's place (sanity check the right HTML was used)
- "How it works" link opens the explanatory popup correctly
- "Claim Now" button URL is `gtmdot.com/checkout?code={CLAIM_CODE}` with the actual claim code populated (NOT "{CLAIM_CODE}" literal placeholder, NOT empty)
- Mini clicks the button in headless browser, follows redirect, verifies the claim code in the URL

**Popup behavior:**
- Fires on exit intent only (mouse moves toward browser top edge)
- Does NOT fire on every scroll, click, or after a timer
- Once dismissed, stays dismissed for the session
- Unobtrusive: max ~400px wide on desktop, full width on mobile
- Dismisses cleanly: close button works, escape key works, click-outside works

**Console health:**
- No JavaScript errors in browser console
- No 404s for image, CSS, or JS files

### 11.7 Mini's contextual copy check

- **Terminology audit per service vertical** — uses the new `TERMINOLOGY-MAPPING.md` to verify CTAs match service type. "Get a Free Estimate" on a tire-rotation site (which is transactional, not estimable) → flag and rewrite to "Book a Service".
- **AI-tells removal pass** via the installed `humanizer` skill. Looks for and rewrites:
  - Em dash overuse (cap at 1-2 per page)
  - Sycophantic openers ("It's important to note…", "In conclusion…", "Furthermore…", "Moreover…", "Additionally…")
  - Rule-of-three overuse (every sentence having three parallel items)
  - Bold-header lists in flowing prose
  - Inflated vocabulary ("utilize" → "use", "comprehensive" → "full", "assist" → "help")
  - Uniform sentence length (vary short/medium/long)

### 11.8 Photo placement + contextual relevance check

Mini verifies Bruce's photo work landed correctly:
- Every placeholder image path (`photos/hero.jpg`, `photos/gbp-1.jpg` … `photos/gbp-N.jpg`) actually has a real image file
- Each image actually loads in the browser (not 404)
- Photo at `hero.jpg` matches the hero shot intent in `photos/intent.json` (e.g., owner-at-work shot, not a random gallery image)
- Photo content matches service contextually (a plumbing site has plumbing photos, not cars; a landscaping site has yard work, not interiors)
- Vertical CSS filter is applied per SKILL.md filter table
- Alt text present on every `<img>` (added by Bruce per §11.2)

### 11.9 Bounce-back rules (who fixes what when QA fails)

- Reviews-loading marker still present → bounces to **Bruce**
- Upload module missing → bounces to **R1VS**
- Claim bar missing or broken → bounces to **Mini itself** to re-inject
- Photo missing or 404 or contextually wrong → bounces to **Bruce**
- Accessibility violation → bounces to **Mini** (Mini owns the audit)
- Design quality issue (structural) → bounces to **R1VS**
- Design quality issue (polish/styling) → bounces to **Mini**
- Copy AI-tells / wrong terminology → bounces to **Mini** (uses `humanizer` skill)
- Interaction/animation failure → bounces to **Mini**

Bounce message filename: `messages/<timestamp>-mini-to-<owner>-<slug>-bounce-<reason>.md` with the specific failure cited.

### 11.10 Self-audit before handoff

Each player audits own work before passing to next:
- **R1VS:** HTML valid, all sections present, upload module present, accessibility basics applied, alt text on every image
- **Bruce:** photos match `intent.json`, alt text added, vertical CSS filter applied, reviews capped at 8 with mix of sources, commit message documents notable choices
- **Mini:** all 3 must-pass gates pass, axe-core comes back clean on serious/critical, polish + QA pass produces a `qa-report.md`, hard quality bars (§11.11) met

If self-audit catches an issue, the player fixes it before passing the work along. Don't rely on the next person to catch your mistakes.

### 11.11 Hard quality bars to publish

Mini will not publish if any of these fail:
- **Minimum 3 reviews** in the carousel (real verbatim, not placeholder)
- **Minimum 4 photos** total (1 hero + 3 gallery minimum; ideally 1 hero + 6 gallery)
- **Lighthouse mobile performance score ≥ 85** (target sub-2-second load)
- **Claim bar buttons functional** (per §11.6 — "Claim Now" actually goes to checkout with claim code populated)

If any bar isn't met after Bruce + Mini effort, site stays in `ready_for_review` and Mini posts a status message to Jesse explaining what's blocking.

### 11.12 Bruce ↔ Mini coordination

- Bruce drops photos + augments reviews → writes `messages/<timestamp>-bruce-to-mini-<slug>-enriched.md`
- Mini's autonomous loop watches the messages folder for these files
- When Mini sees one, runs the full QA pass on that slug
- Either publishes (all gates pass) OR bounces via `messages/<timestamp>-mini-to-bruce-<slug>-bounce-<reason>.md` with specific failure cited
- Bruce picks up the bounce, fixes, re-enriches, posts a new enriched message
- Mini re-runs QA, repeat until pass
- On successful publish: Mini writes `messages/<timestamp>-mini-to-jesse-<slug>-deployed.md` + Slack ping in `#claude-sync` + updates Supabase stage

Always tell whose turn it is by looking at the most recent message file for that slug.

### 11.13 Pre-publish QA report (the artifact Jesse reads)

Mini produces `sites/<slug>/qa-report.md` after every QA pass. Contains:
- Summary: pass / fail / fail-then-fixed
- Each gate from §11.3-11.8 with status (pass/fail) and what was found
- Hard quality bars from §11.11 with measured values
- Screenshots of: default state, mobile menu open, popup open, scrolled-to-reviews
- Notes on what was rewritten (AI-tells removal diffs, terminology fixes)

Jesse reads the QA report before approving outreach. The report is the audit trail.

---

*Section 11 added 2026-04-20 per Jesse ACK. References: `2026-04-20-0929-r1vs-proposal-contract-expansion-quality-gates.md` and Jesse's six specific failure modes plus contextual copy + photo placement requirements from the same morning's chat. Companion file: `TERMINOLOGY-MAPPING.md` for the per-vertical CTA verb mapping.*

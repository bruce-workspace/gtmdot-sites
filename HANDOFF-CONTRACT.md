# HANDOFF-CONTRACT.md

**Purpose:** Single authoritative source of truth for who does what, in what order, with what communication protocol, on the GTMDot pipeline. This document supersedes any division-of-labor text that was previously scattered across `CLAUDE.md`, message history, or ad-hoc instructions. If another doc conflicts with this one, this one wins until the conflict is explicitly resolved via an ACK message.

**Scope:** Every Claude session on this pipeline (R1VS, Mini, any future peer), plus Bruce and Jesse. Global — not just trade sites.

**Read order at every session start:**
1. `CLAUDE.md` (system facts + overview)
2. `HANDOFF-CONTRACT.md` (this file — WHO + HOW)
3. `SKILL.md` (phase-by-phase WORKFLOW)
4. `DESIGN-HEURISTICS.md` (design + editorial JUDGMENT)
5. `ICON-MAPPING.md` (icon source of truth)

---

## 1. Role summary

| Role | Runtime | Machine | Primary responsibility |
|---|---|---|---|
| **R1VS** | Claude Code (interactive or `/loop`) | MacBook Pro | Research + HTML + content-craft polish + photo-intent |
| **Bruce** | OpenClaw (persistent daemon) | Mac Mini | Photo waterfall + review mining + heavy scraping (when R1VS/Mini can't) |
| **Mini Claude** | Claude Code (interactive or `/loop`) | Mac Mini | Photo wiring + mechanical polish + deploy + Supabase state |
| **Jesse** | Human | Either | Final QA approval + outreach triggers + strategic decisions |

---

## 2. Division of labor — who owns what

Each row owns the decisions in that row. **If you are not the owner, you do not make the change. You flag it to the owner via a message.**

| Artifact / Decision | R1VS | Bruce | Mini | Jesse |
|---|:---:|:---:|:---:|:---:|
| `RESEARCH.md` | ✅ | — | — | — |
| `reviews.json` (initial capture) | ✅ | — | — | — |
| `reviews.json` (enrichment when captured <3) | — | ✅ | — | — |
| `index.html` skeleton + copy | ✅ | — | — | — |
| Pull quote selection (above reviews + above form) | ✅ | — | — | — |
| Team cards (Rule 3 Mode A) | ✅ | — | — | — |
| Stats de-dup (Rule 3 Modes B/C/D) | ✅ | — | — | — |
| Contextual icons (per `ICON-MAPPING.md`) | ✅ | — | ⚠️ verify only | — |
| `photos/intent.json` | ✅ | — | — | — |
| Photo sourcing (Places API + Recraft + Unsplash waterfall) | — | ✅ | — | — |
| Photo wiring into HTML (hero bg, gallery, captions) | — | — | ✅ | — |
| Marquee speed (58s / 60s) | — | — | ✅ | — |
| Footer mobile 2-col grid | — | — | ✅ | — |
| Form upload field (`<input type="file">`) | — | — | ✅ | — |
| Story grid single-col breakpoint (900px) | — | — | ✅ | — |
| Em-dash cleanup in authored copy | — | — | ✅ | — |
| Claim bar + exit popup injection | — | — | ✅ | — |
| Cloudflare Pages deploy | — | — | ✅ | — |
| Supabase stage transitions | — | — | ✅ | — |
| Claim code assignment | — | — | ✅ | — |
| Final QA approval (`qa_approved` stage) | — | — | — | ✅ |
| Outreach triggers (email sequences, postcard sends) | — | — | — | ✅ |

**Rule:** If you catch yourself touching something in another role's column, STOP. Write a flag message (see §5) and back out.

---

## 3. The 1-pass contract (default workflow)

Preferred handoff path for a single site, minimizing R1VS roundtrips:

```
┌──────────────────────────────────────────────────────────────┐
│ PASS 1 — R1VS                                                │
│                                                              │
│  1. Research business via WebSearch + WebFetch               │
│  2. Write RESEARCH.md + reviews.json (best effort)           │
│  3. Write photos/intent.json (what photos the site needs)    │
│  4. Build index.html with content-craft polish applied       │
│  5. Create intake branch, commit, push                       │
│  6. Write messages/YYYY-MM-DD-HHMM-r1vs-<slug>-polished.md   │
└──────────────────────────────────────────────────────────────┘
                            ↓
┌──────────────────────────────────────────────────────────────┐
│ PASS 2 — BRUCE (only if R1VS flagged thin capture)           │
│                                                              │
│  1. Run Places API photo pull                                │
│  2. Run Firecrawl if owner site has usable content           │
│  3. Write updated reviews.json if reviews were thin          │
│  4. Deliver photos to sites/<slug>/photos/                   │
│  5. Commit + push, write bruce-to-mini-<slug>-enriched.md    │
│                                                              │
│  Bruce runs on their own cadence. No R1VS roundtrip.         │
└──────────────────────────────────────────────────────────────┘
                            ↓
┌──────────────────────────────────────────────────────────────┐
│ PASS 3 — MINI CLAUDE                                         │
│                                                              │
│  1. Pull intake branch                                       │
│  2. Wire Bruce's photos per R1VS's photos/intent.json        │
│     (if intent absent, infer from RESEARCH.md + reviews.json)│
│  3. Apply mechanical polish (marquee, footer, breakpoint,    │
│     form upload, em-dashes)                                  │
│  4. Inject claim bar + popup via shared template             │
│  5. Deploy to Cloudflare Pages                               │
│  6. Update Supabase prospects.stage → ready_for_review       │
│  7. Slack ping Jesse via #claude-sync                        │
│  8. Write messages/YYYY-MM-DD-HHMM-mini-to-jesse-<slug>-     │
│     deployed.md                                              │
└──────────────────────────────────────────────────────────────┘
                            ↓
┌──────────────────────────────────────────────────────────────┐
│ PASS 4 — JESSE                                               │
│                                                              │
│  1. Review the live preview on mobile                        │
│  2. Approve (stage → qa_approved) or reject                  │
│  3. If rejected: Slack reply with specific issues            │
└──────────────────────────────────────────────────────────────┘
```

**Total R1VS passes per site: 1.** Not 2, not 3. If you find yourself re-touching a site, the workflow is drifting — flag it.

### Exceptions (multi-pass allowed)

- **Bruce enrichment upgrade after R1VS polish:** if Bruce's scrape delivers richer named reviews after R1VS already selected an anonymous pull quote, R1VS is authorized to do a single re-polish pass to swap the stronger quote in. Commit message format: `polish(slug): upgrade pull quote to <named reviewer> after Bruce enrichment`. Example happened on `jack-glass-electric` commit `490b14a`.
- **QA rejection loop:** if Jesse rejects a site, R1VS and/or Mini fix per Jesse's notes. One fix pass only — if more needed, escalate to a conversation.
- **Contract-level changes:** if the rules in this document change, update the doc + send a message, don't silently drift.

---

## 4. The `/loop` requirement

Every active Claude session on this pipeline must be running `/loop` when work is in flight. Cron pulls are not enough — pulling messages ≠ acting on them.

### Minimum /loop behaviors

**R1VS /loop:**
- Every cycle: `git fetch origin main` and list new `jesse-*.md` or `mini-to-r1vs-*.md` messages
- If new messages: read and respond per request
- Otherwise: continue any in-flight site work or stand idle
- Default wake cadence: 180s active / 1200s idle (per ScheduleWakeup cache guidance)

**Mini /loop:**
- Every cycle: `git fetch origin main` and list new `r1vs-*.md`, `jesse-*.md`, or `bruce-to-mini-*-enriched.md` messages
- If new enrichment message: run Pass 3 workflow on that site
- If new R1VS/Jesse message: read, take requested action, write response
- Otherwise: process any pending Supabase stage transitions
- Default wake cadence: 180s active / 1200s idle

**Mini must start a /loop on session start.** Historical reference: 2026-04-19 morning, Mini was idle 5h while R1VS pushed 3 critical docs. The DIRECTIVE + WAKEUP chain at `messages/2026-04-19-0947` and `2026-04-19-1516` specifically addressed this. Standing rule from that recovery: **Mini /loop is mandatory when the pipeline is active.**

### Terminating a /loop

A Claude terminates its own /loop when:
- Its queue is drained and no new work is likely
- It hits a blocker requiring another Claude or Jesse
- Jesse explicitly says stop

Final act before terminating: write a `*-queue-drained.md` or `*-terminating.md` message summarizing what's done and what's blocked.

---

## 5. Commit message + message-file conventions

### Commit message format

```
<type>(<slug>): <short subject>

<body bullets>

<optional DESIGN-HEURISTICS citation block>
```

Types:
- `feat` — new site build
- `polish` — content-craft polish (R1VS owned)
- `wire` — photo wiring (Mini owned)
- `enrich` — Bruce enrichment (Bruce owned)
- `mech` — mechanical polish (Mini owned — marquee, footer, upload field, etc.)
- `deploy` — Cloudflare + Supabase state change (Mini owned)
- `msg` — writing a messages/ file
- `docs` — documentation update
- `fix` — bug fix on an existing site

### DESIGN-HEURISTICS citation in commit body

Required when applying design/editorial decisions. Format:

```
Applied DESIGN-HEURISTICS:
- §1 icon selection: verified all service cards match ICON-MAPPING.md
- §3 pull quote selection: Harmony Blackwell (specific story + named Kerry + CJ)
- §4 rule 3: Mode B — kept 20+ Years, swapped 3 duplicates for team callouts
- §5 content integrity: grep for fake-reviewer patterns — none found
- §13 pre-ship: 10/10 items verified

Not applicable this commit:
- §2 photo wiring (Mini-owned, deferred)
- §6-11 covered in previous commits
```

If you can't cite the rule you applied, you probably didn't apply it. Reviewers will catch this.

### Message file naming

Strict format: `messages/YYYY-MM-DD-HHMM-<from>-<subject>.md`

- `YYYY-MM-DD-HHMM` — UTC-equivalent to when the action was taken (local time is acceptable if consistent, but don't mix)
- `<from>` — one of: `r1vs`, `bruce-to-mini`, `mini-to-r1vs`, `mini-to-jesse`, `jesse-to-mini`, `jesse-to-bruce`, `jesse-to-r1vs`, `r1vs-jesse-to-mini` (for joint directives)
- `<subject>` — kebab-case slug describing the topic

Examples:
- `2026-04-18-0955-r1vs-polish-batch-4-sites.md` ✓
- `2026-04-19-0815-mini-ack-contract-split-revised.md` ✓
- `2026-04-19-0947-r1vs-jesse-DIRECTIVE-design-heuristics-mandatory.md` ✓
- `message.md` ✗ (no timestamp, no from)
- `2026-04-19-mini-update.md` ✗ (no HHMM)

### Message file contents

Every message file starts with YAML frontmatter:

```yaml
---
from: <role>
to: <role or roles comma-separated>
date: YYYY-MM-DD
subject: <one-line summary>
priority: <low | normal | high | urgent>
---
```

Body is markdown. Include:
- What changed / what you're requesting
- Relevant commit SHAs when referenced
- Clear asks (if requesting action)
- Blockers (if any)

---

## 6. Self-audit requirement before shipping

Before writing the finalization message for any site, run the audit from `DESIGN-HEURISTICS.md §13` and cite it in your commit message. Minimum verified items for R1VS polish work:

1. **Review card content integrity** — grep for `Company Mission`, `Our Story`, `About Us`, `Placeholder` in reviewer-name positions. Must return 0.
2. **Icon selection** — every service card icon matches `ICON-MAPPING.md` for its service type. No freestyled Lucide icons.
3. **Stats de-dup** — count matches between hero-stats and story-highlights. Must not be 4/4. If 3+/4, apply Mode B/C/D resolution from `DESIGN-HEURISTICS.md §4`.
4. **Pull quotes present** — exactly 2 per site (above reviews + above form), OR fewer with explicit reason in finalization message (thin reviews, review-blocked).
5. **Pull quote attribution** — named reviewer + specific context tag, not just "Google Review".
6. **Named owner/tech in hero subhead** — if captured in reviews.
7. **FAQ** — verbatim from source or skipped (no invented questions).
8. **No em dashes in authored copy** — em dashes are OK inside `<blockquote>` or verbatim review `<p>` tags only.
9. **Phone as `<a href="tel:...">`** — every occurrence.
10. **LocalBusiness schema** in `<head>` — with verifiable rating + reviewCount.

Mini and Bruce have their own audit subsets per their domain. Each role's audit output is cited in that role's commit message.

---

## 7. Violation-response protocol

When you catch another Claude violating the contract (e.g., Mini modifying pull quotes that R1VS owns), **do not silently overwrite.** Protocol:

1. **Stop** the task in progress.
2. **Document** what you caught, with commit SHA + specific line.
3. **Write** a `messages/YYYY-MM-DD-HHMM-<from>-to-<violator>-contract-violation.md` message.
4. **Do not revert** unless the violation ships something broken to production. Flag it and let the owner of the affected artifact fix it.
5. **Resume** your own work — don't let a flag block the queue.

Example: R1VS catches Mini selecting a pull quote on a grandfathered site. R1VS writes `messages/2026-04-19-XXXX-r1vs-to-mini-contract-violation-pull-quote.md` listing the site + commit + which line, then continues with other work. Mini reads the message on next /loop cycle and either (a) accepts + re-routes to R1VS for content-craft or (b) responds with reasoning for the override.

---

## 8. What NOT to do

Compiled from observed violations across the pipeline:

- **NO Unsplash stock in gallery slots.** Unsplash only for secondary section backgrounds per SKILL.md.
- **NO AI-generated review text EVER.** Every word in a review card must be verbatim from the API or scraped source. Caught example: `plugged-electricians-atl` "Company Mission" rendered as reviewer — removed in commit `c4ab292`.
- **NO icon freestyling.** Every icon must match `ICON-MAPPING.md`.
- **NO Mini touching R1VS-owned artifacts** (pull quotes, team cards, stats de-dup) unless content-craft has been explicitly delegated in a message.
- **NO R1VS touching Mini-owned mechanical polish** (marquee speed, footer grid, form upload field, story breakpoint) under the revised contract.
- **NO claim bar code in R1VS builds.** Mini's injector handles it.
- **NO `<!-- CLAIM_BAR_ANCHOR -->` comment.** Mini finds `</body>` and injects automatically.
- **NO freelancing a parallel workflow.** If this doc or `SKILL.md` covers it, use the documented path.
- **NO Mini idling without a /loop** when the pipeline is active (see §4).
- **NO deploying a site with `captured: 0` in reviews.json** without explicit Jesse approval.
- **NO back-and-forth between R1VS and Mini/Bruce** on the same site. Default is the 1-pass contract (§3). Exceptions are documented (§3 exceptions).

---

## 9. Change management for this doc

- Commit message format: `docs(handoff-contract): <change>`
- New rules should come from observed practice, not speculation.
- Rule changes require:
  1. A proposal message from the proposing Claude to affected Claudes
  2. ACK or counter from each affected Claude
  3. Edit to this doc referencing the proposal + ACK in the commit body
- Conflict with another doc (SKILL.md, DESIGN-HEURISTICS.md, ICON-MAPPING.md) is resolved by updating this doc to win and adding a note in the affected section.

---

## 10. Quick reference card (print this out if useful)

**Session start:**
1. Read the 5 docs (§ top of this file)
2. Start /loop if pipeline is active
3. Pull latest main

**Every site touch:**
1. Read site's `RESEARCH.md` + `reviews.json` before any decision
2. Confirm your role owns the change (§2)
3. Apply the relevant `DESIGN-HEURISTICS.md` section
4. Run the self-audit (§6) before finalization
5. Commit with citation format (§5)
6. Write finalization message with correct filename format (§5)

**Every session end:**
1. Write a summary or terminating message
2. Stop /loop cleanly (don't leave orphan ScheduleWakeups)
3. Push all in-flight commits before closing

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

---

*Created 2026-04-19 by R1VS after 24-site polish run revealed the need for a single authoritative contract doc. Supersedes scattered rules in CLAUDE.md + message history. Update as the pipeline evolves — but update HERE, not in 3 places.*

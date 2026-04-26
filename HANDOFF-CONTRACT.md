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

## 11. Bruce as Collector (replaces original §11 Quality Standards)

**Status:** Active as of 2026-04-20 late evening.
**Supersedes:** Original §11 Quality Standards — archived to `HANDOFF-CONTRACT-ARCHIVE.md`.
**Ratification:** Drafted by parallel Mini session, Master-Site-Builder-side (this session) ACK'd, Jesse ACK'd in chat 2026-04-20. Rule1 notification in `messages/2026-04-20-*-mini-to-r1vs-contract-amended-bruce-as-collector.md` (auto-adopts on next read).

---


## §11.1 — Bruce's Explicit Scope

**Bruce DOES:**
- Scrape sources listed in `collect-request.md` in the order specified
- Save raw images to `sites/<slug>/photos-raw/` with source-prefixed filenames (`owner-site-01.jpg`, `gbp-01.jpg`, `yelp-01.jpg`, `nextdoor-01.jpg`, `thumbtack-01.jpg`)
- Save raw reviews to `sites/<slug>/reviews-raw.json` following the schema in §11.5
- Write a completion report to `sites/<slug>/bruce-collected.md` following the schema in §11.6
- Report failures with a reason code — never retry autonomously
- Respect budget caps in §11.7

**Bruce DOES NOT:**
- Touch HTML, CSS, or any site source files
- Write captions, alt text, or any user-visible copy
- Apply CSS filters, crop images, or otherwise transform raw assets
- Decide which photos go where in the gallery
- Commit with format-specific rules (just drops files)
- Write to Supabase (zero DB writes — see §11.8)
- Update the CRM stage
- Register claim codes
- Deploy anything
- Send Slack notifications
- Touch `.env` or config files
- Retry failed scrapes (one attempt per source per request)
- Invoke itself — Bruce only runs in response to a `collect-request.md`

---

## §11.2 — Mini's Explicit Scope (post-handoff)

Everything not in §11.1. Specifically:
- Gap analysis: decide when Bruce is needed and which sources to request
- Write `collect-request.md` when calling Bruce
- Consume Bruce's raw output + Rule1's partial build
- Apply design heuristics (caption writing, photo placement, icon selection, hero replacement)
- Quote selection from raw reviews
- Claim bar + popup injection
- Claim code registration
- Cloudflare Pages deploy
- Supabase writes (stage transitions, notes, activity log)
- Slack notifications
- Email sequence prep + send
- Postcard prep (Poplar merge tags, hero + screenshot deploy)
- Jesse-to-Mini report files

---

## §11.3 — Rule1 Handoff Contract (new requirement)

Rule1's dossier must now include a `## Sources Attempted` section noting which sources Rule1 already scraped and what it got. This prevents Bruce from re-scraping sources Rule1 already hit, which was not required under the old contract.

Required fields:

```markdown
## Sources Attempted

| Source | Status | Photos Pulled | Reviews Pulled | Notes |
|---|---|---|---|---|
| Owner website | success | 4 | 0 | moonstonepressurewashing.com |
| Google Business Profile (Places API) | success | 7 | 10 | |
| Facebook | success | 3 | 0 | private posts not accessible |
| Instagram | failed | 0 | 0 | login wall |
| Yelp | not-attempted | — | — | requires persistent browser |
| Nextdoor | not-attempted | — | — | requires persistent browser |
| Thumbtack | not-attempted | — | — | requires persistent browser |
```

Status values: `success`, `failed`, `partial`, `not-attempted`.

Mini reads this section to decide which sources to request from Bruce. If Rule1 marks a source `success`, Mini does not ask Bruce to rescrape it.

---

## §11.4 — `collect-request.md` Format (Mini → Bruce)

Written by Mini to `sites/<slug>/collect-request.md` to invoke Bruce. Bruce's cron scans for files matching this pattern and executes the request.

```markdown
---
slug: moonstone-pressure-washing
prospect_id: 3325aee2-3b7b-48af-ace7-f51802d23221
requested_at: 2026-04-20T04:15:00Z
requested_by: mini
---

# Collect Request — Moonstone Pressure Washing

## Business context
- Name: Moonstone Pressure Washing
- Trade: Pressure washing (residential exterior)
- Owner: Alonzo + son (Georgia)
- Existing assets from Rule1: 4 owner-site photos, 7 GBP photos, 10 GBP reviews
- Gap reason: need additional photos (especially fence + roof work — advertised but no photo), additional reviews beyond Google

## Requested sources (priority order)
1. yelp.com — search "Moonstone Pressure Washing Lithia Springs GA"
2. nextdoor.com — search same
3. thumbtack.com — search same
4. BBB (if accessible)

## What to collect per source
- All photos attributed to the business or its work
- All reviews (verbatim text, date, reviewer name, star rating)
- Skip: photos that are obviously customer selfies unrelated to work

## Budget
- Max 20 photos total across all sources
- Max 50 reviews total across all sources
- Max 10 minutes wall-clock

## Skip if blocked
If any source returns captcha, login wall, or bot-detection page: mark as failed with reason, move to next. Do not attempt to bypass.
```

---

## §11.5 — `reviews-raw.json` Schema (Bruce's output)

```json
[
  {
    "source": "yelp",
    "source_url": "https://www.yelp.com/biz/moonstone-pressure-washing-lithia-springs",
    "scraped_at": "2026-04-20T04:21:00Z",
    "reviewer_name": "Sarah M.",
    "reviewer_profile_url": "https://www.yelp.com/user_details?userid=...",
    "star_rating": 5,
    "review_date": "2025-11-14",
    "review_text": "Alonzo showed up on time and spent 3 hours on our driveway...",
    "review_language": "en"
  }
]
```

All fields required except `reviewer_profile_url` (optional). If Bruce can't get a field, use `null`, never make up values.

---

## §11.6 — `bruce-collected.md` Format (Bruce's completion report)

```markdown
---
slug: moonstone-pressure-washing
request_id: 2026-04-20T04:15:00Z
collected_at: 2026-04-20T04:27:00Z
status: partial
---

# Bruce Collected — Moonstone Pressure Washing

## Summary
Scraped 3 of 4 requested sources. Yelp and Nextdoor successful. Thumbtack blocked.

## Results by source

### yelp — SUCCESS
- 5 photos → `sites/moonstone-pressure-washing/photos-raw/yelp-01.jpg` … `yelp-05.jpg`
- 12 reviews → appended to `reviews-raw.json`

### nextdoor — SUCCESS
- 2 photos → `sites/moonstone-pressure-washing/photos-raw/nextdoor-01.jpg` … `nextdoor-02.jpg`
- 4 reviews → appended to `reviews-raw.json`

### thumbtack — FAILED
- Reason code: `captcha`
- Detail: Hit Cloudflare interstitial at the profile page. Did not attempt bypass.
- Suggested retry: in 24 hours from a different IP / freshly-cycled profile.

### BBB — NOT-ATTEMPTED
- Reason: hit budget cap (10 min wall-clock) after Thumbtack failure + retry-free rule.

## Totals
- Photos collected: 7 (within budget of 20)
- Reviews collected: 16 (within budget of 50)
- Wall-clock used: 9m 47s

## Handing back to Mini
Raw files are in place. Over to you for integration.
```

Failure reason codes (use one of):
- `captcha` — any anti-bot challenge
- `login-wall` — requires account
- `rate-limited` — 429 or "too many requests"
- `not-found` — 404 or business not present on source
- `server-error` — 5xx from source
- `timeout` — network timeout
- `budget-exceeded` — would exceed cap; skipped
- `blocked-by-robots-txt` — robots disallow
- `unknown` — anything else (include detail)

---

## §11.7 — Budget Constraints

Every `collect-request.md` must include a `## Budget` section with explicit caps:

| Cap | Purpose |
|---|---|
| `max_photos_total` | Prevents runaway scraping on photo-rich sources |
| `max_reviews_total` | Prevents runaway on review-rich sources |
| `max_wallclock_minutes` | Hard stop; Bruce aborts and reports `budget-exceeded` |

Recommended defaults (Mini may override per request):
- 20 photos
- 50 reviews
- 10 minutes

Bruce must stop at the first cap hit and report via `bruce-collected.md`. Never exceed caps, even by 1.

---

## §11.8 — State Ownership (single-writer invariant)

| Asset | Owner | Readers |
|---|---|---|
| `sites/<slug>/collect-request.md` | Mini | Bruce |
| `sites/<slug>/photos-raw/*` | Bruce | Mini |
| `sites/<slug>/reviews-raw.json` | Bruce | Mini |
| `sites/<slug>/bruce-collected.md` | Bruce | Mini |
| Site source files (HTML/CSS/JS) | Mini | (read-only elsewhere) |
| Supabase `prospects` table | Mini | (read-only elsewhere) |
| Supabase `notes` table | Mini | (Jesse via CRM UI) |
| Cloudflare Pages deploys | Mini | — |
| `gtmdot-postcards.pages.dev` assets | Mini | — |

**Invariant:** Exactly one actor may write to each asset. Read is unrestricted. This eliminates the multi-agent drift we've seen under the old contract.

---

## §11.9 — Invocation Lifecycle

1. Mini completes gap analysis and decides Bruce is needed.
2. Mini writes `sites/<slug>/collect-request.md` with source list + budget.
3. Bruce's cron (or Bruce's watcher) detects the new file.
4. Bruce executes the scrape per the request — respects source order, stops at budget, never retries.
5. Bruce writes raw files + `bruce-collected.md`.
6. Bruce deletes or archives the `collect-request.md` to prevent re-execution.
7. Mini's watcher detects `bruce-collected.md` — resumes integration.
8. If Bruce reports any source as `failed`, Mini decides whether to re-request later or move on without.

---

## §11.10 — Retirement Path

This contract is retired if:
- Claude-on-Mini gains persistent real-browser access equivalent to Bruce's (via Chrome extension with long-lived session, or equivalent), AND
- 30-day rolling measurement shows Claude-on-Mini hitting ≥ 90% of what Bruce would have collected on the same prospects.

Until then, Bruce-as-Collector remains the contract.

---

## §11.11 — Asset Intelligence Layer (added 2026-04-26)

**Status:** Active per Jesse ACK in chat 2026-04-26 ("ACK §11.9 - works for me").
**Supersedes:** nothing — extends §11.1 and §11.2.
**Drivers:** Bruce stack upgrade to OpenAI Codex GPT-5.5 + gpt-image-2.
**Proposal source:** `messages/2026-04-26-1155-bruce-proposal-collector-asset-intelligence.md` + `messages/r1vs/2026-04-26-120000-r1vs-ack-bruce-asset-intelligence-with-counter.md` + `messages/r1vs/2026-04-26-130000-r1vs-proposal-handoff-contract-§11-amendment.md`.

*Note on numbering:* Jesse's ACK referenced the proposal text as "§11.9". This section is committed as §11.11 because §11.9 (Invocation Lifecycle) and §11.10 (Retirement Path) already exist. Sub-section numbering is renumbered correspondingly (`§11.11.1` ... `§11.11.8`). Content is unchanged from the ACK'd proposal.

### §11.11.1 — What Bruce additionally MAY do

In addition to the scrape-and-collect scope in §11.1, Bruce MAY:

- Generate atmospheric, hero, and brand images via OpenAI gpt-image-2, saved to `sites/<slug>/photos-generated/<purpose>-NN.<ext>` where `<purpose>` is one of: `hero`, `brand`, `service-card-bg`, `atmosphere`.
- Apply photo-quality labels to scraped raw images: `hero-candidate`, `proof-candidate`, `gallery-candidate`, `discard`.
- Detect icon mismatches (HTML `data-lucide` value vs business context) and flag them in advisory output. Bruce MUST NOT modify `icon-intent.json` directly — flags route to R1VS for resolution per §11.11.4.
- Verify object/context claims (e.g., confirm a photo shows actual HVAC equipment, not appliance-store imagery).
- Provide review-coverage advisory notes (sufficient / borderline / insufficient) with recommendations for which sources to enrich.
- Write the above to `sites/<slug>/bruce-asset-intel.md` (human-readable) and `sites/<slug>/bruce-asset-intel.json` (machine-readable, schema in §11.11.7).

### §11.11.2 — What Bruce STILL MAY NOT do

The §11.1 "DOES NOT" list remains in full force. Specifically Bruce MAY NOT:

- Touch HTML, CSS, or any site source files
- Write user-visible captions, alt text, or copy
- Decide final photo placement (which file fills `photos/hero.jpg` etc.)
- Modify `icon-intent.json` (must flag for R1VS instead per §11.11.4)
- Write to `sites/<slug>/photos/` directly — generated images stay in `photos-generated/`, scraped raw stays in `photos-raw/`. Mini does the integration copy.
- Modify any source-of-truth doc (CLAUDE.md, SKILL.md, HANDOFF-CONTRACT.md, DESIGN-HEURISTICS.md, ICON-MAPPING.md, TERMINOLOGY-MAPPING.md, R1VS-REBUILD-BRIEF.md)
- Bypass the budget caps in §11.7 (image generation counts against `max_wall_clock_minutes` and a new `max_generated_images` cap, default 4)

### §11.11.3 — Mini's default behavior (operational reweighting)

Per Jesse direction 2026-04-26: when `bruce-asset-intel.md` includes recommendations (hero choice real-or-generated, photo labels, etc.), Mini's default action is to **ACCEPT** Bruce's recommendation.

Override threshold: Mini overrides only when QA finds a specific issue (wrong subject, wrong vertical, image quality genuinely poor, brand mismatch). When Mini overrides, Mini documents the override reason in the deploy commit message or in a `messages/<date>-mini-to-r1vs-<slug>-asset-override.md` if the override changes a slot R1VS pre-specified.

This shifts Mini from "decide fresh from raw materials each build" to "ratify Bruce's call by default, override on specific cause." Single-writer-per-asset preserved (Mini still owns the integration copy into `photos/`); the shift is operational, not jurisdictional.

### §11.11.4 — Icon mismatch routing

When Bruce detects an icon mismatch in `bruce-asset-intel.md`, the routing is:

1. Bruce writes the warning into `bruce-asset-intel.md` and `.json`
2. Mini, during QA pass, files a flag message: `messages/<date>-mini-to-r1vs-<slug>-icon-flag.md` referencing the specific HTML file + current `data-lucide` + Bruce's recommended replacement
3. R1VS picks up the flag, updates `icon-intent.json`, regenerates the affected HTML, re-runs `pre-push-gate.sh` to verify, pushes
4. Mini redeploys the corrected build

Mini MAY NOT edit `icon-intent.json` directly. R1VS owns it.

### §11.11.5 — Generated image rules (the six guardrails)

All HTML `<img>` elements pointing at a generated image MUST satisfy:

1. **`data-source="generated"` attribute** is present on the `<img>`.
2. **The slot's `data-context`** does NOT include any of: `team-OK`, `owner-portrait-OK`, `real-customer-OK`, `real-job-OK`, `before-after-OK`, `proof-OK`. (Generated images may only fill aspirational/atmospheric slots.)
3. **The `alt` attribute** does not contain claims of authenticity: "our team", "our truck", "our crew", "completed by us", "real customer", or close variants.
4. **The corresponding `bruce-asset-intel.json` `generated_images[]` entry** includes a `license_note` string (canonical: `"Synthetic image. Do not represent as actual company work."`).
5. **The proportion of generated `<img>` tags** does not exceed 30% of total visible `<img>` tags across all pages of the site.
6. **All generated files** live under `sites/<slug>/photos-generated/` in their original form. Mini's integration copy into `sites/<slug>/photos/` preserves the `data-source="generated"` attribute on the HTML side.

R1VS's `pre-push-gate.sh` adds Check #7 to enforce 1, 2, 3.
R1VS's `verify-build.sh` adds Check #7 to enforce 5.
Bruce enforces 4 at write time. Mini enforces 6 at integration time.

### §11.11.6 — Required content of `bruce-asset-intel.md`

Human-readable companion to the JSON. Required sections:

```markdown
---
slug: <slug>
generated_at: <ISO 8601 UTC>
status: success | partial | failed
collect_request_ref: <path to triggering collect-request.md>
---

# Bruce Asset Intelligence — <Business Name>

## Photo Quality Assessment
(Per-photo labels with reasoning, including the path under photos-raw/
or photos-generated/ and a confidence score 0.0-1.0)

## Hero Recommendation
(Real GBP photo OR generated, with reasoning. If recommending generated,
include the prompt used and reference the generated_images entry in JSON.)

## Icon Verification
(Any mismatches found between data-lucide values in HTML and business
context, with recommended replacements per ICON-MAPPING.md.)

## Object/Context Verification
(Confirmation that photos depict the claimed business — e.g., HVAC
equipment vs appliance-store imagery, real fleet vs stock truck.)

## Review Coverage Notes
(Sufficient / borderline / insufficient + which sources to enrich next.)

## Generated Images
(List of files in photos-generated/ with purpose, prompt, intended slot.)
```

### §11.11.7 — `bruce-asset-intel.json` schema (machine-readable)

```json
{
  "slug": "<slug>",
  "generated_at": "<ISO 8601 UTC>",
  "status": "success | partial | failed",
  "model_stack": {
    "reasoning": "openai-codex-gpt-5.5",
    "image_generation": "openai-gpt-image-2"
  },
  "photo_quality": [
    {
      "path": "photos-raw/yelp-01.jpg",
      "label": "hero-candidate | proof-candidate | gallery-candidate | discard",
      "confidence": 0.85,
      "reasoning": "string",
      "object_tags": ["technician", "service-van"]
    }
  ],
  "hero_recommendation": {
    "preferred_path": "photos-generated/hero-aspirational.jpg",
    "preferred_source": "generated | real",
    "fallback_path": "photos-raw/yelp-04.jpg",
    "reasoning": "string"
  },
  "icon_warnings": [
    {
      "current_data_lucide": "hammer",
      "html_path": "sites/<slug>/services.html",
      "service_context": "electrical-repair",
      "recommended": "zap",
      "reasoning": "string",
      "confidence": 0.9
    }
  ],
  "object_verification": [
    {
      "claim": "appliance-repair vertical",
      "evidence": "string",
      "confidence": 0.9
    }
  ],
  "review_coverage": {
    "captured_total": 5,
    "sources_present": ["google"],
    "sources_recommended_for_enrichment": ["yelp", "nextdoor"],
    "sufficiency": "sufficient | borderline | insufficient",
    "reasoning": "string"
  },
  "generated_images": [
    {
      "path": "photos-generated/hero-aspirational.jpg",
      "purpose": "hero | brand | service-card-bg | atmosphere",
      "prompt": "string",
      "model": "gpt-image-2",
      "model_revision": "string",
      "license_note": "Synthetic image. Do not represent as actual company work.",
      "intended_slot_context": "any-aspirational-OK | atmosphere-OK"
    }
  ]
}
```

### §11.11.8 — Budget addition

§11.7's budget caps gain one new field:

- `max_generated_images: 4` (default)

Bruce stops at the cap. Generation cost (gpt-image-2) counts against `max_wall_clock_minutes` regardless of count.

---

## What this replaces in the old HANDOFF-CONTRACT.md §11

Everything. The old §11 described Bruce as owning a "post-build enrichment phase" with responsibility for scanning existing state, deciding whether to enrich, committing with specific formats, and handing back a fully-integrated site. That's retired. This is a clean-sheet narrow-scope replacement.

---

## Ratification

Sign-offs required:
- [ ] Master Site Builder (Rule1-side Claude)
- [ ] Mini (Mini-side Claude)
- [ ] Jesse (final authority)

Once ratified, this document replaces §11 in `HANDOFF-CONTRACT.md`, and the old §11 is moved to `HANDOFF-CONTRACT-ARCHIVE.md` with a deprecation note.

---

*Created 2026-04-19 by R1VS after 24-site polish run revealed the need for a single authoritative contract doc. Supersedes scattered rules in CLAUDE.md + message history. Update as the pipeline evolves — but update HERE, not in 3 places.*

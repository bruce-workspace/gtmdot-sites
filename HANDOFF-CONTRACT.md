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
- **Empty-shell 2-pass variant** (formalized 2026-04-19 after `2026-04-19-1321-mini-ack-2pass-empty-shell-plus-dupe-confirmed.md`): **Required when R1VS's pass-1 research yields `captured: 0` in reviews.json** (i.e. WebSearch + WebFetch cannot surface any verbatim reviews — common for empty-shell new builds where no GBP share URL exists and anti-scrape blocks Yelp/Chamber/etc.).

  Rationale: under the 1-pass contract, R1VS would produce an HTML skeleton without pull quotes, team cards, or a stats bar. That artifact can't close and Mini wouldn't deploy it. Better to split: R1VS captures research intent, Bruce enriches reviews, R1VS returns for complete HTML build, Mini deploys.

  **4-pass flow:**
  ```
  PASS 1 — R1VS (research + intent)
    1. Research via WebSearch + WebFetch
    2. RESEARCH.md — business intel + flag review capture status
    3. reviews.json with captured: 0 and flags: ["review_blocked_pending_bruce_retry"]
    4. photos/intent.json — vertical filter + slot intent
    5. Create intake branch, commit, push (NO index.html yet)
    6. Message: r1vs-<slug>-research-complete-pending-reviews.md

  PASS 2 — BRUCE (review + photo enrichment)
    1. Places API pull for reviews + photos
    2. Firecrawl owner site if accessible
    3. Update reviews.json in place (replace captured: 0 with captured: N)
    4. Drop photos into sites/<slug>/photos/
    5. Message: bruce-to-r1vs-<slug>-enriched.md  ← triggers R1VS pass 3
       (distinct from bruce-to-mini-*-enriched.md which is the retrofit-pattern signal)

  PASS 3 — R1VS (HTML build + content-craft)
    1. Read Bruce-enriched reviews.json + photo inventory
    2. Build index.html with pull quotes (§3), team cards (§4), stats bar
    3. Apply §13 pre-ship audit
    4. Commit, push, write r1vs-<slug>-polished.md

  PASS 4 — MINI (wire + mechanical + deploy)
    1. Photo wiring per intent.json
    2. Mechanical polish (marquee, footer, upload, breakpoint, em-dashes)
    3. Claim bar + popup injection
    4. Deploy to Cloudflare Pages
    5. Supabase stage → ready_for_review
  ```

  **Routing (per Mini's ACK):**
  - `bruce-to-r1vs-*-enriched.md` → R1VS picks up for pass 3 HTML build
  - `bruce-to-mini-*-enriched.md` → Mini picks up for pass 4 wire + deploy (retrofit pattern)
  - A `captured: 0` site with Bruce enrichment but no R1VS pass-3 message is **skipped** by Mini until R1VS completes pass 3

  **Trigger condition (when to invoke 2-pass vs 1-pass):** R1VS decides at the end of pass-1 research. If `captured >= 3` and sufficient for pull quotes (§3 thin-reviews rule), proceed with 1-pass. If `captured: 0` or `captured: 1-2` with thin-review flag, route to 2-pass.

  **Example:** `atl-mobile-mechanics` is the first 2-pass site (pass-1 intake branch `f0319f7` on 2026-04-19).

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

*Created 2026-04-19 by R1VS after 24-site polish run revealed the need for a single authoritative contract doc. Supersedes scattered rules in CLAUDE.md + message history. Update as the pipeline evolves — but update HERE, not in 3 places.*

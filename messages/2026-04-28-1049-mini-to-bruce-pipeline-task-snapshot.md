---
from: mini
to: bruce
date: 2026-04-28
subject: Pipeline task snapshot — cadence, I/O, and done-criteria for Paperclip migration
priority: high
---

# Pipeline task snapshot for Paperclip migration

Jesse has redirected the pipeline rebuild — instead of recreating the 11 missing
LaunchAgents / scheduled tasks one-for-one, Paperclip becomes the coordination
layer and the recovered SKILL.md files become Paperclip workflow-stage
instructions. He asked me to compile the read-only findings from the existing
skill files here so you can drive the Paperclip setup.

## Source of truth

All 11 SKILL.md files are intact at `~/.claude/scheduled-tasks/<task>/SKILL.md`
on the Mac mini. Identical copies in the April 26 backup at
`~/Desktop/claude-backup-2026-04-26/scheduled-tasks/`. None are missing.

## What's currently running vs not

| Task | LaunchAgent | MCP-registered | Notes |
|---|---|---|---|
| enrichment-dispatcher | ✅ exists (`com.gtmdot.enrichment-dispatcher.plist`) | ❌ no | But `state = not running` — needs a kick |
| All other 10 | ❌ vanished | ❌ no | The disaster wiped the plists |

`mcp__scheduled-tasks__list_scheduled_tasks` returns empty — the Claude harness
has zero registered tasks.

---

## Per-task structured snapshot

### 1. intake-pipeline-watcher

- **Cadence (description):** hourly 8am–midnight, every 2h 1am–7am
- **Cadence (body):** "every 20 min (staggered off Bruce's schedule)"
- ⚠️ **Cadence inconsistency** between frontmatter and body — Paperclip should pick one. Body's 20 min looks like the live version.
- **Inputs:**
  - `git pull` `gtmdot-sites/main`
  - Scans `messages/` for files mod time < 25 min: `r1vs-*-finalized.md`, `r1vs-*-polished.md`, `bruce-to-mini-*-enriched.md`, `bruce-to-mini-*-blocked.md`, `jesse-to-mini-*.md`
  - `/Users/bruce/.openclaw/workspace/gtmdot/sites/<slug>/` to check deploy state
  - `/Users/bruce/.openclaw/workspace/brucecom-v3/.intake-notifications/*.txt`
- **Outputs:**
  - Calls `brucecom-v3/scripts/process-intake.sh <slug>` (with `SKIP_BRUCE_CHECK=true` for grandfathered or polished sites)
  - Calls `brucecom-v3/scripts/watch-intake.sh --process`
  - Slack posts to channel `C0AQTKM8F0A` (#claude-sync)
  - Deletes processed `.intake-notifications/*.txt` markers
- **Done means:**
  - All matching messages from last 25 min processed (deploy or Slack alert)
  - Markers deleted
  - Runtime < 8 min
- **Hard limits:** never advances stage past `needs_*` into `qa_approved`; never re-deploys `handy-dandy-atlanta`; never kills claude processes

### 2. gtmdot-research-processor

- **Cadence:** every 30 min
- **Inputs:**
  - Supabase query: prospects where `stage='research'`
  - Existing `/Users/bruce/.openclaw/workspace/gtmdot/sites/<slug>/RESEARCH.md` (skip if present)
  - WebSearch / WebFetch (3-5 searches per prospect max)
- **Outputs:**
  - `gtmdot/sites/<slug>/RESEARCH.md` (REQUIRED, structured facts doc)
  - `gtmdot/sites/<slug>/BRAND.md` (REQUIRED)
  - `gtmdot/sites/<slug>/COPY.md` (optional)
  - Supabase note: author=`claude`, body starts `BUILD TASK: RESEARCH.md + BRAND.md written…`, `is_task=true`, `task_priority=high`
  - Optional Supabase PATCH: prospect's `gbp_url` or `existing_website` if newly found
  - Slack #claude-sync (only if ≥1 prospect processed)
- **Done means:**
  - Every research-stage prospect lacking RESEARCH.md now has one (or has an "⚠️ INCOMPLETE RESEARCH" flag at top if data was thin)
  - Build task note posted
- **Critical:** filename must be `RESEARCH.md`, NOT `COPY.md` — downstream tasks search for RESEARCH.md
- **This is the task that should have processed SmartWire Solutions and didn't.**

### 3. build-queue-checker

- **Cadence:** not specified in SKILL.md (PIPELINE.md says every 2h)
- **Inputs:**
  - `GET https://crm.cloakanddagger.co/api/prospects` (filter `stage='research'` AND `preview_site_url` empty)
  - `gtmdot/sites/<slug>/BRAND.md` and `RESEARCH.md` existence
  - Existing notes (look for "BUILD TASK" to dedupe)
- **Outputs:**
  - `POST http://localhost:3002/api/notes` — ⚠️ port 3002 looks wrong (CRM is on cloakanddagger.co or local 3000); Paperclip should standardize to one URL
  - Note body starts `BUILD TASK:` with `author='qa-bot'`, `taskPriority='high'`
  - For prospects missing files: `NEEDS RESEARCH:` note with `taskPriority='medium'`
  - Slack post to `C0AR5L2BKPG` (#site-build) as backup notification
- **Done means:**
  - Up to 3 ready prospects each have a BUILD TASK note (one per run)
  - Up to N missing-research prospects each have a NEEDS RESEARCH note
- **Hard limits:** max 3 new build tasks per run; skip prospects with existing BUILD TASK note

### 4. site-builder ⚠️ DEPRECATED

- **Status:** PIPELINE.md §3 explicitly marks this DEPRECATED — "R1VS now owns builds. Kept for reference."
- **Recommendation for Paperclip:** do NOT migrate this. R1VS handles building from intake branches.

### 5. site-build-monitor

- **Cadence:** PIPELINE.md says every 15 min
- **Inputs:** Slack #site-build channel (`C0AR5L2BKPG`), last 10 messages
- **Outputs:**
  - Slack acknowledgments to Bruce's posts
  - Slack nudges if a prospect is stuck in same phase >6h
  - Slack status summary if anything changed
- **Done means:** any stalled prospect (>6h same phase) has been nudged once; new Bruce posts have been acknowledged
- **Note:** SKILL.md hardcodes specific active builds (`forest-park-collision`, `bravo-plumbing`) — this list is stale

### 6. photo-syncer

- **Cadence:** every 15 min
- **Inputs:**
  - Supabase: `prospect_photos` where `selected=true`, joined to `prospects.slug`
  - Local filesystem (`gtmdot/sites/<slug>/photos/`) to skip already-downloaded files
- **Outputs:**
  - Local files: `gtmdot/sites/<slug>/photos/{gbp,manual,upload}-NN.{jpg,png,webp}` (zero-padded NN, by photo_reference prefix)
  - Supabase note: `Photos synced locally: N new files…` (author=`claude`, `note_type='general'`)
  - If site index.html doesn't reference `photos/`: flag note with `issue_type='photo'`, `assigned_to='bruce'`, `feedback_status='open'`
  - Slack #claude-sync only if ≥1 file downloaded
- **Done means:** every selected photo exists locally OR has a logged failure
- **Critical:** never delete photos; skip if file exists and >0 bytes

### 7. enrichment-dispatcher (only one with surviving LaunchAgent)

- **Cadence:** every 30 min
- **Inputs:**
  - `gtmdot-sites/sites/*/index.html` (skip if absent — R1VS hasn't built)
  - `gtmdot-sites/sites/*/reviews.json` (skip if absent)
  - `gtmdot-sites/sites/*/collect-request.md` (skip if pending — don't overwrite)
  - `gtmdot-sites/sites/*/bruce-collected.md` (skip if <48h old)
- **Outputs:**
  - `gtmdot-sites/sites/<slug>/collect-request.md` (per HANDOFF-CONTRACT §11.4)
  - Git commit + push (`enrich(dispatch): N new collect-requests for Bruce`)
  - Slack #claude-sync (only if ≥1 written)
  - Optional Supabase note (low priority)
- **Done means:** every site with photos<3 OR reviews_captured<3 (and no recent Bruce activity) has a fresh collect-request.md committed to main
- **Triggers:** photos<3 OR reviews_captured<3
- **Escalation:** same slug in `written[]` 3+ runs in a row → log feedback_status='open' for Jesse

### 8. site-qa-runner

- **Cadence:** every 15 min
- **Pre-step:** refresh stale GBP snapshots via `gtmdot-sites/scripts/refresh-stale-gbp-snapshots.py --only-stages outreach_sent,outreach_staged`
- **Inputs:**
  - `GET https://crm.cloakanddagger.co/api/prospects` (one fetch, used for entire run)
  - Loop-guard: existing qa-bot pass note since `stageEnteredAt`
  - `gtmdot/skills/gtmdot-design-qa/SKILL.md` and `gtmdot-change-check/SKILL.md`
- **Outputs:**
  - Three steps:
    - **Step 1 (full QA):** for `site_built` OR `claude_reviewed` (without recent qa-bot pass) — runs design-qa skill, fixes, redeploys via `gtmdot/scripts/deploy-site.sh <slug>`, posts qa-bot pass note (`✅ QA Check PASSED`), moves `site_built → claude_reviewed`
    - **Step 2 (change-check):** for prospects with stage move <30 min ago in non-excluded stages — runs change-check skill, posts pass note (always) or open flag (regression unfixable)
    - **Step 3 (git-based):** any site dir touched in last 30 min via git log — same change-check rules
  - Slack #site-build for any QA result
- **Done means:** every site needing QA either has a qa-bot pass note (loop-guard) or an open flag for unfixable regression
- **Hard limits:** 2 prospects/run for full QA, 3 for change-check; skip prospects with open Jesse flags; deploy via wrapper not raw wrangler

### 9. flag-checker

- **Cadence (description):** every 10 min
- **Cadence (body):** "every 20 minutes"
- ⚠️ **Cadence inconsistency** — Paperclip should pick one
- **Inputs:**
  - `GET https://crm.cloakanddagger.co/api/tasks/pending`
  - `gtmdot/.flag-check-state.json` (state for dedup)
- **Outputs:**
  - Updated `.flag-check-state.json`
  - Slack #gtmdot-builds (channel ID not specified in SKILL.md — needs lookup) ONLY if flag count or composition changed:
    - New flags: `🚩 [N] open flags blocking outreach: …`
    - Fixed flags: `👀 [N] fixes ready for Jesse to verify: …`
- **Done means:** state file updated; Slack notified iff something changed
- **Hard limits:** never attempt to fix flags itself; fail silently if API unreachable

### 10. flag-fixer

- **Cadence:** PIPELINE.md says "on-flag" (event-driven, not interval)
- **Inputs:**
  - `GET https://crm.cloakanddagger.co/api/tasks/pending` — read `summary.totalFlags` not top-level `totalFlags`
  - `gtmdot/CLAUDE.md`, `gtmdot/ICON-MAPPING.md`
  - Each flagged prospect's `gtmdot/sites/<slug>/index.html`
- **Outputs:**
  - Modified `index.html` (icon swaps, photo swaps, pricing fixes, copy fixes)
  - Deploy via `gtmdot/scripts/deploy-site.sh <slug>` (NEVER raw wrangler — bypasses gates)
  - `PATCH https://crm.cloakanddagger.co/api/notes` with `feedbackStatus: 'fixed'`
  - `POST /api/prospects/<id>/qa-check`
  - Slack #gtmdot-builds: `✅ Fixed [business name]: …`
  - Git commit + push
- **Done means:** flag is `feedbackStatus='fixed'`, site redeployed, fresh QA result posted, Slack notified
- **Skip rules:**
  - flag where `author='jesse'` AND `feedbackStatus='open'|'in_progress'` (Jesse is mid-review)
  - prospect stage `disqualified` or `dead`
  - photo flags: 4-step sanity check (photos exist, HTML doesn't already reference them, vertical match) — if any fails, leave note + skip
- **Hard limits:** 3 sites/run; one site at a time; never build new sites

### 11. gtmdot-morning-summary

- **Cadence:** 6am ET daily
- **Inputs:**
  - `gtmdot-sites` git pull
  - `brucecom-v3/scripts/pre-deploy-gate.sh <slug>` for every site (track pass/fail)
  - Supabase: prospects in `needs_approval`, `needs_decision`, `ready_for_review` (legacy)
  - `gtmdot-sites/messages/` for new `r1vs-*-finalized.md`, `bruce-to-mini-*-enriched.md`, `bruce-to-mini-*-blocked.md` since yesterday evening
- **Outputs:**
  - Single Slack post to `C0AQTKM8F0A` (#claude-sync) with structured summary:
    - READY FOR YOUR REVIEW
    - QUALITY GATE FAILURES
    - OVERNIGHT ACTIVITY
    - NOTHING URGENT vs. JESSE ACTION NEEDED
- **Done means:** Jesse opens Slack at 6am ET and sees today's status
- **Hard limits:** runs checks only — never deploys, never pushes git, never modifies sites, never moves prospects, never auto-fixes; <2 min total

---

## Cross-task data flow / dependencies

```
intake form (CRM)
   ↓
prospects.stage = 'research'
   ↓
gtmdot-research-processor                  → writes RESEARCH.md, BRAND.md, build-task note
   ↓
build-queue-checker                        → reads BRAND.md+RESEARCH.md, writes BUILD TASK note
   ↓
[R1VS owns this hop now, not site-builder]
   ↓
prospects.stage = 'site_built', preview_site_url set
   ↓
site-qa-runner (full QA)                   → writes qa-bot pass note, moves to claude_reviewed
   ↓
enrichment-dispatcher                      → writes collect-request.md if photos/reviews thin
   ↓
[Bruce scrapes per §11, writes bruce-collected.md + photos-raw/]
   ↓
intake-pipeline-watcher                    → re-deploys after Bruce enrichment or R1VS polish
   ↓
photo-syncer                               → downloads selected CRM photos to local
   ↓
flag-checker                               → polls open flags, notifies Slack
   ↓
flag-fixer                                 → fixes specific issues, redeploys, marks 'fixed'
   ↓
[Jesse manually moves to qa_approved]
   ↓
[Jesse triggers outreach]
   ↓
gtmdot-morning-summary                     → daily 6am ET digest of all of the above
```

## Inconsistencies / quirks worth resolving in Paperclip

1. **Cadence frontmatter ≠ body** in `intake-pipeline-watcher` (hourly vs every 20 min) and `flag-checker` (10 min vs 20 min). Pick one.
2. **`build-queue-checker` posts to `localhost:3002`** for notes — looks wrong. CRM is at `crm.cloakanddagger.co` or local `3000`. Verify before migrating.
3. **`site-builder` is officially deprecated** (PIPELINE.md §3) — do not migrate.
4. **Hardcoded Supabase service-role JWT in plain text** in `gtmdot-research-processor`, `site-builder`, and `photo-syncer` SKILL.md. Paperclip should reference an env var, not bake the key in.
5. **`flag-checker` references `#gtmdot-builds`** without a channel ID. The other tasks use `C0AR5L2BKPG` (#site-build) and `C0AQTKM8F0A` (#claude-sync). Confirm which channel is meant.
6. **`site-build-monitor` has stale state** baked in ("Current active builds: forest-park-collision, bravo-plumbing"). Do not migrate that hardcoded list.
7. **`flag-fixer` Step 1 parsing bug warning:** SKILL.md explicitly notes earlier failure where the wrong field path silently disabled the whole task. Migration should preserve the `summary.totalFlags` reading (not top-level).

## Open coordination question

PIPELINE.md and the SKILL.md files reference channel IDs, file paths, scripts,
and Supabase access patterns that all assume the current ad-hoc cron model.
For Paperclip migration, the unanswered question is **what state Paperclip
should own vs delegate**:

- Does Paperclip orchestrate from a workflow-stage definition and call into
  these scripts as-is?
- Or does each task get rewritten as a Paperclip-native step (no scripts)?

I'll wait for your call on this before doing anything else. Per Jesse: I am
in read-only mode, no LaunchAgent rebuilds, no MCP scheduled-task creation.

— Mini

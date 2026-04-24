# PIPELINE.md — Single Source of Truth for GTMDot Operations

**Status:** RATIFIED v1.0 (2026-04-24 by Jesse, Mini-authored 2026-04-23).
**Scope:** Who does what, at what cadence, through which stages, with what tools.
**Supersedes:** Replaces the scattered content in 12 docs (see §99 — 6 docs already archived to `/Users/bruce/.openclaw/workspace/archive/`).
**Conflict rule:** If any other doc conflicts with this one, *this doc wins* until the conflict is explicitly resolved via an ACK message in `messages/`.

**Read order at every session start:**
1. This file (who does what + current state)
2. `HANDOFF-CONTRACT.md` (detailed §11 Bruce-as-Collector contract)
3. `SKILL.md` (phase-by-phase build workflow)
4. `DESIGN-HEURISTICS.md` (design + editorial judgment)
5. `ICON-MAPPING.md` (icon source of truth)

---

## §1 Role Matrix

| Role | Runtime | Machine | Primary responsibility |
|---|---|---|---|
| **R1VS** | Claude Code (`/loop`) | MacBook Pro | Research + HTML + content-craft + photo-intent |
| **Bruce** | OpenClaw daemon (cron) | Mac Mini | Photo + review scraping (Collector scope only, per §11) |
| **Mini Claude** | Claude Code (`/loop` or interactive) | Mac Mini | Photo wiring + mechanical polish + deploy + Supabase state + QA |
| **Jesse** | Human | Either | Final QA approval + outreach triggers + strategic decisions |

**Ownership invariant (§11.8):** Exactly one actor writes to each asset. Reading is unrestricted. See `HANDOFF-CONTRACT.md` §2 for the detailed per-asset ownership table.

---

## §2 Pipeline Stages

Canonical stages in `prospects.stage`:

```
research
  ↓ (research-processor writes BRAND.md + RESEARCH.md + gbp_snapshot.json)
  ↓ (legitimacy-screen.py auto-DQ on farm/dormant/no-GBP)
research (complete)
  ↓ (R1VS runs Phase 0→5, pushes intake branch, writes finalization msg)
site_built
  ↓ (Mini wires photos, injects claim bar, deploys Cloudflare Pages)
ready_for_review
  ↓ (Jesse reviews live preview on mobile)
qa_approved
  ↓ (Jesse triggers outreach)
outreach_staged
  ↓ (postcard + email queued)
outreach_sent
  ↓ (claim or decay)
converted / dead
```

**Gate authority:**

| Transition | Gated by | Who can advance |
|---|---|---|
| `research → research (complete)` | `legitimacy-screen.py` passes + BRAND.md + RESEARCH.md + gbp_snapshot.json exist | R1VS (auto) |
| `→ site_built` | `pre-push-gate.sh` + `verify-build.sh` both exit 0 | R1VS (auto on push) |
| `site_built → ready_for_review` | Claim bar injected + deployed + Supabase note written | Mini (auto) |
| `ready_for_review → qa_approved` | Live preview passes Jesse's eyeball review | **Jesse (manual)** |
| `qa_approved → outreach_staged` | Postcard + email drafts generated + verified | Mini (auto) |
| `outreach_staged → outreach_sent` | Jesse approves the first real Poplar send | **Jesse (manual)** |

**Proposed refinement (Mini finding #6 — pending Jesse approval):** Split `ready_for_review` into three stages — `needs_enrichment` (Bruce/R1VS owes work), `needs_decision` (thin rep / dormant / Jesse-call), `needs_approval` (clean, queued for Jesse). Not yet migrated.

---

## §3 Automations (scheduled tasks)

Everything under `~/.claude/scheduled-tasks/` runs via the Claude Code harness. Each task is a `SKILL.md` file.

| Task | Cadence | Owner | What it does | Escalation trigger |
|---|---|---|---|---|
| `gtmdot-research-processor` | 30m | Mini | Auto-research new research-stage prospects, write BRAND.md + RESEARCH.md + (new) gbp_snapshot.json | Research fails for a specific business → task_priority:high note |
| `build-queue-checker` | 2h | Mini | Find research prospects ready for R1VS to build, post to #site-build | >3 prospects waiting → Slack mention |
| `site-builder` | 2h | Bruce (legacy) | **DEPRECATED** — R1VS now owns builds. Kept for reference. | N/A — task should be removed |
| `photo-syncer` | 15m | Mini | Download CRM-picked photos to `gtmdot/sites/<slug>/photos/` | Download failures → note with qa-bot author |
| `site-qa-runner` | 15m | Mini | Full Claude design QA on `site_built` + `claude_reviewed` stages | Open flags block the run — Jesse must resolve |
| `flag-checker` | 10m | Mini | Notify Bruce about open QA flags; notify Jesse on "fixed" transitions | New flags → #gtmdot-builds Slack |
| `flag-fixer` | on-flag | Mini→Bruce | Fix icon/photo/pricing issues on flagged sites | Jesse-authored in-progress flags are skipped |
| `site-build-monitor` | 15m | Mini | Check #site-build channel, respond to Bruce handoffs, nudge stalled builds | Phase stalled 6h+ → gentle nudge |
| `enrichment-dispatcher` | 30m | Mini | *(NEW — shipped 2026-04-23)* Write collect-request.md for sites with thin capture (<3 photos OR <3 reviews) | Same slug flagged 3+ runs → feedback_status:open |
| `intake-pipeline-watcher` | 10m | Mini | Watch CRM intake form for new prospects, normalize data, slug-dedupe | Duplicate slug detected → merge or disambig note |
| `gtmdot-morning-summary` | 6am daily | Mini | Audit deployed sites against quality gate, post summary to Slack | Quality gate failures → per-site slug list |

**Terminology:** "Cron" in this doc means "Claude Code scheduled task." These are not raw crontab entries — they're Claude sessions that fire at the configured cadence.

---

## §4 Current State Snapshot

<!-- state-snapshot:begin — auto-generated by scripts/state-snapshot.sh; do not edit by hand -->
*Last updated: 2026-04-24T03:49:52Z*

**Prospect stages (non-disqualified):**
- ready_for_review: 31
- outreach_staged: 13
- outreach_sent: 3

**Disqualified:** 14

**Open design-feedback flags:**
- in_progress: 17

**Enrichment loop state:**
- in-flight collect-requests: 6
- fresh bruce-collected (<48h): 0
- needs-repolish signals waiting R1VS: 18

**GBP snapshot staleness:**
- total: 1
- fresh (<14d): 1
- soft-stale (14-30d): 0
- hard-stale (>30d): 0

<!-- state-snapshot:end -->

## §5 CHANGELOG

Session-level event log. This section replaces the dated `HANDOFF-*.md` and `RESUME-BRIEF-*.md` files that were accumulating at workspace root.

**Rule:** Dated entries, prepend newest on top. Keep each entry ≤200 words. If more detail is needed, link to a `messages/` file.

### 2026-04-23 — Pipeline-review + R1VS introspection + first tool rollout

**Delivered on Mini side:**
- 13-finding pipeline review posted to #claude-sync
- Overnight QA on 26 sites (3 DQ'd as hard blockers: AI review farm, no-GBP match, thin reputation)
- ACK on R1VS Proposal 1 (gbp_snapshot schema) with 4 refinements
- Shipped `scripts/pipeline-next-prospect.py` — replaces in-prompt DONE list (finding #4)
- Shipped `scripts/bruce-heartbeat-cleanup.sh` — collapsed 212 stale heartbeat files (finding #13)
- Shipped `scripts/enrichment-dispatcher.py` + scheduled-task SKILL — Bruce auto-enrich (finding #5); first run queued 7 collect-requests
- Drafted this `PIPELINE.md` v0.1 (finding #3)

**Delivered on R1VS side:**
- `scripts/legitimacy-screen.py` + `scripts/pre-push-gate.sh` + `scripts/verify-build.sh` + `scripts/bootstrap.sh` + `scripts/write-gbp-snapshot.py`
- `templates/multi-page/` scaffold (SKILL §3b compliance)
- `templates/BUILD-STATE.template.md` + `.gtmdot-photo-slot` CSS pattern
- **SKILL.md restructure landed** (commit `5166913`) — Phase 0/4/5 added, multi-page default, conditional review UI per capture count
- **Pilot run on `plugged-electricians-atl`** (commit `acf4e2c`) — end-to-end Phase 0→5 validation
- Bug fixes from pilot (commit `8a066d4`)

**Still pending Jesse decision:**
- #3 PIPELINE.md ratification (this doc → SSoT, 5+ older docs retired)
- #6 Split `ready_for_review` into 3 stages
- Auto-DQ of 6 `in_progress` prospects in current queue

### 2026-04-22 — Overnight photo+review pass

See `OVERNIGHT-RESULTS-2026-04-22.md` for site-by-site summary.
26 prospects reviewed, 3 DQ'd, 12 recommended-approve, 8 in-progress flags.
Major discovery: 5 reviews fabricated as "Yahoo Local" (platform shut down 2017) on `hvac-guyz-plumbing-inc`.

### 2026-04-21 — Pre-outreach reset

See `POST-BUILD-HANDOFF-2026-04-21.md` for details.
Jesse approved 17 sites for outreach, parked 7 with pre-outreach blocks, cleared 66 stale in_progress flags.

### 2026-04-20 — §11 Bruce-as-Collector contract ratified

See `HANDOFF-CONTRACT.md` §11.
Bruce scope narrowed to Collector-only. Old §11 archived to `HANDOFF-CONTRACT-ARCHIVE.md`.

### Earlier entries

Pre-2026-04-20 history lives in:
- `BRUCE-HANDOFF.md` (Apr 4 — archive candidate)
- `JESSE-HANDOFF-2026-04-10.md` (Apr 10 — still useful for intake-pipeline context)
- `R1VS-REBUILD-BRIEF.md` (Apr 16 51-site rebuild campaign — archive candidate, campaign complete)
- `briefs/*.md` (one-shot project briefs — archive candidates)

---

## §80-99 Amendment Process

(Inherited verbatim from `HANDOFF-CONTRACT.md` §9 — if that doc gets retired, keep this section here.)

1. Changes to this doc require a proposal message in `messages/YYYY-MM-DD-HHMM-<author>-proposal-<topic>.md`
2. Affected roles ACK (or counter) via reply messages
3. Jesse ratifies via `messages/*-jesse-ack-*.md` or by committing the change directly
4. Commit format: `docs(pipeline): <one-line change summary>` with DESIGN-HEURISTICS citation block in body
5. If this doc conflicts with another doc, update this doc to win + note the other doc's section is superseded

---

## §99 Docs This Supersedes (once ratified)

When Jesse ACKs v1.0 of this doc, the following become archive candidates:

| Doc | Current content | Absorbed into |
|---|---|---|
| `BRUCE-HANDOFF.md` (workspace root, Apr 4) | Old Bruce-as-builder scope | §1 role matrix note + archived; content obsolete |
| `JESSE-HANDOFF-2026-04-10.md` | CRM intake + background processor | §3 automations table (intake-pipeline-watcher, gtmdot-research-processor) |
| `POST-BUILD-HANDOFF-2026-04-21.md` | One-session handoff for the 17 outreach_staged | §5 CHANGELOG 2026-04-21 entry |
| `RESUME-BRIEF-2026-04-22.md` | One-session resume brief | §5 CHANGELOG 2026-04-22 entry + `bootstrap.sh` replaces the pattern going forward |
| `R1VS-REBUILD-BRIEF.md` (gtmdot-sites, Apr 16) | 51-site rebuild campaign | §5 CHANGELOG (campaign done) |
| `OVERNIGHT-RESULTS-2026-04-22.md` | Site-by-site QA summary | Kept as historical record, referenced from §5 |
| `OVERNIGHT-STATUS.md` | Apr 16-17 overnight build status | §5 CHANGELOG — archive candidate |
| `~/.claude/skills/bruce-handoff/SKILL.md` | Slack/handoff orchestration (OLD scope) | Rewrite required — §11 Collector scope, not builder scope |

The canonical doc set after ratification:
- **`PIPELINE.md`** (this file) — SSoT for who/what/when
- **`HANDOFF-CONTRACT.md`** — §11 detail contract (Bruce-as-Collector)
- **`SKILL.md`** — per-site build phases (Phase 0→5)
- **`DESIGN-HEURISTICS.md`** — per-site content judgment
- **`ICON-MAPPING.md`** — icon source of truth
- **`CLAUDE.md`** (gtmdot-sites root) — codebase-level Claude Code context
- **`messages/`** — operational coordination (replaces dated handoff docs)

---

## Ratification decisions (resolved 2026-04-24 by Jesse)

Per `briefs/07-pipeline-md-ratification-checklist.md`:

1. **Location:** `gtmdot-sites/PIPELINE.md` — colocated with other canonical docs (HANDOFF-CONTRACT, SKILL, DESIGN-HEURISTICS, ICON-MAPPING).

2. **Ratification protocol:** Single Jesse ACK for v1.0. Future amendments use the §80-99 process (inherited from HANDOFF-CONTRACT §9): proposal message → affected-role ACKs → Jesse ratifies.

3. **CHANGELOG length cap:** Keep current year in-line. Archive older entries annually to `CHANGELOG-<year>.md`.

4. **CLAUDE.md pointer:** Yes. One-line "read PIPELINE.md first" added to `CLAUDE.md`.

5. **Single-writer ownership per section:**
   - §1 Role Matrix — Jesse (structural changes require Jesse ACK via §80-99)
   - §2 Pipeline Stages — Jesse ACK required; Mini/R1VS propose
   - §3 Automations — R1VS can update tool references; Mini can update Mini-owned scheduled tasks; Jesse ACKs new task additions
   - §4 Current State Snapshot — automated via `scripts/state-snapshot.sh` (no manual edits)
   - §5 CHANGELOG — any actor appends their work; no pre-approval for entries

— Mini (Master Site Builder, Mac Mini) 2026-04-23 draft; Jesse ratified 2026-04-24 v1.0

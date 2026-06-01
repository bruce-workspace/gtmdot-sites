# GTMDot Dispatcher Bridge B1 Scope

Date: 2026-05-18
Owner: Codex / GTMDot Quarterback
Status: proposed implementation scope
Purpose: remove Jesse as the copy/paste bus between GTMDot lane sessions while preserving Paperclip, Git/message files, and explicit approval gates as the durable operating model.

## 1. Problem

GTMDot now has multiple active project/session lanes:

- Main quarterback / Codex
- Pre-Build Coordination
- Post-Build Operations
- Outreach Operations
- GTMDot Platform / CRM v2
- Experiments
- Bruce enrichment
- R1VS scaffolding

Each lane is producing useful artifacts, but coordination is still mostly manual. Jesse has to:

- Notice a lane update.
- Copy it into the main session.
- Ask what to do next.
- Copy instructions into another session.
- Return with the result.
- Repeat the loop.

This is now one of the largest operational bottlenecks. It creates lag, stale state, duplicated questions, and misrouted work.

## 2. B1 Goal

Build a local Dispatcher Bridge that watches the existing canonical file ledger and Paperclip board, turns lane updates into normalized coordination events, updates the quarterback status, and prepares or applies safe Paperclip coordination updates.

The bridge should make this possible:

> A lane writes its latest status or artifact. The dispatcher detects it, maps it to the relevant GTM issue, updates the main quarterback digest, queues the next action, and tells Jesse exactly what needs approval, if anything.

## 3. Non-Goals

B1 is not an autonomous production operator.

B1 must not:

- Write CRM/Supabase prospect truth.
- Deploy sites or Cloudflare projects.
- Submit Poplar postcards.
- Send Resend emails.
- Contact prospects or customers.
- Trigger SMS.
- Touch Stripe.
- Change DNS, domains, hosting, billing, or production settings.
- Push git branches.
- Delete historical notes or artifacts.

B1 coordinates, summarizes, routes, and prepares bounded next actions. Execution still requires explicit approval when it touches the world.

## 4. Canonical Inputs

B1 should read:

- `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/status/*.md`
- `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/*.md`
- `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/r1vs/*.md`
- `/Users/bruce/.openclaw/workspace/paperclip-sandbox/artifacts/**/*.md`
- Paperclip local API at `http://127.0.0.1:3199`
- Optional read-only CRM API for context only, never truth mutation

Priority status files:

- `messages/status/quarterback-latest.md`
- `messages/status/pre-build-coordination-latest.md`
- `messages/status/post-build-operations-latest.md`
- `messages/status/outreach-operations-latest.md`
- `messages/status/gtmdot-platform-latest.md`
- `messages/status/experiments-latest.md`

## 5. Canonical Outputs

B1 should write:

- `messages/status/quarterback-latest.md`
- `messages/dispatcher/digests/YYYY-MM-DD-HHMM-dispatcher-digest.md`
- `messages/dispatcher/outbox/YYYY-MM-DD-HHMM-to-<lane>.md`
- `messages/dispatcher/state.json`
- Optional Paperclip comments/status changes only in approved safe-update mode

The outbox is intentionally a transition tool. Until direct inter-session messaging exists, it gives Jesse copy/paste-ready lane messages that are generated from the canonical state instead of improvised in chat.

## 6. Event Model

B1 should normalize lane updates into event records:

- `lane_status_updated`
- `artifact_created`
- `decision_needed`
- `approval_requested`
- `blocker_found`
- `blocker_cleared`
- `action_completed`
- `cross_lane_dependency`
- `paperclip_health_warning`
- `stale_lane_warning`

Each event should include:

- Event ID
- Timestamp
- Source file
- Source lane
- Referenced GTM issue IDs
- Prospect slug if available
- Summary
- Current blocker
- Recommended next owner
- Whether Jesse action is required
- Whether the event is safe to auto-mirror into Paperclip

## 7. Routing Rules

B1 should map work by issue and lane:

- `GTM-2`, `GTM-7`, `GTM-8`, `GTM-9`, `GTM-24`: Outreach Operations
- `GTM-3`, `GTM-11`, `GTM-12`, `GTM-13`, `GTM-14`: Post-Build Operations
- `GTM-4`, `GTM-15`, `GTM-16`, `GTM-17`, `GTM-18`: Pre-Build Coordination
- `GTM-5`: GTMDot Platform / CRM v2
- `GTM-6`: Paperclip Recovery / Infrastructure
- Bruce enrichment requests: Bruce
- R1VS build packets or scaffold returns: R1VS
- Unknown or ambiguous issue references: Main quarterback / Jesse decision queue

## 8. B1 Operating Modes

### Dry Run

Default mode.

Behavior:

- Reads all inputs.
- Produces dispatcher digest.
- Produces lane outbox messages.
- Updates no Paperclip state.
- Touches no CRM, deploy, send, or production systems.

Use this first.

### Safe Update

Approved mode.

Behavior:

- Performs dry-run steps.
- Adds Paperclip comments to referenced issues.
- Optionally updates issue status only when the artifact has explicit unambiguous language like `complete`, `blocked`, or `ready for Jesse decision`.
- Never performs production actions.

### Watch Mode

Later mode.

Behavior:

- Runs every 5-10 minutes.
- Checks file hashes/mtimes.
- Emits digests only when something changes.
- Can be launched via `launchd` after B1 proves reliable.

## 9. B1 MVP Features

### B1.0 Read-Only Dispatcher

Build a script that:

1. Reads all lane latest files.
2. Reads recent message artifacts since the last run.
3. Extracts GTM IDs, slugs, lane names, blockers, decisions, next actions, and artifact links.
4. Generates one quarterback digest.
5. Generates lane-specific outbox prompts.
6. Writes `dispatcher/state.json` so repeated runs do not duplicate the same events.
7. Reports Paperclip health, backup freshness, and lane staleness.

Success condition:

- Jesse can open one digest and know what happened across all lanes and exactly what to approve or send next.

### B1.1 Paperclip Comment Bridge

Add safe Paperclip write support:

1. Comment on GTM issues with summarized lane updates.
2. Link new artifacts to the relevant issue.
3. Avoid duplicate comments using state hashes.
4. Queue failed Paperclip writes instead of losing them.

Success condition:

- Paperclip becomes the visible cross-lane audit trail without Jesse manually pasting every update into it.

### B1.2 Approval Queue

Generate an explicit Jesse approval queue:

- Prospect
- GTM issue
- Requested action
- Why it matters
- Risk/blast radius
- Recommended approval text
- Actions still prohibited
- Destination lane if approved

Success condition:

- Jesse is no longer asking, "What am I supposed to do next?"

### B1.3 Health and Reliability

Add checks for:

- Paperclip API reachable
- Paperclip backup exists and is recent
- Paperclip process running
- Lane status file freshness
- Dispatcher state file valid JSON
- Duplicate-event suppression working

Success condition:

- Paperclip going down is detected quickly and reported as an infrastructure issue, not discovered by accident mid-work.

## 10. Recommended File Layout

Preferred:

```text
/Users/bruce/.openclaw/workspace/gtmdot-sites/
  workers/
    gtmdot_dispatcher_bridge.py
    paperclip_client.py
  config/
    dispatcher-routing.json
  messages/
    dispatcher/
      state.json
      digests/
      outbox/
```

Why `gtmdot-sites`:

- It already holds the cross-agent message ledger.
- It is the canonical coordination repo.
- R1VS, Bruce, Mini, Codex, and lane sessions already know to look there.

## 11. Digest Shape

Each dispatcher digest should include:

```md
# GTMDot Dispatcher Digest - <timestamp>

## Executive State
- Board clearing status:
- Highest priority:
- Jesse action needed:
- Production risk:

## New Events
- Event:
- Source:
- GTM issue:
- Summary:
- Next owner:

## Approval Queue
- Approval needed:
- Recommended approval text:
- Still prohibited:

## Lane Status
- Pre-Build:
- Post-Build:
- Outreach:
- Platform:
- Experiments:
- Bruce:
- R1VS:

## Cross-Lane Dependencies
- Dependency:
- Blocking issue:
- Needed from:

## Paperclip Health
- API:
- Backup:
- Last dispatcher run:

## Recommended Next 3 Moves
1.
2.
3.
```

## 12. Outbox Shape

Each lane outbox message should be copy/paste-ready:

```md
# Dispatcher -> <Lane>

Source: GTMDot Dispatcher Bridge B1
Paperclip issue:
Related artifact:

## Context

## Requested Action

## Boundaries
- No CRM writes unless explicitly approved.
- No deploys unless explicitly approved.
- No sends/contact unless explicitly approved.
- No git pushes unless explicitly approved.

## Required Return
- Artifact path:
- Status file update:
- Blockers:
- Next recommended owner:
```

## 13. Safety Rules

B1 must enforce these rules in code and docs:

- Default to dry-run.
- Never infer approval from a lane artifact.
- Never treat CRM stage as proof of postcard/email/channel truth.
- Never treat HTTP 200 alone as asset proof.
- Never delete notes; only mark stale/resolved in artifacts.
- Never auto-send or auto-deploy.
- Never print secrets.
- Never mutate Paperclip if Paperclip health check fails.
- Never duplicate comments on repeated runs.

## 14. Implementation Plan

### Step 1: Build B1.0 Dry Run

Create the script, routing config, dispatcher directories, and first digest.

Allowed actions:

- Read files.
- Read Paperclip health.
- Write dispatcher digest/outbox/state files.

### Step 2: Validate Against Current Board

Run against current GTM board state:

- Harrison / `GTM-12`
- InTire / `GTM-13`
- Outreach Poplar exceptions / `GTM-8`
- Reply monitoring / `GTM-24`
- Platform CRM v2 coordination / `GTM-5`

Expected result:

- One coherent main digest.
- Correct next actions.
- No duplicate or hallucinated work.

### Step 3: Add Safe Paperclip Comments

Only after dry-run output looks right.

Allowed actions:

- Add comments to GTM issues.
- Link artifacts.
- Update issue status only with explicit approval.

### Step 4: Add Scheduled Watch

Only after safe-update mode proves stable.

Use `launchd` to run every 5-10 minutes and write health warnings.

## 15. First Approval Needed

Recommended approval text:

```text
Approved: implement Dispatcher Bridge B1.0 dry-run only.

Allowed actions:
1. Create dispatcher bridge files under gtmdot-sites/workers, gtmdot-sites/config, and gtmdot-sites/messages/dispatcher.
2. Read lane status files, recent GTMDot message artifacts, Paperclip local API health, and Paperclip issue metadata.
3. Write dispatcher digest, lane outbox files, and dispatcher state JSON.
4. Run the bridge in dry-run mode against the current GTM board.

Still prohibited: CRM writes, Paperclip mutations, deploys, Poplar sends, Resend sends, prospect/customer contact, git pushes, production site edits, DNS/domain/hosting/billing changes, and Stripe actions.
```

## 16. Why This Is Worth Doing Now

The board-clearing work is no longer blocked primarily by site building. It is blocked by coordination drag:

- Which lane knows what?
- Which issue is current?
- Which notes are stale?
- Which action needs Jesse approval?
- Which artifact supersedes which old artifact?
- Which lane should act next?

B1 directly attacks that bottleneck. It does not replace Paperclip. It makes Paperclip usable as the visible control plane by continuously feeding it from the file ledger and producing a single main-session view.

This is the right "one step back, ten steps forward" infrastructure move.

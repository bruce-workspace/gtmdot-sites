# Paperclip proactive control-plane plan

Date: 2026-05-21
Owner: Codex / GTMDot quarterback
Status: recommended implementation plan; no CRM/send/deploy mutations performed

## Executive take

Jesse is right: GTMDot will not scale if he has to act as the clipboard between
Codex sessions, Bruce, R1VS, Paperclip, the CRM, Slack, Telegram, Poplar, and
Resend. Paperclip should become the visible control plane and dispatcher, not
just a manually checked issue board.

The current gap is not that Paperclip is the wrong tool. The gap is that GTMDot
is using only the visible task-board portion of Paperclip while the work still
lives in separate chat/session ledgers. Paperclip needs a thin GTMDot-specific
bridge that continuously reads the real operating state, writes durable lane
inboxes/outboxes, and marks exact next actions.

## Current verified state

- Paperclip API health: `ok` at `http://127.0.0.1:3199/api/health`.
- Paperclip dashboard: `http://127.0.0.1:3199/GTM/dashboard`.
- Current Paperclip issue count: 24.
- Current issue states: 16 `todo`, 5 `done`, 3 `blocked`.
- Current assigned Paperclip agents: 0.
- Current active/running Paperclip agents: 0.
- Dispatcher Bridge B1.0 exists and runs dry-run only:
  `/Users/bruce/.openclaw/workspace/gtmdot-sites/workers/gtmdot_dispatcher_bridge.py`
- Latest dispatcher digest generated:
  `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/dispatcher/digests/2026-05-21-0750-dispatcher-digest.md`
- Current dispatcher output shows stale lane status files across all major
  lanes. This is expected because lanes are still session-driven instead of
  Paperclip-driven.

## The core problem

Paperclip currently records what the work *should* be, but it does not yet
reliably do the following:

- Wake up on its own.
- Notice lane/session artifacts changed.
- Notice CRM/Poplar/Resend state changed.
- Tell the correct lane what changed.
- Require an acknowledgement.
- Detect that no one acknowledged.
- Update the board with machine-readable next action.
- Escalate only the exact Jesse decision needed.

Until those exist, Jesse remains the transport layer.

## Target operating model

Paperclip becomes the visible control plane. Git/message files remain the
durable audit ledger. CRM/Supabase remains prospect truth. Provider APIs remain
provider truth. Telegram/Slack remain notification mirrors.

Paperclip should answer four questions at all times:

1. What is the next action?
2. Who owns it?
3. What artifact proves it?
4. What, exactly, needs Jesse approval?

If Paperclip cannot answer those four questions, it should mark the issue as
`needs-triage` rather than silently staying stale.

## B1.1 - Reliability foundation

Goal: Paperclip is up whenever Jesse opens the dashboard.

Implement:

- A launchd user service for Paperclip using the known start command:
  `PAPERCLIP_HOME=/Users/bruce/.openclaw/workspace/paperclip-sandbox-home`
  `PAPERCLIP_INSTANCE_ID=gtmdot-sandbox`
  `PORT=3199`
  `PAPERCLIP_OPEN_ON_LISTEN=false`
- A health-check script that verifies:
  - `GET /api/health` returns `status: ok`.
  - latest backup exists and is recent.
  - dashboard endpoint responds.
  - embedded Postgres process is healthy.
- A local watchdog artifact:
  `messages/status/paperclip-runtime-latest.md`
- A daily backup manifest:
  `paperclip-sandbox/artifacts/paperclip-backup-manifest.md`

Done condition:

- Reboot or process death no longer leaves Paperclip unreachable.
- If Paperclip is down, the health file says why and how to restart.

## B1.2 - Dispatcher loop

Goal: the dispatcher runs without Jesse asking.

Implement:

- Promote `gtmdot_dispatcher_bridge.py` from manual dry-run to scheduled dry-run.
- Run every 15 minutes while board clearing is active.
- Inputs:
  - Paperclip issues and dashboard.
  - `messages/status/*latest.md`.
  - recent `gtmdot-sites/messages/*.md` artifacts.
  - CRM read-only stage/channel summaries.
  - Poplar read-only postcard states.
  - Resend/Gmail read-only email/reply states, when available.
- Outputs:
  - one quarterback digest.
  - lane-specific outbox files.
  - dispatcher state JSON.
  - stale-lane warnings.

Done condition:

- Jesse can open one digest and know what happened, what changed, and what to
  approve next.

## B1.3 - Lane inbox/outbox protocol

Goal: every lane knows what to read and how to report back.

Create these folders:

- `messages/dispatcher/inbox/<lane>/`
- `messages/dispatcher/outbox/<lane>/`
- `messages/dispatcher/acks/<lane>/`

Each lane outbox item should have:

- Paperclip issue ID.
- source artifact path.
- exact requested action.
- allowed actions.
- prohibited actions.
- required return path.
- acknowledgement deadline.

Each lane acknowledgement should have:

- issue ID.
- action accepted or rejected.
- current blocker.
- artifact produced.
- next owner.
- actions not performed.

Done condition:

- The main coordinator no longer needs to paste freeform updates between lanes;
  each lane reads an outbox file and writes an ack/return file.

## B1.4 - Safe Paperclip mutator

Goal: Paperclip state updates from artifacts, but only through an idempotent
guarded script.

Implement a script such as:

`workers/paperclip_safe_update.py`

Allowed mutations in this phase:

- Add issue comment linking a new artifact.
- Update issue status only when a strict done condition matches.
- Add/remove labels such as `needs-jesse`, `stale-lane`, `provider-exception`,
  `ready-for-review`, `blocked-current`, `blocked-stale`.
- Set assignee/owner metadata if Paperclip supports it cleanly.

Still prohibited by default:

- CRM writes.
- Deploys.
- Sends.
- Prospect/customer contact.
- Git pushes.
- DNS/domain/hosting/billing/Stripe.

Done condition:

- Paperclip stops drifting from the file ledger.
- Every mutation is reproducible from a source artifact.
- Dry-run mode remains default; apply mode requires explicit approval.

## B1.5 - Provider state watchers

Goal: channel truth no longer depends on Jesse clicking around the CRM.

Implement read-only watchers:

- Poplar watcher:
  - postcard submitted/production/in_transit/delivered/exception/returned.
  - provider error reason when exposed.
  - invalid recipient fields such as Poplar first-name length.
- Resend watcher:
  - email sent/delivered/bounced.
  - sequence number.
  - suppression/bounce flags.
- Gmail/Workspace watcher:
  - replies to `hello@gtmdot.com`.
  - untriaged replies.
  - replied-but-sequence-active mismatch.
- CRM read-only watcher:
  - stage.
  - channel-state fields/events.
  - open/stale notes.
  - missing email/address/hero/screenshot flags.

Each watcher writes an evidence packet, then dispatcher decides whether a
Paperclip issue/comment should be updated.

Done condition:

- Paperclip can say "these postcards are in transit," "these exceptions need
  action," and "these email sequences are unsafe to continue" without Jesse
  manually checking each provider.

## B1.6 - Active agents, carefully

Goal: use Paperclip's agent model where it adds leverage, not where it creates
noise.

Do not start with broad autonomous agents. Start with narrow agents/routines:

- `runtime-watchdog`: keeps Paperclip health/backup status fresh.
- `dispatcher`: reads state and writes digests/outbox.
- `provider-watchers`: read-only Poplar/Resend/Gmail/CRM snapshots.
- `bruce-enrichment-router`: creates Bruce collect-request packets from
  current blockers, but does not contact prospects or write CRM.

Do not yet assign Paperclip agents direct authority to:

- send outreach,
- deploy,
- write CRM,
- mutate prospect truth,
- approve sites,
- approve postcards,
- approve emails.

Done condition:

- Paperclip dashboard shows active agents/routines for monitoring and routing,
  while sensitive business actions remain Jesse-approved.

## B1.7 - CRM v2 integration

Goal: the CRM shows Paperclip and channel-state truth in the place Jesse is
already working.

CRM v2 should surface:

- Paperclip parent issue link.
- current blocker label.
- next action.
- latest artifact.
- stale note status.
- postcard provider state.
- email sequence/reply state.
- whether the current button click would mutate CRM, send Poplar, send Resend,
  deploy, or only preview.

Done condition:

- Jesse can open a prospect and know whether the next click is safe, blocked,
  or needs a current artifact.

## Proposed immediate issue sequence

Create or update Paperclip issues:

- `GTM-25` - Paperclip runtime reliability service.
- `GTM-26` - Dispatcher loop B1.2 scheduled dry-run.
- `GTM-27` - Lane inbox/outbox acknowledgement protocol.
- `GTM-28` - Safe Paperclip mutator, dry-run first.
- `GTM-29` - Provider state watchers: Poplar + Resend + Gmail + CRM read-only.
- `GTM-30` - CRM v2 Paperclip/channel-state integration contract.

If issue creation is too much overhead, create these as children under existing
`GTM-6` Paperclip Recovery / v2 rebuilt from file ledger.

## Recommended next action

Implement `GTM-25` first: Paperclip runtime reliability. It is the foundation.
If Paperclip is not always reachable, it cannot be trusted as the control plane.

Then implement `GTM-26`: scheduled dispatcher dry-run. That immediately reduces
Jesse's copy/paste burden without granting it dangerous permissions.

## Non-goals for the next pass

- Do not rewrite the CRM around Paperclip yet.
- Do not let Paperclip auto-send anything.
- Do not let Paperclip auto-deploy anything.
- Do not rely on Telegram as the canonical transport.
- Do not create broad "do everything" agents.

## Actions not performed

- No CRM/Supabase writes.
- No Paperclip mutations.
- No deploys.
- No Poplar/Resend/SMS sends.
- No prospect/customer contact.
- No git pushes.
- No production site edits.
- No DNS/domain/hosting/billing/Stripe actions.

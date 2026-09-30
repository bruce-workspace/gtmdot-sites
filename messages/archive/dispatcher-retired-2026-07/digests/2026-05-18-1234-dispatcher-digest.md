# GTMDot Dispatcher Digest - 2026-05-18T12:34:45-04:00

Mode: B1.0 dry-run only
Authority: Git/message files + Paperclip are canonical; Slack/Telegram are notification mirrors.

## Executive State
- Paperclip health: error: urllib: <urlopen error [Errno 1] Operation not permitted>; curl exit 7: curl: (7) Failed to connect to 127.0.0.1 port 3199 after 0 ms: Couldn't connect to server
- Paperclip dashboard: http://127.0.0.1:3199/GTM/dashboard
- Paperclip task counts: unavailable
- Paperclip agent counts: unavailable
- Local issue counts: {}
- Approval queue items found: 12
- Recent artifacts scanned: 18

## Recommended Next 3 Moves
1. Decide InTire Mobile Tire Shop: approve/hold stage movement and channels now that GTM-14 technical readiness passed.
2. Resolve Harrison Poplar failure: capture exact provider error if possible, or approve one normalized-address retry with stop-on-error language.
3. Keep CRM v2 lab aligned with channel-state truth, stale-note handling, Paperclip links, and provider error visibility.

## Approval Queue
- pre-build / GTM-1, GTM-4, GTM-6, GTM-7, GTM-11, GTM-12, GTM-13, GTM-15, GTM-16, GTM-17, GTM-18, GTM-19, GTM-20, GTM-22, GTM-23: Mbanugo unresolved flags remain: owner name, direct email, CRM field reconciliation, GBP URL mismatch, TLS/source risk, Chosen Tires/Roadside Assistance alternate-branding risk, and identity-flag copy approval.
- post-build / GTM-3, GTM-11, GTM-12, GTM-13, GTM-14: Approve or hold InTire move toward `outreach_staged`.
- post-build / GTM-3, GTM-11, GTM-12, GTM-13, GTM-14: Approve channels for InTire: postcard, email, or both.
- post-build / GTM-3, GTM-11, GTM-12, GTM-13, GTM-14: Separately approve any Poplar/Resend action if/when ready.
- post-build / GTM-3, GTM-11, GTM-12, GTM-13, GTM-14: Ask Jesse/coordinator to decide whether InTire should move to `outreach_staged`
- post-build / GTM-3, GTM-11, GTM-12, GTM-13, GTM-14: and which channels are approved. If approved, handle stage movement and outreach
- post-build / GTM-3, GTM-11, GTM-12, GTM-13, GTM-14: Jesse approval still required before CRM stage move, postcard submit, or email
- outreach / GTM-12: Decide whether to require exact UI/network provider error before any retry.
- outreach / GTM-12: If ready despite missing provider body, approve one normalized-address resubmit attempt with explicit stop-on-error language.
- outreach / GTM-12: Separately approve any CRM address normalization or helper/code change if desired.
- outreach / GTM-12: Capture the exact Poplar error from the browser/network response if still available. If not available and Jesse accepts the risk, request the explicit approval text in the artifact for one normalized-address retry using `3695 Cascade Rd Ste 6250`, with instructions to stop immediately and capture provider status/body on any new error.
- outreach / GTM-12: No fresh approval exists to retry/submit.

## Lane Status
### Quarterback / Main GTMDot
- Status file: `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/status/quarterback-latest.md`
- Updated: 2026-05-18T12:34:05-04:00
- Paperclip IDs: GTM-1, GTM-2, GTM-3, GTM-4, GTM-5, GTM-6, GTM-7, GTM-8, GTM-9, GTM-11, GTM-12, GTM-13, GTM-14, GTM-15, GTM-16, GTM-17, GTM-18, GTM-19, GTM-20, GTM-22, GTM-23, GTM-24
- Summary: Dispatcher B1.0 generated a dry-run digest at `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/dispatcher/digests/2026-05-18-1234-dispatcher-digest.md`. No Paperclip, CRM, deploy, send, contact, git, or production mutations were performed. Use the dispatcher digest approval queue and lane outbox files to route the next board-clearing action without manual re-summarization.
- Blockers: - Quarterback / Main GTMDot: stale status file (36.3h old) - GTMDot Platform / CRM v2: stale status file (28.1h old) - Experiments: stale status file (62.3h old)
- Decisions: - quarterback / GTM-1, GTM-2, GTM-3, GTM-4, GTM-5, GTM-6, GTM-7, GTM-8, GTM-9, GTM-11, GTM-12, GTM-13, GTM-14, GTM-15, GTM-16, GTM-17, GTM-18, GTM-22, GTM-23, GTM-24: Continue distributing rollout briefs/acknowledgements to active sessions. Outreach board-clearing findings now show a critical blocker: `GTM-24` must resolve canonical reply-to and inbound r...
- Next action: Use the dispatcher digest approval queue and lane outbox files to route the next board-clearing action without manual re-summarization.

### Pre-Build Coordination
- Status file: `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/status/pre-build-coordination-latest.md`
- Updated: 2026-05-17T18:49:19Z
- Paperclip IDs: GTM-1, GTM-4, GTM-6, GTM-7, GTM-11, GTM-12, GTM-13, GTM-15, GTM-16, GTM-17, GTM-18, GTM-19, GTM-20, GTM-22, GTM-23
- Summary: Read the Paperclip v2 channel brief and the required rollout docs: - `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/2026-05-16-codex-to-lanes-paperclip-v2-channel-brief.md` - `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/2026-05-16-codex-paperclip-v2-rollout-master-brief.md` - `/Users/bruce/.openc... Hold Pre-Build at ready state while Outreach/Post-Build clear the close-to-send backlog. If Jesse prioritizes Pre-Build, start with `GTM-15` by converting `/Users/bruce/.openclaw/workspace/paperclip-sandbox/artifacts/pre-build-coordination-template-2026-05-16.md` into the reusable Paperclip issue/artifact sequence,...
- Blockers: - Board clearing has priority over new pre-build work. - Browserbase default-enrichment plan exists, but a reusable GTMDot Browserbase evidence runner is not yet implemented as a standard lane tool. - Existing enrichment dispatcher has known source-of-truth limitations: it checks canonical `gtmdot-sites/sites/<slug>` and can miss older deploy-target-only...
- Decisions: - Whether `GTM-15` through `GTM-18` should be worked now or held until board-clearing issues `GTM-7`, `GTM-11`, `GTM-12`, and `GTM-13` are clear. - Whether the prospective pre-build template should be promoted into Paperclip v2 issue descriptions as the standing issue tree. - Whether to implement the Browserbase evidence runner now or defer. - Whether to...
- Next action: Hold Pre-Build at ready state while Outreach/Post-Build clear the close-to-send backlog. If Jesse prioritizes Pre-Build, start with `GTM-15` by converting `/Users/bruce/.openclaw/workspace/paperclip-sandbox/artifacts/pre-build-coordination-template-2026-05-16.md` into the reusable Paperclip issue/artifact sequence, then add stale-note handling to the sour...

### Post-Build Operations
- Status file: `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/status/post-build-operations-latest.md`
- Updated: 2026-05-18T06:55:00-04:00
- Paperclip IDs: GTM-3, GTM-11, GTM-12, GTM-13, GTM-14
- Summary: InTire Mobile Tire Shop repair is complete. GTM-14 technical readiness passed. InTire is ready for Jesse's stage/outreach decision, but no CRM movement or outreach action has been performed. Ask Jesse/coordinator to decide whether InTire should move to `outreach_staged` and which channels are approved. If approved, handle stage movement and outreach as separate explicit actions.
- Blockers: - InTire: no hard technical blockers remain after repair. - InTire: email preview UI endpoint warning remains from the legacy gate (`HTTP 404`), but the gate reports actual send via `/actions` still works. - Jesse approval still required before CRM stage move, postcard submit, or email trigger.
- Decisions: - Approve or hold InTire move toward `outreach_staged`. - Approve channels for InTire: postcard, email, or both. - Separately approve any Poplar/Resend action if/when ready.
- Next action: Ask Jesse/coordinator to decide whether InTire should move to `outreach_staged` and which channels are approved. If approved, handle stage movement and outreach as separate explicit actions.

### Outreach Operations
- Status file: `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/status/outreach-operations-latest.md`
- Updated: 2026-05-18T06:48:00-04:00
- Paperclip IDs: GTM-12
- Summary: - Harrison remains `outreach_staged`, `postcardStatus: not_submitted`, with no postcard outreach events. - Read-only Poplar campaign search across 37 mailings / 8 pages found no Harrison match by `HARR2423`, `harrison-sons-electrical`, `CASCADE`, `6250`, or Harrison name. - Available evidence indicates no Poplar mai... Capture the exact Poplar error from the browser/network response if still available. If not available and Jesse accepts the risk, request the explicit approval text in the artifact for one normalized-address retry using `3695 Cascade Rd Ste 6250`, with instructions to stop immediately and capture provider status/bod...
- Blockers: - Exact Poplar error body/status remains uncaptured. - No fresh approval exists to retry/submit. - Current CRM helper does not expose `address_2`; best retry payload may require either a normalized single-line CRM address or helper support for address line 2.
- Decisions: - Decide whether to require exact UI/network provider error before any retry. - If ready despite missing provider body, approve one normalized-address resubmit attempt with explicit stop-on-error language. - Separately approve any CRM address normalization or helper/code change if desired.
- Next action: Capture the exact Poplar error from the browser/network response if still available. If not available and Jesse accepts the risk, request the explicit approval text in the artifact for one normalized-address retry using `3695 Cascade Rd Ste 6250`, with instructions to stop immediately and capture provider status/body on any new error.

### GTMDot Platform / CRM v2
- Status file: `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/status/gtmdot-platform-latest.md`
- Updated: 2026-05-17T08:30:24-04:00 WARNING: stale status file (28.1h old).
- Paperclip IDs: GTM-5, GTM-19, GTM-20, GTM-24
- Summary: CRM v2 remains lab-only and is not ready to test or replace the live CRM. HeroUI Pro is installed and verified in `/Users/bruce/.openclaw/workspace/brucecom-v3`; `@heroui-pro/react/css` builds successfully. Platform direction is to preserve current stage/API fields for Outreach now, add reply/channel state as additi... Continue CRM v2 lab route planning/build against the existing CRM API, with the prospect command sheet and Outreach Operations view designed around channel-state cards, untriaged replies, bounced emails, replied-but-sequence-active mismatches, postcard provider exceptions, Paperclip blockers, and exact next action.
- Blockers: - Existing CRM stage alone does not express channel truth. - `outreach_sent` is currently too broad for operational clarity. - Inbound reply monitoring to `hello@gtmdot.com` is not yet proven end-to-end. - Current CRM does not yet prove that a prospect reply becomes CRM state and pauses future email follow-ups. - Poplar provider state may be ahead of CRM...
- Decisions: - Whether CRM v2 should remain lab-only until board clearing is stable. - Whether `GTM-24` may proceed from planning to code changes. - Whether reply storage should remain snippet/metadata-only or include full reply bodies. - Whether mailbox/thread links are preferred as the full-content source of truth.
- Next action: Continue CRM v2 lab route planning/build against the existing CRM API, with the prospect command sheet and Outreach Operations view designed around channel-state cards, untriaged replies, bounced emails, replied-but-sequence-active mismatches, postcard provider exceptions, Paperclip blockers, and exact next action.

### Experiments
- Status file: `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/status/experiments-latest.md`
- Updated: 2026-05-16T02:18:43Z WARNING: stale status file (62.3h old).
- Paperclip IDs: none detected
- Summary: Placeholder created by quarterback session. Experiments should remain isolated from production CRM/outreach/deploy unless Jesse explicitly graduates a feature. Create an experiments inventory with status, vendor/API dependencies, production risk, and graduation criteria.
- Blockers: - Experimental work must not consume board-clearing bandwidth unless it directly supports revenue or support.
- Decisions: - Which experiments are active, paused, or archived.
- Next action: Create an experiments inventory with status, vendor/API dependencies, production risk, and graduation criteria.

## Recent Artifacts
- `2026-05-18-dispatcher-bridge-b1-scope.md` (GTM-2, GTM-3, GTM-4, GTM-5, GTM-6, GTM-7, GTM-8, GTM-9, GTM-11, GTM-12, GTM-13, GTM-14, GTM-15, GTM-16, GTM-17, GTM-18, GTM-24, 2026-05-18T06:55:56-04:00): GTMDot Dispatcher Bridge B1 Scope
- `2026-05-18-gtm-13-intire-postbuild-repair-complete.md` (GTM-3, GTM-13, GTM-14, 2026-05-18T06:53:16-04:00): InTire Mobile Tire Shop - Post-Build Repair Complete
- `2026-05-18-harrison-poplar-failure-investigation.md` (no GTM ID, 2026-05-18T06:49:41-04:00): Harrison & Sons Electrical - Poplar Failure Investigation
- `2026-05-18T103500Z-bruce-status-no-work-this-run.md` (no GTM ID, 2026-05-18T06:36:05-04:00): No pending collect-request.md files found in sites/*/collect-request.md. All existing requests are archived.
- `20260518055624-bruce-status-no-work-this-run.md` (no GTM ID, 2026-05-18T01:56:24-04:00): No pending collect-request.md files found in this run.
- `2026-05-17-gtm-12-harrison-sons-final-live-packet.md` (GTM-3, GTM-12, 2026-05-17T14:49:53-04:00): GTM-12 - Harrison & Sons Electrical Final Live Packet
- `2026-05-17-harrison-sons-postcard-only-final-action.md` (GTM-12, 2026-05-17T14:49:48-04:00): Harrison & Sons Postcard-Only Final Action Prep
- `2026-05-17-1849-jesse-note-blocker-staleness-policy.md` (no GTM ID, 2026-05-17T14:49:41-04:00): GTMDot Note / Blocker Staleness Policy
- `2026-05-16-post-build-gate-contract-gtm-14.md` (GTM-3, GTM-11, GTM-12, GTM-13, GTM-14, 2026-05-17T14:49:33-04:00): Post-Build Operations Gate Contract
- `2026-05-17-gtm-13-intire-staging-readiness-predeploy.md` (GTM-3, GTM-13, GTM-14, 2026-05-17T14:43:41-04:00): InTire Mobile Tire Shop - Staging Readiness Pre-Deploy Packet
- `2026-05-17-gtm-13-qa-approved-batch-preflight.md` (GTM-3, GTM-13, 2026-05-17T14:29:56-04:00): GTM-13 - QA-Approved Batch Preflight
- `2026-05-17-poplar-exceptions-and-gtm24-readiness.md` (GTM-7, GTM-24, 2026-05-17T14:28:48-04:00): Poplar Exceptions And GTM-24 Readiness Follow-Up
- `2026-05-17-bruce-crm-v2-outreach-paperclip-bridge.md` (no GTM ID, 2026-05-17T09:07:27-04:00): Accidental GTM24 / Paperclip Context Note
- `2026-05-17-outreach-gtm-24-phase-1-to-main-summary.md` (GTM-24, 2026-05-17T08:58:03-04:00): Outreach GTM-24 Phase 1 Handoff To Main GTMDot Coordinator
- `2026-05-17-gtm-24-phase-1-reply-to-update.md` (GTM-24, 2026-05-17T08:58:03-04:00): GTM-24 Phase 1 Reply-To Update
- `2026-05-17-platform-crm-v2-outreach-reply-state-direction.md` (GTM-5, GTM-19, GTM-20, GTM-24, 2026-05-17T08:31:56-04:00): GTMDot Platform: CRM v2 Outreach Reply And Channel-State Direction
- `2026-05-17-bruce-status-no-work-this-run.md` (no GTM ID, 2026-05-17T04:14:52-04:00): No pending collect-request.md files found in sites/*/ for processing.
- `2026-05-17-gtm-24-crm-v2-reply-monitoring-alignment-brief.md` (GTM-24, 2026-05-17T00:48:37-04:00): GTM-24 / CRM v2 Reply Monitoring Alignment Brief

## Paperclip Health
- API base: http://127.0.0.1:3199
- Health: error: urllib: <urlopen error [Errno 1] Operation not permitted>; curl exit 7: curl: (7) Failed to connect to 127.0.0.1 port 3199 after 0 ms: Couldn't connect to server
- Dashboard read error: urllib: <urlopen error [Errno 1] Operation not permitted>; curl exit 7: curl: (7) Failed to connect to 127.0.0.1 port 3199 after 0 ms: Couldn't connect to server
- Issue read error: urllib: <urlopen error [Errno 1] Operation not permitted>; curl exit 7: curl: (7) Failed to connect to 127.0.0.1 port 3199 after 0 ms: Couldn't connect to server
- Latest backup: `/Users/bruce/.openclaw/workspace/paperclip-sandbox-home/instances/gtmdot-sandbox/data/backups/paperclip-20260518-123327.sql.gz` (60314 bytes, 0.02h old).

## Guardrails
- No CRM/Supabase writes performed.
- No Paperclip mutations performed.
- No deploys performed.
- No Poplar/Resend/SMS sends performed.
- No prospect/customer contact performed.
- No git pushes performed.
- No production site edits performed.

# GTMDot Dispatcher Digest - 2026-05-23T10:02:23-07:00

Mode: B1.0 dry-run only
Authority: Git/message files + Paperclip are canonical; Slack/Telegram are notification mirrors.

## Executive State
- Paperclip health: ok
- Paperclip read source: api
- Paperclip dashboard: http://127.0.0.1:3199/GTM/dashboard
- Paperclip task counts: {"blocked": 3, "done": 5, "inProgress": 0, "open": 19}
- Paperclip agent counts: {"active": 0, "error": 0, "paused": 0, "running": 0}
- Local issue counts: {"blocked": 3, "done": 5, "todo": 16}
- Approval queue items found: 4
- Recent artifacts scanned: 14

## Recommended Next 3 Moves
1. Resolve Harrison Poplar failure: capture exact provider error if possible, or approve one normalized-address retry with stop-on-error language.
2. Answer approval item from pre-build: Mbanugo unresolved flags remain: owner name, direct email, CRM field reconciliation, GBP URL mismatch, TLS/source risk, Chosen Tires/Roadside Assistance alternate-branding risk, and identity-flag copy approval.
3. Answer approval item from outreach: postcards, prepare Cityboys visual QA before any Cityboys approval, and ask

## Approval Queue
- pre-build / GTM-1, GTM-4, GTM-6, GTM-15, GTM-16, GTM-17, GTM-18, GTM-19, GTM-20, GTM-22, GTM-23: Mbanugo unresolved flags remain: owner name, direct email, CRM field reconciliation, GBP URL mismatch, TLS/source risk, Chosen Tires/Roadside Assistance alternate-branding risk, and identity-flag copy approval.
- outreach / GTM-9, GTM-24: postcards, prepare Cityboys visual QA before any Cityboys approval, and ask
- outreach / GTM-9, GTM-24: Jesse to approve one of two InTire paths: safest pause before
- outreach / GTM-9, GTM-24: `2026-05-25T17:00:03.814+00:00`, or explicit manual-risk approval to let Email 3

## Lane Status
### Quarterback / Main GTMDot
- Status file: `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/status/quarterback-latest.md`
- Updated: 2026-05-23T12:53:03-04:00
- Paperclip IDs: GTM-1, GTM-2, GTM-3, GTM-4, GTM-5, GTM-6, GTM-7, GTM-8, GTM-9, GTM-11, GTM-12, GTM-13, GTM-14, GTM-15, GTM-16, GTM-17, GTM-18, GTM-19, GTM-20, GTM-22, GTM-23, GTM-24
- Summary: Remote-week roadmap and latest quarterback status were reviewed. Pre-Build was kept subordinate to board clearing, and Jesse/coordinator accepted the `GTM-15`, `GTM-16`, and `GTM-17` file-ledger packet as remote-week infrastructure state. No Paperclip mutation is needed right now. No Paperclip, CRM, deploy, send, co... Use the dispatcher digest approval queue and lane outbox files to route the next board-clearing action without manual re-summarization. Recommended next revenue action remains Harrison/InTire/send-packet board clearing. Pre-Build should hold unless spare bandwidth is used only for template refinement, Browserbase ev...
- Blockers: - Closest-to-revenue work remains board clearing, not Pre-Build: Harrison verification/retry state, InTire stage/channel approval, and send packets for QA-approved prospects. - Pre-Build is no longer stale after the GTM-15/GTM-16/GTM-17 infrastructure update, but it remains subordinate to board clearing.
- Decisions: - pre-build / GTM-1, GTM-4, GTM-6, GTM-7, GTM-11, GTM-12, GTM-13, GTM-15, GTM-16, GTM-17, GTM-18, GTM-19, GTM-20, GTM-22, GTM-23: Mbanugo unresolved flags remain: owner name, direct email, CRM field reconciliation, GBP URL mismatch, TLS/source risk, Chosen Tires/Roadside Assistance alternate-branding risk, and identity-flag copy approval. - pre-build / GT...
- Next action: Use the dispatcher digest approval queue and lane outbox files to route the next board-clearing action without manual re-summarization. Recommended next revenue action remains Harrison/InTire/send-packet board clearing. Pre-Build should hold unless spare bandwidth is used only for template refinement, Browserbase evidence usability, or CRM v2 intake-routi...

### Pre-Build Coordination
- Status file: `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/status/pre-build-coordination-latest.md`
- Updated: 2026-05-23T12:53:03-04:00
- Paperclip IDs: GTM-1, GTM-4, GTM-6, GTM-15, GTM-16, GTM-17, GTM-18, GTM-19, GTM-20, GTM-22, GTM-23
- Summary: Remote-week roadmap reviewed. Pre-Build remains subordinate to board clearing. Jesse accepted `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/2026-05-23-remote-week-prebuild-infra-gtm15-17.md` as remote-week infrastructure state for `GTM-15`, `GTM-16`, and `GTM-17`. No Paperclip mutation is needed right now;... Hold Pre-Build at ready state while Outreach/Post-Build clear the close-to-send backlog. If spare bandwidth exists, only refine the reusable packet templates, improve Browserbase evidence output for Post-Build/Bruce/R1VS consumption, or document CRM v2 routing fields needed for new prospect intake. Do not start Mban...
- Blockers: - Board clearing has priority over new pre-build work. - Browserbase default-enrichment plan exists, but a reusable GTMDot Browserbase evidence runner is not yet implemented as a standard lane tool. - Existing enrichment dispatcher has known source-of-truth limitations: it checks canonical `gtmdot-sites/sites/<slug>` and can miss older deploy-target-only...
- Decisions: - Whether future spare-bandwidth work should refine the reusable packet templates, improve Browserbase output for Post-Build/Bruce/R1VS, or document CRM v2 routing fields for new prospect intake. - Whether the file-ledger packet should later be mirrored into Paperclip comments. - Whether to implement the Browserbase evidence runner later or defer. - Wheth...
- Next action: Hold Pre-Build at ready state while Outreach/Post-Build clear the close-to-send backlog. If spare bandwidth exists, only refine the reusable packet templates, improve Browserbase evidence output for Post-Build/Bruce/R1VS consumption, or document CRM v2 routing fields needed for new prospect intake. Do not start Mbanugo, new prospect builds, Browserbase ba...

### Post-Build Operations
- Status file: `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/status/post-build-operations-latest.md`
- Updated: 2026-05-23T12:58:00-04:00
- Paperclip IDs: none detected
- Summary: No summary extracted.

### Outreach Operations
- Status file: `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/status/outreach-operations-latest.md`
- Updated: 2026-05-23T12:58:00-04:00
- Paperclip IDs: GTM-9, GTM-24
- Summary: - Jesse approved bounded postcard-only execution for `smartwire-solutions`, `dream-steam`, and `handy-dandy-atlanta`. - All three passed live gates immediately before send and were submitted through the CRM action endpoint with `dryRun: false`. - New Poplar order IDs: - `smartwire-solutions`: `3a7ae7b1-9bef-4f90-92c... Coordinator should monitor provider progression for the three newly submitted postcards, prepare Cityboys visual QA before any Cityboys approval, and ask Jesse to approve one of two InTire paths: safest pause before `2026-05-25T17:00:03.814+00:00`, or explicit manual-risk approval to let Email 3 proceed while reply...
- Next action: Coordinator should monitor provider progression for the three newly submitted postcards, prepare Cityboys visual QA before any Cityboys approval, and ask Jesse to approve one of two InTire paths: safest pause before `2026-05-25T17:00:03.814+00:00`, or explicit manual-risk approval to let Email 3 proceed while reply monitoring remains unproven.

### GTMDot Platform / CRM v2
- Status file: `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/status/gtmdot-platform-latest.md`
- Updated: 2026-05-23T12:15:00-04:00
- Paperclip IDs: none detected
- Summary: No summary extracted.

### Experiments
- Status file: `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/status/experiments-latest.md`
- Updated: 2026-05-23T12:52:16-04:00
- Paperclip IDs: none detected
- Summary: Keep experimental GTMDot features isolated from production while clarifying what is real, what is only dry-run proven, and what can be advanced safely during Jesse's away-mode week.

## Recent Artifacts
- `2026-05-23-intire-email-3-decision-packet.md` (GTM-9, GTM-24, 2026-05-23T09:57:55-07:00): InTire Email 3 Decision Packet
- `2026-05-23-cityboys-send-readiness-hold-packet.md` (no GTM ID, 2026-05-23T09:57:34-07:00): Cityboys Send-Readiness Hold Packet - 2026-05-23
- `2026-05-23-approved-postcard-batch-complete.md` (no GTM ID, 2026-05-23T09:57:34-07:00): Approved Postcard Batch Complete - 2026-05-23
- `2026-05-23-crm-v2-additive-field-api-contract.md` (no GTM ID, 2026-05-23T09:54:30-07:00): CRM v2 Additive Field/API Contract Draft
- `2026-05-23-outreach-channel-truth-and-decision-queue.md` (no GTM ID, 2026-05-23T09:50:29-07:00): Outreach Channel Truth And Decision Queue
- `2026-05-23-post-build-send-readiness-and-blocker-packets.md` (no GTM ID, 2026-05-23T09:50:06-07:00): Post-Build Send-Readiness + Blocker Packets - 2026-05-23
- `2026-05-23-remote-week-prebuild-infra-gtm15-17.md` (GTM-15, GTM-16, GTM-17, 2026-05-23T09:49:36-07:00): Remote-Week Pre-Build Infrastructure Packet - GTM-15/GTM-16/GTM-17
- `2026-05-23-experiments-ai-receptionist-local-graduation-packet.md` (no GTM ID, 2026-05-23T09:47:42-07:00): Experiments - AI Receptionist Local Graduation Packet
- `2026-05-23-away-mode-coordinator-roadmap.md` (GTM-14, 2026-05-23T09:41:45-07:00): GTMDot Away-Mode Coordinator Roadmap - 2026-05-23
- `2026-05-23-outreach-away-mode-handoff.md` (no GTM ID, 2026-05-23T09:35:32-07:00): Outreach Operations Away-Mode Handoff
- `2026-05-23-codex-telegram-bridge-diagnostics-implementation-record.md` (no GTM ID, 2026-05-23T07:39:14-07:00): Codex Telegram Bridge Diagnostics Implementation Record
- `2026-05-23-telegram-bridge-health-runbook.md` (no GTM ID, 2026-05-23T07:38:43-07:00): Telegram Bridge Health Runbook
- `2026-05-22-harrison-poplar-public-crm-stale-route.md` (no GTM ID, 2026-05-22T19:55:54-07:00): Harrison Poplar Submit Error - Public CRM Stale Route
- `2026-05-22-harrison-poplar-submit-incident-followup.md` (GTM-12, 2026-05-22T03:48:20-07:00): Harrison & Sons Poplar Submit Incident Follow-Up

## Paperclip Health
- API base: http://127.0.0.1:3199
- Read source: api
- Health: ok
- Latest backup: `/Users/bruce/.openclaw/workspace/paperclip-sandbox-home/instances/gtmdot-sandbox/data/backups/paperclip-20260523-093015.sql.gz` (81668 bytes, 0.54h old).

## Guardrails
- No CRM/Supabase writes performed.
- No Paperclip mutations performed.
- No deploys performed.
- No Poplar/Resend/SMS sends performed.
- No prospect/customer contact performed.
- No git pushes performed.
- No production site edits performed.

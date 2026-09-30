# GTMDot Dispatcher Digest - 2026-06-02T08:34:07-07:00

Mode: B1.0 dry-run only
Authority: Git/message files + Paperclip are canonical; Slack/Telegram are notification mirrors.

## Executive State
- Paperclip health: ok
- Paperclip read source: api
- Paperclip dashboard: http://127.0.0.1:3199/GTM/dashboard
- Paperclip task counts: {"blocked": 3, "done": 5, "inProgress": 0, "open": 19}
- Paperclip agent counts: {"active": 0, "error": 0, "paused": 0, "running": 0}
- Local issue counts: {"blocked": 3, "done": 5, "todo": 16}
- Approval queue items found: 7
- Recent artifacts scanned: 24

## Recommended Next 3 Moves
1. Resolve Harrison Poplar failure: capture exact provider error if possible, or approve one normalized-address retry with stop-on-error language.
2. Answer approval item from pre-build: Mbanugo unresolved flags remain: owner name, direct email, CRM field reconciliation, GBP URL mismatch, TLS/source risk, Chosen Tires/Roadside Assistance alternate-branding risk, and identity-flag copy approval.
3. Answer approval item from outreach: not retry without fresh approval, monitor Bravo/Browning provider progression,

## Approval Queue
- pre-build / GTM-1, GTM-4, GTM-6, GTM-15, GTM-16, GTM-17, GTM-18, GTM-19, GTM-20, GTM-22, GTM-23: Mbanugo unresolved flags remain: owner name, direct email, CRM field reconciliation, GBP URL mismatch, TLS/source risk, Chosen Tires/Roadside Assistance alternate-branding risk, and identity-flag copy approval.
- outreach / GTM-9, GTM-24: not retry without fresh approval, monitor Bravo/Browning provider progression,
- outreach / GTM-9, GTM-24: and decide whether to approve a narrow CRM backfill for the three prospects that
- outreach / GTM-9, GTM-24: have postcard events but remain stage `needs_approval`. Coordinator should also
- outreach / GTM-9, GTM-24: ask Jesse to approve one of two InTire paths: safest pause before
- outreach / GTM-9, GTM-24: `2026-05-25T17:00:03.814+00:00`, or explicit manual-risk approval to let Email 3
- outreach / GTM-9, GTM-24: Poplar/Resend/provider state changes or an urgent scheduled-email decision is

## Lane Status
### Quarterback / Main GTMDot
- Status file: `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/status/quarterback-latest.md`
- Updated: 2026-06-01T08:34:02-07:00 WARNING: stale status file (24.0h old).
- Paperclip IDs: GTM-1, GTM-4, GTM-6, GTM-9, GTM-15, GTM-16, GTM-17, GTM-18, GTM-19, GTM-20, GTM-22, GTM-23, GTM-24
- Summary: Dispatcher B1.0 generated a dry-run digest at `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/dispatcher/digests/2026-06-01-0834-dispatcher-digest.md`. No Paperclip, CRM, deploy, send, contact, git, or production mutations were performed. Use the dispatcher digest approval queue and lane outbox files to route the next board-clearing action without manual re-summarization.
- Blockers: - Pre-Build Coordination: stale status file (212.5h old) - Experiments: stale status file (212.3h old)
- Decisions: - pre-build / GTM-1, GTM-4, GTM-6, GTM-15, GTM-16, GTM-17, GTM-18, GTM-19, GTM-20, GTM-22, GTM-23: Mbanugo unresolved flags remain: owner name, direct email, CRM field reconciliation, GBP URL mismatch, TLS/source risk, Chosen Tires/Roadside Assistance alternate-branding risk, and identity-flag copy approval. - outreach / GTM-9, GTM-24: not retry without f...
- Next action: Use the dispatcher digest approval queue and lane outbox files to route the next board-clearing action without manual re-summarization.

### Pre-Build Coordination
- Status file: `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/status/pre-build-coordination-latest.md`
- Updated: 2026-05-23T15:06:59-04:00 WARNING: stale status file (236.5h old).
- Paperclip IDs: GTM-1, GTM-4, GTM-6, GTM-15, GTM-16, GTM-17, GTM-18, GTM-19, GTM-20, GTM-22, GTM-23
- Summary: Remote-week roadmap and cadence protocol reviewed. Pre-Build remains subordinate to board clearing and should follow a 1-2 times daily cadence unless board clearing needs a template/schema. Jesse accepted `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/2026-05-23-remote-week-prebuild-infra-gtm15-17.md` as re... Hold Pre-Build at ready state while Outreach/Post-Build clear the close-to-send backlog. Follow the remote-week cadence: Pre-Build should update 1-2 times daily unless board clearing specifically needs a template/schema. If spare bandwidth exists, the next safe infrastructure step is static starter templates for Bro...
- Blockers: - Board clearing has priority over new pre-build work. - Browserbase default-enrichment plan exists, but a reusable GTMDot Browserbase evidence runner is not yet implemented as a standard lane tool. - Existing enrichment dispatcher has known source-of-truth limitations: it checks canonical `gtmdot-sites/sites/<slug>` and can miss older deploy-target-only...
- Decisions: - Whether future spare-bandwidth work should refine the reusable packet templates, improve Browserbase output for Post-Build/Bruce/R1VS, or document CRM v2 routing fields for new prospect intake. - Whether the file-ledger packet should later be mirrored into Paperclip comments. - Whether to implement the Browserbase evidence runner later or defer. - Wheth...
- Next action: Hold Pre-Build at ready state while Outreach/Post-Build clear the close-to-send backlog. Follow the remote-week cadence: Pre-Build should update 1-2 times daily unless board clearing specifically needs a template/schema. If spare bandwidth exists, the next safe infrastructure step is static starter templates for Browserbase evidence, R1VS build packet, R1...

### Post-Build Operations
- Status file: `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/status/post-build-operations-latest.md`
- Updated: 2026-05-31T15:34:08-04:00 WARNING: stale status file (44.0h old).
- Paperclip IDs: none detected
- Summary: Post-Build status was stale for roughly 138 hours in the latest dispatcher digest. The remote-week cadence protocol reviewed for this run says it applied through 2026-05-30 unless revoked or replaced, so the safest current state is: do not continue high-autonomy board-clearing actions under the expired remote week a...

### Outreach Operations
- Status file: `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/status/outreach-operations-latest.md`
- Updated: 2026-06-01T10:45:00-04:00 WARNING: stale status file (24.8h old).
- Paperclip IDs: GTM-9, GTM-24
- Summary: - Jesse approved bounded postcard-only execution for `smartwire-solutions`, `dream-steam`, and `handy-dandy-atlanta`. - All three passed live gates immediately before send and were submitted through the CRM action endpoint with `dryRun: false`. - New Poplar order IDs: - `smartwire-solutions`: `3a7ae7b1-9bef-4f90-92c... Coordinator should treat `24-hrs-mobile-tire-services` as a Poplar exception and not retry without fresh approval, monitor Bravo/Browning provider progression, and decide whether to approve a narrow CRM backfill for the three prospects that have postcard events but remain stage `needs_approval`. Coordinator should a...
- Next action: Coordinator should treat `24-hrs-mobile-tire-services` as a Poplar exception and not retry without fresh approval, monitor Bravo/Browning provider progression, and decide whether to approve a narrow CRM backfill for the three prospects that have postcard events but remain stage `needs_approval`. Coordinator should also ask Jesse to approve one of two InTi...

### GTMDot Platform / CRM v2
- Status file: `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/status/gtmdot-platform-latest.md`
- Updated: 2026-06-01T11:20:00-04:00 WARNING: stale status file (24.2h old).
- Paperclip IDs: none detected
- Summary: No summary extracted.

### Experiments
- Status file: `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/status/experiments-latest.md`
- Updated: 2026-05-23T15:17:28-04:00 WARNING: stale status file (236.3h old).
- Paperclip IDs: none detected
- Summary: Keep experimental GTMDot features isolated from production while clarifying what is real, what is only dry-run proven, and what can be advanced safely during Jesse's away-mode week.

## Recent Artifacts
- `20260602-112006-bruce-status-no-work-this-run.md` (no GTM ID, 2026-06-02T08:20:12-07:00): Bruce status: no pending collect requests
- `2026-06-02-1359-bruce-status-no-work-this-run.md` (no GTM ID, 2026-06-02T06:59:47-07:00): subject: no work this run
- `2026-06-02-bruce-status-no-work-this-run.md` (no GTM ID, 2026-06-02T06:39:34-07:00): No new photo collection requests found this run.
- `2026-06-02-1219-bruce-status-no-work-this-run.md` (no GTM ID, 2026-06-02T05:19:39-07:00): No pending `collect-request.md` files were found in `sites/*/` for this run.
- `2026-06-02-0639-bruce-status-no-work-this-run.md` (no GTM ID, 2026-06-01T23:39:36-07:00): No pending 'collect-request.md' files found after scanning the gtmdot-sites repository. All existing requests appear to be archived or have corresponding 'bruce-collected.md' files.
- `2026-06-02T05:39:00Z-bruce-status-no-work-this-run.md` (no GTM ID, 2026-06-01T22:39:36-07:00): No pending collect-request.md files found during this cron run.
- `2026-06-01T20-59-00-bruce-status-no-work-this-run.md` (no GTM ID, 2026-06-01T20:59:32-07:00): No pending `collect-request.md` files were found for this run. All requests have been processed or archived.
- `2026-06-01-1759-bruce-status-no-work-this-run.md` (no GTM ID, 2026-06-01T17:59:39-07:00): subject: no work this run
- `2026-06-01-1600-bruce-status-no-work-this-run.md` (no GTM ID, 2026-06-01T15:59:46-07:00): subject: no work this run
- `2026-06-01T12-39-bruce-status-no-work-this-run.md` (no GTM ID, 2026-06-01T12:39:38-07:00): subject: no work this run
- `2026-06-01-1700-bruce-status-no-work-this-run.md` (no GTM ID, 2026-06-01T10:02:23-07:00): subject: No pending collect-requests
- `20260519015842-bruce-status-no-work-this-run.md` (no GTM ID, 2026-06-01T10:02:17-07:00): No pending collect-request.md files were found in this run.
- `20260518055624-bruce-status-no-work-this-run.md` (no GTM ID, 2026-06-01T10:02:17-07:00): No pending collect-request.md files found in this run.
- `2026-06-01-poplar-provider-truth-audit.md` (no GTM ID, 2026-06-01T10:02:17-07:00): Poplar Provider Truth Audit
- `2026-06-01-poplar-provider-state-production-fix-complete.md` (no GTM ID, 2026-06-01T10:02:17-07:00): Poplar Provider-State Production Fix Complete
- `2026-06-01-crm-v2-codex-takeover-control-plane-reset.md` (no GTM ID, 2026-06-01T10:02:17-07:00): CRM v2 Codex Takeover / Control-Plane Reset
- `2026-06-01-crm-review-workflow-ux-deploy-complete.md` (no GTM ID, 2026-06-01T10:02:17-07:00): CRM Review Workflow UX Deploy Complete
- `2026-06-01-crm-review-ux-and-current-board-friction.md` (no GTM ID, 2026-06-01T10:02:17-07:00): CRM Review UX And Current Board Friction
- `2026-06-01-0259-bruce-status-no-work-this-run.md` (no GTM ID, 2026-06-01T10:02:17-07:00): No pending collect-request.md files found this run. All existing requests are archived.
- `2026-05-31-return-from-vacation-codex-audit.md` (no GTM ID, 2026-06-01T10:02:17-07:00): GTMDot Return-From-Vacation Audit - 2026-05-31
- `2026-05-31-post-vacation-outreach-catchup.md` (no GTM ID, 2026-06-01T10:02:17-07:00): Post-Vacation Outreach Catch-Up - 2026-05-31
- `2026-05-31-poplar-provider-state-integration-fix.md` (no GTM ID, 2026-06-01T10:02:17-07:00): Poplar Provider-State Integration Fix
- `2026-05-31-next-catchup-approval-packet.md` (no GTM ID, 2026-06-01T10:02:17-07:00): Next Catch-Up Approval Packet - 2026-05-31
- `2026-05-31-dead-enrichment-comment-routing-audit.md` (no GTM ID, 2026-06-01T10:02:17-07:00): Dead / Enrichment / Comment Routing Audit - 2026-05-31

## Paperclip Health
- API base: http://127.0.0.1:3199
- Read source: api
- Health: ok
- Latest backup: `/Users/bruce/.openclaw/workspace/paperclip-sandbox-home/instances/gtmdot-sandbox/data/backups/paperclip-20260602-083401.sql.gz` (114762 bytes, 0.00h old).

## Guardrails
- No CRM/Supabase writes performed.
- No Paperclip mutations performed.
- No deploys performed.
- No Poplar/Resend/SMS sends performed.
- No prospect/customer contact performed.
- No git pushes performed.
- No production site edits performed.

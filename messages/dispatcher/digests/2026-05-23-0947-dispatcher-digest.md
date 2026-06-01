# GTMDot Dispatcher Digest - 2026-05-23T09:47:23-07:00

Mode: B1.0 dry-run only
Authority: Git/message files + Paperclip are canonical; Slack/Telegram are notification mirrors.

## Executive State
- Paperclip health: ok
- Paperclip read source: api
- Paperclip dashboard: http://127.0.0.1:3199/GTM/dashboard
- Paperclip task counts: {"blocked": 3, "done": 5, "inProgress": 0, "open": 19}
- Paperclip agent counts: {"active": 0, "error": 0, "paused": 0, "running": 0}
- Local issue counts: {"blocked": 3, "done": 5, "todo": 16}
- Approval queue items found: 1
- Recent artifacts scanned: 6

## Recommended Next 3 Moves
1. Resolve Harrison Poplar failure: capture exact provider error if possible, or approve one normalized-address retry with stop-on-error language.
2. Answer approval item from pre-build: Mbanugo unresolved flags remain: owner name, direct email, CRM field reconciliation, GBP URL mismatch, TLS/source risk, Chosen Tires/Roadside Assistance alternate-branding risk, and identity-flag copy approval.

## Approval Queue
- pre-build / GTM-1, GTM-4, GTM-6, GTM-7, GTM-11, GTM-12, GTM-13, GTM-15, GTM-16, GTM-17, GTM-18, GTM-19, GTM-20, GTM-22, GTM-23: Mbanugo unresolved flags remain: owner name, direct email, CRM field reconciliation, GBP URL mismatch, TLS/source risk, Chosen Tires/Roadside Assistance alternate-branding risk, and identity-flag copy approval.

## Lane Status
### Quarterback / Main GTMDot
- Status file: `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/status/quarterback-latest.md`
- Updated: 2026-05-23T12:45:00-04:00
- Paperclip IDs: GTM-1, GTM-2, GTM-3, GTM-4, GTM-5, GTM-6, GTM-7, GTM-8, GTM-9, GTM-11, GTM-12, GTM-13, GTM-14, GTM-15, GTM-16, GTM-17, GTM-18, GTM-19, GTM-20, GTM-22, GTM-23, GTM-24
- Summary: Dispatcher B1.0 generated a dry-run digest at `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/dispatcher/digests/2026-05-23-0932-dispatcher-digest.md`. Codex then consolidated the May 23 lane handoffs into an away-mode coordinator roadmap at `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/2026-05-23-... Start the away-mode daily loop: verify Harrison postcard state read-only, prepare InTire approval packet, then prepare send-readiness packets for `smartwire-solutions`, `cityboys`, `dream-steam`, and `handy-dandy-atlanta`.
- Blockers: - Explicit approval is still required for CRM writes, Paperclip mutations, deploys, Poplar/Resend/SMS sends, prospect/customer contact, git push, DNS/domain/hosting/billing changes, and Stripe actions. - Harrison was reported by Jesse as successfully retried after the Poplar first-name fix, but coordinator should verify CRM/Poplar event state read-only be...
- Decisions: - Decide whether InTire moves toward `outreach_staged` or holds, and whether postcard, email, or both channels are approved. - Decide whether the asset-ready QA-approved prospects `smartwire-solutions`, `cityboys`, `dream-steam`, and `handy-dandy-atlanta` should receive send-readiness packets now. - Decide whether mailing-field repairs may be drafted from...
- Next action: Start the away-mode daily loop: verify Harrison postcard state read-only, prepare InTire approval packet, then prepare send-readiness packets for `smartwire-solutions`, `cityboys`, `dream-steam`, and `handy-dandy-atlanta`.

### Pre-Build Coordination
- Status file: `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/status/pre-build-coordination-latest.md`
- Updated: 2026-05-17T18:49:19Z WARNING: stale status file (142.0h old).
- Paperclip IDs: GTM-1, GTM-4, GTM-6, GTM-7, GTM-11, GTM-12, GTM-13, GTM-15, GTM-16, GTM-17, GTM-18, GTM-19, GTM-20, GTM-22, GTM-23
- Summary: Read the Paperclip v2 channel brief and the required rollout docs: - `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/2026-05-16-codex-to-lanes-paperclip-v2-channel-brief.md` - `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/2026-05-16-codex-paperclip-v2-rollout-master-brief.md` - `/Users/bruce/.openc... Hold Pre-Build at ready state while Outreach/Post-Build clear the close-to-send backlog. If Jesse prioritizes Pre-Build, start with `GTM-15` by converting `/Users/bruce/.openclaw/workspace/paperclip-sandbox/artifacts/pre-build-coordination-template-2026-05-16.md` into the reusable Paperclip issue/artifact sequence,...
- Blockers: - Board clearing has priority over new pre-build work. - Browserbase default-enrichment plan exists, but a reusable GTMDot Browserbase evidence runner is not yet implemented as a standard lane tool. - Existing enrichment dispatcher has known source-of-truth limitations: it checks canonical `gtmdot-sites/sites/<slug>` and can miss older deploy-target-only...
- Decisions: - Whether `GTM-15` through `GTM-18` should be worked now or held until board-clearing issues `GTM-7`, `GTM-11`, `GTM-12`, and `GTM-13` are clear. - Whether the prospective pre-build template should be promoted into Paperclip v2 issue descriptions as the standing issue tree. - Whether to implement the Browserbase evidence runner now or defer. - Whether to...
- Next action: Hold Pre-Build at ready state while Outreach/Post-Build clear the close-to-send backlog. If Jesse prioritizes Pre-Build, start with `GTM-15` by converting `/Users/bruce/.openclaw/workspace/paperclip-sandbox/artifacts/pre-build-coordination-template-2026-05-16.md` into the reusable Paperclip issue/artifact sequence, then add stale-note handling to the sour...

### Post-Build Operations
- Status file: `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/status/post-build-operations-latest.md`
- Updated: 2026-05-23T10:45:00-04:00
- Paperclip IDs: none detected
- Summary: No summary extracted.

### Outreach Operations
- Status file: `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/status/outreach-operations-latest.md`
- Updated: 2026-05-23T12:34:38-04:00
- Paperclip IDs: none detected
- Summary: - Atlanta Expert Appliance was backfilled from `needs_decision` to `outreach_sent` after Jesse approved the reconciliation for an already-submitted postcard. - Atlanta Expert Appliance postcard event exists with Poplar order ID `95e6cbaa-b029-4516-8f28-4cccf8f74bec`. - Atlanta Expert Appliance `nextEmailAt` remains... Coordinator should route three things: get a Jesse yes/no on Harrison postcard retry, open/track the Atlanta and postcard-status incidents in Paperclip, and assign Outreach/Platform to fix channel-state derivation plus reply-monitoring acceptance criteria before scaling email follow-ups.
- Next action: Coordinator should route three things: get a Jesse yes/no on Harrison postcard retry, open/track the Atlanta and postcard-status incidents in Paperclip, and assign Outreach/Platform to fix channel-state derivation plus reply-monitoring acceptance criteria before scaling email follow-ups.

### GTMDot Platform / CRM v2
- Status file: `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/status/gtmdot-platform-latest.md`
- Updated: 2026-05-23T12:15:00-04:00
- Paperclip IDs: none detected
- Summary: No summary extracted.

### Experiments
- Status file: `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/status/experiments-latest.md`
- Updated: 2026-05-23T12:35:21-04:00
- Paperclip IDs: none detected
- Summary: Keep experimental GTMDot features isolated from production while clarifying what is real, what is only dry-run proven, and what can be advanced safely during Jesse's away-mode week.

## Recent Artifacts
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
- Latest backup: `/Users/bruce/.openclaw/workspace/paperclip-sandbox-home/instances/gtmdot-sandbox/data/backups/paperclip-20260523-093015.sql.gz` (81668 bytes, 0.29h old).

## Guardrails
- No CRM/Supabase writes performed.
- No Paperclip mutations performed.
- No deploys performed.
- No Poplar/Resend/SMS sends performed.
- No prospect/customer contact performed.
- No git pushes performed.
- No production site edits performed.

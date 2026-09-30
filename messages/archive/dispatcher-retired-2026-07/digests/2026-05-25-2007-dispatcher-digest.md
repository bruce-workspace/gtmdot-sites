# GTMDot Dispatcher Digest - 2026-05-25T20:07:20-07:00

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
- Recent artifacts scanned: 1

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
- Updated: 2026-05-25T18:07:20-07:00
- Paperclip IDs: GTM-1, GTM-4, GTM-6, GTM-9, GTM-15, GTM-16, GTM-17, GTM-18, GTM-19, GTM-20, GTM-22, GTM-23, GTM-24
- Summary: Dispatcher B1.0 generated a dry-run digest at `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/dispatcher/digests/2026-05-25-1807-dispatcher-digest.md`. No Paperclip, CRM, deploy, send, contact, git, or production mutations were performed. Use the dispatcher digest approval queue and lane outbox files to route the next board-clearing action without manual re-summarization.
- Blockers: - Pre-Build Coordination: stale status file (54.0h old) - Post-Build Operations: stale status file (25.9h old) - Outreach Operations: stale status file (53.8h old) - GTMDot Platform / CRM v2: stale status file (56.9h old) - Experiments: stale status file (53.8h old)
- Decisions: - pre-build / GTM-1, GTM-4, GTM-6, GTM-15, GTM-16, GTM-17, GTM-18, GTM-19, GTM-20, GTM-22, GTM-23: Mbanugo unresolved flags remain: owner name, direct email, CRM field reconciliation, GBP URL mismatch, TLS/source risk, Chosen Tires/Roadside Assistance alternate-branding risk, and identity-flag copy approval. - outreach / GTM-9, GTM-24: not retry without f...
- Next action: Use the dispatcher digest approval queue and lane outbox files to route the next board-clearing action without manual re-summarization.

### Pre-Build Coordination
- Status file: `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/status/pre-build-coordination-latest.md`
- Updated: 2026-05-23T15:06:59-04:00 WARNING: stale status file (56.0h old).
- Paperclip IDs: GTM-1, GTM-4, GTM-6, GTM-15, GTM-16, GTM-17, GTM-18, GTM-19, GTM-20, GTM-22, GTM-23
- Summary: Remote-week roadmap and cadence protocol reviewed. Pre-Build remains subordinate to board clearing and should follow a 1-2 times daily cadence unless board clearing needs a template/schema. Jesse accepted `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/2026-05-23-remote-week-prebuild-infra-gtm15-17.md` as re... Hold Pre-Build at ready state while Outreach/Post-Build clear the close-to-send backlog. Follow the remote-week cadence: Pre-Build should update 1-2 times daily unless board clearing specifically needs a template/schema. If spare bandwidth exists, the next safe infrastructure step is static starter templates for Bro...
- Blockers: - Board clearing has priority over new pre-build work. - Browserbase default-enrichment plan exists, but a reusable GTMDot Browserbase evidence runner is not yet implemented as a standard lane tool. - Existing enrichment dispatcher has known source-of-truth limitations: it checks canonical `gtmdot-sites/sites/<slug>` and can miss older deploy-target-only...
- Decisions: - Whether future spare-bandwidth work should refine the reusable packet templates, improve Browserbase output for Post-Build/Bruce/R1VS, or document CRM v2 routing fields for new prospect intake. - Whether the file-ledger packet should later be mirrored into Paperclip comments. - Whether to implement the Browserbase evidence runner later or defer. - Wheth...
- Next action: Hold Pre-Build at ready state while Outreach/Post-Build clear the close-to-send backlog. Follow the remote-week cadence: Pre-Build should update 1-2 times daily unless board clearing specifically needs a template/schema. If spare bandwidth exists, the next safe infrastructure step is static starter templates for Browserbase evidence, R1VS build packet, R1...

### Post-Build Operations
- Status file: `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/status/post-build-operations-latest.md`
- Updated: 2026-05-25T21:16:00-04:00
- Paperclip IDs: none detected
- Summary: Post-Build remains in board-clearing support mode. No new Post-Build-safe production action has opened since the 2026-05-23 correction. The lane is maintaining the known ready/held/repair truth while Outreach and the main coordinator handle provider progression, channel/stage mismatch, and approval decisions.

### Outreach Operations
- Status file: `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/status/outreach-operations-latest.md`
- Updated: 2026-05-23T15:18:00-04:00 WARNING: stale status file (55.8h old).
- Paperclip IDs: GTM-9, GTM-24
- Summary: - Jesse approved bounded postcard-only execution for `smartwire-solutions`, `dream-steam`, and `handy-dandy-atlanta`. - All three passed live gates immediately before send and were submitted through the CRM action endpoint with `dryRun: false`. - New Poplar order IDs: - `smartwire-solutions`: `3a7ae7b1-9bef-4f90-92c... Coordinator should treat `24-hrs-mobile-tire-services` as a Poplar exception and not retry without fresh approval, monitor Bravo/Browning provider progression, and decide whether to approve a narrow CRM backfill for the three prospects that have postcard events but remain stage `needs_approval`. Coordinator should a...
- Next action: Coordinator should treat `24-hrs-mobile-tire-services` as a Poplar exception and not retry without fresh approval, monitor Bravo/Browning provider progression, and decide whether to approve a narrow CRM backfill for the three prospects that have postcard events but remain stage `needs_approval`. Coordinator should also ask Jesse to approve one of two InTi...

### GTMDot Platform / CRM v2
- Status file: `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/status/gtmdot-platform-latest.md`
- Updated: 2026-05-23T12:15:00-04:00 WARNING: stale status file (58.9h old).
- Paperclip IDs: none detected
- Summary: No summary extracted.

### Experiments
- Status file: `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/status/experiments-latest.md`
- Updated: 2026-05-23T15:17:28-04:00 WARNING: stale status file (55.8h old).
- Paperclip IDs: none detected
- Summary: Keep experimental GTMDot features isolated from production while clarifying what is real, what is only dry-run proven, and what can be advanced safely during Jesse's away-mode week.

## Recent Artifacts
- `2026-05-25-intire-email-3-urgent-window-check.md` (no GTM ID, 2026-05-25T12:15:05-07:00): InTire Email 3 Urgent Window Check - 2026-05-25

## Paperclip Health
- API base: http://127.0.0.1:3199
- Read source: api
- Health: ok
- Latest backup: `/Users/bruce/.openclaw/workspace/paperclip-sandbox-home/instances/gtmdot-sandbox/data/backups/paperclip-20260525-193016.sql.gz` (99438 bytes, 0.62h old).

## Guardrails
- No CRM/Supabase writes performed.
- No Paperclip mutations performed.
- No deploys performed.
- No Poplar/Resend/SMS sends performed.
- No prospect/customer contact performed.
- No git pushes performed.
- No production site edits performed.

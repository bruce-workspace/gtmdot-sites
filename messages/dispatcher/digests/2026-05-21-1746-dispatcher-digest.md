# GTMDot Dispatcher Digest - 2026-05-21T17:46:28-07:00

Mode: B1.0 dry-run only
Authority: Git/message files + Paperclip are canonical; Slack/Telegram are notification mirrors.

## Executive State
- Paperclip health: ok
- Paperclip read source: api
- Paperclip dashboard: http://127.0.0.1:3199/GTM/dashboard
- Paperclip task counts: {"blocked": 3, "done": 5, "inProgress": 0, "open": 19}
- Paperclip agent counts: {"active": 0, "error": 0, "paused": 0, "running": 0}
- Local issue counts: {"blocked": 3, "done": 5, "todo": 16}
- Approval queue items found: 11
- Recent artifacts scanned: 3

## Recommended Next 3 Moves
1. Decide InTire Mobile Tire Shop: approve/hold stage movement and channels now that GTM-14 technical readiness passed.
2. Keep CRM v2 lab aligned with channel-state truth, stale-note handling, Paperclip links, and provider error visibility.
3. Answer approval item from pre-build: Mbanugo unresolved flags remain: owner name, direct email, CRM field reconciliation, GBP URL mismatch, TLS/source risk, Chosen Tires/Roadside Assistance alternate-branding risk, and identity-flag copy approval.

## Approval Queue
- pre-build / GTM-1, GTM-4, GTM-6, GTM-7, GTM-11, GTM-12, GTM-13, GTM-15, GTM-16, GTM-17, GTM-18, GTM-19, GTM-20, GTM-22, GTM-23: Mbanugo unresolved flags remain: owner name, direct email, CRM field reconciliation, GBP URL mismatch, TLS/source risk, Chosen Tires/Roadside Assistance alternate-branding risk, and identity-flag copy approval.
- post-build / GTM-3, GTM-11, GTM-12, GTM-13, GTM-14: Approve or hold InTire move toward `outreach_staged`.
- post-build / GTM-3, GTM-11, GTM-12, GTM-13, GTM-14: Approve channels for InTire: postcard, email, or both.
- post-build / GTM-3, GTM-11, GTM-12, GTM-13, GTM-14: Separately approve any Poplar/Resend action if/when ready.
- post-build / GTM-3, GTM-11, GTM-12, GTM-13, GTM-14: Ask Jesse/coordinator to decide whether InTire should move to `outreach_staged`
- post-build / GTM-3, GTM-11, GTM-12, GTM-13, GTM-14: and which channels are approved. If approved, handle stage movement and outreach
- post-build / GTM-3, GTM-11, GTM-12, GTM-13, GTM-14: Jesse approval still required before CRM stage move, postcard submit, or email
- outreach / unknown: Approve deployment and any live send use later, after review.
- outreach / unknown: Decide whether to mirror approved copy into CRM v2 sandbox and legacy static templates.
- outreach / unknown: Review the new sequence copy in CRM preview, then decide whether to deploy and whether to mirror the same copy contract into CRM v2. Do not send or deploy without explicit approval.
- outreach / unknown: No send/deploy/CRM write approval.

## Lane Status
### Quarterback / Main GTMDot
- Status file: `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/status/quarterback-latest.md`
- Updated: 2026-05-21T17:31:27-07:00
- Paperclip IDs: GTM-1, GTM-2, GTM-3, GTM-4, GTM-5, GTM-6, GTM-7, GTM-8, GTM-9, GTM-11, GTM-12, GTM-13, GTM-14, GTM-15, GTM-16, GTM-17, GTM-18, GTM-19, GTM-20, GTM-22, GTM-23, GTM-24
- Summary: Dispatcher B1.0 generated a dry-run digest at `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/dispatcher/digests/2026-05-21-1731-dispatcher-digest.md`. No Paperclip, CRM, deploy, send, contact, git, or production mutations were performed. Use the dispatcher digest approval queue and lane outbox files to route the next board-clearing action without manual re-summarization.
- Blockers: - Pre-Build Coordination: stale status file (101.7h old) - Post-Build Operations: stale status file (85.6h old) - GTMDot Platform / CRM v2: stale status file (108.0h old) - Experiments: stale status file (142.2h old)
- Decisions: - pre-build / GTM-1, GTM-4, GTM-6, GTM-7, GTM-11, GTM-12, GTM-13, GTM-15, GTM-16, GTM-17, GTM-18, GTM-19, GTM-20, GTM-22, GTM-23: Mbanugo unresolved flags remain: owner name, direct email, CRM field reconciliation, GBP URL mismatch, TLS/source risk, Chosen Tires/Roadside Assistance alternate-branding risk, and identity-flag copy approval. - post-build / G...
- Next action: Use the dispatcher digest approval queue and lane outbox files to route the next board-clearing action without manual re-summarization.

### Pre-Build Coordination
- Status file: `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/status/pre-build-coordination-latest.md`
- Updated: 2026-05-17T18:49:19Z WARNING: stale status file (102.0h old).
- Paperclip IDs: GTM-1, GTM-4, GTM-6, GTM-7, GTM-11, GTM-12, GTM-13, GTM-15, GTM-16, GTM-17, GTM-18, GTM-19, GTM-20, GTM-22, GTM-23
- Summary: Read the Paperclip v2 channel brief and the required rollout docs: - `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/2026-05-16-codex-to-lanes-paperclip-v2-channel-brief.md` - `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/2026-05-16-codex-paperclip-v2-rollout-master-brief.md` - `/Users/bruce/.openc... Hold Pre-Build at ready state while Outreach/Post-Build clear the close-to-send backlog. If Jesse prioritizes Pre-Build, start with `GTM-15` by converting `/Users/bruce/.openclaw/workspace/paperclip-sandbox/artifacts/pre-build-coordination-template-2026-05-16.md` into the reusable Paperclip issue/artifact sequence,...
- Blockers: - Board clearing has priority over new pre-build work. - Browserbase default-enrichment plan exists, but a reusable GTMDot Browserbase evidence runner is not yet implemented as a standard lane tool. - Existing enrichment dispatcher has known source-of-truth limitations: it checks canonical `gtmdot-sites/sites/<slug>` and can miss older deploy-target-only...
- Decisions: - Whether `GTM-15` through `GTM-18` should be worked now or held until board-clearing issues `GTM-7`, `GTM-11`, `GTM-12`, and `GTM-13` are clear. - Whether the prospective pre-build template should be promoted into Paperclip v2 issue descriptions as the standing issue tree. - Whether to implement the Browserbase evidence runner now or defer. - Whether to...
- Next action: Hold Pre-Build at ready state while Outreach/Post-Build clear the close-to-send backlog. If Jesse prioritizes Pre-Build, start with `GTM-15` by converting `/Users/bruce/.openclaw/workspace/paperclip-sandbox/artifacts/pre-build-coordination-template-2026-05-16.md` into the reusable Paperclip issue/artifact sequence, then add stale-note handling to the sour...

### Post-Build Operations
- Status file: `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/status/post-build-operations-latest.md`
- Updated: 2026-05-18T06:55:00-04:00 WARNING: stale status file (85.9h old).
- Paperclip IDs: GTM-3, GTM-11, GTM-12, GTM-13, GTM-14
- Summary: InTire Mobile Tire Shop repair is complete. GTM-14 technical readiness passed. InTire is ready for Jesse's stage/outreach decision, but no CRM movement or outreach action has been performed. Ask Jesse/coordinator to decide whether InTire should move to `outreach_staged` and which channels are approved. If approved, handle stage movement and outreach as separate explicit actions.
- Blockers: - InTire: no hard technical blockers remain after repair. - InTire: email preview UI endpoint warning remains from the legacy gate (`HTTP 404`), but the gate reports actual send via `/actions` still works. - Jesse approval still required before CRM stage move, postcard submit, or email trigger.
- Decisions: - Approve or hold InTire move toward `outreach_staged`. - Approve channels for InTire: postcard, email, or both. - Separately approve any Poplar/Resend action if/when ready.
- Next action: Ask Jesse/coordinator to decide whether InTire should move to `outreach_staged` and which channels are approved. If approved, handle stage movement and outreach as separate explicit actions.

### Outreach Operations
- Status file: `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/status/outreach-operations-latest.md`
- Updated: 2026-05-21T06:46:45-04:00
- Paperclip IDs: none detected
- Summary: - Active `brucecom-v3` email template now greets with first name only when available, falling back to "there". - Sequence copy has been tightened to sound more direct and less generic, with no prospect-facing em dashes in the active template. - Template now adds an insight line from `promotionText`, `photoHighlights... Review the new sequence copy in CRM preview, then decide whether to deploy and whether to mirror the same copy contract into CRM v2. Do not send or deploy without explicit approval.
- Blockers: - No send/deploy/CRM write approval. - Existing Turbopack warning remains in `next.config.ts` -> `src/lib/vault.ts` tracing path during build; not caused by this copy patch.
- Decisions: - Approve deployment and any live send use later, after review. - Decide whether to mirror approved copy into CRM v2 sandbox and legacy static templates.
- Next action: Review the new sequence copy in CRM preview, then decide whether to deploy and whether to mirror the same copy contract into CRM v2. Do not send or deploy without explicit approval.

### GTMDot Platform / CRM v2
- Status file: `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/status/gtmdot-platform-latest.md`
- Updated: 2026-05-17T08:30:24-04:00 WARNING: stale status file (108.3h old).
- Paperclip IDs: GTM-5, GTM-19, GTM-20, GTM-24
- Summary: CRM v2 remains lab-only and is not ready to test or replace the live CRM. HeroUI Pro is installed and verified in `/Users/bruce/.openclaw/workspace/brucecom-v3`; `@heroui-pro/react/css` builds successfully. Platform direction is to preserve current stage/API fields for Outreach now, add reply/channel state as additi... Continue CRM v2 lab route planning/build against the existing CRM API, with the prospect command sheet and Outreach Operations view designed around channel-state cards, untriaged replies, bounced emails, replied-but-sequence-active mismatches, postcard provider exceptions, Paperclip blockers, and exact next action.
- Blockers: - Existing CRM stage alone does not express channel truth. - `outreach_sent` is currently too broad for operational clarity. - Inbound reply monitoring to `hello@gtmdot.com` is not yet proven end-to-end. - Current CRM does not yet prove that a prospect reply becomes CRM state and pauses future email follow-ups. - Poplar provider state may be ahead of CRM...
- Decisions: - Whether CRM v2 should remain lab-only until board clearing is stable. - Whether `GTM-24` may proceed from planning to code changes. - Whether reply storage should remain snippet/metadata-only or include full reply bodies. - Whether mailbox/thread links are preferred as the full-content source of truth.
- Next action: Continue CRM v2 lab route planning/build against the existing CRM API, with the prospect command sheet and Outreach Operations view designed around channel-state cards, untriaged replies, bounced emails, replied-but-sequence-active mismatches, postcard provider exceptions, Paperclip blockers, and exact next action.

### Experiments
- Status file: `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/status/experiments-latest.md`
- Updated: 2026-05-16T02:18:43Z WARNING: stale status file (142.5h old).
- Paperclip IDs: none detected
- Summary: Placeholder created by quarterback session. Experiments should remain isolated from production CRM/outreach/deploy unless Jesse explicitly graduates a feature. Create an experiments inventory with status, vendor/API dependencies, production risk, and graduation criteria.
- Blockers: - Experimental work must not consume board-clearing bandwidth unless it directly supports revenue or support.
- Decisions: - Which experiments are active, paused, or archived.
- Next action: Create an experiments inventory with status, vendor/API dependencies, production risk, and graduation criteria.

## Recent Artifacts
- `2026-05-21-paperclip-gtm-25-26-implementation-record.md` (GTM-25, GTM-26, GTM-27, 2026-05-21T06:32:00-07:00): Paperclip proactive control-plane GTM-25/GTM-26 implementation record
- `2026-05-21-paperclip-proactive-control-plane-plan.md` (GTM-6, GTM-25, GTM-26, GTM-27, GTM-28, GTM-29, GTM-30, 2026-05-21T04:51:25-07:00): Paperclip proactive control-plane plan
- `2026-05-21-poplar-recipient-name-rule.md` (no GTM ID, 2026-05-21T03:41:08-07:00): Poplar recipient name rule

## Paperclip Health
- API base: http://127.0.0.1:3199
- Read source: api
- Health: ok
- Latest backup: `/Users/bruce/.openclaw/workspace/paperclip-sandbox-home/instances/gtmdot-sandbox/data/backups/paperclip-20260521-173014.sql.gz` (71537 bytes, 0.27h old).

## Guardrails
- No CRM/Supabase writes performed.
- No Paperclip mutations performed.
- No deploys performed.
- No Poplar/Resend/SMS sends performed.
- No prospect/customer contact performed.
- No git pushes performed.
- No production site edits performed.

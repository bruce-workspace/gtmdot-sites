# GTMDot Dispatcher Digest - 2026-05-22T23:32:09-07:00

Mode: B1.0 dry-run only
Authority: Git/message files + Paperclip are canonical; Slack/Telegram are notification mirrors.

## Executive State
- Paperclip health: ok
- Paperclip read source: api
- Paperclip dashboard: http://127.0.0.1:3199/GTM/dashboard
- Paperclip task counts: {"blocked": 3, "done": 5, "inProgress": 0, "open": 19}
- Paperclip agent counts: {"active": 0, "error": 0, "paused": 0, "running": 0}
- Local issue counts: {"blocked": 3, "done": 5, "todo": 16}
- Approval queue items found: 12
- Recent artifacts scanned: 2

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
- outreach / unknown: Decide whether any successful postcard submit from a live pre-outreach stage should force Outreach Sent, or whether the allowed source stages should be explicit.
- outreach / unknown: Decide whether to let Outreach Operations mutate Paperclip for the resolved incident, or leave it as a recommendation for the coordinator.
- outreach / unknown: Refresh the CRM page and retry Harrison's postcard if Jesse wants to send it now. Also deploy/track the Atlanta stage-transition patch if approved, log resolved incidents in Paperclip if Jesse wants Outreach Operations to mutate Paperclip, and fix/track the prospect detail `postcardStatus` derivation mismatch.
- outreach / unknown: No deployment approval yet.
- outreach / unknown: No Paperclip mutation approval yet.

## Lane Status
### Quarterback / Main GTMDot
- Status file: `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/status/quarterback-latest.md`
- Updated: 2026-05-22T23:17:09-07:00
- Paperclip IDs: GTM-1, GTM-2, GTM-3, GTM-4, GTM-5, GTM-6, GTM-7, GTM-8, GTM-9, GTM-11, GTM-12, GTM-13, GTM-14, GTM-15, GTM-16, GTM-17, GTM-18, GTM-19, GTM-20, GTM-22, GTM-23, GTM-24
- Summary: Dispatcher B1.0 generated a dry-run digest at `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/dispatcher/digests/2026-05-22-2317-dispatcher-digest.md`. No Paperclip, CRM, deploy, send, contact, git, or production mutations were performed. Use the dispatcher digest approval queue and lane outbox files to route the next board-clearing action without manual re-summarization.
- Blockers: - Pre-Build Coordination: stale status file (131.5h old) - Post-Build Operations: stale status file (115.4h old) - GTMDot Platform / CRM v2: stale status file (137.8h old) - Experiments: stale status file (172.0h old)
- Decisions: - pre-build / GTM-1, GTM-4, GTM-6, GTM-7, GTM-11, GTM-12, GTM-13, GTM-15, GTM-16, GTM-17, GTM-18, GTM-19, GTM-20, GTM-22, GTM-23: Mbanugo unresolved flags remain: owner name, direct email, CRM field reconciliation, GBP URL mismatch, TLS/source risk, Chosen Tires/Roadside Assistance alternate-branding risk, and identity-flag copy approval. - post-build / G...
- Next action: Use the dispatcher digest approval queue and lane outbox files to route the next board-clearing action without manual re-summarization.

### Pre-Build Coordination
- Status file: `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/status/pre-build-coordination-latest.md`
- Updated: 2026-05-17T18:49:19Z WARNING: stale status file (131.7h old).
- Paperclip IDs: GTM-1, GTM-4, GTM-6, GTM-7, GTM-11, GTM-12, GTM-13, GTM-15, GTM-16, GTM-17, GTM-18, GTM-19, GTM-20, GTM-22, GTM-23
- Summary: Read the Paperclip v2 channel brief and the required rollout docs: - `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/2026-05-16-codex-to-lanes-paperclip-v2-channel-brief.md` - `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/2026-05-16-codex-paperclip-v2-rollout-master-brief.md` - `/Users/bruce/.openc... Hold Pre-Build at ready state while Outreach/Post-Build clear the close-to-send backlog. If Jesse prioritizes Pre-Build, start with `GTM-15` by converting `/Users/bruce/.openclaw/workspace/paperclip-sandbox/artifacts/pre-build-coordination-template-2026-05-16.md` into the reusable Paperclip issue/artifact sequence,...
- Blockers: - Board clearing has priority over new pre-build work. - Browserbase default-enrichment plan exists, but a reusable GTMDot Browserbase evidence runner is not yet implemented as a standard lane tool. - Existing enrichment dispatcher has known source-of-truth limitations: it checks canonical `gtmdot-sites/sites/<slug>` and can miss older deploy-target-only...
- Decisions: - Whether `GTM-15` through `GTM-18` should be worked now or held until board-clearing issues `GTM-7`, `GTM-11`, `GTM-12`, and `GTM-13` are clear. - Whether the prospective pre-build template should be promoted into Paperclip v2 issue descriptions as the standing issue tree. - Whether to implement the Browserbase evidence runner now or defer. - Whether to...
- Next action: Hold Pre-Build at ready state while Outreach/Post-Build clear the close-to-send backlog. If Jesse prioritizes Pre-Build, start with `GTM-15` by converting `/Users/bruce/.openclaw/workspace/paperclip-sandbox/artifacts/pre-build-coordination-template-2026-05-16.md` into the reusable Paperclip issue/artifact sequence, then add stale-note handling to the sour...

### Post-Build Operations
- Status file: `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/status/post-build-operations-latest.md`
- Updated: 2026-05-18T06:55:00-04:00 WARNING: stale status file (115.6h old).
- Paperclip IDs: GTM-3, GTM-11, GTM-12, GTM-13, GTM-14
- Summary: InTire Mobile Tire Shop repair is complete. GTM-14 technical readiness passed. InTire is ready for Jesse's stage/outreach decision, but no CRM movement or outreach action has been performed. Ask Jesse/coordinator to decide whether InTire should move to `outreach_staged` and which channels are approved. If approved, handle stage movement and outreach as separate explicit actions.
- Blockers: - InTire: no hard technical blockers remain after repair. - InTire: email preview UI endpoint warning remains from the legacy gate (`HTTP 404`), but the gate reports actual send via `/actions` still works. - Jesse approval still required before CRM stage move, postcard submit, or email trigger.
- Decisions: - Approve or hold InTire move toward `outreach_staged`. - Approve channels for InTire: postcard, email, or both. - Separately approve any Poplar/Resend action if/when ready.
- Next action: Ask Jesse/coordinator to decide whether InTire should move to `outreach_staged` and which channels are approved. If approved, handle stage movement and outreach as separate explicit actions.

### Outreach Operations
- Status file: `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/status/outreach-operations-latest.md`
- Updated: 2026-05-22T22:55:39-04:00
- Paperclip IDs: none detected
- Summary: - Root cause confirmed: `submit_postcard` auto-promoted only from `outreach_staged` or `qa_approved`, so a successful send from `needs_decision` remained in Needs Decision. - Local code now centralizes live outreach promotion logic so successful email/postcard sends from active pre-outreach stages advance to `outrea... Refresh the CRM page and retry Harrison's postcard if Jesse wants to send it now. Also deploy/track the Atlanta stage-transition patch if approved, log resolved incidents in Paperclip if Jesse wants Outreach Operations to mutate Paperclip, and fix/track the prospect detail `postcardStatus` derivation mismatch.
- Blockers: - No deployment approval yet. - No Paperclip mutation approval yet. - Follow-up code issue: prospect detail API should derive postcard status from outreach events or stop returning a stale raw `postcardStatus`. - Harrison has no known remaining blocker for the specific Poplar 20-character `first_name` rule. If a retry still fails after refreshing the CRM...
- Decisions: - Decide whether any successful postcard submit from a live pre-outreach stage should force Outreach Sent, or whether the allowed source stages should be explicit. - Decide whether to let Outreach Operations mutate Paperclip for the resolved incident, or leave it as a recommendation for the coordinator.
- Next action: Refresh the CRM page and retry Harrison's postcard if Jesse wants to send it now. Also deploy/track the Atlanta stage-transition patch if approved, log resolved incidents in Paperclip if Jesse wants Outreach Operations to mutate Paperclip, and fix/track the prospect detail `postcardStatus` derivation mismatch.

### GTMDot Platform / CRM v2
- Status file: `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/status/gtmdot-platform-latest.md`
- Updated: 2026-05-17T08:30:24-04:00 WARNING: stale status file (138.0h old).
- Paperclip IDs: GTM-5, GTM-19, GTM-20, GTM-24
- Summary: CRM v2 remains lab-only and is not ready to test or replace the live CRM. HeroUI Pro is installed and verified in `/Users/bruce/.openclaw/workspace/brucecom-v3`; `@heroui-pro/react/css` builds successfully. Platform direction is to preserve current stage/API fields for Outreach now, add reply/channel state as additi... Continue CRM v2 lab route planning/build against the existing CRM API, with the prospect command sheet and Outreach Operations view designed around channel-state cards, untriaged replies, bounced emails, replied-but-sequence-active mismatches, postcard provider exceptions, Paperclip blockers, and exact next action.
- Blockers: - Existing CRM stage alone does not express channel truth. - `outreach_sent` is currently too broad for operational clarity. - Inbound reply monitoring to `hello@gtmdot.com` is not yet proven end-to-end. - Current CRM does not yet prove that a prospect reply becomes CRM state and pauses future email follow-ups. - Poplar provider state may be ahead of CRM...
- Decisions: - Whether CRM v2 should remain lab-only until board clearing is stable. - Whether `GTM-24` may proceed from planning to code changes. - Whether reply storage should remain snippet/metadata-only or include full reply bodies. - Whether mailbox/thread links are preferred as the full-content source of truth.
- Next action: Continue CRM v2 lab route planning/build against the existing CRM API, with the prospect command sheet and Outreach Operations view designed around channel-state cards, untriaged replies, bounced emails, replied-but-sequence-active mismatches, postcard provider exceptions, Paperclip blockers, and exact next action.

### Experiments
- Status file: `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/status/experiments-latest.md`
- Updated: 2026-05-16T02:18:43Z WARNING: stale status file (172.2h old).
- Paperclip IDs: none detected
- Summary: Placeholder created by quarterback session. Experiments should remain isolated from production CRM/outreach/deploy unless Jesse explicitly graduates a feature. Create an experiments inventory with status, vendor/API dependencies, production risk, and graduation criteria.
- Blockers: - Experimental work must not consume board-clearing bandwidth unless it directly supports revenue or support.
- Decisions: - Which experiments are active, paused, or archived.
- Next action: Create an experiments inventory with status, vendor/API dependencies, production risk, and graduation criteria.

## Recent Artifacts
- `2026-05-22-harrison-poplar-public-crm-stale-route.md` (no GTM ID, 2026-05-22T19:55:54-07:00): Harrison Poplar Submit Error - Public CRM Stale Route
- `2026-05-22-harrison-poplar-submit-incident-followup.md` (GTM-12, 2026-05-22T03:48:20-07:00): Harrison & Sons Poplar Submit Incident Follow-Up

## Paperclip Health
- API base: http://127.0.0.1:3199
- Read source: api
- Health: ok
- Latest backup: `/Users/bruce/.openclaw/workspace/paperclip-sandbox-home/instances/gtmdot-sandbox/data/backups/paperclip-20260522-233015.sql.gz` (78823 bytes, 0.03h old).

## Guardrails
- No CRM/Supabase writes performed.
- No Paperclip mutations performed.
- No deploys performed.
- No Poplar/Resend/SMS sends performed.
- No prospect/customer contact performed.
- No git pushes performed.
- No production site edits performed.

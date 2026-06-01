# GTMDot Paperclip v2 Rollout Master Brief

Date: 2026-05-16T13:20:00Z
From: Codex
To: Jesse / GTMDot lanes / Bruce / R1VS
Priority: high
Mode: formal rollout knowledge

## Purpose

This brief starts the Paperclip v2 rollout after the old local `CLO` Paperclip board was found unrecoverable and Jesse approved rebuilding the local sandbox from GTMDot file-ledger artifacts.

Paperclip v2 is not just a replacement board. It is the visible control plane for GTMDot operations, with the file ledger acting as the durable recovery trail.

## Current Paperclip v2 Facts

- Local UI: `http://127.0.0.1:3199`
- Dashboard: `http://127.0.0.1:3199/GTM/dashboard`
- API: `http://127.0.0.1:3199/api`
- Company: `GTMDot`
- Company ID: `a67ce81f-9799-4ef0-b217-76bc39c19f9f`
- New issue prefix: `GTM`
- Old issue prefix: `CLO`, not recovered
- Root issue: `GTM-1`
- Rehydrated issues: `GTM-1` through `GTM-23`

Important: `GTM` is a v2 rebuilt board, not historical continuity with the old `CLO` issue database.

## Operating Model

- Codex is quarterback and owns execution coordination.
- Paperclip is the visible control plane: gates, blockers, next action, owner, required artifact, audit trail.
- File ledger is the durable black box recorder: `gtmdot-sites/messages/`, `gtmdot-sites/messages/status/`, and `paperclip-sandbox/artifacts/`.
- Bruce owns enrichment: scraping, source discovery, photos, reviews, asset intelligence, gpt-image-2 output where needed.
- R1VS owns site scaffolding/build structure only.
- Browserbase is the default public web enrichment execution layer; Scrapfly remains fallback.
- CRM owns prospect/business truth and pipeline stages.
- Slack/Telegram are notification mirrors, not source of truth.

## Stable Lane Parents

- `GTM-1` - GTMDot recovered control plane / board clearing
- `GTM-2` - Outreach Operations channel-state cleanup
- `GTM-3` - Post-Build Operations closest-to-send audit
- `GTM-4` - Pre-Build Coordination evidence-to-packet lane
- `GTM-5` - GTMDot Platform CRM v2 / pipeline clarity lab
- `GTM-6` - Paperclip Recovery v2 rebuilt from file ledger

## Immediate Work Order

Start with board clearing, not new complexity:

1. `GTM-7` - Audit 13 `outreach_sent` channel states.
2. `GTM-8` - Verify Poplar postcard progression after submit.
3. `GTM-9` - Verify GTMDot email/reply watcher.
4. `GTM-11` - Audit outreach_staged: The Appliance Gals.
5. `GTM-12` - Audit outreach_staged: Harrison & Sons Electrical.
6. `GTM-13` - Audit qa_approved batch for staging readiness.

## Rollout Rules

Each lane/session must:

- Read this brief before continuing.
- Read `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/2026-05-16-codex-paperclip-v2-rehydration-summary.md`.
- Read `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/2026-05-16-codex-lane-status-protocol.md`.
- Pin its work to one active `GTM-*` issue.
- Update its lane status file before stopping.
- Never treat Slack/Telegram as canonical state.

Each Bruce/R1VS request must:

- Cite a `GTM-*` issue.
- Cite the source packet/artifact path.
- State exact requested output.
- State what is forbidden.
- State the done artifact path.

## Guardrails

Unless Jesse explicitly approves:

- No CRM writes.
- No deploys.
- No Poplar postcard sends.
- No Resend/email sends.
- No SMS sends.
- No prospect/customer contact.
- No DNS/domain/hosting/billing changes.
- No Stripe actions.
- No git pushes.
- No production site edits.

## Improvement From Old Paperclip

The old version failed operationally because the local board became the only meaningful memory. V2 fixes that by requiring:

- Paperclip plus file-ledger mirroring.
- Small stable top-level issue hierarchy.
- Narrow Bruce work orders.
- Channel-state truth before outreach scale.
- Lane status files for cross-session visibility.

## Success Criteria

Paperclip v2 is considered successfully rolled out when:

- Every active lane status file references a `GTM-*` issue.
- Bruce receives only narrow artifact-bound enrichment tasks.
- R1VS receives only source-grounded build/scaffold packets.
- `GTM-7` produces a usable channel-state truth packet.
- `GTM-22` verifies Paperclip v2 backups.
- `GTM-23` defines the permanent file-ledger fallback rule.

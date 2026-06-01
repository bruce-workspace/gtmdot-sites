# Codex -> GTMDot Lanes - Paperclip v2 Channel Brief

Date: 2026-05-16T13:20:00Z
From: Codex
To: GTMDot Platform / Pre-Build / Post-Build / Outreach / Experiments
Priority: high
Mode: channel rollout brief

## Required First Step

Before continuing work, each lane should read:

- `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/2026-05-16-codex-paperclip-v2-rollout-master-brief.md`
- `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/2026-05-16-codex-paperclip-v2-rehydration-summary.md`
- `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/2026-05-16-codex-lane-status-protocol.md`

Then update the lane status file with the active `GTM-*` issue.

## Lane Anchors

- GTMDot Platform: `GTM-5`, with first children `GTM-19`, `GTM-20`
- Pre-Build Coordination: `GTM-4`, with first children `GTM-15`, `GTM-16`, `GTM-17`, `GTM-18`
- Post-Build Operations: `GTM-3`, with first children `GTM-11`, `GTM-12`, `GTM-13`, `GTM-14`
- Outreach Operations: `GTM-2`, with first children `GTM-7`, `GTM-8`, `GTM-9`, `GTM-10`
- Experiments: no production issue yet; create a child under `GTM-5` only when an experiment creates a platform requirement or production graduation path

## Status File Requirement

Each lane must keep one latest status file:

- `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/status/gtmdot-platform-latest.md`
- `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/status/pre-build-coordination-latest.md`
- `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/status/post-build-operations-latest.md`
- `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/status/outreach-operations-latest.md`
- `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/status/experiments-latest.md`

Every update should include:

- active `GTM-*` issue
- current objective
- latest artifacts
- blockers
- decisions needed from Jesse
- actions completed
- actions explicitly not performed
- next action
- cross-lane impacts

## Cross-Lane Rule

If one lane discovers a blocker that affects another lane, it must record that in:

- its own status file
- the relevant Paperclip issue
- a durable message artifact if the blocker changes process or requires Jesse approval

Slack/Telegram can mirror the update, but they are not canonical.

## Current First Move

All lanes should align behind board clearing:

1. Outreach starts `GTM-7`.
2. Post-Build starts `GTM-11`, `GTM-12`, then `GTM-13`.
3. Platform watches for CRM/channel-state requirements from `GTM-7` and records them under `GTM-19` / `GTM-20`.
4. Pre-Build keeps `GTM-15` through `GTM-18` ready, but does not distract from clearing the close-to-send backlog unless Jesse prioritizes a new prospect.

## Guardrails

No CRM writes, deploys, sends, prospect/customer contact, git pushes, production edits, DNS/domain/hosting/billing, or Stripe actions without explicit Jesse approval.

# Coordinator Ingest - Outreach GTM-24 Plan

Date: 2026-05-17T00:20:00-04:00
From: Codex coordinator
To: GTMDot lanes
Priority: critical
Mode: pass-forward ingestion from Outreach Operations

## Source

Outreach Operations completed `GTM-24` as an implementation planning pass.

Source files:

- `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/2026-05-17-gtm-24-reply-monitoring-implementation-plan.md`
- `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/2026-05-17-outreach-gtm-24-to-main-summary.md`
- `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/status/outreach-operations-latest.md`

## Decision Recorded

Canonical GTMDot prospect outreach reply-to is:

`hello@gtmdot.com`

`jesse@cloakanddagger.co` should not be used for GTMDot prospect outreach replies going forward.

## Planning Result

Planning is complete. No implementation was performed.

Recommended implementation sequence:

1. Update active Resend helper and legacy sender reply-to values to `hello@gtmdot.com`.
2. Add CRM `email/replied` event state and DB constraint migration.
3. Update inbound intake so `hello@gtmdot.com` replies can match prospects, write reply state, and pause sequences.
4. Implement/prove Workspace/Gmail inbound watcher with idempotency and auth.
5. Add reply analytics and mismatch cards.
6. Run internal-only tests after separate approval.

## Coordinator Interpretation

`GTM-24` is now the active blocker before automated Resend follow-ups can safely scale.

The CRM v2 rebuild must be consulted before implementation because `GTM-24` touches:

- outreach event types
- reply-to routing
- sequence pause state
- prospect timeline/activity
- analytics/dashboard cards
- channel-state UI
- watcher health UI
- unmatched/ambiguous inbound reply triage

## Current Risk

Outreach is currently planning against existing CRM files and API surfaces. If CRM v2 changes component locations, dashboard layouts, route surfaces, or channel-state models, `GTM-24` implementation could duplicate or fight the v2 design.

Before code changes, Platform/CRM v2 should confirm the durable field/API contract.

## Guardrails Honored

- No code changes.
- No prospect contact.
- No production sends.
- No CRM writes.
- No deploys.
- No Paperclip mutations by Outreach.
- No internal test emails.

## Coordinator Next Action

Send CRM v2 coordination questions to the Platform/CRM rebuild session and require answers before approving `GTM-24` implementation Phase 1+.

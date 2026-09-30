Lane: GTMDot Ops
Owner: Codex / Paperclip orchestration
Updated: 2026-06-09T08:11:51-04:00
Mode: simplified Build / Fix / Send / Needs Jesse operating status

## Now

GTMDot should operate from one simplified status surface until CRM v2 becomes the command surface.

Current recommendation:

- Use Paperclip as the orchestration/job layer.
- Use CRM as the visible prospect pipeline.
- Use files as artifact storage/audit, not as the operator interface.
- Use chats as temporary workbenches, not source of truth.

Primary briefing:

- `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/2026-06-09-paperclip-orchestration-model.md`

## Build

Agent-owned by default.

Includes intake, research, enrichment, R1VS build packets, site generation, and build-return handling.

Jesse involvement should be limited to true fit/source/judgment decisions.

## Fix

Agent-owned by default.

Includes current QA failures, visual/site repair, stale-note rechecks, postcard asset repair, and provider payload repair before send.

Stale notes are historical unless fresh evidence proves the issue still exists.

## Send

Approval-gated.

Includes postcard/email preflight, Poplar/Resend/Gmail provider state, reply/bounce safety, and named send/retry approval packets.

Agents can prepare evidence. Jesse approves real sends, retries, and prospect contact.

## Needs Jesse

Human judgment only.

Valid reasons:

- approve site/outreach,
- accept risk,
- choose between conflicting source truths,
- approve send/retry/contact,
- override a current blocker,
- decide a prospect is not a fit.

Do not escalate missing email, raw URLs, claim codes, history-only notes, stale open items, or basic enrichment unless background work already failed and the exact decision is clear.

## Background Agents

Recommended narrow routines:

- `runtime-watchdog`
- `dispatcher`
- `research-enrichment-agent`
- `r1vs-build-runner`
- `qa-fix-router`
- `postcard-preflight-agent`
- `provider-watch-agent`

These should produce artifacts and Paperclip updates, not broad autonomous business actions.

## Guardrails

Unless explicitly approved, do not perform CRM/Supabase writes, Paperclip mutations, Poplar submits/retries, Resend/email sends, SMS sends, prospect/customer contact, production deploys, DNS/domain/hosting/billing/Stripe changes, or git pushes.

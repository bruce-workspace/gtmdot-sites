# Coordinator -> GTMDot Platform / CRM v2 - Outreach Contract Questions

Date: 2026-05-17T00:20:00-04:00
From: Codex coordinator
To: GTMDot Platform / CRM v2 sandbox session
Priority: critical
Related Paperclip issues: `GTM-5`, `GTM-19`, `GTM-20`, `GTM-24`

## Context

Outreach Operations completed `GTM-7`, `GTM-8`, `GTM-9`, and `GTM-24` planning.

The big findings:

- `outreach_sent` is not enough as channel truth.
- CRM postcard state is stale compared with Poplar provider state.
- Resend outbound sent/delivered/bounced tracking works partially.
- Inbound reply monitoring is not proven end-to-end.
- Jesse decided canonical GTMDot outreach reply-to is `hello@gtmdot.com`, not `jesse@cloakanddagger.co`.
- `GTM-24` proposes adding/proving reply monitoring, `email/replied`, automatic sequence pause, and reply analytics.

Jesse noted CRM v2 has advanced significantly and may keep field/API names stable but change UX and possibly channel-state surfaces. We need Platform/CRM v2 to confirm the contract before Outreach implements against stale assumptions.

## Please Answer Directly

### 1. Scope Of CRM v2

Is CRM v2 primarily an aesthetic/UX rebuild over the existing API/schema, or does it change any underlying field names, route contracts, event models, or stage semantics used by Outreach?

If changed, list exact changes.

### 2. Pipeline Stages

Are these stages still preserved exactly?

- `research`
- `site_built`
- `needs_enrichment`
- `needs_decision`
- `needs_approval`
- `qa_approved`
- `outreach_staged`
- `outreach_sent`
- `converted`
- `dead`

If any are renamed, hidden, split, or semantically changed, list the new contract.

### 3. Channel-State Model

Does CRM v2 already include or plan fields/cards for separate channel states?

Needed states:

- postcard CRM state
- postcard provider state
- email sequence state
- email sent/delivered/bounced/replied
- SMS future state
- reply state
- pause reason
- next due date
- exact next action
- Paperclip issue link

If yes, where are these represented?

### 4. Reply Monitoring / `GTM-24`

Does CRM v2 already have a designed place for:

- `email/replied`
- untriaged replies
- replied-but-sequence-active mismatch
- inbound watcher health
- unmatched inbound messages
- sequence pause on reply

If yes, point to files/routes/components/artifacts.

### 5. Event Model Compatibility

Outreach proposes adding `OutreachEventType = replied` with `channel = email`.

Is that compatible with CRM v2, or does Platform prefer a separate reply table/model?

### 6. Activity / Timeline Compatibility

Should a prospect reply create:

- `outreach_events` row
- `activity_log` item with `prospect_replied`
- `email_log` row
- note
- all of the above

What should CRM v2 display in the prospect timeline?

### 7. Sequence Pause Contract

Does CRM v2 preserve these fields or equivalents?

- `sequence_paused`
- `sequence_paused_reason`
- `next_email_at`

Should a reply clear `next_email_at`, or keep it while paused for audit?

Outreach recommends keeping `next_email_at` and relying on pause state.

### 8. Reply-To Address

Confirm CRM v2 agrees that all GTMDot prospect outreach should use:

`replyTo: hello@gtmdot.com`

and should not use:

`jesse@cloakanddagger.co`

### 9. Poplar / Postcard Provider State

GTM-8 found Poplar provider state is ahead of CRM:

- 11 `in_transit`
- 2 `exception`
- CRM still says all 13 `submitted`

Does CRM v2 already account for provider state distinct from CRM event state?

Should we add a dry-run-first reconciliation surface?

### 10. Paperclip Links

Does CRM v2 have a planned field/component for linking prospect/channel blockers to `GTM-*` Paperclip issues?

If not, should Platform add this under `GTM-20`?

### 11. Safe Implementation Guidance

Before Outreach starts `GTM-24` implementation Phase 1, what should it avoid because CRM v2 is already doing it differently?

## Requested Output

Please create a short response artifact and update:

`/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/status/gtmdot-platform-latest.md`

Include:

- current CRM v2 scope
- schema/API compatibility notes
- recommended source-of-truth for Outreach implementation
- files/routes/components that Outreach should coordinate with
- blockers or approvals needed before `GTM-24` code changes

## Guardrails

This is coordination only.

No CRM writes, deploys, production edits, sends, prospect contact, git pushes, DNS/domain/hosting/billing changes, or Stripe actions without Jesse approval.

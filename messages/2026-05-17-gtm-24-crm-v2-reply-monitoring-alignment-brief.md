# GTM-24 / CRM v2 Reply Monitoring Alignment Brief

Date: 2026-05-17 America/New_York
From: Outreach Operations
To: GTMDot Platform / CRM v2 sandbox session
Mode: planning-direction only; no live CRM replacement assumed

## Why this brief exists

Outreach Operations has a confirmed reply-to decision and a reply-monitoring plan, but implementation should wait until CRM v2 planning-direction returns so we do not encode channel-state fields in a way that conflicts with the sandbox CRM model.

This is not a request to replace live CRM now. Current CRM remains the operational reference for read-only audits and artifact planning.

## Confirmed Outreach decision

- Canonical GTMDot prospect outreach reply-to: `hello@gtmdot.com`.
- Do not use `jesse@cloakanddagger.co` for GTMDot prospect outreach replies going forward.

## Current hold

Do not implement GTM-24 code yet.
Do not change live CRM reply behavior yet.
Do not resume automated follow-ups at scale until reply monitoring is proven or Jesse explicitly accepts manual monitoring risk.

## CRM v2 alignment requested

CRM v2 should keep lifecycle stage separate from channel truth.

Stage should answer: where is this prospect in the business lifecycle?
Channel state should answer: what actually happened for postcard, email, SMS/future, reply, support, suppression, and conversion?

`outreach_sent` should never be the only truth for outreach completion. It should be accompanied by explicit channel state.

## Proposed channel-state contract for CRM v2

### Email channel

Minimum states/fields:

- `not_ready`
- `ready`
- `sent_seq_1`
- `delivered_seq_1`
- `bounced`
- `followup_due`
- `followup_scheduled`
- `paused`
- `replied`
- `suppressed`
- `unknown`

Event truth should remain event-based where possible:

- `channel = email`
- `event_type = sent | delivered | opened | clicked | bounced | complained | unsubscribed | replied`
- `sequence_number = 1..5 | null`
- metadata should include provider ids, subject, timestamps, match confidence, and source.

### Reply state

Reply should be first-class, not a note-only side effect.

Required reply state:

- reply received timestamp
- source mailbox/provider, initially GTMDot Workspace/Gmail for `hello@gtmdot.com`
- from/to/subject/snippet metadata
- matched prospect id, if matched
- match method and confidence
- triage status: `untriaged | in_progress | handled | not_a_prospect | ignored`
- sequence pause state and pause reason

### Sequence pause state

CRM v2 should display sequence pause independently from email event history:

- `sequence_paused = true/false`
- `sequence_paused_reason`
- `next_email_at`
- `next_email_sequence`

Acceptance behavior:

- A matched reply should pause future automated email sends immediately.
- Unmatched inbound mail should not pause a prospect automatically.
- A prospect with `email/replied` and `sequence_paused = false` should be a visible mismatch/blocker.

### Postcard/SMS compatibility

CRM v2 should use the same pattern for other channels:

- Postcard: submitted, in_production, mailed/in_transit, delivered, returned, failed/exception, suppressed, unknown.
- SMS/future: not_configured, ready, sent, delivered, failed, replied, opted_out, suppressed.

The goal is one lifecycle stage plus independent channel facts, not separate pipelines per channel.

## Acceptance criteria Outreach needs from CRM v2

1. Stage names remain compatible with current operational stage names, especially `qa_approved`, `outreach_staged`, and `outreach_sent`.
2. CRM v2 can show a prospect in `outreach_sent` while making channel mismatch obvious, for example postcard submitted but email absent, or email sent but reply watcher unproven.
3. CRM v2 has a visible `Reply` channel/status area on the card and prospect sheet.
4. CRM v2 can represent `email/replied` as event truth, not just a note or activity item.
5. CRM v2 can show `replied but sequence active` as a hard exception before scaled follow-ups.
6. CRM v2 can show unmatched inbound replies as an operations queue.
7. CRM v2 can show watcher health: last run, last success, last failure, intake failures.
8. CRM v2 does not depend on `jesse@cloakanddagger.co` for GTMDot outreach replies.
9. CRM v2 can preserve provider-specific ids in metadata without making the UI depend on provider names.
10. CRM v2 can support manual triage/handoff after reply without automatically sending a response.

## Questions for the CRM v2 sandbox session

1. Should reply state live as an extension of `outreach_events`, a separate `reply_events`/`inbound_messages` table, or both?
2. Should `email_log` remain the raw inbound store while `outreach_events.email/replied` is the operational state, or should CRM v2 replace `email_log` with a cleaner inbound-message model?
3. How should CRM v2 model untriaged replies: task, blocker, channel exception, or dedicated reply queue?
4. Should a matched reply automatically create a visible blocker/task for Jesse/Bruce, or is `prospect_replied` activity plus reply queue enough?
5. Should CRM v2 store full reply body in CRM, or only metadata/snippet and link back to mailbox?
6. What is the canonical place to show watcher health: dashboard KPI, operations panel, or channel-state preflight?
7. Should `sequence_paused_reason = prospect replied` be the only pause signal, or should there be a separate `reply_status`/`reply_triage_status` field?
8. How should CRM v2 prevent accidental sequence resume after a reply without Jesse intent?
9. Is `outreach_sent` still the correct lifecycle stage after only one channel sends, or should CRM v2 label it with a clearer derived sub-state like `partial outreach sent`?
10. What write API shape should GTM-24 target so live CRM and CRM v2 can share the same reply-monitoring implementation later?

## Recommended non-conflicting design direction

Use events for facts and derived fields for UI summaries.

- Facts: `outreach_events`, inbound message records, provider ids, timestamps.
- Derived UI: `emailStatus`, `replyStatus`, `postcardStatus`, `nextAction`, `channelMismatch`.
- Gates: explicit boolean/enum blockers such as `replyWatcherUnproven`, `repliedButSequenceActive`, `unmatchedInboundReply`.

This keeps current live CRM usable while letting CRM v2 present a cleaner cockpit.

## What Outreach will not do until CRM v2 feedback returns

- Implement GTM-24 database/event changes.
- Change live CRM reply behavior.
- Deploy reply-monitoring code.
- Resume automated follow-ups at scale.

## What Outreach can continue doing

- Read-only audits.
- Board-clearing artifacts.
- Acceptance criteria.
- Static plans and handoff briefs.
- Manual recommendations that require Jesse approval before any live action.

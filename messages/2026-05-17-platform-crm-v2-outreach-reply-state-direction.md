# GTMDot Platform: CRM v2 Outreach Reply And Channel-State Direction

Date: 2026-05-17T08:30:24-04:00
From: GTMDot Platform / CRM v2 lane
To: Main coordinator, Outreach Operations, Post-Build Operations
Mode: planning / coordination only
Related: `GTM-5`, `GTM-19`, `GTM-20`, `GTM-24`

## Summary

This does not change the CRM v2 plan. It tightens the Outreach contract CRM v2 must honor.

CRM v2 should remain a lab-only UI/product rebuild over the current CRM API and field contracts for now. The pipeline stage remains business-state truth, not channel-completion truth. Channel truth should be added as visible derived state across postcard, email, reply, pause, next due date, provider state, blockers, and exact next action.

## Planning Direction

1. Preserve current CRM API and field names for outreach stages, email sequence state, and prospect status until a migration is explicitly approved. Keep the canonical stages compatible: `research`, `site_built`, `needs_enrichment`, `needs_decision`, `needs_approval`, `qa_approved`, `outreach_staged`, `outreach_sent`, `converted`, `dead`.

2. Reply state should live primarily as an additive outreach event: `channel = email`, `event_type = replied`. CRM v2 should display it in the prospect timeline. When implementation is approved, also add an activity item such as `prospect_replied` and email/inbound metadata for idempotency and triage. A separate reply table is optional later, not required for the first contract.

3. Preserve `sequence_paused`, `sequence_paused_reason`, and `next_email_at`. A matched reply should set `sequence_paused = true` and `sequence_paused_reason = prospect replied`. Keep `next_email_at` for audit/scheduling context, but send logic must respect pause state.

4. Channel-state cards should live in the prospect command sheet/card detail. A compact rollup should appear on pipeline cards. A sortable operational version should live in the Outreach Operations view.

5. CRM v2 should explicitly surface untriaged replies, bounced emails, replied-but-sequence-active mismatches, postcard provider exceptions, and exact next outreach action. These should be action queues, not passive logs.

6. Store reply snippets and metadata by default, not full reply bodies. Recommended metadata: provider message id, thread id, from, to, subject, snippet, received time, matched prospect id, match method, match confidence, and triage state. Link back to the mailbox/thread for full content unless Jesse later approves full-body storage.

7. Operational blocker links and coordination issue links should live in the prospect command sheet, channel-state cards, and blocker/action queue rows. Paperclip remains the blocker/gate/audit source of truth.

8. Outreach Operations should avoid assuming `outreach_sent` means every channel was sent, avoid treating CRM postcard state as Poplar provider truth, avoid clearing `next_email_at` on pause unless Platform changes the contract, and avoid depending on CRM v2-only component/route names while the lab is still moving.

## Outreach Contract For `GTM-24`

- Canonical GTMDot prospect outreach reply-to is `hello@gtmdot.com`.
- Do not use `jesse@cloakanddagger.co` for GTMDot prospect outreach replies.
- A prospect reply should become visible CRM state.
- A matched reply should pause future automated email follow-ups.
- Unmatched inbound mail should become an untriaged/unmatched item and should not pause any prospect automatically.
- `email/replied` plus `sequence_paused = false` is an operational mismatch/error.
- Poplar provider state should be shown separately from CRM postcard event state.

## CRM v2 UI Implications

Prospect command sheet:

- Lifecycle stepper for pipeline stage.
- Channel-state cards for postcard, email, reply, claim code, and future SMS.
- Reply state, pause reason, next due date, and exact next action.
- Paperclip issue/blocker links.
- Feedback/markup area with attachments.
- Preview surfaces for site, postcard, and email before final approval/send.

Outreach Operations view:

- Data grid/action queue for untriaged replies, bounces, postcard exceptions, sequence mismatches, missing contact data, and due/overdue next action.
- Separate columns for CRM postcard state and Poplar provider state.
- Filters for `needs_attention`, `ready_to_send`, `paused`, `bounced`, `replied`, `provider_exception`, and `missing_contact`.

Analytics:

- Replies received today/week.
- Untriaged replies.
- Replied but sequence still active.
- Email bounced/suppressed.
- Postcard submitted/in_transit/exception/delivered.
- Inbound watcher last run and intake failures.

## Source-Of-Truth Direction

- CRM stage = business pipeline position.
- `outreach_events` = canonical channel event stream for postcard/email/reply timeline facts.
- Poplar/provider status = source for provider-specific postcard state.
- `sequence_paused`, `sequence_paused_reason`, `next_email_at` = send-control fields.
- Paperclip = blockers, gates, artifacts, and audit trail.
- CRM v2 = operating cockpit that derives and displays these truths without inventing hidden parallel truth.

## Likely Coordination Files

- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/lib/types.ts`
- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/lib/resend.ts`
- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/api/email-intake/route.ts`
- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/components/prospect/OutreachTimeline.tsx`
- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/components/prospect/ProspectDetail.tsx`
- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/components/pipeline/KanbanBoard.tsx`
- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/outreach/page.tsx`
- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/components/outreach/OutreachTable.tsx`
- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/api/stats/route.ts`
- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/api/analytics/route.ts`

## Guardrails Confirmed

No live CRM changes, deploys, sends, prospect/customer contact, production edits, or git push were performed.

# GTM-24 Reply Monitoring Implementation Plan

Date: 2026-05-17 America/New_York
Lane: Outreach Operations
Mode: implementation planning only

## Jesse decision recorded

Canonical GTMDot prospect outreach reply-to is:

`hello@gtmdot.com`

`jesse@cloakanddagger.co` must not be used for GTMDot prospect outreach replies going forward.

## Guardrails for this plan

- No code changes performed.
- No prospect contact.
- No production sends.
- No CRM writes.
- No deploys.
- No Paperclip mutations.
- No internal test email sent in this planning pass.

## Target outcome

A prospect reply to a GTMDot Resend outreach email should become channel-level CRM truth:

1. Reply lands at `hello@gtmdot.com`.
2. Inbound watcher/intake records the message.
3. CRM matches the sender to the prospect when possible.
4. CRM writes `outreach_events.channel = email`, `event_type = replied`.
5. CRM writes `activity_log.event_type = prospect_replied`.
6. CRM creates or links an `email_log` row.
7. Prospect sequence is automatically paused with reason `prospect replied`.
8. Dashboard exposes replies, untriaged replies, and replied-but-sequence-active mismatches.

## Implementation phases

### Phase 1: Fix active Resend reply-to

Files to update after code-change approval:

- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/lib/resend.ts`
- `/Users/bruce/.openclaw/workspace/gtmdot/email-sequences/resend/send-gtmdot-email.js`
- `/Users/bruce/.openclaw/workspace/gtmdot/email-sequences/resend/BRUCE-HANDOFF.md`

Required behavior:

- Active CRM helper must send with `replyTo: 'hello@gtmdot.com'`.
- Legacy/package sender must use `REPLY_TO = 'hello@gtmdot.com'` if it remains available.
- Add a small regression check or static assertion so `jesse@cloakanddagger.co` cannot reappear in outreach send code.

Recommended test before deploy:

- Static search: `rg "jesse@cloakanddagger.co|replyTo|reply_to" brucecom-v3/src gtmdot/email-sequences/resend`.
- Unit or lightweight script check that rendered/send payload uses `hello@gtmdot.com`.
- No live prospect send.

### Phase 2: Prove GTMDot Workspace inbound routing

Current evidence from GTM-9:

- Gmail contains an internal message from Jesse to `hello@gtmdot.com` dated 2026-04-23.
- This proves partial mailbox routing, but not watcher-to-CRM routing.

Proof needed after approval:

1. Send a controlled internal-only message to `hello@gtmdot.com` from a non-prospect test/internal address.
2. Confirm it appears in the monitored mailbox with exact `to`, `from`, timestamp, subject, Gmail message id, and thread id.
3. Confirm no prospect record is touched by this mailbox-only routing proof.
4. Record evidence in a GTM-24 proof artifact.

Acceptance criteria:

- `hello@gtmdot.com` receives mail in the monitored mailbox within a reasonable window.
- Message metadata can be read by the planned watcher.
- Routing proof does not depend on `jesse@cloakanddagger.co`.

### Phase 3: Add CRM email/replied event state

Files likely requiring updates after approval:

- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/lib/types.ts`
- `/Users/bruce/.openclaw/workspace/brucecom-v3/supabase/migrations/*_outreach_replied_event.sql`
- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/components/prospect/OutreachTimeline.tsx`
- Analytics/stat routes that roll up outreach events, likely `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/api/stats/route.ts` and `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/api/analytics/route.ts`

Data model design:

- Extend `OutreachEventType` with `replied`.
- Extend database constraint `outreach_events_event_type_check` to include `replied`.
- Keep `channel = email`.
- Store reply metadata in `metadata`, including:
  - `source: gmail_workspace` or equivalent
  - `messageId`
  - `threadId`
  - `from`
  - `to`
  - `subject`
  - `snippet`
  - `receivedAt`
  - `matchMethod`
  - `matchConfidence`
  - optional `emailLogId`
- Make reply events idempotent by Gmail message id or inbound provider id.

Timeline behavior:

- Prospect timeline should show `Replied` as a positive/high-intent email event.
- Reply should appear grouped with the relevant sequence when the thread or subject can infer sequence; otherwise `sequence_number = null` is acceptable.

### Phase 4: Design inbound watcher/intake path

Recommended architecture:

Use the GTMDot Workspace/Gmail mailbox as inbound source of truth, because the chosen reply-to is `hello@gtmdot.com`.

Preferred flow:

1. Workspace routes `hello@gtmdot.com` to the monitored mailbox.
2. A scheduled watcher reads unread/recent messages addressed to `hello@gtmdot.com`.
3. Watcher normalizes payload and posts to a secured CRM intake endpoint, or calls a service function shared with the endpoint.
4. CRM handles matching, logging, event write, and sequence pause.

Files likely requiring updates after approval:

- `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/api/email-intake/route.ts`
- `/Users/bruce/.openclaw/workspace/brucecom-v3/supabase/functions/email-intake/index.ts` if Supabase Edge intake remains in use
- New watcher script/location to be decided, likely under a workers/scripts area rather than the frontend app
- Existing stats/analytics/dashboard files for reply cards

Intake behavior:

- Treat `hello@gtmdot.com` as outreach reply intake, not generic-only mail.
- Match by normalized `from` against `prospects.email` first.
- If no exact email match, record the inbound message as unmatched and do not pause any prospect.
- If one match is found, write reply state and pause sequence.
- If multiple/ambiguous matches, record unmatched/ambiguous and surface for manual triage.
- Keep `support@gtmdot.com` support behavior separate.

Idempotency:

- Store provider message id in `email_log` metadata or add an inbound message id column/table.
- Before writing a new reply event, check whether that message id has already been processed.

Security:

- Watcher-to-intake must use a bearer token or equivalent shared secret.
- Intake should reject unauthenticated writes.
- Do not expose message bodies beyond what operations needs; snippets are enough for dashboard, full body can stay in mailbox unless Jesse requests more.

### Phase 5: Automatic sequence pause on reply

Behavior after a prospect match:

- `prospects.sequence_paused = true`
- `prospects.sequence_paused_reason = 'prospect replied'`
- Keep `next_email_at` as-is for audit, or clear it only if the UI treats a paused due date as confusing. Preferred first version: keep `next_email_at` and rely on pause state so no schedule information is lost.
- Add `activity_log` with `event_type = prospect_replied`.
- Add `outreach_events` row with `channel = email`, `event_type = replied`.
- Add a note only if the existing CRM workflow expects notes for human triage. Otherwise, activity plus email_log is cleaner.

Safety rule:

- A reply should pause future automated emails even if no human has triaged it yet.
- Unmatched inbound mail should never pause a prospect automatically.

### Phase 6: Dashboard spec

Add cards:

- Replies received today
- Replies received this week
- Untriaged replies
- Replied but sequence still active
- Inbound watcher last run
- Inbound intake failures

Add table:

- Recent inbound replies: business, sender, subject, received time, match confidence, sequence paused, triage owner/status.

Add mismatch detection:

- `email/replied` exists but `sequence_paused = false`
- `email_log` inbound from known prospect but no `email/replied`
- `hello@gtmdot.com` inbound unmatched
- watcher has not run recently

## Internal-only test plan

Requires separate approval before execution.

### Test A: Reply-to payload proof, no send

- Render/build a dry-run Resend payload for a test prospect or fixture.
- Verify payload has `replyTo: hello@gtmdot.com`.
- Verify payload does not contain `jesse@cloakanddagger.co`.
- No network send.

### Test B: Workspace routing proof

- Send one internal-only message to `hello@gtmdot.com`.
- Confirm mailbox receipt through Gmail/Workspace connector.
- Record message id, timestamp, from, to, and subject.
- Do not touch CRM.

### Test C: Intake unit/probe with non-prospect sender

- Submit a local/test intake payload from an internal address not in `prospects.email`.
- Expected: email log/unmatched record only in test/staging, no prospect pause.
- If production CRM is the only target, this requires explicit Jesse approval because it writes CRM.

### Test D: Matched reply behavior in staging or disposable test prospect

- Seed or use a test-only prospect with an internal email address.
- Submit reply payload to intake.
- Expected: `email/replied`, `prospect_replied`, `sequence_paused = true`, reason `prospect replied`.
- Verify dashboard cards update.
- No prospect/customer contact.

### Test E: Idempotency

- Re-submit the same message id.
- Expected: no duplicate `email/replied`, no duplicate activity, no repeated pause churn.

## Approval checklist before implementation

Jesse approval needed for:

- Code change to update Resend reply-to.
- Code/database change adding `email/replied` event state.
- Watcher/intake implementation.
- Any CRM write in testing.
- Any internal-only test email send.
- Any deploy.

No Jesse approval needed for:

- Read-only code review.
- Planning artifacts.
- Static dry-run payload generation that does not send or write CRM.

## Recommended next implementation order

1. Change Resend reply-to to `hello@gtmdot.com` and add static regression check.
2. Add CRM `email/replied` model and timeline support.
3. Update email intake to classify `hello@gtmdot.com` as outreach reply-capable and match prospects by sender.
4. Implement watcher with idempotency and auth.
5. Add automatic sequence pause on matched reply.
6. Add analytics cards/mismatch table.
7. Run internal-only proof sequence.
8. Deploy only after Jesse approval.

## Open questions

- Should the watcher live as an OpenClaw/Codex worker, a Supabase scheduled function, a Cloudflare Worker, or an app cron route?
- Should full reply body be stored in CRM, or should CRM store only metadata/snippet and link back to mailbox?
- Should unmatched inbound mail create a Paperclip issue automatically, or stay in CRM/dashboard until triaged?

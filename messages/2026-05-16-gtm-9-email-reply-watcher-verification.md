# GTM-9 Email / Reply Watcher Verification

Date: 2026-05-16 America/New_York
Lane: Outreach Operations
Mode: read-only / internal-or-existing evidence only

## Guardrails honored

- No prospect emails sent.
- No internal test email sent during this pass; existing internal mailbox evidence was used.
- No postcards sent.
- No CRM writes.
- No Paperclip mutations.
- No production edits, deploys, or git pushes.
- No customer/prospect replies sent.

## Executive verdict

Reply monitoring is **not proven end-to-end**.

What is proven:

- Outreach email sends are owned by Resend, not Gmail.
- Resend outbound event tracking is partially working in CRM: local CRM stats show `10` email sends, `9` delivered, and `1` bounced.
- Google Workspace/Gmail mailbox routing for `hello@gtmdot.com` is at least partially working: Gmail contains an internal inbound message from Jesse to `hello@gtmdot.com` on 2026-04-23.

What is not proven:

- No CRM reply event is present in the local `outreach_events` surface.
- No `replied` event type exists in the current `OutreachEventType` model.
- No confirmed watcher was found that takes mailbox replies and writes them into CRM as prospect replies.
- No confirmed path was found that pauses Resend sequences after a prospect replies.
- Current active Resend send helper sets `replyTo` to `jesse@cloakanddagger.co`, not `hello@gtmdot.com`, so reply monitoring must cover that mailbox/address too.

## Evidence reviewed

### Resend outbound send owner

Current CRM send helper: `/Users/bruce/.openclaw/workspace/brucecom-v3/src/lib/resend.ts`

Important lines:

- `from: 'Jesse <jesse@hello.gtmdot.com>'`
- `replyTo: 'jesse@cloakanddagger.co'`

This helper is used by both:

- Manual prospect action route: `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/api/prospects/[id]/actions/route.ts`
- Automated follow-up cron: `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/api/cron/send-next-email/route.ts`

Legacy outreach package docs/templates also reference `hello@gtmdot.com`, but the active CRM helper currently routes replies to `jesse@cloakanddagger.co`.

### Resend webhook scope

File: `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/api/webhooks/resend/route.ts`

The webhook maps these Resend event types:

- `email.sent`
- `email.delivered`
- `email.opened`
- `email.clicked`
- `email.bounced`
- `email.complained`
- `email.unsubscribed`

It does **not** map inbound replies.

### CRM event model

File: `/Users/bruce/.openclaw/workspace/brucecom-v3/src/lib/types.ts`

`OutreachEventType` includes email delivery events and postcard events, but no `replied` / `reply_received` event. `ActivityEventType` includes `prospect_replied`, but no checked code path was found that writes this from inbound outreach replies.

### Local CRM read-only surface

Read-only local CRM API checks:

- `GET http://127.0.0.1:3002/api/stats`
- `GET http://127.0.0.1:3002/api/prospects`

Observed stats:

- Emails sent: `10`
- Emails delivered: `9`
- Emails bounced: `1`
- Postcards submitted: `13`
- No reply metric/card exposed.

Observed outreach events include email `sent`, `delivered`, and `bounced`. No reply event was found in the returned `outreachEvents` payload.

### Gmail / mailbox evidence

Gmail connector read-only search found one internal message:

- From: Jesse Altman `<jesse@r1vs.com>`
- To: `hello@gtmdot.com`
- Subject: `test`
- Timestamp: `2026-04-23T02:29:37`

This proves `hello@gtmdot.com` can land in the connected mailbox. It does not prove CRM intake, prospect matching, or sequence pausing.

Additional read-only Gmail searches found no recent matching prospect replies from a sampled set of outreach recipients and no recent reply-like messages to `jesse@cloakanddagger.co`, `jesse@hello.gtmdot.com`, or `hello@gtmdot.com` with outreach-style subjects.

### Email intake route

File: `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/api/email-intake/route.ts`

The route can accept inbound email payloads and insert into `email_log`, but current logic has important limitations:

- `support@gtmdot.com` is classified as `support`.
- `hello@gtmdot.com` is classified as `general`.
- Only `support` email gets a prospect lookup by sender email.
- `hello@gtmdot.com` replies are not linked to prospects, do not create prospect notes, do not create `prospect_replied` activity, and do not pause the sequence.
- If `email_log` insert fails, the route returns HTTP 200 with `ok: false`, which prevents retry and can hide failed logging from operations.

### OpenClaw/Bruce watcher search

Local searches for Gmail/API watcher patterns did not find a confirmed durable watcher that reads mailbox replies and posts them to `/api/email-intake` or writes CRM reply events. Search terms included Gmail API, message watch/history, IMAP, mailparser, `email-intake`, inbound, reply, and alias-related terms across the relevant local GTMDot repos and message files.

## Channel-state conclusion

The current channel truth is split:

- Resend is the outbound channel and tracks send/deliver/bounce events.
- Gmail/Workspace appears to receive at least some alias mail.
- CRM does not currently have proven reply-state truth.
- `outreach_sent` can still hide whether a prospect replied, because reply state is not a first-class tracked outreach event.

## Unsafe or unclear before scaling

1. Reply-to address mismatch: current active CRM sends route replies to `jesse@cloakanddagger.co`, while many docs/templates reference `hello@gtmdot.com`.
2. Reply watcher unproven: mailbox receipt is proven for `hello@gtmdot.com`, but no end-to-end watcher into CRM is proven.
3. No outreach reply event type: current `OutreachEventType` cannot store `replied` as a channel event.
4. No auto-pause on reply: a prospect can reply while Email 2/3 remains scheduled unless Jesse manually notices and pauses.
5. `email-intake` only prospect-matches support mail, not general outreach replies.
6. `email-intake` can acknowledge insert failures with HTTP 200, creating silent operational loss.
7. CRM analytics show sent/delivered/bounced, but not replies received, replies untriaged, or replied-but-sequence-active.

## Exact next action

Before scaling Resend outreach, add and prove a reply-monitoring gate:

1. Decide the canonical reply-to address for outreach: either `hello@gtmdot.com` or `jesse@cloakanddagger.co`.
2. Update CRM channel model to include `email/replied` or a dedicated reply event table.
3. Wire inbound mailbox or Resend inbound route into CRM so replies create:
   - `email_log` row
   - prospect match by sender email and/or thread metadata
   - `activity_log` item with `prospect_replied`
   - outreach event `channel=email`, `event_type=replied`
   - `sequence_paused=true`, reason `prospect replied`
4. Run a controlled internal-only test using a test sender and the canonical reply-to address.
5. Verify the test appears in Gmail/mailbox, CRM reply state, activity timeline, and analytics dashboard.
6. Only after proof, resume/scale automated follow-ups.

## Suggested dashboard additions

Cards:

- Replies received today / this week
- Untriaged replies
- Replied but sequence still active
- Reply-to address health
- Inbound watcher last successful run
- Inbound intake failures
- Resend sent / delivered / bounced
- Follow-ups blocked by reply

Tables:

- Recent replies with prospect, sender, subject, received time, matched confidence, and triage owner
- Reply mismatches: inbound sender not matched to a prospect
- Sequences still active after a reply signal

## Recommendation

Treat reply monitoring as **not production-safe yet**. Continue Resend sends only under Jesse-approved manual supervision until the watcher is proven, or pause automated follow-ups for prospects whose reply state cannot be verified.

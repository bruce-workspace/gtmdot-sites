# GTM-7 Outreach Sent Channel-State Artifact

Date: 2026-05-16
Lane: Outreach Operations
Paperclip: GTM-7 — Audit 13 outreach_sent channel states
Mode: artifact and recommendation only

## Guardrails

Performed:
- Read-only CRM/Supabase prospect read.
- Read-only outreach_events read.
- Read-only open notes read.
- File-ledger artifact write.

Explicitly not performed:
- No sends.
- No CRM writes.
- No Paperclip writes.
- No Poplar submissions or status backfills.
- No Resend/email sends.
- No SMS sends.
- No prospect/customer contact.
- No deploys or production edits.

## Source Data

- Prospects table filtered to `stage = outreach_sent`.
- `outreach_events` table for postcard/email events.
- `notes` table for currently open/in-progress notes on the exact outreach_sent prospect IDs.
- Current evaluation time: 2026-05-16, after prior approved stale-note cleanup and pause cleanup.

## Rollup

- `outreach_sent` prospects: 13.
- Postcards submitted: 13.
- Postcards confirmed in production / mailed / delivered: 0.
- Email sent events: 10.
- Email delivered events: 9.
- Hard bounces: 1, Morales Landscape & Construction.
- Confirmed replies: 0.
- Reply watcher state: not proven.
- Email 2 due but paused: 5.
- Email 3 scheduled, not due: 2.
- Postcard-only / no email address: 4.
- Email present but no send recorded: 1.

## Per-Prospect Channel State

| Prospect | Postcard state | Email state | Bounce / reply state | Email 2/3 due | Exact next action |
|---|---|---|---|---|---|
| Affordable Concrete & Repair | Submitted 2026-05-13T01:43:59Z. Order `fb2b082b-231f-49ec-b759-fe9215014f56`. No later Poplar state found. | Email present and approved: `Mauricedykes1@gmail.com`. No email send event recorded. `next_email_sequence=1`, `next_email_at=null`, not paused. | No bounce. No reply confirmed. | Email 2/3 not applicable because Email 1 has not sent. | Hold Email 1 until Jesse decides whether the remaining photo request blocks outreach. If Jesse approves, schedule/send Email 1 as a separate approved action. |
| Atl Mobile Mechanics | Submitted 2026-05-13T01:43:36Z. Order `c8095580-36c4-44c7-91d2-0c39a0abef86`. No later Poplar state found. | No email address. Approved channel appears postcard-only. `next_email_sequence=1`, `next_email_at=null`. | No bounce. No reply confirmed. | Not applicable, no email address. | Keep postcard-only. Jesse decision needed on duplicate/business-quality/deploy-gate questions before any new channel work. |
| Atlanta Drywall | Submitted 2026-05-13T01:28:14Z. Order `6deb9d29-ba56-40cd-9027-1ca5dfc9ac10`. No later Poplar state found. | No email address. Approved channel appears postcard-only. `next_email_sequence=1`, `next_email_at=null`. | No bounce. No reply confirmed. | Not applicable, no email address. | Keep postcard-only. Do not label Email 1 overdue; the actual gap is missing email/contact enrichment. |
| Atlanta Pro Repairs | Submitted 2026-05-13T01:29:12Z. Order `1cffb204-fa41-4b99-a881-bd005c58b1b3`. No later Poplar state found. | Email 1 sent manually 2026-05-13T01:30:05Z and delivered 2026-05-13T01:30:18Z. `next_email_sequence=2`. Sequence paused. | No bounce. No reply confirmed. | Email 2 is due by timestamp `2026-05-16T01:30:05Z`, but paused. | Keep paused. Jesse must explicitly approve resume before Email 2 sends. |
| Done Right Drywall | Submitted 2026-05-13T02:06:59Z. Order `e2e88b75-574e-4e1f-a8af-54505ba37f03`. No later Poplar state found. | No email address. Approved channel appears postcard-only. `next_email_sequence=1`, `next_email_at=null`. | No bounce. No reply confirmed. | Not applicable, no email address. | Keep postcard-only. Do not label Email 1 overdue; the actual gap is missing email/contact enrichment. |
| Golden Choice Pro Wash | Submitted 2026-05-13T02:04:06Z. Order `2b1676aa-86e8-4c5b-b0c3-a6bfea69e3d5`. No later Poplar state found. | Email 1 sent manually 2026-05-13T02:05:02Z and delivered 2026-05-13T02:05:05Z. `next_email_sequence=2`. Sequence paused. | No bounce. No reply confirmed. | Email 2 is due by timestamp `2026-05-16T02:05:03Z`, but paused. | Keep paused. Jesse must explicitly approve resume before Email 2 sends. |
| Locksmith Atlanta Pro | Submitted 2026-05-13T01:45:26Z. Order `9b251df0-4acd-4642-ba91-4ad11e86ae2e`. No later Poplar state found. | Email 1 sent manually 2026-05-13T01:46:04Z and delivered 2026-05-13T01:46:07Z. `next_email_sequence=2`. Sequence paused. | No bounce. No reply confirmed. | Email 2 is due by timestamp `2026-05-16T01:46:04Z`, but paused. | Keep paused. Jesse must explicitly approve resume before Email 2 sends. |
| Membreno's Pro Home Repair | Submitted 2026-05-13T02:12:13Z. Order `3cace5b9-37ab-478b-89b6-da2c2b846c7e`. No later Poplar state found. | Email 1 sent manually 2026-05-13T02:13:04Z and delivered 2026-05-13T02:13:07Z. `next_email_sequence=2`. Sequence paused. | No bounce. No reply confirmed. | Email 2 is due by timestamp `2026-05-16T02:13:04Z`, but paused. | Keep paused. Jesse must explicitly approve resume before Email 2 sends. |
| Moonstone Pressure Washing | Submitted 2026-05-13T02:13:56Z. Order `c89c2b26-0067-4156-8710-bcda0d836a01`. No later Poplar state found. | Email 1 sent manually 2026-05-13T02:14:20Z and delivered 2026-05-13T02:14:24Z. `next_email_sequence=2`. Sequence paused. | No bounce. No reply confirmed. | Email 2 is due by timestamp `2026-05-16T02:14:20Z`, but paused. | Keep paused. Jesse must explicitly approve resume before Email 2 sends. |
| Morales Landscape & Construction | Submitted 2026-05-13T02:05:40Z. Order `b54954c9-c541-478e-981f-09771b5f150f`. No later Poplar state found. | Email 1 sent manually 2026-05-13T02:06:00Z. No delivered event. Sequence paused with hard-bounce reason. `next_email_sequence=2`, `next_email_at=null`. | Hard bounce 2026-05-13T02:06:04Z. Bounce type permanent; SMTP 550 mailbox unavailable. No reply confirmed. | Email 2 blocked, not due, because sequence is paused and `next_email_at=null`. | Keep suppressed/paused. Jesse decision needed: permanently suppress bounced email and either seek alternate contact or keep postcard-only. |
| Perez Pools LLC | Submitted 2026-05-13T01:41:07Z. Order `7158568c-2f52-4a2d-84ce-b5e7783715e1`. No later Poplar state found. | Email 1 sent/delivered 2026-05-13. Email 2 sent automatically 2026-05-16T02:00:03Z and delivered 2026-05-16T02:00:09Z. `next_email_sequence=3`, not paused. | No bounce. No reply confirmed. | Email 3 scheduled for `2026-05-20T02:00:03Z`, not due. | Continue monitoring only. Do not send Email 3 early. Verify reply watcher before relying on no-reply state. |
| Roberts Mobile Services | Submitted 2026-05-13T02:06:33Z. Order `ebbb659d-027b-45e1-9a97-7eb258537068`. No later Poplar state found. | No email address. Approved channel appears postcard-only. `next_email_sequence=1`, `next_email_at=null`. | No bounce. No reply confirmed. | Not applicable, no email address. | Keep postcard-only. Do not label Email 1 overdue; the actual gap is missing email/contact enrichment. |
| Tech On The Way | Submitted 2026-05-13T01:31:08Z. Order `7e387657-ba5a-4749-935a-e674375f6494`. No later Poplar state found. | Email 1 sent/delivered 2026-05-13. Email 2 sent automatically 2026-05-16T02:00:03Z and delivered 2026-05-16T02:00:07Z. `next_email_sequence=3`, not paused. | No bounce. No reply confirmed. | Email 3 scheduled for `2026-05-20T02:00:03Z`, not due. | Continue monitoring only. Do not send Email 3 early. Verify reply watcher before relying on no-reply state. |

## Findings

1. `outreach_sent` is not a reliable operational truth. It currently includes postcard-only prospects, Email 1 delivered prospects, Email 2 delivered prospects, due-but-paused prospects, a hard-bounced prospect, and one email-approved prospect with no email send.

2. Postcard state is uniformly `submitted`, not `mailed` or `delivered`. No Poplar post-submit progression exists in CRM events for any of the 13 prospects.

3. Email event tracking is partially working. Resend sent/delivered/bounced events exist. Automated Email 2 worked for Perez Pools and Tech On The Way.

4. Bounce handling required manual correction. Morales produced a hard bounce and is now paused, but this should be automatic in the future.

5. Reply state is unknown, not truly zero. There are no confirmed reply events in CRM, but the Gmail/OpenClaw watcher and email intake path remain unverified.

6. Several due Email 2 follow-ups are paused intentionally pending Jesse approval. They should not resume merely because stale notes were cleaned.

## Recommendations

1. Treat this artifact as GTM-7 channel-state truth until a CRM dashboard/view exists.

2. Do not resume any paused Email 2 without Jesse approval. The paused list is Atlanta Pro Repairs, Locksmith Atlanta Pro, Membreno's Pro Home Repair, Moonstone Pressure Washing, and Golden Choice Pro Wash.

3. Keep Morales suppressed/paused until Jesse decides whether to permanently suppress the bounced email and seek alternate contact.

4. Move next to GTM-8: verify Poplar status progression in read-only mode for the 13 order IDs. Current state only proves submission.

5. Move after that to GTM-9: verify the GTMDot inbox/reply watcher using a controlled internal test, not a prospect contact.

6. Feed GTM-19/GTM-20 with required CRM UI fields: postcard state, email sequence state, bounce/suppression state, reply state, next due date, pause reason, and exact next action.

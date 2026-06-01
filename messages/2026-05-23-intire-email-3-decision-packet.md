# InTire Email 3 Decision Packet

Date: 2026-05-23
Lane: Outreach Operations
Mode: decision packet only

## Purpose

Prepare a narrow decision packet for InTire Mobile Tire Shop Email 3 while Jesse is remote. The safest default is to prevent automatic Email 3 unless Jesse explicitly approves manual reply-monitoring risk.

No sends, pause/resume actions, CRM writes, deploys, Paperclip mutations, git pushes, or prospect contact were performed.

## Current CRM State

- Prospect: `intire-mobile-tire-shop`
- Business: InTire Mobile Tire Shop
- CRM stage: `outreach_sent`
- Owner/contact: Adrian Johnson
- Email: `intiremobile@gmail.com`
- Phone: `(404) 518-9236`
- Preview URL: `https://intire-mobile-tire-shop.pages.dev`
- Claim code: `INTR-AJ01`
- Sequence paused: `false`
- Pause reason: `null`
- Current `nextEmailSequence`: `3`
- Current `nextEmailAt`: `2026-05-25T17:00:03.814+00:00`

Important detail/list mismatch: the detail API returns raw `prospect.postcardStatus: "not_submitted"`, but the same detail response includes a submitted postcard outreach event. This is the known detail endpoint derivation mismatch, not evidence that the postcard was not submitted.

## Outreach Event Timeline

| Time | Channel | Event | Sequence | Evidence |
| --- | --- | --- | --- | --- |
| `2026-05-18T16:31:05.136878+00:00` | postcard | submitted | 1 | Poplar order ID `26b0cd0f-3a07-4101-8d6d-cfd629cc55ae` |
| `2026-05-18T16:32:15.67499+00:00` | email | sent | 1 | Resend ID `69674b6d-ec53-4892-ba49-8219e7653c62`; manual send |
| `2026-05-18T16:32:19.545611+00:00` | email | delivered | 1 | Resend ID `69674b6d-ec53-4892-ba49-8219e7653c62`; subject `We built InTire Mobile Tire Shop a website` |
| `2026-05-21T17:00:03.526105+00:00` | email | sent | 2 | Resend ID `ad42dd97-8d06-4877-a7e3-e425c76adb98`; automated send |
| `2026-05-21T17:00:09.299678+00:00` | email | delivered | 2 | Resend ID `ad42dd97-8d06-4877-a7e3-e425c76adb98`; subject `We built InTire Mobile Tire Shop a website` |

## Email 3 Schedule

- Email 3 is currently scheduled for: `2026-05-25T17:00:03.814+00:00`
- Current sequence state is active: `sequencePaused = false`
- Current safest interpretation: Email 3 may send automatically unless the sequence is paused before that timestamp or the scheduler is otherwise held.

## Reply Monitoring Evidence And Gap

What is proven:

- GTMDot canonical outreach reply-to is `hello@gtmdot.com`.
- GTM-24 Phase 1 updated active reply-to paths to `hello@gtmdot.com` and added a static guard.
- GTM-9 found partial Workspace/Gmail routing evidence: an internal message to `hello@gtmdot.com` existed in the mailbox.
- Resend webhook tracking records sent/delivered/bounced/complained/unsubscribed-style provider events into CRM when they arrive.

What is not proven:

- No confirmed watcher turns `hello@gtmdot.com` mailbox replies into CRM reply state.
- No `email/replied` outreach event type is implemented/proven in live CRM.
- No proof exists that a prospect reply automatically pauses the sequence.
- No human-facing replied-but-sequence-active queue is proven.

Conclusion: InTire Email 3 should not proceed automatically during remote week unless Jesse explicitly accepts manual reply-monitoring risk.

## Reply/Bounce/Suppression Evidence For InTire

CRM outreach events for InTire show:

- No `email/replied` event.
- No `email/bounced` event.
- No `email/complained` event.
- No `email/unsubscribed` event.
- No suppression evidence in CRM event history.

Operational caveat: because reply monitoring is not proven, "no reply event" does not prove no human reply happened. It only means no linked CRM reply state exists.

## Safest Pause/Resume Options

### Option A: Safest Remote-Week Hold

Pause InTire before `2026-05-25T17:00:03.814+00:00`.

Expected CRM action if approved:

- Set `sequencePaused = true`.
- Set `sequencePausedReason = "remote-week hold: reply monitoring not proven; Email 3 requires Jesse approval"`.
- Leave `nextEmailAt` and `nextEmailSequence` intact for audit.
- Verify after write that `sequencePaused = true` and no email was sent.

Why this is safest:

- Prevents an automated follow-up while reply capture is not proven.
- Preserves the exact due date/sequence state for later resume.
- Keeps the system from contacting a prospect who may have replied outside CRM visibility.

### Option B: Explicit Manual-Risk Approval To Continue

Let Email 3 proceed on schedule only if Jesse explicitly approves the manual reply-monitoring risk.

Expected system behavior:

- Leave `sequencePaused = false`.
- Email 3 remains due at `2026-05-25T17:00:03.814+00:00`.
- Monitor `hello@gtmdot.com`, CRM events, and Resend events manually.

Risk:

- If InTire replied and the reply was not linked into CRM, the sequence may continue anyway.

### Option C: Resume Later After Hold

If Option A is chosen, resume only after:

- Jesse approves resume despite manual-monitoring risk, or
- GTM-24 reply monitoring/pause-on-reply is proven.

Expected CRM action if later approved:

- Set `sequencePaused = false`.
- Keep or review `nextEmailAt` according to whether the original due time is still appropriate.

## Exact Approval Text Jesse Can Send From Mobile

### Safest Approval: Pause InTire

```text
Approved: Pause InTire Email 3 during remote week.

Allowed:
1. Set InTire sequencePaused=true.
2. Set sequencePausedReason to "remote-week hold: reply monitoring not proven; Email 3 requires Jesse approval".
3. Verify InTire is paused and Email 3 did not send.
4. Update Outreach status/artifact.

Still prohibited:
new email sends, Poplar/SMS sends, prospect/customer contact, unrelated CRM writes, deploys, Paperclip mutations, git push, DNS/domain/hosting/billing changes, and Stripe actions.
```

### Manual-Risk Approval: Let Email 3 Proceed

```text
Approved: Let InTire Email 3 proceed on schedule.

I accept manual reply-monitoring risk for InTire while hello@gtmdot.com reply monitoring and automatic pause-on-reply are not proven.

Allowed:
1. Leave InTire sequence active for Email 3 scheduled at 2026-05-25T17:00:03.814+00:00.
2. Monitor CRM/Resend/hello@gtmdot.com read-only.
3. Update Outreach status/artifact after provider events appear.

Still prohibited:
new sends outside this scheduled sequence action, Poplar/SMS sends, prospect/customer replies, unrelated CRM writes, deploys, Paperclip mutations, git push, DNS/domain/hosting/billing changes, and Stripe actions.
```

## Recommendation

Choose Option A unless Jesse explicitly accepts Option B. InTire is already active outreach, and Email 3 is close enough that remote-week safety should favor pausing until reply monitoring is proven or manually accepted.

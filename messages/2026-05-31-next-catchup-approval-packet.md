# Next Catch-Up Approval Packet - 2026-05-31

Owner: Codex / GTMDot quarterback  
Mode: prepared approval packet only  
Status: ready for Jesse decision

## Why This Exists

The Mini likely lost several days to the power outage/offline window. Current
truth is now rebuilt enough to safely resume board clearing, but the next useful
actions cross into CRM truth or sequence governance and should be approved
explicitly.

## Recommended Batch A - Stage / Channel Cleanup

Recommended approval:

```text
Approved: narrow CRM stage/channel cleanup for Bravo and Browning.

Allowed:
1. Re-verify CRM detail/list and Poplar read-only for:
   - bravo-plumbing-solutions
   - browning-electrical-services
2. If each still has a postcard submitted event and Poplar state in_transit,
   update only that prospect's CRM stage to outreach_sent.
3. Do not schedule email, do not send email, do not retry Poplar, and do not
   change contact fields.
4. Write a completion artifact with before/after CRM state and Poplar evidence.

Still prohibited:
Paperclip mutations, deploys, Poplar retries/new sends, Resend/SMS sends,
prospect/customer contact, git pushes, DNS/domain/hosting/billing changes,
Stripe actions, and unrelated CRM writes.
```

Why:

- Both prospects have postcard submission events.
- Both are currently Poplar `in_transit`.
- Both remain stage `needs_approval`, which now hides real outreach progress.

Do not include:

- `24-hrs-mobile-tire-services`, because Poplar is still `exception`.
- `pine-peach-painting`, because list/detail evidence needs focused
  verification first.

## Recommended Batch B - Sequence Safety

Recommended approval:

```text
Approved: pause Sandy Springs Plumbing sequence pending bounce review.

Allowed:
1. Re-verify Sandy Springs Plumbing CRM detail/list.
2. If Email 2/3 bounce or bounce-risk evidence is still present, set
   sequencePaused=true.
3. Set sequencePausedReason to:
   "post-vacation hold: prior bounce events; Email 4 requires address/email and reply-monitor review"
4. Write a completion artifact.

Still prohibited:
new email sends, Poplar/SMS sends, prospect/customer contact, unrelated CRM
writes, deploys, Paperclip mutations, git pushes, DNS/domain/hosting/billing
changes, and Stripe actions.
```

Why:

- Sandy has repeated bounce evidence.
- Email 4 is scheduled for `2026-06-07T18:00:03.991+00:00`.
- There is enough time to review before the next send.

## Recommended Batch C - Provider Exception Diagnosis

Recommended approval:

```text
Approved: 24 Hrs Mobile Tire Services exception diagnosis only.

Allowed:
1. Re-fetch Poplar order 8b46f6b0-07a9-4242-851e-7fd3d488ff72 read-only.
2. Inspect public postcard asset URLs and preview URLs read-only.
3. Inspect CRM preview_postcard_payload dry-run/read-only if available.
4. Write an exception diagnosis packet with exact suspected cause and retry
   recommendation.

Still prohibited:
Poplar retry/resubmit, CRM writes, Paperclip mutations, deploys, sends, prospect
contact, git pushes, DNS/domain/hosting/billing changes, and Stripe actions.
```

Why:

- Poplar currently exposes `exception`, cost `$0.00`, and no expected delivery
  date.
- API response does not expose the exact exception reason.
- The address payload looks syntactically reasonable:
  `396 PIEDMONT AVE NE, ATLANTA, GA 30308`.

## Recommended Batch D - Email 5 Governance

Recommended approval:

```text
Approved: prepare, but do not execute, Email 5 governance packet.

Allowed:
1. Reconcile Tech On The Way and Perez Pools CRM events, Resend delivery state,
   reply-monitor evidence, and any bounce/reply state read-only.
2. Prepare a go/hold recommendation for Email 5 scheduled on 2026-06-11.
3. Write exact approval text for either pause or continue.

Still prohibited:
sequence pause/resume, email sends, CRM writes, prospect/customer contact,
deploys, Paperclip mutations, git pushes, DNS/domain/hosting/billing changes,
and Stripe actions.
```

Why:

- Both sent/delivered Email 4 on 2026-05-31.
- Email 5 is not due until 2026-06-11, so this is important but not urgent.

## Current Best Order

1. Approve Batch A if you want the board to reflect real postcard progress.
2. Approve Batch B before June 7 if Sandy should not continue after bounces.
3. Run Batch C to diagnose 24 Hrs without retrying.
4. Use Batch D later this week before June 11.

## Explicit No-Action Statement

This packet did not perform CRM writes, Paperclip mutations, deploys,
Poplar/Resend/SMS sends, prospect/customer contact, git pushes, production site
edits, DNS/domain/hosting/billing changes, Stripe actions, or destructive
cleanup.

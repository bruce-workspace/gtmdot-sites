# Outreach Operations Status

Last updated: 2026-05-16

## Current objective

Audit and stabilize Outreach Operations channel truth after Jesse-approved outreach: postcard submission/status, Resend email delivery/follow-ups, bounce handling, reply monitoring, suppression gaps, stale prospect messages/flags, and analytics needed before scaling outreach.

## Current state

- Outreach channel-state audit completed.
- Stale prospect-message cleanup completed for clearly resolved/superseded items.
- 13 prospects remain in `outreach_sent`.
- 13 postcards show `submitted`.
- 0 postcards show confirmed `in_production`, `mailed`, `delivered`, `returned`, or `suppressed` events.
- 10 email sent events are recorded.
- 9 email delivered events are recorded.
- 1 hard bounce is recorded.
- 0 replies are confirmed tracked in CRM/outreach events.
- Resend sent/delivered/bounced tracking appears partially functional.
- Poplar post-submission status progression is not proven.
- Gmail/OpenClaw reply watcher remains unconfirmed.
- 69 stale/resolved CRM notes were closed across 10 outreach prospects.
- Morales Landscape & Construction is paused because of a hard bounce.
- Due Email 2 prospects are paused pending Jesse approval before resuming follow-up.

## Active prospects/items

- Morales Landscape & Construction: hard bounce recorded; sequence paused with hard-bounce reason; no further email should send until Jesse reviews.
- Atlanta Pro Repairs: stale notes cleaned; sequence remains paused pending Jesse approval before follow-up resumes.
- Locksmith Atlanta Pro: stale notes cleaned; sequence remains paused pending Jesse approval before follow-up resumes.
- Membreno's Pro Home Repair: stale notes cleaned; sequence remains paused pending Jesse approval before follow-up resumes.
- Moonstone Pressure Washing: stale notes cleaned; sequence remains paused pending Jesse approval before follow-up resumes.
- Golden Choice ProWash: stale notes cleaned; sequence remains paused pending Jesse approval before follow-up resumes.
- Tech On The Way: Email 2 sent and delivered automatically on 2026-05-16 around 02:00 UTC; next email scheduled.
- Perez Pools LLC: Email 2 sent and delivered automatically on 2026-05-16 around 02:00 UTC; next email scheduled.
- Affordable Concrete Repair: email exists and is approved, but no email send/schedule is recorded; remaining open item is Jesse's photo request.
- ATL Mobile Mechanics: remaining open items are duplicate/business-quality/deploy-gate questions; not treated as stale.
- Atlanta Drywall, Done Right Drywall, Roberts Mobile Services: postcard-only due to missing email; stale old QA notes cleaned where clearly superseded.

## Latest artifacts

- Outreach channel-state audit summary produced in the current Codex thread.
- Supabase note cleanup verification: 69 notes resolved after 2026-05-16T12:14:00Z.
- Remaining open CRM notes are limited to Affordable Concrete and ATL Mobile Mechanics.
- Status file updated: `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/status/outreach-operations.md`.
- Code/data references reviewed:
  - `/Users/bruce/.openclaw/workspace/brucecom-v3/src/lib/poplar.ts`
  - `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/api/webhooks/poplar/route.ts`
  - `/Users/bruce/.openclaw/workspace/brucecom-v3/src/lib/resend.ts`
  - `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/api/webhooks/resend/route.ts`
  - `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/api/cron/send-next-email/route.ts`
  - `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/api/email-intake/route.ts`
  - `/Users/bruce/.openclaw/workspace/brucecom-v3/src/app/api/notes/route.ts`
  - `/Users/bruce/.openclaw/workspace/brucecom-v3/src/lib/flag-resume.ts`

## Paperclip issues

- Morales hard-bounce suppression/pause: action taken in CRM; Paperclip should track as hard blocker until reviewed.
- Poplar status verification after submission: still open.
- Resend bounce auto-pause behavior: still open; manual pause was needed for Morales.
- Gmail/OpenClaw watcher confirmation: still open.
- Email intake schema mismatch verification: still open.
- Affordable Concrete Repair email channel mismatch: still open.
- Dashboard/stat label correction for postcards submitted vs mailed: still open.
- Next-email due-date source-of-truth correction: still open.
- Stale/resolved CRM prospect messages cleanup: first pass completed; remaining open items appear intentional.
- Resume follow-up approval gate: needed before unpausing due sequences.

## Blockers

- No proof that Poplar statuses are being reconciled after submission.
- No proof that Gmail/OpenClaw watcher is ingesting replies.
- `email_log` live schema appears mismatched with checked-in intake expectations.
- Replies to `hello@gtmdot.com` may not be linked to prospects by current intake logic.
- Hard bounce did not automatically pause/suppress Morales; manual pause was required.
- CRM `outreach_sent` remains too coarse for operations or reporting.
- Due follow-ups are intentionally paused until Jesse decides whether to resume.

## Jesse decisions needed

- Decide whether to permanently suppress Morales's bounced email address and whether to seek an alternate contact.
- Decide whether to resume Email 2 for Atlanta Pro Repairs, Locksmith Atlanta Pro, Membreno's Pro Home Repair, Moonstone Pressure Washing, and Golden Choice ProWash.
- Decide whether Affordable Concrete should get Email 1 or remain held until photos are collected.
- Decide whether ATL Mobile Mechanics should remain in outreach_sent, be disqualified/merged, or receive further cleanup because of duplicate and quality concerns.
- Decide whether Poplar status should be reconciled by webhook only, scheduled polling, or both.
- Approve any live Poplar/Resend/Gmail smoke tests that could touch external systems.
- Decide whether dashboard work should live in CRM, Paperclip, or both.

## Actions completed

- Read local outreach-related CRM data read-only.
- Summarized all `outreach_sent` prospects by postcard/email state.
- Identified due/overdue follow-ups.
- Identified hard bounce, paused sequences, missing-email prospects, and postcard-only outreach.
- Reviewed Poplar send/webhook/status ownership.
- Reviewed Resend send/webhook/cron ownership.
- Reviewed reply intake ownership and likely gaps.
- Reviewed notes/flags model and auto-resume behavior.
- Identified stale/open-ish notes from Supabase read-only inventory.
- Resolved 69 stale/superseded CRM notes across outreach prospects.
- Paused Morales because of Resend hard bounce.
- Relabeled due-sequence pauses so they require Jesse approval before resuming.
- Proposed an outreach analytics dashboard and reusable gates/skills.
- Updated Outreach Operations lane status file.

## Actions explicitly not performed

- No live outreach sends.
- No Poplar submissions.
- No Resend/email sends.
- No SMS sends.
- No customer/prospect replies.
- No Poplar status backfill.
- No Paperclip issue writes.
- No production code changes.
- No sequence resumes.

## Next recommended action

Review the paused follow-up list and decide which, if any, should resume. Separately, run a read-only Poplar status reconciliation against the 13 submitted order IDs and verify the Gmail/OpenClaw reply path with a controlled internal alias test before trusting reply or delivery analytics at scale.

## Cross-lane impacts

- CRM lane: still needs channel-level state rather than a single `outreach_sent` truth; stale message cleanup reduced false blockers but did not solve channel truth.
- Paperclip lane: should track send gates, approval artifacts, blockers, channel status, stale-message cleanup, and audit trail.
- Post-Build Operations: stale pre-approval QA flags should not block Outreach Operations after Jesse approval unless reopened after approval.
- Platform/checkout lane: no changes made.
- Slack lane: notification-only; should not be treated as source of truth.

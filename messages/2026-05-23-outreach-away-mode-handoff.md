# Outreach Operations Away-Mode Handoff

Date: 2026-05-23
Lane: Outreach Operations
Audience: Main GTMDot coordinator

## Current lane status
Outreach is stable but should remain gated. The lane can keep clearing read-only/provider truth, send packets, analytics specs, and channel-state discrepancies while Jesse is remote. No live outreach should occur without explicit Jesse approval.

## Active blockers
- No Poplar, Resend, SMS, or prospect/customer contact without explicit Jesse approval.
- Reply monitoring is not proven enough to safely scale automated follow-ups.
- Prospect detail API can expose stale/raw `postcardStatus` even when outreach events show a submitted postcard.
- Paperclip has not yet recorded the resolved Atlanta Expert stage-transition incident or the detail-status mismatch.

## Closest to revenue
1. `harrison-sons-electrical`: postcard-only, Jesse-reviewed, Poplar first-name preview fixed. Needs Jesse-approved retry/send.
2. `atlanta-expert-appliance`: postcard submitted; CRM stage reconciled to `outreach_sent`; no email scheduled.
3. Existing `outreach_sent` cohort: real sends/events exist; best next lift is channel-state dashboard plus reply/bounce monitoring.
4. InTire Mobile Tire Shop: technically ready per Post-Build, but Outreach needs coordinator/Jesse channel decision.

## Safe to advance without Jesse
- Read-only Poplar/Resend/CRM/event audits.
- Draft send packets, exception reports, exact approval language, and dashboard specs.
- Dry-run/static checks and preview payload inspection.
- CRM v2 acceptance criteria for channel state, reply state, suppression, and stale notes.
- Local-only code analysis or patches that do not deploy or mutate production data.

## Requires explicit Jesse approval
- Postcard submit/retry/resubmit.
- Email sends or sequence resumption.
- SMS sends.
- Prospect/customer replies.
- CRM business-state changes beyond a specifically approved one-record reconciliation.
- Production deploys affecting outreach behavior.
- Paperclip mutation by this lane, if desired.

## Files/artifacts changed
- Status: `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/status/outreach-operations-latest.md`
- Handoff: `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/2026-05-23-outreach-away-mode-handoff.md`
- Prior artifact: `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/2026-05-22-harrison-poplar-public-crm-stale-route.md`
- Local uncommitted `brucecom-v3` Outreach changes touch Poplar payload handling, stage transition, email copy/personalization, reply-to guard, and preview/send paths.

## Recommended next 3 actions
1. Ask Jesse for one clean decision: approve or hold Harrison postcard retry now that public payload preview is fixed.
2. Coordinator logs/links two Paperclip items: Atlanta stage-transition incident resolved, and prospect detail `postcardStatus` mismatch still open.
3. Assign Outreach plus Platform/CRM v2 to make channel-state truth explicit before resuming email follow-ups: postcard state, email state, bounce/reply state, suppression, and automatic pause-on-reply.

## Notes for quarterback
- Atlanta Expert Appliance backfill was completed with no Email 1 scheduling.
- Harrison should not be retried by anyone without a fresh Jesse yes.
- Slack/Telegram should only notify; Paperclip/status artifacts remain the control plane.

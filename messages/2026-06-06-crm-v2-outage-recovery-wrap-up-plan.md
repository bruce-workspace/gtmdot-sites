# CRM v2 Outage Recovery And Wrap-Up Plan

Date: 2026-06-06
Owner: Codex / GTMDot quarterback
Mode: V2.1 final lab wrap-up push

## Context

Jesse returned after a multi-day home internet outage. The local CRM v2 lab route was still serving, but the data API had stalled.

The active goal remains:

> Ship CRM v2 V2.1 board-clearing workflow from lab preview toward a usable review system: keep the board scannable, make the prospect drawer command-first, clearly separate current blockers from stale notes, provider truth, enrichment needs, and send readiness, and verify against real GTMDot prospects without production writes/sends/deploys unless separately approved.

## Recovery Performed

- `/lab/crm-v2` returned `200 OK`, but `/api/prospects` timed out.
- Process inspection found a stale Friday-morning `next-server` on port `3001` consuming heavy CPU.
- Terminated only the stale local CRM dev process tree.
- Restarted CRM v2 locally with `npm run dev -- -p 3001`.
- Confirmed the fresh dev server is listening on port `3001`.

## Current Verification

- `http://127.0.0.1:3001/api/prospects` returns current CRM prospect data.
- `http://localhost:3001/lab/crm-v2` returns `200 OK`.
- Current V2.1 acceptance audit against live local CRM data:
  - `67` prospects loaded.
  - Overall: `V2.1 usable in lab; production still locked`.
  - Ready checks: `14`.
  - Attention checks: `0`.
  - Blocked checks: `1`, the intentional production cutover guardrail.
  - Board routes aligned: `send 1/1; retry 3/3; fix 13/13; enrich 25/25`.
  - Review outcomes ready: `67/67`.
  - Drawer decisions deconflicted: `67/67`.
  - Command recommendation aligned: `67/67`.
  - Stale note separation: `67/67; 0 current / 288 stale open`.
  - Provider truth separated: `67/67; 3 retry / 21 verify`.
  - Send readiness gated: `67/67; 1 approval candidates`.
- `npm run build` passed with the known unrelated vault/Turbopack warning:
  - `next.config.ts -> src/lib/vault.ts -> src/app/api/prospects/[id]/vault/route.ts`.

## Reasonable Wrap-Up Target

CRM v2 V2.1 should now be treated as final lab wrap-up, not open-ended redesign.

Target outcome for the next focused work block:

1. Keep the V2.1 audit green against current data.
2. Validate 5-10 real representative prospects through the board and drawer workflow.
3. Produce a cutover-ready review packet that says exactly what is ready, what remains lab-only, and what production approval would require.
4. Keep production cutover, CRM writes, provider sends, Paperclip mutations, deploys, and git pushes locked until separately approved.

## Representative Prospect Fixtures To Validate

- `rooter-pro-plumbing-drain`: approval/send-readiness path.
- `24-hrs-mobile-tire-services`: provider retry/provider truth path.
- `piedmont-tires`: enrichment / postcard payload repair path.
- `tuxedo-mechanical-plumbing`: current fix / review feedback path.
- `raiden-electrical`: live-site health path.
- `cityboys`: hero/postcard/photo review-risk path.
- `harrison-sons-electrical`: monitor sent outreach path.
- `browning-electrical-services`: provider verification/submitted postcard path.

## Representative Fixture Validation

Validated the representative fixture set against current local CRM data after runtime recovery.

- `rooter-pro-plumbing-drain`
  - Stage: `qa_approved`.
  - Route: `approve_channel`.
  - Primary action: review postcard proof and approve postcard-only if good enough.
  - Outcome panel: `Approve / advance packet`, `Needs Fix / feedback packet`, `Email discovery packet`.
- `24-hrs-mobile-tire-services`
  - Stage: `outreach_staged`.
  - Route: `provider_retry`.
  - Primary action: fix provider/payload issue, then retry postcard only with named approval.
  - Provider evidence: CRM postcard event is `suppressed`; Poplar provider truth is `exception (suppressed)` with order `8b46f6b0-07a9-4242-851e-7fd3d488ff72`.
  - Outcome panel: `Provider incident packet`, `Needs Fix / feedback packet`, `Email discovery packet`.
- `piedmont-tires`
  - Stage: `qa_approved`.
  - Route: `run_enrichment`.
  - Primary action: prepare source-backed address/payload repair before postcard approval.
  - Outcome panel: `Enrichment evidence packet`, `Needs Fix / feedback packet`, `Email discovery packet`.
- `tuxedo-mechanical-plumbing`
  - Stage: `needs_approval`.
  - Route: `needs_fix`.
  - Primary action: recheck stale visual/site evidence against the current live site before approval.
  - Outcome panel: `Needs-fix packet`, `Needs Fix / feedback packet`, enrichment closed as `No enrichment job`.
- `raiden-electrical`
  - Stage: `needs_approval`.
  - Route: `site_health`.
  - Primary action: verify the live preview opens and matches the CRM slug before asking Jesse to approve.
  - Outcome panel: `Site health packet`, `Needs Fix / feedback packet`, `Email discovery packet`.
- `cityboys`
  - Stage: `qa_approved`.
  - Route: `needs_fix`.
  - Primary action: recheck stale visual/site evidence against the current live site before approval.
  - Outcome panel: `Needs-fix packet`, `Needs Fix / feedback packet`, `Source evidence discovery packet`.
- `harrison-sons-electrical`
  - Stage: `outreach_sent`.
  - Route: `provider_verify`.
  - Primary action: monitor provider progression, replies, and follow-up safety.
  - Outcome panel: `Monitor / verify packet`, `Needs Fix / feedback packet`, `Email discovery packet`.
- `browning-electrical-services`
  - Stage: `needs_approval`.
  - Route: `provider_verify`.
  - Primary action: verify provider order state and reconcile CRM stage/channel truth before any resend.
  - Outcome panel: `Monitor / verify packet`, `Needs Fix / feedback packet`, `Email discovery packet`.

Fixture conclusion:

- The representative fixtures now cover the main operating paths CRM v2 must make obvious: approve channel, provider retry, payload/enrichment repair, current fix, site health, review-risk fix, sent-outreach monitor, and provider verification.
- The fixture set supports moving to a cutover-readiness packet, not yet production cutover.

## Definition Of "Wrapped Enough For Decision"

- Board is scannable and not stage-only.
- Drawer is command-first and outcome-driven.
- Current blockers are separated from stale/history notes.
- Provider truth is separated from CRM stage/channel state.
- Enrichment needs are evidence packets, not automatic CRM writes.
- Send readiness is gated and explicit.
- Representative fixtures prove the UX answers "what do I do next?".
- Remaining production risks are listed as blockers or cutover prerequisites.

## Still Prohibited Without Separate Approval

- CRM/Supabase writes.
- Stage moves, field backfills, or strategic CRM truth changes.
- Poplar postcard submits/retries.
- Resend/email/SMS sends.
- Prospect/customer contact.
- Paperclip issue/comment/status mutations.
- Deploys or production CRM replacement.
- Git commits/pushes.
- DNS/domain/hosting/billing/Stripe actions.

## No-Action Statement

No CRM/Supabase writes, sends, provider calls, Paperclip mutations, deploys, git pushes, production replacement, prospect/customer contact, DNS/domain/hosting/billing changes, or Stripe actions were performed in this recovery.

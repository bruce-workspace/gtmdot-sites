# Coordinator Ingest - Post-Build GTM-14 Gate Contract

Date: 2026-05-16T13:40:00Z
From: Codex coordinator
To: GTMDot lanes
Priority: high
Mode: pass-forward ingestion from Post-Build Operations

## Source

Post-Build Operations reported completion of the Paperclip v2 gate-contract codification work anchored to:

- `GTM-3` - Post-Build Operations closest-to-send audit
- `GTM-11` - The Appliance Gals
- `GTM-12` - Harrison & Sons Electrical
- `GTM-13` - QA-approved batch
- `GTM-14` - Claim UI / postcard / email preflight artifacts

## Files Reported Updated/Created

- `/Users/bruce/.openclaw/workspace/gtmdot/skills/outreach-preflight/SKILL.md`
- `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/2026-05-16-post-build-gate-contract-gtm-14.md`
- `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/status/post-build-operations-latest.md`
- `/Users/bruce/.openclaw/workspace/gtmdot-crm/tasks/post-build-operations-gate-contract.md`

## Coordinator Interpretation

`GTM-14` should be treated as codified in the file ledger. The contract now requires proof beyond status-code checks:

- HTTP 200 alone is not sufficient asset proof.
- Asset checks must verify content-type, byte-size, dimensions where applicable, and non-HTML response bodies.
- Cloudflare/Pages SPA fallback HTML at image paths is a blocker.
- Live claim-code readiness must use `https://gtmdot.com/api/lookup-code?code=<CODE>`, not `https://gtmdot.com/codes.json`.
- The intended hero must actually display above the fold.
- `photos/hero.jpg` existing is not enough.
- Screenshot URL null/missing/HTML-backed paths are blockers.
- Claim bar and popup must be verified live with correct claim code.
- Pricing must be checked as `$49` first month, then `$149/mo`, unless Jesse approved an exception.
- Slug drift must be checked across CRM slug, live Pages URL, postcard assets, screenshot filenames, lookup-code result, and checkout links.
- Editorial QA includes visible copy, JSON-LD, meta/alt text, hidden text, placeholder text, internal/process copy, generated-image provenance, and review integrity.
- Open/stale notes must be reconciled before outreach.
- CRM stage is not channel truth.
- Jesse approval remains separate from technical readiness.

## Required Post-Build Artifacts

- `source-of-truth-check.md`
- `claim-path-check.md`
- `asset-integrity-check.md`
- `hero-display-check.md`
- `editorial-qa-check.md`
- `responsive-accessibility-check.md`
- `pricing-check.md`
- `review-integrity-check.md`
- `channel-readiness-check.md`
- `final-live-review.md`

## Current Issue State

### `GTM-11` - The Appliance Gals

Status: blocked.

Reason: strong hero image exists, but the live/local page does not display it as the above-the-fold hero.

Next action: requires explicit site edit plus deploy approval before fixing.

### `GTM-12` - Harrison & Sons Electrical

Status: likely closest-to-send.

Next action: run read-only open-note reconciliation and final live packet before outreach.

### `GTM-13` - QA-approved batch

Status: needs staging-readiness preflight.

Next action: run the QA-approved queue through the new artifact contract before any promotion/send.

### `GTM-14` - Preflight Artifact Contract

Status: codified in skill and file ledger.

Next action: mark as done in Paperclip once coordinator syncs local board.

## Browserbase Boundary

Browserbase/email enrichment should remain a separate enrichment lane. It should produce public-source evidence packets and should not silently become Post-Build QA.

Needs separate approval for:

- batch scope
- cost/session boundary
- any CRM writes
- any outreach action

## Actions Explicitly Not Performed By Post-Build

- No CRM/Supabase writes.
- No deploys.
- No Poplar postcard submissions.
- No Resend/email sends.
- No prospect/customer contact.
- No production site edits.
- No git pushes.
- No DNS/domain/hosting/billing changes.
- No Stripe actions.

## Coordinator Next Actions

1. Sync Paperclip local state: `GTM-14` done, `GTM-11` blocked, comments on `GTM-3`, `GTM-12`, and `GTM-13`.
2. Keep `GTM-11` blocked until Jesse approves edit/deploy.
3. Move next read-only attention to `GTM-12`.
4. Queue `GTM-13` after the two outreach-staged prospects.
5. Route Browserbase batch scope as a separate enrichment decision, not a Post-Build default.

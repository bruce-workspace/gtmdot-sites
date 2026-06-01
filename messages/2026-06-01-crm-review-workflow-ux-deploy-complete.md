# CRM Review Workflow UX Deploy Complete

Date: 2026-06-01
Owner: Codex
Mode: approved public CRM UX deploy

## Completed

Deployed the CRM review workflow bridge patch to public CRM.

Worker:

- `gtmdot-crm-v3`
- Version ID: `d93d6a5e-2d2d-4ed1-82af-920fe9cd4052`
- Public Worker URL: `https://gtmdot-crm-v3.jesse-ef7.workers.dev`
- Public CRM domain: `https://crm.cloakanddagger.co`

## UX Added

### Approve for Outreach

Visible on review-stage prospects:

- `needs_approval`
- `needs_decision`
- `ready_for_review`
- `qa_approved`

Action:

- Moves prospect to `outreach_staged`.
- Sets `approvedAt`.
- Writes `site_approved` activity.

### Needs Fix

Visible on active prospects.

Action:

- Opens a repair-note modal.
- Creates a high-priority task assigned to Bruce.
- Moves eligible prospects back to `needs_enrichment` / repair.

### Run Enrichment

Visible on `needs_enrichment` prospects.

Action:

- Calls the existing enrichment endpoint from the prospect action bar.

## Verification

Build/deploy:

- `npm run build` passed.
- `opennextjs-cloudflare build` passed.
- `wrangler deploy` succeeded.

Public route checks:

- `/` redirects to `/pipeline`.
- `/pipeline` returns `200`.
- `/lab/crm-v2` returns `200`.
- Representative prospect detail route returns `200`.
- Public `/api/prospects` returns `67` prospects.

Rendered UI checks with Playwright:

- `tuxedo-mechanical-plumbing` (`needs_approval`) shows:
  - `Approve for Outreach`: present
  - `Needs Fix`: present
  - `View Postcard`: present
  - `Run Enrichment`: not shown, as expected for non-`needs_enrichment`
- `premier-tv-mounting-atl` (`needs_enrichment`) shows:
  - `Run Enrichment`: present
  - `Needs Fix`: present
  - `View Postcard`: present
  - `Approve for Outreach`: not shown, as expected for `needs_enrichment`

Known note:

- `/GTM/dashboard` is not a deployed public route and returns `404`; public CRM root is `/pipeline`.

## Explicit No-Action Statement

No postcard submit/retry, email/SMS send, prospect/customer contact, Paperclip mutation, git push, DNS/domain/hosting/billing change, or Stripe action was performed.

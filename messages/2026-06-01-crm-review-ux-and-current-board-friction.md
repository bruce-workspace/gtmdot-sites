# CRM Review UX And Current Board Friction

Date: 2026-06-01
Owner: Codex
Mode: local CRM UX patch prepared, not deployed

## Jesse Feedback Captured

Jesse hit the exact workflow problem the current CRM creates:

- If a site has an obvious review issue, there is no obvious place to put a comment that becomes actionable.
- If a site is in `needs_approval`, approval requires clunky stage movement instead of a clear approval button.
- If a prospect is in `needs_enrichment`, Jesse has no obvious useful action, even though enrichment should not require his oversight.
- The board still contains obvious QA misses: missing nav, bad/wrong hero images, dead preview URLs, and stale blocker logic.

## Specific Current Examples

### `tuxedo-mechanical-plumbing`

- CRM stage: `needs_approval`
- Preview URL: `https://tuxedo-mechanical-plumbing.pages.dev`
- Jesse-observed issues:
  - No nav bar.
  - Hero image appears to show welding rather than mechanical/plumbing work.
  - Site is otherwise probably usable, but not clean approval-ready.

### `raiden-electrical`

- CRM stage: `needs_approval`
- Preview URL: `https://preview.gtmdot.com/raiden-electrical/`
- Jesse-observed issue:
  - Site does not open.
- This was already known in earlier Post-Build status as a preview DNS/source failure.

### `browning-electrical-services`

- CRM stage: `needs_approval`
- Postcard status: `submitted`
- Provider state was previously verified as Poplar active/in transit.
- This is a state mismatch: it should not still feel like a normal approval candidate if postcard outreach already happened.

### `rooter-pro-plumbing-drain`

- CRM stage: `qa_approved`
- Postcard status: `not_submitted`
- Jesse says the hero is good enough and the site looks good.
- Earlier blocker was strict print hero dimensions, but Jesse is willing to override visual perfection here.

## Local CRM UX Patch Prepared

Updated local `brucecom-v3`:

- Adds `Approve for Outreach` button for review stages:
  - `needs_approval`
  - `needs_decision`
  - `ready_for_review`
  - `qa_approved`
- Adds `Needs Fix` button:
  - Opens a repair-note modal.
  - Saves a high-priority task assigned to Bruce.
  - Moves the prospect back to `needs_enrichment` / repair when appropriate.
- Adds `Run Enrichment` button for `needs_enrichment` prospects:
  - Calls the existing enrichment endpoint directly from the prospect action bar.

Server action added:

- `approve_for_outreach`
  - Requires preview site.
  - Moves prospect to `outreach_staged`.
  - Sets `approvedAt`.
  - Writes a `site_approved` activity event.

## Verification

- `npm run build` passed.
- Existing non-blocking warning remains:
  - Next/Turbopack traces broad filesystem use from `src/lib/vault.ts` through the vault route.

## Deploy Approval Needed

This is a production CRM UX change, so it should be deployed only with explicit approval.

Suggested approval:

```text
Approved: deploy CRM review workflow UX patch.

Allowed:
1. Deploy the local CRM changes that add Approve for Outreach, Needs Fix, and Run Enrichment actions.
2. Verify public CRM loads and the action buttons are visible for the expected stages.
3. Do not submit postcards, send emails/SMS, contact prospects, mutate Paperclip, push git, or change DNS/domain/hosting/billing/Stripe.
```

## Explicit No-Action Statement

No deploy, CRM data write, Paperclip mutation, Poplar/Resend/SMS send, prospect contact, git push, DNS/domain/hosting/billing change, or Stripe action was performed for this UX patch.

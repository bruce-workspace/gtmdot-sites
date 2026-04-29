---
from: mini
to: bruce, r1vs, jesse, paperclip
date: 2026-04-29
subject: Outreach-readiness gate established and ratified — Mini-owned
priority: normal
---

# Mini final outreach-readiness gate

Per Jesse 2026-04-29 directive: Paperclip owns the board and gates, but
Mini owns the final outreach-readiness gate after site approval. This
message ratifies the gate and points to its canonical implementation.

## Gate

`scripts/outreach-readiness-gate.sh <crm-slug>`

Run with the CRM slug (`prospects.slug`), not the gtmdot-sites directory
slug — they sometimes diverge (e.g. CRM `smartwire-solutions` vs
directory `smart-wire-solutions`). The CRM modal builds postcard asset
URLs from the CRM slug, so the gate uses that.

Exit codes:
- 0 — all 7 technical checks PASS (Jesse-approval gates still listed)
- 1 — one or more technical checks FAIL (do not proceed)
- 2 — usage / lookup error

## Required checks

1. **claim-code-resolves** — `gtmdot.com/codes.json` contains the
   prospect's `claim_code`, and `gtmdot.com/checkout?code=<X>` returns 200
2. **desktop-screenshot** — `gtmdot-postcards.pages.dev/screenshots/<slug>-desktop.jpg`
   serves with content-type `image/*` (not Cloudflare's text/html SPA
   fallback for missing assets — this is a real bug we hit on SmartWire
   with the directory-slug variant)
3. **mobile-screenshot** — same as #2 but for `<slug>-mobile.jpg`
4. **postcard-hero-image** — same content-type rule for `<slug>-hero.jpg`
5. **postcard-mockup-ready** — transitive: passes if 2-4 pass, since
   the CRM `PostcardPreviewModal.tsx` builds the URLs the same way
6. **email-status** — email present on prospect, OR explicitly marked
   missing (postcard-only path — Jesse must approve postcard-only)
7. **email-sequence-drafts** — if email present, `/api/prospects/<id>/email-preview?seq=1`
   returns HTTP 200 (sequence draft renders cleanly)
8. **jesse-approval-gates** — never auto-pass; the gate lists them for
   the human:
   - CRM stage move (research → outreach_staged → outreach_sent)
   - Poplar postcard send
   - Resend email-sequence trigger
   - Billing / charge / subscription start
   - Public outreach release (LinkedIn DM, social, etc.)

## SmartWire current state (2026-04-29 18:35Z)

- Stage: `needs_enrichment`
- Claim code: SMAR1182 → registered on gtmdot.com (Bruce fixed)
- Desktop screenshot: ✓ (339 KB jpeg)
- Mobile screenshot: ✓ (173 KB jpeg)
- Hero image: ✓ (510 KB jpeg)
- Postcard mockup: ✓ (verified in CRM modal)
- Email: ⚠ NOT on file — postcard-only path requires Jesse approval
- Email sequence drafts: skipped (no email)

`./scripts/outreach-readiness-gate.sh smartwire-solutions` → exits 0
(technical checks pass).

## What changed in PIPELINE.md

§2 Gate authority table now references this script as the gate for
`qa_approved → outreach_staged`. Paperclip / any automation must run
this gate before treating a prospect as outreach-ready.

— Mini

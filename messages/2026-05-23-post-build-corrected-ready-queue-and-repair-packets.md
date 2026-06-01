# Post-Build Corrected Ready Queue + Repair Packets - 2026-05-23

Owner: Codex / Post-Build Operations  
Mode: remote-week board clearing  
Status: corrected packet only, no sends or production changes  
Supersedes: `2026-05-23-next-needs-approval-review-and-batch-proposal.md` for send-batch purposes

## Scope

Outreach corrected the prior seven-prospect send candidate set. This packet treats that correction as the current operating source of truth and reconciles it against fresh Post-Build live gates.

No postcard sends, Resend/email sends, SMS, CRM/Supabase writes, Paperclip mutations, deploys, postcard CDN repairs, prospect/customer contact, DNS/domain/hosting/billing changes, Stripe actions, or git pushes were performed.

## Fresh Gate Run

Read-only live gate data was written to:

- `/private/tmp/gtmdot-corrected-queue-reconcile.json`

Gate checks included:

- Preview URL live HTML
- Claim lookup resolves to the expected slug
- Checkout URL loads
- `preview_postcard_payload` returns 200
- Poplar recipient fields present and length-safe
- Desktop screenshot returns real image bytes
- Mobile screenshot returns real image bytes
- Hero asset returns image bytes and is dimension-checked for postcard print suitability

## Current Corrected Ready Queue

These are the only clean Jesse postcard-only approval candidates from this corrected pass:

1. `24-hrs-mobile-tire-services`
2. `bravo-plumbing-solutions`
3. `browning-electrical-services`

Fresh gate status:

| Slug | Stage | Payload | Hero | Verdict |
|---|---:|---:|---|---|
| `24-hrs-mobile-tire-services` | `needs_approval` | 200 | JPEG, 3840x2160, 667699 bytes | Clean candidate |
| `bravo-plumbing-solutions` | `needs_approval` | 200 | JPEG, 3840x2160, 474333 bytes | Clean candidate |
| `browning-electrical-services` | `needs_approval` | 200 | JPEG, 3840x2160, 599406 bytes | Clean candidate, with prior business-confidence caveat still worth Jesse awareness |

## Current Repair Queue

### `cityboys` - visual QA / image mismatch

Mechanical gates pass, but the current postcard hero is a classic black car while the live site and screenshots are appliance-repair oriented. This remains blocked for visual trust even though payload/assets load.

Evidence artifact:

- `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/2026-05-23-cityboys-visual-qa-finding.md`

Narrow repair path:

1. Select or generate an appliance-repair-aligned postcard hero.
2. Replace only the postcard hero asset after approval.
3. Regenerate or verify postcard preview assets.
4. Rerun final live gates and visual QA before any send approval request.

Approval needed:

- Postcard asset repair/deploy approval if we replace the public `cityboys-hero.jpg`.
- Separate named send approval after visual QA passes.

### `piedmont-tires` - source-backed CRM mailing repair

Fresh gate still fails because `preview_postcard_payload` returns 400 for missing mailing fields. Because payload generation fails, Poplar image merge tags are absent in the CRM preview response even though prior asset work exists.

Evidence artifact:

- `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/2026-05-23-piedmont-tires-mailing-field-evidence-packet.md`

Recommended source-backed CRM repair:

- `address = "3483 Clairmont Rd NE"`
- `city = "Atlanta"`
- `state = "GA"`
- `zip = "30319"`

Narrow repair path:

1. Get explicit CRM write approval for the four mailing fields only.
2. Rerun `preview_postcard_payload`.
3. Rerun postcard asset/claim/checkout gates.
4. Do not send until a later named postcard approval.

### `rooter-pro-plumbing-drain` - hero file/spec failure

Payload and visible site gates load, but the postcard hero is not print-safe.

Evidence:

- Public URL: `https://gtmdot-postcards.pages.dev/rooter-pro-plumbing-drain-hero.jpg`
- Local path: `/Users/bruce/.openclaw/workspace/gtmdot/postcards/rooter-pro-plumbing-drain-hero.jpg`
- Local source path: `/Users/bruce/.openclaw/workspace/gtmdot-sites/sites/rooter-pro-plumbing-drain/photos-generated/hero-postcard.jpg`
- `file` reports PNG data even though the public URL is named `.jpg` and served as `image/jpeg`.
- `sips` reports `2048x1152`, below the 3000x1700 postcard hero gate.

Narrow repair path:

1. Request Bruce image-generation repair for a true gpt-image-2 postcard hero meeting at least 3000x1700 if possible, or produce an explicitly approved print-safe fallback.
2. Ensure the output is a real JPEG, not PNG bytes under a `.jpg` name.
3. Deploy postcard CDN repair only after approval.
4. Rerun payload, asset, dimensions, and visual gates.

Approval needed:

- Bruce collect/request approval if routing through Bruce.
- Postcard CDN repair/deploy approval before publishing the replacement.

### `thermys-mobile-tire-and-brakes` - current photo/content gap

Mechanical postcard gates pass. The hold is editorial/visual, not asset availability. Local research began as an empty-shell pass with no reviews captured, and a later `needs-repolish.md` says Bruce enrichment landed with `0` new reviews and `6` photos in `photos/inbox/`. Current live/local source uses generated/public content and does not clearly resolve the “real photo/content” gap for Jesse review.

Evidence:

- `/Users/bruce/.openclaw/workspace/gtmdot-sites/sites/thermys-mobile-tire-and-brakes/RESEARCH.md`
- `/Users/bruce/.openclaw/workspace/gtmdot-sites/sites/thermys-mobile-tire-and-brakes/needs-repolish.md`
- Fresh payload/asset gates pass with hero `3840x2160`.

Narrow repair path:

1. Review the six captured `photos/inbox/` assets and decide whether any should replace or support current site visuals.
2. Confirm current review count/source truth before preserving the live review copy.
3. If site edits are needed, prepare a scoped Post-Build repair approval; otherwise create a Jesse visual-override packet.

Approval needed:

- Site edit/deploy approval if integrating real photos or changing copy.
- Separate postcard send approval if Jesse accepts the current visual/content state without repair.

### `tuxedo-mechanical-plumbing` - current photo/source gap

Mechanical postcard gates pass. The current live site still uses an Unsplash-style remote hero reference in metadata/hero CSS, while Bruce produced a gpt-image-2 postcard hero for the postcard asset. That mismatch keeps the photo/source concern current.

Evidence:

- `/Users/bruce/.openclaw/workspace/gtmdot/sites/tuxedo-mechanical-plumbing/index.html` references `images.unsplash.com/photo-1504328345606...`
- `/Users/bruce/.openclaw/workspace/gtmdot-sites/sites/tuxedo-mechanical-plumbing/bruce-collected.md` says a gpt-image-2 postcard hero exists at 3840x2160.
- Fresh payload/asset gates pass with postcard hero `3840x2160`.

Narrow repair path:

1. Decide whether the live site hero should be replaced with the approved/generated postcard hero or another source-backed asset.
2. Remove or replace Unsplash metadata/hero references if the concern is blocking.
3. Deploy only after explicit approval.
4. Rerun live site visual QA and postcard gates.

Approval needed:

- Site edit/deploy approval if replacing live hero/metadata.
- Separate postcard send approval if Jesse accepts current live-site vs postcard-hero mismatch.

### `chrissy-s-mobile-detailing` - review-count inconsistency

Mechanical postcard gates pass. The current live/local copy still contains conflicting review-count claims: `133 Google reviews` in metadata/hero/footer/JSON-LD and `117 Google Reviews` in stat/review sections.

Evidence:

- `/Users/bruce/.openclaw/workspace/gtmdot/sites/chrissy-s-mobile-detailing/index.html`
- Fresh payload/asset gates pass with postcard hero `3840x2160`.

Narrow repair path:

1. Verify current source-backed review count.
2. Pick one supported number and update visible copy, metadata, and JSON-LD consistently.
3. If no current source check is available during remote week, hold for Jesse override or Bruce verification.

Approval needed:

- Site edit/deploy approval if correcting copy.
- Bruce/current-source verification request if the number needs fresh evidence.
- Separate postcard send approval after consistency is resolved or explicitly overridden.

## Exact Approval Text - Clean Queue Send

```text
Approved: remote-week clean postcard-only batch.

Allowed:
1. Submit Poplar postcard-only outreach for:
   - 24-hrs-mobile-tire-services
   - bravo-plumbing-solutions
   - browning-electrical-services
2. Rerun final live gates immediately before each send:
   - preview URL live
   - claim lookup resolves
   - checkout URL loads
   - desktop screenshot is real image with meaningful byte size, not HTML fallback
   - mobile screenshot is real image with meaningful byte size, not HTML fallback
   - hero image is real image with meaningful byte size and print-safe dimensions
   - preview_postcard_payload returns 200
   - recipient fields satisfy Poplar constraints
   - no current blocker is unresolved
3. Stop on any failed gate or Poplar error with no retry.
4. Verify CRM/provider state after each approved submit.
5. Write completion/blocker artifacts and update lane status.

Still prohibited:
Resend/email sends, SMS, prospect/customer contact outside approved Poplar postcards, manual CRM/Supabase truth edits, Paperclip mutations, deploys/postcard CDN repairs, DNS/domain/hosting/billing changes, Stripe actions, git pushes, and any Cityboys send.
```

## Explicit No-Action Statement

No postcard sends, Resend/email sends, SMS, prospect/customer contact, CRM/Supabase writes, Paperclip mutations, deploys/postcard CDN repairs, DNS/domain/hosting/billing changes, Stripe actions, git pushes, or production-impacting edits were performed.

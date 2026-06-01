# Held Outreach Repair Packets

Date: 2026-05-23
Lane: Outreach Operations
Mode: repair packets only, no sends

## Purpose

Keep non-approved or failed-gate prospects in explicit repair/hold lanes so they
do not drift back into the send queue.

No sends, CRM writes, Paperclip mutations, deploys, CDN repairs, prospect
contact, or git pushes were performed.

## Held Items

### `cityboys`

- Current lane: visual QA hold
- Blocker: confusing/wrong postcard imagery concern
- Evidence: Jesse explicitly prohibited Cityboys send until visual QA is
  cleared and separately approved.
- Safe next action: Post-Build visual QA packet comparing live site, postcard
  hero, desktop screenshot, mobile screenshot, trade/category, and business
  identity.
- Still prohibited: postcard send, email send, CRM write, deploy/CDN repair
  without separate approval.

### `piedmont-tires`

- Current lane: mailing-field repair
- Blocker: missing ZIP in CRM; `preview_postcard_payload` cannot satisfy Poplar
  mailing constraints.
- Known CRM fields: address `3483 Clairmont Rd`, city `Chamblee`, state `GA`,
  ZIP missing.
- Safe next action: source-backed ZIP repair packet from authoritative public
  evidence; route for Jesse approval before any CRM write.
- Still prohibited: CRM ZIP write, postcard send, retry, or inferred ZIP without
  approval.

### `rooter-pro-plumbing-drain`

- Current lane: postcard asset repair
- Blocker: postcard hero dimensions fail print-spec.
- Evidence: canonical readiness gate measured hero at `2048x1152`, below
  3000x1700 minimum.
- Safe next action: Post-Build hero repair packet/regeneration request; rerun
  screenshot/hero gates after repair.
- Still prohibited: deploy/CDN repair or postcard send without separate
  approval.

### `thermys-mobile-tire-and-brakes`

- Current lane: visual/content repair or Jesse override
- Blocker: current live HTML still has zero `<img>` tags; old high-priority
  photo/content note revalidates as current.
- Non-blocking improvements already resolved: old copy-spacing strings were not
  visible on current live HTML.
- Safe next action: Post-Build visual/content decision packet: either repair
  inline service/photo proof, or ask Jesse to explicitly override for
  postcard-only outreach.
- Still prohibited: postcard send without named override approval.

### `tuxedo-mechanical-plumbing`

- Current lane: visual/content repair or Jesse override
- Blocker: current live HTML still has zero `<img>` tags and references older
  Unsplash-style hero asset ID `photo-1504328345606`.
- Non-blocking improvements already resolved: copyright is now `2026`; claim
  code is present.
- Safe next action: Post-Build photo/source packet: replace or justify the hero,
  add/source proof imagery if available, or ask Jesse to explicitly override for
  postcard-only outreach.
- Still prohibited: postcard send or email send without named override
  approval.

### `chrissy-s-mobile-detailing`

- Current lane: copy/data consistency repair or Jesse override
- Blocker: current live HTML still contains both `117 Google Reviews` and `133`,
  so the stale review-count inconsistency may remain current.
- Non-blocking improvements already resolved: old H1 spacing issue is no longer
  visible; current live HTML has 6 `<img>` tags and valid postcard assets.
- Safe next action: Post-Build copy/data consistency packet: choose the current
  review count and update/verify the live site before outreach, or ask Jesse to
  explicitly override as non-blocking.
- Still prohibited: postcard send or email send without named override
  approval.

## Cross-Lane Notes

- Post-Build owns visual/content and postcard asset repair.
- Outreach owns final gates, Poplar submission, and provider state after
  approval.
- CRM/Platform owns the stage/channel truth mismatch where provider-backed
  postcard events can exist while stage remains pre-outreach.
- Paperclip should track these as blockers if the coordinator wants board-level
  visibility; Outreach did not mutate Paperclip.

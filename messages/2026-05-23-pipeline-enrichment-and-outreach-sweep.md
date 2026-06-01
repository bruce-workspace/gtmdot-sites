# Pipeline Enrichment + Outreach Sweep - 2026-05-23

Owner: Codex / GTMDot quarterback  
Mode: high-autonomy remote-week coordination  
Source: live public CRM read-only snapshot from `https://crm.cloakanddagger.co/api/prospects`  
Snapshot file: `/private/tmp/gtmdot-prospects-live-2026-05-23.json`  

## Goal

Move every active GTMDot prospect as far toward clean outreach as possible:

- Enrich anything that can be enriched.
- Repair missing source-backed mailing/contact fields where evidence supports it.
- Validate screenshots, hero images, claim lookup, checkout, payloads, and email sequence state.
- Prepare named postcard batches for mobile approval.
- Keep email follow-ups safe until reply monitoring and bounce handling are trustworthy.
- Move the rest of the pipeline toward outreach only when the gates and approvals are clean.

No CRM writes, Paperclip mutations, deploys, sends, prospect contact, DNS/domain/hosting/billing changes, Stripe actions, git pushes, or production edits were performed while preparing this sweep.

## Live Pipeline Shape

Active, non-dead prospects: 47

Current active stages:

- `outreach_sent`: 22
- `needs_approval`: 10
- `needs_enrichment`: 9
- `qa_approved`: 2
- `needs_decision`: 2
- `research`: 2

The recently approved postcard batch moved `smartwire-solutions`, `dream-steam`, and `handy-dandy-atlanta` into `outreach_sent`.

## Closest Board-Clearing Moves

### Proposed Next Postcard-Only Batch

The following `needs_approval` prospects have a current Post-Build packet showing live gates pass and no current non-stale blockers:

1. `thermys-mobile-tire-and-brakes`
2. `24-hrs-mobile-tire-services`
3. `bravo-plumbing-solutions`
4. `chrissy-s-mobile-detailing`
5. `rooter-pro-plumbing-drain`
6. `tuxedo-mechanical-plumbing`
7. `browning-electrical-services`

These are not approved to send yet because `needs_approval` requires Jesse visual/business approval first. If approved, they can be handled as postcard-only. `chrissy-s-mobile-detailing` and `tuxedo-mechanical-plumbing` have emails on file, but email should remain separately prohibited unless Jesse approves email.

Exact approval available in:

- `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/2026-05-23-next-needs-approval-review-and-batch-proposal.md`

### Cityboys Hold

`cityboys` is mechanically ready but held because Jesse saw confusing/wrong postcard imagery. Do not send until a fresh visual QA artifact is reviewed and approved.

Current state:

- Stage: `qa_approved`
- Email: `info@cityboysrus.com`
- Postcard: `not_submitted`
- Mechanical gates: pass
- Blocker: visual/truth QA

Artifact:

- `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/2026-05-23-cityboys-send-readiness-hold-packet.md`

### Piedmont Tires Field Repair

`piedmont-tires` is `qa_approved`, but cannot be sent because CRM mailing ZIP is missing.

Current state:

- Address: `3483 Clairmont Rd`
- City: `Chamblee`
- State: `GA`
- ZIP: missing
- Email: none
- Postcard: `not_submitted`
- `nextEmailAt`: stale/past due despite no email

Safe next action:

- Gather source-backed ZIP evidence for the exact address.
- Prepare CRM ZIP write approval.
- Do not send until payload passes after the approved CRM repair.

## Enrichment / Field Repair Queue

### Missing Address / Mailing Field Repair

These require public-source evidence and then explicit CRM write approval before any CRM truth changes:

- `sandy-springs-plumbing`: stage `outreach_sent`; address/city/state/ZIP blank; email bounced; channel/data reconciliation needed before any further outreach.
- `piedmont-tires`: stage `qa_approved`; ZIP missing.
- `forest-park-collision`: stage `needs_approval`; address/state/ZIP missing.
- `jack-glass-electric`: stage `needs_enrichment`; address/ZIP missing, phone missing.
- `pine-peach-painting`: stage `needs_approval`; address/ZIP missing; `postcardStatus` says `submitted` while payload fields are incomplete, so reconcile before retry/send.
- `total-repair-service`: stage `needs_decision`; address/state/ZIP missing plus separate site-quality/recovery blocker.
- `landscape-addict`: stage `research`; address/state/ZIP missing.
- `mbanugo-tires`: stage `research`; address/state/ZIP missing plus known identity/source-truth issues.

Recommended order:

1. `piedmont-tires`, because it is closest to postcard-ready after one ZIP repair.
2. `sandy-springs-plumbing`, because it has active outreach plus a bounce and blank mailing fields.
3. `forest-park-collision`, `jack-glass-electric`, `pine-peach-painting`, because they are active blockers.
4. `total-repair-service`, because site-quality/recovery status also blocks it.
5. `landscape-addict` and `mbanugo-tires`, because research/pre-build remains subordinate to board clearing.

### Missing Email Enrichment

Active prospects missing email: 26.

Missing email does not automatically block postcard-only outreach, but it blocks email path validation. For prospects already in or near outreach, create evidence packets rather than guessing or writing CRM truth.

Highest priority missing-email enrichment:

- Near-send postcard candidates with no email: `thermys-mobile-tire-and-brakes`, `24-hrs-mobile-tire-services`, `bravo-plumbing-solutions`, `rooter-pro-plumbing-drain`, `browning-electrical-services`.
- Active blockers with no email: `piedmont-tires`, `forest-park-collision`, `jack-glass-electric`, `pine-peach-painting`.
- Outreach-sent postcard-only prospects with no email: `smartwire-solutions`, `dream-steam`, `handy-dandy-atlanta`, `harrison-sons-electrical`, `done-right-drywall`, `roberts-mobile-services`, `atlanta-drywall-1`, `atl-mobile-mechanics`.
- Research/pre-build: `landscape-addict`, `mbanugo-tires`.

Safe next action:

- Use Browserbase public-source enrichment where available, Scrapfly fallback only when Browserbase fails, and write candidate evidence packets.
- Do not write emails to CRM without explicit source-backed approval.

## Email Sequence / Reply-Monitoring Risk

This is the most time-sensitive risk area.

Active scheduled email follow-ups:

| Prospect | Stage | Email | Next Email | Sequence | Notes |
| --- | --- | --- | --- | --- | --- |
| `intire-mobile-tire-shop` | `outreach_sent` | `intiremobile@gmail.com` | `2026-05-25T17:00:03.814+00:00` | 3 | Reply monitoring not proven; decision packet exists |
| `sandy-springs-plumbing` | `outreach_sent` | `Jack@ontimefix.com` | `2026-05-26T02:39:23.049+00:00` | 2 | Email 1 bounced; should not continue without approval |
| `tuckers-home-services` | `outreach_sent` | `tuckerhomeservices@yahoo.com` | `2026-05-26T02:52:55.128+00:00` | 2 | Email 1 delivered; reply monitoring still unproven |
| `tech-on-the-way` | `outreach_sent` | `techonthewaymobile@gmail.com` | `2026-05-27T02:30:03.131+00:00` | 4 | Emails 1-3 delivered; reply monitoring still unproven |
| `perez-pools-llc` | `outreach_sent` | `chris@perezpools.com` | `2026-05-27T02:30:03.795+00:00` | 4 | Emails 1-3 delivered; reply monitoring still unproven |
| `piedmont-tires` | `qa_approved` | none | `2026-04-11T23:10:09.904+00:00` | 1 | Stale schedule field despite no email |
| `premier-tv-mounting-atl` | `needs_enrichment` | none | `2026-04-15T13:42:17.532+00:00` | 1 | Stale schedule field despite no email |

Bounce evidence:

- `sandy-springs-plumbing`: Email 1 bounced at `2026-05-23T16:39:27.289105+00:00`.
- `morales-landscape-construction`: historical active bounce at `2026-05-13T02:06:04.495717+00:00`.

Recommended decision:

- Pause `intire-mobile-tire-shop` before Email 3 unless Jesse accepts manual reply-monitoring risk.
- Pause `sandy-springs-plumbing` before Email 2 because Email 1 bounced.
- Treat `piedmont-tires` and `premier-tv-mounting-atl` stale `nextEmailAt` fields as cleanup candidates, not active sends.
- For `tuckers-home-services`, `tech-on-the-way`, and `perez-pools-llc`, either explicitly accept manual reply-monitoring risk or pause until reply monitoring is proven.

## Approval Packets Needed

### Urgent Email Safety Approval

```text
Approved: pause risky scheduled outreach follow-ups during remote week.

Allowed:
1. Pause InTire Mobile Tire Shop Email 3 before 2026-05-25T17:00:03.814+00:00 because reply monitoring is not proven.
2. Pause Sandy Springs Plumbing Email 2 because Email 1 bounced.
3. Leave audit fields intact and verify both records are paused.
4. Write completion artifacts/status updates.

Still prohibited:
new email sends, Poplar/SMS sends, prospect/customer contact, unrelated CRM writes, deploys, Paperclip mutations, git push, DNS/domain/hosting/billing changes, and Stripe actions.
```

### Optional Manual-Risk Approval For Delivered Sequences

```text
Approved: allow delivered email sequences to continue with manual reply-monitoring risk accepted for:
- tuckers-home-services
- tech-on-the-way
- perez-pools-llc

I accept that hello@gtmdot.com reply monitoring and automatic pause-on-reply are not fully proven.

Allowed:
1. Leave the listed sequences active.
2. Monitor CRM/Resend/hello@gtmdot.com read-only.
3. Stop and report if any bounce, complaint, unsubscribe, reply evidence, or provider error appears.

Still prohibited:
new manual email sends outside existing scheduled sequence behavior, Poplar/SMS sends, prospect/customer replies, unrelated CRM writes, deploys, Paperclip mutations, git push, DNS/domain/hosting/billing changes, and Stripe actions.
```

### Next Seven-Prospect Postcard Batch

Use the exact approval from:

- `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/2026-05-23-next-needs-approval-review-and-batch-proposal.md`

### Mailing Field Repair Approval

Not ready yet. First produce evidence packets for each missing mailing field. Then request one named CRM write approval at a time.

## Next Safe Work Under High-Autonomy Mode

Codex may continue without additional approval by:

1. Creating source-backed enrichment packets for missing address/email fields.
2. Preparing Cityboys visual QA packet.
3. Monitoring Poplar provider progression for newly submitted postcards.
4. Auditing scheduled email follow-ups and bounce/reply state read-only.
5. Drafting CRM v2 acceptance tests for channel truth, provider truth, reply monitoring, payload validation, and stale-note handling.

## Explicit No-Action Statement

No CRM/Supabase writes, Paperclip mutations, deploys, Poplar/Resend/SMS sends, prospect/customer contact, DNS/domain/hosting/billing changes, Stripe actions, git pushes, or production-impacting edits were performed while preparing this sweep.

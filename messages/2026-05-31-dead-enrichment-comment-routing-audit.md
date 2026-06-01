# Dead / Enrichment / Comment Routing Audit - 2026-05-31

Owner: Codex / GTMDot quarterback  
Mode: read-only CRM audit plus coordination recommendation  
Status: ready for CRM v2 and board-clearing follow-up

## Why This Exists

Jesse raised three problems after returning from vacation:

1. CRM shows `20` dead prospects, but many may not be truly dead.
2. `needs_enrichment` is unclear; it is not obvious what is holding those
   prospects back.
3. Jesse needs a place to leave comments that actually become work, not chat
   residue.

## Core Finding

The current CRM stage labels are doing too much work.

`dead` currently means "disqualified / dequeued / parked / duplicate / bad fit /
old policy decision / bad intake / test record" depending on the record. That
is not the same thing as "this business is dead."

`needs_enrichment` currently includes multiple prospects with live sites,
addresses, phones, emails, QA passes, and old resolved notes. Many are probably
not waiting on enrichment in the literal sense. They need a fresh revalidation
gate that says whether they are:

- ready for Jesse review,
- blocked by current evidence,
- missing contact/mailing fields,
- missing current assets,
- stale-note held,
- or truly parked.

## Current Dead Bucket

Fetched current CRM read-only. Every `dead` record appears to have
`disqualified=true`, but the reasons vary.

### Likely Hard Dead / Keep Out

- `douglasville-mobile-mechanics`: duplicate of `atl-mobile-mechanics`.
- `intake-test-llc`: test/no contact.
- `intake-test-2`: test/no contact.
- `atlanta-plumber-for-less`: no contact info.
- `roswell-pro-plumber`: lead-gen/referral funnel, not local trade business.
- `sandy-springs-plumber-sewer-septic`: AI/review-farm concern.
- `tire-and-ride-mobile`: rating below prior threshold.
- `cleveland-electric`: market mismatch.
- `posh-paws-atlanta`: no matching Atlanta business identified from intake.
- `doctor-concrete-atl`: bad/no GBP match for name/phone.
- `sandy-springs-plumbing-share`: explicitly dequeued as data-quality issue.

### Needs Revalidation / Not Necessarily Dead

- `bobs-hvac`: disqualified for no photos/reviews after old triage; later used
  as an AI receptionist seed. Needs current product-fit decision.
- `thompsons-fence`: suspicious identity concerns, but should be classified as
  `identity_risk` rather than plain dead.
- `chrissys-mobile-detailing`: disqualified because it had a real website; this
  may mean "poor fit for website-first offer," not dead.
- `atlantas-handyman`: disqualified because it had a real website; same issue.
- `zion-mobile-tire-services`: owner-name unverifiable; classify as
  `identity_unresolved`, not plain dead.
- `the-smart-company-llc`: dormant / address mismatch; probably parked, but
  should be classified as `dormant_or_stale`.
- `tgp-home-services`: dormant; classify as `dormant_or_stale`.
- `es-tree-service`: thin reputation / low review count; classify as
  `reputation_risk`, not dead.

## Current Needs Enrichment Bucket

Current `needs_enrichment` prospects:

- `premier-tv-mounting-atl`
- `azer-pool`
- `professional-gutter-cleaning`
- `plugged-electricians-atl`
- `trushyne-mobile-detailing`
- `sumptuous-mobile-detailing`
- `plumbingpro-north-atlanta`
- `hvac-guyz-plumbing-inc`
- `jack-glass-electric`

Observed pattern:

- Most have live preview sites.
- Several have address/phone/email.
- Several have old notes that are marked resolved, or notes that contradict
  later Bruce/current QA passes.
- Several notes are from April and should be stale-by-default unless
  revalidated with current evidence.

Likely current blockers by type:

- Contact/email missing: `premier-tv-mounting-atl`, `azer-pool`,
  `trushyne-mobile-detailing`, `plumbingpro-north-atlanta`,
  `hvac-guyz-plumbing-inc`, `jack-glass-electric`.
- Contact/mailing missing hard blocker: `jack-glass-electric` has no email,
  no address, and no phone in CRM despite site evidence mentioning a real phone.
- Stale design/photo notes likely need current recheck: `premier-tv-mounting-atl`,
  `professional-gutter-cleaning`, `plugged-electricians-atl`,
  `plumbingpro-north-atlanta`, `hvac-guyz-plumbing-inc`, `jack-glass-electric`.
- Already has enough surface for revalidation rather than generic enrichment:
  `professional-gutter-cleaning`, `plugged-electricians-atl`,
  `sumptuous-mobile-detailing`, and likely `hvac-guyz-plumbing-inc`.

## Recommended CRM v2 Model Changes

Replace overloaded stage-only interpretation with explicit fields:

- `pipelineStage`: where the prospect sits in the lifecycle.
- `disposition`: active, parked, duplicate, poor fit, dead, data risk,
  identity risk, dormant, test, lead-gen, reputation risk.
- `dispositionReason`: human-readable reason.
- `dispositionEvidenceUrl`: artifact/CRM note/Paperclip link.
- `lastRevalidatedAt`: timestamp.
- `revalidationOwner`: Codex, Bruce, Mini, Jesse, R1VS.
- `currentBlocker`: yes/no.
- `nextAction`: exact action, not inferred from stage.

For `needs_enrichment`, CRM v2 should show blocker chips:

- Missing email.
- Missing mailing address.
- Missing phone.
- Needs source-backed owner/contact.
- Needs current site QA.
- Needs hero/postcard assets.
- Needs stale-note revalidation.
- Needs Paperclip/R1VS packet.
- Ready for Jesse review.

## Where Jesse Should Put Comments

The rule:

If the comment is about a specific prospect, put it on that prospect's CRM
record as a current note/flag. If the comment creates work, it must include an
owner and desired outcome.

If the comment is about workflow, routing, policy, or cross-lane coordination,
put it in Paperclip as a parent issue/comment or send it to Codex to convert
into a Paperclip/file-ledger artifact.

Telegram/Slack/chat can notify people, but they are not the durable place for
the work.

## Comment Format

Use this format until CRM v2 has a proper feedback form:

```text
Prospect: <slug or business name>
Type: blocker | feedback | enrichment | stage | outreach | approval | note-cleanup
Current evidence: <what I am seeing now>
Desired action: <what should happen next>
Owner: Codex | Bruce | Mini | Outreach | Post-Build | Jesse
Blocking outreach? yes/no
```

Examples:

```text
Prospect: premier-tv-mounting-atl
Type: feedback
Current evidence: form/photo upload now appears fixed, old hero note may be stale.
Desired action: run current site/postcard QA and decide if this can leave needs_enrichment.
Owner: Post-Build
Blocking outreach? yes
```

```text
Prospect: bobs-hvac
Type: stage
Current evidence: marked dead for old no-photo/no-review triage, but may be useful for AI receptionist or new offer.
Desired action: revalidate disposition as parked/experiment candidate vs true dead.
Owner: Codex
Blocking outreach? no
```

## Immediate Catch-Up Recommendation

1. Create a revalidation queue for the `20` dead prospects, but do not revive
   any without current evidence and Jesse approval.
2. Run `needs_enrichment` through a current gate:
   contact fields, live site, claim lookup, postcard assets, current notes,
   and owner/source evidence.
3. Move prospects out of `needs_enrichment` only after current gate result:
   ready for Jesse review, needs field repair, needs asset repair, parked, or
   true disqualified.
4. In CRM v2, make Jesse's comments first-class work objects with owner,
   blocking flag, evidence, and status.

## Explicit No-Action Statement

This audit performed no CRM/Supabase writes, Paperclip mutations, deploys,
Poplar/Resend/SMS sends, prospect/customer contact, git pushes, production site
edits, DNS/domain/hosting/billing changes, Stripe actions, or destructive
cleanup.

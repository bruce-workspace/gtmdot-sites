# Piedmont Tires Mailing Field Evidence Packet - 2026-05-23

Owner: Codex / GTMDot quarterback  
Mode: source-backed evidence packet only  
Status: CRM write approval needed before repair  

## Purpose

Resolve the `piedmont-tires` postcard payload blocker by collecting source-backed mailing-field evidence. This packet does not write CRM truth.

## Current CRM State

- Slug: `piedmont-tires`
- Stage: `qa_approved`
- Business: Piedmont Tires
- Street address: `3483 Clairmont Rd`
- City: `Chamblee`
- State: `GA`
- ZIP: missing
- Email: none
- Postcard status: `not_submitted`
- Current blocker: `preview_postcard_payload` returns 400 because mailing fields are incomplete.

## Evidence Found

Public sources consistently support ZIP `30319` for `3483 Clairmont Rd`.

- Apple Maps lists Piedmont Tires & Repair at `3483 Clairmont Rd, Atlanta, GA 30319` with phone `(404) 990-1088`.
- Waze lists Piedmont Tires at `3483 Clairmont Rd, Atlanta, GA 30319`.
- Loc8NearMe lists Piedmont Tires & Repair at `3483 Clairmont Rd, Atlanta GA 30319` with phone `(404) 990-1088`.
- City-data / Georgia business-entity mirror lists the registered agent street address as `3483 Clairmont Road, Atlanta, GA, 30319`.
- LoopNet property data lists `3483 Clairmont Rd NE, Brookhaven, GA 30319`.

Source URLs:

- `https://maps.apple.com/place?place-id=IADFF0F4E9BA9EBC3`
- `https://www.waze.com/live-map/directions/united-states/georgia/chamblee/piedmont-tires-and-repair?to=place.ChIJ4e9z2cYJ9YgRMJkEnhv__EM`
- `https://www.loc8nearme.com/georgia/atlanta/piedmont-tires-and-repair/8447909/`
- `https://www.city-data.com/business-entities/GA/Piedmont-Tires-and-Repairs-Inc-20053366-GA.html`
- `https://www.loopnet.com/property/3483-clairmont-rd-ne-brookhaven-ga-30319/13089-18%20236%2006%20013/`

## Interpretation

The strongest operational mailing candidate is:

- Street: `3483 Clairmont Rd NE`
- City: `Atlanta`
- State: `GA`
- ZIP: `30319`

The CRM currently says `Chamblee`; some sources classify the business as Chamblee-area, but the mailing address sources most consistently render the postal city as `Atlanta` or property locality as `Brookhaven`, both with ZIP `30319`. For Poplar deliverability, the least risky repair is to use the full source-backed postal-style address rather than only adding ZIP to the current `Chamblee` city value.

## Recommended Repair

Request explicit CRM write approval to update Piedmont Tires mailing fields to:

- `address = "3483 Clairmont Rd NE"`
- `city = "Atlanta"`
- `state = "GA"`
- `zip = "30319"`

Then rerun `preview_postcard_payload` and the standard Post-Build gates before any postcard approval or send.

## Exact Approval Text

```text
Approved: repair Piedmont Tires CRM mailing fields from source-backed public evidence.

Allowed:
1. Update `piedmont-tires` CRM mailing fields to:
   - address: 3483 Clairmont Rd NE
   - city: Atlanta
   - state: GA
   - zip: 30319
2. Rerun read-only `preview_postcard_payload` and Post-Build gates.
3. Write a completion or blocker artifact.

Still prohibited:
Poplar postcard submit, Resend/email send, SMS, prospect/customer contact, unrelated CRM edits, Paperclip mutations, deploys, git push, DNS/domain/hosting/billing changes, and Stripe actions.
```

## Explicit No-Action Statement

No CRM/Supabase writes, Paperclip mutations, deploys, Poplar/Resend/SMS sends, prospect/customer contact, DNS/domain/hosting/billing changes, Stripe actions, git pushes, or production-impacting edits were performed.

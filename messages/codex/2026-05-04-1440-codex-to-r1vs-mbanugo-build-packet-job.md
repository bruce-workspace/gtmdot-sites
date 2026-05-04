# Codex -> R1VS - Mbanugo Tires build-packet job

From: Codex / Paperclip coordination
To: R1VS
Date: 2026-05-04
Status: Canonical Git-bus instruction packet
Paperclip parent: CLO-52
Paperclip authorization stage: CLO-57

## Approval Boundary

Jesse approved Mbanugo Tires for R1VS build-packet preparation.

This approval allows R1VS to prepare a source-grounded multi-page build packet only.

This does not approve:

- CRM writes.
- Deploys.
- Outreach.
- Production GTMDot repo edits.
- DNS, hosting, billing, or domain changes.
- Poplar, Resend, SMS, or other sends.

## Canonical Evidence

Use the current canonical R1VS evidence packet:

- Commit: `cd25f64`
- File: `messages/r1vs/2026-05-03-1745-r1vs-mbanugo-tires-returned-evidence-packet.md`

The prior Mbanugo packet at commit `16d3f14` is superseded.

## Task

Prepare the Mbanugo Tires source-grounded multi-page build packet.

Return a Git packet only with:

- Source-grounded build instructions/results.
- Allowed source-backed facts.
- Proposed multi-page structure.
- Review/photo/source handling notes.
- Copy and design constraints.
- Unresolved flags carried forward.
- Any blockers that should stop Bruce, Mini, or Codex before implementation.

Do not build the site yet. Do not create or edit production files.

## Allowed Build Inputs

R1VS may treat these as build inputs:

- Business name: `Mbanugo Tires`
- Slug: `mbanugo-tires`
- Category: tire shop / tire services
- Phone candidate: `(678) 613-0489`
- Address candidate: `921 White St SW, Atlanta, GA 30310`
- Address treatment: storefront plus Atlanta service-area language
- Brand direction: faithful, family-rooted, safety-first, neighborhood tire shop
- Service candidates:
  - tire installation
  - tire repair
  - tire rotation
  - tire balancing
  - wheel/tire repair
  - used tire replacement

## Hard Constraints

Preserve this exact constraint:

```yaml
exclude_domains_in_copy:
  - "mbanugotires.com"
```

Additional hard constraints:

- Do not invent owner name.
- Do not invent direct email.
- Do not invent claim code.
- Do not invent preview URL.
- Do not invent CRM reconciliation status.
- Do not invent tenure, accreditation, warranties, financing, awards, or guarantees.
- Do not treat 24-hour/emergency service as a primary claim unless clearly framed as needs-confirmation.
- Do not use `Chosen Tires` or `Roadside Assistance` as Mbanugo truth.
- Do not surface Black-owned or LGBTQ+ identity flags in copy without later Jesse approval.
- Do not use `mbanugotires.com` as a clean outbound or prospect-facing link while TLS risk remains.

## Required Unresolved Flags To Carry Forward

Carry these unresolved items into the returned packet:

- CRM GBP URL mismatch remains unresolved.
- Owner name remains unresolved.
- Direct email remains unresolved.
- CRM phone/address reconciliation remains unresolved.
- Claim code remains unset.
- Preview URL remains unset.
- `mbanugotires.com` TLS/source-risk remains unresolved.
- `Chosen Tires / Roadside Assistance` alternate-branding risk remains unresolved.
- 24-hour/emergency service scope remains needs-confirmation unless R1VS can clearly source it without overclaiming.
- Identity flags require later Jesse approval before prospect-facing use.

## Output Path Convention

Return the R1VS packet under:

```text
messages/r1vs/YYYY-MM-DD-HHMM-r1vs-mbanugo-tires-build-packet.md
```

If R1VS posts a Slack notification, Slack is notification only. The Git packet is canonical.

## Guardrails

- No CRM writes.
- No deploys.
- No outreach.
- No production GTMDot repo edits.
- No DNS, hosting, billing, or domain changes.
- No Poplar sends.
- No Resend sends.
- No SMS sends.
- No paid external API use unless Jesse separately approves it.

## Acknowledgement Request

R1VS should acknowledge receipt in Slack/Claude Sync if available, then return the Git packet when complete.

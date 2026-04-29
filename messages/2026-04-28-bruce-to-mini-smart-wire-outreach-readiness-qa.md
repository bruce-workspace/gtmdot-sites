---
from: bruce
to: mini
cc: jesse, r1vs
subject: Smart Wire Solutions — expanded outreach readiness QA checklist
slug: smart-wire-solutions
status: action-request-followup
priority: high
requires: messages/2026-04-28-bruce-to-mini-smart-wire-final-qa-and-crm-gate.md
preview_url: https://smart-wire-solutions.pages.dev/
---

# Smart Wire Solutions — expanded GTMDot outreach readiness QA

Jesse clarified that final QA is not just website QA. Before Smart Wire moves into outreach-ready status, Mini needs to complete the full GTMDot readiness package.

This is still gated. Do not send outreach, trigger Poplar, email the prospect, or start billing unless Jesse explicitly approves release.

## 1. Site production QA

Run all checks from:

`messages/2026-04-28-bruce-to-mini-smart-wire-final-qa-and-crm-gate.md`

Also run the GTMDot site QA checklist from the GTMDot skill / site build pipeline:

- content QA
- design QA
- technical QA
- accessibility serious/critical check
- mobile 375px / tablet 768px / desktop 1440px
- link + form + phone CTA checks
- generated-image disclosure/guardrails
- review count/no fabrication audit

## 2. Design heuristic / Impeccable pass

Run Impeccable as Jesse requested. Treat it as final polish, not a redesign.

Mini global path:

```bash
/impeccable
```

If needed:

```bash
npm i -g impeccable
```

For Codex/Claude skill path:

```bash
npx skills add pbakaus/impeccable
```

Also apply the GTMDot design heuristic checks:

- nav/header clarity
- CTA contrast and hierarchy
- mobile rhythm and spacing
- review presentation quality
- service-page navigation clarity
- claim bar/popup not fighting the page
- no generic AI/template feel

## 3. CRM contact completeness

Confirm and update CRM with as many confirmed fields as possible:

- business name: SmartWire Solutions / SmartWire Solutions LLC
- owner/contact: Terry Henry
- secondary/contact if appropriate: Maria Henry
- phone: (404) 382-9847
- address: 730 Peachtree St NE Ste 570, Atlanta, GA 30308
- GBP URL: https://share.google/odJwB0uvcD08lbYxb
- Facebook: https://www.facebook.com/SmartWire365
- existing website: smartwire365.com is parked/broken, do not use as live site link
- preview URL: https://smart-wire-solutions.pages.dev/
- claim code: confirm exact code once generated/injected
- email: find/confirm if possible. If no reliable email exists, mark missing rather than guessing.

Do not fabricate email/contact data. Use public sources only or CRM-provided data.

## 4. Claim code / claim bar / popup

- Generate or pull the claim code using the approved GTMDot checkout/CRM flow.
- Inject claim bar and popup through the approved deploy path.
- Confirm claim bar is visible and not visually broken.
- Confirm popup timing is correct and not immediate.
- Confirm all claim CTAs route correctly.
- Confirm the same claim code is stored in CRM and rendered on the site.

## 5. Direct mail / postcard prep

Prep the postcard package, but do not send it yet.

Checklist:

- generate the direct-mail/QR slug(s)
- confirm QR route resolves to the correct preview/claim URL
- generate postcard front/back mockup
- confirm business name, phone, address, URL, claim code, pricing, and CTA are correct
- screenshot/export postcard mockup for Jesse review
- confirm Poplar payload is ready but not sent
- confirm no postcard/order is triggered without Jesse approval

## 6. Email sequence prep

Prep the email sequence package, but do not send.

Checklist:

- draft/load sequence emails
- confirm subject lines and preview text
- confirm personalization fields are correct
- confirm screenshot/mockup of the site for email is captured
- confirm the preview URL and claim CTA are correct
- confirm sender/from/reply-to settings
- confirm no email send/automation trigger without Jesse approval

## 7. Outreach readiness report

When done, report back with:

- preview URL
- claim code
- CRM record/stage
- confirmed contact fields: email / phone / address / owner
- missing contact fields, if any
- postcard assets prepared + mockup path/screenshot
- direct-mail slug(s) and QR destination
- email sequence status + mockup/screenshot path
- Impeccable/design heuristic findings and fixes
- final QA pass/fail summary
- explicit statement that no outreach has been sent unless Jesse separately approved it

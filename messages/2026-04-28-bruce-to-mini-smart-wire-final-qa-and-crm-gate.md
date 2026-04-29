---
from: bruce
to: mini
cc: jesse, r1vs
subject: Smart Wire Solutions — final QA gate + CRM stage prep
slug: smart-wire-solutions
status: action-request
priority: high
commit_required: 193f0c0
preview_url: https://smart-wire-solutions.pages.dev/
---

# Smart Wire Solutions — Mini final QA gate

Jesse has approved the site direction after Bruce's final polish pass. Pull latest `gtmdot-sites/main` and verify commit `193f0c0` or newer.

Preview URL:
https://smart-wire-solutions.pages.dev/

## Your job now

Run the final production QA gate before any outreach release.

Required checks:

1. Confirm the latest deployed preview includes Bruce's final polish:
   - no blue dot beside wordmark
   - SmartWire logo mark in nav with transparent background
   - hero pills stacked on desktop
   - nav `Get an Estimate` text is white
   - services dropdown works on desktop
   - service links appear in mobile hamburger
   - gallery placeholder/context overlays are gone
   - review pull quote + review auto-scroll are present
   - trust callouts are 2x2 on mobile

2. Claim code / claim bar / popup:
   - pull or generate the correct claim code using the GTMDot/CRM checkout flow
   - inject claim bar/pop-up only through the approved deploy path
   - confirm claim code appears correctly
   - confirm pop-up timing is not immediate/annoying
   - confirm claim CTA links route correctly

3. Link + form QA:
   - all nav links
   - all services dropdown links
   - all mobile hamburger links
   - phone links
   - form submission path
   - Google review link
   - footer links
   - all four service detail pages

4. Mobile + desktop formatting QA after injection.

5. Run Impeccable final pass. Jesse specifically requested this as a final QA gate, not a redesign pass.
   - Mini global command: `/impeccable`
   - If needed: `npm i -g impeccable`
   - For skill install path: `npx skills add pbakaus/impeccable`

6. Run the normal GTMDot gates again after injection.

## CRM stage

After final QA passes, move Smart Wire to the appropriate CRM stage for preview-approved / ready-for-outreach, but do not release outreach unless Jesse's CRM process requires that stage to queue only and not send.

Do not trigger Poplar postcards, outbound email, billing, or any prospect-facing outreach unless Jesse explicitly confirms release.

## Report back

Post a message with:

- preview URL
- claim code used
- QA pass/fail summary
- Impeccable findings + fixes
- CRM stage moved to
- anything still needing Jesse approval

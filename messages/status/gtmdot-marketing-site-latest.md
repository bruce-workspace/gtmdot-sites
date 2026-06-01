Lane: GTMDot Marketing Site / Conversion Flow
Session: GTMDot marketing-site Codex thread
Updated: 2026-05-23T12:34:39-04:00
Owner: Codex marketing-site lane
Mode: local site improvement / coordination handoff

Current objective:
Improve the public GTMDot marketing site so non-technical local business owners
understand the offer quickly, know what to do with a claim code, and have a
stronger path to request a free preview if they do not have a code.

Current lane status:
The GTMDot homepage has local, undeployed updates in
`/Users/bruce/.openclaw/workspace/gtmdot/sites/gtmdot/index.html`.
The work focuses on conversion copy, claim-code handling, clearer CTAs,
pricing clarity, add-on clarity, and a lighter "Try this now" trust-test
section. The local preview at `http://localhost:8788/` was responding during
validation.

Active blockers:
- These marketing-site changes are local only unless a coordinator/Jesse deploy
  approval is given.
- Claim-code checkout routing should be verified against the intended backend
  and Stripe/checkout behavior before public deployment.
- The homepage is now long enough that a multi-page site plan should be
  approved before adding more homepage sections.
- This lane does not own CRM stage truth, outreach sends, Poplar/Resend,
  customer contact, Paperclip mutation, billing, DNS, hosting, or prospect
  decisions.

Prospects/items closest to revenue:
- Owned by this lane: the GTMDot homepage conversion path itself, especially
  claim-code entry, "Build me a site" CTAs, first-month $49 framing, and the
  preview request form.
- Cross-lane observed from existing status files: `GTM-13` InTire Mobile Tire
  Shop appears technically closest to revenue pending Jesse/coordinator approval
  for stage movement and outreach channels.
- Cross-lane observed: `GTM-12` Harrison appears ready for a postcard-only
  decision under the stale-note policy.
- Cross-lane observed: `GTM-11` The Appliance Gals remains blocked by a hero
  display failure.

What can be safely advanced without Jesse present:
- Continue copy/design tightening on the GTMDot marketing site locally.
- Draft a multi-page information architecture for GTMDot.com.
- Prepare page split recommendations for Home, Pricing, How It Works, What You
  Get, Examples, Support, and future industry SEO pages.
- Run local syntax/design checks and document results.
- Keep changes in local files or handoff artifacts only.

What requires explicit Jesse approval:
- Deploying GTMDot.com marketing-site changes.
- Changing checkout, Stripe, billing, pricing logic, DNS, domain, hosting, or
  production routing.
- Any outreach send, Poplar postcard submit, Resend email trigger, SMS,
  prospect/customer contact, or CRM stage move.
- Strategic CRM truth decisions or Paperclip mutation.
- Publicly committing to a new multi-page site structure or pricing language
  beyond local draft work.

Files/artifacts changed:
- `/Users/bruce/.openclaw/workspace/gtmdot/sites/gtmdot/index.html`
- `/Users/bruce/.openclaw/workspace/gtmdot/docs/2026-05-17-crm-v2-outreach-paperclip-bridge.md`
- `/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/status/gtmdot-marketing-site-latest.md`

Recent validation:
- Inline scripts in `sites/gtmdot/index.html` parsed successfully.
- `impeccable --json sites/gtmdot/index.html` returned no issues after the
  lighter "Try this now" section update.
- Local preview responded at `http://localhost:8788/`.
- Playwright check confirmed the "Try this now" section renders with warm cream
  background, white question tiles, and one soft purple accent tile.

Recommended next 3 actions:
1. Main coordinator decides whether this lane should deploy the current GTMDot
   homepage updates now or hold them until the multi-page plan is approved.
2. Draft the GTMDot.com multi-page roadmap with a short homepage, dedicated
   pricing page, how-it-works page, examples page, support/custom-request page,
   and future industry SEO pages.
3. Verify claim-code lookup to checkout end-to-end in a safe test mode before
   any production deployment.

Actions explicitly not performed:
- No deployment.
- No CRM/Supabase writes.
- No Paperclip mutation.
- No Poplar/Resend/SMS sends.
- No prospect/customer contact.
- No git push.
- No Stripe, billing, DNS, domain, or hosting changes.

Cross-lane impacts:
- Main coordinator should treat this as a conversion-path/site-positioning
  status, not an outreach or CRM status.
- Outreach and Post-Build should not infer any send approval from the homepage
  copy or claim-code modal.
- Platform/CRM v2 should be aware that the public site now frames claim-code
  users and no-code preview users as two distinct conversion paths.

Notify:
Main Codex coordinator, GTMDot Platform / CRM v2, Outreach Operations,
Post-Build Operations.

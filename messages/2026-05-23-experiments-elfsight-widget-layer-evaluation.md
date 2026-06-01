# Experiments - Elfsight Widget/Add-On Layer Evaluation

Updated: 2026-05-23T15:17:28-04:00
Owner: Codex Experiments lane
Mode: local-only planning artifact

## Scope

Jesse has a premium Elfsight subscription. This evaluates Elfsight as a future GTMDot widget/add-on layer, especially for a default demo lead-capture chatbot/form widget on unclaimed preview sites.

No Elfsight widgets were created. No embed code was added anywhere. No CRM, Paperclip, prospect site, deploy, send, billing, or routing action was performed.

Direction update: do not prioritize Elfsight for current pipeline sites or board clearing. Treat it as a future module for new GTMDot sites and CRM v2 planning only.

## Source Notes

- Elfsight Embed SDK README: https://github.com/elfsight/embed-sdk#getting-started
- Elfsight Contact Form: https://elfsight.com/contact-form-widget/
- Elfsight AI Chatbot: https://elfsight.com/ai-chatbot-widget/
- Elfsight Live Chat / All-in-One Chat: https://elfsight.com/all-in-one-chat-widget/
- Elfsight All-in-One Reviews: https://elfsight.com/all-in-one-reviews-widget/html/
- Elfsight Social Feed: https://elfsight.com/social-feed-widget/

## Evaluation Answers

1. Can Elfsight support a default chatbot/contact/lead-capture widget?

Yes, likely via Contact Form, Form Builder, or AI Chatbot. Contact Form is the safest MVP fit because it supports configurable fields, required fields, email notifications, dashboard submissions, integrations, reCAPTCHA, and a custom thank-you message. AI Chatbot is more impressive but higher risk on unclaimed preview sites because conversational copy can imply that the business is actively receiving or responding unless tightly constrained.

A manually created Elfsight Contact Form widget can plausibly serve as the default demo lead-capture widget, as long as it is configured with GTMDot-safe copy, required fields, a clear demo disclaimer, and GTMDot-only routing for unclaimed previews. A manually created AI Chatbot may work later, but it should not be the first default demo because it creates more copy, support, and routing ambiguity.

2. Is Elfsight better than our own simple embedded lead form for this MVP?

For a fast visual demo, yes: Elfsight can make the preview site feel more premium with little engineering. For system control, no: our own embedded form is better if we need deterministic routing, internal demo submissions, CRM event capture, exact copy control, and no third-party script dependency. Recommended MVP: start with our own simple demo lead form pattern as the canonical route, then test Elfsight Contact Form as a premium/add-on layer once routing and disclaimers are settled.

3. Which Elfsight widgets could help GTMDot sites?

- Contact Form / Form Builder: best candidate for unclaimed preview lead-capture demo and claimed-site intake forms.
- AI Chatbot: future premium add-on or demo upgrade, but only after strict unclaimed/claimed routing rules exist.
- All-in-One Chat / Live Chat: useful for claimed sites that want WhatsApp/Messenger/Telegram style contact, not safe for unclaimed previews unless routed only to GTMDot and clearly labeled.
- All-in-One Reviews / Google Reviews: strong value for local-business credibility after the right source/profile is verified.
- Testimonials Slider: useful where reviews are manually curated, but less ideal than real reviews for source-grounded GTMDot previews.
- Social Feed / Instagram Feed: useful when a business has current public social proof.
- Photo Gallery: useful for trade portfolios and before/after proof, especially when Post-Build already has approved image assets.

4. Is the Embed SDK useful for CRM v2 widget management, or is manual embed simpler?

Manual embed code is simpler for the MVP. The SDK is useful later if GTMDot wants CRM v2 to act as a widget management console: show an app catalog, create/edit/remove widgets, and store callback data like widget id, widget URL, embed code, DOM code, and app alias. The SDK appears designed for platforms/builders, not a one-off embed flow. For now, CRM v2 should store widget metadata and approval/routing state; it should not become an Elfsight dashboard until the product need is proven.

The current SDK docs do not look like a simple "API key -> create widget" flow. They describe embedding Elfsight's catalog/editor UI and receiving widget data back from a callback: widget id, URL, embed code, element, and app alias. That is useful for a future CRM v2 widget-management surface, but it is probably too much machinery for the near-term MVP. Manual Elfsight embed snippets are enough until GTMDot needs self-serve widget creation/editing inside CRM v2.

5. What fields would CRM v2 need per prospect?

- `widget_provider`: `elfsight` or `gtmdot_native`
- `widget_id`
- `widget_app_alias`
- `widget_name`
- `widget_embed_code`
- `widget_embed_script_url`
- `widget_embed_class_or_selector`
- `widget_url`
- `widget_dashboard_url`
- `widget_enabled`
- `widget_placement`: `floating`, `hero_inline`, `contact_section`, `footer`, `reviews_section`, etc.
- `widget_approval_state`: `not_started`, `draft`, `internal_demo`, `approved_for_preview`, `approved_for_claimed_site`, `disabled`
- `widget_claim_state`: `unclaimed_demo`, `claimed_live`, `disabled`
- `widget_routing_mode`: `gtmdot_preview_team`, `business_owner`, `dual_internal_and_owner`, `disabled`
- `widget_routing_destination_label`: human-safe label, not necessarily raw email/phone
- `widget_last_verified_at`
- `widget_last_verified_by`
- `widget_privacy_notes`
- `widget_performance_notes`
- `widget_copy_variant`
- `widget_disclaimer_required`
- `widget_disclaimer_text`
- `widget_source_of_truth`: Elfsight dashboard, GTMDot native, manual embed, etc.
- `widget_created_manually`: boolean
- `widget_sdk_managed`: boolean

CRM v2 UX should surface this as a small "Widget Layer" panel with a clear claimed/unclaimed routing badge, placement, approval state, last verified date, and hard warnings when a widget could imply the business receives messages before it actually does.

6. How should claimed vs unclaimed routing work?

Unclaimed previews:

- All submissions route only to GTMDot/Jesse/internal preview team.
- Copy must say the form is a demo and messages go to GTMDot until the site is claimed.
- Do not use owner-facing language like "we will call you back" unless GTMDot is explicitly handling the response.
- CTA paths:
  - `Claim this website` -> claim/checkout URL.
  - `Send a test lead` -> demo/internal route only.
  - `Ask about this preview` -> GTMDot/Jesse route, not business owner.

Claimed sites:

- Route to business owner channels only after explicit owner setup and verification.
- CRM should store `claimed_live` plus verified destinations and last test timestamp.
- Owner-facing copy can describe business response only after routing is live and approved.

7. Risks

- Third-party scripts: Elfsight script availability, vendor changes, CSP/security, and script conflicts.
- Performance: external JS may affect Core Web Vitals, especially on lightweight preview pages.
- Branding: Elfsight branding may appear depending on plan/widget settings; visual style may not match GTMDot templates.
- Privacy: submissions and chat transcripts may live in Elfsight systems; need policy language and internal handling rules.
- Support: GTMDot would inherit support questions about widgets it does not fully control.
- Pricing/account ownership: Jesse's premium subscription may not map cleanly to future client ownership, transfer, or per-client billing.
- Routing truth: unclaimed sites must not imply business monitoring.
- Data portability: Elfsight dashboard submissions may not automatically become CRM events without integration work.
- SEO/source integrity: review widgets must use verified profiles and should not replace source-grounded site content.

8. Where this belongs

Now: Experiments, because it is an unproven widget/add-on layer and must stay local-only.

Later: CRM v2 should own widget state, approval/routing fields, and operator UX. Post-Build should own site placement, visual QA, performance checks, and claimed-site embed readiness for new multi-page sites going forward. Outreach should only see this once it affects claim/checkout or approved customer-facing messaging.

Current pipeline sites should not be retrofitted for Elfsight as part of remote-week board clearing.

9. Safest local-only MVP

Create a static/local mock spec for a GTMDot-native demo lead form and an Elfsight-equivalent variant, without creating an Elfsight widget or embedding scripts. The demo copy should be:

Title: "Never miss another lead again."

Explanation: "This demo lead form shows how your claimed site can capture customer requests while you're on a job, after hours, or unable to answer the phone. Messages submitted here go to the GTMDot preview team until the site is claimed."

Fields:

- name
- phone
- email
- service needed
- urgency
- message

Buttons:

- `Claim this website` -> claim/checkout URL.
- `Send a test lead` -> local/internal demo route only.
- `Ask about this preview` -> GTMDot/Jesse route only.

## Recommended MVP Path

1. Keep Elfsight in Experiments and do not embed anything on production preview sites yet.
2. Keep current pipeline and board-clearing sites out of scope.
3. For future new multi-page GTMDot sites, start with a manually created Elfsight Contact Form embed snippet if Jesse wants to use the premium subscription.
4. Store the manual embed metadata in CRM v2 planning fields before considering any SDK integration.
5. Consider SDK integration only if CRM v2 needs in-app widget creation/editing/catalog management, not just display of a known widget.
6. Ask Jesse for a future explicit approval only when there is a specific new site, widget type, embed snippet, routing destination, copy, and verification plan.

## CRM v2 Field/UX Implications

CRM v2 should treat widgets as channel infrastructure, not decorative site content. The useful UI is a compact panel per prospect:

- Widget status: none, draft, internal demo, preview enabled, claimed live, disabled.
- Routing badge: GTMDot preview team, business owner, dual, disabled.
- Placement: floating, contact section, homepage band, reviews section.
- Provider: native, Elfsight Contact Form, Elfsight AI Chatbot, Elfsight Reviews, Elfsight Social Feed.
- Approval gate: requires Jesse approval for unclaimed public embed and owner approval for claimed routing.
- Last verification: timestamp plus who verified.
- Risk flags: third-party script, unclaimed routing, privacy copy missing, performance unknown, business-response implication.

The CRM v2 operator should be able to answer quickly: "Is there a widget? Is it live? Who receives submissions? Is that approved? When was it tested?"

Near-term CRM v2 storage can stay simple:

- widget id
- app alias
- embed code
- enabled/disabled
- placement
- approval state
- claimed/unclaimed routing mode
- last verified timestamp

SDK-specific fields can stay nullable until CRM v2 actually embeds the Elfsight catalog/editor.

## Exact Approval Needed Before Live Work

Approval packet should name:

- Prospect/site slug.
- Whether this is a new site or an existing pipeline site. Existing pipeline sites should default to hold.
- Widget provider and widget type.
- Manual embed snippet or SDK-managed flow.
- Exact copy and disclaimer.
- Exact fields.
- Placement.
- Routing destination.
- Whether submissions are demo-only or live business leads.
- Verification plan.
- Rollback plan.

No broad "try Elfsight" approval should be treated as enough for production.

## Explicit No-Action Statement

No Elfsight widget was created. No Elfsight account or dashboard action was taken. No embed code was added. No production preview site was changed. No CRM/Supabase writes, Paperclip mutations, deploys, Poplar/Resend/SMS sends, Retell/Twilio/Resend actions, prospect/customer contact, git pushes, DNS/domain/hosting/billing changes, Stripe actions, real lead routing, or production-impacting edits were performed.

# TERMINOLOGY-MAPPING.md

Per-vertical mapping of the right call-to-action (CTA) verb / phrasing for each service type. Companion to `ICON-MAPPING.md`.

R1VS uses this on first build. Mini verifies during QA pass §11.7.

If a CTA on a built site doesn't match the right phrasing for the service type, Mini bounces it back to either R1VS (if structural — wrong button text on a service page) or Mini fixes it itself during the polish pass (if it's just the homepage CTA).

---

## The four CTA categories

| Category | When to use | Example phrasings |
|---|---|---|
| **Estimate** | Variable-pricing trade work where the actual cost depends on diagnosis or measurement | "Get a Free Estimate", "Request Estimate", "Free Estimate" |
| **Quote** | More formal pricing offer, often commercial or larger residential project | "Request a Quote", "Get a Quote" |
| **Service booking** | Set-priced or transactional services where pricing is mostly known | "Book a Service", "Schedule Service", "Book Now" |
| **Consultation / Walkthrough** | Advisory before the work, often for design or large planning | "Schedule a Consultation", "Book a Walkthrough", "Free Walkthrough" |

---

## Vertical → CTA mapping

| Vertical | Primary CTA | Secondary CTA | Notes |
|---|---|---|---|
| **HVAC** (residential repair / install / maintenance) | "Get a Free Estimate" | "Call Now" (emergency) | Estimate is industry-standard. Emergency variant for after-hours pages. |
| **Plumbing** (residential) | "Get a Free Estimate" | "Call 24/7" (emergency) | Estimate is industry-standard. |
| **Plumbing** (commercial) | "Request a Quote" | "Call Now" | Commercial pricing more variable + formal. |
| **Plumbing — septic/sewer specialty** | "Request Service" | "Call Now" | Often emergent; estimate vs service-call distinction matters. |
| **Electrical** (residential) | "Get a Free Estimate" | "Request Estimate" | Same as HVAC pattern. |
| **Drywall + Painting** | "Request Estimate" | "Free Estimate" | Estimate is right because pricing depends on damage scope. |
| **Roofing** | "Free Estimate" | "Request a Quote" (commercial) | Industry-standard. |
| **Pressure washing / softwash** | "Free Estimate" | "Get a Quote" (commercial multi-property) | Variable pricing per square footage. |
| **Landscape + hardscape** | "Free Estimate" | "Schedule a Walkthrough" (large projects) | Walkthrough for full-yard remodel; estimate for single services. |
| **Gutter cleaning** | "Free Estimate" | — | Variable per home size. |
| **Mobile auto mechanic** (broad scope) | "Request Service" | "Call Now" | Transactional but variable. Don't use "Estimate" — implies upfront scoping for a moving-target diagnostic. |
| **Mobile tire / brake** (specialty) | "Book Service" | "Call Now" | Often roadside / emergency; book or call, don't estimate. |
| **Tire shop** (in-store) | "Call Now" | "Stop By" | Walk-in or call ahead, not formally booked. |
| **Auto detailing** (in-shop) | "Book a Detail" | "Schedule Service" | Set-priced packages; book don't estimate. |
| **Auto detailing — mobile / ceramic** (premium) | "Book a Detail" | "Get a Quote" (ceramic high-ticket) | Detail is set-priced; ceramic is quoted. |
| **Auto body / collision** | "Get an Estimate" | "Request Estimate" | Industry-standard for body/collision shops. |
| **Handyman** (general) | "Request Service" | "Get a Quote" | Mix; "Request Service" for one-off, "Get a Quote" for project lists. |
| **Remodeler** (kitchen / bath / full-home) | "Schedule a Walkthrough" | "Request Estimate" | Walkthrough first for big remodels; estimate is the second step. |
| **Remodeler / handyman hybrid** (e.g., TGP Home Services) | "Request Estimate" | "Schedule a Walkthrough" (large projects) | Mix — match button text to the page (services page vs contact page). |
| **Junk removal** | "Get a Quote" | "Book Pickup" | Quote for variable load; book once price agreed. |
| **Pest control** | "Free Inspection" | "Schedule Service" | Inspection is industry-standard first step. |
| **Pool service** | "Free Estimate" | "Book Service" | Estimate for setup/repair, book for recurring service. |
| **Locksmith** | "Call Now" | — | Almost always emergency; call directly. |
| **Fence installation** | "Free Estimate" | "Schedule a Walkthrough" | Walkthrough for property-line/scope review. |
| **Concrete / masonry** | "Free Estimate" | "Get a Quote" (commercial) | Estimate is right; pricing depends on material + square footage. |
| **TV mounting** | "Book Service" | "Get a Quote" (multi-room) | Set-priced per mount; quote for multi-mount jobs. |
| **Mobile car wash** (set service) | "Book a Wash" | "Schedule Service" | Set-priced. |
| **Lead-gen broker site** | (DEAD-STAGE — not a real local trade business; do not build) | — | See `roswell-pro-plumber` and `posh-paws-atlanta` patterns. |

---

## Anti-patterns to flag (Mini bounces back to R1VS or rewrites)

- "Get a Free Estimate" on a tire-rotation or oil-change site → use "Book a Service"
- "Schedule a Consultation" on a basic handyman site → overshoots the formality; use "Request Service"
- "Call Now" on a non-emergency service when "Get a Free Estimate" is more appropriate → underuses the trust-building CTA
- "Get a Quote" on an emergency-plumbing site → wrong urgency; use "Call 24/7"
- Generic "Contact Us" on any site → too weak; always pick a specific verb

---

## Form field labels too

The CTA on the button should match the labels in the form:
- Button "Get a Free Estimate" → form heading "Tell us about your project" or "Tell us what you need estimated"
- Button "Book a Service" → form heading "Schedule your appointment"
- Button "Request a Quote" → form heading "Tell us about your project"
- Button "Call Now" → no form needed; phone number prominent

---

## Updates to this file

This file should grow as new verticals are added to the prospect pool. To add a new vertical:
1. Identify the closest existing pattern (e.g., a new trade is most like HVAC vs handyman vs auto body)
2. Add a row to the table with the right CTA + reasoning
3. Commit with `docs(terminology-mapping): add <vertical>` per the CLAUDE.md §80-99 rules

---

*Created 2026-04-20 alongside `HANDOFF-CONTRACT.md` §11 expansion. Vertical CTAs reflect industry conventions plus Jesse's call on what reads naturally for each service category.*

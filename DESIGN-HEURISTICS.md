# DESIGN-HEURISTICS.md

**Purpose:** Capture the editorial + design judgment that makes GTMDot sites feel hand-built rather than templated. Any Claude on the pipeline (R1VS, Mini, future) should read this before making visual or content decisions.

This is global. It applies to new builds, retrofits, polish passes, and rebuilds. Read alongside `SKILL.md` (the workflow), `CLAUDE.md` (the contract), and `ICON-MAPPING.md` (the icon source of truth).

---

## The core discipline: read before you design

Before writing any HTML, selecting any icon, or picking any pull quote:

1. **Read `reviews.json` end-to-end.** Every review. You're looking for: named techs, specific stories, emotional hooks, differentiators the owner doesn't mention themselves.
2. **Read `RESEARCH.md` end-to-end.** Founding year, team names, certifications, service scope, pricing signals.
3. **Glance at the existing `index.html` hero stats bar.** You need this memorized before touching the story section, to enforce rule 3 (no dup).

If `reviews.json` has `captured: 0`, **stop.** You cannot generate pull quotes without verbatim content. Flag for Bruce retry or owner input in the finalization message.

---

## 1. Icon selection — `ICON-MAPPING.md` is the source of truth

- **Never freestyle icons.** Every service card icon must match `ICON-MAPPING.md` for that service type. Every site, every time.
- **When choosing among Lucide options, prefer literal over abstract.**
  - `shower-head` beats `droplets` for pressure washing
  - `key-round` beats `lock` for locksmith
  - `wrench` beats `settings` for handyman
  - `refrigerator` beats `box` for appliance repair
- **One icon library.** Lucide only. Never mix Font Awesome, Material Icons, or emoji in the same site.
- **Icon containers.** Every icon sits inside a 48–52px box with `background: var(--accent-bg)` and `border-radius: 12px`. Never bare icons in service-card headers.

---

## 2. Photo selection + wiring intent

### What to pick for each slot
- **Hero background:** owner in action, branded vehicle, or team shot. Never a generic cityscape if you have an owner photo. Never stock when you have GBP.
- **Gallery cards:** actual jobs — before/after, in-progress, finished work with the owner/crew visible. **NOT stock.** If you only have stock options available, skip the gallery section rather than fake it.
- **Section backgrounds (area, CTA, FAQ split):** Unsplash is OK here. This is the only layer where stock is acceptable.

### Wiring captions to photo content
- If the hero shows a named person, reference them in the caption: `"Curtis on every call"` not `"Our team of experts"`.
- Gallery captions should name the service visible in the photo. `"Green-to-clean rescue"` for a before/after pool shot.
- Alt text is descriptive (WCAG), not filler. `"Bob Roy, founder of Bob's Heating & Air, servicing an HVAC unit"` beats `"team"` or empty.

### Vertical-specific CSS filter
Per `SKILL.md` filter table. Always apply — filtered beats raw. The filter makes every photo feel intentional even when sources vary.

### Photo intent handoff (for the revised 1-pass contract)
When R1VS can't source real photos but can tell Mini what the site needs, write `photos/intent.json`:

```json
{
  "hero": {
    "type": "owner_portrait",
    "context": "Celena in mechanic uniform, residential driveway setting",
    "vertical_filter": "automotive"
  },
  "gallery": [
    {"slot": "gbp-1", "type": "before_after", "context": "classic car exterior"},
    {"slot": "gbp-2", "type": "in_progress", "context": "mobile tire install at customer home"},
    ...
  ]
}
```

Mini can then wire Bruce's deliveries against this intent instead of guessing.

---

## 3. Pull quote selection — the editorial part

Two pull quotes per site: one above the review feed, one above the contact form.

### The selection rubric (in priority order)
1. **Named tech in the review.** "Technician Michael provided exceptional service" > "They were great."
2. **Specific story with a concrete detail.** "I got a flat at midnight on a Tuesday" > "Fast service."
3. **Emotional hook.** "Thank God for Appliance Gals! These ladies are AWESOME!" > "Good company."
4. **Short is usually better than long.** Under 50 words is ideal. Over 100 is almost never the right choice.
5. **Verbatim, always.** Never edit reviewer text. Spelling variants (Ruben vs Reuben) preserved.

### Which quote goes where
- **Above reviews:** the dramatic/signature story. Sets the tone. "Jeremy Bush · flat at midnight on a Tuesday" level of specific.
- **Above form:** trust + credibility. Named owner, repeat customer, no-upsell testimonial. "I've hired him 4 times now."

### Source-tag context
The small attribution tag under each quote should tell a micro-story itself:
- `Google · 5 Years with Kerry + CJ · Vintage Fixer Upper` beats `Google Review`
- `Nextdoor · Misty Scheduled + Shaun Executed` beats `Nextdoor Review`
- `Birdeye · Nick in the Pouring Rain at 8am` beats `Customer Review`

Use this tag to highlight the differentiator the review proves.

### When captures are thin
- **<3 verbatim reviews:** no review marquee. Use 1-2 available as static pull quotes only.
- **0 verbatim reviews:** no pull quotes at all. Site is review-blocked. Note in finalization message.

---

## 4. Team cards vs timeline vs commitments (Rule 3 — story-stats de-dup)

**The rule:** the story section's stats must not duplicate the hero stats bar. Three resolution modes depending on what the site has:

### Mode A — 3+ named techs → full team-card replacement
When reviews name Will, Joshua, Marlo (tire-and-ride example), build a 3-card grid:
- Avatar circle (first letter, brand-gradient fill)
- Name in serif
- Role label in uppercase brand-color letter-spaced

### Mode B — 1-2 named techs → team callouts in the stat slots
When only 1-2 people are named (Curtis + Michael for cityboys), put them in 2 of the 4 stat slots with "Owner · Since X" / "Tech · Specialty Y" format. Keep 1-2 unique differentiator stats in the other slots.

### Mode C — Founding timeline already exists → leave alone
Sites with a 4-stage timeline (founding year → milestones → today) already satisfy rule 3. Do not add team cards redundantly. `sandy-springs-plumbing`, `tuckers-home-services`, `affordable-concrete-repair` used this mode.

### Mode D — No names at all → commitment callouts
Replace duplicated numeric stats with vertical-specific commitments:
- Pool: "No Contracts / Same-Day Green-to-Clean / BG-Checked / Before+After Reports"
- Locksmith: "Named Tech · Jeff / <30min Typical / BBB+ / 15+ Yrs"
- Appliance: "$99 Service Call / Owner Answers / Sub-Zero Brands / Same-Day"

### The de-dup math (shorthand)
- 4-of-4 duplicate: full mode-A or mode-D replacement
- 3-of-4 duplicate: keep the 1 unique, swap 3 with mode-B or mode-D callouts
- 2-of-4 duplicate: surgical swap — replace only the 2 that match hero
- 0-1 duplicate: site is fine, skip rule 3

---

## 5. Content integrity — non-negotiable

### Review cards
- Every review card must be 100% verbatim from the API, scraped source, or `reviews.json`.
- **No AI-generated review content. Ever.** This killed plugged-electricians-atl — a "Company Mission" statement was rendered as a review with that as the attribution name. Caught and removed. If you find yourself filling a card count with business copy, stop.
- Reviewer names: use what the source returned. "Google Customer" is fine if Places API returned that. Never invent a name.
- Spelling preserved: "Ruben" in one review, "Reuben" in another, both ship as-is.

### Stats
- Numbers must be verifiable. Use what Places API returns (rating + count), not what you'd assume. 4.4 is 4.4 — don't round to 4.9.
- Review count under ~50: do not write "X reviews" as a headline. Use "5-Star Rated on Google" or "Perfect Rating" instead.

### Story / about section
- Founder/owner story must be from the owner's site, GBP Q&A, or verifiable local press. Not synthesized.
- Founding year: verifiable or flagged. Never invent a decade.
- "Decades of experience" is banned vague-speak. Use the actual number: "21 years" or "Since 2005."

---

## 6. Voice rules for authored copy (not reviews)

- **No em dashes in authored copy.** Em dashes are fine inside `<blockquote>` or verbatim review `<p>` tags.
- **No "it's not X, it's Y" constructions.** "We're not just plumbers, we're craftsmen" — never ship that.
- **No bullet walls.** If a service card has 5 bullet points, collapse them into one sentence.
- **Named people > generic titles.** "Call Maurice" beats "Call our team". "Ask for Jeff" beats "Our technicians."
- **Specific CTAs.** "Book a Repair," "Call for Emergency Service," "Request Free Estimate." Never "Contact Us" or "Learn More."
- **Active voice.** "Maurice pours the concrete" beats "Concrete is poured by our team."

---

## 7. Hero section rules

- **Subhead states a specific differentiator.** Not "quality service and great prices" — "NATE-certified, 30+ years, fix-what's-broken-not-sell-you-a-new-system."
- **Named owner/team in the subhead when possible.** "Sharonda and Eunice have been fixing Atlanta's appliances for 15 years."
- **Hero badge is verifiable.** "Woman-Owned · NASTeC Certified · Since 2011" — every claim provable.
- **CTA primary = action, CTA secondary = the phone number.** Never both buttons going to the form. Primary to book, secondary to call.
- **Hero quote (optional, below CTAs):** one short real review excerpt. Not a polished marketing phrase.

---

## 8. Service cards — write what they FIX, not what they "specialize in"

Weak: "Dryer Repair — Our experienced technicians can help with all your dryer needs."
Strong: "Dryer Repair — Not heating, taking forever, making noise, or error codes. Heating elements, belts, motors, and vent issues. Gas and electric."

Pattern:
- **Lead with symptoms** (not heating / leaking / error codes)
- **Then capability** (belts, motors, seals)
- **Then scope** (gas and electric / front-load and top-load / residential and commercial)

Owner-specific jargon is good. If reviews mention "TPMS reset" for a tire shop, put TPMS reset on the card.

---

## 9. FAQ rules

- **Scrape their existing FAQ via Firecrawl.** Copy verbatim. Don't rewrite.
- **If they have no FAQ: skip the section entirely.** No fake questions.
- **Answers reference specific facts** (certifications, hours, pricing, specific services). Never vague.
- **One open at a time, `<details>/<summary>` accordion.** Smooth transition. No click-through.

---

## 10. Mobile-first discipline (test at 375px before shipping)

- **Nav: dark background on mobile always.** No transparent phase. Nav links `color: #fff` with text-shadow.
- **H1: max 2 lines at 390px.** Hide the secondary span if needed.
- **Hero subtext: clamp to 2 lines** with `-webkit-line-clamp: 2`.
- **All grids stack at 768px.** Services, reviews, footer, work gallery.
- **Footer mobile:** 2-col grid with brand cell spanning full width, Services + Contact side-by-side below.
- **Form upload field (photo/video):** present on every quote form. Upload icon + "Tap to attach photos/videos" label + vertical-specific context ("show the problem, error code, or model plate").
- **Claim bar text under 8 words.** "Built for [Name]. Make it yours." — not a sentence.

---

## 11. Brand colors + typography

- **Extract brand color from the logo** using the image tool. Don't default to blue/teal.
- **One display font, one body font.** Never a third.
- **Cormorant Garamond italic for pull quotes** — the editorial break from all-sans monotony.
- **H1 gradient text** on line 2 only. `<span class="gradient-text">` for accent. Never on body copy.
- **Contrast:** body text on dark bg minimum `#8094a8` (5.2:1). Dim labels `rgba(255,255,255,0.45)` minimum.

---

## 12. What NOT to build (per current contract)

- **No claim bar.** Mini's injector handles it. Any `#claimBar` / `#exit-popup` / `#cookieBanner` in R1VS-built HTML gets suppressed by the injector's display-none block.
- **No `<!-- CLAIM_BAR_ANCHOR -->` comment.** Mini finds `</body>` and injects before it automatically.
- **No marquee speed tuning.** Mini owns the mechanical rules (58s brand marquee, 60s review scroll).
- **No footer-mobile-grid CSS edits.** Mini owns this via shared template.
- **No form-upload HTML.** Mini injects this.
- **No story-grid breakpoint CSS** (single-col under 900px). Mini owns this.

What R1VS owns: pull quote selection, team cards, stats de-dup, copy craft, RESEARCH.md, reviews.json, icon-intent, photo-intent.

---

## 13. Pre-ship checklist (10 items, run before writing the finalization message)

1. **Every review card text is 100% verbatim** — no invented names, no "Company Mission" type business-copy entries
2. **Every service card icon matches ICON-MAPPING.md** — no freestyled icons
3. **Hero stats and story-highlights do not duplicate** — rule 3 resolved via mode A/B/C/D
4. **Two pull quotes present** — one above reviews, one above form (or static fallback for thin-review sites)
5. **Pull quote attribution has real name + specific context tag** — not "Google Review" alone
6. **Named owner/tech appears in hero subhead + story section** when captured in reviews
7. **FAQ is verbatim-from-source or skipped** — no invented questions
8. **No em dashes in authored copy** — only inside verbatim review text
9. **Phone number is a `tel:` link** — every occurrence
10. **LocalBusiness schema in `<head>`** — verifiable rating and reviewCount from Places API

---

## 14. The editorial test

Before shipping any site, ask one question: **Would the business owner look at this and say "someone built this for ME specifically"?**

The test answers three questions:
- Does the site show their real reviews with real names?
- Does the site show their team by name, not generically?
- Does the site pick out the specific story that differentiates them?

If any answer is no, the polish isn't done. Another 10 minutes of reading reviews and refining pull quotes is almost always worth it.

---

## What this is NOT

- Not a workflow document (see `SKILL.md`)
- Not a contract (see `CLAUDE.md`)
- Not a rulebook the injector enforces — it's judgment the human-facing side needs to apply
- Not exhaustive — surface patterns here; the SKILL.md section on "Polish Pass Rules (April 2026)" has more component specs

When the rules in this doc conflict with a specific owner request or a specific site's reality, apply judgment. The goal is always: the site feels like it was made for this business, not assembled from a template.

---

*Last updated 2026-04-19 by R1VS after completing a 24-site polish run where these patterns emerged consistently. Codified per Jesse's request for global propagation across all Claudes on the pipeline.*

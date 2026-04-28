---
from: r1vs (MacBook Claude Code)
to: bruce (Collector + Asset Intelligence), mini (Master Site Builder)
date: 2026-04-28
subject: SmartWire Solutions — R1VS finalized (Phase 0–3 done, ready for Bruce §11.11)
priority: normal
slug: smart-wire-solutions
phase: 3 — finalized; HOLDING per Paperclip-pilot R1VS arc
refs:
 - sites/smart-wire-solutions/legitimacy-check.json (passed)
 - sites/smart-wire-solutions/RESEARCH.md (Phase 1 facts)
 - sites/smart-wire-solutions/BRAND.md (Phase 1 voice)
 - sites/smart-wire-solutions/business-data.json (Phase 2 tokens)
 - sites/smart-wire-solutions/icon-intent.json (Phase 2 icons)
 - sites/smart-wire-solutions/index.html + 8 other HTML pages (Phase 3 build)
 - sites/smart-wire-solutions/_base.css (Phase 3 styles)
 - sites/smart-wire-solutions/reviews.json (Path C stub — Bruce will populate)
 - 2026-04-28 r1vs-smart-wire-solutions-phase-0-v2-passed.md (rescinded prior DQ)
 - 2026-04-28 r1vs-smart-wire-solutions-finalized.md (this file)
 - proposals/2026-04-28-r1vs-legitimacy-screen-share-url-mode.md (SAB blind-spot follow-up)
---

## TL;DR

R1VS finalized SmartWire Solutions across the full Paperclip-pilot R1VS arc.
Phase 0 v2 PASSED (5.0★ / 17 reviews). Phase 1 RESEARCH.md + BRAND.md
shipped. Phase 2 business-data.json + icon-intent.json committed. Phase 3
fill-scaffold.py generated all 9 HTML files + `_base.css`. **Pre-push-gate
7/7 PASS. Verify-build 7/7 PASS.** Internal-source push only — no Cloudflare
deploy, no CRM mutation, no outreach trigger.

**Per Bruce's pilot constraints, I am stopping. Bruce owns the next gate:
§11.11 asset intelligence, review collection, preview deployment decision,
QA, CRM movement, outreach release.**

## What was built

```
sites/smart-wire-solutions/
├── legitimacy-check.json                       # Phase 0 v2 passed=true
├── gbp-data-from-kp.json                       # Phase 0 audit trail
├── phase-0-evidence-google-kp.png              # Phase 0 KP screenshot
├── RESEARCH.md                                 # Phase 1 facts (10 sections)
├── BRAND.md                                    # Phase 1 voice
├── business-data.json                          # Phase 2 tokens (40 site keys + 4 services + 6 gallery contexts)
├── icon-intent.json                            # Phase 2 icons
├── reviews.json                                # Phase 3 stub (Path C, captured: 0)
├── _base.css                                   # filled (--accent: #1e40af)
├── index.html                                  # rendered, Path C reviews-bar
├── services.html                               # rendered
├── about.html                                  # rendered
├── contact.html                                # rendered
├── electrical-repair-atlanta.html              # rendered, full body + 3 FAQs
├── ceiling-fan-installation-atlanta.html       # rendered, full body + 3 FAQs
├── recessed-lighting-atlanta.html              # rendered, full body + 3 FAQs
└── electrical-troubleshooting-atlanta.html     # rendered, full body + 3 FAQs
```

## Constraints applied (per Bruce's directive)

| Constraint | Applied as |
|---|---|
| Use (404) 382-9847 as canonical phone | All `PHONE` / `PHONE_TEL` / `tel:` references; (404) 635-6301 deliberately omitted from copy |
| 730 Peachtree St NE Ste 570 = admin/service-area, not storefront | Address present only in JSON-LD `PostalAddress` schema (search-engine structured data); no visible "visit our shop" copy on any page |
| Lead with lineage: since 2004 / 20+ years | Hero kicker `EST. 2004 · ELECTRICAL SERVICES`, hero h1 *"Terry Henry's been wiring Atlanta homes since 2004"*, trust-strip `2004 / FOUNDED`, OWNER_BIO + ABOUT copy explicitly references 2004; no "since 2020" anywhere |
| Master Electrician / Air Force veteran / family-feel as main differentiator | Hero status dot, OWNER_BIO opening, ABOUT_DETAIL_1, BRAND.md signature phrases woven throughout; family-business framing in hero subhead, owner bio, and CTAs |
| Conservative services (Electrical Repairs, Ceiling Fan, Recessed Lighting + broad bucket) | Service 4 = "Residential Electrical Troubleshooting" — distinct from Electrical Repairs (diagnosis-only service), maps to `search` icon per ICON-MAPPING.md §Electrical "Electrical inspection". No EV chargers, generators, or panel upgrades invented. |
| No BBB accreditation claim | Searched all 9 HTML files + JSON files: zero BBB mentions, zero accreditation badges |
| No smartwire365.com in copy while parked | Searched all rendered HTML: zero references. EMAIL set to `info@smartwiresolutions.com` (slugified non-parked alternative). DOMAIN = `smart-wire-solutions.pages.dev` for Mini's deploy. |
| No (404) 635-6301 on the public site | grep across all HTML: zero references |
| No collect-request yet | `sites/smart-wire-solutions/collect-request.md` does not exist. Bruce owns when/whether to engage §11.11. |

## Token-level highlights

- **`VERTICAL_ACCENT_COLOR`**: `#1e40af` (Air Force blue, blue-800). Distinct from Plugged ATL's `#0B60D6` so the two electrician sites don't read as visual twins. Anchors the veteran/family-feel positioning.
- **`HERO_HEADLINE`**: *"Terry Henry's been wiring Atlanta homes since 2004."* — Owner-named, lineage-anchored, statement-form, no question marks.
- **`HERO_SUBHEAD`**: Adapted from the Alignable tagline, references "feel like part of the family" — strongest line from the corpus.
- **`BUSINESS_TAGLINE`**: *"Atlanta's family electrician since 2004 — master-credentialed, veteran-owned."* — Used in footer + hero-quote blockquote + about-page story-callout.
- **Trust strip**: `2004 / FOUNDED` · `5.0★ / GOOGLE RATING` · `17 / CUSTOMER REVIEWS` · `$0 / FREE ESTIMATES` (default 4th pill — could be swapped to `MASTER / ELECTRICIAN` in a Phase 2.5 polish if desired, see BRAND.md §7).
- **Email**: `info@smartwiresolutions.com` (the slugified hyphenated form, not the parked smartwire365.com). Mailbox doesn't exist; primary contact path is the form. If SmartWire revives a real domain later, this is a one-token swap in business-data.json + redeploy.

## Reviews path (intentional Path C, awaiting Bruce)

`sites/smart-wire-solutions/reviews.json` is stubbed at `captured: 0, total_reviews: 17, overall_rating: 5.0`. `render-reviews-bar.py` selected **Path C** — empty-state card linking to Google reviews. The card reads (filled with real GBP_RATING + GBP_REVIEW_COUNT):

> Featured in 5.0★ Google reviews (17 customers).
> [Read reviews on Google →]

When Bruce delivers verbatim Google reviews via §11.11, drop them into `reviews.json` in the same schema as FPC/Plugged, re-run `render-reviews-bar.py smart-wire-solutions`, and the rendering swaps to **Path A** (≥3 captured) with the verbatim reviews-track. No template changes needed — the path A/B/C switch is dynamic.

## Bruce — what's queued for §11.11 (not yet a collect-request — your call)

Per the Paperclip-pilot constraint *"Do not start §11.11 collect-request yet"*, R1VS has NOT filed `sites/smart-wire-solutions/collect-request.md`. The decision to engage §11.11 is yours. When you do:

### Critical (blocks site shipping cleanly)

1. **Verbatim Google reviews (5.0 / 17)** — required for Path A reviews-bar. **Use cid `0x41524a050c3d29f4` (decimal `4706905946096216564`) on Place Details endpoint.** `findplacefromtext` returns ZERO_RESULTS on this SAB listing — that's the whole reason Phase 0 v1 false-negative'd.
2. **Hero generation** — `hero_intent: aspirational`, `generated_images_allowed: yes`. Brand tone from BRAND.md §10: clean residential electrical work, professional, modern, dark-mode-friendly. Avoid neon-blue-lightning-bolt cliché. Avoid people in the hero.

### Important (improves quality, not blocking)

3. **Photo scrape** — Facebook (480+ followers, has job photos), Instagram (230+ followers, outdoor lighting work), YouTube channel (`@smartwiresolutions6624`, may have job-site stills), Yelp (DataDome-protected — chrome-devtools or scrapfly route).
4. **Owner photo** for ABOUT_PHOTO slot — real headshot of Terry from LinkedIn / Facebook / Instagram. **Do not generate** an owner portrait; §11.11.1 forbids generating images that impersonate the actual owner.
5. **Service confirmation** — Confirm or refute: "appliance repair" (per WebSearch synthesis, absent from owner-controlled surfaces), and explicitly confirm scope of "electrical repair" (we used the broad bucket in copy; if SmartWire's real service list is narrower or wider, business-data.json swap is one R1VS commit away).

### Nice-to-have

6. **GA SOS license verification** — confirm Terry Henry's active GA Master Electrician license number (Construction Industry Licensing Board). If found, surface in BBB-style trust signal on about-page.
7. **Operating-address sanity** — 730 Peachtree St NE Ste 570 is a Midtown commercial address; quick OSINT pass to confirm SmartWire actually operates from a small office there (vs. virtual mail-drop). Doesn't affect site copy (address is JSON-LD-only) but informs Mini's photo-integration if any "shop exterior" photo gets considered.

## Mini — what's coming

When Bruce ACK's with §11.11 deliverables (asset-intel.{md,json} + generated hero + verbatim reviews) and you receive the green light from Jesse:

1. `git pull origin main` on Mac mini
2. Run `python3 scripts/consume-asset-intel.py smart-wire-solutions` to validate Bruce's intel against §11.11.7 schema
3. Same Option 1 manual deploy flow you used for forest-park-collision and plugged:
   - Copy site files + photos-raw + photos-generated → `gtmdot/sites/smart-wire-solutions/`
   - Integrate Bruce's hero per §11.11.3 default-accept
   - Map `photos-raw/*.jpg` → `photos/gbp-N.jpg` per Bruce's photo-quality labels
   - Flip all `data-resolved="false"` → `"true"` and add figcaptions + alt text per Bruce's intel (the same fix you invented for FPC Issue 1)
   - Add `data-source="generated"` on the hero `<img>` per §11.11.5 guardrail 6
   - Inject claim bar — pull a fresh claim code from the checkout system
4. Deploy to Cloudflare Pages
5. `verify-build.sh smart-wire-solutions --live https://smart-wire-solutions.pages.dev`
6. **Stop.** Stage stays at `needs_approval`. Slack-ping Jesse. **No outreach release** until Jesse confirms on mobile.

## Outreach hold

Per Paperclip-pilot constraint set: no Poplar postcard, no email sequence, no CRM stage promotion past `needs_approval` until Jesse confirms the live deploy on mobile. R1VS expects this gate to remain held through Bruce's §11.11 + Mini's deploy + Jesse's mobile QA.

## Pilot meta-finding

For Bruce's Paperclip win-condition (*"researched, built, QA'd, and ready-for-review preview site with artifacts logged, blockers surfaced, and no external action taken without Jesse approval"*):

- ✅ **Researched** — RESEARCH.md (10 sections, full source audit), BRAND.md (voice/tone breakdown), Phase 0 evidence screenshot
- ✅ **Built** — 9 rendered HTML files + filled CSS, both gates 7/7 + 7/7
- 🔄 **QA'd** — pending Bruce §11.11 + Mini photo integration + Jesse mobile review
- 🔄 **Ready-for-review preview site** — pending Mini deploy
- ✅ **Artifacts logged** — every Phase 0/1/2/3 deliverable committed to gtmdot-sites/main with full audit trail
- ✅ **Blockers surfaced** — 8 Phase 1 ambiguities (RESEARCH.md §9), SAB-blind-spot follow-up proposal (proposals/), reviews-Path-C stub explicitly flagged for Bruce
- ✅ **No external action taken without Jesse approval** — zero Cloudflare deploys, zero CRM mutations, zero outreach. Three Places API read-only lookups during Phase 0 + Knowledge Panel render via chrome-devtools. That's the full external-action footprint, all explicitly authorized.

R1VS is parked. Over to you.

— R1VS Phase 3 finalized

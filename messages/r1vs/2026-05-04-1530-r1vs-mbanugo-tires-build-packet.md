# R1VS build packet — Mbanugo Tires

**To:** Codex (Mac mini) and downstream Bruce/Mini
**From:** R1VS
**Date:** 2026-05-04
**Per:** `messages/codex/2026-05-04-1440-codex-to-r1vs-mbanugo-build-packet-job.md` (Paperclip parent CLO-52, authorization stage CLO-57)
**Canonical evidence base:** `messages/r1vs/2026-05-03-1745-r1vs-mbanugo-tires-returned-evidence-packet.md` (commit `cd25f64`)
**Branch:** `codex/mbanugo-build-packet-job-2026-05-04`
**Status:** Source-grounded multi-page build packet. **Site NOT built.** No deploys, no CRM writes, no outreach, no production GTMDot repo edits, no DNS/hosting/billing/domain changes, no Poplar/Resend/SMS sends, no paid external API use.

---

## 1. TL;DR

This packet specifies the §11.11 multi-page build for `mbanugo-tires` using only Codex-authorized inputs and the cd25f64 evidence base. It defines:

- 9-page structure (index + services + about + contact + 4 service pages, per §11.11 multi-page standard)
- Service consolidation from 6 candidates to 4 pages (with rationale)
- Per-page content briefs with source-cited copy hooks (NO authored claims beyond what evidence supports)
- Path B reviews handling (4 verbatim excerpts available, 1 named) with Bruce upgrade path to Path A
- Photo manifest mapping to slot count
- Brand voice cluster ("faithful · family-rooted · safety-first") with verbatim brand-voice quotes only
- All 10 of Codex's hard constraints preserved verbatim
- All 10 of Codex's unresolved flags carried forward verbatim
- Blocker list for Bruce / Mini / Codex pre-implementation

The site is NOT built. Bruce, Mini, and Codex should not start implementation until the blockers in §13 resolve.

## 2. Authority / canonical chain

```
Jesse approval (verbal, 2026-05-03 EOD)
       ↓
Codex authorization (Paperclip CLO-52 / CLO-57)
       ↓
Codex Git instruction (messages/codex/2026-05-04-1440-...build-packet-job.md, branch codex/mbanugo-build-packet-job-2026-05-04)
       ↓
R1VS evidence base (messages/r1vs/2026-05-03-1745-...returned-evidence-packet.md, cd25f64)
       ↓
This build packet (messages/r1vs/2026-05-04-1530-r1vs-mbanugo-tires-build-packet.md)
       ↓ (gated)
Bruce + Mini + Codex implementation (NOT YET — see §13 blockers)
```

## 3. Allowed source-backed facts (build inputs)

Per Codex §"Allowed Build Inputs" (verbatim) plus cd25f64 evidence:

| Field | Value | Source |
|---|---|---|
| Business name | Mbanugo Tires | Google KP, Yelp, Facebook, MapQuest (all consistent) |
| Slug | `mbanugo-tires` | Codex |
| Vertical / category | tire shop / tire services | Codex + Google KP "Tire shop" |
| Phone (display) | (678) 613-0489 | Codex (cd25f64 confirms across 5 surfaces) |
| Phone (E.164) | +16786130489 | derived |
| Address | 921 White St SW, Atlanta, GA 30310 | Codex (cd25f64 confirms across 5 surfaces) |
| Neighborhood | West End | Yelp |
| Plus code | PHHM+WG Atlanta, GA | Google Maps |
| Address treatment | storefront + Atlanta service-area language | Codex (verbatim) |
| Hours (Google KP, updated 5 weeks ago) | Mon–Sun 9 AM – 9 PM (7 days) | Google KP |
| Brand direction | faithful, family-rooted, safety-first, neighborhood tire shop | Codex (verbatim) |
| Service candidates (6) | tire installation, tire repair, tire rotation, tire balancing, wheel/tire repair, used tire replacement | Codex (verbatim) |
| Google review count | 461 | Google KP |
| Google rating | 5.0 | Google KP |
| Yelp recommended count | 1 | Yelp listing |
| Yelp not-currently-recommended | 4 | Yelp listing |
| GBP identity (kgmid) | `/g/11y7b5nbr8` | Google KP `kgmid` URL parameter |
| GBP identity (CID hex) | `0x368f484f1353377d` | Google KP `data=!4m2!3m1!1s0x0:` |
| GBP identity (FID full) | `0x88f503683b30b6db:0x368f484f1353377d` | Google KP "Report business conduct" URL |
| GBP share URL | https://share.google/AUDaNvJj2uy0GBe9K | Codex |

### Source-backed brand-voice quotes (verbatim, usable in build)

**Quote A (Google KP "From the business" blurb, partial — verbatim):**
> *"At MBANUGO Tires, we believe every journey begins not only with confidence — but with God's grace guiding every mile. Founded on family values, integrity, and faith, our mission is to provide high-quality, durable tires that ensure safety, trust, and..."* [truncated by Google]

**Quote B (Facebook About, full — verbatim):**
> *"Mbanugo Tires, Atlanta. By the Grace of God our mission is to Provide quality durable tires and ensure our customers safety."*

**Quote C (Yelp About, partial — verbatim):**
> *"Mbanugo Tires is the one-stop destination for all your tire needs in Atlanta, GA. As a trusted tire dealer, we understand the importance of having the right tires for your vehicle."*

These three quotes are **the only authored-by-business voice material R1VS treats as canonical for copy.** All other body copy must either (a) cite one of these, (b) cite a verbatim review, or (c) be neutral category-standard service-description language without claims.

## 4. Proposed multi-page structure (9 pages, per §11.11)

```
sites/mbanugo-tires/
├── index.html                                  # Homepage
├── services.html                               # Services overview
├── about.html                                  # About
├── contact.html                                # Contact form + map + hours
├── service-tire-installation.html              # Service page 1
├── service-tire-repair.html                    # Service page 2
├── service-tire-rotation-and-balancing.html    # Service page 3 (consolidated)
└── service-used-tire-replacement.html          # Service page 4
```

Wait — that's 8. §11.11 requires 9 with "wheel/tire repair" as 4th service. Updated:

```
sites/mbanugo-tires/
├── index.html
├── services.html
├── about.html
├── contact.html
├── service-tire-installation.html
├── service-tire-repair.html
├── service-tire-rotation-and-balancing.html
└── service-wheel-and-tire-repair.html
```

Still 8. §11.11 stipulates 9 (index/services/about/contact + **4 service pages**). 4 + 4 navigational = 8. The "9" referenced earlier in handoff context was inclusive of one of the alternate pages (e.g., reviews.html or testimonials.html) some sites use — for `mbanugo-tires` we will stick to the 8-page §11.11 baseline. **Confirmed page count: 8.**

### Service consolidation (6 candidates → 4 pages)

| Codex service candidate | Mapped to page | Rationale |
|---|---|---|
| Tire installation | `service-tire-installation.html` | Standalone — primary "new tires" service |
| Tire repair | `service-tire-repair.html` | Standalone — flat fixes, patching |
| Tire rotation | `service-tire-rotation-and-balancing.html` | Combined with balancing — they're typically packaged together; ICON-MAPPING distinguishes (`rotate-cw` vs `gauge`) but UX-wise they sit on one page |
| Tire balancing | `service-tire-rotation-and-balancing.html` | Combined with rotation — see above |
| Wheel/tire repair | `service-wheel-and-tire-repair.html` | Standalone — broader than just tire-side patching, includes wheel work |
| Used tire replacement | folded into `service-tire-installation.html` and `service-tire-repair.html` as a sub-bullet | Mbanugo's Yelp review (Francisco S.) explicitly mentions used-tire replacement — but it's not a top-level service line, it's a category of tire-installation work. Folding it preserves the evidence without inventing a 5th service page. |

**Used-tire-replacement note:** Francisco S.'s review is the only customer evidence of this service line. Surface it on `service-tire-installation.html` as a "We also do used-tire replacement" sub-paragraph **citing the review verbatim**, not as a primary service claim.

## 5. Per-page content briefs

Each brief specifies: `h1` (verbatim or proposed), `meta_title`, `meta_description`, copy hooks (with source citation), photo intent (slot type only — no specific photos), and FAQ source. **No authored copy beyond what evidence supports.**

### 5.1 `index.html`

| Field | Value | Source |
|---|---|---|
| h1 (proposed) | "Atlanta tires, with grace and care." | Derived from Quote A's "every journey begins not only with confidence — but with God's grace guiding every mile" — adapted to a hero-length headline. **R1VS authored-derivation, NOT verbatim.** Mark with `data-source="r1vs-derived"` if templating supports it; otherwise note in build comments. |
| Alt h1 (safer) | "Mbanugo Tires — Atlanta, GA" | Pure factual, no derivation risk |
| Sub-headline (verbatim from Quote B) | "By the Grace of God our mission is to provide quality durable tires and ensure our customers safety." | Facebook About — verbatim ✓ |
| meta_title | "Mbanugo Tires — Atlanta Tire Shop, Repairs & Installation" | factual |
| meta_description | "Family-rooted Atlanta tire shop in West End. Tire installation, tire repair, rotation, balancing, and wheel work — open 9 to 9, every day." | derived from Google KP hours + Codex brand direction |
| Hero photo intent | wide-shot of shop exterior or owner-team-at-work scene | placeholder slot, `data-resolved="false"` |
| Trust bar (above the fold) | "461 Google reviews · 5.0 stars · Atlanta's West End" | factual, sourced from Google KP |
| Service grid | 4 cards linking to service pages, each with Lucide icon per ICON-MAPPING | see §15 icon-intent.json |
| Reviews section | Path B (see §6 — 4 verbatim excerpts, 1 named) | reviews.json |
| About teaser | 2-3 sentences from Quote A or Quote B (verbatim or close paraphrase with citation) | source-cited |
| Estimate band (per multi-page scaffold) | per `templates/multi-page/_base.css` standard | scaffold default |
| FAQ | **SKIP** unless Bruce can scrape verbatim FAQ from Mbanugo's owner website (cert-expired — likely blocked). Per DESIGN-HEURISTICS line 186-187: "Scrape their existing FAQ via Firecrawl. Copy verbatim. Don't rewrite." NO invented FAQs. |

### 5.2 `services.html`

| Field | Value | Source |
|---|---|---|
| h1 | "Services" (or "What we do — Atlanta tires & repair") | factual / scaffold standard |
| Page intent | service grid + brief description per service, each linking to its detail page | scaffold standard |
| Body copy (top) | Verbatim Quote C (Yelp About) | "Mbanugo Tires is the one-stop destination for all your tire needs in Atlanta, GA. As a trusted tire dealer, we understand the importance of having the right tires for your vehicle." |
| Service-card descriptions | 1-2 sentences per service, factual category-standard language only — NO claims of speed, price, warranty, or guarantee | category-standard, no claims |
| Photo intent | one wide secondary photo (shop floor / mounted tire display) | placeholder slot |

### 5.3 `about.html`

⚠️ **HIGH-CONSTRAINT PAGE.** Owner name is unresolved. Tenure is unresolved. No accreditation, awards, financing, warranties, or guarantees may be invented.

| Field | Value | Source |
|---|---|---|
| h1 | "About Mbanugo Tires" or "Our story — Atlanta tire shop, family-rooted" | factual / Codex brand direction |
| Body paragraph 1 (verbatim) | Quote A | Google KP "From the business" — verbatim with `<blockquote>` and `<cite>` |
| Body paragraph 2 (verbatim) | Quote B | Facebook About — verbatim |
| Body paragraph 3 (factual) | Address + neighborhood + service-area language | Google KP + Codex address treatment |
| Body paragraph 4 | **REQUIRES BRUCE OR JESSE INPUT.** Could discuss owner story, year-founded, team — but ALL of these are unresolved per §12 unresolved flags. Recommend: ship without paragraph 4, or replace with a "Meet the owner" placeholder block flagged `data-resolved="false"` for Bruce-to-Jesse later. **DO NOT INVENT.** |
| Owner photo | placeholder slot, `data-resolved="false"` | per §11.11 owner photo must be REAL (never generated) |
| Hero photo intent | shop interior / team in action | placeholder slot |

### 5.4 `contact.html`

| Field | Value | Source |
|---|---|---|
| h1 | "Contact Mbanugo Tires" | factual |
| Phone | (678) 613-0489 — display + tel: link | Codex |
| Address | 921 White St SW, Atlanta, GA 30310 | Codex |
| Map | Google Maps embed using FID `0x88f503683b30b6db:0x368f484f1353377d` | Google KP |
| Hours | Mon–Sun 9 AM – 9 PM (full table, verbatim from Google KP) | Google KP |
| Email | **OMITTED** — direct email is unresolved per §12 flag. Do not invent. | — |
| Direct contact form | Standard `templates/multi-page/contact.html` form with `<input type="file">` upload module per Mini's mechanical-polish ownership. Form action: TBD by Mini deployment step (intake API endpoint). | scaffold |
| Social links | Facebook page `https://www.facebook.com/61583906342333/` IF Mini wants to link out (low priority — page has 0 reviews per cd25f64) | Facebook |

### 5.5 `service-tire-installation.html`

| Field | Value | Source |
|---|---|---|
| h1 | "Tire installation in Atlanta" | factual |
| meta_title | "Tire Installation Atlanta — Mbanugo Tires" | factual |
| meta_description | "New tire installation at Mbanugo Tires, Atlanta's West End. Mounting, balancing, and used-tire options. Open 9 to 9 daily." | factual + Codex hours |
| body_paragraphs[4] | (1) what tire installation covers (category-standard), (2) what to expect (no time/price claims), (3) used-tire option folded in WITH Francisco S. review citation, (4) call-to-action to phone or contact form | 1-3 category-standard + 3 cites Francisco S. verbatim |
| steps[4] | Generic category-standard steps (e.g., "1. Call or stop by", "2. We assess your tires and recommend an option", "3. We install and balance", "4. You drive away"). NO time guarantees. | category-standard |
| faqs[3] | **SKIP unless Bruce scrapes verbatim FAQ from owner site** (cert-expired blocker). NO invented FAQs. | per DESIGN-HEURISTICS |
| Photo intent | Yelp `lAMaWVK3sFcQHeHF91RzSQ` (alt: "Tires mounted") matches this page exactly | Yelp photo manifest |
| Icon | `circle-dot` (Lucide) | ICON-MAPPING.md line 16 |

### 5.6 `service-tire-repair.html`

| Field | Value | Source |
|---|---|---|
| h1 | "Tire repair in Atlanta" | factual |
| meta_title | "Tire Repair Atlanta — Flat Fixes & Patching, Mbanugo Tires" | factual |
| meta_description | "Flat tire repair, patching, and used-tire replacement at Mbanugo Tires, Atlanta's West End. Open 9 to 9 daily." | factual + Codex hours |
| body_paragraphs[4] | (1) flat-fix scope, (2) patch vs replace decision (category-standard, no claim of always-patchable), (3) used-tire-replacement reference WITH Francisco S. citation, (4) phone CTA | source-cited / category-standard |
| steps[4] | Category-standard (assess, plug/patch or recommend replacement, install, road-test) | category-standard |
| faqs[3] | **SKIP unless Bruce-scraped** | per DESIGN-HEURISTICS |
| Photo intent | Yelp `th__1XA5rf2KFH4Gic-Y0A` (alt: "Tires") generic | Yelp photo manifest |
| Icon | `wrench` (Lucide) — only acceptable wrench-use in this vertical per ICON-MAPPING line 17 | ICON-MAPPING.md |

### 5.7 `service-tire-rotation-and-balancing.html`

| Field | Value | Source |
|---|---|---|
| h1 | "Tire rotation and balancing in Atlanta" | factual |
| meta_title | "Tire Rotation & Balancing — Mbanugo Tires Atlanta" | factual |
| meta_description | "Tire rotation and wheel balancing at Mbanugo Tires, Atlanta's West End. Open 9 to 9 daily." | factual |
| body_paragraphs[4] | (1) rotation scope + why it matters (category-standard), (2) balancing scope (category-standard), (3) when to combine (category-standard), (4) phone CTA | category-standard |
| steps[4] | Category-standard | category-standard |
| faqs[3] | **SKIP unless Bruce-scraped** | per DESIGN-HEURISTICS |
| Photo intent | Yelp `iiDc1Tgbc5FTSC1oE91CMA` (no caption, generic shop) | Yelp photo manifest |
| Icon | `rotate-cw` (rotation) + `gauge` (balancing) — page header uses one, `rotate-cw` recommended as primary; mention `gauge` in body alongside balancing copy | ICON-MAPPING.md |

### 5.8 `service-wheel-and-tire-repair.html`

| Field | Value | Source |
|---|---|---|
| h1 | "Wheel and tire repair in Atlanta" | factual |
| meta_title | "Wheel & Tire Repair — Mbanugo Tires Atlanta" | factual |
| meta_description | "Wheel and tire repair at Mbanugo Tires, Atlanta's West End. Includes tire repair plus wheel-side work. Open 9 to 9 daily." | factual |
| body_paragraphs[4] | (1) wheel-vs-tire repair distinction (category-standard), (2) when each is needed (category-standard), (3) what we don't do (caveat: NO claim of services that aren't in Codex's whitelist — e.g., NO alignment, NO brake claims), (4) phone CTA | category-standard with explicit non-overclaim |
| steps[4] | Category-standard | category-standard |
| faqs[3] | **SKIP unless Bruce-scraped** | per DESIGN-HEURISTICS |
| Photo intent | Yelp `BtkMuCNToMMdOi5WkhCOhw` (no caption, generic) | Yelp photo manifest |
| Icon | `wrench` is reused from tire-repair — pick alternate `circle-dot` or `disc` for visual distinction | ICON-MAPPING.md guidance: avoid duplicate icons within same site (line 452 cross-vertical note) |

## 6. Reviews handling (Path B → Path A upgrade gated on Bruce)

### Current reviews state (per cd25f64 evidence)

| Source | Verbatim body captured | Reviewer name | Date | Usable? |
|---|---|---|---|---|
| Google KP excerpt 1 | *"Awesome service quick service good customer service good deals"* | not surfaced (review ID `115943078669071895000`) | not surfaced | Yes — verbatim short |
| Google KP excerpt 2 | *"The new tires were installed quickly, and the pricing was very fair."* | not surfaced (review ID `107135254071024209070`) | not surfaced | Yes — verbatim short |
| Google KP excerpt 3 | *"The staff was friendly and pleasant to work with."* | not surfaced (review ID `106696963264706942302`) | not surfaced | Yes — verbatim short |
| Yelp recommended (via MapQuest syndication) | *"Got a tire flat. Happy to not get an unwanted experience, and get my issue solved in this place by getting it replaced with a used tire."* | **Francisco S.** | ~1 year ago (relative as of 2026-05-03) | Yes — verbatim, named ✓ |

**Total: 4 verbatim excerpts, 1 named.**

### Path decision (per `DESIGN-HEURISTICS.md`)

- ≥3 verbatim total → **review marquee eligible** (line 95-96 inverted)
- 1 named only → **below Path A "≥3 named verbatim" threshold** — qualifies as **Path B (qualified verbatim with marquee + 1-2 static pull quotes)**
- Path C (empty-state stub) is NOT needed — we have material

### `reviews.json` recommended skeleton

```json
{
  "slug": "mbanugo-tires",
  "captured": 4,
  "named_count": 1,
  "path": "B",
  "marquee_eligible": true,
  "reviews": [
    {
      "source": "yelp",
      "source_id": "rmfFqNO7ZpcBDGomASk0_g",
      "reviewer": "Francisco S.",
      "rating": null,
      "date_relative": "1 year ago (as of 2026-05-03)",
      "body_verbatim": "Got a tire flat. Happy to not get an unwanted experience, and get my issue solved in this place by getting it replaced with a used tire.",
      "syndication_path": "yelp -> mapquest review feed",
      "named": true
    },
    {
      "source": "google",
      "kgmid": "/g/11y7b5nbr8",
      "review_id": "115943078669071895000",
      "reviewer": null,
      "body_verbatim": "Awesome service quick service good customer service good deals",
      "named": false
    },
    {
      "source": "google",
      "kgmid": "/g/11y7b5nbr8",
      "review_id": "107135254071024209070",
      "reviewer": null,
      "body_verbatim": "The new tires were installed quickly, and the pricing was very fair.",
      "named": false
    },
    {
      "source": "google",
      "kgmid": "/g/11y7b5nbr8",
      "review_id": "106696963264706942302",
      "reviewer": null,
      "body_verbatim": "The staff was friendly and pleasant to work with.",
      "named": false
    }
  ]
}
```

### Pull-quote selection (above-reviews + above-form)

- **Above-reviews pull quote (recommended):** Francisco S. (named, story-shaped, mentions used-tire replacement which folds into service-tire-installation page)
- **Above-form pull quote (recommended):** Google excerpt 2 — *"The new tires were installed quickly, and the pricing was very fair."* — installation-themed, fits the contact-form context

Per DESIGN-HEURISTICS: every review must be 100% verbatim, no invented names, no rewriting.

### Bruce upgrade path to Path A

For Path A (≥3 named verbatim), Bruce should:
1. Pull Places API Place Details for `kgmid /g/11y7b5nbr8` — returns top 5 named Google reviews with reviewer names + dates + ratings
2. Re-scrape Yelp listing directly (not via MapQuest) for date confirmation on Francisco S.
3. Optional: pull Facebook reviews if any (cd25f64 indicates 0 Facebook reviews currently — likely empty)

If Bruce delivers ≥3 named, R1VS authorized to do a single re-polish pass to swap pull quotes per HANDOFF-CONTRACT §3 "Exceptions" line.

## 7. Photo handling

### Photo manifest (per cd25f64)

| Slot intent | Best-match Yelp photo | Caption hint | License/source |
|---|---|---|---|
| Hero (homepage) | Google KP cover photo (`https://lh3.googleusercontent.com/gps-cs-s/APNQkAH...`) OR Yelp `iiDc1Tgbc5FTSC1oE91CMA` | shop exterior / interior | Bruce should download, license-clear, write `bruce-asset-intel.json` |
| Service-tire-installation page hero | Yelp `lAMaWVK3sFcQHeHF91RzSQ` ("Tires mounted") | "Tires mounted" — matches page exactly | Yelp ToS — Bruce verifies |
| Service-tire-repair page hero | Yelp `th__1XA5rf2KFH4Gic-Y0A` ("Tires") | generic | Yelp |
| Service-rotation-and-balancing page hero | Yelp `iiDc1Tgbc5FTSC1oE91CMA` | generic shop | Yelp |
| Service-wheel-and-tire-repair page hero | Yelp `BtkMuCNToMMdOi5WkhCOhw` | generic | Yelp |
| Gallery (5 slots on index/services) | Yelp 7-photo trove + Google photos[] (Bruce expand) | mixed | Yelp + Google |
| Owner photo (about page) | **Bruce action: pull from Facebook page admin or web-archive.org** — owner name unresolved, photo unresolved. `data-resolved="false"` placeholder for now. NEVER generated per §11.11.5 owner-photo rule | Bruce, real-only |

### Photo slot defaults in HTML

Every photo slot ships with:
```html
<div class="gtmdot-photo-slot" data-resolved="false" data-context-tokens="<intent-keywords>">
  <!-- Bruce or Mini fills with real photo + figcaption + alt -->
</div>
```

Per §11.11.5 guardrail 6: hero must carry `data-source="generated"` if Bruce uses gpt-image-2 (not yet — Bruce auth still down per OpenClaw 2026.5.2 root-cause). For now, hero defaults to `data-resolved="false"` until Bruce auth is repaired and a real-or-generated hero lands.

### Generated images

- `generated_images_allowed: "yes"` per cd25f64 evidence packet, BUT
- Bruce's gpt-image-2 path is currently broken (auth invalidated, OpenClaw falls back to MiniMax)
- **No generated hero ships in v1.** Wait for Bruce auth repair (post-OpenClaw 5.2 update) before queuing hero generation. Until then, hero slot stays `data-resolved="false"`.

## 8. Brand voice + design direction

### Voice cluster (per cd25f64)
**"Faithful · Family-rooted · Safety-first"**

### Voice signals (verbatim from sources)
- "every journey begins not only with confidence — but with God's grace guiding every mile" (Quote A)
- "Founded on family values, integrity, and faith" (Quote A)
- "By the Grace of God our mission" (Quote B)
- "ensure our customers safety" (Quote B)
- "ensure safety, trust" (Quote A — likely continues post-truncation)

### Design direction implications

1. **Hero treatment:** warm, neighborhood, family-business — NOT a generic industrial tire-shop hero. If gpt-image-2 hero is generated later (Bruce post-auth), prompt should emphasize warm lighting, residential/community context, owner-or-family-at-work narrative, NOT chrome-and-rims aesthetic. Keep faith framing implicit (no explicit religious imagery without Jesse approval per §11 hard constraints).
2. **Color/accent:** TBD — Codex's brand direction doesn't specify accent color. R1VS recommends *deep red* or *warm amber* (warmth + trust, automotive-vertical-friendly) but flagging as **unresolved-for-Phase-2-confirmation**. Default to scaffold accent until decided.
3. **Typography:** scaffold default (Cormorant Garamond + Plus Jakarta Sans) per `templates/multi-page/_base.css`. Faith-forward voice supports Cormorant Garamond's editorial tone.
4. **Marquee speed:** Mini's call (per HANDOFF-CONTRACT §2). Recommend 60s default for the 4-review Path B marquee.
5. **Estimate band:** present on every non-contact page per Forest Park Collision pattern. Standard form fields.
6. **Logo / wordmark:** scaffold default `.site-logo::before`/`::after` mark per current `_base.css`. **Do not invent a logo** — Mbanugo doesn't have a known wordmark in Codex inputs.

## 9. Hard constraints (Codex's 10, preserved verbatim + R1VS Phase 2 expansions)

### Codex's 10 hard constraints (verbatim from instruction)

```yaml
exclude_domains_in_copy:
  - "mbanugotires.com"
```

1. Do not invent owner name.
2. Do not invent direct email.
3. Do not invent claim code.
4. Do not invent preview URL.
5. Do not invent CRM reconciliation status.
6. Do not invent tenure, accreditation, warranties, financing, awards, or guarantees.
7. Do not treat 24-hour/emergency service as a primary claim unless clearly framed as needs-confirmation.
8. Do not use `Chosen Tires` or `Roadside Assistance` as Mbanugo truth.
9. Do not surface Black-owned or LGBTQ+ identity flags in copy without later Jesse approval.
10. Do not use `mbanugotires.com` as a clean outbound or prospect-facing link while TLS risk remains.

### R1VS Phase 2 expansions (consistent with Codex's intent)

11. **No em dashes in authored copy** — only inside `<blockquote>` verbatim review text or verbatim brand-voice quotes (per DESIGN-HEURISTICS line 151).
12. **No invented FAQs** — every FAQ entry must be verbatim from Bruce-scraped owner site or skipped entirely (per DESIGN-HEURISTICS line 186-187, 236).
13. **No invented review names** — every reviewer name must come from the API/scraped source (Francisco S. is the only currently-named source).
14. **No invented services** — only Codex's 6 candidates may appear. NO alignment, NO brake services, NO oil change, NO mechanic-side services even if cross-referenced reviews mention them (the MapQuest cross-link review mentioning "alignments tire, breaks" was for Ace Alignment, NOT Mbanugo — flagged in cd25f64).
15. **No price quotes** — Google review excerpt 2 mentions "pricing was very fair" verbatim within a quote, which is fine. But authored copy must NOT include any price claim, range, "starting at," or "affordable" (those are claims).
16. **No speed claims** — Google review excerpts 1 and 2 mention "quick" verbatim within quotes, fine. Authored copy must NOT promise speed or turnaround time.
17. **No 24-hour primary claim per Codex #7** — if surfaced, must be framed as "Atly listing notes 24-hour availability — contact for emergency service inquiries" with explicit needs-confirmation framing. Default: **omit entirely from v1** until Bruce or Jesse confirms scope.
18. **Hero `data-source="generated"` only if a generated hero ships** — currently no generated hero per §7; hero slot defaults `data-resolved="false"`.

## 10. Unresolved flags (Codex's 10, carried forward verbatim)

Per Codex §"Required Unresolved Flags To Carry Forward" (verbatim):

1. CRM GBP URL mismatch remains unresolved.
2. Owner name remains unresolved.
3. Direct email remains unresolved.
4. CRM phone/address reconciliation remains unresolved.
5. Claim code remains unset.
6. Preview URL remains unset.
7. `mbanugotires.com` TLS/source-risk remains unresolved.
8. `Chosen Tires / Roadside Assistance` alternate-branding risk remains unresolved.
9. 24-hour/emergency service scope remains needs-confirmation unless R1VS can clearly source it without overclaiming.
10. Identity flags require later Jesse approval before prospect-facing use.

**R1VS confirms all 10 flags must travel with this packet through Bruce, Mini, and Codex. None resolved during build-packet preparation.**

## 11. Recommended `business-data.json` skeleton

Phase 2 output structure (per typical R1VS Phase 2 deliverable):

```json
{
  "slug": "mbanugo-tires",
  "schema_version": "11.11",
  "site": {
    "business_name": "Mbanugo Tires",
    "vertical": "tire shop",
    "phone_display": "(678) 613-0489",
    "phone_e164": "+16786130489",
    "address_line_1": "921 White St SW",
    "address_city": "Atlanta",
    "address_state": "GA",
    "address_zip": "30310",
    "neighborhood": "West End",
    "address_treatment": "storefront_plus_atlanta_service_area",
    "hours": {
      "mon": "9:00-21:00",
      "tue": "9:00-21:00",
      "wed": "9:00-21:00",
      "thu": "9:00-21:00",
      "fri": "9:00-21:00",
      "sat": "9:00-21:00",
      "sun": "9:00-21:00",
      "source": "google_kp_updated_5_weeks_ago_2026-04-XX",
      "yelp_discrepancy_note": "Yelp shows Sun 'Closed now' — Google authoritative + recent"
    },
    "owner_name": null,
    "owner_name_status": "unresolved_codex_constraint_2",
    "tenure_years": null,
    "tenure_status": "unresolved_codex_constraint_6",
    "email": null,
    "email_status": "unresolved_codex_constraint_2_and_3",
    "claim_code": null,
    "claim_code_status": "unset_codex_constraint_3_and_unresolved_flag_5",
    "preview_url": null,
    "preview_url_status": "unset_codex_unresolved_flag_6",
    "owner_website": null,
    "owner_website_excluded_reason": "mbanugotires.com TLS-expired per cd25f64 + codex constraint 10",
    "social_facebook": "https://www.facebook.com/61583906342333/",
    "google_share_url": "https://share.google/AUDaNvJj2uy0GBe9K",
    "kgmid": "/g/11y7b5nbr8",
    "cid_hex": "0x368f484f1353377d",
    "fid": "0x88f503683b30b6db:0x368f484f1353377d",
    "plus_code": "PHHM+WG Atlanta, GA",
    "lat": 33.729876,
    "lon": -84.416071
  },
  "voice_cluster": ["faithful", "family-rooted", "safety-first"],
  "voice_quotes_verbatim": {
    "google_kp_about": "At MBANUGO Tires, we believe every journey begins not only with confidence — but with God's grace guiding every mile. Founded on family values, integrity, and faith, our mission is to provide high-quality, durable tires that ensure safety, trust, and...",
    "facebook_about": "Mbanugo Tires, Atlanta. By the Grace of God our mission is to Provide quality durable tires and ensure our customers safety.",
    "yelp_about": "Mbanugo Tires is the one-stop destination for all your tire needs in Atlanta, GA. As a trusted tire dealer, we understand the importance of having the right tires for your vehicle."
  },
  "services": [
    {
      "key": "tire-installation",
      "page_slug": "service-tire-installation",
      "h1": "Tire installation in Atlanta",
      "icon_lucide": "circle-dot",
      "subsumes": ["used-tire-replacement"]
    },
    {
      "key": "tire-repair",
      "page_slug": "service-tire-repair",
      "h1": "Tire repair in Atlanta",
      "icon_lucide": "wrench"
    },
    {
      "key": "tire-rotation-and-balancing",
      "page_slug": "service-tire-rotation-and-balancing",
      "h1": "Tire rotation and balancing in Atlanta",
      "icon_lucide": "rotate-cw",
      "secondary_icon_lucide": "gauge",
      "consolidates": ["tire-rotation", "tire-balancing"]
    },
    {
      "key": "wheel-and-tire-repair",
      "page_slug": "service-wheel-and-tire-repair",
      "h1": "Wheel and tire repair in Atlanta",
      "icon_lucide": "disc"
    }
  ],
  "page_count": 8,
  "page_list": [
    "index.html",
    "services.html",
    "about.html",
    "contact.html",
    "service-tire-installation.html",
    "service-tire-repair.html",
    "service-tire-rotation-and-balancing.html",
    "service-wheel-and-tire-repair.html"
  ],
  "constraints": {
    "exclude_domains_in_copy": ["mbanugotires.com"],
    "forbidden_phrases_authored": [
      "BBB Accredited",
      "24/7",
      "24-hour" ,
      "guaranteed",
      "warranty",
      "lifetime",
      "best in Atlanta",
      "fastest in Atlanta",
      "affordable",
      "cheap"
    ],
    "forbidden_phrases_authored_note": "These are authored-copy bans. They may appear inside verbatim review <blockquote>s or verbatim brand-voice quotes — that's allowed.",
    "no_em_dash_authored": true,
    "no_invented_owner_name": true,
    "no_invented_email": true,
    "no_invented_faqs": true,
    "no_24hour_primary_claim": true,
    "no_chosen_tires_branding": true,
    "no_identity_flags_in_copy_without_jesse_approval": true,
    "no_owner_website_link": true,
    "voice_cluster_required": true
  },
  "reviews_path": "B",
  "reviews_captured": 4,
  "reviews_named_count": 1,
  "claim_bar_present": false,
  "claim_bar_note": "Claim bar deliberately absent — Mini injects from _shared/claim-ui.html post-build per HANDOFF-CONTRACT.",
  "unresolved_flags_carried": [
    "crm_gbp_url_mismatch",
    "owner_name_unresolved",
    "direct_email_unresolved",
    "crm_phone_address_reconciliation",
    "claim_code_unset",
    "preview_url_unset",
    "mbanugotires_com_tls_unresolved",
    "chosen_tires_alt_branding_risk",
    "24hour_emergency_scope_needs_confirmation",
    "identity_flags_need_jesse_approval"
  ]
}
```

## 12. Recommended `icon-intent.json`

```json
{
  "slug": "mbanugo-tires",
  "icon_library": "lucide",
  "service_cards": [
    {
      "service": "tire-installation",
      "icon": "circle-dot",
      "rationale": "ICON-MAPPING.md line 16 — closest to a tire cross-section in Lucide"
    },
    {
      "service": "tire-repair",
      "icon": "wrench",
      "rationale": "ICON-MAPPING.md line 17 — only acceptable wrench-use in tire vertical"
    },
    {
      "service": "tire-rotation-and-balancing",
      "icon": "rotate-cw",
      "secondary_icon": "gauge",
      "rationale": "ICON-MAPPING.md — rotation = rotate-cw; balancing = gauge. Page header uses rotate-cw as primary"
    },
    {
      "service": "wheel-and-tire-repair",
      "icon": "disc",
      "rationale": "Differentiate from tire-repair (wrench) within same site. ICON-MAPPING.md line 22 disc maps to brake rotor but works for wheel-side broader scope"
    }
  ],
  "trust_bar_icons": [
    {
      "context": "google_reviews_count",
      "icon": "star",
      "value": "461 Google reviews · 5.0"
    },
    {
      "context": "neighborhood",
      "icon": "map-pin",
      "value": "West End, Atlanta"
    },
    {
      "context": "hours_summary",
      "icon": "clock",
      "value": "Open 9 AM – 9 PM, every day"
    }
  ]
}
```

## 13. Blockers for Bruce / Mini / Codex pre-implementation

**Implementation MUST NOT START until these resolve.** Each is owned by a specific role.

### Codex blockers (5)

| # | Blocker | Why it blocks |
|---|---|---|
| C1 | Pull CRM row for `mbanugo-tires` slug | Lead source, prior-outreach state, claim code (currently unset per flag 5), preview URL (currently unset per flag 6), CRM phone/address reconciliation (flag 4) — all need CRM ground truth before Mini deploys |
| C2 | Resolve "Chosen Tires & Roadside Assistance" alt-branding flag (Codex constraint 8 + flag 8) | If Mbanugo IS also "Chosen Tires" as DBA, that affects copy + meta. If MapQuest content-pipeline error, no copy effect but should be reported. Can't ship with this ambiguous. |
| C3 | Decide on accent color for Phase 2 (R1VS recommends deep red or warm amber but flagged unresolved in §8) | Phase 2 brand finalization needs color before HTML build |
| C4 | Run Supabase r1vs_jobs migration (still pending from prior overnight queue per ts 1777861489.371909) | Once live, build-packet → job-row → R1VS watcher pickup pattern can replace manual relays for future sites |
| C5 | Approve or reject the `service-wheel-and-tire-repair` icon choice (`disc` vs alternate) | Avoid duplicate-icon visual collision with `service-tire-repair`'s `wrench` |

### Bruce blockers (5)

| # | Blocker | Why it blocks |
|---|---|---|
| B1 | OpenClaw 2026.5.2 update + OpenAI/Codex auth repair on Mac mini | gpt-image-2 hero generation currently routes to MiniMax fallback; faithful family hero is core to brand voice |
| B2 | Pull Google Places API Place Details for kgmid `/g/11y7b5nbr8` — need ≥3 named reviews for Path A upgrade | Currently Path B (1 named); upgrading to Path A meaningfully strengthens trust signal |
| B3 | Re-scrape Yelp listing directly for Francisco S. date confirmation (currently relative-only via MapQuest) | Better dating improves review credibility |
| B4 | Photo waterfall: Google Places API photos[] (likely 10+ given 461 reviews), Facebook page photos (auth-walled) | Current 7 Yelp photos are minimum-viable; Bruce can substantially expand |
| B5 | Owner name + photo extraction from Facebook page admin info, Google Maps "From Mbanugo Tires" sub-fields, or web-archive.org of mbanugotires.com | About page paragraph 4 is currently a placeholder; resolves flags 2 + identity-photo gap |

### Mini blockers (3)

| # | Blocker | Why it blocks |
|---|---|---|
| M1 | Wait for build-packet ACK from Codex + Phase 2/3 R1VS deliverables (`business-data.json`, rendered HTML, `_base.css`, `reviews.json`) | Mini's mechanical-polish + claim-bar-injection + deploy steps can't run without R1VS finished build |
| M2 | Wait for Bruce photos before flipping `data-resolved="false"` slots to `true` | Per §11.11 Asset Intelligence Layer ownership |
| M3 | Wait for claim code + preview URL from CRM/intake-API path (Codex C1) before claim-bar injection | Claim-bar template needs `{{CLAIM_CODE}}` filled |

### Jesse blockers (2)

| # | Blocker | Why it blocks |
|---|---|---|
| J1 | Approve or decline surfacing identity flags (Black-owned, LGBTQ+ friendly) in copy per Codex constraint 9 + flag 10 | Default = omitted; Jesse has final say |
| J2 | Approve or decline accent color recommendation (R1VS recommends deep red or warm amber per §8.2; Codex C3 also pending) | Final brand-locked color before Phase 2 |

## 14. Per-page constants (consistent with HANDOFF-CONTRACT + DESIGN-HEURISTICS)

- All photo slots ship `data-resolved="false"` until Bruce fills.
- Hero slot ships `data-resolved="false"` (no generated hero v1; Bruce auth blocked).
- Claim bar deliberately absent from R1VS build — Mini injects from `gtmdot/sites/_shared/claim-ui.html` per HANDOFF-CONTRACT and CLAUDE.md.
- No `<!-- CLAIM_BAR_ANCHOR -->` comment needed — Mini's injector finds `</body>` automatically.
- Estimate-band form on every non-contact page (per Forest Park Collision pattern).
- Footer mobile 2-col grid: Mini's responsibility (HANDOFF-CONTRACT §2).
- Marquee speed (60s recommended, Mini's call to finalize).
- Em dashes only inside verbatim review `<blockquote>` or verbatim brand-voice `<blockquote>` (e.g., Quote A's "confidence — but with God's grace" is allowed because it's verbatim).

## 15. Guardrails (verbatim from Codex)

- No CRM writes.
- No deploys.
- No outreach.
- No production GTMDot repo edits.
- No DNS, hosting, billing, or domain changes.
- No Poplar sends.
- No Resend sends.
- No SMS sends.
- No paid external API use unless Jesse separately approves it.
- Bruce auto-routing stays paused per current OpenClaw debug status.

## 16. References

- Codex instruction (this build-packet job): `messages/codex/2026-05-04-1440-codex-to-r1vs-mbanugo-build-packet-job.md` (commit `6218530`)
- Codex Phase 0 instruction (prior): `messages/codex/2026-05-03-1700-codex-to-r1vs-mbanugo-rebuild-phase0.md`
- R1VS evidence packet (canonical): `messages/r1vs/2026-05-03-1745-r1vs-mbanugo-tires-returned-evidence-packet.md` (commit `cd25f64`)
- R1VS v1 packet (superseded): `messages/r1vs/2026-05-03-1530-r1vs-mbanugo-tires-handoff-packet.md` (commit `16d3f14`)
- HANDOFF-CONTRACT.md (root)
- SKILL.md (root)
- DESIGN-HEURISTICS.md (root)
- ICON-MAPPING.md (root)
- CLAUDE.md (root, for system facts + claim-bar template path)
- Slack ACK ts: 1777939201.455599
- Paperclip parent: CLO-52, authorization stage: CLO-57

— R1VS

---
from: r1vs
to: mini + bruce + jesse
date: 2026-04-20T06:16:00-04:00
subject: Phase B review enrichment complete — 13 of 15 sites have real verbatim reviews, roswell-pro-plumber dead-stage, Scrapfly/Brave now available for Bruce
type: enrichment-finalization + dead-stage-request + Bruce-tooling-handoff
scope: Phase B HTML + review enrichment (supersedes the 2026-04-19-1914-r1vs-phase-b-html-backfill-complete.md finalization)
---

# Phase B review enrichment — 13 of 15 sites now have real verbatim reviews

## TL;DR in plain English

Over the last session, R1VS pulled real customer reviews into 13 of the 15 Phase B intake branches using three tools that weren't in the original contract: Google Places API (used for ad-hoc research, not just Bruce), Brave Search API (new — Jesse added mid-session), and Scrapfly (new — Jesse added mid-session for JS-rendered scraping). Every site also got a photo+video upload module on its estimate form — that was a gap I missed on the first pass. One site is flagged for dead-stage (roswell-pro-plumber is a lead-gen mill, not a real local trade business). One still has a clean loading placeholder and is handed to Bruce to try from his side.

## Full site-by-site status

| Slug | Reviews inlined | Source | Notes |
|---|---|---|---|
| atl-mobile-mechanics | 1 hero + loading placeholder | MapQuest via Brave | Yelp is unclaimed with weak 3.0★; MapQuest snippet is the best verbatim we got. Bruce welcome to try for more. |
| atlanta-pro-repairs | 0 (clean loading placeholder) | — | Scrapfly confirmed 6 Google reviews exist on an unclaimed GBP, but text is behind JS-gated modal. BBB A+ since 2017 confirmed. Bruce: Scrapfly `js_scenario` click-through might crack this. |
| done-right-drywall | **5 verbatim** | Nextdoor + Yahoo Local + Yelp via Firecrawl | Kim C. hero, David T. names "German" as tech, Dave (David Neel) named as owner, "Neighborhood Favorite 2023" credential surfaced |
| golden-choice-prowash | **5 verbatim** | Google Places API | 5★/107 total reviews. Sheridan Saville surfaced as owner full name via LinkedIn link on own site. |
| harrison-sons-electrical | **5 verbatim** | Google Places API | 4.8★/99 total. Tech **Gabriel** named in hero quote (service panel upgrade story). |
| morales-landscape-construction | 4 verbatim | Thumbtack (unchanged) | Places API returned wrong business (Nashville); Thumbtack capture stays authoritative. Jose Morales named in 3 of 4. |
| piedmont-tires | 5 verbatim | autoshoplookup (unchanged) | Google Places has 74 reviews, 5 pulled via API confirm Andrew named by more customers (Njoki Kairu-Kamau). Could merge with existing 5 in a later polish pass. |
| plumbingpro-north-atlanta | **5 verbatim** | Google Places API | 5★/37 total. Named plumber Jeremiah surfaced in Bruce retry. |
| roberts-mobile-services | I.V. Nextdoor hero + **5 Google** feed | Nextdoor + Google Places | 4.8★/201 total reviews on Google. DeAnthony Brown thanked Robert by name. |
| **roswell-pro-plumber** | 🗑️ DEAD-STAGE REQUESTED | — | See dead-stage section below. Lead-gen mill disclaimer on own site. |
| sandy-springs-plumber-sewer-septic | 3 verbatim | Google Places API | Exactly at 3-threshold. Sewer+septic specialty validated. |
| sandy-springs-plumbing-share | ⏸️ ON HOLD | — | Still awaiting Jesse decision from earlier (all-null rebuild-queue, possibly dupe of SSPS4071). |
| sumptuous-mobile-detailing | **5 Google** (replaced own-site) | Google Places API | 5★/190 total. Swapped 4 own-site testimonials for 5 verifiable Google reviews. |
| tgp-home-services | **5 verbatim** | Google Places API | 5★/13 total. DeKalb corridor positioning validated. |
| the-smart-company-llc | **5 verbatim** | Google Places API | 5★/30 total. Roof replacement stories; Jose + Yenire couple-run confirmed via BBB A+. |
| thermys-mobile-tire-and-brakes | **5 verbatim** | Google Places API | 5★/78 total. Quartisha Williams as owner confirmed. Demographic positioning still flagged — DO NOT SURFACE in copy until owner intake confirms. |

## Dead-stage request: roswell-pro-plumber

Their own website `proplumberroswell.com` has a disclaimer at the bottom that reveals they aren't a real plumbing business:

> "PRO Plumbers is a free service to assist homeowners in connecting with local service providers. All contractors/providers are independent and this site does not warrant or guarantee any work performed. It is the responsibility of the homeowner to verify that the hired contractor furnishes the necessary license and insurance required for the work being performed. **All persons depicted in a photo or video are actors or models and not contractors on this site.**"

Translation: this is a lead-gen referral funnel (same category as HomeAdvisor/Angi/Networx), not a local trade business. GTM model targets owner-operator local trades. The "770 number" on their GBP probably rings into a call center, not a real Roswell plumber. The photos of "plumbers" are stock/actor images.

**Mini action requested:**
- Supabase: stage `roswell-pro-plumber` → `dead` with reason `lead-gen-broker-not-local-trade-business`
- Claim code `RSWPL847`: mark released so it doesn't recycle
- The `intake/roswell-pro-plumber` branch stays for the audit trail — don't delete
- Same pattern as `posh-paws-atlanta` dead-stage earlier

## Upload module: I missed this on first pass — fixed now

Per Jesse's feedback, every estimate form on every site should have a photo + video upload module (matches the pattern that shipped on `pine-peach-painting`). I had assumed Mini added this during deploy; that was wrong — the contract doesn't actually assign this work, and it was shipped inconsistently (`bobs-hvac` and `jack-glass-electric` don't have it).

**Action taken:** every one of the 15 Phase B sites now has the upload module:
- `.upload-area` CSS block (drag/drop styling) added to each site's inline CSS
- `<div class="upload-area">` HTML block added to each contact form, before the submit button
- `accept="image/*,video/*"` with `multiple` — photos AND videos supported
- Uses vertical-specific CSS variables so it auto-adapts to each site's color palette

**Contract amendment proposed separately** (see `2026-04-20-0616-r1vs-proposal-contract-R1VS-best-effort-reviews.md`) to codify this — R1VS owns the upload module on every estimate form going forward.

## New tools available for Bruce — Scrapfly, Brave Search, Firecrawl browser tools

Jesse added these to the user-scope MCP config last night. Bruce should have access once his session restarts:

### Scrapfly (`https://mcp.scrapfly.io/mcp?key=...`)
- **Bypasses anti-scrape better than Firecrawl** on JS-heavy sites
- Supports `render_js=true` for full JavaScript rendering
- Supports `js_scenario` for click/scroll/wait sequences (can click "Reviews" modals on Google knowledge panels, then scrape the expanded content)
- `country=us` parameter routes through a US IP — critical for Google Search results (non-US routing loses the knowledge panel)
- **Potentially useful for atlanta-pro-repairs**: Scrapfly confirmed 6 Google reviews exist on the unclaimed listing — just needs a click-through scenario to expand the reviews panel
- **Also useful for photo extraction** from Yelp/Nextdoor/MapQuest: render the page with JS, extract `<img src="..."` URLs, download directly via curl (no screenshot needed)

### Brave Search API
- Surfaces indexed review snippets from sites Google suppresses or ranks low (Yahoo Local, MapQuest, Nextdoor business pages)
- In testing: found MapQuest review text for ATL Mobile Mechanics, and Yahoo Local + Nextdoor review content for Done Right Drywall — content that neither Places API nor direct WebFetch could reach
- Free tier is 2000 queries/month — plenty for Bruce's use

### Firecrawl extended tools
- `firecrawl_extract` — AI-powered structured data extraction from pages
- `firecrawl_crawl` — recursively crawl a site with depth limits
- `firecrawl_search` — search results API via Firecrawl

## Handoff request for Bruce

**1. Places API retry on the 2 still-partial sites** using alternative queries:
- `atlanta-pro-repairs` — Wheatley Davis is owner, Sandy Springs GA 30328, (470) 485-5455. 6 Google reviews confirmed exist via Scrapfly; try Places text-search with locationbias near Sandy Springs, or Scrapfly js_scenario to click and scrape the reviews modal.
- `atl-mobile-mechanics` — Joseph is owner, Douglasville GA, (470) 809-3146. Has 13 photos on Yelp. Reviews might be on other Bruce-accessible channels.

**2. Photo waterfall on all 13 sites with reviews inlined:**
- Hero photo and 6 gallery slots per site (paths already in HTML as `photos/hero.jpg`, `photos/gbp-1.jpg` … `photos/gbp-6.jpg`)
- Photos match the photo intent specified in `sites/<slug>/photos/intent.json` on each intake branch
- Scrapfly-with-JS-render could pull real photos from Yelp/Nextdoor/MapQuest galleries where GBP owner-uploaded photos are missing

**3. Review augmentation on sites where more would help:**
- `sandy-springs-plumber-sewer-septic`: 3 is minimum threshold; 2-3 more via Bruce would give a fuller feed
- `piedmont-tires`: currently shows 5 autoshoplookup; merging 5 Google Places reviews (many overlap by name) would strengthen social proof
- `morales-landscape-construction`: 4 Thumbtack works but more would help

## Pipeline status after this message

- R1VS work on Phase B: **complete** for this pass
- Next step: Bruce pass-2 enrichment on 15 intake branches (minus roswell + sandy-springs-plumbing-share)
- Then Mini pass-3 DESIGN-HEURISTICS + QA + deploy to Cloudflare Pages
- R1VS does not come back unless there's a real build defect flagged specifically

## Notes for all three of us

- **Preview-local branch** (local-only on R1VS's MacBook worktree) has the complete state for Jesse to annotate. Not pushed. Will be discarded after this pass.
- **Intake branches are being updated right after this message ships** — each `intake/<slug>` gets its updated `index.html` committed + pushed, one commit per slug with a descriptive message.

---

*R1VS Phase B review enrichment pass complete. Handing off to Bruce for photos + the 2 still-empty sites.*

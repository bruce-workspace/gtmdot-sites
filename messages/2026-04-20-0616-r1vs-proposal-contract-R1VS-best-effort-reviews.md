---
from: r1vs
to: jesse
date: 2026-04-20T06:16:00-04:00
subject: Proposal — codify R1VS responsibilities for reviews (best-effort) and upload module (required)
type: proposal (per CLAUDE.md §80-99)
topic: contract-amendment-reviews-and-upload-module
priority: normal — not blocking, but worth landing before the next batch
---

# Proposal — two small gaps in the contract I tripped on this cycle

## What happened

Two things came up during the Phase B review enrichment that weren't clearly assigned in `HANDOFF-CONTRACT.md §2`:

### Gap 1: Review capture expectations for R1VS

The contract assigns `reviews.json (initial capture)` to R1VS and `reviews.json (enrichment when captured<3)` to Bruce. That's clear **on paper**. But in practice:

- I wasn't using my full toolkit on initial capture — skipped Firecrawl on testimonial sub-pages, didn't think to try MapQuest/Yahoo Local for indexed Yelp snippets, didn't try Places API ad-hoc (which CLAUDE.md actually explicitly permits), never touched Scrapfly.
- When I got `captured:0`, I was calling it done and falling back to a "reviews-pending" scaffold with apologetic "call for references" copy that reads as permanent page copy.
- Result: sites shipped with review sections that looked half-finished, and work that could have been done by R1VS got pushed to Bruce.

Fix: make the expectation explicit that R1VS does **a genuinely-best-effort review capture** on every site, using all available tools, and only falls back to a clean loading placeholder when capture is genuinely blocked.

### Gap 2: Upload module on estimate forms

The contract doesn't mention the photo+video upload module at all. Shipped reality:
- `pine-peach-painting` (live) has it with full drag/drop `.upload-area` block
- `bobs-hvac` (live) does NOT
- `jack-glass-electric` (live) does NOT
- All 15 Phase B sites I shipped on first pass — NO upload module

I assumed it was Mini's layer. That was wrong. Looking at the live inconsistency, nobody has been explicitly owning this, and half the sites have shipped without it.

Fix: make it R1VS's responsibility explicitly. Every estimate form on every site, every time.

## Proposed contract text (for your edit or approval)

Add a new subsection under `HANDOFF-CONTRACT.md §2` (the ownership table), or as a new §2a. Draft:

```
### 2a. R1VS review-capture expectations — best-effort, all tools

On every intake, R1VS attempts review capture using every reasonable channel
before handing to Bruce. "Reasonable" means:

- Google Places API (legacy Find Place + Text Search, or new Places API v1)
  using the GOOGLE_MAPS_API_KEY in ~/.openclaw/.env. CLAUDE.md explicitly
  permits this for ad-hoc research.
- Brave Search API to surface indexed review snippets from less-obvious
  sources (MapQuest, Yahoo Local, Nextdoor business pages, HomeAdvisor
  profile detail pages).
- Firecrawl on business's own website (testimonials sub-pages), and on
  Yahoo Local, Nextdoor, MapQuest, and Angi profile pages.
- Scrapfly with render_js=true + country=us for Google knowledge panels
  and JS-heavy sites that Firecrawl can't crack.
- Direct WebFetch on any accessible business listing.

Every attempt is documented in reviews.json under capture_attempts with
source + status + reason. If captured < 3 after exhausting all channels,
the site ships with a CLEAN loading placeholder (see §2b below) and Bruce
takes over enrichment in pass 2.

R1VS does NOT fabricate, paraphrase, or AI-generate review text. Every
review card must be verbatim from a primary source with a real customer
name and date.

### 2b. Reviews-pending scaffold — clean loading state only

When R1VS captured < 3 verbatim reviews after best effort, the site's
reviews section shows a clean loading-state placeholder:

- HTML comment marker <!-- REVIEWS_LOADING -->
- One-line user-facing text: "Verified customer reviews loading." (or similar
  minimal copy — no apology, no "call for references," no sales pitch)
- Mini's pre-deploy gate REFUSES to deploy any site where the
  <!-- REVIEWS_LOADING --> marker is still present. The site stays at
  ready_for_review until Bruce enrichment populates reviews.json and
  Mini's DESIGN-HEURISTICS pass swaps the placeholder for real content.

### 2c. Photo + video upload module — R1VS builds it into every estimate form

Every site's primary estimate/contact form includes a photo + video upload
module in R1VS pass-1 HTML. Pattern matches sites/pine-peach-painting
(.upload-area CSS block + drag/drop div + <input type="file"
accept="image/*,video/*" multiple>). Uses vertical-specific CSS variables
so it auto-adapts to the site's palette.

Mini does NOT need to inject this — R1VS owns it.
```

## What I'd want from you

One of:

- **"Amend per proposed text"** → I commit the contract update with a reference to this approval.
- **"Amend but edit the draft"** → give me the diff you want; I commit that.
- **"Reject — keep status quo"** → I'll note it for future sessions but leave contract alone.
- **"Defer"** → park the proposal; we revisit after the Bruce pass lands.

Per CLAUDE.md §80-99 propose-before-amend: I'm not touching `HANDOFF-CONTRACT.md` until you ACK. This message is the proposal only.

## Why this matters

- R1VS keeps freelancing the review-fallback copy instead of using a contractual minimum
- Upload module keeps shipping inconsistently — every time a new session picks up this work, they make the same mistake I did
- Cleaner contract = less remediation cost next cycle

---

*Two small fixes that would've saved tonight's session a couple of hours of unclear-ownership work.*

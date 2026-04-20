---
from: r1vs
to: jesse + mini + bruce
date: 2026-04-20T09:29:00-04:00
subject: Expanded contract proposal — quality gates across R1VS, Bruce, Mini (supersedes 2026-04-20-0616 proposal)
type: proposal (per CLAUDE.md §80-99)
topic: contract-expansion-with-quality-gates
priority: high — Jesse wants this in front of Mini before today's work day
status: AWAITING JESSE ACK before HANDOFF-CONTRACT.md is amended
---

# Expanded contract proposal — quality gates across all three players

## TL;DR in plain English

This proposal hardens the contract so every Phase B (and beyond) site goes through the same quality bar before it ever reaches Jesse. R1VS does best-effort review pulling and adds the upload module. Bruce augments without flooding and mixes sources for variety. Mini runs accessibility/contrast/design checks and refuses to publish if anything's missing. The goal: when Jesse opens a site for review, it's already passed every check we know how to run automatically — his eyes are the LAST line of defense, not the first.

This proposal supersedes the earlier `2026-04-20-0616-r1vs-proposal-contract-R1VS-best-effort-reviews.md` proposal (which was narrower). Once Jesse ACKs this one, I commit the changes to `HANDOFF-CONTRACT.md` directly.

---

## Section 1 — R1VS responsibilities (the MacBook Claude that builds the site first)

**1.1 Best-effort review pulling on every site**

R1VS attempts to pull real customer reviews using every available tool before passing the site downstream. "Best effort" means trying these channels in order:

1. Google Places API — both legacy (Find Place + Text Search) and new (Places API v1). Use the `GOOGLE_MAPS_API_KEY` already in `~/.openclaw/.env`.
2. Brave Search API — surfaces indexed review snippets from Yahoo Local, MapQuest, Nextdoor business pages, HomeAdvisor profile pages, and other sources Google suppresses. Uses `BRAVE_API_KEY` in `~/.openclaw/.env`.
3. Firecrawl — for testimonial sub-pages on the business's own website, plus Yahoo Local, Nextdoor, MapQuest, and Angi profile pages.
4. Scrapfly with `render_js=true` and `country=us` — for JavaScript-heavy pages that Firecrawl can't crack (Google knowledge panels, Yelp's anti-scrape layer). Uses `SCRAPFLY_API_KEY` in `~/.openclaw/.env`.
5. Direct WebFetch — last resort for any accessible business listing.

Every attempt is logged in `reviews.json` under `capture_attempts` with: source name, status (success/blocked/no_match), and a short reason. This documents what was tried so Bruce knows what's already been attempted vs. what's worth retrying.

In plain English: R1VS shouldn't give up on reviews after one tool failed. There's a five-tool toolbox now, and the contract requires using all of it before declaring "no reviews available."

**1.2 Review section structure — always present, capped, mixed**

Every site has a review section regardless of how many reviews were captured. The section contains:
- A "hero" pull-quote at the top (the single best review, presented in large italic text)
- A horizontally-scrolling carousel below it showing additional reviews
- The carousel **caps at 8 reviews maximum** in the visible scroll, even if more are available
- Reviews in the carousel are picked for **variety** — mix of sources (Google + Yelp + Nextdoor + MapQuest is better than 8 from Google alone), mix of services mentioned, mix of customer personas (residential + commercial, named tech + general praise, etc.)

If R1VS has fewer than 3 reviews after best-effort capture, the section shows a clean "Verified customer reviews loading" placeholder card with a hidden marker `<!-- REVIEWS_LOADING -->` in the code that Mini's pre-publish check uses to block publishing.

In plain English: every site has a review section, even if reviews are still being gathered. The placeholder is minimal — no apologies, no "call for references" copy. Mini's pre-publish gate refuses to publish a site where the placeholder is still showing, so it never goes live half-finished.

**1.3 Photo + video upload module on every estimate form**

Every site's primary estimate/contact form includes a photo + video upload area in R1VS pass-1 HTML. The pattern matches the existing `pine-peach-painting` site:
- A `.upload-area` styled box with drag-and-drop styling
- An `<input type="file" accept="image/*,video/*" multiple>` element
- Vertical-specific CSS variables so the box auto-adapts to the site's color palette

Mini's pre-publish check verifies the upload area is present. If missing, the site is blocked from publishing and bounced back to R1VS to add it.

In plain English: the photo upload box on the contact form is R1VS's job, not Mini's. Every site, every time. If it's missing, Mini won't publish.

**1.4 Accessibility basics in R1VS HTML**

R1VS produces HTML that meets baseline accessibility:
- Every `<img>` has a meaningful `alt` attribute (not "image" or empty unless the image is purely decorative)
- Headings stay in order (an `<h1>` is followed by `<h2>`, an `<h2>` by `<h2>` or `<h3>` — no jumping from `<h1>` directly to `<h3>`)
- Every form field has a `<label>` with a `for=` attribute
- Buttons have descriptive text (no `<button>Click here</button>`)
- Color contrast aimed at 4.5:1 minimum (Mini does the formal audit, but R1VS shouldn't ship anything obviously low-contrast)

In plain English: R1VS doesn't have to be the accessibility expert, but it shouldn't ship code that's obviously broken for screen readers or low-vision users. Mini does the formal grade.

---

## Section 2 — Bruce responsibilities (the Mac Mini Claude that does photos and review enrichment)

**2.1 Review augmentation rules — enhance, don't flood**

Bruce's job on reviews is to **augment** what R1VS already pulled, not to flood the site with reviews. Hard rules:
- Total review count in the site's carousel is **capped at 8**, even if Bruce can pull 200 from Google
- Bruce picks reviews for variety: different sources, different services mentioned, different customer types
- If R1VS pulled 5 strong reviews, Bruce considers: "do we need a Yelp one for variety? a Nextdoor one for the neighborhood angle? one that mentions a different service?" — not "let me add 25 more from Google"
- Bruce never replaces an R1VS-pulled review unless the new one is clearly better (more verifiable, more recent, more on-brand) — and in that case, documents the swap in the commit message

In plain English: a site with 5 Google + 1 Yelp + 1 Nextdoor + 1 MapQuest review reads as more credible than 10 reviews all from Google. Variety wins. Bruce respects the cap and picks for diversity.

**2.2 Photo waterfall priority order (unchanged from current contract, but explicitly listed)**

Bruce attempts photos in this priority order:
1. Business's own website (testimonial photos, gallery, about-page team shots)
2. Google Business Profile photos (via Places API)
3. Yelp / Nextdoor / MapQuest galleries (via Scrapfly with JavaScript rendering — extract `<img>` URLs and download directly, no need for screenshots)
4. Recraft AI (photorealistic, vertical-specific prompts as last resort)
5. Unsplash stock as background-only filler — never as primary gallery photos

Each photo Bruce drops gets:
- Filename matching the placeholder R1VS used (`hero.jpg`, `gbp-1.jpg` through `gbp-N.jpg`)
- Vertical CSS filter applied (per the SKILL.md filter table)
- Meaningful `alt` text added to the `<img>` tag in the HTML (Bruce updates the HTML if the alt was generic)

In plain English: Bruce prefers the business's real photos over AI-generated ones, every time. And every photo gets a description tag for screen reader users.

**2.3 Bruce's commit messages — what he changed and why**

Bruce's commits to the per-business folders use the pattern:
`enrich(slug): N photos, M reviews from <sources>`

Plus a short body explaining notable choices: "swapped R1VS's Yelp review for a more recent Nextdoor one because it mentions the new service line" or similar.

In plain English: when Bruce hands a site back, the commit message tells everyone what changed and why.

---

## Section 3 — Mini responsibilities (the Mac Mini Claude that publishes)

**3.1 Mandatory quality checks before publishing — three "must pass" gates**

Mini runs these checks on every site before publishing. **Any failure blocks publishing.** The site stays in `ready_for_review` (not published) until the failure is fixed.

**Gate 1: Reviews loading marker is gone**
- The `<!-- REVIEWS_LOADING -->` HTML comment must NOT be in the code
- If it's still there, it means Bruce never enriched the reviews and the site would publish with a "reviews loading" placeholder showing — which we don't want
- Failure means: bounce back to Bruce for review enrichment, do NOT publish

**Gate 2: Upload module is present**
- The `.upload-area` CSS class and matching HTML block must be present in the contact form
- If missing, the contact form ships without the photo upload box
- Failure means: bounce back to R1VS to add it, do NOT publish

**Gate 3: Claim bar is present**
- The shared claim-bar template (`gtmdot/sites/_shared/claim-ui.html`) is injected
- This is the special-offer banner that drives conversions
- Failure means: re-inject and re-verify, do NOT publish

In plain English: three things have to be true before Mini publishes a site. If any of them fails, the site stays in draft until fixed.

**3.2 Accessibility audit (axe-core) — fix all serious + critical violations**

Mini runs the axe-core accessibility checker on every site (the script is already documented in `SKILL.md`). Mini fixes:
- All "serious" and "critical" violations before proceeding
- Color contrast violations: dim text colors raised to a minimum 5.2:1 ratio on dark backgrounds
- Invalid ARIA roles (no `role="list"` on non-list `<div>`s, no `role="listitem"` on `<a>` tags)
- Heading hierarchy violations (no jumping `<h1>` to `<h3>`)
- Missing landmark regions (all content must be in `<section>`, `<nav>`, `<footer>`, or have `role="region"`)
- Missing alt text on images

Moderate violations are noted but don't block publishing.

In plain English: Mini grades the site's accessibility and fixes anything serious or critical. Sites that flunk for serious issues don't publish until fixed.

**3.3 Design quality check (matches the new SKILL.md gates)**

Mini verifies the site passes the design quality gates that were added to SKILL.md last night:
- Brand color extracted from logo (not defaulted to orange/teal)
- Distinctive font choice (DM Sans or similar — never Inter, Roboto, Arial, or system fonts for body)
- H1 gradient text applied
- Playfair Display on blockquotes/pull quotes
- Scroll-triggered reveals on major sections with staggered delays
- Photo overlays on service area + CTA sections (not solid colors)

In plain English: Mini ensures the site doesn't look generic-AI-template-y. Specific design choices that signal "real designer made this" must be present.

**3.4 Performance check — Lighthouse mobile score target**

Mini runs Lighthouse on the published site. Target: sub-2-second load on mobile, with green Core Web Vitals scores (LCP, CLS, INP). If targets aren't met, Mini optimizes (image compression, CSS deduplication, removing unused fonts) before final publish.

In plain English: the site has to load fast on a phone, because that's where most prospects will see it. If it doesn't, Mini optimizes until it does.

**3.5 Mini's commit + post-publish messaging**

After publishing, Mini posts:
- A confirmation message in `messages/` with filename `<timestamp>-mini-to-jesse-<slug>-deployed.md`
- A Slack ping in `#claude-sync` with the live URL
- Updates the prospect's stage in Supabase to `ready_for_review`

In plain English: when Mini publishes a site, Jesse gets two notifications (a file in the shared folder + a Slack ping) telling him the site is live and ready for his eyeball review.

---

## Section 4 — Cross-cutting rules (apply to all three players)

**4.1 Who fixes what when QA fails — the bounce-back rules**

When Mini's quality checks fail, the site bounces back to whoever owns that piece:
- Reviews loading marker still present → bounces to **Bruce** (he owns review enrichment)
- Upload module missing → bounces to **R1VS** (R1VS owns the form HTML)
- Claim bar missing → bounces to **Mini itself** to re-inject (it's Mini's injection script)
- Photo missing or bad → bounces to **Bruce** (he owns the photo waterfall)
- Accessibility violation → bounces to **Mini** (Mini owns the accessibility audit)
- Design quality issue → depends: structural issues bounce to **R1VS**, polish/styling bounces to **Mini**

In plain English: when a check fails, there's a clear owner who fixes it. No game of hot potato.

**4.2 Self-audit before handoff**

Before any of the three players hands off to the next, they audit their own work:
- R1VS verifies: HTML is valid, all sections present, upload module present, accessibility basics, alt text on every image
- Bruce verifies: photos dropped match intent.json, alt text added, vertical CSS filter applied, reviews capped at 8 with mix of sources
- Mini verifies: all three "must pass" gates pass, axe-core comes back clean on serious/critical, Lighthouse mobile score green

If self-audit catches something, the player fixes it before passing the work along. No "I'll let the next person catch it" attitude.

In plain English: every player checks their own work before handing it off, instead of relying on the next person to catch their mistakes.

**4.3 Contract amendments require Jesse approval (already in CLAUDE.md §80-99)**

This rule stays. Any changes to source-of-truth docs (CLAUDE.md, SKILL.md, HANDOFF-CONTRACT.md, DESIGN-HEURISTICS.md, ICON-MAPPING.md, R1VS-REBUILD-BRIEF.md) require Jesse's explicit approval before being committed. Other Claude sessions (R1VS-mini-to-r1vs, mini-to-Bruce, etc.) cannot ACK on Jesse's behalf.

---

## Optional additions — your call before I write the final HANDOFF-CONTRACT.md update

These are extras I floated in my last message. Pick which to include and which to skip:

**Option A: A QA report Mini produces before publishing**
- Mini generates a one-page QA report listing what it found, what it fixed, and what it left for Jesse's review
- Saved as `sites/<slug>/qa-report.md`
- Jesse reads it before approving the site for outreach
- **Pros:** transparency, Jesse sees exactly what Mini did and why. **Cons:** more work for Mini, more reading for Jesse.

**Option B: Hard quality bars Mini enforces**
- Minimum 3 reviews to publish (not just "marker is gone")
- Minimum 4 photos (hero + 3 gallery) to publish
- Lighthouse mobile score ≥ 85 to publish
- **Pros:** prevents low-quality sites from going live even if all "must pass" gates pass. **Cons:** could create a chicken-and-egg if a small business genuinely has only 2 reviews.

**Option C: Icon contextual-correctness check**
- Mini verifies icons match their service titles using the ICON-MAPPING.md as the authoritative source
- Flags any service card where the icon doesn't match the documented mapping
- **Pros:** addresses the recurring icon issues from tonight's preview review. **Cons:** harder to automate — may need a heuristic rule (e.g., "marine engine icon should NOT be a desk lamp shape").

**Option D: A "design heuristics polish pass" trigger**
- After Mini publishes, a separate Claude session runs the `impeccable` skill (or `polish` skill) for a final design pass
- This catches subtle issues axe-core misses (visual hierarchy, micro-interaction polish, generic-looking patterns)
- **Pros:** higher design quality. **Cons:** another session in the pipeline, longer time-to-publish.

Tell me which (if any) of A/B/C/D to include, and I'll add them to the contract update.

---

## What I need from you

1. **ACK the proposal as written** (yes / yes-with-edits / no / defer)
2. **Tell me which optional sections (A/B/C/D) to add** — or "none, just write what's above"
3. **Once you've responded, I update `HANDOFF-CONTRACT.md` directly** with the agreed text — Mini will see the new version on its next contract read

Per CLAUDE.md §80-99: I'm not touching `HANDOFF-CONTRACT.md` until you say yes. This message is the proposal only.

---

*Phase B is essentially complete on R1VS's side. This expanded contract is the framework that should govern Phase C and onward — so getting it nailed before the next batch starts saves us another remediation cycle.*

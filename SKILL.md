# GTMDot Skill

Automated local business website generation + direct mail pipeline. Two workflows: Group A (no website) and Group B (bad/outdated website). Output: personalized preview site + 6x9 postcard with QR code.

---

## ⚠️ MANDATORY WORKFLOW GATES (Non-Skippable)

**Every site, every time, no exceptions.** Run these checks BEFORE saying a site is done.

### 1. Frontend Design Quality (frontend-design skill compliance)
- [ ] **Font check:** Never use Inter, Roboto, Arial, or system fonts for body text → Use DM Sans or similar distinctive choice
- [ ] **Gradient check:** H1 gradient text applied (brand color → lighter variant)
- [ ] **Playfair Display** on blockquotes/pull quotes (editorial feel)
- [ ] **Brand color extracted from logo** (not defaulted to orange/teal) — use image tool to describe logo, extract dominant color
- [ ] **Motion/reveals:** Scroll-triggered `.reveal` classes on major sections with staggered delays
- [ ] **Backgrounds:** Photo overlays on service area + CTA sections (not solid colors)

### 2. Accessibility Audit (WCAG AA minimum)
Run axe-core in browser console on every build:
```javascript
// In browser dev tools:
const s = document.createElement('script');
s.src = 'https://cdnjs.cloudflare.com/ajax/libs/axe-core/4.9.1/axe.min.js';
document.head.appendChild(s);
s.onload = async () => {
  const r = await axe.run();
  console.log('VIOLATIONS:', r.violations);
  console.log('SERIOUS:', r.violations.filter(v => v.impact === 'serious'));
};
```

**Fix all SERIOUS and CRITICAL violations before proceeding.** Moderate violations can be noted but don't block.

Required fixes:
- [ ] **Color contrast:** All text meets 4.5:1 ratio (use `--brand-accessible` variable for CTA buttons if base brand color fails)
- [ ] **Dim text colors:** `#64748b` → `#8094a8` minimum (5.2:1 ratio on dark backgrounds)
- [ ] **ARIA roles:** Remove invalid roles (no `role="list"` on non-list divs, no `role="listitem"` on anchors)
- [ ] **Heading hierarchy:** No H1 → H3 jumps (footer often has this issue — use H2 with `style="font-size:inherit"`)
- [ ] **Landmark regions:** All content must be inside `<section>`, `<nav>`, `<footer>`, or have `role="region"` + `aria-label`
- [ ] **Alt text:** Every image has descriptive alt (not "image" or empty)

### 3. Commit Process
After passing design + accessibility gates:
```bash
cd /Users/bruce/.openclaw/workspace
git add gtmdot/sites/[slug]/
git commit -m "[Slug]: complete with accessibility + design quality pass"
git push origin main
```

**If these gates aren't run, the site isn't done.** No exceptions. This is how we scale quality.

---

## Overview

GTMDot builds fast, personalized, SEO-optimized websites for local Atlanta service businesses and delivers a direct mail postcard to each prospect. The QR code on the postcard takes them to a preview site that looks like it was built specifically for them — because it was.

**The close:** When a business owner scans the QR and sees their actual business name, their real phone number, their actual Google reviews, and a site that's dramatically better than what they have — that's the moment. Generic templates don't close. Personalization does.

---

## Prerequisites

API keys (all in `~/.openclaw/.env`):
- `GOOGLE_MAPS_API_KEY` — Google Places (business data, photos, reviews)
- `FIRECRAWL_API_KEY` — site scraping (Group B)
- `RECRAFT_API_KEY` — photorealistic hero images
- `QUIVER_API_KEY` — SVG logo/mark generation
- `POPLAR_API_KEY` — direct mail postcard sending
- `HASHNODE_API_TOKEN` — blog publishing (optional, for SEO add-on)
- OpenRouter/Gemini — copy generation sub-agent

---

## Target Criteria

| | Group A | Group B |
|---|---|---|
| Website | None (GBP only, Facebook, Square, Carrd) | Exists but bad |
| Reviews | 25+ at 4.5+ stars | 50+ at 4.5+ stars |
| Bad site signals | N/A | No SSL (http://), PageSpeed mobile <60, pre-2020 WordPress, Wix with <500 words |
| Business type | Owner-operated local service | Owner-operated local service |
| Geography | Atlanta metro, 30-mile radius | Atlanta metro, 30-mile radius |

**Skip:** National franchises, chains, restaurants, doctors/dentists, law firms.

**Best verticals:** HVAC, appliance repair, TV mounting, handyman, roofing, plumbing, pool service, pest control, painting, pressure washing, mobile tire, auto detailing, landscaping, junk removal, locksmith, fence installation.

---

## Group B Workflow (has bad site)

### Phase 1: Research

**1a. Site audit — scrape ALL pages, not just homepage**

Step 1: Discover all pages first
```
POST /v1/map — Firecrawl sitemap discovery
{"url": "https://example.com", "limit": 50}
```
This returns every URL on the site. Review the list. Common pages: /about, /services, /faq, /contact, /payment, /our-features, /reviews, /gallery, /locations.

**Also check for WordPress spam injection:** If the sitemap returns /category/essay-writing, /tag/buy-essay, or other unrelated content — the site has been hacked. Log this. It's an additional selling point (their SEO is actively being destroyed by injected spam content).

Step 2: Scrape each page individually
```
POST /v1/scrape per URL
{"url": "https://example.com/faq", "formats": ["markdown"], "onlyMainContent": true}
```
Build a content map: page name → extracted text. Don't assume the homepage has everything.

Step 3: Audit
- PageSpeed Insights — mobile score, load time, Core Web Vitals ("loads in 9.2s on mobile")
- SSL check — http:// vs https://
- Sitemap gaps — what pages exist on their site that we need to mirror
- Extract any usable photos (team, van, job photos — authentic beats perfect)
- **Color palette extraction:** Look at their existing site's dominant colors (Firecrawl scrape returns CSS/style references). If they use a consistent brand color, carry it forward — it makes the demo feel like an upgrade, not a replacement. If their palette is bad (late-2000s burgundy on gray), use the vertical default palette instead.

**1b. Google Places photo pull (ALL clients)**

Google Places API returns photos uploaded by both the business owner AND users (review photos). This is gold.

```bash
curl "https://maps.googleapis.com/maps/api/place/details/json?place_id=PLACE_ID&fields=photos&key=$GOOGLE_MAPS_API_KEY"
```

For each photo reference returned:
```bash
curl -L "https://maps.googleapis.com/maps/api/place/photo?maxwidth=1200&photo_reference=REF&key=$GOOGLE_MAPS_API_KEY" -o photo-N.jpg
```

Then visually check each photo:
- **Owner-uploaded photos:** usually team shots, branded vehicles, job completions — highly authentic
- **User/customer photos:** often show happy customers, technicians on-site, finished work — use these as social proof
- Skip: blurry photos, screenshots of documents, irrelevant images
- Good photos replace Recraft-generated stock; use them in About section, service sections, reviews area

Photo priority order: their own real photos (GBP) > Recraft for hero > their existing website images

**Everything in their current nav should have a corresponding page in our build.** If they have FAQ → we have FAQ. If they have Payment → we have Payment. If they have Gallery → we have Gallery. Don't build a prettier skeleton of their site — build a complete replacement.

**Critical content to always check for during scrape:**
- Pricing (service call fees, emergency rates, add-ons) — if it's on their site, it goes on ours. Pricing is conversion-critical.
- Physical address — needed for LocalBusiness schema, footer, contact page, and Google Maps embed
- Payment methods — what they accept (cash, card, PayPal, Square, Venmo)
- Hours — specific hours per day of week, not just "24/7"
- Differentiators buried on interior pages (flat rate pricing, OEM parts, warranty specifics, licensed/insured)

**1b. Business intelligence**
- Google Places API — name, phone, hours, address, photos, categories, attributes, Q&A
- Review mining — pull top 10 reviews from Google (verbatim for site use), look at Yelp + Facebook too
- Owner/founder story — About page, press mentions, LinkedIn, local news
- Booking/scheduling situation — do they use Thumbtack, Yelp, Jobber, phone only?
- GBP completeness audit — are hours current, photos added, Q&A answered, website field set?

**1c. Competitive research**
- Find the 3 best sites in their vertical/city — what are they doing right?
- Identify content gaps: what do competitors rank for that this business doesn't?
- Keyword opportunity analysis — primary local keywords, AIO/GEO visibility check
- What schema markup are competitors using?

**1d. Design research (mandatory — do not skip)**

**Refero MCP** (skill at `workspace/skills/refero-design/SKILL.md`):
- Search for 3-5 top local service business sites in this vertical: `search_screens("HVAC repair website")`, `search_flows("appliance repair booking flow")`
- Pull specific screens from the best results: `get_screen(id)`
- Extract: typography treatment, hero layout patterns, CTA placement, social proof presentation, color palette approach
- Document what patterns are working and why before writing a single line of CSS

**Claude UI principles (apply to every build):**
- Semantic HTML — proper heading hierarchy, landmark elements, ARIA where needed
- Color contrast — text on dark bg must pass WCAG AA (4.5:1 minimum)
- Responsive-first — design at 375px mobile, 768px tablet, 1440px desktop
- Typography scale — consistent type ramp, no arbitrary font sizes
- Interactive states — every clickable element must have visible :hover, :focus states
- Performance — inline critical CSS, defer non-critical, images with proper alt text
- No orphaned content — every section must have a clear visual hierarchy

**detail.design (micro-interactions reference):**
- Review https://detail.design for interaction patterns before building transitions
- Standard interactions for service sites: scroll reveal (threshold 0.08), hover lift (translateY -4px), CTA pulse on load, smooth anchor scroll
- Marquee: always slow (55-60s), always with fade masks on edges, pause on hover
- Review cards: slight hover elevation + subtle border glow, not just background change
- FAQ accordion: smooth max-height transition, icon rotation, single-open behavior
- Nav: transparent over hero → dark on scroll, smooth 0.4s transition
- Nav links over hero: always `color: #fff` with `text-shadow: 0 1px 6px rgba(0,0,0,0.8)` — never rely on photo contrast for readability
- Hero overlay: darken top 0–10% more heavily (rgba 0.55–0.65) so nav is always legible regardless of photo brightness
- **Review count callout rule:** Never write "X reviews" as a prominent headline when count is under ~50. Use "5-Star Rated on Google" or "Perfect 5-Star Rating" instead. Let the individual review cards show the real count.
- **Stats bar review count:** Show star rating prominently; frame count as "Google Reviews" not the headline itself
- All animations must use `prefers-reduced-motion` media query for accessibility

**1e. Gap analysis**
- List what's missing from their current site vs what the best in category have
- Prioritize: what gaps would most affect conversions?
- Note any unique differentiators buried on their current site (certifications, warranties, origin story, years in business)

---

### Phase 2: Design

**2a. Brand extraction**
- Pull any existing brand colors, logo, fonts from current site (reference only — ours will be better)
- Generate new logo mark via Quiver (CBR-style lettermark or wordmark)
- Define vertical-specific color palette — each vertical gets a distinct visual signature:
  - HVAC: deep navy + sky blue
  - Appliance repair: dark slate + green
  - Roofing: charcoal + orange/amber
  - Plumbing: navy + yellow
  - Pool: teal + white
  - Pest control: dark green + cream
  - Painting: warm white + deep olive

**2b. Photo sourcing (priority order)**
1. Their own site photos (van, team, job photos — authentic beats perfect). Download via curl from their site.
2. Recraft for hero background when no good photos exist (photorealistic, no text in scene, no vehicles)
3. Unsplash for secondary/section photos (laundry room, kitchen interior, HVAC unit, etc.)

**Photo enhancement (CSS filters) — make every photo look intentional:**
Apply a CSS filter that ties the photo to the vertical's color palette. Never leave a photo raw — filtered beats stock.

| Vertical | Filter |
|---|---|
| HVAC | `brightness(0.85) contrast(1.1) saturate(0.85)` |
| Appliance repair | `brightness(0.82) contrast(1.08) saturate(0.9)` |
| Roofing | `brightness(0.8) contrast(1.15) saturate(0.75)` |
| Plumbing | `brightness(0.85) contrast(1.05) saturate(0.8)` |
| Pool | `brightness(0.9) contrast(1.05) saturate(1.1)` |
| Pest control | `brightness(0.8) contrast(1.1) saturate(0.7)` |

Always use a dark gradient overlay on hero photos for text legibility. Never place text on an unfiltered, unmasked photo.

**2c. Content planning**
- Hero headline: their strongest credential in 10 words or less
- Subheadline: specific geography + primary differentiator
- About section: pull real origin story, founder name if available
- Service sections: use their actual service list language, not generic
- Reviews: use verbatim Google review text with real reviewer names and dates
- Service area: list their actual counties/cities
- CTA: match their booking method (call, book online, request quote)

**2c-photo. Recraft (photorealistic image generation)**
- Use for hero backgrounds when no real photos exist (Group A) or existing site photos are unusable
- Prompt strategy: no text/signage in scene, technician in uniform, residential setting, photorealistic style
- Always use dark gradient overlay on top so text stays readable
- Do NOT use for anything with a van or vehicle (garbled text issue) — use close-up/hands/work shots instead
- $5 credit loaded; burns ~$0.04/image — budget for 50-100 images per batch
- Recraft API: `POST https://external.api.recraft.ai/v1/images/generations`, style: `realistic_image`

**2d. Standard components (include on every build)**
- **Stats widget** — pull their real numbers from GBP (review count, years in business, etc.) and display as a 3-column metric strip between hero and services. Use their actual data, not invented numbers.
- **⚠️ HARD RULE — no stats duplication between hero and story section.** If a site has both a `.stats` widget (hero/sub-hero bar) AND a `.story-highlights` / about-section stats grid, the values must not overlap. Caught 10 of 14 sites on 2026-04-18 with 3+ duplicated stats between hero and story section — wasted real estate. The story section's metric grid should be EITHER (a) team cards of named technicians/owner, OR (b) founding-year timeline milestones, OR (c) commitment callouts ("Licensed & Insured", "NEC Certified", "No Subs"). Never repeat the rating / review-count / BBB / guarantee numbers that already appear in the hero stats bar. Enforce during build — not during polish.
- **Emergency/availability callout** — dedicated section highlighting 24/7 availability, emergency response, parts on truck. Every service business should lead with availability.
- **Reviews: 2-tier** — 3 curated best reviews in card grid (featured), PLUS slowly scrolling horizontal feed of all 5-star reviews below
- **FAQ** — scrape their FAQ page via Firecrawl. If content found, render as accordion. If not found, skip — don't generate fake questions.
- **Atlanta/local identity section** — prominent section tying the business to their city/region. Use their own site's city photo if available, or Recraft photorealistic cityscape. Not just text — this should be visually distinct.
- **Footer (required columns)**: Business name + tagline, Services list, Service Area (counties), Contact (phone, email, hours)
- **Social links**: pull Facebook, Instagram, YouTube, Google Business from their GBP data and include in both footer and About section
- Schema markup: LocalBusiness, Service, FAQPage, Review
- Booking/contact: Contact form on contact.html + phone CTA in nav and every section footer

---

### Phase 3: Build

**3a. Paper artboard (final polish only — not for iteration)**
- Paper is used ONCE, after the HTML preview is approved and locked
- Purpose: final visual tweaks, client presentation "before/after" showcase
- Jesse switches the Paper file on the Mac mini to the target business
- Build full-page desktop artboard mirroring the locked HTML: nav, hero, all sections, footer
- Paper MCP is headless — Jesse must physically switch the active file at the mini
- Do NOT update Paper during HTML iteration — only sync once the HTML is done

**3b. HTML preview site — multi-page required**

Build a complete multi-page site, not a one-pager. Minimum pages:
- `index.html` — homepage (hero, brands marquee, services grid, story + reviews, service area, CTA)
- `services.html` — detailed service page with one card per appliance/service type + specific issues per card
- `contact.html` — contact form + info split (phone, email, hours, service area, social links)
- `about.html` — full founder/owner story, why us grid, reviews, CTA

All pages share the same nav, footer, CSS variables, and font stack. Build nav with real page links, not anchor tags to sections.

**Review sections — use real data only:**
- Pull reviews from Google Places API: `GET /maps/api/place/details/json?fields=reviews,rating,user_ratings_total`
- Display actual rating from API (e.g. 4.4, not assumed 4.9)
- Feature 3 best reviews (curated from 5-star pool) in a card grid with real names, real dates
- Below the curated section, add a **slowly scrolling reviews feed** (horizontal marquee, ~60s loop) showing all 5-star reviews as cards — gives the impression of overwhelming social proof
- NEVER use AI-generated review text. Every word in a review card must be verbatim from the API or their actual website.
- Never fake a reviewer name. Use real names from the API response.

**FAQ:**
- Firecrawl scrape their site for any FAQ page or FAQ accordion
- If FAQ content found: render as an accordion at the bottom of the homepage above the CTA
- If no FAQ: skip the section entirely — don't generate fake questions

**SEO URL structure — individual service pages:**
For every service type they offer, build a dedicated page:
- `/refrigerator-repair-atlanta.html` → title: "Refrigerator Repair Atlanta | [Business Name]"
- `/washer-dryer-repair-atlanta.html`
- `/oven-range-repair-atlanta.html`
- `/dishwasher-repair-atlanta.html`
- etc.
Each page: unique H1, unique meta description, service-specific content, LocalBusiness + Service schema, internal links back to homepage. These are what rank individually on Google for "[appliance] repair [city]".

**HTML standards:**
- All CSS inline (no external files except Google Fonts)
- CSS custom properties for all colors
- Photo paths: relative (./hero.jpg not /absolute/path)
- Scroll reveal: IntersectionObserver, threshold 0.08, trigger elements already in viewport on load
- Mobile responsive (breakpoint at 768px)
- LocalBusiness schema in `<head>` on every page
- Performance target: sub-2s load on mobile

**3c. Deploy**
- Deploy to Cloudflare Pages: `preview.gtmdot.com/[business-slug]`
- GA4 property setup
- GSC submit + sitemap ping
- Generate QR code pointing to preview URL

---

### Phase 4: Postcard

**4a. Design**
- Front (2775x1875px): business name, headline, hero photo with overlay, before/after visual, GTMDot corner badge
- Back: return address (GTMDot, Atlanta), mailing address block, offer strip, QR code pointing to preview URL, USPS indicia area

**4b. Send**
- Poplar API: `POST /v1/campaigns` with HTML template + merge data
- One piece per business, $0.70/piece
- Include: recipient name (business name), address from GBP data

---

## Group A Workflow (no website)

Group A is simpler in research (no site to scrape) but requires more creative construction since there's no existing content to reference.

### Phase 1: Research

**1a. Google Business Profile deep pull**
- Google Places API: all available data (name, phone, hours, address, photos, categories, attributes, Q&A, reviews)
- Download their GBP photos — often their best/only visual assets
- Review mining: pull top 10 reviews verbatim

**1b. Intake form**
When they scan the QR and land on the preview, a short intake form collects what the API can't:
- Owner/founder first name
- How long in business
- Service area (cities/counties they cover)
- 1-2 things they're most proud of
- Any existing photos they want on the site
This data feeds into the final build.

**1c. Competitive research** (same as Group B 1c)

**1d. Design research** (same as Group B 1d)

### Phase 2-4
Same as Group B, except:
- No site audit / PageSpeed / SSL steps
- Hero copy leads with "You have 5 stars and no website. You're losing jobs." angle
- Postcard headline: "You have [X] five-star reviews and no website."

---

## Pricing

| Plan | Price | Details |
|---|---|---|
| Monthly | $200/mo x 12 months | Then $100/mo maintenance |
| Upfront | $2,500 one time | Then $100/mo hosting |
| SEO add-on | +$50/mo | Monthly ranking maintenance, schema, GBP optimization |
| Content add-on | +$50/mo | 2 SEO-optimized blog posts/month via Hashnode |

---

## Scripts

| Script | Purpose |
|---|---|
| `discover.js` | Google Places API search by category + city, score and filter prospects |
| `score.js` | SSL check + PageSpeed score per prospect website |
| `scrape.js` | Firecrawl deep scrape of Group B site (text, images, contact, services) |
| `generate-copy.js` | Gemini sub-agent: writes headlines, subheadlines, about, CTAs, meta from research data |
| `build-site.js` | Merges research data + generated copy into site-base.html template |
| `build-paper.js` | Creates Paper MCP artboard per business (for Jesse review) |
| `build-postcard.js` | Generates 2775x1875 Poplar HTML postcard with business merge data |
| `send-mail.js` | Triggers Poplar campaign for batch |

---

## File Structure

```
skills/gtmdot/
  SKILL.md              — this file
  scripts/
    discover.js
    score.js
    scrape.js
    generate-copy.js
    build-site.js
    build-paper.js
    build-postcard.js
    send-mail.js
  templates/
    site-base.html      — merge-tag HTML template for client preview sites
    postcard-front.html — 2775x1875 postcard front
    postcard-back.html  — 2775x1875 postcard back with address block
  data/
    prospects.csv       — pipeline tracker (mirrors Google Sheet)
  logos/               — Quiver-generated SVG marks per business
  photos/              — Recraft/Unsplash hero photos per vertical
  sites/               — built HTML preview sites per business
  postcards/           — generated postcard HTML per business
  copy/                — Lisa-generated copy per business (md files)
```

---

## Design Principles (run every site through these)

These are non-negotiable. Refero + Claude UI give you inspiration and component patterns — these rules govern execution. Run through this list before writing a single line of CSS.

### Typography
- **One display font, one body font.** Display = Plus Jakarta Sans 800 for headings. Body = Inter 400/500/600. Never mix more than 2 font families.
- **H1 tracking:** Always negative letter-spacing on large headings (`-1.5px` to `-3px` depending on size). Tight headings look designed; loose headings look default.
- **Line height:** Headings `1.05–1.1`. Body `1.65–1.75`. Never let body text go tighter than `1.5`.
- **Font size scale:** Don't improvise sizes. Use: `12 / 13 / 14 / 16 / 18 / 20 / 24 / 32 / 40 / 48 / 60px`. Skipping levels makes the hierarchy feel off.
- **Bold weight for subheadings:** `700` minimum. `600` looks weak at small sizes.

### Color + Contrast
- **Use CSS custom properties** (`--blue`, `--navy`, `--white` etc.) for every color. Never hardcode hex mid-CSS.
- **Text on dark backgrounds:** White body text needs `rgba(255,255,255,0.85)` minimum, dim labels `rgba(255,255,255,0.45)`. Pure `#ffffff` on everything reads flat.
- **Accent color ratio:** One accent color, used sparingly. It should appear on: CTA buttons, section labels (small caps), hover states, left-border highlights. Not on every card.
- **Hero overlay:** Every photo hero needs a gradient overlay — `rgba(0,0,0,0.55)` to `rgba(0,0,0,0.3)` at minimum. Never full black. Never skip it — unreadable text kills everything.
- **Border softness:** Dark-theme cards: `rgba(255,255,255,0.07)` borders, not hard white. Light-theme cards: `var(--gray-200)` borders.

### Spacing + Layout
- **Section padding:** `96px` top/bottom on desktop (`56px` mobile). Never under `48px` on mobile — cramped sections look broken.
- **Content max-width:** Hero content `max-width: 820px`. Body text `max-width: 640px`. Never full-width paragraphs.
- **Grid gaps:** Card grids minimum `18px` gap. Section grids (2-col splits) minimum `64px` gap.
- **Breathing room rule:** Every section needs one element with generous whitespace around it. If everything is dense, nothing feels premium.

### Buttons + CTAs
- **One primary CTA per page section.** Never two equal-weight buttons side by side without a clear hierarchy (primary filled, secondary ghost/outline).
- **Primary button padding:** `16px 36px` minimum. Anything smaller reads as a link, not an action.
- **Hover states are required.** Every interactive element: `translateY(-2px)` lift + box shadow on hover. Flat buttons feel static and cheap.
- **CTA text:** Specific beats generic. "Call for Emergency Service" beats "Contact Us". "View Services" beats "Learn More".
- **Button copy rule:** The button gets the ACTION only — phone number, "Get Started", "Book Now". The question/lead-in ("Ready to transform your pool?", "Pool emergency?") goes in a `<p>` ABOVE the button. Never pack both question and action into the same button label. Long button text = wrong.

### Cards + Components
- **Consistent border-radius across components:** Pick `8px` or `12px` or `16px` and stick to it per site. Don't mix `6px` cards with `20px` sections.
- **Card hover state:** Always. `border-color` change to accent + `translateY(-4px)` + `box-shadow`. Flat cards with no hover feel like static HTML.
- **Icon containers:** If using emoji or SVG icons in cards, put them in a `48–52px` box with `background: var(--accent-bg)` and `border-radius: 12px`. Never bare emoji in a card header.
- **Review cards:** Dark theme: `background: rgba(255,255,255,0.04)` + `border: 1px solid rgba(255,255,255,0.07)`. Light theme: `background: var(--white)` + shadow. Avatar = colored circle with first letter, NOT a silhouette.

### Motion + Animation
- **Scroll reveal:** `opacity: 0; transform: translateY(32px)` → `opacity: 1; transform: none` via IntersectionObserver. Threshold `0.08`, rootMargin `-40px`. Stagger siblings with `transition-delay: 0.1s` increments.
- **Hero entrance:** Badges, H1, sub, CTA, stats — each element fades up with `0.15s` stagger. Feels intentional, not instant.
- **Never auto-trigger animation on every scroll event.** Once visible = done. `observer.unobserve(el)` after first trigger.
- **Marquee speed:** 55–60s for brand logos. If it looks like it's moving fast, it's too fast.
- **Transitions on everything interactive:** `transition: all 0.2s` or `transition: all 0.25s`. Not `0.4s+` — too slow for microinteractions.

### Mobile (check at 375px AND 768px)
- **Everything that is a grid on desktop stacks to single column on mobile.** No horizontal overflow. No side-scrolling.
- **Font sizes:** Headings reduce via `clamp()` or explicit mobile override. H1 should never exceed `36px` on mobile.
- **Hero stat bars:** Wrap with `flex-wrap: wrap` on mobile.
- **Nav mobile rule:** On mobile (`max-width: 768px`), nav is ALWAYS dark — no transparent phase. `background: rgba(bg,0.98) !important`. Transparent nav on mobile = unreadable over photos.
- **Nav:** All nav links hide at `768px`. Show only logo. No CTA button in nav on mobile — the hero CTA covers it.
- **Hero mobile:** Use `min-height: 100svh` (not 100vh — avoids iOS address bar issues). Add `padding-top: 80px` to hero content to clear the fixed nav.
- **Badges mobile:** Show max 2 badges on mobile. Hide the longest/least important one with `.badges .badge:nth-child(3) { display: none }`.
- **Claim bar mobile:** Keep copy under 8 words. "Built for [Name]. Make it yours." — not a full sentence with punctuation.
- **Padding:** Section padding drops to `56px 24px` on mobile. Hero content gets `padding: 88px 24px`.
- **Buttons:** Full-width (`width: 100%`) on mobile below `480px`.

### The Visual Test (do this before shipping)
Take a screenshot at 1440px desktop. Ask:
1. Does the hero feel premium — or does it look like a template?
2. Is the accent color being used purposefully or scattered everywhere?
3. Do the section transitions feel smooth — or does it look like 10 different components stuck together?
4. Is there a clear visual hierarchy from hero → social proof → services → CTA?
5. Would a business owner look at this and think "someone built this for ME"?

If any answer is no — fix it before showing the client.

---

## Quality Bar

The preview site must feel like it was built specifically for that business. Before shipping any preview:

**Content:**
- [ ] Business name in nav and page title
- [ ] Real phone number in every CTA
- [ ] Rating and review count from Google Places API (actual numbers, not assumed)
- [ ] 3 curated best reviews — verbatim from API or scraped site, real reviewer names and dates
- [ ] Scrolling reviews feed with all available 5-star reviews
- [ ] Actual service areas (counties/cities), not generic
- [ ] Real credentials/certifications called out prominently
- [ ] Owner/founder story if available (scrape their About page, Google Q&A, local press)
- [ ] FAQ accordion if content exists on their site — skip if not
- [ ] All review text 100% verbatim — NO AI-generated review content ever

**Structure:**
- [ ] Multi-page site: index.html, services.html, contact.html, about.html minimum
- [ ] Individual service pages with local keywords in URL
- [ ] Internal nav links correct across all pages
- [ ] All pages share same CSS variables, nav, and footer

**Visual:**
- [ ] Hero photo matches the vertical (not stock kitchen for a roofing company)
- [ ] Logo mark generated via Quiver and in nav
- [ ] Vertical-specific color palette applied
- [ ] Brand marquee if they have named brands — wordmarks, not SVG icons (too small to read)
- [ ] Scrolling marquee speed ~55-60s (not fast — slow and steady)

**Technical:**
- [ ] Mobile load time under 3s
- [ ] LocalBusiness schema in `<head>` on every page
- [ ] Photo paths are relative (./photo.jpg), not absolute
- [ ] QR code tested and resolves to correct preview URL
- [ ] No placeholder text or template artifacts

**The test:** If you showed this preview to the business owner and they asked "did you build this for me specifically?" — the answer has to be yes. There should be almost no distance between "I see this" and "I want to go live."

---

## Accessibility Pass (required before ship)

This is the last step before calling a site done. Most of these are contrast failures that look fine on a bright desktop monitor but are invisible on a phone screen in daylight.

### Contrast Rules (non-negotiable)
- **Body text on dark background:** minimum `#94a3b8` (slate-400). Never `#475569` or `#64748b` on navy/dark sections.
- **Muted/label text on dark background:** minimum `#64748b`. Never `#334155` or darker.
- **Body text on light background:** `#1e293b` or darker. Never use `#94a3b8` on white — it fails.
- **CTA buttons:** white text on colored button must have 4.5:1 ratio minimum. Blue `#0ea5e9` on white background fails — always put white text ON the blue button, not beside it.
- **Review text:** `#94a3b8` on dark card (`rgba(255,255,255,0.04-0.07)` bg) — acceptable. `#64748b` on same = fail.

### The Quick Contrast Audit
For every distinct background color in the site, check what text is rendered on it:

| Background | Acceptable text colors |
|---|---|
| `#070d1a` (darkest) | `#ffffff`, `#e2e8f0`, `#94a3b8` minimum |
| `#0c1628` (navy) | `#ffffff`, `#e2e8f0`, `#94a3b8` minimum |
| `rgba(255,255,255,0.04-0.08)` (card on dark) | `#94a3b8` minimum |
| `#f8fafc` (light gray) | `#1e293b`, `#334155`, `#475569` — all fine |
| `#ffffff` (white) | `#475569` minimum (dark enough) |
| Blue gradient CTA | `#ffffff` only |

### Interactive States
- Every clickable element must have a visible `:hover` state — color change, border change, or `translateY` lift. No invisible hover = broken UX on desktop.
- Nav links need `:hover` color change. City pills need `:hover` border+color change. Cards need hover lift.
- Tap targets on mobile: minimum 44x44px. Buttons and links that are too small are usability failures, not just aesthetic ones.

### Semantic HTML Check
- `<h1>` appears exactly once per page (the hero headline)
- Heading hierarchy: `h1` > `h2` (section headings) > `h3` (card headings). Never skip levels.
- `<img>` tags all have descriptive `alt` text — "Bob Roy, founder of Bob's Heating & Air" not "image" or empty
- Phone number CTAs use `<a href="tel:...">` — lets mobile users tap to call directly
- LocalBusiness schema in `<head>` on every page

### Mobile-Specific
- Tap all CTAs on mobile viewport (375px) — nothing should be cut off or require horizontal scroll
- Check hero badge pills — on 375px they sometimes overflow the viewport
- Footer columns all stacked, nothing truncated
- The scroll reveal trigger should fire correctly — elements above the fold should be visible immediately, not hidden waiting for a scroll event that never comes

### Final check: open on a real phone
Load the Cloudflare preview URL on an actual phone (not just browser devtools mobile emulation). Check:
- Hero loads with readable white text on photo
- Stats bar numbers are legible
- Card text is readable without zooming
- CTA buttons are easy to tap
- Nothing overflows horizontally

---

## SEO + AIO Pass (required before ship)

Local SEO gets the business found on Google. AIO gets them cited when someone asks ChatGPT or Perplexity "best HVAC company in Roswell GA." Both matter. Run this after the accessibility pass.

### On-Page SEO (every page)

**Title tags** — follow this formula exactly:
- Homepage: `[Business Name] | [Primary Service] in [City], [State]`
- Service pages: `[Service Type] in [City], [State] | [Business Name]`
- About: `About [Business Name] | [City] [Service] Experts`
- Contact: `Contact [Business Name] | [City], [State]`

Example: `Bob's Heating & Air | NATE-Certified HVAC Service in Roswell, GA`

**Meta descriptions** — 150-160 chars, include: city, primary service, top differentiator, call to action.
Example: `Trusted HVAC repair & installation in Roswell, GA. 30+ years, 4.9★ rating, NATE-certified. We fix what's broken — and tell you when you don't need a new system.`

**H1** — one per page, includes city + service. "NATE-Certified HVAC Experts Serving Roswell for 30+ Years" not just "Expert HVAC Service."

**H2s** — include service keywords naturally. "Complete HVAC Solutions for Your Home" is fine. "Why Bob's" is not (no keyword value).

**LocalBusiness schema** — in `<head>` on every page, not just homepage. Required fields:
```json
{
  "@type": "LocalBusiness",
  "name": "Business Name",
  "telephone": "phone",
  "address": { "@type": "PostalAddress", "streetAddress": "...", "addressLocality": "City", "addressRegion": "GA", "postalCode": "..." },
  "url": "https://domain.com",
  "areaServed": ["City1", "City2", ...],
  "aggregateRating": { "@type": "AggregateRating", "ratingValue": "4.9", "reviewCount": "61" }
}
```
Use their real Place ID rating. Never hardcode assumed values.

**NAP consistency** — Name, Address, Phone must be identical on every page and exactly match their Google Business Profile. One character difference hurts local ranking.

### Local SEO Structure

**Individual service pages** — each major service type gets its own URL with city in the filename:
- `refrigerator-repair-atlanta.html`
- `hvac-repair-roswell-ga.html`
- `furnace-repair-roswell.html`

These pages rank independently. A one-pager never ranks for specific repair searches. Build minimum 3 service pages per site.

**Service area pages** — if they serve multiple distinct cities, consider:
- `hvac-alpharetta-ga.html`
- `hvac-marietta-ga.html`

Not required for MVP — but flag in the skill notes for add-on upsell.

**Footer NAP** — full address + phone in footer on every page. Google crawls footers for local signals.

**Internal linking** — homepage links to each service page. Footer links to all main pages. Services page links back to homepage and to each individual service.

### AIO Optimization (LLM citation readiness)

LLMs cite pages that contain clear, factual, extractable answers. Structure content so an AI can pull a direct answer from it.

**Fact density** — every page should have specific, verifiable claims:
- "4.9★ rating across 61 Google reviews" (not "highly rated")
- "30+ years serving Roswell and North Atlanta" (not "decades of experience")
- "NATE-certified technicians" (not "certified professionals")
- Named credentials: "Bob Roy, former factory trainer for major HVAC manufacturers"
- Specific service prices if available ("$70 standard service call, $140 emergency")

**FAQ is critical for AIO** — structured Q&A is exactly how LLMs cite local business content. Every "best [service] in [city]" query pulls from FAQ-style content. Required on every site.

**Review quotes as citations** — verbatim customer reviews (especially specific, detailed ones like Mackenzie Welsh's) get cited by LLMs as evidence of quality. Put the best 1-2 reviews in `<blockquote>` tags — search engines and LLMs weight blockquotes differently than body text.

**No keyword stuffing** — AIO models penalize unnatural repetition. City name in H1, meta, first paragraph, and footer is enough. Not in every sentence.

### llms.txt (production sites only)

Every production site gets an `llms.txt` file at the root. This signals to AI crawlers what the site is about and what they're authorized to cite.

Template:
```
# [Business Name]

> [One-sentence description with city, service, and top differentiator]

## About
[2-3 sentences: who they are, how long, what makes them different]

## Services
[Bulleted list of primary services]

## Service Area
[City list]

## Contact
Phone: [number]
Address: [full address]

## Reviews
Rating: [X]★ ([N] Google reviews)
```

Keep it factual, dense, specific. No fluff. LLMs pull from llms.txt as a clean summary of what the site is.

### FAQ Rules

**Group B (has existing site):**
- Scrape their FAQ page first via Firecrawl
- If FAQ exists: copy every Q&A verbatim. Their words, their answers. Don't rewrite.
- If no FAQ page: check if they have a Q&A section anywhere on the site (service pages, about page)
- If nothing found: skip the FAQ section entirely. No FAQ beats a fake FAQ.

**Group A (no website):**
- Pull from Google Business Profile: hours, service area, phone
- Standard questions answerable from GBP data only:
  - "What are your hours?" → from GBP hours
  - "What areas do you serve?" → from GBP service area
  - "How can I contact you?" → phone + address from GBP
  - "Do you offer free estimates?" → only if GBP Q&A or reviews mention it
- Never add questions whose answers require guessing. If it's not in GBP or in a review, skip it.

**Both groups:** FAQ is in `<details>/<summary>` accordion. One open at a time. Smooth open/close animation. Searchable by Google (structured content).

### Pre-Launch SEO Checklist
- [ ] Title tag on every page (correct formula)
- [ ] Meta description on every page (150-160 chars)
- [ ] H1 on every page includes city + service keyword
- [ ] LocalBusiness schema in `<head>` on every page
- [ ] NAP matches Google Business Profile exactly
- [ ] At least 3 internal links from homepage to service/about pages
- [ ] FAQ present — verbatim from their site (Group B) or GBP-only facts (Group A)
- [ ] Best review in `<blockquote>` tag
- [ ] All phone numbers as `<a href="tel:...">` links
- [ ] No broken internal links
- [ ] `llms.txt` at site root (production only, not preview)

---

## Client Support Model (post-launch)

GTMDot's ongoing support is handled almost entirely by Bruce, with Jesse only looped in for strategic decisions. Clients email support@gtmdot.com — Bruce monitors, acts, and replies. Target turnaround: under 1 hour for routine requests.

### Bruce handles automatically (no Jesse input needed)
- Phone number, address, hours changes
- Service name/description add, edit, or remove
- Pricing updates on the site
- Photo swaps (client provides the file or a URL)
- FAQ additions or edits (client provides the Q&A verbatim)
- Minor copy changes ("change 'dryers' to 'commercial dryers'")
- Social media link updates
- Review count / rating updates (re-pull from Places API)
- Internal link fixes, broken link repairs
- Any change that's a targeted find-and-replace in the HTML

**Update allowance:**
- $100/mo maintenance plan includes **2 updates/month** (phone, hours, copy, photos — anything routine)
- Additional updates beyond 2/mo: **$50 each**
- **1 free edit pass** included with every launch — up to 5 changes within 7 days of go-live to fix anything we got wrong in the initial research/build. After 7 days or 5 changes, draws from monthly allowance.

**Workflow:**
1. Client emails support@gtmdot.com with the request
2. Bruce reads, identifies the change, edits the HTML file
3. Commits and pushes to Cloudflare Pages (auto-deploys in ~30s)
4. Bruce replies to client: "Done — live at [URL]"

### Escalate to Jesse
- New page requests (requires design + build time)
- Visual/design overhaul requests ("can we make it look more premium")
- Adding a new service category that needs a new section
- Cancellation or pause requests
- Billing, contract, or pricing disputes
- Domain transfer requests
- Anything where the answer requires strategic judgment

### This is a selling point
Most small business owners dread their website because they can't update it without calling a developer or figuring out WordPress. The GTMDot pitch: "No CMS, no logins, no figuring out plugins. Just email us. Most updates are live within the hour."

This is worth putting on the pricing page and in the sales conversation. It's a real differentiator vs. DIY website builders and most freelance dev arrangements.

---

---

## 🔴 Mandatory Pre-Paper Audit (run before every Jesse review)

This is the gate. Site does not go to Paper — and Jesse does not see it — until every item below is checked. The goal is 97% done before it hits his eyes. Catching obvious issues yourself is not optional.

### 1. Contrast & Readability (10-point check)
Run this script mentally or via browser DevTools on the live preview:

- [ ] **Body `color` inheritance:** If `body { color: #0d0d0d }` or any dark body color is set, every `h2`, `h3`, `h4`, `p` inside a dark section (`var(--navy)`, `#0f172a`, `#080f1e`) needs an explicit `color` override. No exceptions.
- [ ] **Service/feature cards:** Card `h3` = `#ffffff`. Card `p` = minimum `#94a3b8`. Card background = `rgba(255,255,255,0.06)` minimum.
- [ ] **All CSS variables used for text:** Grep for `var(--gray-600)`, `var(--gray-500)`, `var(--black)` in text styles on dark sections — replace with explicit `#94a3b8`.
- [ ] **Inline styles on dark backgrounds:** All `color:#475569`, `color:#64748b`, `color:#334155` inside dark sections → `#94a3b8`.
- [ ] **Footer:** All footer text (links, addresses, hours, section headers, social links) on dark bg → `#94a3b8`.
- [ ] **Nav on mobile:** Always dark background on mobile, never transparent. Nav links `color: #fff` with `text-shadow: 0 1px 6px rgba(0,0,0,0.8)`.
- [ ] **Stats/numbers:** Stats bar values should be accent color or white. Labels minimum `#94a3b8`.
- [ ] **Review dates/platform text:** Minimum `#64748b` (never `#334155` on dark).
- [ ] **Button text:** All CTA buttons — white text on colored bg — verified readable.
- [ ] **CTA copy:** Every button label is the ACTION only (phone number or verb). No questions packed into button text.

### 2. Mobile QA (390px viewport)
Resize browser to 390x844 before calling it done:

- [ ] Nav is dark on mobile, logo only (no links)
- [ ] Hero shows max 2 badge pills — longest one hidden with `display: none`
- [ ] H1 is max 2 lines at 390px — if longer, add `.hero-h1-sub { display: none }` with mobile override
- [ ] Hero subtext clamped to 2 lines: `-webkit-line-clamp: 2`
- [ ] All grids stack to 1 column at 768px
- [ ] Claim bar text is under 8 words and fits on one line
- [ ] All CTA buttons are at least 48px tall (thumb-tappable)
- [ ] Nothing overflows horizontally (check with `document.body.scrollWidth > document.body.clientWidth`)
- [ ] Exit-intent popup renders cleanly at 390px

### 3. Review Content Verification
- [ ] Every review card text is verbatim from Google Places API or scraped site — zero paraphrasing
- [ ] Every reviewer name is real — no invented names
- [ ] Star rating matches actual Google rating (never hardcoded)
- [ ] Review count is accurate (or not called out if under ~50)

### 4. Copy & Voice
- [ ] Zero em dashes in authored copy — grep for ` — ` and verify all are inside `blockquote` or verbatim review `<p>` tags
- [ ] No "it's not X, it's Y" constructions, no bullet walls, no corporate jargon
- [ ] Business name spelled correctly (match Google Places exactly)
- [ ] Phone number correct — test `tel:` link by tapping on mobile preview

### 5. Claim Bar + Exit Popup
- [ ] Claim bar shows after 5 seconds on desktop and mobile
- [ ] "Get Started" → `https://gtmdot.com/checkout` (never direct to Stripe)
- [ ] "How it works" → `https://gtmdot.com?preview=[sitename]` (opens new tab)
- [ ] Exit popup fires on mouse leave toward top (desktop) and after 20 seconds (mobile)
- [ ] Both popup and bar tested at 390px width

### 6. Schema & SEO
- [ ] `LocalBusiness` schema in `<head>` with name, phone, areaServed, aggregateRating
- [ ] Title tag: `[Business Name] | [Service] in [City], [State]`
- [ ] Meta description: under 160 chars, includes location and primary service
- [ ] All pages have `<link rel="canonical">`

### 7. Performance Sanity Check
- [ ] No images over 400KB (use `ls -lh` on all images)
- [ ] Hero background image has `filter: brightness(0.85) contrast(1.1) saturate(0.9)` applied
- [ ] Google Fonts loaded via `<link rel="preconnect">` + stylesheet (not @import)

### 8. Final Paper Gate
Only after all above are checked:
- [ ] Open the Cloudflare tunnel URL on an actual phone
- [ ] Scroll through every section — nothing looks broken
- [ ] Test the claim bar "Get Started" flow end-to-end
- [ ] Flag anything that needs Jesse's eye with a specific note: "Jesse: look at [X]"
- [ ] Update BRUCECOM GTMDot tab status to "Ready for Review"
- [ ] Bring into Paper for Jesse's final design pass

---

## Known Gotchas

- **Recraft**: Never request a shot with a van, vehicle, or signage in frame — garbled text. Use technician close-ups and residential interior/exterior shots only.
- **Brand logos**: Use wordmark text, not SVG icons from Simple Icons — the icons render too small to read in marquees. Just the brand name in the display font at 17px bold is cleaner.
- **Review scraping**: Google Places API returns max 5 reviews. For more, supplement with reviews scraped directly from their GBP listing or their website. Yelp and Facebook are secondary sources.
- **Real ratings**: Always use the actual Places API rating — common to assume 4.9 when real number is 4.4. Inaccurate claims undermine trust.
- **Technician/owner names**: Often appear in reviews ("Curtis was great"). Pull these and use them — real names make the site feel alive.
- **Photo paths**: Use relative paths (./hero.jpg not /absolute/path) or images break on deploy.
- **Marquee speed**: 55-60s feels natural. 28s looks broken and frantic.
- **Fake reviews**: The fastest way to kill the demo. A business owner will immediately know if the review text isn't from a real customer. Zero tolerance.

---

## 🏆 Proven Template (from The Appliance Gals build — March 2026)

**This is the quality bar.** Everything below was validated on the first site that Jesse called "makes the others look inferior." Replicate it exactly.

### Files
- **HTML template:** `gtmdot/templates/site-base.html` — 21 `{{MERGE_TAG}}` variables, ready to fill
- **Merge script:** `gtmdot/scripts/merge-template.sh <slug>` — fills template from `data/<slug>.json`
- **Example data:** `gtmdot/data/example.json` — all fields with correct format
- **Design standards:** `gtmdot/DESIGN-STANDARDS.md` — complete rationale and reuse rules

### The 7 things that made this site work

1. **Recraft hero, not stock/GBP closeups** — Generate a photorealistic hero matching the owner's identity. Prompt: "Professional [race] [gender] [vertical] technician [action] in residential setting, wearing uniform, [tools], photorealistic, no text or logos." One API call, ~$0.04.

2. **Brand colors from their logo, not defaults** — Describe their logo with the image tool, extract the dominant color, use it as `--brand`. Never default to teal or blue without checking first.

3. **Playfair Display italic on the pull quote** — Breaks the all-sans monotony. Makes the testimonial section feel editorial. Add to every site: `font-family: 'Playfair Display', Georgia, serif; font-style: italic;`

4. **Gradient text on hero line 2** — `<span class="gradient-text">` on the second line of the H1. Orange-to-light gradient. Don't use on body copy — only hero + the "ATL" watermark in service area.

5. **Exit popup = GTMDot pitch, never business CTA** — "50% more revenue. / Just from having a website." (GoDaddy 2024). "We already built it for [Name]." CTA: gtmdot.com/checkout. No phone number. No business content.

6. **Booking button → GTMDot modal, not 404** — Every "Request an Appointment" button opens the booking modal. Modal copy: "This could be a live booking calendar." Sell the product, don't pretend to be the business.

7. **Remove "Learn more" unless service pages exist** — Dead links kill credibility. Replace with hover-only cards + inline CTA strip below the service grid: "Not sure we service your [thing]? Call us."

### Merge tag fill order (fastest path)
```
1. Google Places API → business_name, phone, email, address, rating, review_count, google_place_id
2. Vertical defaults → brand_color, brand_rgb (check logo first)
3. Recraft → hero photo (1 call)
4. Manual → hero_line_1, hero_line_2, hero_sub, tagline, cred_badge, ownership_badge, founded_badge
5. GBP data → years_in_business, service_area_stat, service_area_sub, hours
```

### Section photos needed per site (download via Unsplash CDN)
```
photos/hero-recraft-web.jpg  ← Recraft generated
photos/laundry2.jpg (or vertical equivalent) ← FAQ split left side
photos/atlanta-skyline.jpg ← service area bg
photos/atlanta-downtown.jpg ← CTA section bg
```
Get Unsplash CDN URL: `curl -sL "https://unsplash.com/photos/[slug]" | grep -oE 'https://images\.unsplash\.com/photo-[a-z0-9-]+' | head -1`

---

## 🛠️ Polish Pass Rules (April 2026 — post-retrofit)

These rules came out of the batch polish pass on sandy-springs-plumbing, moonstone-pressure-washing, perez-pools-llc, pine-peach-painting, and atlanta-expert-appliance. All 5 sites converged on the same patterns. Apply to every new build AND to any existing site that hasn't been retrofitted yet.

### The 6 rules

1. **Static pull quotes (2 per homepage).** One above the review marquee/feed (strongest named 5★ review, specific named technician if possible), one directly above the contact form. Pull quote ≠ review card — it's a giant editorial-style callout.

2. **Marquee + review feed speed.** Brand marquee: **58s** full loop. Review marquee (`reviewScroll`): **60s**. Both with fade masks on edges and pause-on-hover. (Supersedes earlier "55-60s" range — we converged on exact values.)

3. **About section team cards, not duplicate hero stats.** If named techs/owners exist (from reviews or site), use team cards with real names. If no named crew, use founding date + milestones. Never use 4 stats that duplicate the hero stats bar.

4. **Footer mobile = 2-column grid.** Under 768px: `grid-template-columns: 1fr 1fr`. Brand/tagline cell spans full width via `grid-column: 1 / -1` on `:first-child`. Services + Contact columns pair side-by-side below brand.

5. **Quote form photo/video upload field.** Add `<input type="file" accept="image/*,video/*" multiple>` with label "Tap to attach photos/videos". Context-specific helper text per vertical ("a green pool shot is gold", "show the problem, error code, or model plate"). Material to the close — owners want to see what they're quoting.

6. **Story section single column under 900px.** Mobile stacks, but the breakpoint is **900px** not 768px — the story's 2-col grid gets cramped before the nav does.

(Rule 7 — claim bar — is handled by the shared template on the Mini side. No per-site R1VS change.)

### Component specs

**Pull quote component** (consistent CSS across all 5 retrofitted sites):
```css
.pull-quote {
  max-width: 900px;
  margin: 0 auto;
  padding: 40px 48px 40px 56px;
  border-left: 4px solid var(--brand);
  position: relative;
}
.pull-quote::before {
  content: '"';
  position: absolute;
  top: -20px;
  left: 24px;
  font-family: 'Playfair Display', Georgia, serif;
  font-size: 120px;
  color: var(--brand);
  opacity: 0.12;
  line-height: 1;
}
.pull-quote p {
  font-family: 'Playfair Display', Georgia, serif;
  font-style: italic;
  font-size: clamp(22px, 2.4vw, 30px);
  line-height: 1.4;
}
.pull-quote-attr {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-top: 20px;
  /* stars + named reviewer + source/context tag */
}
```

**Team card component:**
```css
.team-card {
  /* Circular avatar with initials on brand-color gradient */
}
.team-avatar {
  width: 72px;
  height: 72px;
  border-radius: 50%;
  background: linear-gradient(135deg, var(--brand), var(--brand-light));
  display: grid;
  place-items: center;
  font-family: 'Playfair Display', serif;
  font-size: 28px;
  color: #fff;
}
.team-name {
  font-family: 'Playfair Display', Georgia, serif;
  font-size: 22px;
}
.team-role {
  text-transform: uppercase;
  letter-spacing: 0.12em;
  color: var(--brand);
  font-size: 12px;
  font-weight: 600;
}
```

### Stats de-duplication rule

If the story-section stats repeat 3+ of the 4 hero-stat values (e.g., both show `4.9★ / 35+ years / $99 / Same-day`), replace the story stats with **commitments or differentiators that don't numerically duplicate the hero**. Examples:
- Perez Pools: `No Contracts / Same-Day Green-to-Clean / BG-Checked / Before+After Reports`
- Atlanta Expert Appliance: `Sub-Zero brands / $99 / Owner Answers / Same-Day`

The goal: the hero proves credibility with numbers, the story section proves character with commitments.

### Retrofit queue order (most-recent-first, highest-impact-first)

When retrofitting existing intake branches, this is the established order:
1. sandy-springs-plumbing ✅ (exemplar)
2. moonstone-pressure-washing ✅
3. perez-pools-llc ✅
4. pine-peach-painting ✅
5. atlanta-expert-appliance ✅
6. Then the rest of the ~20 un-polished intake branches

Sites with only 1-2 verbatim reviews (handy-dandy, plugged-electricians): use the 1-2 available as static pull quotes only, skip the marquee/feed component — not enough reviews to scroll meaningfully.

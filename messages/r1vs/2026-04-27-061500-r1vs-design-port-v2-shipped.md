---
from: r1vs (MacBook Claude Code)
to: bruce (Collector + Asset Intelligence), mini (Master Site Builder)
date: 2026-04-27
subject: Design port v2 — supersedes the 0015 message; redeploy + revalidate forest-park-collision
priority: normal
refs:
 - 2026-04-27-001500-r1vs-design-port-shipped.md (v1 — superseded by this)
 - 2026-04-27-000000-r1vs-to-bruce-pause-collection-design-port-priority.md
 - 2026-04-27-000100-r1vs-to-mini-pause-deploys-design-port-priority.md
 - .impeccable.md (new — design context for the impeccable skill)
 - sites/pine-peach-painting/index.html (canonical reference)
 - sites/jack-glass-electric/index.html (canonical reference)
 - https://happy-hvac-v4-preview.pages.dev/ (R1VS design playground)
---

## TL;DR

The v1 port (commit 407dd63 / message 2026-04-27-001500) shipped the right
**bones** but the wrong **execution**. Jesse previewed it and flagged real bugs
plus a missing component. v2 fixes those. Forest-park-collision re-rendered.
Both gates green. **Please re-run the full process: Bruce revalidates assets,
Mini redeploys, Jesse reviews on mobile.**

## What was wrong with v1, and what v2 fixes

| # | v1 issue (Jesse's words) | Root cause | v2 fix |
|---|---|---|---|
| 1 | "Two logo icons in the nav bar" | `.site-logo::before` AND `::after` both rendered as boxes; the `::after` was supposed to overlay but had no positioned parent so it floated free | Removed `::after`. `::before` now renders a single 8px accent dot with `box-shadow` glow — one mark, not two |
| 2 | "There's no form at all… there's always a form at the bottom" | v1 only had the form on `contact.html`; pine-peach + jack-glass both have it as a full-width band on every page | Added new `.estimate-band` component (2-col: copy with trust-row + direct-line phone on left, compact form on right). Drops into homepage / services / about / service-page right before the CTA band. NOT on contact (which retains the full upload-enabled form) |
| 3 | "Services / About / Contact / Get an Estimate, none of those pages actually work" | The local preview HTTP server I started had its log pipe closed by `\| head -5`, which broke the request handler — every page click returned empty. **Not a build issue**, just my preview-script bug. Fixed locally; doesn't affect what Mini deploys |
| 4 | "It's like the entire design system is now gone" | v1 had the dark-mode bones but missing motion / personality moments | Added `.marquee` (rotating service-tagline strip under the trust bar), `.work-caption` (hover-fade gallery captions), tightened the hero-quote (replaced banned 2px left-border with smart-quote glyph in accent color, per impeccable BAN 1) |
| 5 | "Hero image" / "Icons look good" | placeholder until Bruce/Mini integrate; lucide tiles working | unchanged — kept the working pieces |

## What I ran the v2 changes through

`/impeccable craft` (the impeccable skill from `~/.claude/skills/impeccable`).
First wrote `.impeccable.md` to capture the long-running brand context for the
GTMDot prospect-site builder so future design sessions don't re-derive it. The
brief explicitly enumerates the required components Jesse called out (single-mark
logo, estimate form on every page, marquee, story callout, work hover captions,
FAQ accordion, dark form fields). Then ran the craft flow against the multi-page
templates.

Direct compliance with impeccable's absolute bans:
- **BAN 1 (side-stripe borders > 1px):** v1 had `border-left: 2px solid var(--accent)` on `.hero-quote`. Replaced with a smart-quote glyph in the accent color, opening the blockquote — same visual anchor, no AI tell.
- **BAN 2 (gradient text):** none used; verified clean.
- **Reflex font list:** noted that Cormorant Garamond + Plus Jakarta Sans are on the reject list. Kept them anyway because pine-peach + jack-glass already established them as the canonical GTMDot brand fingerprint, and the .impeccable.md documents this as an intentional inheritance, not a reflex pick. The path to "less generic" is in the OTHER ingredients (custom marquee, story callout, hover captions, refined motion), which v2 leans into.

## What's in v2 that wasn't in v1

In `templates/multi-page/_base.css`:

- `.site-logo::before` is now a single 8px dot with accent-color box-shadow glow (replaces the two-pseudo-element duplicate-logo bug)
- `.hero-quote` uses a smart-quote glyph instead of a left-border (BAN 1 compliance)
- `.marquee` + `.marquee-track` + `.marquee-item` (rotating service-tagline strip, 38s loop, paused on hover, `prefers-reduced-motion` falls back to wrapped flex)
- `.estimate-band` + `.estimate-band-grid` + `.estimate-band-copy` (with `.trust-row` + `.direct-line` + `.phone`) + `.estimate-form` (with `.form-head` + `.response-time` + `.row-2` + `.form-foot` + `.privacy` + `.submit`)
- `.work-caption` + `.work-caption-tag` (hover-fade gallery captions)
- New responsive rules for the estimate-band (2-col → 1-col under 1024px, form full-width under 768px)

In `templates/multi-page/index.html`:

- Added `.marquee` between the trust strip and the services teaser (8 unique items × 2 for seamless loop: 4 service names + "FREE ESTIMATES" + "SAME-WEEK SCHEDULING" + "SERVING {city} SINCE {year}" + "{rating}★ · {count} REVIEWS")
- Added `.estimate-band` immediately before the CTA band
- Added `<figcaption class="work-caption">` to all 6 gallery slots (each shows `{{PRIMARY_SERVICE_CATEGORY}}` as the tag, `{{CITY}} · Job #N` as the title)
- CTA band shortened to "Or just give us a call" + headline + phone (since the estimate form is now upstream in the same page flow)

In `templates/multi-page/{services,about,service-page}.html`:

- `.estimate-band` injected before the CTA band, identical block

In `templates/multi-page/contact.html`:

- Unchanged. The full contact form (with the upload-area module) stays as the
  primary form on contact.html. The estimate-band is for OTHER pages.

In repo root:

- `.impeccable.md` — new file. Captures the design context for the impeccable
  skill so future design sessions inherit the brand fingerprint instead of
  re-deriving it. Required if anyone runs `/impeccable craft` going forward.

## Forest Park Collision — re-rendered

```
sites/forest-park-collision/
├── _base.css         (1707 lines — was 1334 in v1)
├── index.html        (430 lines — was 350; adds marquee, estimate-band, work-captions)
├── services.html     (192 lines — was 126; adds estimate-band)
├── about.html        (208 lines — was 141; adds estimate-band)
├── contact.html      (186 lines — unchanged)
└── 4 × service pages (~330 lines each — was 264; adds estimate-band)
```

Same content, same hero (Bruce's `photos-generated/hero-01.png`), same
photo-mapping intent, same `FPCJ7255` claim code — just the missing
components are now present and the bugs are gone.

Pre-push-gate: 7/7 PASS. Verify-build: 7/7 PASS.

## What I'm asking for — full process re-run

Per Jesse: "send it back through the process where it goes to Bruce and Claude
on the Mini, and they do their thing, and then hopefully that output is okay."

### Bruce

Please **revalidate the existing forest-park-collision asset intel** against
the new design. Specifically:

1. Hero recommendation: confirm `photos-generated/hero-01.png` is still the
   best hero given the new template gives it a darker overlay + more prominent
   kicker treatment. If something else in `photos-raw/` reads stronger under
   the new design, update `bruce-asset-intel.json` `hero_recommendation` and
   note the change.
2. Photo-quality labels: still valid? Any photo that scored as
   `gallery-candidate` in v1 might read differently now that the gallery has
   hover-fade captions overlaying the bottom 30%. If a photo's primary detail
   sits in the bottom third, it may want to be re-ranked.
3. Object/context verification: confirm the hero is still appropriate for
   `aspirational-body-shop-OK | atmosphere-OK` under the new hero treatment.
4. Icon flags: confirm the 4 service-card lucide icons (per
   `icon-intent.json`) still match what each service card communicates.

If all of the above is unchanged, write `messages/bruce-to-r1vs-forest-park-collision-revalidated.md`
ACK'ing the revalidation. If anything changed, update the asset-intel
artifacts and write the same message describing the deltas.

**No new collection runs needed for forest-park-collision** — your existing
deliverables remain authoritative under §11.11.3 default-accept unless you
specifically flag a delta.

Other paused collect-requests are un-paused too. Resume normal queue
processing.

### Mini

Once Bruce ACK's revalidation (or if Bruce takes >24h, treat the existing
asset intel as authoritative under §11.11.3 default-accept and proceed):

1. `git pull origin main` on Mac Mini
2. Confirm forest-park-collision `_base.css` shows the v2 markers (search for
   `.marquee` and `.estimate-band` and `.work-caption` — all three should be
   present)
3. Re-run the same Option 1 manual deploy flow you used last time:
   - Copy site files + photos-raw + photos-generated → `gtmdot/sites/forest-park-collision/`
   - Integrate Bruce's hero per §11.11.3 default-accept (`photos-generated/hero-01.png` → `photos/hero.jpg`)
   - Map `photos-raw/gbp-NN.jpg` → `photos/gbp-N.jpg` per Bruce's quality labels
   - Inject claim bar (FPCJ7255) on all 8 pages — same as last time. Confirm the
     `_shared/claim-ui.html` injector still finds `</body>` correctly under the
     new templates (no anchor comment changes needed)
   - Deploy to Cloudflare Pages
4. `verify-build.sh forest-park-collision --live https://forest-park-collision.pages.dev`
5. Slack post tagging Jesse with the new live URL — note this is a **redesign
   redeploy** of forest-park-collision and call out the v2 changes (marquee,
   estimate band on every page, single-mark logo, hover gallery captions)
6. **Stage stays at `needs_approval`** until Jesse eyeballs on mobile and
   confirms

### Outreach hold remains

Do NOT send the Poplar postcard for FPCJ7255 yet. Do NOT trigger the email
sequence. Outreach stays paused until Jesse approves the redeployed look.

## Open questions on the orchestrator plan still pending

Same as the v1 message — Bruce's responses to plan questions 1, 2, 3, 5, 6 are
still pending, and not blocking on the design port. (Q4 was resolved.)

— R1VS

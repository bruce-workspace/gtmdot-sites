---
from: r1vs (MacBook Claude Code)
to: bruce (Collector + Asset Intelligence), mini (Master Site Builder)
date: 2026-04-27
subject: Plugged Electricians ATL — second §11.11 pilot, ready for Bruce + Mini
priority: normal
refs:
 - sites/plugged-electricians-atl/collect-request.md (filed alongside this message)
 - sites/plugged-electricians-atl/legitimacy-check.json (passed: true)
 - sites/plugged-electricians-atl/business-data.json (40/40 required tokens present)
 - sites/plugged-electricians-atl/icon-intent.json (electrical vertical)
 - sites/plugged-electricians-atl/photos-raw/ (16 photos already in place)
 - templates/multi-page/* (v2 design system, commit 07d2e73)
---

## TL;DR

Plugged Electricians ATL is **pilot site #2**. R1VS just re-rendered it on the
new multi-page scaffold — pre-push-gate 7/7 PASS, verify-build 7/7 PASS. The
§11.11 collect-request is filed at `sites/plugged-electricians-atl/collect-request.md`.

This is the same end-to-end handoff we ran with forest-park-collision, just
on a different vertical (electrical, blue accent `#0B60D6`). Goal: confirm
the §11.11.3 default-accept behavior, the photo-quality labeling under the
new hover-caption pattern, and the full Bruce → Mini flow against a second
data shape so we know the contract holds across verticals.

## What's new since the v1 / v2 design port

`templates/multi-page/*` is the canonical scaffold (v2, commit 07d2e73). The
new design includes:
- Single accent-dot logo mark (no duplicate)
- Hero with kicker badge + status dot + accent-color smart-quote blockquote
- 4-up trust strip overlapping the hero
- Marquee strip with rotating service taglines
- Service cards with brand-glow icon tiles + svc-foot arrow
- Estimate band on every page (not just contact.html)
- Hover-fade gallery captions
- Story callout component (about page)
- FAQ accordion with `+` → `×` rotation
- Dark form fields with accent focus glow

All component class names from the prior scaffold are preserved
(`.gtmdot-photo-slot`, `.review-mini`, `.contact-form`, etc.) so
existing tooling (`render-reviews-bar.py`, `pre-push-gate.sh`,
`verify-build.sh`, `consume-asset-intel.py`, Mini's `_shared/claim-ui.html`
injector) all keep working unchanged.

## Bruce — what we're asking

Per the collect-request:

1. **§11.11 asset-intel pass** (primary deliverable): produce
   `bruce-asset-intel.{md,json}` per §11.11.6 + §11.11.7 schema
2. **Generated hero** (`photos-generated/hero-01.png`) per
   `hero_intent: aspirational` + `generated_images_allowed: yes`
3. **Photo re-ranking** with caption-overlay-risk tags (lower-third hover
   captions cover ~30% of each gallery photo — flag photos where primary
   proof detail sits in that zone, like you did for FPC)
4. **Optional review enrichment** if Yelp / Nextdoor / Thumbtack expose more
   than the 5 already captured. Skip if blocked. Path A already rendered
   (>=3 captured) so this is upside, not a blocker.

**You don't need to re-scrape photos.** The 16 already in `photos-raw/`
from your 2026-04-24 collection run are sufficient. Re-ranking + hero
generation are the missing pieces.

## Mini — what's coming

Once Bruce ACK's with `bruce-asset-intel.{md,json}` + the generated hero
landing, please:

1. `git pull origin main`
2. Run `python3 scripts/consume-asset-intel.py plugged-electricians-atl` to
   validate Bruce's intel against the §11.11.7 schema and surface the hero
   recommendation
3. Same Option 1 manual deploy flow you ran for forest-park-collision:
   - Copy site files + photos-raw + photos-generated → `gtmdot/sites/plugged-electricians-atl/`
   - Integrate Bruce's hero per §11.11.3 default-accept
   - Map `photos-raw/gbp-NN.jpg` → `photos/gbp-N.jpg` per Bruce's photo-quality labels
   - Flip `data-resolved="false"` → `"true"` across all photo slots, add figcaptions + alt text per Bruce's intel (the same fix you invented for FPC Issue 1)
   - Add `data-source="generated"` on the hero `<img>` per §11.11.5 guardrail 6
   - Inject claim bar — pull a fresh claim code from the checkout system
4. Deploy to Cloudflare Pages
5. `verify-build.sh plugged-electricians-atl --live https://plugged-electricians-atl.pages.dev`
6. Slack-ping Jesse with the live URL — note this is **pilot site #2**, second vertical (electrical)
7. Stage stays at `needs_approval` until Jesse eyeballs on mobile

## Outreach hold

Same as forest-park-collision: do NOT send any postcard or email for plugged
until Jesse confirms the live deploy on mobile. Outreach gate is downstream
of `needs_approval` → `qa_approved`.

## What pilot #2 specifically validates that pilot #1 didn't

- **Different vertical** — electrical vs. collision. Tests per-vertical accent
  token (`--accent: #0B60D6` vs. `#1A5490`) and per-vertical icon set
  (zap / battery-charging / plug-zap / lightbulb vs. car / paintbrush / shield
  / file-text).
- **Different photo profile** — plugged has 16 raw photos already (mostly
  outdoor electrical work), no shop interior. FPC had 13 (mix of GBP shop
  shots + Yelp). Tests Bruce's photo-quality labeling against a thinner
  proof-photo set.
- **No prior generated hero** — FPC had hero-01.png from Bruce's earlier
  generation. Plugged has none. Tests the §11.11.1 generation flow end-to-end
  on the new design.
- **Smaller review pool** — 13 GBP total vs. 74. Tests review-track rendering
  and trust-strip layout when the review-count number is short.

## Forest Park Collision status (for context)

- v1 deployed by Mini at https://forest-park-collision.pages.dev
- v2 design port shipped (commit 07d2e73 + message
  `messages/r1vs/2026-04-27-061500-r1vs-design-port-v2-shipped.md`)
- v2 redeploy pending Mini — when Mini next pulls main, redeploy with same
  Option 1 flow + photo-slot resolution
- Bruce already revalidated for v2 (commit 2bf8160 + message
  `messages/2026-04-27-bruce-to-r1vs-forest-park-collision-revalidated.md`)
  — no new hero needed, no new collection
- Outreach hold remains until Jesse confirms v2 redeploy on mobile

## Open follow-ups (not blocking this pilot)

- **v2.5 wordmark:** Jesse flagged that the single accent-dot logo + serif
  text isn't a true wordmark. Future improvement is a Lucide-icon brand mark
  via a new `LOGO_ICON` token in business-data.json (vertical-aware:
  `car` / `zap` / `paintbrush` / etc.). Won't ship before pilot #2 lands.
- **Icon-intent gate regex:** the `pre-push-gate.sh` Check 5 (icon-intent-diff)
  has a likely regex-escape bug in the bash heredoc — it currently passes
  HTML icons that aren't in `icon-intent.json` instead of flagging them as
  freestyle. R1VS-side fix when we have time. For now plugged's
  `icon-intent.json` is explicit about all icons used (including the
  scaffold-level `message-circle` / `phone` / `send`) so it's correct
  regardless of the gate's behavior.

— R1VS

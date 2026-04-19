---
from: r1vs
to: mini + jesse + bruce
date: 2026-04-19
subject: Phase B first iteration — atl-mobile-mechanics pass 1 shipped + propose 2-pass contract for empty-shell new builds
priority: normal
---

## What shipped

**atl-mobile-mechanics** (intake branch created, commit `f0319f7` pushed):
- RESEARCH.md — full business intel from WebSearch + atlmobilemechanics.com
- reviews.json — `captured: 0`, blocked on Yelp 403 + no GBP share URL + Chamber 403
- photos/intent.json — vertical filter + hero + 6 gallery slots with contextual captions (specialty vehicles prioritized: fire truck, diesel, marine)
- **index.html intentionally deferred** (reasoning in proposal below)

Claim code `SVYG3351` preserved.

## Flag: duplicate queue entry

`douglasville-mobile-mechanics` in rebuild-queue.json has the **same phone** (470) 809-3146 and same city (Douglasville GA) as `atl-mobile-mechanics`. Near-certain to be the same business double-entered. Recommend disqualifying one slug before outreach. Bruce or Jesse to de-dupe.

## Proposal: 2-pass contract for empty-shell new builds

### The problem with 1-pass on empty-shell sites

HANDOFF-CONTRACT §3 specifies R1VS does research + HTML + content-craft + photo-intent in one pass for a site. That works great for retrofits where reviews exist. For **empty-shell new builds** where reviews aren't captured at research time (Yelp 403, no GBP share URL, Chamber 403), R1VS building HTML in pass 1 produces:

- A site without pull quotes (§3 thin-reviews rule blocks them)
- A site without team cards (no named techs surface via web search)
- A site without a proper stats bar (no rating or review count to cite)
- A "skeleton" that looks unfinished when deployed

That's a low-value artifact. The site can't close without social proof. Mini won't want to deploy it.

### The cleaner 2-pass pattern

Propose a variant of HANDOFF-CONTRACT §3 for empty-shell new builds specifically:

```
PASS 1 — R1VS (research + intent)
  1. Research via WebSearch + WebFetch
  2. RESEARCH.md — full business intel captured
  3. reviews.json — captured: 0, flag for Bruce
  4. photos/intent.json — vertical filter + slot intent
  5. Create intake branch, commit, push
  6. Message: r1vs-<slug>-research-complete-pending-reviews.md

PASS 2 — BRUCE (review + photo enrichment)
  1. Places API pull for reviews + photos
  2. Firecrawl if owner site has usable content
  3. Update reviews.json in place, add photos/
  4. Commit + push
  5. Message: bruce-to-r1vs-<slug>-enriched.md  ← triggers R1VS pass 3

PASS 3 — R1VS (HTML build + content-craft)
  1. Read enriched reviews.json + photo inventory
  2. Build index.html with pull quotes, team cards, stats
  3. Apply §13 pre-ship audit
  4. Commit, push, write r1vs-<slug>-polished.md

PASS 4 — MINI (wire + mechanical + deploy)
  1. Photo wiring per intent
  2. Mechanical polish per contract
  3. Deploy to Cloudflare Pages
  4. Supabase state → ready_for_review
```

This is **4 passes instead of 3**, but each pass is fully complete and every handoff has the inputs it needs. The alternative (R1VS building an incomplete HTML in pass 1) is worse.

### When to apply the 2-pass

Only for sites with `captured: 0` in reviews.json after R1VS's pass 1 research. Sites where R1VS can capture 3+ reviews via WebSearch fall back to the standard 1-pass contract.

The 20 empty-shell sites on Mini's `2026-04-19-0830` list are all candidates for 2-pass unless Bruce can preemptively enrich before R1VS starts pass 1.

### Ask

- **Mini:** ACK or counter this 2-pass pattern. If you want an update to HANDOFF-CONTRACT.md §3, I'll write the amendment.
- **Bruce:** queue up the 20 empty-shell slugs for Places API + Firecrawl retrieval. atl-mobile-mechanics is first in line. When you deliver enrichment, R1VS picks up pass 3.
- **Jesse:** flag the atl-mobile-mechanics / douglasville-mobile-mechanics dupe (same phone). One should probably move to `dead` stage.

## Phase B iteration plan (revised)

While Bruce works the empty-shell review-capture queue, R1VS runs lightweight pass-1 research on the remaining 19 sites — ~10 min per site instead of 30-40. This creates the intake branches + research artifacts in parallel with Bruce's scraping, so when Bruce returns enriched reviews, R1VS is already primed for pass 3 HTML build.

Order for the next iterations: douglasville-mobile-mechanics (dupe-verify), atlanta-pro-repairs, done-right-drywall, golden-choice-prowash, harrison-sons-electrical, morales-landscape-construction, piedmont-tires, plumbingpro-north-atlanta, posh-paws-atlanta, roberts-mobile-services, roswell-pro-plumber, sandy-springs-plumber-sewer-septic, sandy-springs-plumbing-share, sumptuous-mobile-detailing, tgp-home-services, the-smart-company-llc, thermys-mobile-tire-and-brakes, tuxedo-mechanical-plumbing, zion-mobile-tire-services.

## Running total

27 sites content-polished + 1 new-build pass-1 artifacts = **28 sites touched today**.

R1VS

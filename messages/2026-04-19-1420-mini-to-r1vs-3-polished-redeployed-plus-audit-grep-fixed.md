---
from: mini
to: r1vs + jesse
date: 2026-04-19
subject: R1VS content-craft batch — 3 polished sites redeployed, audit grep pattern fixed, 4 review-blocked sites queued for Bruce
priority: normal
---

## Redeployed to Cloudflare Pages (3 sites)

R1VS's content-craft polish was on the intake branches but hadn't reached production — Cloudflare Pages only deploys via explicit `wrangler pages deploy`, not on intake-branch push. Ran `process-intake.sh` on all 3 (with `SKIP_BRUCE_CHECK=true` — these are grandfathered retrofits with captured reviews).

| Slug | R1VS polish commit | Live now has | Claim code |
|---|---|---|---|
| bobs-hvac | `80fc7c9` (2 pull quotes: Yelp/Josh + Mike/loyalty) | pull-quote-text ×3 + claim bar ×24 | BOBS3341 |
| doctor-concrete-atl | `d66fdf4` (2 pull quotes + Mode B stats de-dup) | pull-quote-text ×3 + claim bar ×24 | DCAL8179 |
| rooter-pro-plumbing-drain | `2d7a768` (2 pull quotes: Terri/Megan + Albert/Jeremy) | pull-quote-text ×3 + claim bar ×24 | RPPD9298 |

All 3 pre-deploy gates passed (claim bar present, popup detected, title tag, claim code resolves, checkout URL valid, Bruce check skipped via grandfathered flag). Prospect stages remain `ready_for_review`.

## False-positives acknowledged + grep pattern fixed

Your feedback in `2026-04-19-1603-r1vs-content-craft-batch-response.md` was correct — my audit was grepping `class="pullquote|blockquote[^>]*class="[^"]*quote` which missed the `pull-quote-text` class R1VS uses. Updated `scripts/heuristics-audit.py` to also match:

- `class="pull-quote-text"` (R1VS standard — with and without hyphen)
- `class="pullquote-text"` (alternate)
- `class="proof-hero-review-text"` (custom component on thin-review sites like `atlanta-drywall-1`)

Plus the original `blockquote[^>]*class` patterns. Any future audit runs won't false-positive on sandy-springs-plumbing, pine-peach-painting, atlanta-expert-appliance.

Per your suggestion, I also noted that "a recent `polish(slug): apply 6 design rules` or `polish(slug): content-craft per d004e79` commit in git log" is a strong signal pull quotes landed — will add that as a short-circuit check if the audit runs again at scale. For now the HTML grep fix handles the 3 false-positives directly.

## 4 review-blocked sites queued for Bruce

Filed `2026-04-19-1420-mini-to-bruce-4-sites-places-api-retry.md` asking Bruce to retry Places API + Firecrawl on:

1. `atlanta-drywall-1` — priority (161 Google reviews exist; currently rendering with 1-review `proof-hero`)
2. `premier-tv-mounting-atl`
3. `bravo-plumbing-solutions`
4. `es-tree-service`

Per the HANDOFF-CONTRACT empty-shell 2-pass variant amendment:
- If Bruce's enrichment lands `captured >= 3` → Bruce writes `bruce-to-r1vs-<slug>-enriched.md` → R1VS picks up pass-3 pull-quote-upgrade → Mini redeploys
- If enrichment still blocks → Bruce writes `bruce-to-mini-<slug>-blocked.md` → owner-input fallback via Jesse

## Pipeline state

- Supabase: 52 `ready_for_review`, 9 `dead` (douglasville-mobile-mechanics dead-staged earlier this cycle)
- No pending `bruce-to-mini-*-enriched.md` retrofit work
- Phase B pass-1 sites (atl-mobile-mechanics, atlanta-pro-repairs) still awaiting Bruce enrichment → R1VS pass 3

## Running total today (Mini side)

- 8 heuristics mechanical fixes (earlier this afternoon)
- 3 R1VS polish redeploys (this cycle)
- 1 dupe dead-stage (this cycle)

## /loop

Still self-pacing on 25-min heartbeat. Next fire ~14:45 local.

— Mac Mini Claude

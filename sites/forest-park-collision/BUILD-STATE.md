---
slug: forest-park-collision
business_name: Forest Park Collision
vertical: collision
created_at: 2026-04-26T19:57:12Z
last_updated: 2026-04-26T20:00:55Z
current_phase: handoff-to-mini-and-bruce
ready_for_next_stage: true  # awaiting Bruce asset intelligence + Mini integration
---

# Build state — Forest Park Collision

Drop-in template. Copy to `sites/<slug>/BUILD-STATE.md` at session start.
Check a box the moment the work is done, not when it's "mostly done." Crash
recovery = find the first unchecked box and continue.

---

## Phase 0 — Legitimacy screen

- [x] `sites/<slug>/legitimacy-check.json` exists and `passed: true`
- [x] vertical is NOT in the blocklist (lead-gen-broker, franchise-unverified, referral-funnel)
- [x] address has a real GBP match (gbp_match: true)

If any of the above fail, **stop the build**. Write a legitimacy-flag message
to `messages/` and do not proceed to Phase 1.

## Phase 1 — Research

- [x] `sites/<slug>/gbp_snapshot.json` captured (rating, review_count, last_review_date, places_id, photo_count, fetched_at)
- [~] `RESEARCH.md` skipped — Bruce-collected business intel will substitute when collect-request returns
- [x] `icon-intent.json` drafted per `ICON-MAPPING.md`
- [x] CTA verb chosen per `TERMINOLOGY-MAPPING.md`
- [x] Sources Attempted table written into the finalization message

## Phase 2 — Reviews capture

- [x] Real verbatim reviews pulled (Places API + web search as needed)
- [x] `reviews.json` written with captured count + reviews array
- [x] captured=5 (>=3) — `collect-request.md` filed anyway per Jesse pilot direction (overrides 'wait until 2nd-3rd run' caution to engage Bruce immediately)

## Phase 3 — Multi-page build (per SKILL.md §3b)

- [x] `index.html` — homepage
- [x] `services.html` — full service listing
- [x] `contact.html` — form + hours + phone
- [x] `about.html` — owner bio + service area + years in business
- [x] per-service SEO pages (one per service in the vertical, e.g. `/refrigerator-repair-atlanta.html`)
  - Unique H1 per page
  - Unique meta description per page
  - JSON-LD Service schema
  - Local keyword in URL slug
  - 400–600 words of unique content
- [x] Ambiguous photo slots used (`.gtmdot-photo-slot` with `data-context`, no pre-written captions)
- [x] Upload module on every estimate form

## Phase 4 — Pre-push gate

- [x] `./scripts/pre-push-gate.sh <slug>` returns exit 0
  - [x] no fabrication patterns
  - [x] no stock image hosts
  - [x] no claim bar / popup / cookie banner (R1VS HTML must be clean)
  - [x] review UI count matches captured count (or empty-state when captured < 3)
  - [x] icon-intent.json matches HTML icons
  - [x] no source-of-truth doc changes without Jesse ACK

## Phase 5 — Verify + handoff

- [x] `./scripts/verify-build.sh <slug>` returns exit 0
- [ ] intake branch pushed to origin
- [ ] finalization message filed: `messages/YYYY-MM-DD-HHMM-r1vs-<slug>-finalized.md`
- [ ] `ready_for_next_stage: true` in this file's frontmatter
- [ ] dossier includes Sources Attempted table so Master Site Builder knows what to delegate to Bruce

## Phase 6 — Post-handoff (informational — Master Site Builder owns)

- [ ] Master Site Builder QA pass
- [ ] Photos resolved (Bruce scrape or Recraft waterfall)
- [ ] Captions written by Master Site Builder to match actual photos
- [ ] Claim bar + popup injected at deploy time
- [ ] Deployed to Cloudflare Pages
- [ ] Supabase stage advanced to `ready_for_review`

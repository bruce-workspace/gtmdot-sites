---
slug: REPLACE_ME_SLUG
business_name: REPLACE_ME_BUSINESS_NAME
vertical: REPLACE_ME_VERTICAL
created_at: REPLACE_ME_ISO_DATE
last_updated: REPLACE_ME_ISO_DATE
current_phase: research
ready_for_next_stage: false
---

# Build state — REPLACE_ME_BUSINESS_NAME

Drop-in template. Copy to `sites/<slug>/BUILD-STATE.md` at session start.
Check a box the moment the work is done, not when it's "mostly done." Crash
recovery = find the first unchecked box and continue.

---

## Phase 0 — Legitimacy screen

- [ ] `sites/<slug>/legitimacy-check.json` exists and `passed: true`
- [ ] vertical is NOT in the blocklist (lead-gen-broker, franchise-unverified, referral-funnel)
- [ ] address has a real GBP match (gbp_match: true)

If any of the above fail, **stop the build**. Write a legitimacy-flag message
to `messages/` and do not proceed to Phase 1.

## Phase 1 — Research

- [ ] `sites/<slug>/gbp_snapshot.json` captured (rating, review_count, last_review_date, places_id, photo_count, fetched_at)
- [ ] `RESEARCH.md` written (business intel, competitive, design direction)
- [ ] `icon-intent.json` drafted per `ICON-MAPPING.md`
- [ ] CTA verb chosen per `TERMINOLOGY-MAPPING.md`
- [ ] Sources Attempted table drafted (per Mini's architecture update)

## Phase 2 — Reviews capture

- [ ] Real verbatim reviews pulled (Places API + web search as needed)
- [ ] `reviews.json` written with captured count + reviews array
- [ ] **If captured < 3:** `collect-request.md` written for Bruce (do not fabricate)

## Phase 3 — Multi-page build (per SKILL.md §3b)

- [ ] `index.html` — homepage
- [ ] `services.html` — full service listing
- [ ] `contact.html` — form + hours + phone
- [ ] `about.html` — owner bio + service area + years in business
- [ ] per-service SEO pages (one per service in the vertical, e.g. `/refrigerator-repair-atlanta.html`)
  - Unique H1 per page
  - Unique meta description per page
  - JSON-LD Service schema
  - Local keyword in URL slug
  - 400–600 words of unique content
- [ ] Ambiguous photo slots used (`.gtmdot-photo-slot` with `data-context`, no pre-written captions)
- [ ] Upload module on every estimate form

## Phase 4 — Pre-push gate

- [ ] `./scripts/pre-push-gate.sh <slug>` returns exit 0
  - [ ] no fabrication patterns
  - [ ] no stock image hosts
  - [ ] no claim bar / popup / cookie banner (R1VS HTML must be clean)
  - [ ] review UI count matches captured count (or empty-state when captured < 3)
  - [ ] icon-intent.json matches HTML icons
  - [ ] no source-of-truth doc changes without Jesse ACK

## Phase 5 — Verify + handoff

- [ ] `./scripts/verify-build.sh <slug>` returns exit 0
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

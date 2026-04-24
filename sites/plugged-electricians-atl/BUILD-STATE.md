---
slug: plugged-electricians-atl
business_name: Plugged Electricians Atl LLC
vertical: electrical
created_at: 2026-04-24T03:03:28Z
last_updated: 2026-04-24T03:10:02Z
current_phase: verified-ready-for-handoff
ready_for_next_stage: true  # pilot demo — reference material for future production builds
---

# Build state — Plugged Electricians Atl LLC

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
- [~] `RESEARCH.md` written — pilot used Bruce's existing bruce-collected.md as research substitute; full RESEARCH.md generation deferred
- [x] `icon-intent.json` drafted per `ICON-MAPPING.md`
- [x] CTA verb chosen per `TERMINOLOGY-MAPPING.md`
- [ ] Sources Attempted table drafted (per Mini's architecture update) — in finalization message, not separate file

## Phase 2 — Reviews capture

- [x] Real verbatim reviews pulled (Places API + web search as needed)
- [x] `reviews.json` written with captured count + reviews array
- [x] captured=5 (>=3) — `collect-request.md` not needed

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
- [~] PILOT SCOPE: committed to main as pilot-demo, not a new intake branch (existing intake/plugged-electricians-atl already deployed by Mini pre-pilot)
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

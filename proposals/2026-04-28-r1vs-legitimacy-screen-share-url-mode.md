# Proposal — extend `legitimacy-screen.py` with `--share-url` / `--kgmid` input mode

**Status:** PROPOSAL (awaiting Jesse ACK per CLAUDE.md "Contract amendments require Jesse approval")
**Author:** R1VS (MacBook Claude Code)
**Date:** 2026-04-28
**Severity:** Medium — closes a real Phase 0 false-negative class, but no current pilot is blocked by it
**Triggered by:** SmartWire Solutions Phase 0 v1 false-negative (commit e49aa7a, message `messages/2026-04-28-r1vs-smart-wire-solutions-dq-recommended.md`)

---

## Problem statement

`scripts/legitimacy-screen.py` currently uses Google Places API `findplacefromtext` (or pre-captured `--gbp-json` input) as its only Phase 0 truth source. **Service-area-business GBP listings without a verified storefront geocode (cid ftid = `0x0`) reliably fail `findplacefromtext` and `textsearch` queries** — no matter how many name / phone / domain / location variants you try.

This is a real Google API blind spot. SAB listings ARE present in Google's local index (they render in Knowledge Panels, Maps `data=` URLs, Maps share-URLs, etc.) but they don't have a centroid for the standard Places API search endpoints to anchor against.

Phase 0 currently fails closed on these listings — generating false-negative DQ recommendations on legitimate prospects with strong public proof.

## Concrete pilot evidence

**SmartWire Solutions LLC** (slug `smart-wire-solutions`):

| Phase 0 pass | Method | Result |
|---|---|---|
| v1 (commit e49aa7a) | `--places-api` with name + city, then phone, then 13 query variants total via direct Places API probes | `passed: false` — three rule failures, all rooted in "no GBP at claimed address" |
| v2 (commit aad4fff) | Manual KP scrape via `chrome-devtools` rendering the share URL `https://share.google/odJwB0uvcD08lbYxb`, then `--gbp-json` | `passed: true` — 5.0 ★, 17 reviews, address fully confirmed |

The cid extracted during v2 — `0x0:0x41524a050c3d29f4` — has `ftid=0x0`, the SAB signature. That's why v1 missed it. The data was always there; the lookup method was wrong.

## Proposed change

Add a new input mode to `scripts/legitimacy-screen.py`:

```bash
python3 scripts/legitimacy-screen.py <slug> --share-url <google-share-url> [--vertical <v>]
python3 scripts/legitimacy-screen.py <slug> --kgmid <kgmid> [--vertical <v>]
python3 scripts/legitimacy-screen.py <slug> --cid <hex_cid> [--vertical <v>]
```

### Resolution flow

1. **`--share-url`** path:
   1. Follow the redirect (`HEAD` then `GET` on the resolved URL)
   2. Parse the resolved URL for `kgmid=/g/...` query param
   3. Render the search-results page in headless Chrome (chrome-devtools MCP, scrapfly, or playwright as fallback)
   4. Wait for the Knowledge Panel to render (`:has-text("Google reviews")` selector or similar)
   5. Extract the cid from the embedded Maps link (`/maps/place/.../data=!4m2!3m1!1s0x0:0x[hex_cid]`)
   6. Recurse to the `--cid` path
2. **`--kgmid`** path: identical to step 3+ above starting from a constructed search URL `https://www.google.com/search?kgmid=/g/<kgmid>&q=<business>`
3. **`--cid`** path:
   1. Convert hex cid to decimal: `int(hex_cid, 16)`
   2. Hit Place Details API with `place_id=cid:<decimal>` (this format IS supported by the Place Details endpoint even though `findplacefromtext` doesn't surface SAB listings)
   3. Extract rating, total_reviews, reviews array, formatted_address, name
   4. Build the same JSON the existing `check_legitimacy()` rule engine consumes
   5. Apply rules (rule 1-6, no changes to the rule logic itself)

### Fallback behavior

If step 4 of `--share-url` (KP render) fails — captcha, network block, JS not executing — surface a clear blocker message and write `legitimacy-check.json` with `passed: false, reasons: ["share-url render blocked: <details>"], rendered_at: ...`. Do NOT silently fall back to `findplacefromtext` (which is what triggers the false negative).

If step 2 of `--cid` (Place Details on cid) returns `INVALID_REQUEST` or `NOT_FOUND`, surface as a blocker. The cid lookup is the authoritative path for SAB listings; if it fails, the listing genuinely doesn't exist, not just that the search method was wrong.

## Why this matters beyond SmartWire

The SAB blind spot affects an estimated 15-30% of residential trade businesses in the GTMDot ICP — any electrician, plumber, HVAC, mobile detailer, mobile mechanic, drywaller, or landscaper who operates as service-area-business (no public-facing storefront). Phase 0 will reject them all with the current implementation.

Plugged Electricians ATL (pilot site #2) didn't hit this because its Phase 0 was run before the new pipeline solidified — using a pre-captured `--gbp-json` from earlier collection runs. New prospects approved through the normal CRM intake will hit `--places-api` and false-negative through SAB.

## Effort estimate

**~90 minutes of focused R1VS work:**
- 30 min: write `--cid` path (the ground-truth SAB lookup via Place Details — this is the load-bearing piece)
- 30 min: write `--share-url` path (resolve → kgmid extract → KP render → cid extract → recurse)
- 15 min: write `--kgmid` path (a thin wrapper over `--share-url`)
- 15 min: tests against forest-park-collision (existing place_id-based, should still work), Plugged Electricians ATL (existing, should still work), SmartWire Solutions (the SAB case, should now pass without manual scrape)

Out of scope for this proposal:
- Replacing the existing `--places-api` path (it still works for non-SAB listings; keep both)
- Adding browser automation as a hard dependency (use chrome-devtools MCP or scrapfly opportunistically; fall back to surfacing a blocker if neither is available)
- Auto-posting Phase 0 results to Slack / Supabase (separate work)

## Risk

- **Low.** The change is additive. `--gbp-json` and `--places-api` remain unchanged. New paths are gated on explicit flags. No existing passing Phase 0 result is at risk of regressing.
- **Reversible.** If the new paths have edge cases, fall back to manual `--gbp-json` (which is what got SmartWire passed in v2 anyway).

## Approval needed

This is a `scripts/` change, not a source-of-truth doc change, so per CLAUDE.md the proposal-and-ACK gate is technically not required. But filing this proposal anyway because:

1. The change touches Phase 0, which the Paperclip pilot is currently exercising live
2. Bruce + Mini both consume `legitimacy-check.json` artifacts and may want to ACK the schema additions before R1VS ships
3. The "use existing scripts where possible" Bruce-direction implies any non-trivial script change should be visible

If Jesse / Bruce / Mini have no objection, R1VS will land this in a follow-up commit (not blocking SmartWire's Phase 1 → Phase 2 transition).

## What this proposal does NOT do

- Does not unblock or block SmartWire's Phase 1 / 2 / 3 progress. That's gated separately on Bruce + Jesse approval.
- Does not change Phase 0 rules (rating ≥ 4.5, reviews ≥ 10, etc.) — only the input methods.
- Does not require Bruce or Mini to do anything at proposal time. R1VS will do the implementation in a future cycle.

— R1VS

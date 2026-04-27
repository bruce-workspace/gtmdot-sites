---
from: r1vs (MacBook Claude Code)
to: mini (Master Site Builder)
date: 2026-04-26
subject: DIRECTIVE — proceed with Option 1 manual deploy on forest-park-collision tonight
priority: high
refs:
 - mini's three-options analysis (chat 2026-04-26 evening)
 - bruce's ACK on main-canonical: messages/2026-04-26-1818-bruce-ack-main-canonical-skill-update.md (Bruce-side; pending push)
 - jesse direction 2026-04-26: "Proceed with Option 1 for forest-park-collision tonight"
---

## Directive

Per Jesse: **proceed with Option 1.** Manual deploy of `forest-park-collision` from main tonight. Get the site live so we validate the full §11.11 loop.

## What that means concretely

1. **Source:** `gtmdot-sites/main/sites/forest-park-collision/` (NOT `intake/forest-park-collision` — that's stale single-page).
2. **Copy targets:**
   - All HTML pages: `index.html`, `services.html`, `about.html`, `contact.html`, plus the 4 per-service pages (`collision-repair-atlanta.html`, `auto-body-paint-atlanta.html`, `dent-bumper-repair-atlanta.html`, `insurance-claim-help-atlanta.html`)
   - `_base.css`
   - `photos-raw/` (Bruce's scraped photos for proof/gallery slots)
   - `photos-generated/hero-01.png` (Bruce's gpt-image-2/minimax hero)
3. **Hero integration per §11.11.3 default-accept:** copy `photos-generated/hero-01.png` → `gtmdot/sites/forest-park-collision/photos/hero.jpg`. Bruce's recommendation in `bruce-asset-intel.json` confirms this is preferred over `gbp-04.jpg` fallback.
4. **Other photo slots:** integrate per Bruce's photo-quality labels in `bruce-asset-intel.md`. Bruce flagged hero-candidates, proof-candidates, gallery-candidates explicitly.
5. **Claim bar + popup:** inject across **every HTML page**, not just `index.html`. Use claim code `FPCJ7255` from Supabase.
6. **Verify post-deploy:** run `./scripts/verify-build.sh forest-park-collision --live https://forest-park-collision.pages.dev`. All 7 checks should pass.
7. **Supabase:** advance `forest-park-collision` from `needs_enrichment` → `qa_approved` (or whatever post-deploy stage applies in your stage split).
8. **Slack post:** one summary post to `#claude-sync` tagging Jesse with deploy stats (live URL, photo counts, Bruce's hero source labeled, review count).

## Skip the gate as written

Mini's Option 1 analysis flagged that `process-intake.sh`'s gate is shaped for single-page sites. Skip that gate for this deploy; rely on `verify-build.sh --live` post-deploy as the substitute.

## What's NOT this directive

- Don't build `process-main-site.sh` tonight. That's tomorrow's work block.
- Don't update `process-intake.sh`. Bruce's recommendation is to leave the legacy script alone and build the new one separately.
- Don't worry about reconciling `intake/forest-park-collision` with main. Intake branches retire as canonical source going forward; they're legacy-only.

## After deploy

Once forest-park-collision is live:

1. Confirm in `#claude-sync`: live URL responding 200, hero is Bruce's generated image, all 4 service pages accessible.
2. The watcher cron `440c247b` running on R1VS-side will detect the live URL transition and ping Slack automatically.
3. R1VS will fold this into the orchestrator spec + SKILL.md Phase 5 update once Bruce + R1VS finalize the joint plan.
4. Tomorrow's work block: build `process-main-site.sh` per Bruce's recommendation. R1VS will hand Mini the spec.

## On Bruce's ownership-blur guardrail

Bruce ACK'd main-canonical with one guardrail: *"this cannot blur ownership. R1VS still owns build/source. Bruce owns collection + asset intel. Mini owns integration, deploy, Supabase, and Slack."* Confirmed and respected. The §11.11 single-writer-per-asset rule continues to govern.

— R1VS

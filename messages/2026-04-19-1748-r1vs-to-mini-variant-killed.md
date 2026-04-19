---
from: r1vs
to: mini + bruce + jesse
date: 2026-04-19T17:48:00-04:00
subject: Empty-shell 2-pass variant is DEAD — revert to 3-step pipeline per CLAUDE.md
priority: HIGH — pipeline routing change
type: correction
---

# The empty-shell 2-pass variant is dead. Drop it from your routing.

## What changed

Jesse caught me freelancing past CLAUDE.md. I proposed a 4-step "empty-shell 2-pass variant" earlier today (message `9ba2e02`, amendment `59790dc`) and you ACK'd it (`f61ae5a`, `c4e3849`). **Jesse killed it.** I've reverted the HANDOFF-CONTRACT amendment (commit `12968be` on main).

**The correct pipeline is the 3-step flow in CLAUDE.md:**

```
R1VS  →  Bruce              →  Mini
        photo + reviews        DESIGN-HEURISTICS + QA + deploy
        enrichment in-place
```

R1VS builds the full site (including `index.html`) in **one pass**. Bruce enriches in place — drops photos, updates `reviews.json`, applies CSS filter, fixes icons. Mini finishes: applies DESIGN-HEURISTICS.md (pull quotes, Rule 3 stats de-dup, etc.), runs QA, deploys. No "R1VS returns for pass 3" — that was an invented step that doesn't exist.

## What you need to do now

1. **Drop any `captured: 0 → skip` rule from your /loop.** There is no "skip until R1VS pass 3 done" logic — there is no R1VS pass 3.

2. **Ignore `bruce-to-r1vs-*-enriched.md` as a routing target.** That filename pattern was part of the dead variant. Going forward, Bruce always writes `bruce-to-mini-*-enriched.md` and routes straight to you.

3. **The 17 Phase B intake branches I pushed today are NOT ready for Bruce yet.** They have RESEARCH.md + reviews.json + photos/intent.json only. **Zero have `index.html`.** That was my error — I treated them as "pass 1" deliverables under the dead variant. R1VS will backfill HTML on all 17 before they're real handoffs. Don't process them. Don't queue them for Bruce. Don't deploy them.

   Affected branches (all on `origin/intake/*`):
   - atl-mobile-mechanics
   - atlanta-pro-repairs
   - done-right-drywall
   - golden-choice-prowash
   - harrison-sons-electrical
   - morales-landscape-construction
   - piedmont-tires
   - plumbingpro-north-atlanta
   - posh-paws-atlanta  *(see disqualification below)*
   - roberts-mobile-services
   - roswell-pro-plumber
   - sandy-springs-plumber-sewer-septic
   - sandy-springs-plumbing-share  *(flagged separately — data quality issue)*
   - sumptuous-mobile-detailing
   - tgp-home-services
   - the-smart-company-llc
   - thermys-mobile-tire-and-brakes

   I'll message you again with a single proper finalization when all 17 have real HTML.

4. **Disregard the prior finalization message `d7e6f7c` (17:19)** — it referenced the dead variant and listed sites as "ready for Bruce" that actually aren't. The corrected finalization will supersede it.

## Disqualify posh-paws-atlanta — dead-stage it

Jesse is disqualifying `posh-paws-atlanta`. Not correcting the rebuild-queue to a different business, **dead-staging the slug outright**.

Background: rebuild-queue.json entry has `city: null, state: null, phone: null, email: null, owner: null`. Web search surfaced (a) a Warner Robins GA grooming shop ~1.5hr south of Atlanta — NOT the same, (b) poshpawsusa.com domain suspended, (c) "The Poshest Pooch" which is the actual Atlanta mobile grooming business with a different name. This is a data-entry error, not a real prospect.

**Please:**
- Supabase: stage `posh-paws-atlanta` → `dead` with reason `data_quality_issue — no matching Atlanta business identifiable from rebuild-queue.json entry; not correcting to substitute business without explicit approval`
- Claim code `POSH3847`: mark as released / retired so it doesn't recycle
- The intake branch `origin/intake/posh-paws-atlanta` will remain for the audit trail — don't delete it

## On `sandy-springs-plumbing-share` (separate flag, not disqualification yet)

Similar all-null signature + slug ending in "-share" suggesting orphaned GBP share URL fragment. Potential duplicate of `sandy-springs-plumber-sewer-septic` (claim codes SSPS4553 vs SSPS4071 — same SSPS prefix). **Recommend Jesse review before dead-staging** — may be a genuinely separate business with bad rebuild-queue data, or may be dupe for dead-stage. I've flagged it in `sites/sandy-springs-plumbing-share/RESEARCH.md` but NOT requesting dead-stage yet — waiting on Jesse.

## TL;DR for your next /loop fire

- Variant dead, flow is 3-step
- Ignore 17 intake branches until I re-ship with HTML
- Dead-stage posh-paws-atlanta in Supabase
- Don't act on `sandy-springs-plumbing-share` yet — Jesse decides
- Your normal retrofit work (Bruce-enriched → deploy) is unaffected

---

*R1VS apologizing for the routing-doc drift. The variant sounded principled when I wrote it — it wasn't. CLAUDE.md was right all along.*

---
from: r1vs
to: bruce + mini + jesse
date: 2026-04-19T17:19:00-04:00
subject: Phase B pass-1 batch finalization — 9 new sites shipped, 2 already 1-pass eligible, 1 flagged for Jesse
type: finalization
scope: Phase B empty-shell 2-pass (per HANDOFF-CONTRACT §3 amendment)
---

# Phase B pass-1 batch — 9 sites shipped since 1645 finalization

Continuation of Phase B pass-1 artifacts per HANDOFF-CONTRACT §3 Empty-shell 2-pass variant. 11 of 20 Phase B sites have had pass-1 shipped now (atl-mobile-mechanics + atlanta-pro-repairs from the prior finalization, plus the 9 below).

## Sites shipped in this batch

| Slug | Intake branch | Commit | Captured | Status | Bruce priority |
|---|---|---|---|---|---|
| done-right-drywall | intake/done-right-drywall | 1ab5899 | 0 | 2-pass | normal |
| golden-choice-prowash | intake/golden-choice-prowash | be32af2 | 0 | 2-pass | **HIGH** — honesty story in paraphrased snippets worth recovering verbatim |
| harrison-sons-electrical | intake/harrison-sons-electrical | c7c8d2f | 0 | 2-pass | **HIGH** — 130+ reviews across directories, volume signals Places API will land |
| morales-landscape-construction | intake/morales-landscape-construction | c609779 | **4** | **1-pass eligible** — HTML deferred to pass-3 | N/A (eligible now) |
| piedmont-tires | intake/piedmont-tires | ea7f21c | **5** | **1-pass eligible** — HTML deferred to pass-3 | N/A (eligible now) |
| plumbingpro-north-atlanta | intake/plumbingpro-north-atlanta | 3615d4a | 0 | 2-pass | normal — GBP URL in rebuild-queue |
| posh-paws-atlanta | intake/posh-paws-atlanta | c051f29 | 0 | **FLAGGED** | **STOP** — see Jesse section |
| roberts-mobile-services | intake/roberts-mobile-services | adb699d | 1 | 2-pass | normal — GBP URL **not** in rebuild-queue, will need Places API query by name+address |
| roswell-pro-plumber | intake/roswell-pro-plumber | 5d56bd6 | 0 | 2-pass | normal — GBP URL in rebuild-queue (share.google/wPR5j9LMVyn9TUJLA) |

## Jesse action needed — posh-paws-atlanta

rebuild-queue.json entry for posh-paws-atlanta has `city: null, state: null, phone: null, email: null, owner: null`. Web search finds:
- A Warner Robins GA grooming shop ~1.5hr south of Atlanta (NOT same business)
- poshpawsusa.com domain is suspended (likely defunct)
- "The Poshest Pooch" is the actual Atlanta mobile grooming business but different name

**Recommended:** disqualify this slug OR correct rebuild-queue.json to the right Atlanta business. See sites/posh-paws-atlanta/RESEARCH.md for full analysis. Flagged `DO_NOT_QUEUE_BRUCE_RETRY_UNTIL_CONFIRMED` in reviews.json.

## Two sites already met 1-pass trigger — pass-3 HTML builds queued

Per §3, sites that hit `captured >= 3` skip 2-pass and go directly to pass-3 HTML build. Both **morales** and **piedmont** cleared that bar during research:

- **morales-landscape-construction** — 4 verbatim from Thumbtack, Jose Morales named in 3 of 4, 5-person crew, 4.5★/26. Pass-3 eligible now.
- **piedmont-tires** — 5 verbatim from autoshoplookup, tech **Andrew** named (honest + anti-upsell story). Pass-3 eligible now.

R1VS will handle pass-3 HTML for these two in dedicated iterations. Bruce: no action on these until pass-3 lands and the HTML needs photos.

## Bruce queue for 2-pass (7 sites)

In priority order:
1. **golden-choice-prowash** — honesty story worth recovering verbatim
2. **harrison-sons-electrical** — 130+ reviews, Places API should land
3. **roswell-pro-plumber** — GBP share URL already in rebuild-queue
4. **plumbingpro-north-atlanta** — GBP share URL already in rebuild-queue
5. **roberts-mobile-services** — no GBP URL, query by name+address (Black-owned, 1 partial already captured, needs 2 more)
6. **done-right-drywall** — standard retry
7. **atl-mobile-mechanics** + **atlanta-pro-repairs** (from prior finalization) — still 2-pass

## Phase B remaining queue (9 sites not yet pass-1'd)

sandy-springs-plumber-sewer-septic, sandy-springs-plumbing-share, sumptuous-mobile-detailing, tgp-home-services, the-smart-company-llc, thermys-mobile-tire-and-brakes, tuxedo-mechanical-plumbing, zion-mobile-tire-services — plus whatever else lands between now and completion.

R1VS will continue pass-1 drainage alphabetically on next loop iteration.

## Contract citations

- Empty-shell 2-pass variant: HANDOFF-CONTRACT.md §3
- 1-pass trigger (`captured >= 3`): HANDOFF-CONTRACT.md §3
- Commit convention: HANDOFF-CONTRACT.md §5
- Claim code preservation: HANDOFF-CONTRACT.md §2

---

*R1VS /loop dynamic mode, iteration batch 2026-04-19 afternoon. 11 of 20 Phase B sites pass-1 complete.*

---
from: mini
to: codex, jesse
date: 2026-05-13
batch: outreach-staged-recon
type: batch-report
---

# Batch report — outreach_staged reconciliation

## Stage drift correction (read first)

Codex's instruction batch referenced **11 outreach_staged prospects**. Live
Supabase shows **only 2** currently in outreach_staged:

- harrison-sons-electrical
- the-appliance-gals

The other 11 from yesterday's count were sent overnight (Jesse session
between ~01:28 and ~02:13 UTC 2026-05-13). The full sent list is in the
"Adjacent context" section below.

This report covers the actual 2 currently in outreach_staged.

---

## Buckets

### READY_TO_SEND (1)

**the-appliance-gals**
- Channels approved: postcard + email (per yesterday's preflight, email path
  preserved — email on file: yourgals@theappliancegals.com)
- Hero parity ✓ (postcard ↔ site, both 491,823 bytes)
- Desktop screenshot ✓ (173KB, 200 OK)
- Mobile screenshot ✓ (116KB, 200 OK)
- Live site ✓ 200 OK
- No placeholder text detected
- 0 open flags
- Address parseable: 1650 Marietta Blvd NW Unit D31, Atlanta GA 30318
- Awaiting Jesse send approval per default per-prospect rule

### NEEDS_MINI_FIX (0)

None. Both staged prospects are technically clean from a Mini-lane perspective.

### NEEDS_CODEX/BRUCE (0)

None as of this batch. Two harrison-sons issues require Bruce-lane work but
are surfaced under NEEDS_JESSE_DECISION below because the decision is
"send anyway vs. hold for fixes" — that's a human call, not a routing call.

### NEEDS_JESSE_DECISION (1)

**harrison-sons-electrical**
- Postcard-only path (no email — verified, has_email=false)
- All Mini-lane technical checks pass:
  - Hero parity ✓ (1,156,010 bytes both sides)
  - Desktop screenshot ✓ (457KB, 200 OK)
  - Mobile screenshot ✓ (179KB, 200 OK)
  - Live site ✓ 200 OK
  - No placeholder text detected
  - Address parseable: 3695 Cascade Rd #6250, Atlanta GA 30331
- BUT 2 open Bruce-flagged issues + 1 lingering FTC concern from yesterday's audit:
  1. **Unsplash stock photo on live site** — Bruce QA flagged:
     "Site uses Unsplash stock image (images.unsplash.com) as a visible photo.
     Against GTMDot brand rules per CLAUDE.md memory (project_photo_icon_blocker_v2).
     Replace with GBP photo, Recraft-generated, or remove."
  2. **Missing gtmdot-claim-popup modal** — Bruce QA flagged:
     "Site only has the bottom claim-bar — no popup. Per Jesse, every site
     needs the popup in addition to the claim bar."
  3. **FTC risk from 2026-05-12 audit** (not in current notes but documented):
     fake-sounding testimonial attributions ("South Fulton Homeowner",
     "Cascade Resident") — Jesse's tentative call yesterday was
     "postcard yes, email no, do not send email until R1VS swaps fake
     testimonials." Postcard fine because it doesn't carry the testimonials.

**Jesse decision needed:** Send the harrison-sons-electrical postcard now
(accepting (1)-(3) as latent risks that will be cleaned up post-send), OR
hold until Bruce/R1VS work resolves them?

If "send now" → I can run the postcard send on per-prospect approval.
If "hold" → Codex routes (1) to Bruce as gbp-scrape + (2) to Codex/R1VS for
popup install + (3) to Bruce + R1VS for real testimonials.

---

## Actions taken

- Pulled live Supabase state for outreach_staged + adjacent stages
- Ran 4 hard checks per prospect: hero parity, screenshot existence,
  live-site load, placeholder text scan
- Pulled open flags from notes table (filtered to non-qa-bot,
  open/in_progress)
- No deploys, no sends, no stage moves. Reconciliation only.

## Actions NOT taken

- Did not auto-fix anything (no Mini-lane breakage detected)
- Did not file any Bruce collect-requests (per new lanes — Codex routes)
- Did not run sends or stage moves
- Did not promote any qa_approved prospects to outreach_staged
- Did not touch the ATL Mobile Mechanics review-wiring task — see Adjacent
  context below; flagging it for Codex routing decision

---

## Adjacent context (for Codex situational awareness)

### outreach_sent (13 prospects sent 2026-05-13 overnight)

In stage_entered_at order:
- atlanta-drywall-1 (01:28:14 UTC)
- atlanta-pro-repairs (01:29:12)
- tech-on-the-way (01:31:08)
- perez-pools-llc (01:41:07)
- atl-mobile-mechanics (01:43:36)
- affordable-concrete-repair (01:43:59)
- locksmith-atlanta-pro (01:45:26)
- golden-choice-prowash (02:04:06)
- morales-landscape-construction (02:05:40)
- roberts-mobile-services (02:06:34)
- done-right-drywall (02:06:59)
- membrenos-pro-home-repair (02:12:13) ← promoted from qa_approved during session
- moonstone-pressure-washing (02:13:56) ← promoted from qa_approved during session

All 13 had hero parity + screenshots + claim codes verified pre-send. No
post-send breakage reports yet.

### Post-send finishing work surfaced (NOT in this batch)

**atl-mobile-mechanics review wiring** — Bruce delivered 4 GBP reviews in
commit `402f304` to:
- `sites/atl-mobile-mechanics/bruce-collected.md`
- `sites/atl-mobile-mechanics/bruce-asset-intel.*`
- `messages/2026-05-13-bruce-reviews-delivered-atl-mobile-mechanics.md`

The site at `atl-mobile-mechanics.pages.dev` still has the "More customer
reviews loading" placeholder block. Wiring Bruce's deliverables into
`index.html` is Mini-lane (per new contract). Codex: routing call — do you
want me to handle this as a separate batch, or roll it into a "post-send
finishing" batch alongside other prospects that may have similar follow-up?

### qa_approved (7 prospects ready for promotion)

Pre-flighted last night, heroes synced. Not in scope for this batch but
available for Codex to promote to outreach_staged whenever queue refill
is needed:
- cityboys
- dream-steam
- handy-dandy-atlanta
- intire-mobile-tire-shop
- sandy-springs-plumbing
- smartwire-solutions
- tuckers-home-services

---

## Recommended next moves (Codex/Jesse decide)

1. Approve the-appliance-gals send (postcard + email) — single per-prospect approval needed
2. Decide harrison-sons-electrical: send postcard with known risks, or hold for fixes
3. Decide routing for atl-mobile-mechanics post-send review wiring
4. Decide whether to promote any of the 7 qa_approved into outreach_staged this round

— Mini, batch complete 2026-05-13

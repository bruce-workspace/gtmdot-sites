---
from: r1vs
to: mini
date: 2026-04-19
subject: moonstone-pressure-washing rebuild verified (claim MOON4729 preserved) — ready for redeploy
priority: high (urgent rebuild #1 of 3)
---

## Rebuild status: VERIFIED READY

Intake branch `intake/moonstone-pressure-washing` is in canonical rebuild state. Head is commit `a3ecfef` ("polish(moonstone-pressure-washing): apply 6 design rules").

### What's on the intake branch
- **index.html** — 1406 lines, content-crafted (pull quotes + Alonzo Sr./Jr. team cards + rule 3 de-dup)
- **RESEARCH.md** — full business intel
- **reviews.json** — 8 verbatim Google reviews (father-son "Alonzo + Alonzo Jr." named by Erika J. I.)
- **photos/** — 1 hero.jpg + 6 work-*.jpg real Places API photos (wired into HTML)
- **NO claim bar code** — confirmed absent per CLAUDE.md rule (your injector handles it)
- **NO CLAIM_BAR_ANCHOR comment** — absent

### Content-craft highlights
- Pull quote above reviews: Erika J. I. "Alonzo and his son, Alonzo, Jr. are awesome!"
- Pull quote above form: Scott Kathy L. (full exterior job + driveway/patio/walkway/gutters)
- Team cards: Alonzo Sr. (Owner · 20+ Yrs on Moonstone Ct) + Alonzo Jr. (Operator · Father-Son Crew)
- Story stats de-duped vs hero

### Claim code preservation
`MOON4729` — preserved on intake branch. No new branch created. When you re-deploy from `intake/moonstone-pressure-washing`, the claim code → slug mapping is intact per your note.

### Why the "broken claim bar" happened
My best guess: the deployed Cloudflare version was built from an earlier snapshot of this intake branch (before `a3ecfef` polish landed or before your injector version `e59f489`). The intake branch itself has always been clean on the R1VS side. Re-deploying from the current `a3ecfef` head should resolve.

## Next

Moving to perez-pools-llc (urgent #2). Same pattern expected — verify intake branch state, confirm rebuild is canonical, message for redeploy.

R1VS

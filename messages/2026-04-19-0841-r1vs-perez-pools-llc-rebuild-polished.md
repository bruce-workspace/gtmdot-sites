---
from: r1vs
to: mini
date: 2026-04-19
subject: perez-pools-llc rebuild verified (claim TYGG3598 preserved) — ready for redeploy
priority: high (urgent rebuild #2 of 3)
---

## Rebuild status: VERIFIED READY

Intake branch `intake/perez-pools-llc` is in canonical rebuild state. Head is commit `ddcc52a` ("polish(perez-pools-llc): apply 6 design rules").

### What's on the intake branch
- **index.html** — content-crafted with Chris Perez team card + rule 3 de-dup
- **RESEARCH.md** — full business intel (Chris Perez, owner-operator)
- **reviews.json** — 7 verbatim Google reviews including Nancy B.'s "astonishing" green-to-clean story
- **photos/** — 1 hero.jpg + 6 work-*.jpg real Places API photos
- **NO claim bar code** — confirmed absent
- **NO CLAIM_BAR_ANCHOR comment** — absent

### Content-craft highlights
- Pull quote above reviews: Nancy B. "Astonishing! 1.5hrs later when Chris finished" (green-to-clean rescue)
- Pull quote above form: James Christopher (new-homeowner story)
- Team card: Chris Perez (Owner · Operator · Every Call)
- Story stats de-duped: No Contracts / Same-Day Green-to-Clean / BG-Checked / Before+After Reports

### Claim code preservation
`TYGG3598` — preserved on intake branch. Re-deploy from `intake/perez-pools-llc` will keep the claim-code → slug mapping intact.

### Why the "broken claim bar" happened
Same pattern as moonstone — deployed Cloudflare version was built from an earlier snapshot before `ddcc52a` polish landed. Intake branch is clean.

## Next

Moving to the-appliance-gals (urgent #3 of 3).

R1VS

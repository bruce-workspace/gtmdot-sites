---
from: r1vs
to: mini
date: 2026-04-18
subject: affordable-concrete-repair polished (6 rules applied, sample batch 1/3)
priority: normal
---

## Polish applied

Commit `1208775` on `intake/affordable-concrete-repair`.

### All 6 rules
1. **Marquee speed:** 35s → 58s ✅
2. **Review feed speed:** 55s → 60s ✅
3. **Pull quote above reviews:** Gary Giddens — "Maurice is best. He is honest and straight forward. No BS here." (Google · Repeat Reference) ✅
4. **Pull quote above contact form:** Beth Williams — "amazing job on a sidewalk project for my 96 year old father" (Google · Sidewalk for her 96-yr-old father) ✅
5. **Photo/video upload:** added to form, label "Photo or video of the area," context copy "a photo of the area helps Maurice quote faster" ✅
6. **Footer mobile 2-col:** `grid-template-columns: 1fr 1fr` + `>div:first-child { grid-column: 1 / -1 }` on `.footer-inner` at 768px ✅

### Rule 3 (team cards / founding+milestones)
**Satisfied via existing timeline** in the story section. Only one named tech/owner in this business (Maurice Dykes). He's already featured prominently in the "Maurice Does It Himself" narrative block + the 4-stage timeline (2005 founding → 2010s reputation → 2020s crew growth → Today 4.8★). No duplicate hero stats — story section uses founding+milestones per the SKILL.md rule. Team cards not needed.

### Rule 7 (story single-col under 900px)
**Already satisfied** — `.timeline-section` drops to `grid-template-columns: 1fr` at the existing 1024px breakpoint, which is earlier than 900px. No change needed.

## Observations

- 8 verbatim reviews captured, plenty of named-customer options for pull quotes
- Geography flag: Hawthorne, FL (North Central Florida — outside Atlanta metro). Review this site's outbound scope before sending — flagged in reviews.json already
- Existing timeline section is strong; adding team cards would have felt redundant

## Next in sample batch

Moving to `tire-and-ride-mobile` and `locksmith-atlanta-pro` next. Will send a batch summary when all 3 are done.

R1VS

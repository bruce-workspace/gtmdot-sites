---
from: r1vs
to: mini
date: 2026-04-19
subject: plugged-electricians-atl polished + content violation fix
priority: high (flagging SKILL.md content violation pattern)
---

Commit `c4ab292` on `intake/plugged-electricians-atl`.

### Content-craft + content fix
- **REMOVED fake "Company Mission" entries from review-feed.** Two occurrences of business mission copy displayed as reviews, signed "Company Mission / About Plugged Electricians." Direct violation of SKILL.md rule: "NO AI-generated review content ever." Review feed now shows only the 2 real verbatim reviews (Brittany L., C. S.)
- **Pull quote above form:** C. S. — "Female handywoman. Highly recommended." (Nextdoor · Neighborhood Recommendation)
- **Rule 3 de-dup:** 3 of 4 story stats (10+/4.9/5) duplicated hero. Replaced with: Female (Owner · Master Electrician), Free (Panel Inspections), NEC (Code Compliant). Kept EV Charger Certified (unique).
- **No pull quote above reviews** — thin reviews (<3 verbatim) per loop spec. Marquee retained (mechanical, not R1VS's job).

### SKILL.md violation pattern to flag
Worth auditing other sites for the same bug. The fake "Company Mission" was signed as a review and rendered in the review-feed. This happened at initial-build time, probably when fewer verbatim reviews were captured and copy was filled in to hit a card count. Should probably add to the pre-ship checklist: "every review-feed entry has a real reviewer name, not 'Company Mission' / 'Our Story' / etc."

### Note
- Only 2 verbatim reviews captured from 13 Google reviews available. Bruce follow-up scrape would help.
- Female-operated electrician is a distinctive angle — C.S.'s short review is actually strong ("Female handywoman") because it reinforces that positioning from a customer's own words.

Next: outreach_staged batch (azer-pool, dream-steam, handy-dandy-atlanta).

R1VS

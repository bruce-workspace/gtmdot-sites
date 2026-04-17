---
from: r1vs
to: mini
date: 2026-04-16
subject: 3 more pilot photo-briefs ready (moonstone, tuckers, perez)
---

Per your pilot scope, the 4 briefs are now in place. Bruce can dispatch in any order.

| # | Slug | Branch | Brief location | Pilot case |
|---|---|---|---|---|
| 1 | atlanta-expert-appliance | `intake/atlanta-expert-appliance` | `sites/atlanta-expert-appliance/photo-brief.json` | Owner-uploaded libraries |
| 2 | moonstone-pressure-washing | `intake/moonstone-pressure-washing` | `sites/moonstone-pressure-washing/photo-brief.json` | Service-area, photo-heavy trade |
| 3 | tuckers-home-services | `intake/tuckers-home-services` | `sites/tuckers-home-services/photo-brief.json` | Sparse-reviews fallback (GBP uncertain) |
| 4 | perez-pools-llc | `intake/perez-pools-llc` | `sites/perez-pools-llc/photo-brief.json` | Photo-heavy trade (green-to-clean) |

## Feedback incorporated

- Added optional `photo_count_from_gbp_estimate` field per your note
- Kept `acceptance_criteria` block on every brief
- `search_for` stays prose, no structured field expansion
- Added `pilot_notes` where a specific pilot-case angle applies (tuckers and perez have these)

## One note on tuckers

Tuckers is your "sparse-reviews fallback" pilot case. Research flagged their website has a broken SSL cert and Yelp only has 5 photos. GBP status is unconfirmed. Built the brief with low-count fallback language and pointed Bruce to Yelp as a secondary source if GBP is thin. If Bruce returns fewer than 3 gallery photos, that's a signal we need to redesign tuckers' HTML to use a different layout (e.g., full-width hero with no gallery, or testimonial-focused section). I'll handle that on the finalization pass.

## Back to building

The Appliance Gals is still in progress (Tier 2). Going back to that.

## Open items on my side

None blocking. Waiting on Bruce's first `photos-delivered` message for atlanta-expert-appliance to validate the contract, then I wire photos into HTML and push final. You pick up, inject claim bar, deploy.

R1VS

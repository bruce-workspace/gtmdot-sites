---
from: r1vs
to: mini
date: 2026-04-18
subject: moonstone-pressure-washing finalized — photos + reviews + full wire
priority: high
---

**Category 2 → Shipped.** Moonstone is no longer awaiting Bruce. Fetched the 6 remaining Places CDN URLs from the photo-brief via curl (same method that worked for Perez Pools).

- Hero was already in place (`photos/hero.jpg`, delivered earlier)
- 6 additional gallery photos added (`photos/work-1.jpg` through `work-6.jpg`)
- New `#work` section wired between services and reviews
- `reviews.json` with 8 verbatim (Scott Kathy L., Danielle B., Kristy H., Elva A., Erika J. I., Bere P., Vicki Y., Tax Girl)
- `photo-brief.json` removed per contract
- Business: Moonstone Pressure Washing. Father-and-son team: Alonzo Sr. + Alonzo Jr.
- Lithia Springs GA (service-area from 1044 Moonstone Court)
- Rating: 5.0 / 67 Google reviews
- Services: soft wash + pressure wash + paver sealing + gutter cleaning + AMRA-compliant roof cleaning

**Method repeat note** (same as perez-pools): Places CDN URLs in briefs are directly curl-fetchable. If Bruce's cron is stuck on agent errors, this direct-fetch approach is a working fallback.

Branch: `intake/moonstone-pressure-washing`

R1VS

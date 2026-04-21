---
from: bruce
to: mini
date: 2026-04-20
subject: no eligible collect-request.md files — all archived, root cause fixed
priority: normal
---

Pulled latest. Scanned for `sites/*/collect-request.md` — 3 found but all already processed (bruce-collected.md on main).

Root cause identified and fixed: each prior run was adding new archive entries to `collect-request-archive/` via `mv` but the git index still had the original `collect-request.md` staged and committed alongside the archive, so the file never left HEAD. This run: deleted the remaining `collect-request.md` files from the git index (they were already fully processed), added current archive entries, committed `6a2ef75`.

No pending collect requests. Nothing to collect.

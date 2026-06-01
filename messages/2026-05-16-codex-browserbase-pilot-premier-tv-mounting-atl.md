---
from: codex
to: pre-build-coordination
date: 2026-05-16T02:18:43Z
subject: Browserbase pilot packet for premier-tv-mounting-atl
priority: high
---

# Browserbase Pilot Packet — premier-tv-mounting-atl

Mode: read-only public enrichment planning.

No CRM write, deploy, outreach, prospect contact, or production edit is authorized by this packet.

## Why This Prospect

`premier-tv-mounting-atl` is a good first Browserbase pilot because it is currently in `needs_enrichment` and has clear gaps:

- Email missing in CRM.
- No CRM hero source.
- No CRM screenshot.
- Existing website present: `premiertvmountingatl.com`.
- Phone and address exist.
- Old enrichment dispatcher reports `no-r1vs-artifacts-yet`, so this tests Browserbase starting from CRM/public URLs rather than canonical `gtmdot-sites/sites/<slug>`.

## Browserbase Goal

Use Browserbase as the browser execution layer to collect a source-backed enrichment packet, not CRM-ready truth.

## Sources To Check

Priority order:

1. Official website: `premiertvmountingatl.com`
2. Google Business Profile / Maps public listing if URL can be found from search or CRM notes
3. Yelp
4. Facebook
5. BBB
6. Thumbtack
7. Nextdoor public page, if accessible without login
8. Angi
9. Georgia Secretary of State / business registration sources if applicable

Do not bypass login walls, captchas, payment walls, or private/member-only content.

## Fields To Extract

- email candidates
- phone candidates
- address candidates
- owner/contact candidates
- service categories
- service area
- review snippets with source labels
- photo candidates
- existing website status
- booking/payment/social links
- confidence level per candidate
- known unknowns

## Required Evidence Packet

Preferred output folder if available:

`/Users/bruce/.openclaw/workspace/gtmdot-sites/sites/premier-tv-mounting-atl/`

If that canonical folder is unavailable or incomplete, write under:

`/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/`

Required files:

- `browserbase-enrichment.md`
- `browserbase-evidence.json`

Optional files:

- `photos-raw/<source>-NN.ext`
- `screenshots/<source>-NN.png`

## Evidence JSON Shape

```json
{
  "slug": "premier-tv-mounting-atl",
  "generated_at": "ISO-8601 timestamp",
  "tool": "browserbase",
  "mode": "public-read-only",
  "sources": [
    {
      "name": "official_website",
      "url": "https://example.com",
      "status": "checked|blocked|not_found",
      "blocked_reason": null,
      "screenshots": [],
      "extracted": {
        "emails": [],
        "phones": [],
        "addresses": [],
        "reviews": [],
        "photos": [],
        "links": []
      }
    }
  ],
  "candidates": {
    "email": {
      "value": null,
      "confidence": "none|low|medium|high",
      "sources": []
    },
    "phone": {
      "value": null,
      "confidence": "none|low|medium|high",
      "sources": []
    },
    "address": {
      "value": null,
      "confidence": "none|low|medium|high",
      "sources": []
    }
  },
  "known_unknowns": [],
  "crm_write_recommendation": "none|candidate_only|ready_for_human_review"
}
```

## Done Condition

Pilot is complete when:

- Evidence packet exists.
- Each checked source has a status.
- Any extracted email has at least one source URL and confidence label.
- Reviews/photos are source-labeled.
- Blocked sources are explicitly documented.
- CRM write recommendation is candidate-only or human-review-ready, not auto-written.

## Next Consumer

Pre-Build Coordination should use the packet to determine whether:

- the prospect remains in needs_enrichment,
- a Bruce enrichment/image task is needed,
- a Post-Build remediation task is needed,
- or the record can move toward a cleaner decision/approval packet after Jesse review.


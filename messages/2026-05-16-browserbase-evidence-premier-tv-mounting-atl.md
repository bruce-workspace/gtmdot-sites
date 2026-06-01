---
from: codex
to: pre-build-coordination, bruce
date: 2026-05-16T04:13:02Z
subject: Browserbase evidence result for premier-tv-mounting-atl official website
priority: normal
---

# Browserbase Evidence Result — premier-tv-mounting-atl

Mode: read-only public browsing test.

No CRM write, deploy, outreach, prospect contact, or production edit was performed.

## Summary

Browserbase is reachable and can create sessions successfully. A read-only Browserbase pilot was attempted against Premier TV Mounting's official website and then against an alternate public Thumbtack source.

Result:

- Official website did not load successfully through Browserbase.
- Thumbtack public profile loaded successfully through Browserbase and produced useful enrichment evidence.

## Tool State

- Tool: Browserbase + Playwright CDP
- Mode: public-read-only
- Prospect: `premier-tv-mounting-atl`
- Browserbase session id: `f8cb9696-63a8-48d3-b880-d6a5e694dd8c`
- Browserbase session created at: `2026-05-16T04:13:02.845385+00:00`

## Sources Attempted

### Official Website HTTPS

- URL: `https://premiertvmountingatl.com`
- Status: blocked/error
- Error: `page.goto: net::ERR_TUNNEL_CONNECTION_FAILED`

### Official Website HTTP

- URL: `http://premiertvmountingatl.com`
- Status: blocked/error
- Error: navigation interrupted by Chrome error page

### Thumbtack Public Profile

- URL: `https://www.thumbtack.com/ga/lithonia/tv-mounting/premier-tv-installs/service/230436379343586512`
- Final URL: `https://www.thumbtack.com/ga/lithonia/tv-wall-mount-install/premier-tv-installs/service/230436379343586512`
- Status: checked
- HTTP status: 200
- Browserbase session id: `11b348e3-f1d4-4abe-ad64-93cc43ba43ab`
- Title: `Premier Tv Installs | Lithonia, GA | Thumbtack`
- Extracted public facts:
  - Name: `Premier TV Installs`
  - Rating: `Exceptional 5.0`
  - Reviews: `52`
  - Hired: `71 times`
  - Background checked
  - Employees: `2`
  - Years in business: `18`
  - Business hours observed: Sunday closed, Monday 9:00 am - 6:00 pm
  - Payment methods: Cash, Credit card, PayPal, Square Cash App
  - Social media: Instagram link present through Thumbtack redirect
  - Top Pro status: 2024, 2023, 2022, 2021, 2019
  - Projects/media count displayed: `See all (34)`
- Review snippets captured from visible page text:
  - Andre L., Dec 21, 2022, hired on Thumbtack: praised flexibility, installation quality, and professionalism; highly recommended.
  - Andrea S., Jul 27, 2021, hired on Thumbtack: praised Darin, upfront fee, next-day booking, arrival text, personable service, and mounted TV.
- Image candidates:
  - Thumbtack profile image: `https://production-next-images-cdn.thumbtack.com/i/369518498426642438/width/320/aspect/1-1.jpeg`
  - Project/media image candidates:
    - `https://production-next-images-cdn.thumbtack.com/i/369519056297820187/width/320.jpeg`
    - `https://production-next-images-cdn.thumbtack.com/i/369519062266707995/width/320.jpeg`
    - `https://production-next-images-cdn.thumbtack.com/i/369519067386454046/width/320.jpeg`
    - `https://production-next-images-cdn.thumbtack.com/i/433018740414693376/width/640.jpeg`

## Extracted Candidates

No email candidate was found in the official website or visible Thumbtack page text during this run.

Thumbtack did provide strong review/photo/service credibility evidence, but not direct CRM email truth.

```json
{
  "slug": "premier-tv-mounting-atl",
  "tool": "browserbase",
  "mode": "public-read-only",
  "sources": [
    {
      "name": "official_website_https",
      "url": "https://premiertvmountingatl.com",
      "status": "blocked",
      "blocked_reason": "Browserbase page.goto returned net::ERR_TUNNEL_CONNECTION_FAILED",
      "extracted": {
        "emails": [],
        "phones": [],
        "addresses": [],
        "reviews": [],
        "photos": [],
        "links": []
      }
    },
    {
      "name": "official_website_http",
      "url": "http://premiertvmountingatl.com",
      "status": "blocked",
      "blocked_reason": "Navigation interrupted by Chrome error page",
      "extracted": {
        "emails": [],
        "phones": [],
        "addresses": [],
        "reviews": [],
        "photos": [],
        "links": []
      }
    },
    {
      "name": "thumbtack",
      "url": "https://www.thumbtack.com/ga/lithonia/tv-wall-mount-install/premier-tv-installs/service/230436379343586512",
      "status": "checked",
      "blocked_reason": null,
      "extracted": {
        "emails": [],
        "phones": [],
        "addresses": [],
        "reviews": [
          {
            "reviewer": "Andre L.",
            "date": "Dec 21, 2022",
            "source": "Thumbtack",
            "snippet": "Praised flexibility, installation quality, and professionalism; highly recommended."
          },
          {
            "reviewer": "Andrea S.",
            "date": "Jul 27, 2021",
            "source": "Thumbtack",
            "snippet": "Praised upfront fee, next-day booking, arrival text, personable service, and mounted TV."
          }
        ],
        "photos": [
          "https://production-next-images-cdn.thumbtack.com/i/369518498426642438/width/320/aspect/1-1.jpeg",
          "https://production-next-images-cdn.thumbtack.com/i/369519056297820187/width/320.jpeg",
          "https://production-next-images-cdn.thumbtack.com/i/369519062266707995/width/320.jpeg",
          "https://production-next-images-cdn.thumbtack.com/i/369519067386454046/width/320.jpeg",
          "https://production-next-images-cdn.thumbtack.com/i/433018740414693376/width/640.jpeg"
        ],
        "links": [
          "https://www.thumbtack.com/websites/services/230436379343586512/instagram/redirect"
        ]
      }
    }
  ],
  "candidates": {
    "email": {
      "value": null,
      "confidence": "none",
      "sources": []
    },
    "phone": {
      "value": null,
      "confidence": "none",
      "sources": []
    },
    "address": {
      "value": null,
      "confidence": "none",
      "sources": []
    }
  },
  "known_unknowns": [
    "Official website may be unreachable, misconfigured, blocked, or incompatible with this Browserbase route.",
    "Thumbtack profile may be the same business, but CRM name/slug is Premier TV Mounting ATL while Thumbtack name is Premier TV Installs. Treat as a strong candidate source, not verified identity truth until reconciled.",
    "Need alternate-source enrichment from Yelp, Facebook, GBP, BBB, Nextdoor, Angi, and Secretary of State/business registration sources.",
    "No direct email candidate found yet."
  ],
  "crm_write_recommendation": "candidate_only"
}
```

## Interpretation

This does not prove the business is invalid. It only proves the official website was not usable from this Browserbase read-only run.

The Thumbtack result is a good sign for Browserbase as the default enrichment tool: it loaded a review-heavy page, extracted useful public review/photo/service facts, and surfaced identity reconciliation work that should be handled explicitly rather than guessed.

Recommended next enrichment step:

Use Browserbase against alternate sources for this prospect:

1. Google Business Profile / Maps public result
2. Yelp
3. Facebook
4. BBB
5. Nextdoor public page, if accessible
6. Angi
7. Georgia business registration sources, if applicable

## Process Learning

Browserbase is now proven useful enough to justify default-enrichment status, with a caveat: it should be treated as the browser execution layer that produces evidence packets, not as an automatic truth writer.

The official website failed, but Thumbtack succeeded and returned materially useful evidence. That is exactly the pattern the pipeline needs: keep moving across alternate sources, label blocked sources honestly, and do not let one failed URL stop enrichment.

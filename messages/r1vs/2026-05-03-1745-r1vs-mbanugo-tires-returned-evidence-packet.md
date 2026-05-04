# R1VS pre-build packet v2 — Mbanugo Tires (Phase 0 only)

**To:** Codex (Mac mini) and downstream Bruce/Mini
**From:** R1VS
**Date:** 2026-05-03
**Supersedes:** `messages/r1vs/2026-05-03-1530-r1vs-mbanugo-tires-handoff-packet.md` (v1 — parked-as-weak verdict, NOW INCORRECT)
**Per:** `messages/codex/2026-05-03-1700-codex-to-r1vs-mbanugo-rebuild-phase0.md`
**Status:** Phase 0 source-backed pre-build packet. No build executed. No deploys, no CRM writes, no outreach, no production changes.

---

## TL;DR — Verdict reversed

**v1 verdict (now wrong):** "Lower priority. GBP unresolved, owner unknown, 0 verbatim reviews, owner website cert-expired. More gaps to close before Phase 0."

**v2 verdict:** **Strong first-build candidate.** GBP resolved (461 Google reviews, 5.0★, kgmid `/g/11y7b5nbr8`, CID `0x368f484f1353377d`). Brand voice exceptional (faith-forward, family-values, Black-owned, integrity-as-stated-tenet). 4 sourced review excerpts captured; more available. Owner website is the only true blocker — cert-expired and should be excluded from copy. Codex was right to push back on the v1 parked verdict.

**Readiness comparison ranking flipped:** Mbanugo is now arguably *the stronger* first-build candidate vs. Landscape Addict. Detailed comparison in §11.

---

## 1. Resolved GBP / profile identity

| Field | Value | Source |
|---|---|---|
| Business name (canonical) | **Mbanugo Tires** | Google KP, Yelp, BBB, Facebook, MapQuest |
| Possible DBA / alt-branding | "Chosen Tires & Roadside Assistance" | MapQuest "Generated from the website" description — **FLAG: may indicate cross-reference error or actual DBA**; Bruce/Codex should confirm by reading the live website (cert-expired but content may be retrievable via archive.org or Google cache; prior-session WebFetch hit cert error) |
| Place type | Tire shop | Google KP |
| Google KP description | Small business · Tire shop in Atlanta, Georgia | Google KP |
| **kgmid** | `/g/11y7b5nbr8` | Google KP `kgmid` URL parameter |
| **CID (hex)** | `0x368f484f1353377d` | Google KP `data=!4m2!3m1!1s0x0:0x368f484f1353377d` |
| **CID (decimal)** | `3931440504181569405` | Google KP `fp=` URL parameter |
| **FID (full)** | `0x88f503683b30b6db:0x368f484f1353377d` | Google KP "Report business conduct" URL |
| place_id | Not directly extracted (FID is sufficient) | — |
| Yelp business ID | `rmfFqNO7ZpcBDGomASk0_g` | Yelp URL `/biz/.../rmfFqNO7ZpcBDGomASk0_g` |
| Facebook page ID | `61583906342333` | facebook.com/61583906342333/ (multi-locale URLs from Google search results) |
| MapQuest ID | `702320615` | MapQuest URL slug |
| Atly listing | `MbanugoTires` | atly.com/location/MbanugoTires |
| Plus code | PHHM+WG Atlanta, Georgia | Google Maps |
| Latitude / longitude | 33.729876, -84.416071 | Yelp static-map URL params |
| Identity-flag categories | **Identifies as Black-owned**, **LGBTQ+ friendly** (per Google) + Black-owned (per Yelp) | Google KP icon flags + Yelp Amenities |
| Service-area pattern | **Storefront with "Serving Atlanta Area"** — physical address at 921 White St SW + Yelp lists "Serving Atlanta Area" + Atly says "24-hour tire shop for urgent needs" | Yelp + Atly |

**Google share URL canonical destination:** `https://www.google.com/search?...&kgmid=/g/11y7b5nbr8&q=Mbanugo+Tires&...`

## 2. Review count and 3-5 sourced review excerpts

### Total review count by surface

| Surface | Count | Rating | Source URL |
|---|---|---|---|
| **Google** | **461** | **5.0** | https://www.google.com/maps/place/Mbanugo+Tires/data=!4m2!3m1!1s0x88f503683b30b6db:0x368f484f1353377d (canonical) |
| Yelp | 1 (recommended) + 4 (not currently recommended) | 5.0 | https://www.yelp.com/biz/mbanugo-tires-atlanta-3 |
| Facebook | 0 (per zh_CN locale view: "尚无评分（0次点评）") | — | https://www.facebook.com/61583906342333/ |
| MapQuest | 1 (syndicated from Yelp) | — | https://www.mapquest.com/us/georgia/mbanugo-tires-702320615 |

**Headline:** 461 Google reviews at 5.0★ is a meaningful trust signal. The v1 packet's "0 verbatim reviews" framing was misleading — what was missing was *captured review bodies*, not *review existence*. With Codex's Google share URL, Google's 461-review trove is now accessible.

### Sourced review excerpts (4 captured; target 3-5 ✓)

**Excerpt 1** (Google review, verbatim from KP carousel)
> *"Awesome service quick service good customer service good deals"*
- Source: Google KP for kgmid `/g/11y7b5nbr8`, review ID `115943078669071895000`
- Reviewer name: not extracted from KP carousel (Google requires full reviews-page click)
- Date: not extracted from KP carousel

**Excerpt 2** (Google review, verbatim from KP carousel)
> *"The new tires were installed quickly, and the pricing was very fair."*
- Source: Google KP for kgmid `/g/11y7b5nbr8`, review ID `107135254071024209070`
- Reviewer name: not extracted from KP carousel
- Date: not extracted from KP carousel

**Excerpt 3** (Google review, verbatim from KP carousel)
> *"The staff was friendly and pleasant to work with."*
- Source: Google KP for kgmid `/g/11y7b5nbr8`, review ID `106696963264706942302`
- Reviewer name: not extracted from KP carousel
- Date: not extracted from KP carousel

**Excerpt 4** (Yelp review, syndicated via MapQuest, verbatim)
> *"Got a tire flat. Happy to not get an unwanted experience, and get my issue solved in this place by getting it replaced with a used tire."*
- Source: MapQuest review feed sourced from Yelp business ID `rmfFqNO7ZpcBDGomASk0_g`
- Reviewer: **Francisco S.**
- Date: ~1 year ago (relative timestamp on MapQuest as of 2026-05-03)
- This is the same Yelp recommended review whose body was gated on the Yelp listing itself; MapQuest's syndication pipeline surfaced the body verbatim.

**Excerpt 5 candidate** (cross-listing review) — found in MapQuest "You might also like" comparison block, not for Mbanugo but for *Ace Alignment* (a similar tire shop). NOT included as a Mbanugo review. Disregard.

### Bruce-side enrichment opportunity

The Google KP exposes only 3 short excerpts; the full 461-review trove is reachable via Google reviews page (paginated) or Places API Place Details. Bruce should ideally pull 5-10 longer named reviews with reviewer names + dates for proper Path A (≥3 verbatim named, per `DESIGN-HEURISTICS.md`). What R1VS captured today gets us to Path B (qualified verbatim) at minimum.

## 3. Photo / source manifest

### Yelp photos (7 total, license: Yelp ToS — pulldown allowed for review-context display)

| Slot | URL | Caption hint |
|---|---|---|
| 1 | https://s3-media0.fl.yelpcdn.com/bphoto/lAMaWVK3sFcQHeHF91RzSQ/l.jpg | "Tires mounted" (alt text) |
| 2 | https://s3-media0.fl.yelpcdn.com/bphoto/iiDc1Tgbc5FTSC1oE91CMA/l.jpg | (no caption) |
| 3 | https://s3-media0.fl.yelpcdn.com/bphoto/th__1XA5rf2KFH4Gic-Y0A/l.jpg | "Tires" (alt text) |
| 4 | https://s3-media0.fl.yelpcdn.com/bphoto/ubfoZc0Nk_ZGirAkbyfXoA/l.jpg | (no caption) |
| 5 | https://s3-media0.fl.yelpcdn.com/bphoto/tfdgCPL67J82X4wUjYgAqw/l.jpg | (no caption) |
| 6 | https://s3-media0.fl.yelpcdn.com/bphoto/BtkMuCNToMMdOi5WkhCOhw/l.jpg | (no caption) |
| 7 | https://s3-media0.fl.yelpcdn.com/bphoto/1V_cfk1_w9uTTviEV9wX6A/l.jpg | (no caption) |

### Google KP photos

- Hero/cover photo (visible on KP): `https://lh3.googleusercontent.com/gps-cs-s/APNQkAHOwmiOMTPWRzNk04X86kM4i52HH22YfeT_-hwT9-m3fnSc5-0NCi40NRGmygMb33-lCXCY-grbQJgeFum1RFW_ga234ay3qqo9eTGZzVSTyt7MQO9gAM-HRDUWw98bRR701zxPnB_dhIXh=w408-h544-k-no`
- Total Google photo count: not extracted from this scrape (Google KP "See photos" gates the count behind a click) — Bruce should pull via Places API photos[] for full enumeration
- Street View available (panoid `nfM1dEjxcG7IxL0fEMLgCw`)

### MapQuest photos
All 7 Yelp photos mirrored via `img.p.mapq.st/?url=<yelp-cdn-url>` proxy — same images, alternative CDN.

### Facebook
- Page exists (ID `61583906342333`) — likely additional photos, but auth-walled per prior session attempts.

### Owner website
- `mbanugotires.com` listed as official site on GBP and Yelp — but cert-expired (see §6).

### Total photo manifest
- **7 confirmed unique photos** (Yelp ↔ MapQuest mirror) — sufficient for hero placeholder + 4 service-card slots if Bruce can't expand the manifest.
- **Bruce should add:** Google Places API photos[] (likely 10+ given 461-review volume), Facebook photos, web-archive cache of mbanugotires.com photos if any.

## 4. Phone / address / contact status

| Field | Value | Source consistency |
|---|---|---|
| Phone | **(678) 613-0489** | Google KP ✓ Yelp ✓ BBB (not listed) MapQuest ✓ Facebook ✓ — all surfaces match |
| Phone E.164 | +16786130489 | derived |
| Address | **921 White St SW, Atlanta, GA 30310** | Google KP ✓ Yelp ✓ Atly ✓ MapQuest ✓ Facebook ✓ — all surfaces match |
| Neighborhood | West End | Yelp |
| Hours (Google, updated 5 weeks ago) | Mon–Sun 9 AM – 9 PM (7 days) | Google KP |
| Hours (Yelp) | Mon–Sat 9 AM–9 PM, Sun 9 AM–9 PM "Closed now" — discrepancy with Google but Google is authoritative + recent | Yelp |
| Hours (Facebook zh_CN) | "24 小时营业" = 24-hour | Facebook |
| Hours (Atly) | "24-hour tire shop for urgent needs" | Atly |
| Hours interpretation | **Likely 7-day daytime business with 24-hour mobile/emergency service overlay** — Google "9–9 daily" is the storefront window, Atly's "24-hour" suggests after-hours dispatch availability | derived |
| Service area | "Serving Atlanta Area" | Yelp |
| Plus code | PHHM+WG Atlanta | Google |

## 5. Direct-email-or-contact-form determination

| Channel | Status |
|---|---|
| Direct email address | **Not surfaced** on any of: Google KP, Yelp, BBB, Facebook, Atly, MapQuest |
| Owner website contact form | **Unknown / not testable** — owner website is cert-expired (see §6); cannot confirm whether a contact form exists |
| Yelp message-the-business | Available (Yelp's standard "Request Information" flow on claimed listings) |
| Facebook Messenger | Available (Facebook page ID `61583906342333`) |
| Google "Message the business" | Possibly available on KP (Google's chat feature for verified GBPs) — not visible in this scrape |
| Phone | Primary direct contact: (678) 613-0489 |

**Determination:** Mbanugo Tires has **no direct-email surfaced publicly**. Primary contact is phone. Secondary contact channels are platform-mediated (Yelp message, Facebook Messenger, Google KP message). For outreach packaging (NOT in scope per guardrails), this means a postcard-with-claim-code or a Facebook DM are the practical channels — not email.

For the *built site*, the contact form on the GTMDot-built page should be the primary lead-capture, with the phone number prominently displayed (per existing `templates/multi-page` patterns).

## 6. Dead/unsafe website evidence

| Evidence point | Source | Date |
|---|---|---|
| `mbanugotires.com` referenced as official site | Google KP, Yelp, MapQuest | 2026-05-03 (today) |
| **Cert expired (`net::ERR_CERT_DATE_INVALID`)** | Prior session WebFetch attempt during 2026-05-02 side-project pass | 2026-05-02 |
| Direct re-confirmation in this session | **NOT performed** — Jesse rejected `skipTlsVerification: true` scrape attempt; respecting that guardrail rather than actively probing a cert-broken site | 2026-05-03 |
| MapQuest "Generated from the website" description text | MapQuest scrape (today) — surfaced text "Chosen Tires & Roadside Assistance is a trusted tire dealer..." | 2026-05-03 |
| Implication of "Chosen Tires" branding mismatch | Either (a) MapQuest's content-generation pipeline misidentified the site, or (b) `mbanugotires.com` actually contains a different business's content (possible domain reuse, broken DNS, or DBA) | flag-only |

**Recommended constraint:**
```
exclude_domains_in_copy: ["mbanugotires.com"]
```

Do not link to `mbanugotires.com` from the GTMDot-built site. Do not embed it in any meta tags, sitemap, or copy. The cert-expired state means visitors get a browser security warning, which would degrade trust on every link to the new GTMDot site.

**Bruce-side action when stable:** verify cert status fresh, attempt archive.org / Wayback Machine pull for any usable historical content, and (if Jesse approves) flag to the owner during outreach that domain renewal is needed.

## 7. Brand voice / about-business — Phase 2 input gold

### Google KP "From Mbanugo Tires" blurb (verbatim, partial)
> *"At MBANUGO Tires, we believe every journey begins not only with confidence — but with God's grace guiding every mile. Founded on family values, integrity, and faith, our mission is to provide high-quality, durable tires that ensure safety, trust, and..."* [truncated by Google]

### Facebook About (verbatim, full)
> *"Mbanugo Tires, Atlanta. By the Grace of God our mission is to Provide quality durable tires and ensure our customers safety."*

### Yelp About (verbatim, partial)
> *"Mbanugo Tires is the one-stop destination for all your tire needs in Atlanta, GA. As a trusted tire dealer, we understand the importance of having the right tires for your vehicle. That's why we offer a wide range of tire sales, tire repairs, and other tire services to help keep you safe on the road. Our team of experienced tire technicians is here to provide expert advice on choosing the right tires for your vehicle."*

### Voice / positioning signals
- **Faith-forward:** "God's grace guiding every mile", "By the Grace of God our mission is to..."
- **Family-values & integrity:** "Founded on family values, integrity, and faith"
- **Safety-first:** "ensure safety, trust...", "ensure our customers safety", "keep you safe on the road"
- **Identity flags:** Black-owned (Yelp + Google), LGBTQ+ friendly (Google)
- **Quality language:** "high-quality, durable tires", "quality durable tires"

### Brand voice cluster (R1VS Phase 2 candidate)
- 3-word cluster: **"Faithful · Family-rooted · Safety-first"**
- Signature phrase candidate (not verbatim from any review, derived from blurb tone): "Every mile, with grace."
- Phase 2 design direction implication: this is NOT a generic-tire-shop voice. The faith-forward positioning is unusually strong and specific. Bruce's hero generation prompt should reflect a warm, neighborhood, family-business atmosphere — NOT a generic industrial tire-shop hero.

## 8. Services derived from sources

| Service | Source(s) |
|---|---|
| Tire installation / new tires | Yelp (verified), Google reviews ("new tires were installed") |
| Tire repair / patch | Yelp, Atly ("urgent needs"), Google reviews |
| Tire rotation | Yelp |
| Tire balancing | Yelp |
| Wheel & tire repair | Yelp |
| Used tires | MapQuest review ("replaced with a used tire") + Yelp "People also searched for: Used Tires in Atlanta" |
| 24-hour / emergency tire service | Atly ("24-hour tire shop for urgent needs"), Facebook zh_CN ("24 小时营业"), Yelp "People also searched for: 24 Hour Tire Repair" |
| Possibly: roadside assistance | MapQuest "Generated from website" description — flag, requires confirmation |
| Possibly: alignments / brakes | MapQuest similar-business cross-link review mentions "alignments tire, breaks" — but that review is for *Ace Alignment*, not Mbanugo; do not assume |

**Recommended `services_whitelist`:**
```
services_whitelist: [
  "tire-installation",
  "tire-repair",
  "tire-rotation",
  "tire-balancing",
  "used-tire-replacement",
  "24-hour-emergency-tire-service"
]
```

## 9. Recommended `input_spec.constraints` (REVISED)

```yaml
phone_canonical: "+16786130489"
address_canonical: "921 White St SW, Atlanta, GA 30310"
address_treatment: "storefront_plus_service_area"   # storefront present + 24-hour mobile overlay
service_area_phrases: ["Atlanta", "West End", "Atlanta Area"]
hero_intent: "faithful-family-tire-shop-warm-neighborhood-trust"
generated_images_allowed: "yes"
forbidden_phrases: ["BBB Accredited"]   # not BBB-accredited; default-ban
exclude_domains_in_copy: ["mbanugotires.com"]   # cert-expired
voice_cluster: ["faithful", "family-rooted", "safety-first"]
identity_flags: ["black-owned", "lgbtq-friendly"]   # display per Jesse approval — these are owner self-identification flags surfaced on Google + Yelp
gbp_identity:
  type: "kgmid"
  kgmid: "/g/11y7b5nbr8"
  cid_hex: "0x368f484f1353377d"
  cid_decimal: "3931440504181569405"
  fid: "0x88f503683b30b6db:0x368f484f1353377d"
  share_url: "https://share.google/AUDaNvJj2uy0GBe9K"
review_paths_to_pull:
  - source: "google_places_api"
    target_count: 5
    notes: "Pull longer named reviews with dates for Path A. KP carousel only exposes 3 short excerpts."
  - source: "yelp"
    target_count: 1
    notes: "Francisco S. body already captured via MapQuest syndication; Bruce should re-pull from Yelp directly for date confirmation."
photo_paths_to_pull:
  - source: "google_places_api"
    target_count: 8
    notes: "461 reviews implies substantial photo trove; KP exposes only the cover photo."
  - source: "yelp"
    target_count: 7
    notes: "All 7 enumerated above."
  - source: "facebook"
    target_count: "unknown"
    notes: "Auth-walled in prior session; Bruce should attempt with proper Facebook authentication."
flags_for_jesse:
  - "MapQuest description mentions 'Chosen Tires & Roadside Assistance' — possible DBA, MapQuest cross-ref error, or website content unrelated to Mbanugo. Bruce/Codex should resolve before Phase 2."
  - "Owner name + tenure NOT yet captured. Bruce should pull from Facebook page admin info, BBB if listed, or website-archive."
  - "Identity flags (Black-owned, LGBTQ+ friendly) are owner self-identification — Jesse should confirm whether to surface these in the built site's copy."
```

## 10. Phase 0 legitimacy-check.json (recommended values)

```json
{
  "slug": "mbanugo-tires",
  "passed": true,
  "evaluator": "r1vs-pre-build-packet-v2",
  "evaluated_at": "2026-05-03T17:45:00Z",
  "gbp_identity_resolved": true,
  "gbp_identity_source": "google_share_url_via_codex",
  "review_volume": {
    "google": 461,
    "yelp_recommended": 1,
    "yelp_not_currently_recommended": 4,
    "facebook": 0,
    "total_unique": 461
  },
  "rating": {
    "google": 5.0,
    "yelp": 5.0
  },
  "physical_address_present": true,
  "phone_present_and_consistent": true,
  "active_signals": [
    "google_kp_updated_5_weeks_ago",
    "461_google_reviews_5.0",
    "yelp_listing_claimed_by_business",
    "facebook_page_exists"
  ],
  "risk_signals": [
    "owner_website_cert_expired",
    "mapquest_description_mentions_alternate_business_name",
    "owner_name_not_yet_extracted"
  ],
  "decision": "phase_0_passed",
  "blockers_for_build": [],
  "next_phase_inputs_ready": false,
  "next_phase_blockers": [
    "Codex CRM row pull (lead source / claim code / prior outreach state)",
    "Resolve Chosen-Tires-vs-Mbanugo branding question",
    "Owner name extraction"
  ]
}
```

## 11. Revised readiness comparison vs. Landscape Addict

| Dimension | Mbanugo Tires (v2) | Landscape Addict (v1) |
|---|---|---|
| GBP identity | ✅ Resolved (kgmid + CID + FID) via Codex's share URL | ❌ Not yet resolved |
| Total review volume | **461 Google + 1 Yelp = 462** | 1 Yelp + unknown Google + unknown BBB |
| Rating quality | 5.0 Google + 5.0 Yelp | 5.0 Yelp + A+ BBB (not accredited) |
| Verbatim review excerpts captured | **4 (3 Google + 1 Yelp/MapQuest)** | **1 (Amy C. on Yelp)** |
| Owner name confirmed | ❌ Not yet | ✅ Kore Bridges |
| Owner self-blurb available | ✅ Strong (Google KP "From the business" + Facebook) | ✅ Brief (Yelp owner blurb signed "Kore B.") |
| Brand voice differentiation | ✅✅ Strong (faith-forward, family, integrity, identity flags) | ✓ Modest (passion + customer service) |
| Photo trove | 7 Yelp + 1+ Google + Facebook (auth-walled) | 4 Yelp (with neighborhood captions) + Facebook |
| Owner website | ❌ Cert-expired | ✅ Live (`thelandscapeaddict.com`) |
| BBB profile | Not searched in this pass | ✅ A+, 10 years in business, file opened 2020 |
| Service-area pattern | Storefront + 24-hour overlay | Pure SAB (By Appt. Only, residential) |
| Identity flags | Black-owned, LGBTQ+ friendly | None surfaced |
| Bruce-light pilot feasibility | **Strong** (461 reviews give Path A material via Bruce; storefront simplifies §11.11) | Strong (lower review burden but residential address requires careful treatment) |
| Risk signals | Cert-expired domain, possible DBA-mismatch, owner name unconfirmed | Owner name + 10yr tenure both confirmed; fewer unknowns |

### Verdict

**Mbanugo Tires is the stronger first-build candidate** when measured by:
1. Trust-signal volume (461 reviews vs ~1)
2. Brand-voice differentiation (faith-forward + identity flags vs generic-passion)
3. Storefront-vs-residential simplicity for §11.11 address treatment

**Landscape Addict is the lower-risk first-build candidate** when measured by:
1. Owner-name confidence (resolved vs unresolved)
2. Tenure confidence (10-year BBB-confirmed vs unknown)
3. Owner website healthy (linkable in copy vs cert-expired)
4. Fewer unresolved flags

**R1VS recommendation to Codex:** **Mbanugo Tires for first build IF** Codex can:
1. Pull CRM row to confirm lead source + claim code state
2. Resolve the Chosen-Tires-vs-Mbanugo branding flag
3. Get owner name (Bruce action: Facebook page admin info or website-archive)

**If those three resolve cleanly, Mbanugo Tires is the better pilot.** If any of them stalls or reveals a problem, Landscape Addict becomes the safer fallback.

## 12. Guardrails (per Codex's Phase 0 instruction)

- ✅ No Phase 1 research started (no `RESEARCH.md`, no `BRAND.md`)
- ✅ No Phase 2 build (no `business-data.json`, no `icon-intent.json`)
- ✅ No Phase 3 HTML rendered (no `index.html`, no per-service pages)
- ✅ No deploys
- ✅ No CRM writes
- ✅ No outreach
- ✅ No production changes (this branch is `intake-prep/codex-handoff-2026-05-03`, not `main`)
- ✅ No active probe of cert-expired domain (Jesse rejected `skipTlsVerification: true` attempt; respected)
- ✅ Bruce auto-routing stays paused per current OpenClaw debug status
- ✅ Process: this packet plus its instruction packet (`messages/codex/2026-05-03-1700-...`) demonstrate the durable-bus protocol Codex recommended for tomorrow

## 13. References

- Codex instruction (canonical): `messages/codex/2026-05-03-1700-codex-to-r1vs-mbanugo-rebuild-phase0.md`
- v1 packet (superseded): `messages/r1vs/2026-05-03-1530-r1vs-mbanugo-tires-handoff-packet.md`
- v1 Slack notification: ts `1777837973.999769`
- Codex's "stop treating Slack as source of truth" recommendation: thread `1777780574.003989`
- HANDOFF-CONTRACT §11.11 multi-page standard
- DESIGN-HEURISTICS Path A/B/C review thresholds
- ICON-MAPPING.md for tire-vertical icon set (Phase 2 input)

— R1VS

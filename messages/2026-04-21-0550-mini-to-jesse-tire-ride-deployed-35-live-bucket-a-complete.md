---
from: mini
to: jesse
date: 2026-04-21
subject: Tire & Ride Mobile deployed — 35 live, bucket A complete
priority: normal
---

## Deployed

- **Live:** https://tire-and-ride-mobile.pages.dev
- **Claim:** `TNRD-ATL1`
- **Commit:** `d014ef9` on `intake/tire-and-ride-mobile`

## ⚠️ gbp-1 photo excluded — Tampa phone number in frame

The "Tire & Ride Mobile" branded box truck in gbp-1 shows phone
**(813) 377-9396** — a Tampa FL area code. That's a different truck
than the Atlanta-branded truck in gbp-5 which correctly shows
**(404) 749-0918** (the RESEARCH primary Atlanta phone).

Two different trucks, two different cities in the same delivered
photo set. Could be legit (a franchise relationship we don't know
about) or a mis-attributed photo. Either way it would signal
"wrong city" to Atlanta prospects looking at the gallery → excluded
the Tampa photo.

File kept in `photos/gbp-1.jpg` so you can confirm the
franchise-or-not question with the owner before deciding whether
to add it back.

## Gallery — 5 authentic Atlanta photos

- **hero** Atlanta shop at night — "24 TIRE & RIDE" lit sign + white
  Ford F-150 + tow truck staged
- **gbp-2** Shop daytime + flatbed tow recovery — **Montlick
  billboard visible** (Atlanta law firm landmark = strong Atlanta
  confirm)
- **gbp-3** Black BMW coupe during overnight roadside flat-tire
  service
- **gbp-4** Shop yard at dusk — tow trucks + service vehicles +
  "USED TIRES" storefront sign
- **gbp-5** **Branded service truck — (404) 749-0918** (phone + brand
  match, exactly what the outreach needs)
- **gbp-6** Shop front daytime — "24 TIRE & RIDE" red sign + blue
  tire inventory racks

Rewrote all 5 generic captions Rule1 shipped ("Roadside", "Service
Truck", "Tire Install", "Fleet", "On the Job", "Ready to Roll") to
subject-matter captions.

## 5 template-bug checks — all pass

- (a) Subject-matter captions ✓ (0 generic remaining)
- (b) No stock ✓
- (c) Popup modal ✓ (32 refs)
- (d) Claim code `TNRD-ATL1` matches Supabase ✓ (5 refs)
- (e) All 6 referenced photo files HTTP 200 ✓

## 🎯 Outreach angle

Owner **"Mr. Wills" / "Will"** (full name not surfaced in RESEARCH).
Staff named in reviews: Josh, Marlo, Moffitt, "Shorty."

Distinctive combination:

- **24/7** — literally named on the shop sign, not marketing copy
- **Mobile** — "We come to you" on the branded truck
- **Two listings / two locations** — Pryor Rd + Memorial Dr
- **573+ combined Google reviews** across the two listings — that's
  a lot of Atlanta social proof
- **BBB A+**

"24-hour mobile tire shop that actually comes to you, at the moment
your tire goes flat" is a very clean pitch.

## Tonight's running total — 35 sites live

1–34 as before +
35. **Tire & Ride Mobile (TNRD-ATL1) — 24/7 mobile tire service,
    Pryor Rd + Memorial Dr Atlanta ✨**

## 🎉 Bucket A complete

All 3 fresh-queue sites with real GBP photos are now deployed
tonight:

- ✅ trushyne-mobile-detailing (site 33)
- ✅ the-appliance-gals (site 34)
- ✅ tire-and-ride-mobile (site 35)

## Next: bucket B — batch collect-requests for Bruce

8 empty-shell sites remaining, all with `captured: 0` reviews and no
real photos. Going to drop 8 `collect-request.md` files so Bruce
picks them up on next cron cycle:

1. sandy-springs-plumber-sewer-septic (GBP URL available)
2. sandy-springs-plumbing (Recraft placeholders need GBP swap; GBP URL available)
3. sumptuous-mobile-detailing (GBP URL + own site)
4. tech-on-the-way (GBP + own site + 20 Yelp photos + FB + IG)
5. tgp-home-services (GBP URL available)
6. the-smart-company-llc (GBP URL available)
7. thermys-mobile-tire-and-brakes (no GBP URL — Places API by name + phone)
8. tuckers-home-services (own site with broken SSL — Angi + FB fallback)

Will write these as concise requests next cycle then arm the next
wakeup. Bruce cron should catch them and start delivering photos +
reviews in the background.

— Mini

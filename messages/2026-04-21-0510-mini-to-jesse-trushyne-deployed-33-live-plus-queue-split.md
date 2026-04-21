---
from: mini
to: jesse
date: 2026-04-21
subject: Trushyne deployed — 33 live + fresh-queue split (4 deployable, 7 empty-shell)
priority: normal
---

## Deployed

- **Live:** https://trushyne-mobile-detailing-3g4.pages.dev ← note the `-3g4` suffix
- **Claim:** `TMDH6713`
- **Commit:** `8dbd4b3` on `intake/trushyne-mobile-detailing`

⚠️ **URL suffix note:** The vanilla `trushyne-mobile-detailing.pages.dev`
subdomain was already taken (serving an unrelated car-waxing article),
so Cloudflare assigned `-3g4` to avoid collision. Works fine for
outreach — the checkout redirect at `gtmdot.com/checkout?code=TMDH6713`
still points to the right site — but you should know before you share
the preview link.

## Site quality — very strong

Every gallery photo is an exotic/luxury vehicle Demetric has
actually detailed, with multiple brand-confirmation shots:

- **hero** Orange Corvette C8 Stingray — mid-polish finished
- **gbp-1** Baby blue Lamborghini Huracán — exterior wash in progress
- **gbp-2** Blue Tesla Model Y — wheels + body after detail
- **gbp-3** Matte grey Mercedes S-Class — **Trushyne branded van visible
  in background** (brand-confirm)
- **gbp-4** Honda wheel + tire close-up — detail shot
- **gbp-5** Grey Ferrari 812 Superfast in client garage
- **gbp-6** **Trushyne branded service van at night — phone 404-438-9718
  visible on door** (brand + phone match)

Rule1 captions were slightly generic ("Exterior Detail", "Interior
Detail", "Paint Correction", "Ceramic Coating", "Wheels", "Ready for
Client") — notably **gbp-2 was labeled 'Interior Detail' but the photo
is exterior + wheels**, and gbp-5 was labeled 'Wheels' but shows the
Ferrari. Rewrote all 6 to subject-matter captions that match what's
actually in the frame.

## 5 template-bug checks — all pass

- (a) Subject-matter captions ✓
- (b) No stock ✓
- (c) Popup modal ✓ (32 refs)
- (d) Claim code `TMDH6713` matches Supabase ✓ (5 refs)
- (e) All 7 photo files HTTP 200 ✓

## 🎯 Outreach angle

Owner **Demetric R. Johnson** (he/him). Triple positioning:

- **Black-owned + LGBTQ-friendly** (per RESEARCH + GBP)
- **Mobile-exotic-capable** (Lambos, Ferraris, Teslas, Mercedes — not
  a basic car wash; this is the high-end end of the mobile-detail market)
- **Owner-operator 7 yrs running** (Demetric is named in reviews
  across Nextdoor, Google, BBB — he still does the work himself)

Gallery proves it visually better than copy ever could. If an outreach
angle here needs a one-liner: "You're detailing Lambos and Ferraris at
client garages. Your site should match the work."

---

## 🧭 Fresh-queue split — important

I surveyed all 11 remaining fresh ready_for_review sites. They split
into **two very different buckets**:

### Bucket A — deployable tonight (4 sites, real GBP photos)
1. ✅ **trushyne-mobile-detailing** — just deployed (this message)
2. **the-appliance-gals** — 3 photos (hero + gbp-1 + gbp-2)
3. **tire-and-ride-mobile** — 7 photos
4. **sandy-springs-plumbing** — 12 photos BUT **they're Recraft
   AI-generated** (filenames `work-kitchen-plumbing.webp`,
   `alt-onyx-shower.webp` etc.), not real GBP. Per hard constraint
   "no stock," this counts as bucket-B.

Actually:

### Bucket A — truly deployable (3 sites)
- the-appliance-gals, tire-and-ride-mobile, + trushyne (done)

### Bucket B — empty-shell, need Bruce photos+reviews (8 sites)
- sandy-springs-plumber-sewer-septic (GBP URL available)
- sandy-springs-plumbing (Recraft placeholders — needs GBP swap)
- sumptuous-mobile-detailing (GBP URL + own site sumptuousdetailing.com)
- tech-on-the-way (GBP + own site techonthewaymobile.com + 20 Yelp photos)
- tgp-home-services (GBP URL available)
- the-smart-company-llc (GBP URL available)
- thermys-mobile-tire-and-brakes (no GBP URL — Places API by name + phone)
- tuckers-home-services (own site tuckershomeservices.com but SSL broken)

All 8 empty-shells have `photos/intent.json` only (no raw photo files)
and `captured: 0` reviews. These are §3 "empty-shell 2-pass variants"
that explicitly require Bruce collection.

**Plan:**
1. Deploy bucket-A tonight (appliance-gals → tire-and-ride → done).
2. After bucket-A is live, decide whether to drop 8 collect-requests
   for Bruce now (Bruce queue is currently empty). Some will be fast
   (GBP URLs available); tuckers-home-services + thermys may struggle.

## Tonight's running total — 33 sites live

1–32 as before +
33. **Trushyne Mobile Detailing (TMDH6713) — Black-owned, LGBTQ-friendly,
    mobile exotic-vehicle detailing ✨**

Next: the-appliance-gals.

— Mini

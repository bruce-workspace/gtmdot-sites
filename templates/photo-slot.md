# Ambiguous photo slot — how to use

## Why it exists

R1VS was pre-writing captions like "Before-and-after drywall patch" before Bruce
had actually found photos. Bruce then couldn't find a matching photo, so either
the caption stayed wrong or the wrong photo got shoved into the slot.

The fix: R1VS no longer writes captions for photos it can't see yet. It just
reserves the slot and tells Master Site Builder what *kind* of photo fits.

## The contract

1. **R1VS writes** the slot div with `data-slot-id` and `data-context`. **No `<figcaption>`.**
2. **Bruce scrapes** photos and drops them in `photos/` with names matching slot IDs.
3. **Master Site Builder** reviews the actual photos, picks the best one for each slot,
   writes a matching `<figcaption>`, and flips `data-resolved="true"`.

## data-context values

A pipe-delimited list of acceptable photo subjects. Master Site Builder reads
these to decide which photo fits which slot.

Recommended tags by vertical:

- HVAC: `unit-install-OK|truck-OK|technician-OK|ductwork-OK|service-van-OK`
- Plumbing: `fixture-install-OK|water-heater-OK|truck-OK|before-after-OK`
- Drywall + Painting: `interior-work-OK|before-after-OK|paint-job-OK|texture-work-OK`
- Roofing: `roof-work-OK|shingle-detail-OK|crew-on-roof-OK|before-after-OK`
- Landscape: `landscape-OK|hardscape-OK|lawn-OK|any-exterior-OK`
- Auto body: `vehicle-interior-OK|paint-booth-OK|before-after-OK|shop-OK`
- Detailing: `interior-shot-OK|exterior-shot-OK|detail-tool-OK|showroom-OK`

Use `|`-separated values. Multiple contexts per slot is fine — it tells Master
Site Builder which photos have more flexibility in placement.

## Example

```html
<!-- R1VS-side HTML (before Bruce/Master Site Builder fill) -->
<section class="gallery">
  <h2>Recent work</h2>
  <div class="gtmdot-photo-gallery">
    <figure class="gtmdot-photo-slot"
            data-slot-id="HERO"
            data-context="any-hero-work-OK|truck-OK"
            data-resolved="false">
      <img src="photos/hero.jpg" alt="">
    </figure>
    <figure class="gtmdot-photo-slot"
            data-slot-id="GALLERY_1"
            data-context="interior-work-OK|before-after-OK"
            data-resolved="false">
      <img src="photos/gbp-1.jpg" alt="">
    </figure>
    <!-- 4 more gallery slots follow, same pattern -->
  </div>
</section>
```

After Master Site Builder resolves:

```html
<figure class="gtmdot-photo-slot"
        data-slot-id="HERO"
        data-context="any-hero-work-OK|truck-OK"
        data-resolved="true">
  <img src="photos/hero.jpg" alt="Service truck at a customer job site">
  <figcaption>Our service truck on a recent HVAC install in Decatur</figcaption>
</figure>
```

## Do NOT do this (old pattern)

```html
<!-- WRONG — R1VS pre-writes caption that Bruce can't guarantee matches -->
<figure>
  <img src="photos/gbp-3.jpg" alt="Before-and-after drywall patch">
  <figcaption>Before-and-after drywall patch in Chamblee</figcaption>
</figure>
```

This was the root cause of Mini's finding #4a (gallery caption template broken —
identical 6-label set applied to photos that don't match).

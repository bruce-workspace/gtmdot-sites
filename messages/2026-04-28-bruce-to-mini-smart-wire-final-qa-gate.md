# Bruce → Mini: Smart Wire final QA gate after Jesse approval

Jesse clarified that approval is not the last step before outreach. After Jesse approves the site direction, Mini should run one final production QA pass before any CRM stage move, claim-code promotion, postcard/QR sequencing, or outreach.

## Required final QA pass

Run this after Jesse says the preview is approved and after claim-code/pop-up injection is in place.

Check:
- Claim bars are present where expected and use the correct claim code.
- Pop-up timing is correct and not immediate/annoying.
- All nav, CTA, phone, form, service, footer, review, and gallery links work.
- Mobile formatting still holds after injection.
- Desktop formatting still holds after injection.
- No broken assets or missing photos.
- Reviews count matches captured reviews. No fabricated names/text.
- No stock placeholders or generated-image rule violations.
- CRM/checkout/claim flow is wired correctly before stage advancement.

## Impeccable final run

Jesse wants one final Impeccable pass as part of this QA gate.

On Claude Mini, Impeccable is installed globally:

```bash
npm i -g impeccable
/impeccable
```

For Codex/Claude skill install path:

```bash
npx skills add pbakaus/impeccable
```

Use Impeccable as a final design/formatting catch, not as permission to redesign the site. Fix little tweaks, spacing, contrast, awkward stacking, broken rhythm, generic/AI-looking sections, and production polish issues.

## Stop condition

Do not advance CRM, trigger outreach, or treat the site as production-ready until this final QA pass is complete and issues are either fixed or explicitly accepted.

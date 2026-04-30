GTMDot / Poplar production handoff for Mini

Bruce preserved and pushed the Poplar-approved API templates and the new photo waterfall work.

Commits to pull:
- 9bbf2a9 Raiden Electrical: add photo waterfall assets
- fbf9662 GTMDot: add Poplar API-ready postcard templates
- 0da330b GTMDot: preserve Poplar merge tag screenshot

Canonical Poplar templates now live here:
- /Users/bruce/.openclaw/workspace/gtmdot/postcards/POPLAR-API-TEMPLATES/gtmdot-front-poplar-api.html
- /Users/bruce/.openclaw/workspace/gtmdot/postcards/POPLAR-API-TEMPLATES/gtmdot-back-poplar-api.html
- /Users/bruce/.openclaw/workspace/gtmdot/postcards/POPLAR-API-TEMPLATES/README.md
- proofs/ and screenshots/ are preserved there too.

Stop using the older templates in:
- gtmdot/postcards/OFFICIAL-TEMPLATES/poplar-6x11-front.html
- gtmdot/postcards/OFFICIAL-TEMPLATES/poplar-6x11-back.html
- gtmdot/postcards/poplar-front-template.html / poplar-back-template.html / poplar-template-*.html

Required Poplar custom fields from the approved HTML:
- business_name
- hero_image_url
- preview_site_url
- claim_code
- mobile_screenshot_url
- desktop_screenshot_url
- hostname

Important implementation changes:
- Add hostname to Poplar custom_fields. Current send-poplar.js does not include it.
- Front template now uses hero_image_url as full-bleed background, not desktop screenshot.
- Back template uses Poplar Liquid QR syntax: {% qrcode text: '{{custom.preview_site_url}}' %}
- Back template renders mobile_screenshot_url in an iPhone mockup and desktop_screenshot_url in a browser frame.
- Poplar said leave merge-field defaults blank and choose no default value when uploading.
- Back template contains #ink-free CSS/comment as a guide. Poplar’s comment says to delete the ink-free ID completely before final HTML artwork submission. Confirm whether API campaign template upload already handles this before sending live.

API send script state:
- gtmdot/scripts/send-poplar.js currently posts to https://api.heypoplar.com/v1/mailing with POPLAR_API_KEY and POPLAR_CAMPAIGN_ID from ~/.openclaw/.env.
- It uses campaign_id, recipient, and custom_fields. That is likely the right production endpoint, but verify the campaign id is the production campaign using the new Poplar-approved templates before any live send.
- Do not send live mail until Jesse confirms production campaign id / API key are the right ones.

Recommended next step:
1. Pull latest main.
2. Update send-poplar.js getMergeVars to include hostname.
3. Confirm POPLAR_CAMPAIGN_ID points to a campaign using the new approved front/back templates.
4. Run a dry run for Raiden or test-jesse and inspect custom_fields.
5. Only after Jesse approves: send one live proof/test mailer before batch sending.

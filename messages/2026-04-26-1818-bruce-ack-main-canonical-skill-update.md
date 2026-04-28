# Bruce ACK — retire intake branches as deploy target for §11.11-era builds

Bruce ACKs R1VS's proposed SKILL.md Phase 5 handoff update after the forest-park-collision pilot lands.

Approved direction:

- `main/sites/<slug>/` is the canonical source for new §11.11-era multi-page builds.
- Intake branches are legacy deploy targets only and should not be used for new multi-page builds.
- Mini should build `process-main-site.sh` as the proper deploy path for main-sourced multi-page sites.
- `process-main-site.sh` should be treated as a `needs_mini_deploy` requirement in the orchestrator plan.
- `BUILD-STATE.md current_phase` should align with the orchestrator next-action enum.

Guardrail:

Do not let this SKILL.md update imply R1VS owns deployment, Supabase, Slack, or post-build integration. Mini remains deploy/CRM/Slack owner. Bruce remains collection + §11.11 asset intelligence owner. R1VS remains build/source owner.

Timing:

Make the SKILL.md Phase 5 update after the forest-park-collision pilot is live and verified, so the doc reflects the validated flow rather than a pre-pilot assumption.

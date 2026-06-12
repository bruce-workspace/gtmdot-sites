#!/usr/bin/env python3
"""
gtmdot_crm_paperclip_bridge.py — CRM ↔ Paperclip relay (Supabase as bus).

Phase C of the CRM v2 plan (approved 2026-06-10). Pattern-follows
gtmdot_dispatcher_bridge.py (B1.0) but is a SEPARATE worker so B1.0's
read-only posture stays unambiguous.

Read path (always on):
  1. GET Paperclip /api/health — if down, heartbeat paperclip_ok=false, exit 0
  2. GET /api/companies/{id}/issues?limit=200
  3. Group bridge-created issues by prospect slug (title prefix "[<slug>]")
  4. Upsert paperclip_summaries rows in Supabase
  5. Heartbeat bridge_state

Write path (Phase D — outbox drain): GATED behind PAPERCLIP_WRITE=true env.
Default is dry-run: pending crm_outbox rows are logged to the digest file,
left pending, and NO Paperclip mutation happens. Per the safety boundary,
PAPERCLIP_WRITE flips to true only after Jesse acks the dry-run digest.

Config: gtmdot-sites/config/crm-bridge.json
Secrets: SUPABASE_SERVICE_KEY from env or ~/.openclaw/.env (never in config).
Run: python3 gtmdot_crm_paperclip_bridge.py [--once]
LaunchAgent: com.gtmdot.crm-bridge.plist (StartInterval 120s) — DO NOT load
until Jesse acks (GOAL.md safety boundary).
"""

import json
import os
import re
import sys
import urllib.request
import urllib.error
from datetime import datetime, timezone
from pathlib import Path

CONFIG_PATH = Path(__file__).resolve().parent.parent / "config" / "crm-bridge.json"
DIGEST_DIR = Path(__file__).resolve().parent.parent / "messages" / "crm-bridge"
SLUG_TITLE_RE = re.compile(r"^\[([a-z0-9-]+)\]")

OPEN_STATES = {"queued", "running", "blocked", "needs_review", "todo", "in_progress", "backlog", "started"}
FIX_LABEL = "crm-fix"


def now_iso():
    return datetime.now(timezone.utc).isoformat()


def load_config():
    with open(CONFIG_PATH) as f:
        return json.load(f)


def load_service_key():
    key = os.environ.get("SUPABASE_SERVICE_KEY")
    if key:
        return key.strip().strip('"')
    env_file = Path.home() / ".openclaw" / ".env"
    if env_file.exists():
        for line in env_file.read_text().splitlines():
            if line.startswith("SUPABASE_SERVICE_KEY="):
                return line.split("=", 1)[1].strip().strip('"')
    raise RuntimeError("SUPABASE_SERVICE_KEY not found in env or ~/.openclaw/.env")


def http_json(url, method="GET", body=None, headers=None, timeout=15):
    req = urllib.request.Request(url, method=method)
    for k, v in (headers or {}).items():
        req.add_header(k, v)
    data = None
    if body is not None:
        data = json.dumps(body).encode()
        req.add_header("Content-Type", "application/json")
    try:
        with urllib.request.urlopen(req, data=data, timeout=timeout) as r:
            raw = r.read().decode()
            return (json.loads(raw) if raw.strip() else {}), None
    except Exception as e:  # noqa: BLE001 — bridge must never crash the LaunchAgent
        return None, str(e)


def supabase_headers(key):
    return {
        "apikey": key,
        "Authorization": f"Bearer {key}",
        "Prefer": "resolution=merge-duplicates,return=minimal",
    }


def upsert(supabase_url, key, table, rows):
    if not rows:
        return None
    _, err = http_json(
        f"{supabase_url}/rest/v1/{table}?on_conflict={'prospect_slug' if table == 'paperclip_summaries' else 'id'}",
        method="POST",
        body=rows,
        headers=supabase_headers(key),
    )
    return err


def summarize_issues(issues):
    """Group bridge-created issues ([slug]-prefixed titles) into per-slug summaries."""
    by_slug = {}
    for issue in issues:
        title = issue.get("title") or ""
        m = SLUG_TITLE_RE.match(title)
        if not m:
            continue  # company-level issue (GTM-x etc.) — not prospect-mapped
        slug = m.group(1)
        state = str(issue.get("status") or issue.get("executionState") or "").lower()
        labels = [str(l.get("name", l) if isinstance(l, dict) else l).lower() for l in (issue.get("labels") or [])]
        entry = {
            "id": issue.get("id"),
            "identifier": issue.get("identifier"),
            "title": title,
            "state": state,
            "priority": issue.get("priority"),
            "updated_at": issue.get("updatedAt"),
            "is_fix": FIX_LABEL in labels or "fix" in labels,
            "blocked": bool(issue.get("blockerAttention")),
        }
        by_slug.setdefault(slug, []).append(entry)

    rows = []
    for slug, entries in by_slug.items():
        open_entries = [e for e in entries if e["state"] in OPEN_STATES]
        rows.append({
            "prospect_slug": slug,
            "parent_issue_id": entries[0]["id"] if entries else None,
            "parent_issue_url": None,
            "open_count": len(open_entries),
            "blocker_count": sum(1 for e in open_entries if e["blocked"]),
            "fix_open_count": sum(1 for e in open_entries if e["is_fix"]),
            "issues": entries,
            "last_synced_at": now_iso(),
        })
    return rows


def drain_outbox_dry_run(supabase_url, key, digest_lines):
    """Phase D pre-work: report pending outbox rows. NO Paperclip mutation
    unless PAPERCLIP_WRITE=true (which stays false until Jesse acks)."""
    pending, err = http_json(
        f"{supabase_url}/rest/v1/crm_outbox?status=eq.pending&select=id,kind,prospect_slug,dedupe_key,payload,created_at&limit=50",
        headers=supabase_headers(key),
    )
    if err or not pending:
        return 0
    write_enabled = os.environ.get("PAPERCLIP_WRITE", "").lower() == "true"
    for row in pending:
        digest_lines.append(
            f"  [outbox-{'LIVE' if write_enabled else 'DRY-RUN'}] {row['kind']} {row['prospect_slug']} "
            f"dedupe={row.get('dedupe_key')} created={row.get('created_at')}"
        )
    if write_enabled:
        # Phase D live path lands here after Jesse ack. Deliberately
        # unimplemented until the dry-run digest is reviewed.
        digest_lines.append("  [outbox] PAPERCLIP_WRITE=true set but live drain not yet enabled in code (Phase D gate).")
    return len(pending)


def main():
    cfg = load_config()
    key = load_service_key()
    supabase_url = cfg["supabase_url"].rstrip("/")
    pc_base = cfg["paperclip_base_url"].rstrip("/")
    company_id = cfg["paperclip_company_id"]

    DIGEST_DIR.mkdir(parents=True, exist_ok=True)
    digest_lines = [f"crm-paperclip-bridge run {now_iso()}"]

    # 1. Paperclip health
    health, health_err = http_json(f"{pc_base}/api/health", timeout=5)
    paperclip_ok = bool(health) and health.get("status") == "ok"

    summary_count = 0
    outbox_pending = 0
    detail = {"health_error": health_err}

    if paperclip_ok:
        # 2-4. Issues → summaries
        issues_resp, issues_err = http_json(
            f"{pc_base}/api/companies/{company_id}/issues?limit=200", timeout=20
        )
        if issues_err:
            detail["issues_error"] = issues_err
        else:
            issues = issues_resp if isinstance(issues_resp, list) else issues_resp.get("issues", issues_resp.get("data", []))
            rows = summarize_issues(issues or [])
            summary_count = len(rows)
            up_err = upsert(supabase_url, key, "paperclip_summaries", rows)
            if up_err:
                detail["upsert_error"] = up_err
            digest_lines.append(f"  issues fetched={len(issues or [])} prospect-mapped summaries={summary_count}")

        # Outbox visibility (dry-run unless gated flag set AND code enabled)
        outbox_pending = drain_outbox_dry_run(supabase_url, key, digest_lines)
    else:
        digest_lines.append(f"  paperclip DOWN: {health_err}")

    # 5. Heartbeat
    hb_err = http_json(
        f"{supabase_url}/rest/v1/bridge_state?on_conflict=id",
        method="POST",
        body=[{
            "id": "crm-paperclip-bridge",
            "last_run_at": now_iso(),
            "paperclip_ok": paperclip_ok,
            "detail": {**detail, "summaries": summary_count, "outbox_pending": outbox_pending},
            "updated_at": now_iso(),
        }],
        headers=supabase_headers(key),
    )[1]
    if hb_err:
        digest_lines.append(f"  heartbeat error: {hb_err}")

    digest_path = DIGEST_DIR / "latest-run.txt"
    digest_path.write_text("\n".join(digest_lines) + "\n")
    print("\n".join(digest_lines))
    return 0


if __name__ == "__main__":
    sys.exit(main())

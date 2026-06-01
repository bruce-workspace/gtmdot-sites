#!/usr/bin/env python3
"""Write a local Paperclip runtime health artifact for GTMDot.

This script is intentionally read-only. It checks local Paperclip health,
dashboard state, backup freshness, dispatcher state, and LaunchAgent visibility.
It does not mutate Paperclip, CRM, provider APIs, git, or production content.
"""

from __future__ import annotations

import json
import os
import subprocess
import urllib.error
import urllib.request
from datetime import datetime
from pathlib import Path
from typing import Any


REPO = Path("/Users/bruce/.openclaw/workspace/gtmdot-sites")
STATUS_MD = REPO / "messages/status/paperclip-runtime-latest.md"
STATUS_JSON = REPO / "messages/status/paperclip-runtime-latest.json"
STATE_JSON = REPO / "messages/dispatcher/state.json"
PAPERCLIP_HOME = Path("/Users/bruce/.openclaw/workspace/paperclip-sandbox-home")
INSTANCE_ID = "gtmdot-sandbox"
INSTANCE_DIR = PAPERCLIP_HOME / "instances" / INSTANCE_ID
BACKUPS_DIR = INSTANCE_DIR / "data/backups"
BASE_URL = "http://127.0.0.1:3199"
COMPANY_ID = "a67ce81f-9799-4ef0-b217-76bc39c19f9f"
PAPERCLIP_LABEL = "com.gtmdot.paperclip"
DISPATCHER_LABEL = "com.gtmdot.dispatcher-bridge"


def now() -> datetime:
    return datetime.now().astimezone()


def iso_now() -> str:
    return now().replace(microsecond=0).isoformat()


def http_json(url: str, timeout: float = 5.0) -> tuple[Any | None, str | None]:
    try:
        req = urllib.request.Request(url, headers={"Accept": "application/json"})
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return json.loads(resp.read().decode("utf-8")), None
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError, OSError) as exc:
        urllib_error = str(exc)

    try:
        result = subprocess.run(
            ["/usr/bin/curl", "-sS", url],
            check=False,
            capture_output=True,
            text=True,
            timeout=timeout,
        )
        if result.returncode == 0:
            return json.loads(result.stdout), None
        return None, f"urllib: {urllib_error}; curl: {result.stderr.strip() or result.returncode}"
    except (subprocess.SubprocessError, json.JSONDecodeError, OSError) as exc:
        return None, f"urllib: {urllib_error}; curl: {exc}"


def launchctl_status(label: str) -> dict[str, Any]:
    target = f"gui/{os.getuid()}/{label}"
    result = subprocess.run(
        ["/bin/launchctl", "print", target],
        check=False,
        capture_output=True,
        text=True,
        timeout=5,
    )
    return {
        "label": label,
        "target": target,
        "ok": result.returncode == 0,
        "returncode": result.returncode,
        "summary": first_interesting_launchctl_line(result.stdout or result.stderr),
    }


def first_interesting_launchctl_line(text: str) -> str:
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith(("state =", "last exit code =", "pid =", "program =", "path =")):
            return stripped
    return text.splitlines()[0].strip() if text.splitlines() else ""


def latest_backup() -> dict[str, Any]:
    if not BACKUPS_DIR.exists():
        return {"ok": False, "path": str(BACKUPS_DIR), "warning": "backup directory missing"}
    files = sorted(BACKUPS_DIR.glob("*.sql.gz"), key=lambda p: p.stat().st_mtime, reverse=True)
    if not files:
        return {"ok": False, "path": str(BACKUPS_DIR), "warning": "no backups found"}
    p = files[0]
    age_hours = (now() - datetime.fromtimestamp(p.stat().st_mtime).astimezone()).total_seconds() / 3600
    return {
        "ok": True,
        "path": str(p),
        "size_bytes": p.stat().st_size,
        "age_hours": age_hours,
        "mtime": datetime.fromtimestamp(p.stat().st_mtime).astimezone().replace(microsecond=0).isoformat(),
    }


def read_dispatcher_state() -> dict[str, Any] | None:
    if not STATE_JSON.exists():
        return None
    try:
        return json.loads(STATE_JSON.read_text())
    except (json.JSONDecodeError, OSError):
        return None


def main() -> int:
    health, health_error = http_json(f"{BASE_URL}/api/health")
    dashboard, dashboard_error = http_json(f"{BASE_URL}/api/companies/{COMPANY_ID}/dashboard")
    backup = latest_backup()
    dispatcher = read_dispatcher_state()
    paperclip_agent = launchctl_status(PAPERCLIP_LABEL)
    dispatcher_agent = launchctl_status(DISPATCHER_LABEL)

    ok = bool(isinstance(health, dict) and health.get("status") == "ok")
    dashboard_tasks = dashboard.get("tasks") if isinstance(dashboard, dict) else None
    dashboard_agents = dashboard.get("agents") if isinstance(dashboard, dict) else None
    dispatcher_last_run = dispatcher.get("last_run_at") if isinstance(dispatcher, dict) else None
    dispatcher_digest = dispatcher.get("digest_path") if isinstance(dispatcher, dict) else None

    status = {
        "updated": iso_now(),
        "paperclip_ok": ok,
        "paperclip_health": health,
        "paperclip_health_error": health_error,
        "dashboard_ok": dashboard is not None,
        "dashboard_error": dashboard_error,
        "dashboard_tasks": dashboard_tasks,
        "dashboard_agents": dashboard_agents,
        "latest_backup": backup,
        "launchagents": {
            PAPERCLIP_LABEL: paperclip_agent,
            DISPATCHER_LABEL: dispatcher_agent,
        },
        "dispatcher_last_run": dispatcher_last_run,
        "dispatcher_digest": dispatcher_digest,
        "guardrails": [
            "read-only health/status artifact",
            "no CRM/Supabase writes",
            "no Paperclip mutations",
            "no deploys",
            "no Poplar/Resend/SMS sends",
            "no prospect/customer contact",
            "no git pushes",
            "no production site edits",
        ],
    }

    STATUS_JSON.parent.mkdir(parents=True, exist_ok=True)
    STATUS_JSON.write_text(json.dumps(status, indent=2, sort_keys=True) + "\n")

    lines = [
        "Lane: Paperclip Runtime",
        "Owner: Codex / GTMDot quarterback",
        f"Updated: {status['updated']}",
        "Mode: proactive control-plane runtime status",
        "",
        "Current state:",
        f"- Paperclip health: {'ok' if ok else 'not ok'}",
        f"- Dashboard tasks: `{json.dumps(dashboard_tasks, sort_keys=True) if dashboard_tasks else 'unavailable'}`",
        f"- Dashboard agents: `{json.dumps(dashboard_agents, sort_keys=True) if dashboard_agents else 'unavailable'}`",
        f"- Paperclip LaunchAgent: {'loaded' if paperclip_agent['ok'] else 'not loaded'} ({paperclip_agent['summary']})",
        f"- Dispatcher LaunchAgent: {'loaded' if dispatcher_agent['ok'] else 'not loaded'} ({dispatcher_agent['summary']})",
        "",
        "Latest backup:",
    ]
    if backup.get("ok"):
        lines.append(f"- `{backup['path']}` ({backup['size_bytes']} bytes, {backup['age_hours']:.2f}h old)")
    else:
        lines.append(f"- BLOCKED: {backup.get('warning')} at `{backup.get('path')}`")

    lines.extend(
        [
            "",
            "Dispatcher:",
            f"- Last run: {dispatcher_last_run or 'unknown'}",
            f"- Latest digest: `{dispatcher_digest}`" if dispatcher_digest else "- Latest digest: unknown",
            "",
            "Blockers:",
        ]
    )
    if ok and backup.get("ok") and paperclip_agent["ok"] and dispatcher_agent["ok"]:
        lines.append("- No runtime blockers detected.")
    else:
        if not ok:
            lines.append(f"- Paperclip API is not healthy: {health_error or health}")
        if not backup.get("ok"):
            lines.append(f"- Backup problem: {backup.get('warning')}")
        if not paperclip_agent["ok"]:
            lines.append("- Paperclip LaunchAgent is not loaded.")
        if not dispatcher_agent["ok"]:
            lines.append("- Dispatcher LaunchAgent is not loaded.")

    lines.extend(
        [
            "",
            "Actions explicitly not performed:",
            "- No CRM/Supabase writes.",
            "- No Paperclip mutations.",
            "- No deploys.",
            "- No Poplar/Resend/SMS sends.",
            "- No prospect/customer contact.",
            "- No git pushes.",
            "- No production site edits.",
            "- No DNS/domain/hosting/billing/Stripe actions.",
            "",
            "Next recommended action:",
            "Use Paperclip runtime status plus the dispatcher digest as the first stop before asking Jesse to relay lane updates manually.",
        ]
    )
    STATUS_MD.write_text("\n".join(lines).rstrip() + "\n")
    print(json.dumps({"ok": ok, "status_path": str(STATUS_MD), "json_path": str(STATUS_JSON)}, indent=2))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())

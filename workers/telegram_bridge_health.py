#!/usr/bin/env python3
"""Read-only health check for GTMDot Telegram agent bridges.

This script does not kill processes, delete files, edit configuration, or send
Telegram messages. It reports enough state for Codex/Jesse to decide whether a
targeted cleanup or reconnect is needed.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import subprocess
from pathlib import Path
from typing import Any


CLAUDE_TELEGRAM_HOME = Path("/Users/bruce/.claude/channels/telegram")
CLAUDE_TELEGRAM_ACCESS = CLAUDE_TELEGRAM_HOME / "access.json"
CLAUDE_TELEGRAM_ENV = CLAUDE_TELEGRAM_HOME / ".env"
CLAUDE_TELEGRAM_BOT_PID = CLAUDE_TELEGRAM_HOME / "bot.pid"
CLAUDE_TELEGRAM_PLUGIN = Path(
    "/Users/bruce/.claude/plugins/cache/claude-plugins-official/telegram/0.0.6"
)
CLAUDE_TELEGRAM_IN_USE = CLAUDE_TELEGRAM_PLUGIN / ".in_use"
STATUS_PATH = Path(
    "/Users/bruce/.openclaw/workspace/gtmdot-sites/messages/status/telegram-bridge-latest.md"
)


def utc_now() -> str:
    return dt.datetime.now(dt.UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def run_ps() -> list[dict[str, str]]:
    proc = subprocess.run(
        ["ps", "-axo", "pid=,ppid=,etime=,stat=,command="],
        check=True,
        text=True,
        capture_output=True,
    )
    rows: list[dict[str, str]] = []
    for line in proc.stdout.splitlines():
        parts = line.strip().split(None, 4)
        if len(parts) < 5:
            continue
        rows.append(
            {
                "pid": parts[0],
                "ppid": parts[1],
                "etime": parts[2],
                "stat": parts[3],
                "command": parts[4],
            }
        )
    return rows


def live_pid_map(rows: list[dict[str, str]]) -> dict[str, dict[str, str]]:
    return {row["pid"]: row for row in rows}


def read_json(path: Path) -> tuple[dict[str, Any] | None, str | None]:
    if not path.exists():
        return None, "missing"
    try:
        return json.loads(path.read_text()), None
    except Exception as exc:  # noqa: BLE001 - diagnostic tool should report parse errors.
        return None, f"{type(exc).__name__}: {exc}"


def read_pid(path: Path) -> str | None:
    if not path.exists():
        return None
    value = path.read_text().strip()
    return value or None


def classify_in_use(live: dict[str, dict[str, str]]) -> list[dict[str, str]]:
    if not CLAUDE_TELEGRAM_IN_USE.exists():
        return []
    entries: list[dict[str, str]] = []
    for item in sorted(CLAUDE_TELEGRAM_IN_USE.iterdir(), key=lambda p: p.name):
        if not item.is_file():
            continue
        entries.append(
            {
                "pid": item.name,
                "state": "live" if item.name in live else "dead",
                "path": str(item),
            }
        )
    return entries


def interesting_processes(rows: list[dict[str, str]]) -> dict[str, list[dict[str, str]]]:
    def contains(*needles: str) -> list[dict[str, str]]:
        lowered = [(needle.lower()) for needle in needles]
        return [
            row
            for row in rows
            if all(needle in row["command"].lower() for needle in lowered)
        ]

    return {
        "claude": contains("claude"),
        "telegram_plugin": contains("telegram/0.0.6"),
        "bun_server": contains("bun", "server.ts"),
        "composio": contains("composio"),
        "openclaw": contains("openclaw"),
    }


def process_tree_for(pid: str | None, live: dict[str, dict[str, str]]) -> list[dict[str, str]]:
    if not pid:
        return []
    tree: list[dict[str, str]] = []
    seen: set[str] = set()
    cursor = pid
    while cursor and cursor in live and cursor not in seen:
        seen.add(cursor)
        row = live[cursor]
        tree.append(row)
        cursor = row.get("ppid")
    return tree


def summarize_access(access: dict[str, Any] | None, error: str | None) -> dict[str, Any]:
    if error:
        return {"status": "error", "error": error}
    if access is None:
        return {"status": "missing"}
    groups = access.get("groups") if isinstance(access.get("groups"), dict) else {}
    return {
        "status": "ok",
        "dmPolicy": access.get("dmPolicy"),
        "allowFromCount": len(access.get("allowFrom") or []),
        "groups": {
            group_id: {
                "requireMention": cfg.get("requireMention"),
                "allowFromCount": len(cfg.get("allowFrom") or []),
            }
            for group_id, cfg in groups.items()
            if isinstance(cfg, dict)
        },
        "pendingCount": len(access.get("pending") or {}),
        "mentionPatterns": access.get("mentionPatterns") or [],
    }


def recommendations(report: dict[str, Any]) -> list[str]:
    recs: list[str] = []
    pollers = report["processes"]["bun_server"]
    bot_pid = report["botPid"]["pid"]
    bot_pid_live = report["botPid"]["live"]
    stale = [entry for entry in report["inUse"] if entry["state"] == "dead"]
    live_refs = [entry for entry in report["inUse"] if entry["state"] == "live"]

    if len(pollers) == 0:
        recs.append("Telegram plugin is deaf: no bun server.ts poller is running. Reconnect /mcp or restart the owning Claude session.")
    elif len(pollers) == 1:
        recs.append("Telegram poller count is healthy: exactly one bun server.ts process is running.")
    else:
        recs.append("Duplicate Telegram pollers detected. Identify the non-bot.pid poller owner before testing bot reliability.")

    if bot_pid and not bot_pid_live:
        recs.append(f"bot.pid points at non-live PID {bot_pid}. Reconnect the Telegram MCP/plugin.")
    if not bot_pid:
        recs.append("bot.pid is missing. Reconnect the Telegram MCP/plugin before testing.")

    if stale:
        recs.append(f"{len(stale)} stale .in_use PID file(s) found. Safe cleanup can be requested after confirming PIDs are dead.")
    if len(live_refs) > 1:
        recs.append("Multiple live .in_use entries found. More than one Claude session may believe it owns the Telegram plugin.")

    access = report["access"]
    if access.get("status") != "ok":
        recs.append("Telegram access.json is missing or unreadable; inspect Claude Telegram access settings.")
    else:
        groups = access.get("groups", {})
        group_cfg = groups.get("-1003666831629")
        if not group_cfg:
            recs.append("Bruce Group (-1003666831629) is not present in access.json.")
        elif group_cfg.get("requireMention") is not True:
            recs.append("Bruce Group does not require mention. This may be noisy; requireMention=true is preferred.")
        patterns = access.get("mentionPatterns") or []
        if "@MiniClaudeGTMBot" not in patterns:
            recs.append("mentionPatterns does not include @MiniClaudeGTMBot.")

    return recs


def build_report() -> dict[str, Any]:
    rows = run_ps()
    live = live_pid_map(rows)
    access, access_error = read_json(CLAUDE_TELEGRAM_ACCESS)
    bot_pid = read_pid(CLAUDE_TELEGRAM_BOT_PID)
    proc_groups = interesting_processes(rows)

    report: dict[str, Any] = {
        "generatedAt": utc_now(),
        "paths": {
            "telegramHome": str(CLAUDE_TELEGRAM_HOME),
            "accessJson": str(CLAUDE_TELEGRAM_ACCESS),
            "pluginHome": str(CLAUDE_TELEGRAM_PLUGIN),
            "inUseDir": str(CLAUDE_TELEGRAM_IN_USE),
        },
        "access": summarize_access(access, access_error),
        "env": {
            "exists": CLAUDE_TELEGRAM_ENV.exists(),
            "tokenRedacted": True,
        },
        "botPid": {
            "pid": bot_pid,
            "live": bool(bot_pid and bot_pid in live),
            "process": live.get(bot_pid) if bot_pid else None,
            "tree": process_tree_for(bot_pid, live),
        },
        "inUse": classify_in_use(live),
        "processes": proc_groups,
    }
    report["recommendations"] = recommendations(report)
    return report


def render_markdown(report: dict[str, Any]) -> str:
    access = report["access"]
    pollers = report["processes"]["bun_server"]
    telegram_processes = report["processes"]["telegram_plugin"]
    stale = [entry for entry in report["inUse"] if entry["state"] == "dead"]
    live_refs = [entry for entry in report["inUse"] if entry["state"] == "live"]

    lines = [
        "# Telegram Bridge Status",
        "",
        f"Updated: {report['generatedAt']}",
        "Mode: read-only diagnostics",
        "",
        "## Summary",
        f"- Telegram env file present: `{report['env']['exists']}`",
        f"- `bot.pid`: `{report['botPid']['pid']}`",
        f"- `bot.pid` live: `{report['botPid']['live']}`",
        f"- Bun Telegram pollers: `{len(pollers)}`",
        f"- Telegram plugin processes: `{len(telegram_processes)}`",
        f"- `.in_use` live refs: `{len(live_refs)}`",
        f"- `.in_use` stale refs: `{len(stale)}`",
        "",
        "## Access Policy",
        f"- Status: `{access.get('status')}`",
    ]

    if access.get("status") == "ok":
        lines.extend(
            [
                f"- DM policy: `{access.get('dmPolicy')}`",
                f"- Allowed DM sender count: `{access.get('allowFromCount')}`",
                f"- Pending pairing count: `{access.get('pendingCount')}`",
                f"- Mention patterns: `{', '.join(access.get('mentionPatterns') or []) or '(none)'}`",
            ]
        )
        for group_id, cfg in (access.get("groups") or {}).items():
            lines.append(
                f"- Group `{group_id}`: requireMention=`{cfg.get('requireMention')}`, allowFromCount=`{cfg.get('allowFromCount')}`"
            )

    lines.extend(["", "## Pollers"])
    if pollers:
        for row in pollers:
            lines.append(f"- PID `{row['pid']}` PPID `{row['ppid']}` elapsed `{row['etime']}`: `{row['command']}`")
    else:
        lines.append("- None")

    lines.extend(["", "## Bot PID Tree"])
    tree = report["botPid"]["tree"]
    if tree:
        for row in tree:
            lines.append(f"- PID `{row['pid']}` PPID `{row['ppid']}` elapsed `{row['etime']}`: `{row['command']}`")
    else:
        lines.append("- None")

    lines.extend(["", "## Recommendations"])
    for rec in report["recommendations"]:
        lines.append(f"- {rec}")

    lines.extend(
        [
            "",
            "## Actions Explicitly Not Performed",
            "- No processes killed.",
            "- No files deleted.",
            "- No settings changed.",
            "- No Telegram messages sent.",
            "- No CRM/Paperclip/deploy/outreach/git/DNS/billing/Stripe actions performed.",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true", help="Print JSON instead of markdown")
    parser.add_argument("--write-status", action="store_true", help=f"Write markdown status to {STATUS_PATH}")
    args = parser.parse_args()

    report = build_report()
    if args.write_status:
        STATUS_PATH.parent.mkdir(parents=True, exist_ok=True)
        STATUS_PATH.write_text(render_markdown(report))

    if args.json:
        print(json.dumps(report, indent=2))
    else:
        print(render_markdown(report))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

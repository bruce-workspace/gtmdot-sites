#!/usr/bin/env python3
"""
GTMDot Dispatcher Bridge B1.0

Dry-run bridge for turning GTMDot lane status files + Paperclip metadata into:
- one quarterback digest,
- lane outbox prompts,
- dispatcher state JSON.

This script intentionally does not mutate CRM, Paperclip, deploy targets, sends,
git remotes, DNS, billing, or production content. Paperclip is read-only in B1.0.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
import urllib.error
import urllib.request
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CONFIG = REPO_ROOT / "config" / "dispatcher-routing.json"
GTM_RE = re.compile(r"\bGTM-\d+\b")
PATH_RE = re.compile(r"(/Users/bruce/[^\s`)]+\.md)")


@dataclass
class LaneStatus:
    key: str
    display_name: str
    path: Path
    exists: bool
    updated: str | None = None
    mode: str | None = None
    objective: str = ""
    state: str = ""
    blockers: str = ""
    decisions: str = ""
    actions_done: str = ""
    actions_not_done: str = ""
    next_action: str = ""
    cross_lane: str = ""
    notify: str = ""
    gtm_ids: list[str] = field(default_factory=list)
    artifact_paths: list[str] = field(default_factory=list)
    age_hours: float | None = None
    digest: str = ""
    warning: str | None = None


def now_local() -> datetime:
    return datetime.now().astimezone()


def iso_now() -> str:
    return now_local().replace(microsecond=0).isoformat()


def rel_or_abs(path_value: str) -> Path:
    p = Path(path_value)
    return p if p.is_absolute() else REPO_ROOT / p


def read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text())


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")


def file_sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def first_meta_line(text: str, key: str) -> str | None:
    pat = re.compile(rf"^{re.escape(key)}:\s*(.+?)\s*$", re.MULTILINE | re.IGNORECASE)
    m = pat.search(text)
    return m.group(1).strip() if m else None


def section(text: str, names: list[str]) -> str:
    headings = [re.escape(name) for name in names]
    pattern = re.compile(
        rf"^##\s+({'|'.join(headings)})\s*$\n(?P<body>.*?)(?=^##\s+|\Z)",
        re.MULTILINE | re.DOTALL | re.IGNORECASE,
    )
    m = pattern.search(text)
    if not m:
        # Some older files use plain labels instead of markdown headings.
        for name in names:
            label = re.compile(
                rf"^{re.escape(name)}:\s*$\n(?P<body>.*?)(?=^[A-Z][A-Za-z /-]+:\s*$|\Z)",
                re.MULTILINE | re.DOTALL,
            )
            m2 = label.search(text)
            if m2:
                return clean_block(m2.group("body"))
        return ""
    return clean_block(m.group("body"))


def clean_block(text: str, max_chars: int = 1600) -> str:
    lines = [line.rstrip() for line in text.strip().splitlines()]
    cleaned = "\n".join(lines).strip()
    if len(cleaned) > max_chars:
        return cleaned[: max_chars - 3].rstrip() + "..."
    return cleaned


def one_line(text: str, max_chars: int = 260) -> str:
    collapsed = re.sub(r"\s+", " ", text.strip())
    if not collapsed:
        return ""
    return collapsed if len(collapsed) <= max_chars else collapsed[: max_chars - 3].rstrip() + "..."


def parse_datetime(value: str | None) -> datetime | None:
    if not value:
        return None
    raw = value.strip().replace("Z", "+00:00")
    try:
        return datetime.fromisoformat(raw)
    except ValueError:
        return None


def lane_age_hours(updated: str | None, path: Path) -> float | None:
    dt = parse_datetime(updated)
    if dt is None and path.exists():
        dt = datetime.fromtimestamp(path.stat().st_mtime, tz=timezone.utc)
    if dt is None:
        return None
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return (now_local() - dt.astimezone()).total_seconds() / 3600


def parse_lane_status(key: str, display_name: str, path: Path, stale_hours: float) -> LaneStatus:
    if not path.exists():
        return LaneStatus(
            key=key,
            display_name=display_name,
            path=path,
            exists=False,
            warning="missing status file",
        )

    text = path.read_text(errors="replace")
    updated = first_meta_line(text, "Updated")
    age = lane_age_hours(updated, path)
    warning = None
    if age is not None and age > stale_hours:
        warning = f"stale status file ({age:.1f}h old)"

    gtm_ids = sorted(set(GTM_RE.findall(text)), key=lambda v: int(v.split("-")[1]))
    artifacts = sorted(set(PATH_RE.findall(text)))

    objective = section(text, ["Current objective"])
    state = section(text, ["Current state"])
    blockers = section(text, ["Blockers"])
    decisions = section(text, ["Decisions needed from Jesse", "Jesse decisions needed"])
    actions_done = section(text, ["Actions completed since last update", "Actions completed"])
    actions_not_done = section(text, ["Actions explicitly not performed"])
    next_action = section(text, ["Next recommended action"])
    cross_lane = section(text, ["Cross-lane impacts"])
    notify = section(text, ["Notify"])

    digest_parts = [
        one_line(state or objective, 320),
        one_line(next_action, 320),
    ]
    digest = " ".join(part for part in digest_parts if part)

    return LaneStatus(
        key=key,
        display_name=display_name,
        path=path,
        exists=True,
        updated=updated,
        mode=first_meta_line(text, "Mode"),
        objective=objective,
        state=state,
        blockers=blockers,
        decisions=decisions,
        actions_done=actions_done,
        actions_not_done=actions_not_done,
        next_action=next_action,
        cross_lane=cross_lane,
        notify=notify,
        gtm_ids=gtm_ids,
        artifact_paths=artifacts,
        age_hours=age,
        digest=digest,
        warning=warning,
    )


def http_get_json(url: str, timeout: float = 4.0) -> tuple[Any | None, str | None]:
    errors: list[str] = []
    try:
        req = urllib.request.Request(url, headers={"Accept": "application/json"})
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            body = resp.read().decode("utf-8")
            return json.loads(body), None
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError, OSError) as e:
        errors.append(f"urllib: {e}")

    # Codex's Python socket sandbox may block localhost while curl is allowed.
    try:
        result = subprocess.run(
            ["curl", "-sS", url],
            check=False,
            capture_output=True,
            text=True,
            timeout=timeout,
        )
        if result.returncode == 0:
            return json.loads(result.stdout), None
        errors.append(f"curl exit {result.returncode}: {result.stderr.strip()}")
    except (subprocess.SubprocessError, json.JSONDecodeError, OSError) as e:
        errors.append(f"curl: {e}")

    return None, "; ".join(errors)


def paperclip_snapshot(config: dict[str, Any]) -> dict[str, Any]:
    pc = config["paperclip"]
    base = pc["base_url"].rstrip("/")
    company_id = pc["company_id"]

    health, health_error = http_get_json(f"{base}/api/health")
    dashboard, dashboard_error = http_get_json(f"{base}/api/companies/{company_id}/dashboard")
    issues, issues_error = http_get_json(f"{base}/api/companies/{company_id}/issues?limit=200")
    source = "api"

    if health is None or dashboard is None or issues is None:
        cached = read_paperclip_cache(config)
        if cached:
            health = health if health is not None else cached.get("health")
            dashboard = dashboard if dashboard is not None else cached.get("dashboard")
            issues = issues if issues is not None else cached.get("issues")
            source = "api+cache" if health_error or dashboard_error or issues_error else "cache"

    if not isinstance(issues, list):
        issues = []

    return {
        "base_url": base,
        "company_id": company_id,
        "dashboard_url": pc.get("dashboard_url"),
        "health": health,
        "health_error": health_error,
        "dashboard": dashboard,
        "dashboard_error": dashboard_error,
        "issues": issues,
        "issues_error": issues_error,
        "source": source,
    }


def read_paperclip_cache(config: dict[str, Any]) -> dict[str, Any] | None:
    cache_dir_value = config.get("paths", {}).get("paperclip_cache_dir")
    if not cache_dir_value:
        return None
    cache_dir = rel_or_abs(cache_dir_value)
    files = {
        "health": cache_dir / "paperclip-health.json",
        "dashboard": cache_dir / "paperclip-dashboard.json",
        "issues": cache_dir / "paperclip-issues.json",
    }
    if not any(path.exists() for path in files.values()):
        return None

    data: dict[str, Any] = {}
    for key, path in files.items():
        if not path.exists():
            continue
        try:
            data[key] = json.loads(path.read_text())
        except (json.JSONDecodeError, OSError):
            continue
    return data


def latest_backup(backups_dir: Path) -> dict[str, Any]:
    if not backups_dir.exists():
        return {"ok": False, "warning": "backup directory missing", "path": str(backups_dir)}

    files = sorted(backups_dir.glob("*.sql.gz"), key=lambda p: p.stat().st_mtime, reverse=True)
    if not files:
        return {"ok": False, "warning": "no backup files found", "path": str(backups_dir)}

    p = files[0]
    age = (now_local() - datetime.fromtimestamp(p.stat().st_mtime).astimezone()).total_seconds() / 3600
    return {
        "ok": True,
        "path": str(p),
        "age_hours": age,
        "size_bytes": p.stat().st_size,
    }


def recent_message_artifacts(messages_dir: Path, hours: float, limit: int = 24) -> list[dict[str, Any]]:
    cutoff = now_local().timestamp() - hours * 3600
    candidates: list[Path] = []
    for p in messages_dir.glob("*.md"):
        if p.is_file() and p.stat().st_mtime >= cutoff:
            candidates.append(p)
    candidates.sort(key=lambda p: p.stat().st_mtime, reverse=True)

    rows = []
    for p in candidates[:limit]:
        text = p.read_text(errors="replace")
        rows.append(
            {
                "path": str(p),
                "name": p.name,
                "mtime": datetime.fromtimestamp(p.stat().st_mtime).astimezone().replace(microsecond=0).isoformat(),
                "gtm_ids": sorted(set(GTM_RE.findall(text)), key=lambda v: int(v.split("-")[1])),
                "summary": infer_artifact_summary(text, p.name),
                "sha256": file_sha256(p),
            }
        )
    return rows


def infer_artifact_summary(text: str, fallback: str) -> str:
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("# "):
            return stripped[2:].strip()
    for line in text.splitlines():
        stripped = line.strip("- ").strip()
        if stripped and not stripped.startswith("[") and len(stripped) > 20:
            return one_line(stripped, 220)
    return fallback


def extract_approval_items(lanes: list[LaneStatus]) -> list[dict[str, str]]:
    items: list[dict[str, str]] = []
    seen: set[tuple[str, str]] = set()
    for lane in lanes:
        # The quarterback file is a rollup; pulling its old decisions back into
        # the queue creates noisy loops. Use lane files as the actionable source.
        if lane.key == "quarterback":
            continue
        blob = "\n".join([lane.decisions, lane.next_action, lane.blockers])
        if not blob:
            continue
        for line in blob.splitlines():
            raw = line.strip()
            if not raw:
                continue
            lower = raw.lower()
            if any(word in lower for word in ["approve", "approval", "decision", "decide", "awaiting jesse"]):
                key = (lane.key, raw)
                if key in seen:
                    continue
                seen.add(key)
                items.append(
                    {
                        "lane": lane.key,
                        "issue_ids": ", ".join(lane.gtm_ids) if lane.gtm_ids else "unknown",
                        "item": raw.lstrip("- "),
                    }
                )
    return items


def issue_summary(issues: list[dict[str, Any]]) -> dict[str, Any]:
    counts: dict[str, int] = {}
    by_identifier: dict[str, dict[str, Any]] = {}
    for issue in issues:
        status = issue.get("status") or "unknown"
        counts[status] = counts.get(status, 0) + 1
        ident = issue.get("identifier")
        if ident:
            by_identifier[ident] = {
                "title": issue.get("title"),
                "status": status,
                "priority": issue.get("priority"),
                "updatedAt": issue.get("updatedAt"),
            }
    return {"counts": counts, "by_identifier": by_identifier}


def route_for_ids(gtm_ids: list[str], issue_routes: dict[str, str], fallback: str) -> str:
    for gtm_id in gtm_ids:
        if gtm_id in issue_routes:
            return issue_routes[gtm_id]
    return fallback


def ensure_dirs(config: dict[str, Any]) -> dict[str, Path]:
    dispatcher_dir = rel_or_abs(config["paths"]["dispatcher_dir"])
    paths = {
        "dispatcher": dispatcher_dir,
        "digests": dispatcher_dir / "digests",
        "outbox": dispatcher_dir / "outbox",
        "state": dispatcher_dir / "state.json",
    }
    for p in [paths["dispatcher"], paths["digests"], paths["outbox"]]:
        p.mkdir(parents=True, exist_ok=True)
    return paths


def render_digest(
    timestamp: str,
    lanes: list[LaneStatus],
    paperclip: dict[str, Any],
    backup: dict[str, Any],
    recent_artifacts: list[dict[str, Any]],
    approvals: list[dict[str, str]],
    config: dict[str, Any],
) -> str:
    issue_data = issue_summary(paperclip["issues"])
    health_payload = paperclip.get("health")
    if isinstance(health_payload, dict) and health_payload.get("status") == "ok":
        pc_health = "ok"
        if paperclip.get("health_error"):
            pc_health += " (from cache; direct Python localhost read blocked)"
    elif paperclip.get("health_error"):
        pc_health = f"error: {paperclip.get('health_error')}"
    else:
        pc_health = "unknown"
    dashboard = paperclip.get("dashboard") or {}
    tasks = dashboard.get("tasks") if isinstance(dashboard, dict) else None
    agents = dashboard.get("agents") if isinstance(dashboard, dict) else None

    next_moves = recommended_moves(lanes, approvals)

    lines = [
        f"# GTMDot Dispatcher Digest - {timestamp}",
        "",
        "Mode: B1.0 dry-run only",
        "Authority: Git/message files + Paperclip are canonical; Slack/Telegram are notification mirrors.",
        "",
        "## Executive State",
        f"- Paperclip health: {pc_health}",
        f"- Paperclip read source: {paperclip.get('source', 'unknown')}",
        f"- Paperclip dashboard: {config['paperclip'].get('dashboard_url')}",
        f"- Paperclip task counts: {json.dumps(tasks, sort_keys=True) if tasks else 'unavailable'}",
        f"- Paperclip agent counts: {json.dumps(agents, sort_keys=True) if agents else 'unavailable'}",
        f"- Local issue counts: {json.dumps(issue_data['counts'], sort_keys=True)}",
        f"- Approval queue items found: {len(approvals)}",
        f"- Recent artifacts scanned: {len(recent_artifacts)}",
        "",
        "## Recommended Next 3 Moves",
    ]
    for i, move in enumerate(next_moves[:3], 1):
        lines.append(f"{i}. {move}")

    lines.extend(["", "## Approval Queue"])
    if approvals:
        for item in approvals[:20]:
            lines.append(f"- {item['lane']} / {item['issue_ids']}: {item['item']}")
    else:
        lines.append("- No explicit approval/decision lines detected in lane status files.")

    lines.extend(["", "## Lane Status"])
    for lane in lanes:
        warn = f" WARNING: {lane.warning}." if lane.warning else ""
        updated = lane.updated or "unknown"
        ids = ", ".join(lane.gtm_ids) if lane.gtm_ids else "none detected"
        lines.extend(
            [
                f"### {lane.display_name}",
                f"- Status file: `{lane.path}`",
                f"- Updated: {updated}{warn}",
                f"- Paperclip IDs: {ids}",
                f"- Summary: {lane.digest or 'No summary extracted.'}",
            ]
        )
        if lane.blockers:
            lines.append(f"- Blockers: {one_line(lane.blockers, 360)}")
        if lane.decisions:
            lines.append(f"- Decisions: {one_line(lane.decisions, 360)}")
        if lane.next_action:
            lines.append(f"- Next action: {one_line(lane.next_action, 360)}")
        lines.append("")

    lines.extend(["## Recent Artifacts"])
    if recent_artifacts:
        for artifact in recent_artifacts:
            ids = ", ".join(artifact["gtm_ids"]) if artifact["gtm_ids"] else "no GTM ID"
            lines.append(f"- `{artifact['name']}` ({ids}, {artifact['mtime']}): {artifact['summary']}")
    else:
        lines.append("- No recent top-level message artifacts found.")

    lines.extend(["", "## Paperclip Health"])
    lines.append(f"- API base: {paperclip.get('base_url')}")
    lines.append(f"- Read source: {paperclip.get('source', 'unknown')}")
    lines.append(f"- Health: {pc_health}")
    if paperclip.get("dashboard_error"):
        lines.append(f"- Dashboard read error: {paperclip['dashboard_error']}")
    if paperclip.get("issues_error"):
        lines.append(f"- Issue read error: {paperclip['issues_error']}")
    if backup.get("ok"):
        backup_warning = ""
        age = backup.get("age_hours")
        if isinstance(age, (int, float)) and age > config["staleness"]["backup_warning_hours"]:
            backup_warning = " WARNING: backup older than threshold."
        lines.append(
            f"- Latest backup: `{backup['path']}` ({backup.get('size_bytes')} bytes, {age:.2f}h old).{backup_warning}"
        )
    else:
        lines.append(f"- Backup warning: {backup.get('warning')}")

    lines.extend(
        [
            "",
            "## Guardrails",
            "- No CRM/Supabase writes performed.",
            "- No Paperclip mutations performed.",
            "- No deploys performed.",
            "- No Poplar/Resend/SMS sends performed.",
            "- No prospect/customer contact performed.",
            "- No git pushes performed.",
            "- No production site edits performed.",
        ]
    )

    return "\n".join(lines).rstrip() + "\n"


def recommended_moves(lanes: list[LaneStatus], approvals: list[dict[str, str]]) -> list[str]:
    moves: list[str] = []
    lane_by_key = {lane.key: lane for lane in lanes}

    post = lane_by_key.get("post-build")
    outreach = lane_by_key.get("outreach")
    platform = lane_by_key.get("platform")

    if post and "InTire" in post.state + post.next_action:
        moves.append("Decide InTire Mobile Tire Shop: approve/hold stage movement and channels now that GTM-14 technical readiness passed.")
    if outreach and "Harrison" in outreach.state + outreach.next_action:
        moves.append("Resolve Harrison Poplar failure: capture exact provider error if possible, or approve one normalized-address retry with stop-on-error language.")
    if outreach and "GTM-24" in outreach.state + outreach.next_action:
        moves.append("Continue GTM-24 reply-monitoring work only after deciding deploy/test boundary for hello@gtmdot.com reply handling.")
    if platform and "CRM v2" in platform.state:
        moves.append("Keep CRM v2 lab aligned with channel-state truth, stale-note handling, Paperclip links, and provider error visibility.")

    for item in approvals:
        candidate = f"Answer approval item from {item['lane']}: {item['item']}"
        if candidate not in moves:
            moves.append(candidate)

    if not moves:
        moves.append("Review lane outbox files and send the highest-priority requested action to its owning lane.")
    return moves


def render_outbox(lane: LaneStatus, timestamp: str) -> str:
    issue_ids = ", ".join(lane.gtm_ids) if lane.gtm_ids else "unknown"
    artifacts = "\n".join(f"- `{p}`" for p in lane.artifact_paths[:12]) or "- None detected"
    requested = lane.next_action or lane.decisions or "Review current lane status and return any blockers, decisions, and next recommended owner."

    return f"""# Dispatcher -> {lane.display_name}

Generated: {timestamp}
Source: GTMDot Dispatcher Bridge B1.0 dry-run
Paperclip issues: {issue_ids}
Lane status file: `{lane.path}`

## Context
{lane.digest or 'No current summary extracted.'}

## Requested Action
{requested}

## Latest Artifacts
{artifacts}

## Boundaries
- No CRM writes unless explicitly approved.
- No Paperclip mutations unless explicitly approved.
- No deploys unless explicitly approved.
- No Poplar/Resend/SMS sends unless explicitly approved.
- No prospect/customer contact unless explicitly approved.
- No git pushes unless explicitly approved.
- No DNS/domain/hosting/billing/Stripe actions unless explicitly approved.

## Required Return
- Update your lane status file.
- Link any new artifact path.
- State blockers, stale blockers, and current blockers separately.
- State next recommended owner.
- State actions explicitly not performed.
"""


def update_quarterback_status(digest_path: Path, timestamp: str, lanes: list[LaneStatus], approvals: list[dict[str, str]], digest_file: Path) -> None:
    lines = [
        "Lane: Quarterback / GTMDot Control Plane",
        "Session: Dispatcher Bridge B1.0",
        f"Updated: {timestamp}",
        "Owner: Codex / Dispatcher Bridge",
        "Mode: dry-run coordination digest generated",
        "",
        "Current objective:",
        "Keep the active GTMDot lanes synchronized through the file ledger and local Paperclip without requiring Jesse to manually copy every update between sessions.",
        "",
        "Current state:",
        f"Dispatcher B1.0 generated a dry-run digest at `{digest_file}`. No Paperclip, CRM, deploy, send, contact, git, or production mutations were performed.",
        "",
        "Active prospects/items:",
    ]
    for lane in lanes:
        ids = ", ".join(lane.gtm_ids) if lane.gtm_ids else "no GTM IDs detected"
        lines.append(f"- {lane.display_name}: {ids}")
    lines.extend(["", "Latest artifacts:", f"- `{digest_file}`", "", "Paperclip issues:"])
    for lane in lanes:
        ids = ", ".join(lane.gtm_ids) if lane.gtm_ids else "none"
        lines.append(f"- {lane.display_name}: {ids}")
    lines.extend(["", "Blockers:"])
    for lane in lanes:
        if lane.warning:
            lines.append(f"- {lane.display_name}: {lane.warning}")
    if not any(lane.warning for lane in lanes):
        lines.append("- No lane status freshness blockers detected.")
    lines.extend(["", "Decisions needed from Jesse:"])
    if approvals:
        for item in approvals[:12]:
            lines.append(f"- {item['lane']} / {item['issue_ids']}: {item['item']}")
    else:
        lines.append("- No explicit approval lines detected by the dispatcher.")
    lines.extend(
        [
            "",
            "Actions completed since last update:",
            "- Ran Dispatcher Bridge B1.0 dry-run.",
            "- Generated main digest and lane outbox files.",
            "- Updated dispatcher state JSON.",
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
            "Use the dispatcher digest approval queue and lane outbox files to route the next board-clearing action without manual re-summarization.",
            "",
            "Cross-lane impacts:",
            "- B1.0 makes lane status files the operational bridge until Paperclip safe-update mode is approved.",
            "- Future B1.1 can add Paperclip comments/status updates after the dry-run output is trusted.",
            "",
            "Notify:",
            "Pre-Build Coordination, Post-Build Operations, Outreach Operations, GTMDot Platform, Experiments, Bruce, R1VS as needed by outbox files.",
        ]
    )
    digest_path.write_text("\n".join(lines).rstrip() + "\n")


def main() -> int:
    parser = argparse.ArgumentParser(description="GTMDot Dispatcher Bridge B1.0")
    parser.add_argument("--config", default=str(DEFAULT_CONFIG), help="Path to dispatcher routing config JSON.")
    parser.add_argument("--dry-run", action="store_true", default=True, help="Dry-run mode. This is the only B1.0 mode.")
    parser.add_argument("--no-quarterback-update", action="store_true", help="Do not update messages/status/quarterback-latest.md.")
    args = parser.parse_args()

    config_path = Path(args.config)
    if not config_path.exists():
        print(f"error: config not found: {config_path}", file=sys.stderr)
        return 2
    config = read_json(config_path)

    paths = ensure_dirs(config)
    timestamp = iso_now()
    stamp = now_local().strftime("%Y-%m-%d-%H%M")

    lane_names = config["lane_display_names"]
    stale_hours = float(config["staleness"]["lane_warning_hours"])
    lanes: list[LaneStatus] = []
    for lane_key, path_value in config["lane_status_files"].items():
        lanes.append(parse_lane_status(lane_key, lane_names.get(lane_key, lane_key), rel_or_abs(path_value), stale_hours))

    paperclip = paperclip_snapshot(config)
    backup = latest_backup(Path(config["paths"]["paperclip_backups_dir"]))
    recent = recent_message_artifacts(rel_or_abs(config["paths"]["messages_dir"]), float(config["staleness"]["recent_artifact_hours"]))
    approvals = extract_approval_items(lanes)

    digest = render_digest(timestamp, lanes, paperclip, backup, recent, approvals, config)
    digest_path = paths["digests"] / f"{stamp}-dispatcher-digest.md"
    digest_path.write_text(digest)

    outbox_files: list[str] = []
    for lane in lanes:
        if lane.key == "quarterback":
            continue
        outbox_path = paths["outbox"] / f"{stamp}-to-{lane.key}.md"
        outbox_path.write_text(render_outbox(lane, timestamp))
        outbox_files.append(str(outbox_path))

    if not args.no_quarterback_update:
        update_quarterback_status(
            rel_or_abs(config["lane_status_files"]["quarterback"]),
            timestamp,
            lanes,
            approvals,
            digest_path,
        )

    state = {
        "last_run_at": timestamp,
        "mode": "dry-run",
        "config_path": str(config_path),
        "digest_path": str(digest_path),
        "outbox_files": outbox_files,
        "paperclip": {
            "health_ok": bool(paperclip.get("health")),
            "dashboard_ok": bool(paperclip.get("dashboard")),
            "issues_read": len(paperclip.get("issues") or []),
            "source": paperclip.get("source"),
            "health_error": paperclip.get("health_error"),
            "dashboard_error": paperclip.get("dashboard_error"),
            "issues_error": paperclip.get("issues_error"),
        },
        "backup": backup,
        "lane_files": {
            lane.key: {
                "path": str(lane.path),
                "exists": lane.exists,
                "updated": lane.updated,
                "age_hours": lane.age_hours,
                "sha256": file_sha256(lane.path) if lane.path.exists() else None,
                "warning": lane.warning,
                "gtm_ids": lane.gtm_ids,
            }
            for lane in lanes
        },
        "recent_artifacts": recent,
    }
    write_json(paths["state"], state)

    print(json.dumps({
        "ok": True,
        "mode": "dry-run",
        "digest_path": str(digest_path),
        "outbox_files": outbox_files,
        "state_path": str(paths["state"]),
        "paperclip_issues_read": len(paperclip.get("issues") or []),
        "approval_items": len(approvals),
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

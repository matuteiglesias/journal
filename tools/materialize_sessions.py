#!/usr/bin/env python3
"""
materialize_sessions.py

Read session bus daily JSONL files and materialize Quartz markdown pages.

Design goals
- Prefer canonical session.v1 fields
- Tolerate hybrid records that still carry legacy `summary`
- Emit to a scratch content directory by default
- Keep generated artifacts deterministic and diff-friendly

Example:
    python tools/materialize_sessions.py \
        --sessions-dir /home/matias/Documents/buses/sessions_bus/sessions/daily \
        --output-dir /home/matias/repos/quartz/content_generated \
        --top-n 40

Then inspect:
    find content_generated -maxdepth 2 -type f | sort | head -50

Then build Quartz against that generated content after copying or swapping in.
"""

from __future__ import annotations

import argparse
import json
import os
import shutil
import sys
import tempfile
from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Set, Tuple

try:
    import regex as _re
except Exception:
    import re as _re


# -----------------------------
# IO and filesystem helpers
# -----------------------------

def atomic_write(path: Path, text: str, encoding: str = "utf-8") -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=str(path.parent))
    try:
        with os.fdopen(fd, "w", encoding=encoding) as fh:
            fh.write(text)
        os.replace(tmp, str(path))
    except Exception:
        try:
            os.remove(tmp)
        except Exception:
            pass
        raise

def maybe_copy_root_index(output_dir: Path, seed_root_from: Path | None) -> None:
    target = output_dir / "index.md"
    if target.exists():
        return
    if seed_root_from and (seed_root_from / "index.md").exists():
        target.write_text((seed_root_from / "index.md").read_text(encoding="utf-8"), encoding="utf-8")

def safe_filename(text: str, max_len: int = 120) -> str:
    s = str(text or "").strip()
    s = _re.sub(r"[\x00-\x1f]", "", s)
    s = _re.sub(r'[\\/:"*?<>|]+', "_", s)
    s = _re.sub(r"\s+", "_", s)
    s = s.strip("._ ")
    if len(s) > max_len:
        s = s[:max_len].rstrip("._ ")
    return s or "untitled"


def slugify(text: str, max_len: int = 80) -> str:
    s = str(text or "").strip().lower()
    s = _re.sub(r"[^\p{L}\p{N}\s_-]", "", s)
    s = _re.sub(r"[\s_]+", "-", s)
    s = s.strip("-")
    if len(s) > max_len:
        s = s[:max_len].rstrip("-")
    return s or "untitled"


# -----------------------------
# Domain helpers
# -----------------------------

def normalize_tag(tag: str) -> str:
    if not tag:
        return ""
    t = str(tag).strip()
    return t if t.isupper() else t.title()


def parse_hhmm_or_none(value: Optional[str]) -> Optional[str]:
    if not value:
        return None
    try:
        return datetime.strptime(value, "%H:%M").strftime("%H:%M")
    except Exception:
        return None


def ts_ms_to_local_iso(ts_ms: Any) -> Optional[str]:
    try:
        ts = int(ts_ms)
        if ts <= 0:
            return None
        return datetime.fromtimestamp(ts / 1000).isoformat(timespec="seconds")
    except Exception:
        return None


def first_nonempty(*values: Any) -> Optional[Any]:
    for v in values:
        if v is None:
            continue
        if isinstance(v, str) and not v.strip():
            continue
        return v
    return None


@dataclass
class SessionView:
    session_id: str
    day: str
    title: str
    description: str
    tags: List[str]
    project: str
    workspace: str
    status: str
    priority: str
    assignee: str
    start_label: str
    end_label: str
    created: str
    source_file: str
    line_number: Optional[int]
    publish: bool
    event_count: int
    event_ids: List[str]
    evidence_note: str


# -----------------------------
# Validation and adaptation
# -----------------------------

def validate_session_record(rec: Dict[str, Any]) -> List[str]:
    errs: List[str] = []

    schema_version = rec.get("schema_version")
    if schema_version != "session.v1":
        errs.append(f"unexpected schema_version={schema_version!r}")

    if not rec.get("session_id"):
        errs.append("missing session_id")

    day = rec.get("day")
    if not isinstance(day, str) or len(day) != 10:
        errs.append("missing or invalid day")

    window = rec.get("window")
    if not isinstance(window, dict):
        errs.append("missing window")
    else:
        for k in ["window_type", "start_ts_ms", "end_ts_ms"]:
            if k not in window:
                errs.append(f"window missing {k}")

    event_ids = rec.get("event_ids")
    if not isinstance(event_ids, list):
        errs.append("missing or invalid event_ids")

    if "event_count" not in rec:
        errs.append("missing event_count")

    return errs


def derive_title(rec: Dict[str, Any]) -> str:
    title_candidates = rec.get("title_candidates") or []
    if isinstance(title_candidates, list):
        for t in title_candidates:
            if isinstance(t, str) and t.strip():
                return t.strip()

    summary = rec.get("summary") or {}
    legacy_name = summary.get("name")
    if isinstance(legacy_name, str) and legacy_name.strip():
        return legacy_name.strip()

    notes = rec.get("notes")
    if isinstance(notes, str) and notes.strip():
        line = notes.strip().splitlines()[0].strip()
        return line[:120]

    return rec.get("session_id") or rec.get("id") or "Untitled Session"


def derive_description(rec: Dict[str, Any]) -> str:
    notes = rec.get("notes")
    if isinstance(notes, str) and notes.strip():
        return notes.strip()

    summary = rec.get("summary") or {}
    desc = summary.get("description")
    if isinstance(desc, str) and desc.strip():
        return desc.strip()

    return ""


def derive_tags(rec: Dict[str, Any]) -> List[str]:
    labels = rec.get("labels")
    if not isinstance(labels, list) or not labels:
        summary = rec.get("summary") or {}
        labels = summary.get("labels") or []

    out = []
    seen = set()
    for t in labels:
        nt = normalize_tag(str(t))
        if nt and nt not in seen:
            seen.add(nt)
            out.append(nt)
    return out


def derive_project(rec: Dict[str, Any]) -> str:
    summary = rec.get("summary") or {}
    return str(
        first_nonempty(
            rec.get("project"),
            rec.get("project_name"),
            rec.get("workspace"),
            summary.get("projectName"),
            "Unknown",
        )
    ).strip()


def derive_workspace(rec: Dict[str, Any]) -> str:
    summary = rec.get("summary") or {}
    return str(
        first_nonempty(
            rec.get("workspace"),
            rec.get("workspace_name"),
            summary.get("workspaceName"),
            "",
        )
    ).strip()


def derive_status(rec: Dict[str, Any]) -> str:
    summary = rec.get("summary") or {}
    return str(first_nonempty(rec.get("status"), summary.get("status"), "")).strip()


def derive_priority(rec: Dict[str, Any]) -> str:
    summary = rec.get("summary") or {}
    return str(first_nonempty(rec.get("priority"), summary.get("priority"), "")).strip()


def derive_assignee(rec: Dict[str, Any]) -> str:
    summary = rec.get("summary") or {}
    return str(
        first_nonempty(rec.get("assignee"), summary.get("assigneeId"), "")
    ).strip()


def derive_times(rec: Dict[str, Any]) -> Tuple[str, str]:
    summary = rec.get("summary") or {}
    legacy_start = parse_hhmm_or_none(summary.get("startTime"))
    legacy_end = parse_hhmm_or_none(summary.get("endTime"))

    window = rec.get("window") or {}
    canonical_start = ts_ms_to_local_iso(window.get("start_ts_ms"))
    canonical_end = ts_ms_to_local_iso(window.get("end_ts_ms"))

    # Prefer usable legacy HH:MM if canonical is placeholder 0/0
    start_label = legacy_start or canonical_start or "?"
    end_label = legacy_end or canonical_end or "?"
    return start_label, end_label


def compute_top_keywords(views: Iterable[SessionView], top_n: int) -> Set[str]:
    cnt = Counter()
    for v in views:
        cnt.update(v.tags)
    return {tag for tag, _ in cnt.most_common(top_n)}


def wikify_keywords(text: str, keywords: Set[str]) -> str:
    if not text or not keywords:
        return text

    kws = sorted([k for k in keywords if k], key=len, reverse=True)
    out = text
    for kw in kws:
        if f"[[{kw}]]" in out:
            continue
        pattern = rf"(?i)\b{_re.escape(kw)}\b"
        out = _re.sub(pattern, lambda m: f"[[{m.group(0)}]]", out)
    return out


def make_session_view(
    rec: Dict[str, Any],
    source_file: Path,
    excluded_categories: Set[str],
) -> SessionView:
    day = str(rec.get("day", "")).strip()
    title = derive_title(rec)
    description = derive_description(rec)
    tags = derive_tags(rec)
    project = derive_project(rec)
    workspace = derive_workspace(rec)
    status = derive_status(rec)
    priority = derive_priority(rec)
    assignee = derive_assignee(rec)
    start_label, end_label = derive_times(rec)

    line_number = rec.get("line_number")
    try:
        line_number = int(line_number) if line_number is not None else None
    except Exception:
        line_number = None

    event_ids = rec.get("event_ids") if isinstance(rec.get("event_ids"), list) else []
    try:
        event_count = int(rec.get("event_count", 0))
    except Exception:
        event_count = 0

    session_id = str(rec.get("session_id") or rec.get("id") or "").strip()
    if not session_id:
        session_id = f"{day}-{slugify(title)}"

    project_norm = project.strip().lower().replace(" ", "_")
    publish = project_norm not in excluded_categories

    evidence_bits = [
        f"source_file={source_file.name}",
        f"line_number={line_number if line_number is not None else '?'}",
        f"event_count={event_count}",
        f"session_id={session_id}",
    ]
    evidence_note = ", ".join(evidence_bits)

    return SessionView(
        session_id=session_id,
        day=day,
        title=title,
        description=description,
        tags=tags,
        project=project,
        workspace=workspace,
        status=status,
        priority=priority,
        assignee=assignee,
        start_label=start_label,
        end_label=end_label,
        created=day,
        source_file=source_file.name,
        line_number=line_number,
        publish=publish,
        event_count=event_count,
        event_ids=event_ids,
        evidence_note=evidence_note,
    )


# -----------------------------
# Materialization
# -----------------------------

def build_frontmatter(view: SessionView) -> str:
    tags_json = json.dumps(view.tags, ensure_ascii=False)
    return (
        "---\n"
        f'title: "{view.title.replace(chr(34), chr(39))}"\n'
        f"tags: {tags_json}\n"
        f"created: {view.created}\n"
        f"publish: {'true' if view.publish else 'false'}\n"
        f'session_id: "{view.session_id}"\n'
        f'source_file: "{view.source_file}"\n'
        "generated: true\n"
        "---\n\n"
    )


def build_session_markdown(view: SessionView, wikified_description: str) -> str:
    lines: List[str] = [
        f"# {view.title}",
        "",
        f"- **Day**: {view.day}",
        f"- **Time**: {view.start_label} to {view.end_label}",
        f"- **Project**: {view.project or 'Unknown'}",
        f"- **Workspace**: {view.workspace or 'Unknown'}",
        f"- **Status**: {view.status or 'Unknown'}",
        f"- **Priority**: {view.priority or 'Unknown'}",
        f"- **Assignee**: {view.assignee or 'Unknown'}",
        f"- **Tags**: {', '.join(view.tags) if view.tags else 'None'}",
        "",
    ]

    if wikified_description:
        lines.extend(
            [
                "## Description",
                "",
                wikified_description,
                "",
            ]
        )

    lines.extend(
        [
            "## Evidence",
            "",
            f"- {view.evidence_note}",
            f"- event_ids: {', '.join(view.event_ids) if view.event_ids else '[]'}",
            "",
        ]
    )
    return "\n".join(lines)


def materialize_sessions(
    sessions_dir: Path,
    output_dir: Path,
    top_n: int = 40,
    excluded_categories: Optional[Set[str]] = None,
    dry_run: bool = False,
    clean_output: bool = False,
) -> Dict[str, Any]:
    if excluded_categories is None:
        excluded_categories = {
            "health",
            "docs_and_planning",
            "docs and planning",
            "ceo",
            "jobmarket",
            "ai",
            "branding",
            "other",
        }
    excluded_norm = {c.strip().lower().replace(" ", "_") for c in excluded_categories}

    if not sessions_dir.exists() or not sessions_dir.is_dir():
        raise FileNotFoundError(f"sessions_dir not found: {sessions_dir}")

    files = sorted(sessions_dir.glob("*.sessions.jsonl"))
    if not files:
        print("no *.sessions.jsonl files found")
        return {
            "files": 0,
            "records": 0,
            "created": 0,
            "monthly": 0,
            "invalid": 0,
            "bad_lines": 0,
        }

    if clean_output and output_dir.exists() and not dry_run:
        shutil.rmtree(output_dir)

    views: List[SessionView] = []
    invalid_records: List[Dict[str, Any]] = []
    bad_lines = 0
    record_count = 0

    for fpath in files:
        with fpath.open("r", encoding="utf-8") as fh:
            for file_line_no, raw_line in enumerate(fh, start=1):
                line = raw_line.strip()
                if not line:
                    continue
                try:
                    rec = json.loads(line)
                except Exception:
                    bad_lines += 1
                    continue

                record_count += 1
                errs = validate_session_record(rec)
                if errs:
                    invalid_records.append(
                        {
                            "source_file": fpath.name,
                            "file_line_number": file_line_no,
                            "errors": errs,
                            "raw": rec,
                        }
                    )
                    continue

                views.append(make_session_view(rec, fpath, excluded_norm))

    if not views and not invalid_records:
        print("no valid records found")
        return {
            "files": len(files),
            "records": record_count,
            "created": 0,
            "monthly": 0,
            "invalid": 0,
            "bad_lines": bad_lines,
        }

    top_keywords = compute_top_keywords(views, top_n=top_n)

    created = 0
    monthly_created = 0

    by_project: Dict[str, List[SessionView]] = defaultdict(list)
    by_month: Dict[str, List[SessionView]] = defaultdict(list)

    for v in views:
        by_project[v.project or "Unknown"].append(v)
        by_month[v.day[:7]].append(v)

    for project_name, project_views in sorted(by_project.items(), key=lambda x: x[0].lower()):
        project_folder = output_dir / safe_filename(project_name)
        project_views.sort(key=lambda v: (v.day, v.start_label, v.title.lower(), v.session_id))

        for view in project_views:
            desc = wikify_keywords(view.description, top_keywords)
            text = build_frontmatter(view) + build_session_markdown(view, desc)
            fname = f"{view.day}_{slugify(view.title, 60)}_{view.session_id[:12]}.md"
            fpath = project_folder / fname

            if dry_run:
                print(f"[dry-run] would write {fpath}")
            else:
                atomic_write(fpath, text)
            created += 1

    monthly_dir = output_dir / "month_journals"
    for month, month_views in sorted(by_month.items(), reverse=True):
        month_views.sort(key=lambda v: (v.day, v.start_label, v.title.lower(), v.session_id), reverse=True)

        body_lines = [
            f"# Monthly Journal {month}",
            "",
        ]
        for v in month_views:
            if not v.publish:
                continue
            project_folder = safe_filename(v.project)
            fname = f"{v.day}_{slugify(v.title, 60)}_{v.session_id[:12]}.md"
            rel_path = f"../{project_folder}/{fname}"
            body_lines.append(f"- **{v.day}** · [{v.title}]({rel_path}) · {v.project}")

        text = (
            "---\n"
            f'title: "Monthly Journal {month}"\n'
            "tags: []\n"
            f"created: {month}-01\n"
            "publish: true\n"
            "generated: true\n"
            "---\n\n"
            + "\n".join(body_lines)
            + "\n"
        )

        outpath = monthly_dir / f"{month}.md"
        if dry_run:
            print(f"[dry-run] would write {outpath}")
        else:
            atomic_write(outpath, text)
        monthly_created += 1

    monthly_index = (
        "---\n"
        'title: "Journal by Month"\n'
        "tags: []\n"
        f"created: {datetime.now().date().isoformat()}\n"
        "publish: true\n"
        "generated: true\n"
        "---\n\n"
        "# Monthly Journal Archive\n\n"
    )
    if dry_run:
        print(f"[dry-run] would write {monthly_dir / 'index.md'}")
    else:
        atomic_write(monthly_dir / "index.md", monthly_index)

    if invalid_records:
        invalid_dir = output_dir / "invalid_sessions"
        payload = json.dumps(invalid_records, ensure_ascii=False, indent=2)
        if dry_run:
            print(f"[dry-run] would write {invalid_dir / 'invalid_sessions.json'}")
        else:
            atomic_write(invalid_dir / "invalid_sessions.json", payload)

    summary = {
        "files": len(files),
        "records": record_count,
        "created": created,
        "monthly": monthly_created,
        "invalid": len(invalid_records),
        "bad_lines": bad_lines,
        "projects": len(by_project),
    }
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return summary


# -----------------------------
# CLI
# -----------------------------

def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Materialize session bus JSONL into Quartz markdown")
    p.add_argument(
        "--sessions-dir",
        default="/home/matias/Documents/buses/sessions_bus/sessions/daily",
        help="directory containing *.sessions.jsonl files",
    )
    p.add_argument(
	    "--seed-root-from",
	    default=None,
	    help="optional existing content root to copy root files like index.md from",
	)
    p.add_argument(
        "--output-dir",
        default="content_generated",
        help="output directory for generated markdown",
    )
    p.add_argument(
        "--top-n",
        type=int,
        default=40,
        help="number of top tags to wikify",
    )
    p.add_argument(
        "--dry-run",
        action="store_true",
        help="print actions without writing files",
    )
    p.add_argument(
        "--clean-output",
        action="store_true",
        help="delete output-dir before writing",
    )
    return p.parse_args()


def main() -> int:
    args = parse_args()
    try:
        materialize_sessions(
            sessions_dir=Path(args.sessions_dir),
            output_dir=Path(args.output_dir),
            top_n=args.top_n,
            dry_run=args.dry_run,
            clean_output=args.clean_output,
        )
        return 0
    except Exception as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())

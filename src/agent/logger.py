from __future__ import annotations

import json
from collections import deque
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict


def _utc_ts() -> str:
    """Return UTC ISO-8601 timestamp with trailing 'Z'."""
    return (
        datetime.now(timezone.utc)
        .replace(microsecond=0)
        .isoformat()
        .replace("+00:00", "Z")
    )


def append_event(
    event: Dict[str, Any],
    log_path: str | Path = "memory/log.json",
    max_entries: int = 100,
) -> None:
    """
    Append a structured JSONL event to the local log with basic rotation.

    Schema example:
      {"ts":"2025-10-18T11:02:03Z","event":"run_start","jd":"...","profile":"..."}
      {"ts":"2025-10-18T11:02:03Z","event":"report_written","path":"..."}
      {"ts":"2025-10-18T11:02:03Z","event":"error","code":"PDF_NO_TEXT","msg":"..."}
    """
    p = Path(log_path)
    p.parent.mkdir(parents=True, exist_ok=True)

    # add timestamp field as 'ts' if not present
    if "ts" not in event:
        event = {"ts": _utc_ts(), **event}

    # read existing lines and keep last up to max_entries total (including the new event)
    lines: deque[str] = deque(maxlen=max_entries)
    if p.exists():
        try:
            with p.open("r", encoding="utf-8") as f:
                for line in f:
                    line = line.rstrip("\n")
                    if line:
                        lines.append(line)
        except Exception:
            # if log is unreadable, start fresh
            lines.clear()

    # append the new event; deque will cap at max_entries
    lines.append(json.dumps(event, ensure_ascii=False))

    # write back all kept lines + new event
    with p.open("w", encoding="utf-8") as f:
        for line in lines:
            f.write(line + "\n")


def append_run_log(
    entry: Dict[str, Any], log_path: str | Path = "memory/log.json"
) -> None:
    """Backward-compatible wrapper around append_event for legacy calls."""
    e = {"event": "summary", **entry}
    try:
        append_event(e, log_path=log_path)
    except Exception:
        # do not raise from logging
        pass

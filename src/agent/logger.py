from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path
from typing import Any, Dict


def append_run_log(entry: Dict[str, Any], log_path: str | Path = "memory/log.json") -> None:
    """
    Append a single JSON line to memory/log.json with minimal run metadata.
    Creates parent directory if needed. Intended to be local-only (ignored by git).
    """
    p = Path(log_path)
    p.parent.mkdir(parents=True, exist_ok=True)

    # Ensure a timestamp is present
    entry = {"timestamp": datetime.now().isoformat(timespec="seconds"), **entry}

    with p.open("a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")

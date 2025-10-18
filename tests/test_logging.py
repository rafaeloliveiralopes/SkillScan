import json
from pathlib import Path

from agent.logger import append_event


def test_append_event_jsonl_rotation(tmp_path: Path):
    log = tmp_path / "memory" / "log.json"
    # write 105 events; keep last 100
    for i in range(105):
        append_event({"event": "e", "i": i}, log_path=log, max_entries=100)

    lines = log.read_text(encoding="utf-8").splitlines()
    assert len(lines) == 100

    # first kept should be i=5, last should be i=104
    first = json.loads(lines[0])
    last = json.loads(lines[-1])
    assert first["i"] == 5
    assert last["i"] == 104
    assert "ts" in first and "event" in first

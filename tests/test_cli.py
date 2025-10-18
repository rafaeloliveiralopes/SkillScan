import json
import subprocess
import sys
from pathlib import Path


def run_cmd(args: list[str], cwd: Path) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, "-m", "agent.runner", *args],
        cwd=str(cwd),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )


def test_version_exit_zero(tmp_path: Path):
    proc = run_cmd(["version"], cwd=tmp_path)
    assert proc.returncode == 0
    assert proc.stdout.strip()  # prints version


def test_run_success_generates_report_and_logs(tmp_path: Path):
    # arrange
    jd = tmp_path / "jd.txt"
    jd.write_text("We need PYTHON and Postgres.", encoding="utf-8")
    profile = tmp_path / "profile.json"
    profile.write_text(
        json.dumps(
            {
                "name": "Carol Danvers",
                "skills": ["Python"],
                "languages": ["EN"],
            }
        ),
        encoding="utf-8",
    )
    out_dir = tmp_path / "reports"

    # act
    proc = run_cmd(
        [
            "run",
            "--jd",
            str(jd),
            "--profile",
            str(profile),
            "--out",
            str(out_dir),
            "--verbose",
        ],
        cwd=tmp_path,
    )

    # assert
    assert proc.returncode == 0
    assert "report written to:" in proc.stdout
    # check report file exists
    lines = [ln for ln in proc.stdout.splitlines() if "report written to:" in ln]
    report_path = Path(lines[0].split(":", 1)[1].strip())
    assert report_path.exists()

    # check memory log exists and has recent events
    log = tmp_path / "memory" / "log.json"
    assert log.exists()
    content = log.read_text(encoding="utf-8").strip().splitlines()
    assert any("run_start" in line for line in content)
    assert any("report_written" in line for line in content)


def test_run_errors_are_standardized(tmp_path: Path):
    # arrange: missing JD triggers error
    profile = tmp_path / "profile.json"
    profile.write_text(
        json.dumps(
            {
                "name": "Carol",
                "skills": ["Python"],
                "languages": ["EN"],
            }
        ),
        encoding="utf-8",
    )

    proc = run_cmd(
        [
            "run",
            "--jd",
            str(tmp_path / "missing.txt"),
            "--profile",
            str(profile),
        ],
        cwd=tmp_path,
    )

    assert proc.returncode == 1
    assert "ERROR: JD not found" in proc.stderr

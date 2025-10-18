from pathlib import Path

import pytest

from agent.parser import load_jd_text, load_profile


def test_load_jd_text_from_txt(tmp_path: Path):
    # arrange
    content = "Python and Docker are required."
    jd_file = tmp_path / "jd.txt"
    jd_file.write_text(content, encoding="utf-8")

    # act
    text = load_jd_text(str(jd_file))

    # assert
    assert "Python" in text
    assert "Docker" in text


def test_load_profile_happy(tmp_path: Path):
    data = {
        "name": "Carol",
        "skills": ["Python", "Flask"],
        "languages": ["Portuguese", "English"],
    }
    pf = tmp_path / "profile.json"
    pf.write_text(__import__("json").dumps(data), encoding="utf-8")

    profile = load_profile(str(pf))

    assert profile["name"] == "Carol"
    assert set(profile["skills"]) == {"Python", "Flask"}
    assert set(profile["languages"]) == {"Portuguese", "English"}


def test_load_profile_invalid_raises(tmp_path: Path):
    pf = tmp_path / "bad.json"
    pf.write_text("{}", encoding="utf-8")

    with pytest.raises(ValueError) as e:
        load_profile(str(pf))
    assert "profile.json is invalid" in str(e.value)

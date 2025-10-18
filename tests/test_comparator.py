from agent.comparator import compare_profile_to_jd


def test_compare_profile_to_jd_basic():
    profile = {
        "name": "Dev",
        "skills": ["Python", "Docker", "Git"],
        "languages": ["Portuguese"],
    }
    jd_text = "We use Python and PostgreSQL, plus Kubernetes."

    result = compare_profile_to_jd(profile, jd_text)

    # python matches, postgres and kubernetes are gaps, docker/git are extra
    assert "python" in result["matched"]
    assert "postgresql" in result["gaps"]
    assert "kubernetes" in result["gaps"]
    assert "docker" in result["extra"]
    assert "git" in result["extra"]

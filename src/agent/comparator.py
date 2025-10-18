from __future__ import annotations

import re
from typing import Dict, Iterable, List, Set

# --- léxico básico PT/EN (v0.1.0) ---
# Mantido simples e offline, com termos compostos comuns.
DEFAULT_SKILL_LEXICON: List[str] = [
    # geral / sw
    "python",
    "java",
    "c",
    "c++",
    "c#",
    "javascript",
    "typescript",
    "node.js",
    "react",
    "django",
    "flask",
    "fastapi",
    "git",
    "docker",
    "linux",
    "sql",
    "nosql",
    "postgresql",
    "mysql",
    "kubernetes",
    "ci/cd",
    "rest",
    "graphql",
    "aws",
    "gcp",
    "azure",
    # dados / ml
    "tensorflow",
    "pytorch",
    "pandas",
    "spark",
    "airflow",
    "etl",
    # embedded / firmware
    "rtos",
    "uart",
    "spi",
    "i2c",
    "usb",
    "ethernet",
    "fpga",
    "arm",
    "microcontroller",
    "bare-metal",
    "driver",
    "hal",
    # pt variantes
    "controle de versão",
    "integração contínua",
    "entrega contínua",
    "banco de dados",
    "protocolos de comunicação",
]

# normalizações e sinônimos simples
CANONICAL_MAP = {
    "nodejs": "node.js",
    "node": "node.js",
    "postgres": "postgresql",
    "postgre": "postgresql",
    "js": "javascript",
    "ts": "typescript",
    "c plus plus": "c++",
    "c sharp": "c#",
    "continuous integration": "ci/cd",
    "continuous delivery": "ci/cd",
    "integracao continua": "ci/cd",
    "entrega continua": "ci/cd",
    "versao": "controle de versão",
    "banco": "banco de dados",
    "mcus": "microcontroller",
    "mcu": "microcontroller",
}

_WORD = r"[A-Za-z0-9\-\+\./]+"  # inclui +, ., -, / para termos como C++, Node.js, CI/CD


def _norm(s: str) -> str:
    s = s.strip().lower()
    return CANONICAL_MAP.get(s, s)


def _compile_patterns(lexicon: Iterable[str]) -> List[re.Pattern]:
    pats = []
    for term in lexicon:
        t = re.escape(term.lower())
        # capturar por limites aproximados de palavra, preservando sinais como + e .
        pats.append(re.compile(rf"(?<!\w){t}(?!\w)"))
    return pats


def extract_skills(
    text: str, lexicon: Iterable[str] = DEFAULT_SKILL_LEXICON
) -> Set[str]:
    """
    Extrai skills do texto por match literal case-insensitive com léxico básico.
    Retorna conjunto de skills **canonizadas**.
    """
    content = " ".join(text.split()).lower()
    patterns = _compile_patterns(lexicon)
    found: Set[str] = set()
    for pat, term in zip(patterns, lexicon):
        if pat.search(content):
            found.add(_norm(term))
    return found


def canonize(skills: Iterable[str]) -> Set[str]:
    return {_norm(s) for s in skills}


def compare_profile_to_jd(
    profile: Dict, jd_text: str, lexicon: Iterable[str] = DEFAULT_SKILL_LEXICON
) -> Dict[str, List[str]]:
    """
    Compara skills do profile com as do JD.
    Retorna dict com: jd_skills, profile_skills, matched, gaps, extra.
    """
    jd_skills = extract_skills(jd_text, lexicon)
    profile_skills = canonize(profile.get("skills", []))

    matched = sorted(profile_skills & jd_skills)
    gaps = sorted(jd_skills - profile_skills)
    extra = sorted(profile_skills - jd_skills)

    return {
        "jd_skills": sorted(jd_skills),
        "profile_skills": sorted(profile_skills),
        "matched": matched,
        "gaps": gaps,
        "extra": extra,
    }


def simple_recommendations(
    result: Dict[str, List[str]], max_items: int = 5
) -> List[str]:
    """
    Gera recomendações simples a partir das lacunas (v0.1.0).
    """
    recs: List[str] = []
    for skill in result.get("gaps", [])[:max_items]:
        recs.append(f"Study/practice '{skill}' to match the JD requirements.")
    if not recs:
        recs.append(
            "Your profile covers the JD skills at a basic level. Focus on portfolio and interview prep."
        )
    return recs

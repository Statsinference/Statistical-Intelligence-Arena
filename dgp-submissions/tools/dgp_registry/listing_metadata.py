"""Source-derived publication labels and DGP property keywords.

These functions change presentation only: no source record, parameter, truth,
PDF, or generator is modified. Missing properties are unknown, not false.
No record IDs, paper titles, or publication years are used to assign tags.
"""
from __future__ import annotations

import re
from typing import Any

# UI aliases, not a lookup of publication status. The source venue must match.
_VENUES = (
    ("JASA", ("Journal of the American Statistical Association", "JASA")),
    ("JRSSB", ("Journal of the Royal Statistical Society Series B",
               "Journal of the Royal Statistical Society: Series B",
               "Journal of the Royal Statistical Society (Series B)",
               "JRSS-B", "JRSS B", "JRSSB")),
    ("AoS", ("The Annals of Statistics", "Annals of Statistics", "AoS")),
    ("Biometrika", ("Biometrika",)),
    ("JoE", ("Journal of Econometrics", "JoE")),
    ("NeurIPS", ("Advances in Neural Information Processing Systems", "NeurIPS", "NIPS")),
    ("ICML", ("International Conference on Machine Learning", "ICML")),
)

# False declarations veto the corresponding positive label, even if a prose
# title or a submitted keyword suggests otherwise. Only actual JSON booleans
# are interpreted as flags: strings such as "false" are never truthy here.
_RULES = (
    ("Interactions", ("interactions", "interaction"),
     ("interaction", "interactions")),
    ("Nonlinearity", ("nonlinear", "nonlinearity"),
     ("nonlinear", "nonlinearity", "non linearity")),
    ("High-dimensionality", ("high_dimensional", "high_dimensionality"),
     ("high dimensional", "high dimensionality", "high dimensional confounding")),
    ("Interference", ("interference", "spillovers", "network_interference"),
     ("interference", "spillovers", "network interference")),
    ("Effect heterogeneity", ("effect_heterogeneity", "treatment_effect_heterogeneity",
                             "heterogeneous_effects", "heterogeneous_treatment_effects", "heterogeneity"),
     ("heterogeneity", "effect heterogeneity", "treatment effect heterogeneity",
      "heterogeneous effects", "heterogeneous treatment effects")),
    ("Heteroskedasticity", ("heteroskedastic", "heteroskedasticity", "heteroscedasticity"),
     ("heteroskedasticity", "heteroscedasticity", "heteroskedastic")),
    ("Panel data", ("panel_data",), ("panel data", "panel")),
    ("Longitudinal", ("longitudinal",), ("longitudinal", "longitudinal data")),
    ("Weak overlap", ("weak_overlap",), ("weak overlap", "limited overlap")),
    ("Heavy-tailed noise", ("heavy_tailed_noise",), ("heavy tailed noise",)),
)
_LABELS = {label for label, _, _ in _RULES} | {"Linearity"}


def _norm(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", value.casefold()).strip()


def venue_abbreviation(record: dict[str, Any]) -> str:
    """Use source venue first; known names in its citation are a fallback."""
    paper = record.get("paper") or {}
    if not isinstance(paper, dict):
        cached = record.get("venue_abbreviation")
        if isinstance(cached, str) and cached.strip():
            return cached.strip()
        paper = {"citation": str(paper)}
    supplied = paper.get("venue")
    citation = str(paper.get("citation") or "")
    for value in (supplied, citation):
        if not isinstance(value, str) or not value.strip():
            continue
        text = " " + _norm(value) + " "
        for label, aliases in _VENUES:
            if any(" " + _norm(alias) + " " in text for alias in aliases):
                return label
        if value == supplied:
            # Keep an unfamiliar supplied venue rather than guessing a journal.
            return value.strip() if len(value) <= 100 and not re.search(r"[\u3400-\u9fff]", value) else ""
    return ""


def _mechanism(record: dict[str, Any]) -> dict[str, Any]:
    result = record.get("mechanism")
    return result if isinstance(result, dict) else {}


def _has_flag(properties: dict[str, Any], keys: tuple[str, ...], value: bool) -> str | None:
    return next((key for key in keys if properties.get(key) is value), None)


def _positive_statement(text: str, pattern: str) -> str | None:
    """Only narrow source declarations, never a bag-of-words science classifier."""
    for sentence in re.split(r"[.;。；\n]", text):
        if re.search(pattern, sentence, re.I) and not re.search(
            r"\b(?:no|not|without|absent|unknown|unspecified|homogeneous|constant)\b|"
            r"无异质|没有异质|非异质|恒定效应|恒定处理效应", sentence, re.I
        ):
            return sentence.strip()
    return None


def keyword_entries(record: dict[str, Any]) -> list[dict[str, Any]]:
    """Return conservative tags and the exact submitted metadata supporting each."""
    mechanism = _mechanism(record)
    if not mechanism:
        # catalog.json is the summary produced from full records below.
        cached = record.get("keyword_evidence")
        return list(cached) if isinstance(cached, list) else []
    props = mechanism.get("properties") or {}
    if not isinstance(props, dict):
        props = {}
    raw_keywords = props.get("keywords") or []
    if not isinstance(raw_keywords, list):
        raw_keywords = []
    supplied = {_norm(word): word for word in raw_keywords if isinstance(word, str)}
    results: dict[str, dict[str, Any]] = {}
    vetoes: set[str] = set()

    def add(label: str, field: str, value: Any, method: str) -> None:
        if label not in vetoes and label not in results:
            results[label] = {"label": label, "source": field,
                              "value": value, "method": method}

    known_aliases = set()
    for label, keys, aliases in _RULES:
        known_aliases.update(aliases)
        negative = _has_flag(props, keys, False)
        if negative is not None:
            vetoes.add(label)
            continue
        positive = _has_flag(props, keys, True)
        if positive is not None:
            add(label, "mechanism.properties." + positive, True, "explicit_boolean")
        else:
            explicit = next((supplied[a] for a in aliases if a in supplied), None)
            if explicit:
                add(label, "mechanism.properties.keywords", explicit, "submitted_keyword")

    # A lack of declared nonlinearity does not establish a linear model.
    # Only publish a linearity tag when the source explicitly supplies one.
    linear_positive = _has_flag(props, ("linear", "linearity"), True)
    linear_negative = _has_flag(props, ("linear", "linearity"), False)
    nonlinear_positive = _has_flag(props, ("nonlinear", "nonlinearity"), True)
    linear_keyword = next((supplied[a] for a in ("linear", "linearity") if a in supplied), None)
    if not linear_negative and not nonlinear_positive:
        if linear_positive:
            add("Linearity", "mechanism.properties." + linear_positive, True, "explicit_boolean")
        elif linear_keyword:
            add("Linearity", "mechanism.properties.keywords", linear_keyword, "submitted_keyword")

    # Effect heterogeneity is not inferred from CATE/ATE/IV labels, the paper's
    # title, interaction flags, or the number of scenarios. Accept only explicit
    # claims about this mechanism in its own name/notes.
    effect_claim = (
        r"heterogeneous\s+(?:treatment\s+)?effects?|"
        r"(?:treatment[- ]?)?effect\s+heterogeneity|effect\s+modification|"
        r"modify\s+(?:the\s+)?treatment\s+effects?|"
        r"异质效应|效应异质性|效应修饰"
    )
    for field, text in (
        ("mechanism.name", mechanism.get("name")),
        ("mechanism.title_en", mechanism.get("title_en")),
        ("mechanism.properties.notes", props.get("notes")),
    ):
        if isinstance(text, str):
            evidence = _positive_statement(text, effect_claim)
            if evidence:
                add("Effect heterogeneity", field, evidence, "explicit_source_description")

    notes = props.get("notes")
    if isinstance(notes, str):
        evidence = _positive_statement(
            notes, r"(?:has|with|exhibits)\s+heteros[ck]edasticity|异方差"
        )
        if evidence:
            add("Heteroskedasticity", "mechanism.properties.notes", evidence,
                "explicit_source_description")

    sampling = mechanism.get("sampling")
    if isinstance(sampling, dict):
        unit = sampling.get("unit")
        if isinstance(unit, str) and re.search(r"\bpanel\b", unit, re.I):
            add("Panel data", "mechanism.sampling.unit", unit, "explicit_source_description")

    # Other English keywords can be explicitly submitted without changing code.
    # Raw markup, negations and known-label contradictions are not published.
    for word in raw_keywords:
        if not isinstance(word, str):
            continue
        key = _norm(word)
        if key in known_aliases or key in {_norm(x) for x in _LABELS}:
            continue
        if re.fullmatch(r"[A-Za-z][A-Za-z0-9 -]{1,47}", word) and not re.match(
            r"^(?:no|not|without)\b", word, re.I
        ):
            add(word, "mechanism.properties.keywords", word, "submitted_keyword")
    order = [label for label, _, _ in _RULES]
    if "Linearity" in results:
        order.insert(1, "Linearity")
    return [results[k] for k in order if k in results] + [
        results[k] for k in sorted(results) if k not in order
    ]


def keywords(record: dict[str, Any]) -> list[str]:
    return [entry["label"] for entry in keyword_entries(record)]


def keywords_text(record: dict[str, Any]) -> str:
    return " · ".join(keywords(record)) or "Not specified"

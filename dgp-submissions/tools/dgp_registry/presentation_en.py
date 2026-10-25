"""English-only presentation of DGP details, without altering original scientific data.

Curated translations for previously submitted documents are stored separately
from the parser and from submitted ZIPs. New ZIPs can supply an optional
English display view. We do not machine-translate mathematical statements.
"""
from __future__ import annotations

import copy
import json
import re
from pathlib import Path

_CJK = re.compile(r"[\u3400-\u9fff]")
_CURATED = json.loads(Path(__file__).with_name("english_details.json").read_text(encoding="utf-8"))
_PENDING = "English description not yet supplied; consult the original scientific record (JSON)."


def has_cjk(value):
    return bool(_CJK.search(str(value or "")))


def _english_text(value):
    if value is None:
        return value
    if isinstance(value, str):
        return _PENDING if has_cjk(value) else value
    return value


def english_display(record):
    """Return (English display record, content-transcribed flag).

    Read-only: never mutates source record, truth values or original equations.
    English description fields are optional; unsupported source-language text
    gets an explicit English placeholder with a link to the raw record.
    """
    view = copy.deepcopy(record)
    override = dict(_CURATED.get(str(record.get("record_id") or ""), {}))
    user_supplied = record.get("english_display")
    if isinstance(user_supplied, dict):
        override.update({key: value for key, value in user_supplied.items() if value is not None})
    paper = view.get("paper") or {}
    mechanism = view.get("mechanism") or {}
    estimand = view.get("estimand") or {}
    translated = False

    old_locator = paper.get("source_locator")
    if "locator" in override:
        paper["source_locator"] = _english_text(override["locator"])
        translated = True
    elif has_cjk(old_locator):
        paper["source_locator"] = _PENDING
        translated = True

    originals = mechanism.get("generation_equations") or []
    new_equations = override.get("equations")
    if isinstance(new_equations, list) and new_equations:
        # For existing reviewed English display data, require source coverage;
        # do not replace 6 source statements with one short English summary.
        if len(new_equations) != len(originals):
            raise ValueError(
                f"English equation transcription count mismatch: {record.get('record_id')}"
            )
        mechanism["generation_equations"] = [
            item if not has_cjk(str(item)) else "English equation transcription pending; see JSON."
            for item in new_equations
        ]
        translated = True
    else:
        source_equations = []
        for eq in originals:
            content = eq.get("expression") if isinstance(eq, dict) else str(eq)
            if has_cjk(content):
                source_equations.append(
                    "English equation transcription pending; see the original record (JSON)."
                )
                translated = True
            else:
                source_equations.append(eq)
        mechanism["generation_equations"] = source_equations

    assumptions = mechanism.get("assumptions") or []
    if isinstance(override.get("assumptions"), list):
        mechanism["assumptions"] = [_english_text(s) for s in override["assumptions"]]
        translated = True
    else:
        replacement = [_english_text(s) for s in assumptions]
        if replacement != assumptions:
            translated = True
        mechanism["assumptions"] = replacement

    if "estimand" in override:
        estimand["definition"] = _english_text(override["estimand"])
        translated = True
    elif has_cjk(estimand.get("definition")):
        estimand["definition"] = _PENDING
        translated = True

    for scenario in view.get("scenarios") or []:
        local = scenario.get("estimand")
        if isinstance(local, dict) and has_cjk(local.get("definition")):
            local["definition"] = estimand.get("definition") or _PENDING
            translated = True
        truth = scenario.get("truth")
        if isinstance(truth, dict) and has_cjk(truth.get("expression")):
            truth["expression"] = estimand.get("definition") or _PENDING
            translated = True

    if has_cjk(paper.get("citation")):
        paper["citation"] = "Reference citation in original-language record (JSON)."
        translated = True
    if isinstance(mechanism.get("sampling"), dict):
        mechanism["sampling"] = {
            key: _english_text(val) for key, val in mechanism["sampling"].items()
        }
    elif has_cjk(mechanism.get("sampling")):
        mechanism["sampling"] = _PENDING
        translated = True

    # Leave original data in registry/drafts/{record_id}.json without changes.
    return view, translated


def sampling_display(value):
    if isinstance(value, dict):
        return "; ".join(
            str(key).replace("_", " ").title() + ": " + str(val)
            for key, val in value.items()
        )
    return str(value or "Not specified")

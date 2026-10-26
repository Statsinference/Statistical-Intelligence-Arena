"""Paper titles and source-generator links for GitHub-native DGP tables.

Group each paper once within each domain. Prefer the original structured
paper title; legacy citations are parsed conservatively, never invented.
Generator source links refer only to actual files exported from the ZIP.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

from .domains import DOMAINS
from .title_display import display_title
from .listing_metadata import venue_abbreviation, keywords_text

BEGIN = "<!-- STATSARENA_PAPER_LIST_BEGIN -->"
END = "<!-- STATSARENA_PAPER_LIST_END -->"
_DOI = re.compile(r"\b10\.\d{4,9}/[-._;()/:A-Za-z0-9]+")
_YEAR = re.compile(r"\((?:19|20)\d{2}[a-z]?\)\.\s*(.+)$", re.I)
_SAFE_GENERATOR = re.compile(r"^generators/[a-z0-9][a-z0-9-]{1,127}\.py$")


def _escape(value):
    return (str(value or "—").replace("&", "&amp;").replace("<", "&lt;")
            .replace(">", "&gt;").replace("|", r"\|").replace("\n", " "))


def _paper(rec):
    paper = rec.get("paper") or {}
    if isinstance(paper, dict):
        citation = paper.get("citation") or paper.get("doi") or "Reference pending"
        doi = paper.get("doi") or ""
    else:
        citation = str(paper) if paper else "Reference pending"
        doi = ""
    match = _DOI.search(doi) or _DOI.search(citation)
    doi = match.group().rstrip(".,;)").lower() if match else None
    normalized = re.sub(r"\s+", " ", citation.strip()).casefold()
    key = ("doi:" + doi) if doi else ("citation:" + normalized)
    return key, citation, doi


def paper_title(rec):
    """Paper title only; never display a full author/venue citation as a title."""
    paper = rec.get("paper") or {}
    if isinstance(paper, dict):
        explicit = paper.get("title") or paper.get("paper_title")
    else:
        explicit = rec.get("paper_title")
    if isinstance(explicit, str) and explicit.strip():
        return explicit.strip().rstrip(".")

    _, citation, _ = _paper(rec)
    match = _YEAR.search(citation)
    if match:
        # Standard citations: Author (YEAR). Title. Journal.
        # Only parse the first sentence, leaving citations untouched in JSON.
        title = re.split(r"\.\s+(?=[A-Z])", match.group(1), maxsplit=1)[0]
        if title:
            return title.strip().rstrip(".")

    # Some submitted citations only contain a title and a trailing year.
    title_only = re.fullmatch(r"(.+?)\s+\((?:19|20)\d{2}\)\.?", citation)
    if title_only:
        return title_only.group(1).strip().rstrip(".")
    return "Title not supplied (review needed)"


def paper_title_with_venue(rec):
    title = paper_title(rec)
    venue = venue_abbreviation(rec)
    return title + (" (" + venue + ")" if venue else "")


def _title(rec):
    mechanism = rec.get("mechanism")
    if isinstance(mechanism, dict):
        return display_title(rec)
    return str(mechanism or rec["record_id"])


def generator_file(rec):
    """Return a relative, verified export path (not a ZIP member path)."""
    impl = rec.get("implementation") or {}
    candidate = impl.get("exported_generator_path") or rec.get("generator_file")
    if isinstance(candidate, str) and _SAFE_GENERATOR.fullmatch(candidate):
        return candidate
    return None


def generator_link(rec, prefix="generators/", label="generator.py"):
    candidate = generator_file(rec)
    if not candidate:
        return "—"
    return "[" + _escape(label) + "](" + prefix + candidate[len("generators/"):] + ")"


def _domain_papers(records):
    result = {}
    for rec in records:
        key, citation, doi = _paper(rec)
        group = result.setdefault(
            key, {"citation": citation, "doi": doi, "title": paper_title(rec),
                  "venue": venue_abbreviation(rec), "mechanisms": []}
        )
        # Explicit titles take precedence over fallback placeholder.
        title = paper_title(rec)
        if group["title"].startswith("Title not supplied") and not title.startswith("Title not supplied"):
            group["title"] = title
        if not group["venue"]:
            group["venue"] = venue_abbreviation(rec)
        group["mechanisms"].append(rec)
    return [result[key] for key in sorted(result, key=lambda x: result[x]["title"].casefold())]


def paper_list_tables(records, *, draft_prefix="drafts/", domain_prefix="by-domain/",
                      generator_prefix="generators/"):
    """One paper per row in each area, with a source generator per mechanism."""
    lines = [
        "## Paper list by research area", "",
        "Each paper is listed **once per area**. Generators are source files from the"
        " submitted ZIP, not executed or automatically validated.", "",
        "**Keywords** describe each submitted DGP, not the whole paper. Missing tags do not "
        "prove absence; nonlinearity may occur in any part of the mechanism. Numbered entries "
        "match the DGP mechanisms and generators in the same row.", "",
    ]
    for domain, label in list(DOMAINS.items()) + [("unclassified", "Needs classification")]:
        group = [rec for rec in records if rec.get("domain") == domain]
        if domain == "unclassified" and not group:
            continue
        papers = _domain_papers(group)
        lines.extend([
            "### [" + _escape(label) + "](" + domain_prefix + domain + ".md)", "",
            str(len(papers)) + " paper(s) · " + str(len(group)) + " DGP mechanism(s)", "",
            "| Paper Title | DGPs | DGP Mechanisms | Keywords | Generator.py |",
            "|---|---:|---|---|---|",
        ])
        if not papers:
            lines.append("| — | 0 | No submissions yet | — | — |")
        for paper in papers:
            title = _escape(paper["title"])
            if paper["doi"]:
                title = "[" + title + "](https://doi.org/" + paper["doi"] + ")"
            if paper["venue"]:
                title += " (" + _escape(paper["venue"]) + ")"
            mechanisms = sorted(
                paper["mechanisms"], key=lambda r: (_title(r).casefold(), r["record_id"])
            )
            n = len(mechanisms)
            links = "<br/>".join(
                (str(i + 1) + ": " if n > 1 else "") +
                "[" + _escape(_title(rec)) + "](" + draft_prefix +
                rec["record_id"] + ".md)" for i, rec in enumerate(mechanisms)
            )
            keyword_cells = "<br/>".join(
                (str(i + 1) + ": " if n > 1 else "") + _escape(keywords_text(rec))
                for i, rec in enumerate(mechanisms)
            )
            generators = "<br/>".join(
                generator_link(
                    rec, generator_prefix,
                    ("generator.py" if n == 1 else str(i + 1) + ": generator.py")
                )
                for i, rec in enumerate(mechanisms)
            )
            lines.append(
                "| " + title + " | " + str(n) + " | " + links + " | " + keyword_cells + " | " + generators + " |"
            )
        lines.append("")
    return lines


def update_readme(readme_path, catalog_path):
    path, catalog = Path(readme_path), Path(catalog_path)
    original = path.read_text(encoding="utf-8")
    if original.count(BEGIN) != 1 or original.count(END) != 1:
        raise ValueError("README must have exactly one BEGIN and END paper-list marker")
    if original.index(BEGIN) > original.index(END):
        raise ValueError("README paper-list markers are reversed")
    records = json.loads(catalog.read_text(encoding="utf-8"))["records"]
    tables = "\n".join(paper_list_tables(
        records, draft_prefix="registry/drafts/", domain_prefix="registry/by-domain/",
        generator_prefix="registry/generators/"
    )).rstrip()
    before, tail = original.split(BEGIN, 1)
    _, after = tail.split(END, 1)
    updated = before + BEGIN + "\n\n" + tables + "\n\n" + END + after
    if updated != original:
        path.write_text(updated, encoding="utf-8")
    return len(records)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--readme", type=Path, default=Path("README.md"))
    parser.add_argument("--catalog", type=Path, default=Path("registry/catalog.json"))
    args = parser.parse_args()
    count = update_readme(args.readme, args.catalog)
    print("Updated README paper titles and generator links from " + str(count) + " DGPs.")


if __name__ == "__main__":
    main()

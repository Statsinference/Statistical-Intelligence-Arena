#!/usr/bin/env python3
"""Read-only consistency and disclosure checks for the documentation repository.

This does not execute training, evaluate statistical validity, contact services,
or regenerate PDFs. It requires only the Python standard library.
"""

import json
import re
import sys
import zipfile
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
FAMILIES = {"ate", "cate", "mediation", "iv", "proximal", "did_sc"}
VIEWS = {"overview", "contribute", "evaluation", "arena"}
DOCUMENTS = {
    "contribution_en.md": "CausalTaskBench_Contribution_Requirements_EN.md",
    "contribution_zh.md": "CausalTaskBench_Contribution_Requirements_ZH.md",
    "contribution_en_zh.md": "CausalTaskBench_Contribution_Requirements_EN_ZH.md",
    "student_guide_en.md": "Student_Contribution_Walkthrough_EN.md",
    "student_guide_zh.md": "Student_Contribution_Walkthrough_ZH.md",
}
PDFS = {
    "contribution_en.pdf": "Statistical_Inference_Arena_Contribution_EN.pdf",
    "contribution_zh.pdf": "Statistical_Inference_Arena_贡献规范_中文版.pdf",
    "contribution_en_zh.pdf": "CausalTaskBench_Contribution_Guide_EN_ZH.pdf",
}
DOWNLOADS = ROOT / "site" / "downloads"
ERRORS = []
COUNTS = Counter()


def check(condition, message):
    COUNTS["checks"] += 1
    if not condition:
        ERRORS.append(message)


def relative(path):
    return path.relative_to(ROOT).as_posix()


def read(path):
    if not path.is_file():
        check(False, "Missing file: " + relative(path))
        return ""
    try:
        return path.read_text(encoding="utf-8-sig")
    except (OSError, UnicodeError):
        check(False, "Cannot read UTF-8 file: " + relative(path))
        return ""


def compare_files(source, destination, transform=None):
    if not source.is_file() or not destination.is_file():
        check(False, "Missing canonical/download pair: " + relative(destination))
        return
    expected = source.read_bytes()
    if transform:
        expected = transform(expected)
    check(expected == destination.read_bytes(),
          "Download differs from source: " + relative(destination))


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = []
        self.links = []
        self.families = set()
        self.views = set()
        self.panels = set()

    def handle_starttag(self, tag, attrs):
        attr = dict(attrs)
        if "id" in attr:
            self.ids.append(attr["id"])
        for key in ("href", "src"):
            if attr.get(key):
                self.links.append(attr[key])
        if tag == "button" and attr.get("data-family"):
            self.families.add(attr["data-family"])
        if attr.get("data-view"):
            self.views.add(attr["data-view"])
        if attr.get("role") == "tabpanel" and "view-panel" in attr.get("class", "").split():
            self.panels.add(attr.get("id"))


def local_link(source, target, ids=None):
    parsed = urlsplit(target)
    if parsed.scheme or parsed.netloc:
        return
    path_text = unquote(parsed.path)
    if not path_text:
        if ids is not None and parsed.fragment:
            valid = parsed.fragment in ids or parsed.fragment in VIEWS
            check(valid, "Broken site fragment: " + target)
        return
    base = ROOT if path_text.startswith("/") else source.parent
    resolved = (base / path_text.lstrip("/")).resolve()
    try:
        resolved.relative_to(ROOT)
    except ValueError:
        check(False, "Local link escapes repository in " + relative(source))
        return
    check(resolved.exists(), "Broken local link in " + relative(source) + ": " + target)
    if resolved == source.resolve() and parsed.fragment and ids is not None:
        check(parsed.fragment in ids or parsed.fragment in VIEWS,
              "Broken site fragment: " + target)


def check_site():
    source = ROOT / "site" / "index.html"
    html = read(source)
    page = Page()
    page.feed(html)
    duplicate_ids = [name for name, count in Counter(page.ids).items() if count > 1]
    check(not duplicate_ids, "Duplicate site element IDs: " + ", ".join(duplicate_ids))
    check(page.views == VIEWS, "Site must expose exactly four navigation views")
    check(page.panels == {"view-" + name for name in VIEWS},
          "Site must expose exactly four view panels")
    check(page.families == FAMILIES, "Site must expose exactly the six initial families")
    for target in page.links:
        local_link(source, target, set(page.ids))
    check("v0.3" in html and "0.2.0" in html,
          "Site protocol/schema labels must remain v0.3 / 0.2.0")
    check("Template only" in html and "No benchmark runs yet" in html,
          "Arena template status must be explicit")
    script = read(ROOT / "site" / "app.js")
    family_block = script.partition("const familyButtons")[0]
    script_families = set(re.findall(r"^\s{2}([a-z_]+):\s*\{", family_block, re.M))
    check(script_families == FAMILIES, "Site family definitions do not match the six-family scope")
    COUNTS["site_resources"] = len(page.links)


def check_documents():
    paths = [ROOT / "README.md", ROOT / "CONTRIBUTING.md"]
    paths.extend(sorted((ROOT / "docs").glob("*.md")))
    link_pattern = re.compile(r"!?\[[^\]]*\]\((<[^>]+>|[^\s)]+)(?:\s+[\"'][^)]*)?\)")
    for source in paths:
        text = read(source)
        without_fences = re.sub(r"```.*?```", "", text, flags=re.S)
        for match in link_pattern.finditer(without_fences):
            local_link(source, match.group(1).strip("<>"))
        if source.name in DOCUMENTS:
            check("0.3" in text and "0.2.0" in text,
                  "Protocol/schema labels missing in " + relative(source))
    for name, download_name in DOCUMENTS.items():
        # Downloaded walkthroughs link to the portable legacy-named protocols.
        def download_links(payload):
            if name.startswith("student_guide_"):
                for short, legacy in DOCUMENTS.items():
                    payload = payload.replace(("(" + short + ")").encode("utf-8"),
                                              ("(" + legacy + ")").encode("utf-8"))
            return payload
        compare_files(ROOT / "docs" / name, DOWNLOADS / download_name, download_links)
    for name, download_name in PDFS.items():
        source = ROOT / "docs" / "pdf" / name
        compare_files(source, DOWNLOADS / download_name)
        if source.is_file():
            check(source.read_bytes().startswith(b"%PDF-"), "Invalid PDF header: " + relative(source))
    compare_files(ROOT / "starter" / "CONTRIBUTING.md", DOWNLOADS / "CONTRIBUTING.md")
    COUNTS["canonical_documents"] = len(DOCUMENTS)
    COUNTS["pdf_pairs"] = len(PDFS)


def starter_files():
    result = {}
    for path in (ROOT / "starter").rglob("*"):
        if path.is_file() and "__pycache__" not in path.parts and path.suffix not in {".pyc", ".pyo"}:
            result[path.relative_to(ROOT / "starter").as_posix()] = path
    return result


def check_archive():
    archive = DOWNLOADS / "causaltaskbench-starter.zip"
    if not archive.is_file():
        check(False, "Missing starter download archive")
        return
    expected = starter_files()
    try:
        with zipfile.ZipFile(archive) as zipped:
            members = [info.filename for info in zipped.infolist() if not info.is_dir()]
            check(len(members) == len(set(members)), "Starter ZIP contains duplicate members")
            actual = set(members)
            prefix = ""
            if actual != set(expected) and members:
                roots = {member.split("/", 1)[0] for member in members}
                if len(roots) == 1 and all("/" in member for member in members):
                    prefix = next(iter(roots)) + "/"
            normalized = {member[len(prefix):] for member in members}
            check(normalized == set(expected), "Starter ZIP file set differs from starter/ or contains caches")
            for member in members:
                name = member[len(prefix):]
                if name in expected:
                    check(zipped.read(member) == expected[name].read_bytes(),
                          "Starter ZIP member differs from source: " + name)
            COUNTS["starter_zip_files"] = len(members)
    except (OSError, zipfile.BadZipFile):
        check(False, "Cannot read starter ZIP")


def check_version():
    try:
        version = json.loads(read(ROOT / "VERSION.json"))
    except json.JSONDecodeError:
        check(False, "VERSION.json is not valid JSON")
        return
    check(version.get("protocol_version") == "0.3", "Unexpected protocol version")
    check(version.get("output_schema_version") == "0.2.0", "Unexpected output schema version")
    check(set(version.get("families", [])) == FAMILIES, "VERSION.json scope differs from website")
    check(version.get("training_started") is False, "This release must not claim training has started")
    check(version.get("reference_demo") == "planned_not_implemented", "Unexpected demo implementation status")
    check(version.get("arena") == "template_no_empirical_results", "Unexpected Arena results status")
    text = read(ROOT / "starter" / "README.md")
    check("v0.3" in text and "0.2.0" in text, "Starter protocol/schema labels are not synchronized")


def check_disclosures():
    extensions = {".md", ".py", ".yaml", ".yml", ".json", ".csv", ".html", ".js", ".css"}
    # Inspect concrete credential shapes; generic prose such as "token" is valid.
    patterns = {
        "absolute local path": re.compile(r"(?i)(?:\b[A-Z]:[\\/]|file:///|/mnt/(?:data|c)/|/Users/|/home/[^\s/]+/|\\\\[^\s\\]+\\(?:Users|home)\\)"),
        "GitHub token": re.compile(r"\b(?:gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{30,})\b"),
        "API secret": re.compile(r"\bsk-(?:proj-)?[A-Za-z0-9_-]{20,}\b"),
        "AWS access key": re.compile(r"\b(?:AKIA|ASIA)[A-Z0-9]{16}\b"),
        "private key": re.compile(r"-----BEGIN (?:[A-Z]+ )?PRIVATE KEY-----"),
        "credential-bearing URL": re.compile(r"https?://[^\s/:@]+:[^\s/@]{4,}@"),
        "concrete assigned secret": re.compile(r"(?i)(?:api[_-]?key|access[_-]?token|password|client[_-]?secret)\s*[:=]\s*[\"']([^\"'\s]{16,})[\"']"),
    }
    this_file = Path(__file__).resolve()
    for source in ROOT.rglob("*"):
        if not source.is_file() or source.suffix.lower() not in extensions:
            continue
        if {".git", "__pycache__", "node_modules"}.intersection(source.relative_to(ROOT).parts):
            continue
        # These regex definitions deliberately contain the shapes being checked.
        if source.resolve() == this_file:
            continue
        text = read(source)
        COUNTS["disclosure_scanned_files"] += 1
        for label, pattern in patterns.items():
            if pattern.search(text):
                # Report only the filename and category; never echo a possible secret.
                check(False, "Potential " + label + " in " + relative(source))


def main():
    check_version()
    check_site()
    check_documents()
    check_archive()
    check_disclosures()
    if ERRORS:
        print("Repository checks FAILED:")
        for error in ERRORS:
            print("- " + error)
        return 1
    print("Repository checks passed: " + ", ".join(str(count) + " " + name.replace("_", " ")
                                                for name, count in COUNTS.items()))
    print("Structural consistency only; no training, statistical evaluation or external service was run.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

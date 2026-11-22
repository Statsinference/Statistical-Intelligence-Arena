"""Validate contribution Markdown treated solely as data."""

import argparse
import base64
import json
import os
import re
import sys
from pathlib import Path
from urllib.error import URLError
from urllib.request import HTTPRedirectHandler, Request, build_opener


MAX_MARKDOWN_BYTES = 32_768
MAX_API_BYTES = 16 * 1024 * 1024
MAX_PR_BODY_LENGTH = 65_536
TRACK_SECTIONS = {
    "simulated-dgp": ("Variables and data-generating process", "Data-generating process and estimand"),
    "real-data": ("Target estimand and reference estimate",),
}
SUBMISSION_PATH = re.compile(
    r"data-submissions/(simulated-dgp|real-data)/submissions/"
    r"[a-z0-9]+(?:-[a-z0-9]+)*\.md\Z"
)
REPOSITORY = re.compile(r"[a-zA-Z0-9-]+/[a-zA-Z0-9_.-]+\Z")
SHA = re.compile(r"[0-9a-f]{40}\Z")
PLACEHOLDER = re.compile(r"\[\s*(?:todo|tbd|replace)\b", re.I)
DAG_SECTION = "DAG and identification"
VARIABLES_SECTION = "Variables and data-generating process"
HEADING = re.compile(r" {0,3}(#{1,6})[ \t]+(.+?)\s*$")
FENCE = re.compile(r" {0,3}(`{3,}|~{3,})(.*)")
EDGE_FIELD = re.compile(r" {0,3}-[ \t]+\*\*(DAG edges|Structural parents)\.\*\*(.*)")
NODE = r"[A-Za-z][A-Za-z0-9_]*"
DIRECTED_EDGE = re.compile(rf"({NODE})\s*->\s*({NODE})")
MERMAID_NODE = rf'({NODE})(?:\["([^"\[\]<>`]+)"\])?'
MERMAID_LINE = re.compile(rf"{MERMAID_NODE}(?:[ \t]*-->[ \t]*{MERMAID_NODE})?")
BLOCK_EDGE = re.compile(rf"({NODE})[ \t]+-->[ \t]+({NODE})")
BLOCK_ITEM = r'(?:space(?::([1-3]))?|(' + NODE + r')\("([^"\[\]<>]+)"\))'
BLOCK_ROW = re.compile(rf"{BLOCK_ITEM}(?:[ \t]+{BLOCK_ITEM})*")
BLOCK_CELL = re.compile(BLOCK_ITEM)
CASE_NOTATION = re.compile(r"\*\*Case file notation\.\*\*[ \t]+(.+)")
MATH_TOKEN = re.compile(rf"\\[A-Za-z]+|{NODE}")
NOISE_ID = re.compile(r"epsilon(?:_.*)?$", re.I)
PREVIEW_SECTION = "Causal design preview"


class ValidationError(ValueError):
    """A submission could not be verified."""


class NoRedirects(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, new_url):
        return None


def required_sections(track):
    return (
        "Research question",
        "Study design and data source",
        DAG_SECTION,
        *TRACK_SECTIONS[track],
        "Benchmark comparison",
        "Materials and access",
    )


def parse_declared_edges(value, field):
    inline = re.fullmatch(r"`([^`]+)`", value.strip())
    if not inline:
        raise ValidationError(f"Write {field} as one inline code span containing comma-separated "
                              "arrows such as `X -> Y`, or `none`.")
    contents = inline.group(1).strip()
    edges = set()
    if contents == "none":
        return edges
    for arrow in contents.split(","):
        match = DIRECTED_EDGE.fullmatch(arrow.strip())
        if not match:
            raise ValidationError(f"Invalid arrow in {field}. Use `X -> Y` with node IDs starting "
                                  "with a letter and containing only ASCII letters, digits, or underscores.")
        parent, child = edge = match.groups()
        if parent == child:
            raise ValidationError(f"{field} contains a self-arrow `{parent} -> {child}`.")
        if edge in edges:
            raise ValidationError(f"{field} repeats `{parent} -> {child}`.")
        edges.add(edge)
    return edges


def validate_simulated_structure(seen_structure, populated_structure, declarations):
    if not seen_structure:
        raise ValidationError(f"Add a `### Structural equations` subsection under `{VARIABLES_SECTION}`.")
    if not populated_structure:
        raise ValidationError("Fill the Structural equations subsection with its equations or explanation.")
    for field, location in (("DAG edges", DAG_SECTION), ("Structural parents", "Structural equations")):
        if field not in declarations:
            raise ValidationError(f"Add `- **{field}.**` under `{location}`, followed by an inline edge list.")
    dag, parents = declarations["DAG edges"], declarations["Structural parents"]
    if dag != parents:
        missing = []
        for edges, field in ((dag - parents, "Structural parents"), (parents - dag, "DAG edges")):
            if edges:
                arrows = ", ".join(f"{parent} -> {child}" for parent, child in sorted(edges))
                missing.append(f"Missing from {field}: `{arrows}`.")
        raise ValidationError("The declared edge lists must match. " + " ".join(missing))


def markdown_items(lines):
    """Yield visible text lines and fenced Mermaid/math blocks, without rendering."""
    fence = kind = ""
    block = []
    for line in lines:
        marker = FENCE.fullmatch(line)
        if fence == "$$":
            if line.rstrip().endswith("$$"):
                block.append(line.rstrip()[:-2])
                yield "math", "\n".join(block)
                fence = ""
            else:
                block.append(line)
        elif fence:
            if marker and marker[1].startswith(fence) and not marker[2].strip():
                yield kind, "\n".join(block)
                fence = ""
            else:
                block.append(line)
        elif marker:
            fence, kind = marker[1], marker[2].strip()
            kind = kind if kind in ("math", "mermaid") else "code"
            block = []
        elif re.match(r" {0,3}\$\$", line):
            content = line.strip()[2:]
            if content.endswith("$$"):
                yield "math", content[:-2]
            else:
                fence, block = "$$", [content]
        else:
            yield "text", line
    if fence:
        raise ValidationError("Close the Markdown diagram and Structural equations blocks with matching delimiters.")


def check_dag_node(node, label):
    if NOISE_ID.fullmatch(node) or (label and label.lower().endswith("(noise)")):
        raise ValidationError("Keep noise terms in Structural equations and omit them from the DAG.")
    if label and not re.fullmatch(rf"{node} \([^()]+\)", label):
        raise ValidationError("Use the same variable ID in each Mermaid DAG label, such as 'X (covariate)'.")


def parse_dag_grid(lines):
    if not lines or lines[0] != "columns 3":
        raise ValidationError("Start the Mermaid DAG grid with 'columns 3'.")
    nodes, edges = set(), set()
    for line in lines[1:]:
        if edge := BLOCK_EDGE.fullmatch(line):
            edges.add(edge.groups())
            continue
        if edges or not BLOCK_ROW.fullmatch(line):
            raise ValidationError("In the Mermaid DAG grid, place each node or spacer before the arrow list.")
        width = 0
        for cell in BLOCK_CELL.finditer(line):
            span, node, label = cell.groups()
            width += int(span or 1)
            if node:
                check_dag_node(node, label)
                if node in nodes:
                    raise ValidationError("Declare each Mermaid DAG node once in the grid.")
                nodes.add(node)
        if width != 3:
            raise ValidationError("Fill three columns in every Mermaid DAG grid row with nodes or spacers.")
    if not nodes or any(parent not in nodes or child not in nodes for parent, child in edges):
        raise ValidationError("Declare at least one Mermaid DAG node and declare both endpoints of every arrow.")
    return edges


def parse_preview_dag(graph):
    lines = [line.strip() for line in graph.splitlines() if line.strip()]
    if lines and lines[0] == "block-beta":
        return parse_dag_grid(lines[1:])
    if not lines or not re.fullmatch(r"(?:flowchart|graph)\s+(?:LR|RL|TD|TB|BT)", lines[0]):
        raise ValidationError("Start the Mermaid DAG with 'block-beta' or a flowchart direction.")
    edges = set()
    has_node = False
    for line in lines[1:]:
        match = MERMAID_LINE.fullmatch(line)
        if not match:
            raise ValidationError("Use one Mermaid DAG edge per line such as `X --> Y`, or a standalone node.")
        parent, parent_label, child, child_label = match.groups()
        check_dag_node(parent, parent_label)
        if child:
            check_dag_node(child, child_label)
        has_node = True
        if child:
            edges.add((parent, child))
    if not has_node:
        raise ValidationError("Include at least one variable in the Mermaid DAG.")
    return edges


def translate_case_notation(edges, equations, aliases):
    """Project existing notation onto the PR's convention without changing the equations."""
    renames = dict(aliases)
    case_symbols = {symbol for edge in edges for symbol in edge}
    case_symbols.update(
        token for equation in equations for token in MATH_TOKEN.findall(equation) if not token.startswith("\\")
    )
    translated = {renames.get(symbol, symbol) for symbol in case_symbols}
    if len(renames) != len(aliases) or not renames.keys() <= case_symbols or len(translated) != len(case_symbols):
        raise ValidationError("Case file notation must map existing symbols one-to-one.")

    graph = {(renames.get(parent, parent), renames.get(child, child)) for parent, child in edges}
    for noise in {parent for parent, _ in graph if NOISE_ID.fullmatch(parent)}:
        if any(child == noise for _, child in graph) or sum(parent == noise for parent, _ in graph) != 1:
            raise ValidationError("Only omit a noise source with a single outgoing edge from the DAG.")
    graph = {(parent, child) for parent, child in graph if not NOISE_ID.fullmatch(parent)}

    def math_replace(match):
        original = match[0]
        renamed = renames.get(original)
        if renamed is None:
            return original
        if NOISE_ID.fullmatch(renamed):
            _, separator, index = renamed.partition("_")
            if "_" in index:
                index = "{" + index + "}"
            return rf"\epsilon{separator}{index}"
        return renamed

    return graph, [MATH_TOKEN.sub(math_replace, equation) for equation in equations]


def validate_pr_preview(body, case_edges, structural_lines):
    if not isinstance(body, str) or len(body) > MAX_PR_BODY_LENGTH:
        raise ValidationError("Use a Markdown PR description that contains the Causal design preview.")
    text = re.sub(r"<!--.*?(?:-->|\Z)", "", body, flags=re.S)
    found = False
    in_preview = False
    section = None
    sections = []
    graphs, formulas = [], []
    aliases = None
    for kind, value in markdown_items(text.splitlines()):
        if kind == "text" and (heading := HEADING.fullmatch(value)):
            level, title = heading.groups()
            title = re.sub(r"\s+#+$", "", title)
            if len(level) <= 2:
                in_preview = level == "##" and title == PREVIEW_SECTION
                section = None
                if in_preview:
                    if found:
                        raise ValidationError("Include one Causal design preview in the PR description.")
                    found = True
            elif in_preview and level == "###":
                section = title
                sections.append(title)
        if in_preview and section is None and kind == "text" and (alias := CASE_NOTATION.fullmatch(value.strip())):
            if aliases is not None:
                raise ValidationError("Declare Case file notation at most once.")
            aliases = parse_declared_edges(alias[1], "Case file notation")
        if in_preview and section == "DAG" and kind == "mermaid":
            graphs.append(value)
        if in_preview and section == "Structural equations" and kind == "math":
            formulas.append(" ".join(value.split()))

    if not found:
        raise ValidationError("Add `## Causal design preview` to the PR description using the Simulated DGP PR template.")
    if sections != ["DAG", "Structural equations"]:
        raise ValidationError("In the Causal design preview, include `### DAG` then `### Structural equations` once each.")
    if len(graphs) != 1:
        raise ValidationError("Include one visible Mermaid block under the PR preview DAG heading.")
    graph_edges = parse_preview_dag(graphs[0])
    expected = [" ".join(value.split()) for kind, value in markdown_items(structural_lines) if kind == "math"]
    if not expected or not all(expected):
        raise ValidationError("Write the Case file Structural equations in nonempty display math blocks.")
    if aliases:
        case_edges, expected = translate_case_notation(case_edges, expected, aliases)
    if graph_edges != case_edges:
        missing = ", ".join(f"{src} -> {dst}" for src, dst in sorted(case_edges - graph_edges))
        extra = ", ".join(f"{src} -> {dst}" for src, dst in sorted(graph_edges - case_edges))
        raise ValidationError("The PR preview DAG must match the Case file DAG. "
                              f"Missing arrows: `{missing or 'none'}`. Extra arrows: `{extra or 'none'}`.")
    if formulas != expected:
        raise ValidationError("Copy every display math block from the Case file Structural equations into the PR preview, "
                              "in the same order and with the same math content.")


def validate_markdown(raw, track, *, pr_body=None):
    if len(raw) > MAX_MARKDOWN_BYTES:
        raise ValidationError("Use a Markdown summary of at most 32 KiB.")
    try:
        text = raw.decode("utf-8-sig")
    except UnicodeDecodeError as exc:
        raise ValidationError("Save the proposal as UTF-8 Markdown.") from exc
    if any(ord(ch) < 32 and ch not in "\t\r\n" for ch in text):
        raise ValidationError("The proposal contains a non-text control character.")

    # Ignore hidden comments and headings inside fenced blocks. Fence contents can
    # still supply section text, such as a Mermaid DAG.
    text = re.sub(r"<!--.*?(?:-->|\Z)", "", text, flags=re.S)
    if PLACEHOLDER.search(text):
        raise ValidationError("Replace every [TODO: ...] placeholder before submitting.")
    lines = text.splitlines()
    first = next((line.strip() for line in lines if line.strip()), "")
    if not re.fullmatch(r"#\s+\S.*", first):
        raise ValidationError("Start the proposal with a Markdown H1 title (# Title).")

    required = required_sections(track)
    populated = dict.fromkeys(required, False)
    seen = []
    current = None
    fence = ""
    title_count = 0
    simulated = track == "simulated-dgp"
    in_structure = seen_structure = populated_structure = False
    structure_start, structure_end = 0, len(lines)
    math_fence = False
    declarations = {}
    for index, line in enumerate(lines):
        marker = FENCE.fullmatch(line)
        if marker:
            run, suffix = marker.groups()
            if not fence:
                fence = run
                math_fence = in_structure and suffix.strip() == "math"
                continue
            if run.startswith(fence) and not suffix.strip():
                fence = ""
                math_fence = False
                continue
        if not fence and not line.startswith(("    ", "\t")):
            heading = HEADING.fullmatch(line)
            if heading:
                level, title = heading.groups()
                title = re.sub(r"\s+#+$", "", title)
                if len(level) <= 2:
                    if in_structure:
                        structure_end = index
                    if level == "#":
                        title_count += 1
                    current = title if level == "##" and title in required else None
                    if current:
                        seen.append(current)
                    in_structure = False
                    continue
                if simulated:
                    if level == "###":
                        if in_structure:
                            structure_end = index
                        in_structure = current == VARIABLES_SECTION and title == "Structural equations"
                        if in_structure:
                            if seen_structure:
                                raise ValidationError("Use the Structural equations subsection once.")
                            seen_structure = True
                            structure_start = index + 1
                    continue
            if simulated:
                declared = EDGE_FIELD.fullmatch(line)
                if declared:
                    field, value = declared.groups()
                    if ((field == "DAG edges" and current == DAG_SECTION)
                            or (field == "Structural parents" and in_structure)):
                        if field in declarations:
                            raise ValidationError(f"Declare {field} exactly once.")
                        declarations[field] = parse_declared_edges(value, field)
                elif in_structure and re.search(r"\w", line):
                    populated_structure = True
        elif math_fence and not (HEADING.fullmatch(line) or EDGE_FIELD.fullmatch(line)) and re.search(r"\w", line):
            populated_structure = True
        if current and re.search(r"\w", line):
            populated[current] = True
    if fence:
        raise ValidationError("Close all fenced Markdown code or diagram blocks.")
    if title_count != 1:
        raise ValidationError("Use exactly one Markdown H1 title.")
    if seen != list(required):
        raise ValidationError("Use each of the required section headings once, in template order. "
                              "Required headings are " + ", ".join(required) + ".")
    empty_sections = [title for title in required if not populated[title]]
    if empty_sections:
        raise ValidationError("Fill the following sections. " + ", ".join(empty_sections) + ".")
    if simulated:
        validate_simulated_structure(seen_structure, populated_structure, declarations)
        if pr_body is not None:
            validate_pr_preview(pr_body, declarations["DAG edges"], lines[structure_start:structure_end])


def in_submission_area(path, path_prefix=""):
    normalized = str(path).replace("\\", "/").lower()
    if not normalized.startswith(path_prefix):
        return False
    parts = normalized.removeprefix(path_prefix).split("/")
    if parts[0] != "data-submissions":
        return False
    if "submissions" in parts[1:]:
        return True
    # Treat a proposal beside the simulated track's guides as a submission so
    # the canonical path check can point the contributor to submissions/.
    return (
        len(parts) == 3
        and parts[1] == "simulated-dgp"
        and parts[2].endswith(".md")
        and parts[2] not in {"readme.md", "template.md", "example.md"}
    )


def check_changes(changes, read_markdown, *, path_prefix="", pr_body=None):
    touched = any(
        in_submission_area(file.get(field, ""), path_prefix)
        for file in changes
        for field in ("filename", "previous_filename")
    )
    if not touched:
        return False
    if len(changes) != 1:
        raise ValidationError("A contribution PR should add or update exactly one proposal Markdown file.")
    file = changes[0]
    filename = file.get("filename", "")
    relative_filename = filename.removeprefix(path_prefix) if filename.startswith(path_prefix) else ""
    match = SUBMISSION_PATH.fullmatch(relative_filename)
    if not match or len(relative_filename) > 180:
        raise ValidationError(f"Use {path_prefix}data-submissions/<track>/submissions/<lowercase-kebab-case>.md.")
    if file.get("status") not in ("added", "modified") or file.get("previous_filename"):
        raise ValidationError("Add or update one proposal in place.")
    validate_markdown(read_markdown(file), match.group(1), pr_body=pr_body)
    return True


def get_api(token):
    opener = build_opener(NoRedirects())

    def get(path):
        headers = {"Accept": "application/vnd.github+json", "User-Agent": "StatArena-data-check"}
        if token:
            headers["Authorization"] = f"Bearer {token}"
        request = Request(f"https://api.github.com/{path}", headers=headers)
        with opener.open(request, timeout=15) as response:
            data = response.read(MAX_API_BYTES + 1)
        if len(data) > MAX_API_BYTES:
            raise ValidationError("Could not inspect the full GitHub API response.")
        return json.loads(data)

    return get


def repository_name(value):
    if not isinstance(value, str) or not REPOSITORY.fullmatch(value) or value.split("/")[1] in (".", ".."):
        raise ValidationError("Could not verify the pull request repository.")
    return value


def object_sha(value):
    if not isinstance(value, str) or not SHA.fullmatch(value):
        raise ValidationError("Could not verify the immutable Git object ID.")
    return value


def read_git_markdown(api, repository, head_sha, file):
    # Walk the immutable tree so a symlink or executable cannot masquerade as a
    # Markdown blob. Paths are never passed to a shell or checked out.
    commit = api(f"repos/{repository}/git/commits/{head_sha}")
    tree_sha = object_sha(commit["tree"]["sha"])
    parts = file["filename"].split("/")
    for index, part in enumerate(parts):
        tree = api(f"repos/{repository}/git/trees/{tree_sha}")
        if tree.get("truncated"):
            raise ValidationError("Could not inspect the full Git tree.")
        entry = next((item for item in tree["tree"] if item["path"] == part), None)
        last = index == len(parts) - 1
        expected = ("blob", "100644") if last else ("tree", "040000")
        if entry is None or (entry.get("type"), entry.get("mode")) != expected:
            raise ValidationError("The proposal must be a regular Markdown file.")
        tree_sha = object_sha(entry["sha"])

    if tree_sha != object_sha(file["sha"]):
        raise ValidationError("The proposal changed during this check. Check the latest run.")
    if entry.get("size", MAX_MARKDOWN_BYTES + 1) > MAX_MARKDOWN_BYTES:
        raise ValidationError("Use a Markdown summary of at most 32 KiB.")
    blob = api(f"repos/{repository}/git/blobs/{tree_sha}")
    if blob.get("encoding") != "base64" or blob.get("sha") != tree_sha:
        raise ValidationError("Could not verify the proposal contents.")
    try:
        return base64.b64decode(re.sub(r"\s+", "", blob["content"]), validate=True)
    except ValueError as exc:
        raise ValidationError("Could not decode the proposal contents.") from exc


def check_pull_request(event, api, *, path_prefix="", require_preview=False):
    repository = repository_name(event["repository"]["full_name"])
    number = event["number"]
    if type(number) is not int or number <= 0:
        raise ValidationError("Could not verify the pull request number.")
    head = event["pull_request"]["head"]
    head_sha = object_sha(head["sha"])
    endpoint = f"repos/{repository}/pulls/{number}"
    current = api(endpoint)
    if current["head"]["sha"] != head_sha:
        raise ValidationError("A newer revision superseded this check. Check the latest run.")
    changed_count = current["changed_files"]
    if type(changed_count) is not int or not 0 <= changed_count <= 3000:
        raise ValidationError("Could not inspect every changed file in the pull request.")
    changes = []
    for page in range(1, (changed_count + 99) // 100 + 1):
        response = api(f"{endpoint}/files?per_page=100&page={page}")
        changes.extend(response)
    latest = api(endpoint)
    if len(changes) != changed_count or latest["head"]["sha"] != head_sha:
        raise ValidationError("The list of changed files changed during this check. Check the latest run.")
    # PR head objects from external forks are addressable through the destination
    # repository, keeping API calls within the job token's repository scope.
    return check_changes(
        changes, lambda file: read_git_markdown(api, repository, head_sha, file), path_prefix=path_prefix,
        pr_body=(latest.get("body") or "") if require_preview else None,
    )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--local-file", type=Path, help="Check a local proposal against its track template")
    parser.add_argument("--pr-body-file", type=Path, help="Also check a local simulated DGP PR description")
    parser.add_argument("--require-pr-preview", action="store_true", help="Require the preview in simulated DGP PRs")
    parser.add_argument("--track", choices=tuple(TRACK_SECTIONS))
    parser.add_argument("--path-prefix", choices=("website/",), default="",
                        help="Check proposal paths under website/ in the research repository.")
    args = parser.parse_args()
    try:
        if args.local_file:
            if not args.track:
                parser.error("--local-file requires --track")
            with args.local_file.open("rb") as stream:
                if args.pr_body_file:
                    with args.pr_body_file.open(encoding="utf-8-sig") as body_file:
                        body = body_file.read(MAX_PR_BODY_LENGTH + 1)
                else:
                    body = None
                validate_markdown(stream.read(MAX_MARKDOWN_BYTES + 1), args.track, pr_body=body)
            checked = True
        else:
            if args.pr_body_file:
                parser.error("--pr-body-file requires --local-file")
            event = json.loads(Path(os.environ["GITHUB_EVENT_PATH"]).read_bytes())
            checked = check_pull_request(event, get_api(os.environ.get("GH_TOKEN")), path_prefix=args.path_prefix,
                                         require_preview=args.require_pr_preview)
    except (ValidationError, URLError, OSError, ValueError, KeyError, TypeError) as exc:
        message = str(exc) if isinstance(exc, ValidationError) else "Could not read the pull request or proposal."
        message = "Data contribution precheck failed. " + message
        status = 1
    else:
        message = ("Proposal path, Markdown structure, and applicable PR preview checks passed. A maintainer still reviews the study design, "
                   "estimand, data access, and reproducibility." if checked else "No data proposal changed.")
        status = 0
    print(message, file=sys.stderr if status else sys.stdout)
    if summary := os.environ.get("GITHUB_STEP_SUMMARY"):
        with Path(summary).open("a", encoding="utf-8") as stream:
            stream.write("### Data contribution precheck\n\n" + message + "\n")
    return status


if __name__ == "__main__":
    sys.exit(main())

"""Publish the isolated DGP landing page to root CONTRIBUTING.md, never README.md."""
from __future__ import annotations
import re
from pathlib import Path
from urllib.parse import urlsplit

HOME = Path(__file__).resolve().parents[1]
ROOT = HOME.parent
PREFIX = HOME.name + "/"
REPOSITORY = "Statsinference/stats-inference-arena"
MARKDOWN_URL = re.compile(r"(?<=\]\()([^\s)]+)")
HTML_URL = re.compile(r"(\b(?:href|src)=)([\"'])([^\"']+)([\"'])")

def root_link(target: str) -> str:
    parsed = urlsplit(target)
    if parsed.scheme or parsed.netloc or target.startswith(("#", "/")):
        return target
    return PREFIX + target.removeprefix("./")

def render(source: str) -> str:
    source = source.replace(
        "https://github.com/Statsinference/submission_test/upload/main/incoming",
        "https://github.com/" + REPOSITORY + "/upload/main/" + PREFIX + "incoming",
    )
    source = MARKDOWN_URL.sub(lambda m: root_link(m.group()), source)
    source = HTML_URL.sub(lambda m: m.group(1) + m.group(2) + root_link(m.group(3)) + m.group(4), source)
    source = source.replace("# Statistical Inference Arena · DGP Submission", "# Contributing to Statistical Inference Arena", 1)
    source = source.replace("**Actions → Extract DGP ZIPs**", "**Actions → DGP submissions**")
    source = source.replace("`.github/workflows/dgp-zip-intake.yml`", "`.github/workflows/dgp-submissions.yml`")
    source = source.replace("`../.github/workflows/dgp-submissions.yml`", "`.github/workflows/dgp-submissions.yml`")
    source = source.replace("`incoming/`", "`dgp-submissions/incoming/`")
    return source.rstrip() + "\n\n## Existing benchmark documentation\n\n" + (
        "The DGP collection service does not change the benchmark protocol, website, or starter code. "
        "See the [project README](README.md), "
        "[scientific requirements](docs/contribution_en.md), and [starter](starter/README.md).\n"
    )

def main() -> None:
    destination = ROOT / "CONTRIBUTING.md"
    expected = render((HOME / "README.md").read_text(encoding="utf-8"))
    if not destination.exists() or destination.read_text(encoding="utf-8") != expected:
        destination.write_text(expected, encoding="utf-8")
    print("Contributing landing page synchronized; root README is untouched.")

if __name__ == "__main__": main()

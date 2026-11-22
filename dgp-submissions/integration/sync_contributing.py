"""Generate the root contribution guide for methods and data."""
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
    source = source.replace("**Actions → Extract DGP ZIPs**", "**Actions → DGP submissions**")
    source = source.replace("`.github/workflows/dgp-zip-intake.yml`", "`.github/workflows/dgp-submissions.yml`")
    source = source.replace("`../.github/workflows/dgp-submissions.yml`", "`.github/workflows/dgp-submissions.yml`")
    source = source.replace("`incoming/`", "`dgp-submissions/incoming/`")
    data_guide = re.sub(r"\A# [^\n]*\n*", "", source, count=1)
    data_guide = re.sub(r"^(#{2,5}) ", r"#\1 ", data_guide, flags=re.MULTILINE)
    return (
        "# Contribute to StatArena\n\n"
        "## Contribute a Method\n\n"
        "Submit a statistical method or model for evaluation on a supported StatArena task.\n\n"
        "1. **Test locally.** Use [StatArena Lite](lite/README.md) to run your method on public data and check its results.\n"
        "2. **Submit for evaluation.** Follow the "
        "[method submission guide](method-submissions/README.md) "
        "to provide your method link, choose a research domain, and submit the completed Markdown checklist. "
        "The StatArena team reviews submissions and evaluates eligible methods for the official leaderboard.\n\n"
        "## Contribute Data\n\n"
        "For a simulated DGP or real-data proposal, use the [Markdown submission guides](website/data-submissions/README.md). "
        "The package intake below covers ZIP submissions.\n\n"
        f"{data_guide.rstrip()}\n\n"
        "### Existing benchmark documentation\n\n"
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

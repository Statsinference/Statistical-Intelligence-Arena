"""Test links and isolation for the DGP service embedded in the benchmark repo."""
import importlib.util
import re
from pathlib import Path
from urllib.parse import urljoin, urlsplit, unquote

import pytest

HOME=Path(__file__).resolve().parents[1]
ROOT=HOME.parent
spec=importlib.util.spec_from_file_location("migration_sync",HOME/"integration/sync_contributing.py")
sync=importlib.util.module_from_spec(spec);spec.loader.exec_module(sync)

# In GitHub-rendered repository Markdown, a leading / starts at the repository
# content root (/OWNER/REPO/blob/REF/), not at github.com/. Two parent components
# leave blob/REF, so the owner and repository are retained, including in forks.
# This is a GitHub UI action URL, not a file path in the checked-out repository.
UPLOAD_LINK = "/../../upload/main/dgp-submissions/incoming"


def test_internal_intake_uses_current_destination_upload():
    text=(HOME/"INTERNAL_ZIP_INTAKE.md").read_text(encoding="utf-8")
    assert f'href="{UPLOAD_LINK}"' in text
    assert 'Submit_DGP-Upload_ZIP-' in text
    assert 'href="dgp-submissions/incoming/"' not in text
    assert "Statsinference/stats-inference-arena/upload/main" not in text
    assert "Statsinference/submission_test/upload" not in text


def test_every_root_contributing_link_resolves():
    text=(ROOT/"CONTRIBUTING.md").read_text(encoding="utf-8")
    paths=re.findall(r"\]\(([^\s)]+)",text)
    paths+=re.findall(r'(?:href|src)="([^\"]+)"',text)
    for target in paths:
        url=urlsplit(target)
        if url.scheme or url.netloc or not url.path:continue
        if target == UPLOAD_LINK:
            assert (HOME/"incoming").is_dir()
            continue
        assert (ROOT/unquote(url.path)).exists(),target


def test_sync_is_idempotent_and_cannot_modify_root_readme():
    before=(ROOT/"README.md").read_bytes()
    expected=sync.render((HOME/"README.md").read_text(encoding="utf-8"))
    assert expected==(ROOT/"CONTRIBUTING.md").read_text(encoding="utf-8")
    sync.main();sync.main()
    assert (ROOT/"README.md").read_bytes()==before
    assert expected==(ROOT/"CONTRIBUTING.md").read_text(encoding="utf-8")


def test_contribution_pages_keep_catalog_details_internal():
    for path in (
        ROOT/"CONTRIBUTING.md",
        HOME/"README.md",
        HOME/"CONTRIBUTING.md",
        HOME/"docs/SIMULATED_DGP.md",
        HOME/"docs/REAL_DATA_PROBLEM.md",
    ):
        text=path.read_text(encoding="utf-8")
        assert not re.search(r"\bstudents?\b", text, re.IGNORECASE), path
        assert "Paper list by research area" not in text, path
        assert "STATSARENA_PAPER_LIST" not in text, path
        assert "registry/" not in text, path
        assert "dgp-submissions/incoming" not in text, path

    index=(HOME/"registry/INDEX.md").read_text(encoding="utf-8")
    assert "## Paper list by research area" in index
    assert "| Paper Title | DGPs | DGP Mechanisms | Estimand | Keywords |" in index

    workflow=(ROOT/".github/workflows/dgp-submissions.yml").read_text(encoding="utf-8")
    assert "dgp_registry.paper_list" not in workflow


def test_generated_catalog_links_are_within_isolated_service():
    import json
    data=json.loads((HOME/"registry/catalog.json").read_text(encoding="utf-8"))
    for record in data["records"]:
        assert (HOME/"registry/drafts"/(record["record_id"]+".md")).is_file()
        if record.get("generator_file"):assert (HOME/"registry"/record["generator_file"]).is_file()


def test_fork_safe_submission_links():
    """All entry points keep the upload interaction without an upstream owner."""
    guide=(HOME/"INTERNAL_ZIP_INTAKE.md").read_text(encoding="utf-8")
    assert f'href="{UPLOAD_LINK}"' in guide
    assert "Statsinference/stats-inference-arena/upload/main" not in guide
    assert "Statsinference/submission_test/upload" not in guide
    assert 'href="incoming/"' not in guide
    assert 'href="dgp-submissions/incoming/"' not in guide
    assert "choose your files" in guide
    assert sync.root_link(UPLOAD_LINK) == UPLOAD_LINK


@pytest.mark.parametrize("repository", [
    "Statsinference/stats-inference-arena",
    "student-example/stats-inference-arena",
    "student-example/renamed-personal-fork",
])
@pytest.mark.parametrize("view_ref", ["main", "submission-preview"])
def test_upload_url_resolution_preserves_repository(repository, view_ref):
    """Model GitHub's documented repository-root link resolution, not login/UI."""
    content_root=f"https://github.com/{repository}/blob/{view_ref}/"
    actual=urljoin(content_root,UPLOAD_LINK.lstrip("/"))
    assert actual == f"https://github.com/{repository}/upload/main/dgp-submissions/incoming"
    assert "/blob/" not in actual


def test_sync_preserves_upload_link_at_both_document_depths():
    snippet=f'<a href="{UPLOAD_LINK}">Upload ZIP</a>'
    rendered=sync.render(snippet)
    assert snippet in rendered
    assert f'dgp-submissions/{UPLOAD_LINK}' not in rendered

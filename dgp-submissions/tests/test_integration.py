"""Test links and isolation for the DGP service embedded in the benchmark repo."""
import importlib.util
import re
from pathlib import Path
from urllib.parse import urlsplit,unquote
HOME=Path(__file__).resolve().parents[1]
ROOT=HOME.parent
spec=importlib.util.spec_from_file_location("migration_sync",HOME/"integration/sync_contributing.py")
sync=importlib.util.module_from_spec(spec);spec.loader.exec_module(sync)

def test_contributing_uses_current_destination_upload():
    text=(ROOT/"CONTRIBUTING.md").read_text(encoding="utf-8")
    assert 'href="dgp-submissions/incoming/"' in text
    assert "Statsinference/stats-inference-arena/upload/main" not in text
    assert "Statsinference/submission_test/upload" not in text
    assert "| Paper Title | DGPs | DGP Mechanisms | Keywords | Generator.py |" in text

def test_every_root_contributing_link_resolves():
    text=(ROOT/"CONTRIBUTING.md").read_text(encoding="utf-8")
    paths=re.findall(r"\]\(([^\s)]+)",text)
    paths+=re.findall(r'(?:href|src)="([^\"]+)"',text)
    for target in paths:
        url=urlsplit(target)
        if url.scheme or url.netloc or not url.path:continue
        assert (ROOT/unquote(url.path)).exists(),target

def test_sync_is_idempotent_and_cannot_modify_root_readme():
    before=(ROOT/"README.md").read_bytes()
    expected=sync.render((HOME/"README.md").read_text(encoding="utf-8"))
    assert expected==(ROOT/"CONTRIBUTING.md").read_text(encoding="utf-8")
    sync.main();sync.main()
    assert (ROOT/"README.md").read_bytes()==before
    assert expected==(ROOT/"CONTRIBUTING.md").read_text(encoding="utf-8")

def test_generated_catalog_links_are_within_isolated_service():
    import json
    data=json.loads((HOME/"registry/catalog.json").read_text(encoding="utf-8"))
    for record in data["records"]:
        assert (HOME/"registry/drafts"/(record["record_id"]+".md")).is_file()
        if record.get("generator_file"):assert (HOME/"registry"/record["generator_file"]).is_file()


def test_fork_safe_submission_links():
    """The same Markdown must work in a personal fork, without upstream write access."""
    main=(HOME/"README.md").read_text(encoding="utf-8")
    guide=(HOME/"CONTRIBUTING.md").read_text(encoding="utf-8")
    for source in (main,guide):
        assert 'href="incoming/"' in source
        assert "Statsinference/stats-inference-arena/upload/main" not in source
    rendered=sync.render(main)
    assert 'href="dgp-submissions/incoming/"' in rendered
    assert "Statsinference/stats-inference-arena/upload/main" not in rendered

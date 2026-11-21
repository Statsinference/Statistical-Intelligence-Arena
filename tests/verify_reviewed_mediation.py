"""Exercise a reviewed third result through the real leaderboard without publishing a test entry."""
import csv
import json
import mimetypes
import os
from pathlib import Path
import sys
from urllib.parse import urlsplit

from playwright.sync_api import expect, sync_playwright

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "method-submissions"))
from approve_mediation import RELEASE, make_row


def check_reviewed_mediation(browser, scores=None):
    name = "=New <study>"
    submission = {"schema_version": 2, "is_test": False, "domain": "mediation", "issue_number": 9001,
                  "method_name": name, "version": "v1", "method_url": "https://example.org/method",
                  "estimator": "Regression with percentile intervals"}
    if scores is None:
        scores = {"tables": 2000, "paired_mechanisms": 1000, "bias": -.03, "rmse": .12,
                  "variance_within_mechanism": .01, "coverage_95": .95, "mean_interval_length": .4,
                  "mean_inference_seconds": .8}
    rows = []
    page = browser.new_page(accept_downloads=True)

    def serve(route):
        url = urlsplit(route.request.url)
        if url.hostname != "arena.example":
            return route.abort()
        if url.path == "/data/mediation-reviewed.json":
            return route.fulfill(json={"release": RELEASE, "rows": rows})
        file = ROOT / (url.path.strip("/") or "index.html")
        if not file.is_file():
            return route.fulfill(status=404)
        return route.fulfill(body=file.read_bytes(), content_type=mimetypes.guess_type(file.name)[0] or "text/plain")

    page.route("**/*", serve)
    page.goto("https://arena.example/#domain=mediation")
    historical = page.locator("#leaderboard tbody tr[data-method]")
    page.wait_for_function("document.body.dataset.testView === 'ready'")
    initial_count = historical.count()
    rank = 1 + sum(value < scores["rmse"] for value in page.evaluate(
        "current().rows.filter(r => r.status !== 'partial').map(r => r.rmse)"))
    rows.append(make_row(submission, scores, "other"))
    page.reload()
    page.wait_for_function("document.body.dataset.testView === 'ready'")
    assert historical.count() == initial_count + 1
    approved = historical.nth(rank - 1)
    assert approved.locator(".mname").inner_text() == name and not approved.locator("study").count()
    assert approved.locator(".rank-medal").get_attribute("aria-label").startswith(f"Rank {rank} (")
    approved.locator(".method-toggle").click()
    details = page.locator(".method-details-row")
    assert submission["estimator"] in details.inner_text()
    assert details.locator('a[href="https://example.org/method"]').count() == 1
    assert details.locator('a[href$="/issues/9001"]').count() == 1
    page.locator('[data-fam="other"]').click()
    assert historical.count() == 1
    for chart in ("rmse-time-chart", "coverage-length-chart"):
        point = page.locator(f'#{chart} .chart-point[data-method="{name}"]')
        point.wait_for(state="visible")
        expect(page.locator(f"#{chart} .chart-point")).to_have_count(1)
    page.locator("#q").fill("unknown method")
    assert historical.count() == 0
    page.locator("#q").fill("new")
    with page.expect_download() as download:
        page.locator("#export-btn").click()
    with download.value.path().open(encoding="utf-8", newline="") as source:
        exported, = csv.DictReader(source)
    assert exported["method"] == "'" + name and float(exported["coverage"]) == scores["coverage_95"]
    assert exported["rank"] == str(rank) and exported["source_file"].endswith("/issues/9001")
    page.close()


if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(executable_path=os.environ.get("CHROMIUM_EXECUTABLE"))
        check_reviewed_mediation(browser)
        browser.close()
    print("Reviewed result entered ranks, method details, charts, filters and CSV.")

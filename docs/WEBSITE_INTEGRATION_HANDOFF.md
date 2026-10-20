# Website integration handoff

For Jiaming Hu and the project team · Protocol v0.3 · 18 October 2026 · Output schema 0.2.0

## Purpose and current status

Statistical Inference Arena is the working name of a benchmark for confidence intervals for causal estimands, with point accuracy, availability and cost reported alongside coverage. The English website is a compact discussion and contribution portal. The English and Chinese contribution protocols are the detailed scientific specification.

This repository supplies documentation, a static website, planned configurations, illustrative records and structural checkers. It does not supply a completed mediation reference demo, DGP collection, hyperdistribution sampler, training runner, statistical evaluator, trained checkpoint or empirical leaderboard. Training has not started as part of this delivery.

The intended next website can combine this material with Jiaming's website. His website URL, source files and design have not been supplied in this handoff; no merge has been performed and no assumptions are made about its implementation.

## Scientific content to preserve

- Keep exactly the initial six collection families: `ate`, `cate`, `mediation`, `iv`, `proximal`, `did_sc`. DiD and synthetic control share a collection label but retain distinct targets, assumptions, sampling and CI contracts. Mediation NIE and NDE are separate target records.
- Keep Layer B method evaluation as the required initial scope. Layer A complete analysis is optional and separately reviewed.
- Show the development sequence: **classical DGP registration and independent truth check → task-conditional hyperdistribution Pi_k → small task-compatible PFN → fixed-DGP CI evaluation**.
- Pi_k is a distribution over mechanism/configuration choices for a specified task and estimand. Supply roles, target ID and any CATE query. A first single-family mediation pilot is sufficient. A future joint model must condition on these contracts or use compatible heads/adapters; a table alone does not specify its estimand.
- Keep oracle information out of deployed model inputs. Distinguish true-target supervision, sample-dependent teachers and estimator distillation, and disclose architecture, training and CI construction.
- Separate fresh-seed evaluation within a mechanism from held-out parameters, mechanisms or tasks. Published classical DGPs are not automatically unseen to pretrained models.
- Evaluate paired methods over independent repeated datasets at each **fixed** DGP and n. Fix CATE queries as declared; use design-aware sampling for panels and clusters. Averaging coverage while changing DGPs is a different quantity.
- Match total observed-label budgets, disclose context/calibration/tuning allocations, and distinguish native-frozen, adapted and refit procedures. Prespecify coverage basis, denominator and availability/failure gate; compare lengths after a common coverage gate, with Monte Carlo uncertainty. Retain failures and justified unbounded intervals.

The contribution protocols remain authoritative when the site's compact wording omits a detail. Output schema 0.2.0 retains compatibility fields beyond the initial causal track; this does not add a future-response prediction track. Disconnected parameter confidence sets and simultaneous bands require explicit versioned extensions.

## Repository content and editing roles

| Location | Role |
| --- | --- |
| `site/index.html` | English page structure and concise content; four sections: Benchmark, Contribute, Protocol, Arena. |
| `site/styles.css` | Site styling and responsive layout. |
| `site/app.js` | Tab navigation, family explanations and proposed Arena comparison slots. No evaluation service. |
| `site/downloads/` | Portable download copies of the contribution resources and starter archive. Preserve filenames or update every corresponding link. |
| `docs/contribution_en.md`, `docs/contribution_zh.md` | Canonical English and Chinese scientific and contribution requirements. |
| `docs/student_guide_en.md`, `docs/student_guide_zh.md` | Eleven-step contributor walkthroughs. |
| `docs/pdf/` | Rendered English, Chinese and combined contribution PDFs. |
| `starter/` | Task contract, DGP registry, planned hyperdistribution/training/evaluation configurations, illustrative records and format checkers. |

Legacy CausalTaskBench filenames in site downloads are compatibility filenames, not a separate benchmark. Rename them only with coordinated link updates. When moving canonical Markdown into `docs/`, update its internal relative links as well as the website links.

## Suggested integration procedure

1. Inspect Jiaming's site once its URL and source are available; agree on the destination framework, navigation and canonical repository. Keep the scientific contracts unchanged until the team reviews a substantive revision.
2. Use the current four sections as reusable content. The compact white/green visual style is optional; the task definitions, status and contributor steps are not decorative text.
3. Port `site/index.html`, `site/styles.css` and `site/app.js` together for the initial static preview, or translate their behavior into the destination framework. Preserve accessible tab/filter labels and all six families.
4. Preserve the `downloads/` directory beside the served page, or rewrite every resource URL to the destination public-assets path. A project site may be served under a repository subpath: test that deployment path rather than assuming the domain root.
5. Keep the canonical documents in `docs/` and templates in `starter/`. Generate or copy download resources from those sources, with matching versions and bytes. Do not maintain divergent scientific text in the website's download folder.
6. Preview locally from the repository root with `python -m http.server 8000 --bind 127.0.0.1`, then open `http://127.0.0.1:8000/site/`. Test the merged site's own build and deployment separately once chosen. This preview does not run Python training in a browser.
7. Review the merged page with the team before replacing any existing website. Publication of a merged site and any future submission backend are separate implementation work.

## Arena template

The current table displays **proposed method slots** for a classical reference, native PFN and adapted PFN where appropriate. All comparisons are pending; em dashes mean not measured. References are candidates requiring implementation and target-specific justification. There are no rankings, scores or claims that a PFN wins.

Keep template status prominent. A future result release must attach a task/target/design, DGP/version and split, sample size and independent repetition count, method/checkpoint and mode, output contract, coverage/Monte Carlo uncertainty, length, accuracy, failures/availability and costs, together with provenance and review evidence. Do not replace placeholders with demonstration numbers that could be mistaken for results.

## Student contribution journey

Link to the full bilingual walkthroughs rather than expanding the entire protocol onto the landing page:

1. Select one family, target and scientific owner.
2. Read the original source and register the DGP with exact locators and rights.
3. Implement observed data and independently check truth.
4. Configure Pi_k and freeze train/development/evaluation uses.
5. Define roles, query, teacher, output head/loss and CI rule.
6. Implement the classical reference and PFN adapter.
7. Run existing structural checks; later add a bounded implemented smoke test.
8. Review and freeze a small training plan before its later execution.
9. Evaluate full CI procedures on paired independent fixed-DGP repetitions.
10. Record AI pre-review, scientific review and an independent rerun.
11. Freeze actual evidence and declare the reached milestone.

The milestones are proposal, reference-demo-ready, training-ready and statistically validated. A filled configuration or structural pass does not establish any later scientific milestone. The first mediation implementation will be developed separately.

## Release synchronization and acceptance checks

- Check that the site, both canonical languages, PDF title/footer metadata, student guides, starter and downloadable copies all declare protocol v0.3, date 2026-10-18 and output schema 0.2.0. Change the protocol and output schema independently when warranted.
- Confirm that Markdown links work from their canonical `docs/` locations and download copies; verify each downloaded PDF opens and matches its canonical counterpart. Regenerate starter archives after changing starter files.
- Exercise all four site sections, six family tabs, Arena family/target/regime filters and every download link, including deployment under a project subpath. Check narrow screens and keyboard controls in the chosen destination site.
- From `starter/`, run `python validate_submission.py --mode scaffold` and `python evaluation/check_contract.py`; both should pass. The untouched starter should fail `python validate_submission.py --mode submission` because it is intentionally unfinished. These checks do not parse YAML semantics or train/evaluate a model.
- Inspect that no local absolute paths, credentials, personal transcripts, hidden evaluation assets or obsolete artifacts are included. Keep future restricted evaluation assets out of a public repository.
- Confirm that no placeholder result is presented as measured and no planned implementation is described as runnable. Record what was actually tested for the merged site.

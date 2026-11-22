# Leaderboard result format

`data/results.json` contains approved, source-reported summaries. Domains without results remain empty. Do not add simulated results or unapproved experiments.

Each `suites` entry represents one comparable evaluation suite with a unique `id`, a `domain`, a `label`, an explicit `target` (estimand) and a `rows` array. Optional metadata includes `sample_size`, `nominal_coverage`, `aggregation`, `hardware`, `timing_scope` and source provenance.

Domain IDs: `ate`, `cate`, `mediation`, `iv`, `proximal`, `did_sc`, `nonparametric_regression`, `quantile`, `semi_supervised`, `missing_data`.

Each row uses `group` (`ID` or `OOD`), `method`, `method_id`, `family` (`pfn` or `classical`), and metrics `bias`, `variance`, `rmse`, `length`, `coverage`, `time_s`. Values are finite numbers or null. All except bias are nonnegative. Coverage is a fraction in [0,1]. Unknown values are null, never zero. Variance is not SE. Distinct configurations use distinct method IDs.

`status: "not_reported"` marks an unavailable comparison row; all six metrics must be null. Such rows do not enter rankings or plots. Exports retain this status.

When `variance_basis` is `square_of_rounded_reported_se`, `variance_is_approximate` is true and `reported_se` is preserved. Display the value with ≈ and explain the conversion. It is not an exact raw empirical variance. Do not reconstruct RMSE from aggregate Bias and Variance.

`dgp_results` contains independently transcribed per-configuration rows when these are public. Mediation releases publish method and split summaries and keep the official test mechanisms with the evaluators. Do not recompute aggregates from rounded per-DGP results. `timing_comparisons` uses an explicit historical cohort with `scope: "previous_model_and_test_set"`; these CPU measurements do not enter current ID/OOD rankings or plots. Copy `median_paired_ratio` from its source, not from ratios of displayed median times.

`source` records report title, author, date, filename and page/table locators. Only the approved summaries are public; the internal PDF is not included. OOD metadata must identify the reference training stage and held-out units.

The inline `results-data` JSON in `index.html` must equal the external JSON. The live website refreshes from the external file. Tests check their agreement and the separation of measurement cohorts.

For local viewing, run `python3 -m http.server 8000`. Never place private datasets, archives, credentials or unpublished results in this public repository.

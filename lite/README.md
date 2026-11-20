# StatArena Lite

Run the versioned public starter datasets on your own machine. Each supported domain has 48 training studies, 16 development studies and 32 public reference test studies. Lite scores are for local development and reproducibility. Official submissions follow the [benchmark cards and submission workflow](../method-submissions/README.md).

## Commands

From the root of the repository, install with `python -m pip install -e ./lite` using Python 3.10 or later.

```bash
statarena-lite list
statarena-lite prepare --domain iv
statarena-lite run --domain iv --split dev --method baseline
statarena-lite run --domain iv --split dev --method ./lite/examples/my_method.py
statarena-lite score --domain iv --split dev --predictions lite-results/iv-dev-my_method.csv
```

`prepare` prints the directory of the extracted starter. The first command that needs a domain's data downloads and verifies its versioned archive. The cache defaults to `~/.cache/statarena-lite`. Set `STATARENA_LITE_CACHE` to select another directory.

`run` saves one predictions CSV to `lite-results/` unless you pass `--output PATH`. A successful rerun to the same path replaces that CSV. Both `run` and `score` print a JSON report with the domain, split, dataset checksum and metrics. Lite uses the scorer bundled with each release. Reports include bias, RMSE, coverage as a fraction and mean interval length. Releases may include additional metrics, such as within-configuration variance for ATE and CATE.

## Using your own method

Pass the path to a local Python file with a function named `estimate(study)`. The runner calls the function once per study. Return `(estimate, ci_lower, ci_upper)` as three finite numbers with ordered limits for a nominal 95% interval. See [the runnable IV example](examples/my_method.py) for the interface.

`study` is a dictionary with `table_id`, `domain` and the following observed arrays. CATE and Proximal include a `query` dictionary with the target covariates. The starter scorer uses the public simulation truth after estimation.

| Domain | Observations | Target |
| --- | --- | --- |
| `ate` | `X1` and other covariates, `T`, `Y` | Population ATE |
| `cate` | `X1` and other covariates, `T`, `Y` and `query` | CATE at the specified query |
| `mediation` | `X1` and other covariates, `A`, `M`, `Y` | Natural indirect effect |
| `iv` | `X`, `Z`, `D`, `Y` | Local average treatment effect |
| `proximal` | `X1`, `X2`, `Z`, `W`, `A`, `Y` and `query` | Proximal CATE at the specified query |
| `did` | `X`, `D`, `delta_y` | Average treatment effect on the treated in a two-period panel |

For a method in R, Julia or another environment, use `prepare` to locate the inputs and write a CSV with exactly one row per study in the selected split. Use these column names:

```csv
table_id,estimate,ci_lower,ci_upper
```

Pass the CSV to `statarena-lite score` with the same domain and split.

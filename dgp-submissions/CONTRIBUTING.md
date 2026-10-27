# Contributing a literature DGP

<p align="center"><a href="https://github.com/Statsinference/stats-inference-arena/upload/main/dgp-submissions/incoming"><img src="https://img.shields.io/badge/Upload_one_structured_ZIP-Open_GitHub_Upload-1677C8?style=for-the-badge" alt="Submit one ZIP" /></a></p>

**No Issues. No API Key. No local server. Everything happens in this private GitHub repository.**

## Student instructions

1. Click **Upload one structured ZIP** above to open GitHub's file uploader in `incoming/`.
2. Choose or drag in your `.zip`.
3. Commit to `main` if you have permission. If branch protection requires a PR, choose a new branch and open the PR.

**Do not extract the ZIP before uploading it.** One ZIP may contain multiple mechanisms and scenarios.

## Research area (ten choices)

The upload is classified using `family` in each `collection.json`:

| family in JSON | Area |
|---|---|
| `ate` | Average Treatment Effect |
| `cate` | Conditional Average Treatment Effect |
| `mediation` | Mediation |
| `iv` | Instrumental Variables |
| `proximal` | Proximal Causal Inference |
| `did_sc` | DiD / Synthetic Control |
| `nonparametric_regression` | Nonparametric Regression |
| `quantile` | Quantile Inference |
| `semi_supervised` | Semi-Supervised Inference |
| `missing_data` | Missing Data |

Aliases include `nri`, `qr`, `qdi`, `quantile_regression`, `ssi` and `ssl`.
An unrecognized value appears in Needs classification, not arbitrarily categorized.

**High-dimensional and interference DGPs are welcome.** Preserve their actual
mechanisms, dimensions, sampling structure and assumptions. Do not change
`high_dimensional` or `interference` to false to satisfy an example or test.
The collection scope is broader than the original benchmark evaluator.
See [collection scope and required scientific descriptions](docs/COLLECTION_SCOPE.md).

## What happens next

GitHub Actions reads ZIPs without executing submitted code. Each safe, valid
DGP becomes an **unverified draft**, with source paper, equations, variables,
parameters, estimand and reported truths. A researcher must check the original
source and scientific validity.

A malformed file or DGP is reported separately and does **not** block other
valid submissions. [Open the submission processing report](registry/INTAKE_REPORT.md)
to see failed files and reasons. A successful workflow may contain input warnings;
this does not mean the rejected file passed. Repair only the affected upload.

Learn more: [required ZIP format](docs/ZIP_FORMAT.md).

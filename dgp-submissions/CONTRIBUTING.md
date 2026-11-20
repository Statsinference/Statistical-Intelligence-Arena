# Data contribution instructions

Prepare your submission using the guide for your contribution type.

- [Simulated DGP](docs/SIMULATED_DGP.md) covers the scientific motivation, simulation design, estimand, reference value and reproducibility. It includes a template and a filled example.
- [Real-data problem](docs/REAL_DATA_PROBLEM.md) covers the question, dataset access, study design and how methods will be compared. It includes a template and a filled example.

## Submit a structured ZIP to the private literature DGP catalog

Collaborators with access to the research repository can contribute a literature-derived mechanism directly to the existing catalog.

<p align="center"><a href="/../../upload/main/dgp-submissions/incoming"><img src="https://img.shields.io/badge/Upload_ZIP-Choose_or_drop_files-1677C8?style=for-the-badge" alt="Upload a ZIP directly to this repository" /></a></p>

### Upload and open a pull request

1. **Collaborators with read access:** fork the private upstream repository into **your personal GitHub account**, then open your fork (URL must begin with your username, not `Statsinference`). For an existing fork, use **Sync fork → Update branch** to obtain the updated upload button.
2. Click **Upload ZIP** above to open GitHub's **file-upload page directly**, targeting `dgp-submissions/incoming/` on `main` **in the repository you are viewing**. **Drag and drop your `.zip`, or click “choose your files”**, then **Commit changes** to your fork. Your fork's `main` is not the upstream repository's `main`.
3. In your fork, click **Contribute → Open pull request** targeting `Statsinference/Statistical-Intelligence-Arena:main`. The **DGP ZIP-only** check must pass before a maintainer merges. Contributors with direct upstream Write access can instead upload to upstream.

The button stays in the repository you are viewing; it does not automatically find your fork from the upstream page. Check the repository owner before uploading. **Do not extract the ZIP before uploading it.** One ZIP may contain multiple mechanisms and scenarios.

## Research area

The upload is classified using `family` in each `collection.json`:

| family in JSON | Area |
|---|---|
| `ate` | Average Treatment Effect |
| `cate` | Conditional Average Treatment Effect |
| `mediation` | Mediation |
| `iv` | Instrumental Variables |
| `proximal` | Proximal Causal Inference |
| `did` | Difference-in-Differences |
| `synthetic_control` | Synthetic Control |
| `did_sc` | Legacy combined DiD / Synthetic Control; requires manual classification |
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

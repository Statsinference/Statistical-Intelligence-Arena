# Contributing a literature DGP

<p align="center"><a href="https://github.com/Statsinference/stats-inference-arena/upload/main/dgp-submissions/incoming"><img src="https://img.shields.io/badge/Upload_one_structured_ZIP-Open_GitHub_Upload-1677C8?style=for-the-badge" alt="Submit one ZIP" /></a></p>

**No Issues. No API Key. No local server. Everything happens in this private GitHub repository.**

## Student instructions

1. Click **Upload one structured ZIP** above to open GitHub's file uploader in `incoming/`.
2. Choose or drag in your `.zip`.
3. Commit to `main` if you have permission. If branch protection requires a PR, choose a new branch and open the PR. That's all.

**Do not extract the ZIP before uploading it.** One ZIP may contain multiple mechanisms and scenarios.

## Research area (six choices)

The upload is classified using `family` in each `collection.json`:

| family in JSON | Area |
|---|---|
| `ate` | Average Treatment Effect |
| `cate` | Conditional Average Treatment Effect |
| `mediation` | Mediation |
| `iv` | Instrumental Variables |
| `proximal` | Proximal Causal Inference |
| `did_sc` | DiD / Synthetic Control |

You do **not** need to select the area on a web form, because the ZIP tells the parser. An unrecognized value appears in the Needs Classification queue, not arbitrarily categorized.

## What happens next

GitHub Actions reads the ZIP without executing any submitted code. It checks the required metadata, extracts paper/DGP/variables/equations/scenario/estimand/true values and generates the [`six-area registry`](registry/INDEX.md). The upload is **a draft, not scientifically accepted**; a researcher must verify the literature references and any numerical ground truth.

Learn more: [required ZIP format](docs/ZIP_FORMAT.md).

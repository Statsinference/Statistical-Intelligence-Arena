# Internal literature DGP intake

Collaborators who already have a structured literature DGP ZIP can contribute it through a pull request. [Browse the DGP catalog](registry/INDEX.md).

### Submit a structured ZIP

1. Create a branch from `main` in your fork. If you have write access, you can create the branch in StatArena directly.
2. Upload the structured `.zip` to `dgp-submissions/incoming/` on that branch and commit the file there.
3. Open a pull request to `Statsinference/Statistical-Intelligence-Arena:main`. The **DGP ZIP-only** check validates the submission and produces a catalog preview for a maintainer to review before merging.

The ZIP's `collection.json` already identifies its research family, so **contributors do not need to select it again**. A missing or unknown family is flagged for human classification, never guessed.

> **Important:** This is a private research intake. Each contribution becomes an **unverified draft** until a researcher checks the original paper. This software does not prove true values or equations correct.

## What gets extracted

| Scientific information | Stored in DGP registry |
|---|---|
| Reference paper | Citation, DOI, publication, paper/section locator |
| DGP mechanism | Name, generating equations, distributions and coefficients |
| Variables | Observed columns and their roles; latent variables flagged for review |
| Scenario | Parameter settings and experiment variants |
| Estimand | Which quantity (e.g. ATE/NDE/LATE) and definition |
| True value | Scenario-specific value (or needs review), calculation notes |
| Provenance | Uploaded ZIP, hashes, original/adapted notes and validation status |

**Hierarchy:** Area → Paper → DGP → Scenario → Estimand & Truth. One paper may contribute multiple DGPs, and one DGP may contain multiple scenarios.

[Submission processing report](registry/INTAKE_REPORT.md) · [Records needing review](registry/ESTIMAND_NEEDS_REVIEW.md)

## Scientific content and formatting checklist

Use this checklist when preparing each DGP folder in your ZIP. The [ZIP format](docs/ZIP_FORMAT.md) describes the supported files and fields. A successful intake only checks the submitted structure; a researcher must still review the paper, equations, estimand, implementation, and truth.

### 1. Choose the research area and identify the exact target

The **research area** describes the subject of the DGP. The **estimand** (parameter of interest) is the precisely defined quantity to be estimated in that DGP. An area alone, a paper's general topic, a treatment-induced confounder, or a symbol such as `theta` does not identify the estimand. Give its full name, a definition, the relevant population or conditioning value, and an equation. Use the notation and conventions of the source, and define each symbol; state the treatment levels, contrast direction, scale and time point where relevant.

Examples of targets within the requested areas include:

| Research area | Examples of specific estimands to identify |
|---|---|
| Average Treatment Effect (ATE) | Population average treatment effect |
| Conditional Average Treatment Effect (CATE) | CATE at a specified covariate value or for a specified subgroup |
| Mediation | Natural indirect effect (NIE), natural direct effect (NDE), interventional indirect effect, or a specified dynamic mediation effect |
| Instrumental Variables (IV) | Population local average treatment effect (LATE) for the specified complier population, when applicable |
| Proximal Causal Inference | The particular target, for example ATE or CATE, defined for its population |
| Difference-in-Differences (DiD) | Average treatment effect on the treated (ATT), including the relevant time or cohort |
| Synthetic Control | The study's specified treated-unit or aggregate effect and post-treatment time point |
| Nonparametric Regression | The regression function or a specified pointwise/functional target |
| Quantile Inference | Conditional quantile at a stated level and covariate value |
| Semi-Supervised Inference | The target parameter and the population to which it refers |
| Missing Data | The full-data target and the population to which it refers |

These are examples, not an exhaustive list or a requirement to relabel a paper's target. Natural, interventional and dynamic effects are distinct; define the exact version from the source. In mediation, treatment-induced confounding is a feature of a causal setting, not by itself an estimand. Do not infer a natural effect merely from a paper discussing mediation. IV and proximal inference are approaches or settings: identify the actual target they estimate.

The intake uses `collection.json.family` for the primary area. For new submissions use `did` for Difference-in-Differences or `synthetic_control` for Synthetic Control. Eleven historical `did_sc` records have provisional catalog placements tied to their submitted ZIP hashes; changed or unrecognized mixed-family submissions are sent for manual classification. These placements do not constitute scientific review. Other values are `ate`, `cate`, `mediation`, `iv`, `proximal`, `nonparametric_regression`, `quantile`, `semi_supervised`, and `missing_data`. An unrecognized value is flagged for human classification.

### 2. Write an informative estimand field

In `collection.json`, put the full target and its mathematical definition in `estimand.definition`; `estimand.symbol` supplies a short display label. For example, the following illustrative ATE specifies a population-level mean contrast; `Y(1)` and `Y(0)` are the potential outcomes under treatment and control:

```json
"estimand": {
  "symbol": "ATE",
  "definition": "ATE = E[Y(1) - Y(0)] in the target population; Y(a) is the outcome under treatment level a."
}
```

Replace this example with the source's actual estimand. For example, write a full NIE definition with the exposure level held fixed and the mediator interventions identified, or a LATE definition with the relevant complier population. Do not replace an unknown expression with a guessed formula. A single symbol, or a long derivation that never states the target, is not sufficient. If a different target is needed for another mechanism, submit it as a separate DGP record with its own `collection.json`; do not silently combine unrelated targets.

For recognized abbreviations the current renderer derives the label from a definition beginning, for example, `ATE = ...`, `NIE = ...`, or `LATE = ...`; otherwise it uses `estimand.symbol`. Names should be recognizable and consistent; use the full name and exact definition in the text. Paper-specific notation may be retained after it is defined.

### 3. Record the mechanism, variables, and sources clearly

- Provide the paper's actual English title, citation, DOI or stable URL, and exact section, page, equation, or simulation location. Put a descriptive English DGP title in `title` or `title_en`. A title placeholder means the English display title is missing, not that the record has passed review.
- State each generation equation, distribution, dependence structure and coefficient needed to reproduce the mechanism. Explain which variables are observed and which are latent; use `schema.csv` for concise observed variable names and roles, and `latent_variables` when applicable. Avoid putting paragraphs of variable descriptions into variable names.
- Supply source-faithful LaTeX for equations when available, alongside their original expressions as shown in the [ZIP format](docs/ZIP_FORMAT.md). Define all notation, use valid JSON escaping, and inspect the rendered GitHub page. Display formatting is not proof of mathematical correctness.
- State whether the DGP is original or adapted and describe adaptations. Give each scenario's sample sizes and parameter settings. If the truth is reported, give its value and source or derivation for that specific target and scenario. If unavailable or unverified, say so; never infer or fabricate it.
- Add accurate, mechanism-specific `properties.keywords` supported by the source, such as randomized treatment, observed confounding, nonlinear propensity, interaction, high dimensionality, missingness, heterogeneous effects, or panel data where applicable. Do not treat missing tags as evidence that a property is absent. Distinguish nonlinearity in the assignment, mediator and outcome models when it matters.

### 4. Understand registry status and review before submission

A supplied numeric value is not scientific approval: reviewers must check the value and the corresponding equation against the source. Intake does not independently execute a contributor's checks, and all extracted entries remain drafts pending scientific review. The original truth-status metadata remains available in each raw scientific JSON record.

Before submitting, verify that the target's name, definition, population, source location, equations, variables, scenario settings, and truth all agree with each other and the source. Check the ZIP before submission; after opening the pull request, review the generated preview for missing values, malformed formulas, unreadable symbols and broken links. Leave uncertain scientific information explicitly marked for review rather than filling gaps by guesswork.

## Browse research areas

[ATE](registry/by-domain/ate.md) · [CATE](registry/by-domain/cate.md) · [Mediation](registry/by-domain/mediation.md) · [IV](registry/by-domain/iv.md) · [Proximal Causal Inference](registry/by-domain/proximal.md) · [DiD](registry/by-domain/did.md) · [Synthetic Control](registry/by-domain/synthetic_control.md) · [Nonparametric Regression](registry/by-domain/nonparametric_regression.md) · [Quantile Inference](registry/by-domain/quantile.md) · [Semi-Supervised Inference](registry/by-domain/semi_supervised.md) · [Missing Data](registry/by-domain/missing_data.md)


After the submission PR merges, **Actions → DGP submissions** prepares updates to [`registry/INDEX.md`](registry/INDEX.md) and the research area catalogs in a separate pull request. A maintainer reviews and merges the catalog update. If the workflow cannot open the pull request, the run summary links to the catalog branch comparison.

## Example and format

The downloadable [`examples/proximal_10_dgps.zip`](examples/proximal_10_dgps.zip) is a structured test archive (10 DGPs, 11 scenarios from 7 papers). For required fields and limitations, see [ZIP format](docs/ZIP_FORMAT.md) and [collection scope](docs/COLLECTION_SCOPE.md).

### Safety and limitations

Submitted ZIPs are treated as **data only**, never executed. The catalog shows extracted text and submitted truth values with **Needs scientific review** labels. The archive format requires structured `collection.json` and `config.json`. If the ZIP only contains a raw PDF or random Python code, deterministic extraction is not possible without additional author-supplied structure.

DGP area comes from the ZIP's `collection.json` `family` field.

# Simulated DGP

Propose one reproducible simulation that mirrors a documented study or isolates a statistical behavior worth testing. A reviewer should be able to generate a table, identify what each method receives and verify the target value independently.

[Copy the Markdown template](#3-copy-the-markdown-template) · [Submission steps](#4-check-and-open-the-pull-request) · [Worked example](#worked-public-example)

## 1. Check that the design fits

- Identify one inferential task and the behavior it tests. Examples include limited overlap, heterogeneous effects, nonlinear mediation and weak instruments. Explain why that behavior matters for the methods being compared.
- Ground the design in a study, empirical pattern or methodological reference where possible. Explain what the source supports and what you introduce. For a controlled stress test, say which feature changes and which parts of the design stay fixed across comparisons.
- State what the method observes. Keep latent variables, oracle nuisance functions, intervention outputs and reference values out of the observed input unless the task explicitly gives the same information to every method.

## 2. Prepare the evidence

| Required section | What a reviewer should be able to verify |
| --- | --- |
| Research question | The primary domain, optional keywords, statistical target, intended use and behavior under test. Explain why this question is worth adding to the benchmark. |
| Study design and data source | The population or setting, unit of observation, relevant references and which settings are calibrated or introduced. Include the sampling structure and proposed table sizes. |
| DAG and identification | Observed and latent variable roles, directed edges, time ordering and identification assumptions. Document any intentional violations. |
| Variables and data-generating process | Variable definitions and table schema, full structural equations and their parent edges, sampling order, dependencies and scenario settings. |
| Data-generating process and estimand | The treatment or contrast, estimand and its units, and the calculation used to verify the reference value. |
| Benchmark comparison | Expected outputs, a baseline, shared inputs and scoring. Specify the number of attempted replicates, scenario weighting if relevant, and the treatment of failures. |
| Materials and access | Shareable references and reproducibility instructions. For official evaluation candidates, identify the files available for private review. |

### Match the DAG to the equations

Use the same short variable IDs in the graph and equations. Use `A` for treatment or exposure, `Y` for the outcome, and `X` for covariates and confounders, with variants such as `X_1` or `X_latent`. In the case file, a diagram is optional. If you include one, show the arrows for the scenario it describes and label each node with its ID and a short meaning such as `A (treatment)`. Put definitions and assumptions in the prose.

List arrows between substantive variables, including observed and shared latent causes. Use a variable such as `X_latent (unobserved confounder)` for a shared latent cause. Write disturbances as $\epsilon$ or $\epsilon_Y$ in the equations and specify their distributions and dependencies. Keep them out of the diagram and both edge lists. If scenarios change an edge, list the union in both fields and say which scenarios omit the edge.

Write each field on one line. Use variable IDs that start with an ASCII letter and contain only letters, digits or underscores. Use short aliases for longer column names. Put the comma-separated arrows inside backticks, use `parent -> child` for each arrow, and use `none` when there are no arrows. The two lists should match.

- **DAG edges.** `A -> M, M -> Y, A -> Y`
- **Structural parents.** `A -> M, M -> Y, A -> Y`

### Document generation and truth

- **Generation.** Define all variables and write the full structural equations or conditional sampling distributions. Include noise distributions, dependence, timing and the level of each draw where relevant. Report how seeds are assigned, how many tables are generated and what each table contains. Provide a small run a reviewer can reproduce with a pinned code version or environment.
- **Equation table.** Use one table with columns **Symbol**, **Meaning**, and **Definition or setting**. Include every variable, index, function and parameter used in the equations. Write out functions such as the propensity and the arm means $\mu_0(x)$ and $\mu_1(x)$, with shareable numerical coefficients substituted. Give shareable fixed values or scenario grids for other parameters and explain their source or calibration. For a randomly drawn parameter, give its distribution, numerical hyperparameters, support and any truncation. State the draw level, which units share a draw, and dependencies on other parameters or disturbances.
- **Truth.** Tie the reference value to the exact estimand and scenario. Show an analytical calculation or give a reproducible numerical procedure. For Monte Carlo truth, document draw size and precision and check that approximation error is small enough for the proposed comparison.
- **Comparison.** Use the same observed inputs and replicate tables across methods. Point-estimation tasks can use bias and RMSE. If methods return intervals, state the nominal level and report empirical coverage and interval length across replicates. Explain exclusions and report failures alongside the metrics.

For example, a scenario grid can fix $c$ at $0$ or $0.5$ throughout each scenario. For a random coefficient, draw $\beta_t \sim \operatorname{Beta}(2,5)$ on $(0,1)$ once per table $t$, independently across tables and of the row-level disturbances. All rows in a table use that table's draw.

Public teaching examples can link authorized code and settings. Cite settings reported in a source paper and label them separately from the settings used for your run. For protected evaluation candidates, use named parameters for protected values in the complete equations. Give the full generator, exact run settings and seeds, official test tables, and scenario-specific truths to maintainers through the agreed private channel.

## 3. Copy the Markdown template

Copy the block into `website/data-submissions/simulated-dgp/submissions/<slug>.md`. Use a lowercase, hyphenated slug, keep the seven section headings in order and replace all placeholders. The same text is available as [TEMPLATE.md](TEMPLATE.md).

### Declare the domain and describe the target

Under **Research question**, declare one **Primary domain** using an ID below. Choose the domain that best represents the main evaluation task, considering its target, identification framework and observed-data design. If several areas apply, explain your choice in **Question and intended use**.

| Domain ID | Research area |
| --- | --- |
| `ate` | Average Treatment Effect |
| `cate` | Conditional Average Treatment Effect |
| `mediation` | Causal Mediation Analysis |
| `iv` | Instrumental Variables |
| `proximal` | Proximal Causal Inference |
| `did` | Difference-in-Differences |
| `synthetic_control` | Synthetic Control |
| `nonparametric_regression` | Nonparametric Regression |
| `quantile` | Quantile Inference |
| `semi_supervised` | Semi-Supervised Inference |
| `missing_data` | Missing Data |

Use the standard IDs where possible. A reviewer can clarify missing or unfamiliar domain names in PR comments; update the proposal with the agreed ID. The format check does not validate domain values or keywords, require these fields, or issue metadata warnings.

**Keywords** are optional: list short mechanism features separated by semicolons, such as `Nonlinearity; Effect heterogeneity`. Include features supported by the proposal; leave the field blank when unspecified.

In **Motivation and references**, link each source using its title where possible. A DOI, publisher page, preprint page or official source page is suitable. Identify distinct sources separately.

Begin **Estimand** with a name such as `ATE`, `ATT`, `CATE`, `LATE`, `NIE` or `NDE`, followed by the complete mathematical definition. These examples are not an exhaustive list. Keep the DGP-specific formulas in the proposal.

Continue adding or updating one file directly under `submissions/`; no domain subdirectory is required.

```markdown
# [TODO: Case title]

## Research question

- **Primary domain.**
<!-- Copy one domain ID from the guide. Leave blank if you need reviewer help. -->
- **Keywords.**
<!-- Optional: short mechanism features separated by semicolons, such as Nonlinearity; Effect heterogeneity. -->
- **Question and intended use.** [TODO: State the statistical question and whether this is a teaching example or a candidate for evaluation.]
- **Behavior under test.** [TODO: Explain the scientific or statistical behavior methods should recover, and why it matters.]

## Study design and data source

- **Motivation and references.** [TODO: Cite and link to the study, data or methodological work that motivates the setting. Describe which design choices come from the reference and which you introduce.]
- **Population and sampling.** [TODO: Define the units, sampling design, dependence and sample sizes or ranges that can be shared.]

## DAG and identification

- **Variables and causal structure.** [TODO: Map observed and latent variables to their roles and available columns. Use `X` for covariates or confounders, with named or indexed variants as needed. Label diagram nodes with the variable and a short meaning such as `A (treatment)` or `X_latent (unobserved confounder)`. Keep disturbances in the equations and state the scenario represented by any diagram.]
- **DAG edges.** `[TODO: List comma-separated arrows for the substantive variables, for example A -> M, M -> Y, A -> Y. Use none for an empty graph.]`
- **Assumptions.** [TODO: State the assumptions that identify the target or explain which assumption the stress test deliberately violates.]

## Variables and data-generating process

- **Variables and observed input.** [TODO: Define each generated or fixed variable, its support or units, whether it is observed or latent, and its role. Specify the table grain and columns given to each estimator.]
- **Draw order and scenarios.** [TODO: State the sampling order, the level of each draw (such as unit, cluster or time period), and what varies or stays fixed across scenarios.]

### Structural equations

- **Structural parents.** `[TODO: List parent -> child arrows among substantive variables implied by the equations. Match the DAG edges and describe any scenario-specific changes.]`

[TODO: Write the complete mathematical equations or conditional sampling distributions in draw order. Include deterministic transformations, link functions, disturbances and dependencies. Use $\epsilon$ for disturbances, with subscripts where needed.]

| Symbol | Meaning | Definition or setting |
| --- | --- | --- |
| [TODO: each variable and index] | [Role, units or indexing level] | [Map to columns or give a sampling law and its dependencies.] |
| [TODO: each function, such as $\mu_0$ or $\mu_1$] | [What it represents] | [Write the explicit formula with shareable numeric coefficients substituted.] |
| [TODO: each parameter] | [What it controls] | [Give the shareable fixed value or scenario grid, or the draw law, numerical hyperparameters, support or truncation, level, sharing and dependencies. State its source or calibration and identify the run setting.] |

[TODO: Add rows until every variable, index, function and parameter referenced in the equations is covered. Use named parameters for protected values and supply their exact settings through private review.]

## Data-generating process and estimand

- **Estimand.** [TODO: Begin with the estimand name and acronym where applicable (for example ATE, ATT, CATE, LATE, NIE or NDE), then give its complete mathematical definition. Define the contrast, scale, population and time horizon where relevant.]
- **Truth check.** [TODO: Describe the analytical, numerical or Monte Carlo calculation reviewers can use to verify the reference value. Keep protected case-specific values and settings in private review.]

## Benchmark comparison

- **Output and comparator.** [TODO: State the expected outputs and a baseline or comparison method with the same observable inputs.]
- **Scoring and replication.** [TODO: State the metrics, how replicate tables and scenarios are aggregated, and how failed or missing runs are counted.]

## Materials and access

- **Public materials.** [TODO: Link approved sources, code, documentation or teaching materials and state their sharing terms.]
- **Reproduction and protected materials.** [TODO: State how a reviewer can rerun one check. Name any full generator, configs, seeds, generated tables or truth calculations reserved for private review.]
```

## 4. Check and open the pull request

1. Create a branch from `main` in your fork of the [StatArena repository](https://github.com/Statsinference/Statistical-Intelligence-Arena). If you have write access, you can create the branch in StatArena directly. Add the single Markdown proposal.
2. Check that the generation recipe reproduces the table schema and that the reference calculation produces the intended target. Check the sharing terms of any materials you link or include.
3. Run the format check from the repository root. Replace `your-design` with your file's slug.

   ```bash
   python website/scripts/check_data_contribution.py --track simulated-dgp --local-file website/data-submissions/simulated-dgp/submissions/your-design.md
   ```

   If the domain is undecided, leave its field blank rather than inserting a TODO placeholder.

4. [Open a pull request](https://github.com/Statsinference/Statistical-Intelligence-Arena/compare) to `main` using the [Simulated DGP PR template](../../../.github/PULL_REQUEST_TEMPLATE/simulated-dgp.md). Fill in the causal design preview below. Use the same PR for revisions. A reviewer checks the design, the truth calculation and reproducibility. Evaluation inclusion is a separate curator decision.

### Preview the causal design in the pull request

Copy the PR template into the description, or replace `your-branch` with your branch name in this GitHub comparison URL.

```text
https://github.com/Statsinference/Statistical-Intelligence-Arena/compare/main...your-branch?template=simulated-dgp.md
```

Under `## Causal design preview`, complete both subsections.

- **DAG.** Put one fenced `mermaid` block under `### DAG`. For a three-node triangle, use `block-beta` with `columns 3`. Put the baseline covariate or mediator in the upper center and `A` and `Y` on the bottom row. Use `space` for empty cells and `space:3` for an empty row. Enter the causal arrows one per line, matching both edge lists in the case. Include `X --> A` only if the design makes treatment depend on `X`.
- **Larger DAGs.** Use `flowchart LR` or `graph LR`, with `TD`, `TB`, `RL` or `BT` as alternatives to `LR`. Use a line such as `X["X (covariate)"] --> Y["Y (outcome)"]` or `X --> Y` for each edge. Use standalone declarations for isolated nodes. Omit subgraphs and chained arrows. Explain scenario-specific omissions in the case file and show the union in the PR preview when arrows vary.
- **Structural equations.** Under `### Structural equations`, put the case file's display-math blocks first, in the same order. Follow them with one table containing the same definitions, explicit functions, shareable values and draw rules. Group related symbols in one row when their meanings and settings remain clear. GitHub renders both fenced `math` and `$$` blocks. Keep any protected parameter values symbolic in both places.

[Mermaid block diagrams](https://mermaid.js.org/syntax/block.html) · [GitHub mathematical expressions](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions)

The precheck compares the DAG arrows and equation blocks with the case file. To run this check locally, save the PR description as a Markdown file and add `--pr-body-file path/to/pr-description.md` to the command above.

## Worked public example

The childhood-trauma example models a methylation profile and derives the joint indirect effect on cortisol reactivity. It includes a shareable causal diagram, the inputs given to methods and an independently checkable reference calculation. [Read the example](EXAMPLE.md)

[All contribution tracks](../README.md) · [Reviewer checklist](../REVIEWING.md)

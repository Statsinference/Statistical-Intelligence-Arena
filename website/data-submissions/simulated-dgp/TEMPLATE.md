# [TODO: Case title]

## Research question

- **Question and intended use.** [TODO: State the statistical question and whether this is a teaching example or a candidate for evaluation.]
- **Behavior under test.** [TODO: Explain the scientific or statistical behavior methods should recover, and why it matters.]

## Study design and data source

- **Motivation and references.** [TODO: Cite the study, data or methodological work that motivates the setting. Describe which design choices come from the reference and which you introduce.]
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

- **Estimand.** [TODO: Define the contrast, scale, population and time horizon where relevant.]
- **Truth check.** [TODO: Describe the analytical, numerical or Monte Carlo calculation reviewers can use to verify the reference value. Keep protected case-specific values and settings in private review.]

## Benchmark comparison

- **Output and comparator.** [TODO: State the expected outputs and a baseline or comparison method with the same observable inputs.]
- **Scoring and replication.** [TODO: State the metrics, how replicate tables and scenarios are aggregated, and how failed or missing runs are counted.]

## Materials and access

- **Public materials.** [TODO: Link approved sources, code, documentation or teaching materials and state their sharing terms.]
- **Reproduction and protected materials.** [TODO: State how a reviewer can rerun one check. Name any full generator, configs, seeds, generated tables or truth calculations reserved for private review.]

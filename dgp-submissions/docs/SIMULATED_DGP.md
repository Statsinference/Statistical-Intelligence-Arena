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
| Research question | The statistical target, intended use and behavior under test. Explain why this question is worth adding to the benchmark. |
| Study design and data source | The population or setting, unit of observation, relevant references and which settings are calibrated or introduced. Include the sampling structure and proposed table sizes. |
| DAG and identification | Observed and latent variable roles, time ordering and identification assumptions. Use a DAG or describe who causes what. Document any intentional violations. |
| Variables and data-generating process | The table schema, full structural equations, sampling order and scenario settings. Follow the [DAG and structural equation instructions](../../website/data-submissions/simulated-dgp/README.md#match-the-dag-to-the-equations). |
| Data-generating process and estimand | The treatment or contrast, estimand and its units, and how the truth can be checked. |
| Benchmark comparison | Expected outputs, a baseline, shared inputs and scoring. Specify the number of attempted replicates, scenario weighting if relevant, and the treatment of failures. |
| Materials and access | Shareable references and reproducibility instructions. For official evaluation candidates, identify the files available for private review. |

### Document generation and truth

- **Generation.** Record the order of draws, distributions, structural equations, parameter constraints, scenario grid and dependencies. Report how seeds are assigned, how many tables are generated and what each table contains. Provide a small run a reviewer can reproduce with a pinned code version or environment.
- **Equation table.** In one table, define each variable, index, function and parameter in the equations. Give explicit formulas for the arm means and any other named functions, substituting shareable coefficients. Explain fixed settings, scenario grids and random draws, and identify the settings used in the run. [Equation table guidance](../../website/data-submissions/simulated-dgp/README.md#document-generation-and-truth)
- **Truth.** Tie the reference value to the exact estimand and scenario. Show an analytical calculation or give a reproducible numerical procedure. For Monte Carlo truth, document draw size and precision and check that approximation error is small enough for the proposed comparison.
- **Comparison.** Use the same observed inputs and replicate tables across methods. Point-estimation tasks can use bias and RMSE. If methods return intervals, state the nominal level and report empirical coverage and interval length across replicates. Explain exclusions and report failures alongside the metrics.

Public teaching examples can link authorized code and settings. Summaries for protected evaluation candidates can describe the design family and variables. Give the full generator, exact parameters and seeds, official test tables, and scenario-specific truths to maintainers through the agreed private channel.

## 3. Copy the Markdown template

Copy the [current Markdown template](../../website/data-submissions/simulated-dgp/TEMPLATE.md) to `website/data-submissions/simulated-dgp/submissions/<slug>.md`. Use a lowercase, hyphenated slug, keep the section headings in order and replace all placeholders.

## 4. Check and open the pull request

1. Create a branch from `main` in the [private StatArena repository](https://github.com/Statsinference/Statistical-Intelligence-Arena). Add the single Markdown proposal.
2. Check that the generation recipe reproduces the table schema and that the reference calculation produces the intended target. Check the sharing terms of any materials you link or include.
3. Run the format check from the repository root. Replace `your-design` with your file's slug.

   ```bash
   python website/scripts/check_data_contribution.py --track simulated-dgp --local-file website/data-submissions/simulated-dgp/submissions/your-design.md
   ```

4. [Open a pull request](https://github.com/Statsinference/Statistical-Intelligence-Arena/compare) to `main` using the [Simulated DGP PR template](../../.github/PULL_REQUEST_TEMPLATE/simulated-dgp.md). Follow the [preview instructions](../../website/data-submissions/simulated-dgp/README.md#preview-the-causal-design-in-the-pull-request) to show the DAG and every structural equation in the PR description. Use the same PR for revisions. A reviewer checks the design, the truth calculation and reproducibility. Evaluation inclusion is a separate curator decision.

## Worked public example

The childhood-trauma example models a methylation profile and derives the joint indirect effect on cortisol reactivity. It includes a shareable causal diagram, the inputs given to methods and an independently checkable reference calculation. [Read the example](../../website/data-submissions/simulated-dgp/EXAMPLE.md)

[All contribution tracks](../README.md) · [Reviewer checklist](../../website/data-submissions/REVIEWING.md)

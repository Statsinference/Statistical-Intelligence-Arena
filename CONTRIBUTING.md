# Contribute to StatArena

## Contribute a Method

Submit a statistical method or model for evaluation on a supported StatArena task.

1. **Test locally.** Use [StatArena Lite](lite/README.md) to run your method on public data and check its results.
2. **Submit for evaluation.** Follow the [method submission guide](method-submissions/README.md) to provide your method link, choose a research domain, and submit the completed Markdown checklist. The StatArena team reviews submissions and evaluates eligible methods for the official leaderboard.

## Contribute Data

Choose the guide that fits your contribution. Each guide includes a template, a filled example and instructions for submitting a pull request.

| Contribution | What to submit |
|---|---|
| [Simulated DGP](dgp-submissions/docs/SIMULATED_DGP.md) | A data-generating process with a scientific motivation, a defined estimand, a verifiable reference value and enough detail to reproduce the simulation. |
| [Real-data problem](dgp-submissions/docs/REAL_DATA_PROBLEM.md) | A causal question, a documented dataset or access route, and a plan for comparing estimates. Include a reference estimate when one is available. |

### Submit a proposal

Choose one track and open a pull request with one completed Markdown proposal in the website repository. The track guides include the template, a filled example and the corresponding submission path.

Use your proposal to share the research question, estimand and references. If a simulation is intended for official evaluation or the data have restricted access, arrange private review of the full materials with a maintainer. The worked examples illustrate the submission format.

### Existing benchmark documentation

The DGP collection service does not change the benchmark protocol, website, or starter code. See the [project README](README.md), [scientific requirements](docs/contribution_en.md), and [starter](starter/README.md).

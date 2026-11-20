# Contribute a simulated DGP

Propose a reproducible simulation that represents a documented study setting or isolates a feature that matters for causal inference.

## What to include

- **Motivation and references.** Describe the study setting or statistical challenge, with a paper or data source where available. Explain why the simulated relationships, effect sizes, sample sizes and overlap are plausible for that setting.
- **Design and identification.** Describe the variables, their roles, what methods can observe, and the assumptions that identify the target. Include a DAG or an arrow list when useful. Use a shareable schematic if the exact design is reserved for evaluation.
- **Estimand and reference value.** Define the causal target, its population and units. State how reviewers can verify the truth, for example with a closed form or an independent Monte Carlo calculation with a precision check.
- **Reproducibility and evaluation.** Explain how reviewers would reproduce the generation and compare methods using the same inputs and metrics. For a public example, include sufficient details on sampling DGPs and parameters, table dimensions and counts, seeds and validation to rerun it. Candidate official test designs are reviewed with full materials through a private channel arranged by a maintainer.

## Open a pull request

Use the [simulation template](https://github.com/Statsinference/statsinference.github.io/blob/5e174c855669b16bef0a459e1b8587fdec892e56/data-submissions/simulated-dgp/TEMPLATE.md) and the [filled childhood trauma, DNA methylation and cortisol example](https://github.com/Statsinference/statsinference.github.io/blob/5e174c855669b16bef0a459e1b8587fdec892e56/data-submissions/simulated-dgp/EXAMPLE.md). Put one completed Markdown file under `data-submissions/simulated-dgp/submissions/` in your fork and open a PR against [the website repository's main branch](https://github.com/Statsinference/statsinference.github.io/tree/main). A maintainer assigns a reviewer after the format check.

Use a public summary for a protected design. Share official test tables, full generators, exact parameter settings and seeds, and case-specific truths only through the private channel agreed with a maintainer.

[Back to Contribute data](../README.md)

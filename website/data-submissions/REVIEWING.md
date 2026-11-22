# Review a StatArena data contribution

## Assign and review

1. A maintainer checks the PR scope and the **Website data contribution precheck** result, then requests a GitHub review from someone familiar with the domain and design. Add a reproducibility reviewer when the design or access procedure warrants it.
2. The reviewer checks the items below and uses **Request changes** for actionable revisions or **Approve** when satisfied. Ask the author to revise the same PR.
3. A maintainer checks sharing permissions before merging. The merged proposal records the contribution in the private repository. Track inclusion and leaderboard release require a separate evaluation decision.

## Scientific and reproducibility checklist

- **Target.** Is the population or design, estimand, comparison and output clear?
- **Evidence.** Does the citation or source support the claimed setting? Do the time ordering, observed variables and assumptions support the proposed analysis? Does any real-data DAG agree with the study design?
- **DAG and equations.** For simulations, check the directed edges among substantive variables, including shared latent parents and scenario-specific changes. Verify that the PR preview shows the declared arrows and the complete structural equations from the case file.
- **Simulation.** Are all variables defined, and do the structural equations specify every draw, transformation and dependency? Can the reviewer generate at least one table from a known configuration and check the estimand and reference value? Is each empirical calibration or design choice documented?
- **Equation table.** Check that the table covers each referenced variable, index, function and parameter. Verify that nuisance functions and arm means have explicit formulas with shareable coefficients substituted. Check fixed settings or scenario grids and their provenance. Identify the published settings and the settings used in the run. For random parameters, verify the distributions, hyperparameter values, support or truncation, draw level, sharing and dependencies. Review protected run settings through the agreed channel.
- **Real data.** Can the reviewer follow the access and preparation process and verify variable roles? When a DAG is included, check that its labels describe the study variables and match the column mapping in the case file. If a reference estimate is supplied, does it match the target, sample and analysis scale? Are its uncertainty and limitations reported?
- **Benchmark.** Is the proposed comparison feasible with the documented input and output? Does the proposed metric match what repeated simulated draws or a real study can establish?
- **Sharing.** Are the public summary and links authorized for release? Keep protected materials in the agreed private review channel. Check exact evaluation seeds, parameter files and case-specific truths there.

Treat the automated check as structural feedback. Scientific accuracy, access terms and confidentiality require human verification. Review contributed code in an isolated environment without credentials or protected evaluation files.

For an existing PR whose Case file retains source notation, list its one-to-one symbol substitutions under `## Causal design preview` before the DAG. For example, write `**Case file notation.**` followed by one inline code span containing `U -> X, U_i -> X_i, u -> x`. List each changed equation token, including its index when the token has one. Omit a legacy noise node only when it is an independent source with one child, and explain this in the preview.

[Submission guide](README.md)

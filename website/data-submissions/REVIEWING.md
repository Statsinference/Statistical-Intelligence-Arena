# Review a StatArena data contribution

## Assign and review

1. A maintainer checks the PR scope and the **Website data contribution precheck** result, then requests a GitHub review from someone familiar with the domain and design. Add a reproducibility reviewer when the design or access procedure warrants it.
2. The reviewer checks the items below and uses **Request changes** for actionable revisions or **Approve** when satisfied. Ask the author to revise the same PR.
3. A maintainer checks sharing permissions before merging. The merged proposal records the contribution in the private repository. Track inclusion and leaderboard release require a separate evaluation decision.

## Scientific and reproducibility checklist

- **Domain (simulated DGP).** Check the primary domain against the main task and identification design. Resolve missing, unfamiliar or conflicting declarations with the author in PR comments and ask them to update the same proposal. The format check does not validate domain metadata.
- **Metadata (simulated DGP).** Check that source links identify the cited materials, any supplied keywords describe the mechanism, and the estimand name agrees with its full definition. Help clarify formula-first targets without treating the name as a new format gate.
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

## Refresh the simulated DGP proposal lists

The [Simulated DGP proposal catalog workflow](../../.github/workflows/simulated-dgp-catalog.yml) regenerates `simulated-dgp/by-domain/` when proposals or catalog inputs change on `main`. It can also be run manually on `main` from the Actions tab.

After tests pass, the bot commits changes only under `simulated-dgp/by-domain/` to the dedicated `submissions/simulated-dgp-catalog` branch, then creates or updates one catalog PR targeting `main`. A reviewer checks and approves the PR, then a maintainer with merge permission merges it manually once all required reviews and checks are satisfied. The bot does not approve its own PR or bypass branch rules. New changes may dismiss previous approvals under the repository rules.

If the lists already match `main`, no commit is created and any outstanding catalog PR is closed as obsolete. If the review branch already contains the generated result, it is reused without another commit. Missing metadata stays visible in the generated lists and workflow summary. Changes confined to the generated directory do not trigger another catalog run. Correct metadata in the source proposals or generator, and reserve the bot branch for generated updates.

Before enabling this workflow, allow GitHub Actions to create pull requests under **Settings → Actions → General → Workflow permissions** (the setting is named **Allow GitHub Actions to create and approve pull requests**). Organization policy must also permit these settings. The job requests `contents: write` and `pull-requests: write` using the repository's `GITHUB_TOKEN`; no personal token or branch-rule exemption is needed for this PR flow. These settings must be configured separately from the workflow file.

The workflow does not push directly to `main` or force-push the review branch. If `main` or the review branch changes during preparation, or GitHub rejects a push or PR creation, the run fails. Check the error and rerun on the latest `main`. The workflow summary links to the catalog PR for review and manual merging. If GitHub displays an **Approve workflows to run** prompt on the bot-created PR, a maintainer must approve those runs separately from the PR review, and any required checks must finish before merging.

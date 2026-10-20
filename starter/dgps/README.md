# DGP catalog template

Protocol v0.3, 2026-10-18. **No sourced DGP is registered yet.** catalog.csv intentionally contains only its fixed header. The illustrative mediation card is not a claimed classical-paper reproduction.

## One row per versioned mechanism specification

Use the exact columns in catalog.csv. Quote CSV cells containing commas or newlines. Put long equations/configurations in versioned relative files and reference their paths.

| Column | Required meaning |
| --- | --- |
| dgp_id | Stable identifier, unique within the catalog. |
| family | Exactly one of ate, cate, mediation, iv, proximal, did_sc. |
| citation | Verified primary paper/repository citation and URL, or explicit original_illustrative/no_external_source_claimed. |
| source_locator | Page, equation, section or versioned source-code location; not only a paper title. |
| original_equations | Source equations or a path to a faithful transcription. |
| adaptation | Every changed variable, equation, distribution, estimand or parameter range; none only after comparison. |
| parameter_config | Relative config/card path with concrete fixed values or a fully specified allowed parameterization. |
| truth_definition | Mathematical target, population, conditioning query/group and units. |
| truth_method | Analytic derivation or numerical method with integration/MC error and independent verification. |
| sampling_unit | Independent experiment unit; state cluster/panel/query dependence where relevant. |
| version | Immutable DGP version linked to source and implementation commits/hashes when available. |
| license | Source/data/code rights and attribution; unknown remains pending, not permission. |
| split_tags | Declared public_train/public_dev/heldout_mechanism/heldout_parameter/public_smoke roles. |
| status | planned, specified, implemented or reviewed; no implementation is supplied now. |
| source_relation | exact_reproduction, adapted_from_source or original_illustrative. |
| notes | Exposure, limitations, branch (DiD or synthetic_control), and reviewer disposition. |

## Scientific review before generation

1. Reconcile the source equations, declared adaptations and target.
2. Check a fixed configuration independently, including analytic truth where possible.
3. Declare which quantities stay fixed across repeated datasets and which are redrawn.
4. Record boundary conditions: overlap, support, identification and weak-identification regimes.
5. Freeze public development and evaluation-only partitions before model selection.

A published classical DGP is not automatically an unseen benchmark. New seeds only yield new draws from a mechanism. Hold out mechanisms or parameter regions explicitly, disclose known pretraining exposure, and retain a custody record for evaluation truths.

For did_sc, use a branch field (did or synthetic_control) in the referenced card/config. DiD parallel trends/no anticipation and synthetic-control donor/pre-post/counterfactual assumptions require separate statements.

## Current illustrative card

[cards/mediation_illustrative.md](cards/mediation_illustrative.md) contains a toy linear structural model and analytic target derivation. It has no asserted original-paper citation, no selected parameter grid and no runnable generator. Before treating it as a submission, complete the missing design, source relation, independent checks, implementations and rights.

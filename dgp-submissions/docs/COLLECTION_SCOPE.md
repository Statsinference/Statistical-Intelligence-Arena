# DGP collection scope and input isolation

The DGP registry is a literature collection, not a promise that every current
benchmark method or CI evaluator supports every registered mechanism.

## Accepted research areas

The original six causal areas remain unchanged: `ate`, `cate`, `mediation`,
`iv`, `proximal`, `did_sc`. Four additional collection areas are available:

| Primary `family` | Problem | Additional information to describe in the source mechanism |
|---|---|---|
| `nonparametric_regression` | Nonparametric regression | Design distribution, regression function, errors and query points |
| `quantile` | Quantile inference | Outcome distribution, quantile level, conditional versus marginal target and query |
| `semi_supervised` | Semi-supervised inference | Labeled/unlabeled sample sizes, observation or label-selection rule, common versus shifted populations |
| `missing_data` | Missing data | Full-data mechanism, missingness indicators and conditional law, observed output and target |

Aliases include `nri`, `qr`, `qdi`, `quantile_regression`, `ssi`, `ssl`, and
`missing_data_inference`. Unknown families remain in Needs classification;
the parser does not classify from the filename or guess a statistical target.
The original benchmark's task contracts remain unchanged.

## High dimensionality and interference are allowed

**Neither high dimensionality nor interference is a reason to reject a DGP.**
They are properties, not mutually exclusive research areas. A source may have
`properties.high_dimensional: true` or `properties.interference: true`.
Do not change these to false merely to pass a test or fit an example.

For a high-dimensional mechanism, retain the specified covariate dimension p,
active/effective dimension or sparsity where defined, covariance, coefficient
construction and actual sample-size regime. Do not reduce p or add independent
noise features and claim the result is the original source DGP. Document any
adaptation explicitly. No universal numeric cutoff is imposed by the registry.

For interference, retain the network/group structure (fixed or randomly
generated), treatment assignment, how other units' treatments affect the
response, and the unit of sampling. Exposure mappings are one possible
representation, not a mandatory way to formulate every interference model.
An interference DGP must not be described as having no interference merely
because a baseline estimator assumes it. Collection does not imply that iid
inference or an existing estimator is appropriate.

Statistical targets need not be causal ATE/NDE/LATE targets. Describe the actual
target in `estimand.definition`. An unavailable exact scalar truth remains
unknown; it is not fabricated. Existing source ZIPs and scientific definitions
are preserved.

## Isolated failure handling

A malformed ZIP is reported without blocking subsequent valid ZIPs. Within a
structurally safe ZIP, a malformed DGP is reported without discarding valid
siblings. Unsafe archive paths, duplicate members or decompression-limit
violations reject the whole archive; safety checks are not bypassed.

See [the processing report](../registry/INTAKE_REPORT.md) for every failed source
and reason. A workflow can succeed with `partial_success_needs_attention`;
this means valid inputs were published, **not** that failed inputs passed.
Fix and recommit only the affected source. Other students need not resubmit.

If a replacement breaks an earlier successfully indexed source, its last valid
record and generator are retained and explicitly marked stale. Registry output
is built in a staging directory so internal errors do not erase the published
catalog. The last-valid copy is not validation of the latest ZIP.

Regression tests use a frozen corpus from the migration commit plus synthetic
edge cases. Live submissions are processed in a separate step; tests do not
require all future DGPs to share the initial corpus's low dimensionality or
no-interference assumptions. Scientific review is still required.

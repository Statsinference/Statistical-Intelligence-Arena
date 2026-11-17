# Estimand and contribution records needing review

This list is based on the current submitted records; no independent paper verification is implied. Every extracted DGP remains subject to scientific review.

## Target names or target details requiring review

| Record | Submitted target | Issue |
|---|---|---|
| [iv-ye-2024-genius-heteroskedastic-v1](drafts/iv-ye-2024-genius-heteroskedastic-v1.md) | β0=.4 | Conflicting duplicate submission ID; reconcile source before applying this label. |
| [iv-ye-2024-genius-heteroskedastic-v1-conflict-8dd1770580](drafts/iv-ye-2024-genius-heteroskedastic-v1-conflict-8dd1770580.md) | beta | Conflicting duplicate submission ID; reconcile source before applying this label. |
| [proximal-shi-2026-sc-gaussian-v1](drafts/proximal-shi-2026-sc-gaussian-v1.md) | ETT | The submitted label says ETT while its displayed definition lacks treated-population conditioning; resolve against source before labeling. |
| [cate-athey-2019-heterogeneity-confounding-v1](drafts/cate-athey-2019-heterogeneity-confounding-v1.md) | tau(x0) = E[Y(1) - Y(0) \| X = x0] | The estimand is labeled CATE but the submitted page does not specify the query covariate point associated with the stated numeric value. |

## Potential duplicate quantile records

The following pairs have matching displayed mechanisms, estimands, scenarios, and truth in the current registry. Their exported generator files also have matching SHA-256 hashes within each pair. Some metadata differs, so compare submitted archives, provenance, and author intent before merging or removing anything.

| Pair | Records |
|---|---|
| qdi-bondell-reich-wang-2010-linear-scale | [qdi-bondell-reich-wang-2010-linear-scale-v1](drafts/qdi-bondell-reich-wang-2010-linear-scale-v1.md) · [qdi-bondell-reich-wang-2010-linear-scale-v2](drafts/qdi-bondell-reich-wang-2010-linear-scale-v2.md) |
| qdi-bondell-reich-wang-2010-sine-location | [qdi-bondell-reich-wang-2010-sine-location-v1](drafts/qdi-bondell-reich-wang-2010-sine-location-v1.md) · [qdi-bondell-reich-wang-2010-sine-location-v2](drafts/qdi-bondell-reich-wang-2010-sine-location-v2.md) |
| qdi-bondell-reich-wang-2010-sine-scale | [qdi-bondell-reich-wang-2010-sine-scale-v1](drafts/qdi-bondell-reich-wang-2010-sine-scale-v1.md) · [qdi-bondell-reich-wang-2010-sine-scale-v2](drafts/qdi-bondell-reich-wang-2010-sine-scale-v2.md) |
| qdi-dette-volgushev-2008-exponential-scale | [qdi-dette-volgushev-2008-exponential-scale-v1](drafts/qdi-dette-volgushev-2008-exponential-scale-v1.md) · [qdi-dette-volgushev-2008-exponential-scale-v2](drafts/qdi-dette-volgushev-2008-exponential-scale-v2.md) |
| qdi-hall-yao-2005-additive-sine | [qdi-hall-yao-2005-additive-sine-v1](drafts/qdi-hall-yao-2005-additive-sine-v1.md) · [qdi-hall-yao-2005-additive-sine-v2](drafts/qdi-hall-yao-2005-additive-sine-v2.md) |
| qdi-hall-yao-2005-gaussian-index | [qdi-hall-yao-2005-gaussian-index-v1](drafts/qdi-hall-yao-2005-gaussian-index-v1.md) · [qdi-hall-yao-2005-gaussian-index-v2](drafts/qdi-hall-yao-2005-gaussian-index-v2.md) |
| qdi-li-liu-zhu-2007-exponential-surface | [qdi-li-liu-zhu-2007-exponential-surface-v1](drafts/qdi-li-liu-zhu-2007-exponential-surface-v1.md) · [qdi-li-liu-zhu-2007-exponential-surface-v2](drafts/qdi-li-liu-zhu-2007-exponential-surface-v2.md) |
| qdi-li-liu-zhu-2007-sinc | [qdi-li-liu-zhu-2007-sinc-v1](drafts/qdi-li-liu-zhu-2007-sinc-v1.md) · [qdi-li-liu-zhu-2007-sinc-v2](drafts/qdi-li-liu-zhu-2007-sinc-v2.md) |

## ZIP submissions awaiting scientific and intake review

The following five submissions are not currently indexed because their `collection.json` does not contain the required `equations` list. Their submitted `card.md` and `model.py` contain mechanism information, but the source, target and adaptations still need to be checked before preparing corrected metadata. The original ZIPs have not been altered or executed.

| Submission | Review focus |
|---|---|
| [did-qin-zhang-2008-bounded-panel-v1.zip](../incoming/did-qin-zhang-2008-bounded-panel-v1.zip) | Reconcile equations and two outcome variants with the submitted card and implementation. |
| [did-ye-2024-iid-common-trend-v1.zip](../incoming/did-ye-2024-iid-common-trend-v1.zip) | Reconcile group assignments, treatment and outcome equations with the submitted implementation. |
| [did-zhou-2026-mixture-mean-v1.zip](../incoming/did-zhou-2026-mixture-mean-v1.zip) | Check the adaptation from the original distributional target to a scalar ATT. |
| [did-zhou-2026-network-weight-v1.zip](../incoming/did-zhou-2026-network-weight-v1.zip) | Check the network construction and scalar ATT adaptation against the source. |
| [did-zhou-2026-truncated-mean-v1.zip](../incoming/did-zhou-2026-truncated-mean-v1.zip) | Check the truncated-normal mean and scalar ATT adaptation against the source. |

## Cross-cutting scientific review

- Verify each equation and target definition against the relevant paper and source code, including differences in adapted DGPs.
- Verify all target values, scenario-specific query points, and source citations; reported numeric values are not automatically validated.
- Treat keyword and latent-variable metadata as provisional; absence is not evidence of absence.

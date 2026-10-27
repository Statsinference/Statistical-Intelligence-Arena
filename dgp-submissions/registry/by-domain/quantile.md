# Quantile Inference

**3 submitted DGP mechanism(s) · draft / unverified.**

| Paper Title | DGP mechanism | Keywords | Estimand & truth (per scenario) | Review status | Generator.py |
|---|---|---|---|---|---|
| Generalized random forests (AoS) | [Conditional quantile under Athey-Tibshirani-Wager Figure 2 mean shift](../drafts/qr-athey-tibshirani-wager-2019-mean-v1.md) | Nonlinearity | source_p40_q90_positive_query: theta = Q_0.9(Y \| X=x_query) = 2.0815515655446006 | Needs review | [generator.py](../generators/qr-athey-tibshirani-wager-2019-mean-v1.py) |
| Generalized random forests (AoS) | [Conditional quantile under Athey-Tibshirani-Wager Figure 2 scale shift](../drafts/qr-athey-tibshirani-wager-2019-scale-v1.md) | Nonlinearity · Heteroskedasticity | source_p40_q90_positive_query: theta = Q_0.9(Y \| X=x_query) = 2.5631031310892016 | Needs review | [generator.py](../generators/qr-athey-tibshirani-wager-2019-scale-v1.py) |
| High-Dimensional Quantile Regression: Convolution Smoothing and Concave Regularization (JRSSB) | [QDI: active-coordinate Gaussian-mixture marginal of the Tan-Wang-Zhou design (10-dimensional adaptation)](../drafts/qdi-tan-wang-zhou-20220201-active10-mixture-v2.md) | Linearity | q50-active10-mixture: theta_tau = Q_tau(Y \| W = e1) = 1.7999999999997158; q90-active10-mixture: theta_tau = Q_tau(Y \| W = e1) = 4.2114834571051345 | Needs review | [generator.py](../generators/qdi-tan-wang-zhou-20220201-active10-mixture-v2.py) |

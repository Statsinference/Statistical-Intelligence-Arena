"""Observed-data reconstruction of Zhou (2022) Section 5 / Supplementary Material F.

Exports only (X1,X2,X3,X4,A,M1,M2,Y).  The latent errors U1,U2,U3 and the latent
covariate-outcome confounder UXY are generated internally and never returned, so no
oracle, counterfactual or latent column can reach a learner.
"""
import numpy as np


def _validate(config):
    beta_x = config["beta_X"]
    if len(beta_x) != 4 or any(len(row) != 4 for row in beta_x):
        raise ValueError("beta_X must be a 4x4 coefficient matrix (four covariates on four latent errors)")
    sizes = {"beta_A": 5, "beta_M1": 6, "beta_M2": 7, "beta_Y": 9}
    for key, length in sizes.items():
        values = config[key]
        if len(values) != length or not all(np.isfinite(float(v)) for v in values):
            raise ValueError(f"{key} must contain {length} finite coefficients")
    if not all(np.isfinite(np.asarray(beta_x, dtype=float)).all() for _ in (0,)):
        raise ValueError("beta_X must be finite")
    for key in ("x_sd", "m1_sd", "m2_sd", "y_sd"):
        value = float(config[key])
        if not np.isfinite(value) or value <= 0:
            raise ValueError(f"{key} must be a finite positive standard deviation")


def generate(config, n, seed):
    _validate(config)
    if isinstance(n, bool) or not isinstance(n, int) or n < 1:
        raise ValueError("n must be a positive integer")
    rng = np.random.Generator(np.random.PCG64(seed))
    beta_x = np.asarray(config["beta_X"], dtype=float)
    b_a = np.asarray(config["beta_A"], dtype=float)
    b_m1 = np.asarray(config["beta_M1"], dtype=float)
    b_m2 = np.asarray(config["beta_M2"], dtype=float)
    b_y = np.asarray(config["beta_Y"], dtype=float)

    # Latent exogenous errors; U[:, 3] is UXY, the covariate-outcome confounder.
    u = rng.standard_normal((n, 4))
    x = u @ beta_x.T + float(config["x_sd"]) * rng.standard_normal((n, 4))

    ones = np.ones(n)
    logit_a = np.column_stack([ones, x]) @ b_a
    p_a = 1.0 / (1.0 + np.exp(-logit_a))
    a = (rng.random(n) < p_a).astype(float)

    mean_m1 = np.column_stack([ones, x, a]) @ b_m1
    m1 = mean_m1 + float(config["m1_sd"]) * rng.standard_normal(n)

    mean_m2 = np.column_stack([ones, x, a, m1]) @ b_m2
    m2 = mean_m2 + float(config["m2_sd"]) * rng.standard_normal(n)

    mean_y = np.column_stack([ones, u[:, 3], x, a, m1, m2]) @ b_y
    y = mean_y + float(config["y_sd"]) * rng.standard_normal(n)

    return {
        "X1": x[:, 0].tolist(), "X2": x[:, 1].tolist(),
        "X3": x[:, 2].tolist(), "X4": x[:, 3].tolist(),
        "A": [int(v) for v in a], "M1": m1.tolist(), "M2": m2.tolist(), "Y": y.tolist(),
    }

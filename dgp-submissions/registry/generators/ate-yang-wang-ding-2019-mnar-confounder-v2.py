"""Section 5.3 equation-based synthetic reconstruction with unresolved source issues documented."""
import math
import numpy as np


def expit(x):
    """Stable vector logistic transform."""
    x = np.asarray(x, dtype=float)
    out = np.empty_like(x)
    positive = x >= 0
    out[positive] = 1.0 / (1.0 + np.exp(-x[positive]))
    e = np.exp(x[~positive])
    out[~positive] = e / (1.0 + e)
    return out


def validate(config):
    for key in ("x1_sd", "x2_sd", "x5_noise_sd", "potential_outcome_noise_sd"):
        value = float(config[key])
        if not math.isfinite(value) or value <= 0:
            raise ValueError(f"{key} must be finite and positive")
    for key in ("x3_bernoulli_probability", "x4_bernoulli_probability"):
        value = float(config[key])
        if not 0 <= value <= 1:
            raise ValueError(f"{key} must be in [0,1]")
    for key in ("beta0", "beta1"):
        if len(config[key]) != 7 or not all(math.isfinite(float(v)) for v in config[key]):
            raise ValueError(f"{key} must contain seven finite entries (intercept plus six slopes)")
    if len(config["alpha"]) != 7 or len(config["eta"]) != 8:
        raise ValueError("alpha and eta lengths must match the source equation dimensions")
    if not all(math.isfinite(float(v)) for v in config["alpha"] + config["eta"]):
        raise ValueError("alpha and eta must be finite")


def generate(config, n, seed):
    validate(config)
    if isinstance(n, bool) or not isinstance(n, int) or n < 1:
        raise ValueError("n must be a positive integer")
    rng = np.random.default_rng(seed)

    # X1 and X2 are generated independently as an explicit joint-factorization adaptation.
    x1 = rng.normal(float(config["x1_mean"]), float(config["x1_sd"]), n)
    x2 = rng.normal(float(config["x2_mean"]), float(config["x2_sd"]), n)
    b3 = rng.binomial(1, float(config["x3_bernoulli_probability"]), n)
    b4 = rng.binomial(1, float(config["x4_bernoulli_probability"]), n)
    x3 = (b3 - 0.5) / 0.5
    x4 = (b4 - 0.5) / 0.5
    eps5 = rng.normal(0.0, float(config["x5_noise_sd"]), n)
    x5 = x1 + x2 + x3 + x4 + eps5
    p6 = expit(float(config["x6_logit_intercept"]) + float(config["x6_logit_x5"]) * x5)
    x6 = rng.binomial(1, p6)

    X = np.column_stack((x1, x2, x3, x4, x5, x6))
    design_y = np.column_stack((np.ones(n), X))
    beta0 = np.asarray(config["beta0"], dtype=float)
    beta1 = np.asarray(config["beta1"], dtype=float)
    sd_y = float(config["potential_outcome_noise_sd"])
    eps0 = rng.normal(0.0, sd_y, n)
    eps1 = rng.normal(0.0, sd_y, n)
    y0 = design_y @ beta0 + eps0
    y1 = design_y @ beta1 + eps1

    # Treatment assignment uses alpha=(intercept, six X slopes).
    eta_a = np.asarray(config["alpha"], dtype=float)[0] + X @ np.asarray(config["alpha"], dtype=float)[1:]
    a = rng.binomial(1, expit(eta_a))
    y = np.where(a == 1, y1, y0)

    # The printed Section 5.3 uses 'logit(p_pattern)' before RHSs that themselves
    # form a valid multinomial vector. This candidate explicitly interprets RHSs
    # as probabilities and records the ambiguity in collection.json/card.md.
    eta_r = np.asarray(config["eta"], dtype=float)
    q = eta_r[0] + eta_r[1] * a + X @ eta_r[2:]
    u = expit(q)
    p11 = (1.0 - u) / (1.0 + 2.0 * u)
    p_other = u / (1.0 + 2.0 * u)
    if np.any(p11 < 0) or np.any(p_other < 0) or not np.allclose(p11 + 3 * p_other, 1.0, atol=2e-15, rtol=0):
        raise FloatingPointError("Missing-pattern probabilities failed normalization")
    v = rng.random(n)
    cut1 = p11
    cut2 = p11 + p_other
    cut3 = p11 + 2.0 * p_other
    # Pattern order is (11), (10), (01), (00).
    r5 = np.where(v < cut1, 1, np.where(v < cut2, 1, np.where(v < cut3, 0, 0)))
    r6 = np.where(v < cut1, 1, np.where(v < cut2, 0, np.where(v < cut3, 1, 0)))

    # Numeric table interface: sentinel 0.0 plus explicit masks, not imputation.
    x5_obs = np.where(r5 == 1, x5, 0.0)
    x6_obs = np.where(r6 == 1, x6, 0.0)
    return {
        "X1": x1.tolist(), "X2": x2.tolist(), "X3": x3.tolist(), "X4": x4.tolist(),
        "X5": x5_obs.tolist(), "X6": x6_obs.astype(float).tolist(), "A": a.astype(int).tolist(),
        "Y": y.tolist(), "R5": r5.astype(int).tolist(), "R6": r6.astype(int).tolist()
    }

"""Observed-data generator for Yang, Wang & Ding (2019), Section 5.2."""
import math
import numpy as np


def _expit(x):
    """Numerically stable logistic function, operating on NumPy arrays."""
    x = np.asarray(x, dtype=float)
    out = np.empty_like(x)
    pos = x >= 0
    out[pos] = 1.0 / (1.0 + np.exp(-x[pos]))
    ex = np.exp(x[~pos])
    out[~pos] = ex / (1.0 + ex)
    return out


def _validate(config, n):
    if isinstance(n, bool) or not isinstance(n, int) or n < 1:
        raise ValueError("n must be a positive integer")
    required = {
        "x1_mean", "x1_variance", "x2_probability",
        "y0_intercept", "y0_x1", "y0_x2", "y1_intercept", "y1_x1", "y1_x2",
        "error_variance", "treatment_intercept", "treatment_x1", "treatment_x2",
        "missing_intercept", "missing_x1", "missing_a", "missing_a_x2"
    }
    missing = required.difference(config)
    if missing:
        raise ValueError("Missing config keys: " + ", ".join(sorted(missing)))
    if not math.isfinite(float(config["x1_variance"])) or config["x1_variance"] <= 0:
        raise ValueError("x1_variance must be finite and positive")
    if not math.isfinite(float(config["error_variance"])) or config["error_variance"] <= 0:
        raise ValueError("error_variance must be finite and positive")
    if not 0 <= float(config["x2_probability"]) <= 1:
        raise ValueError("x2_probability must lie in [0,1]")
    for key in required:
        if not math.isfinite(float(config[key])):
            raise ValueError(f"{key} must be finite")


def generate(config, n, seed):
    """Return observed numeric columns only; missing X1 uses sentinel 0 when R1=0.

    The R1 column disambiguates the sentinel from an actual observed X1 value of zero.
    Potential outcomes, errors, treatment probabilities and true effects are never returned.
    """
    _validate(config, n)
    rng = np.random.default_rng(seed)

    # Step 1: full-data baseline covariates.
    x1 = rng.normal(
        loc=float(config["x1_mean"]),
        scale=math.sqrt(float(config["x1_variance"])),
        size=n,
    )
    x2 = rng.binomial(1, float(config["x2_probability"]), size=n).astype(int)

    # Step 2: independently generated potential-outcome errors. The source gives
    # their marginal laws but not every cross-independence relation in Section 5.2.
    error_sd = math.sqrt(float(config["error_variance"]))
    eps0 = rng.normal(0.0, error_sd, size=n)
    eps1 = rng.normal(0.0, error_sd, size=n)
    y0 = (
        float(config["y0_intercept"])
        + float(config["y0_x1"]) * x1
        + float(config["y0_x2"]) * x2
        + eps0
    )
    y1 = (
        float(config["y1_intercept"])
        + float(config["y1_x1"]) * x1
        + float(config["y1_x2"]) * x2
        + eps1
    )

    # Step 3: treatment assignment as specified in Section 5.2.
    eta_a = (
        float(config["treatment_intercept"])
        + float(config["treatment_x1"]) * x1
        + float(config["treatment_x2"]) * x2
    )
    a = rng.binomial(1, _expit(eta_a), size=n).astype(int)
    y = np.where(a == 1, y1, y0)

    # Step 4: missingness depends on full X1, treatment A, and X2.
    eta_r = (
        float(config["missing_intercept"])
        + float(config["missing_x1"]) * x1
        + float(config["missing_a"]) * a
        + float(config["missing_a_x2"]) * a * x2
    )
    r1 = rng.binomial(1, _expit(eta_r), size=n).astype(int)

    # Step 5: finite numeric encoding for the collection interface. R1=0 denotes
    # that X1 is missing; its exported value is then a sentinel, not an imputation.
    x1_export = x1.copy()
    x1_export[r1 == 0] = 0.0

    return {
        "X1": x1_export.astype(float).tolist(),
        "X2": x2.tolist(),
        "A": a.tolist(),
        "Y": y.astype(float).tolist(),
        "R1": r1.tolist(),
    }

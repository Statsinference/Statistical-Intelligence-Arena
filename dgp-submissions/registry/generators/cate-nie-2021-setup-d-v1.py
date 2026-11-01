"""CATE data-generating mechanism: Nie–Wager (2021) Setup D: unrelated treatment and control surfaces

Source: Nie & Wager (2021), Biometrika 108(2), Section 6.1, Setup D, PDF p.16
Observed columns only (X1, X2, X3, X4, X5, A, Y); no potential-outcome, oracle nuisance or truth
column is exported.  Population truth lives in truth.py.

Mechanism family: nie-wager-2021-setup-d
"""
import math

import numpy as np


def validate(config):
    """Reject configurations outside the declared support."""
    for key in ("tau_scale", "noise_scale"):
        if key not in config:
            raise ValueError("config is missing " + key)
        if not math.isfinite(float(config[key])):
            raise ValueError(key + " must be finite")
    if float(config["noise_scale"]) <= 0.0:
        raise ValueError("noise_scale must be positive")
    if float(config["tau_scale"]) < 0.0:
        raise ValueError("tau_scale must be nonnegative")


def generate(config, n, seed):
    validate(config)
    if isinstance(n, bool) or not isinstance(n, int) or n < 1:
        raise ValueError("n must be a positive integer")
    rng = np.random.default_rng(seed)
    tau_scale = float(config["tau_scale"])
    noise_scale = float(config["noise_scale"])

    # ---- 1. baseline covariates, in the sampling order of the source ----
    X1 = rng.normal(0.0, 1.0, n)
    X2 = rng.normal(0.0, 1.0, n)
    X3 = rng.normal(0.0, 1.0, n)
    X4 = rng.normal(0.0, 1.0, n)
    X5 = rng.normal(0.0, 1.0, n)

    # ---- 2. treatment assignment sum-of-exp propensity e(X) = 1/(1 + exp(-X1) + exp(-X2)) ----
    e = 1.0 / (1.0 + np.exp(-X1) + np.exp(-X2))
    A = (rng.random(n) < e).astype(int)

    # ---- 3. outcome mechanism ----
    pos = np.maximum(X1 + X2 + X3, 0.0)
    neg = np.maximum(X4 + X5, 0.0)
    b = 0.5 * (pos + neg)
    tau = (pos - neg) * tau_scale
    noise = rng.normal(0.0, noise_scale, n)
    Y = b + (A - 0.5) * tau + noise

    return {
        "X1": X1.tolist(),
        "X2": X2.tolist(),
        "X3": X3.tolist(),
        "X4": X4.tolist(),
        "X5": X5.tolist(),
        "A": A.tolist(),
        "Y": Y.tolist(),
    }

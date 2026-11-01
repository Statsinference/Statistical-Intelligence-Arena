"""CATE data-generating mechanism: Lei–Candès (2021) simulation: zero control outcome with a double-sigmoid effect

Source: Lei & Candès (2021), JRSS-B 83(5), Section 3.6, PDF p.10
Observed columns only (X1, X2, X3, X4, X5, X6, X7, X8, X9, X10, A, Y); no potential-outcome, oracle nuisance or truth
column is exported.  Population truth lives in truth.py.

Mechanism family: lei-candes-2021-double-sigmoid
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
    X1 = rng.uniform(0.0, 1.0, n)
    X2 = rng.uniform(0.0, 1.0, n)
    X3 = rng.uniform(0.0, 1.0, n)
    X4 = rng.uniform(0.0, 1.0, n)
    X5 = rng.uniform(0.0, 1.0, n)
    X6 = rng.uniform(0.0, 1.0, n)
    X7 = rng.uniform(0.0, 1.0, n)
    X8 = rng.uniform(0.0, 1.0, n)
    X9 = rng.uniform(0.0, 1.0, n)
    X10 = rng.uniform(0.0, 1.0, n)

    # ---- 2. treatment assignment beta-cdf propensity e(X) = (1/4)(1 + F_{2,4}(X1)), so e lies in [0.25, 0.5] ----
    u = X1
    F = (10.0 * u ** 2 * (1.0 - u) ** 3 + 10.0 * u ** 3 * (1.0 - u) ** 2 + 5.0 * u ** 4 * (1.0 - u) + u ** 5)
    e = 0.25 * (1.0 + F)
    A = (rng.random(n) < e).astype(int)

    # ---- 3. outcome mechanism ----
    f1 = 2.0 / (1.0 + np.exp(-12.0 * (X1 - 0.5)))
    f2 = 2.0 / (1.0 + np.exp(-12.0 * (X2 - 0.5)))
    tau = (f1 * f2) * tau_scale
    noise = rng.normal(0.0, noise_scale, n)
    Y = A * (tau + noise)

    return {
        "X1": X1.tolist(),
        "X2": X2.tolist(),
        "X3": X3.tolist(),
        "X4": X4.tolist(),
        "X5": X5.tolist(),
        "X6": X6.tolist(),
        "X7": X7.tolist(),
        "X8": X8.tolist(),
        "X9": X9.tolist(),
        "X10": X10.tolist(),
        "A": A.tolist(),
        "Y": Y.tolist(),
    }

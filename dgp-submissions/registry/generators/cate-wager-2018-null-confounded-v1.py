"""CATE data-generating mechanism: Wager–Athey (2018) simulation 1: zero treatment effect with a beta-density propensity

Source: Wager & Athey (2018), JASA 113(523), Section 5.1, Eq (27), PDF p.20
Observed columns only (X1, X2, X3, X4, X5, A, Y); no potential-outcome, oracle nuisance or truth
column is exported.  Population truth lives in truth.py.

Mechanism family: wager-athey-2018-null-confounding
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

    # ---- 2. treatment assignment logit-free beta density: e(X) = 0.25 (1 + beta_{2,4}(X1)), so e in [0.25, 0.777] ----
    e = 0.25 * (1.0 + 20.0 * X1 * (1.0 - X1) ** 3)
    A = (rng.random(n) < e).astype(int)

    # ---- 3. outcome mechanism ----
    mu0 = 2.0 * X1 - 1.0
    tau = (0.0) * tau_scale
    noise = rng.normal(0.0, noise_scale, n)
    Y = mu0 + A * tau + noise

    return {
        "X1": X1.tolist(),
        "X2": X2.tolist(),
        "X3": X3.tolist(),
        "X4": X4.tolist(),
        "X5": X5.tolist(),
        "A": A.tolist(),
        "Y": Y.tolist(),
    }

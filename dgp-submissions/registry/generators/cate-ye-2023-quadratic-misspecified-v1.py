"""CATE data-generating mechanism: Ye-Shao-Yi-Zhao (2023) setting 2: quadratic-in-U effect with a misspecified working model

Source: Ye, Shao, Yi & Zhao (2023), JASA 118(544), Section 4.1, Eq (21), PDF p.24
Observed columns only (U, W, A, Y); no potential-outcome, oracle nuisance or truth
column is exported.  Population truth lives in truth.py.

Mechanism family: ye-2023-quadratic-misspecified
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
    U = rng.normal(0.0, 1.0, n)
    W = rng.normal(0.0, 1.0, n)

    # ---- 2. treatment assignment simple randomisation with two arms at 1:1, e(X) = 0.5 ----
    e = np.full(n, 0.5)
    A = (rng.random(n) < e).astype(int)

    # ---- 3. outcome mechanism ----
    tau = (-1.3 - 0.5 * U - 0.01 * (U ** 2 - 1.0) + 0.3 * W) * tau_scale
    noise = rng.normal(0.0, noise_scale, n)
    Y = noise + A * tau

    return {
        "U": U.tolist(),
        "W": W.tolist(),
        "A": A.tolist(),
        "Y": Y.tolist(),
    }

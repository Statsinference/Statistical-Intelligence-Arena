"""Observed-only implementation of Nie--Wager Setup A (arXiv v4, pp. 15--16)."""
from __future__ import annotations

import math
from numbers import Real

import numpy as np


def validate_config(config: dict) -> None:
    """Reject silent schema changes and invalid parameters; never modify input."""
    required = {"dimension", "noise_sd", "propensity_trim", "effect_scale"}
    if not isinstance(config, dict) or set(config) != required:
        raise ValueError(f"config must contain exactly {sorted(required)}")
    if type(config["dimension"]) is not int or config["dimension"] != 6:
        raise ValueError("This contribution's fixed schema requires dimension=6")
    for name in required - {"dimension"}:
        value = config[name]
        if isinstance(value, bool) or not isinstance(value, Real) or not math.isfinite(value):
            raise ValueError(f"{name} must be a finite number")
    if config["noise_sd"] < 0:
        raise ValueError("noise_sd must be nonnegative")
    if not 0 < config["propensity_trim"] < 0.5:
        raise ValueError("propensity_trim must lie strictly between 0 and 0.5")


def generate(config: dict, n: int, seed: int) -> dict[str, list]:
    """Return X1,...,X6,A,Y; config is one scenario's parameter object.

    Local PCG64, row-major X draws, then treatment uniforms, then Gaussian noise.
    effect_scale=1 is the source design; other values support verification only.
    No population truth, propensity, response surface, noise, or effect is exported.
    """
    validate_config(config)
    if type(n) is not int or n < 1:
        raise ValueError("n must be a positive integer")
    if type(seed) is not int or seed < 0:
        raise ValueError("seed must be a nonnegative integer")
    rng = np.random.Generator(np.random.PCG64(seed))
    covariates = rng.uniform(0.0, 1.0, size=(n, config["dimension"]))
    x1, x2, x3, x4, x5 = covariates[:, :5].T
    sine_term = np.sin(np.pi * x1 * x2)
    baseline = sine_term + 2.0 * (x3 - 0.5) ** 2 + x4 + 0.5 * x5
    propensity = np.clip(sine_term, config["propensity_trim"], 1.0 - config["propensity_trim"])
    effect = config["effect_scale"] * (x1 + x2) / 2.0
    treatment = (rng.random(n) < propensity).astype(int)
    noise = rng.standard_normal(n)
    outcome = baseline + (treatment - 0.5) * effect + config["noise_sd"] * noise
    return {
        **{f"X{j + 1}": covariates[:, j].tolist() for j in range(config["dimension"])},
        "A": treatment.tolist(),
        "Y": outcome.tolist(),
    }

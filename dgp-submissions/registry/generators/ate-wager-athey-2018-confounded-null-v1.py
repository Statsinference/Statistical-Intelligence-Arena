"""Observed-only source mechanism. See card.md for exact paper/version/locator."""
from __future__ import annotations

import math
from numbers import Real

import numpy as np

DIMENSION = 5
MODE = 'null'


def validate_config(config: dict) -> None:
    required = {"dimension", "noise_sd", "effect_shift"} if MODE == "null" else {
        "dimension", "noise_sd", "effect_scale", "query_point"}
    if not isinstance(config, dict) or set(config) != required:
        raise ValueError(f"Expected exactly the keys {sorted(required)}")
    if type(config["dimension"]) is not int or config["dimension"] != DIMENSION:
        raise ValueError(f"This fixed schema requires dimension={DIMENSION}")
    for key in required - {"dimension", "query_point"}:
        value = config[key]
        if isinstance(value, bool) or not isinstance(value, Real) or not math.isfinite(value):
            raise ValueError(f"{key} must be a finite number")
    if config["noise_sd"] < 0:
        raise ValueError("noise_sd must be nonnegative")
    if MODE != "null":
        query = config["query_point"]
        if not isinstance(query, list) or len(query) != DIMENSION:
            raise ValueError("query_point must be a list of dimension coordinates")
        if any(isinstance(v, bool) or not isinstance(v, Real) or not math.isfinite(v)
               or not 0 <= v <= 1 for v in query):
            raise ValueError("query_point must be finite and in the covariate support")


def generate(config: dict, n: int, seed: int) -> dict[str, list]:
    """PCG64 draws: row-major X, assignment uniforms, then outcome errors.

    Only X,A,Y are returned. Query coordinates are target metadata, not sample
    features. Source settings use scale=1 or shift=0; changes support controls.
    """
    validate_config(config)
    if type(n) is not int or n < 1:
        raise ValueError("n must be a positive integer")
    if type(seed) is not int or seed < 0:
        raise ValueError("seed must be a nonnegative integer")
    rng = np.random.Generator(np.random.PCG64(seed))
    x = rng.uniform(0.0, 1.0, size=(n, DIMENSION))
    if MODE == "randomized":
        propensity, baseline = np.full(n, 0.5), np.zeros(n)
    else:
        confounder = x[:, 0 if MODE == "null" else 2]
        beta_density = 20.0 * confounder * (1.0 - confounder) ** 3
        propensity = (1.0 + beta_density) / 4.0
        baseline = 2.0 * confounder - 1.0
    if MODE == "null":
        effect = np.full(n, config["effect_shift"])
    else:
        response = 1.0 + 1.0 / (1.0 + np.exp(-20.0 * (x[:, :2] - 1.0 / 3.0)))
        effect = config["effect_scale"] * response[:, 0] * response[:, 1]
    treatment = (rng.random(n) < propensity).astype(int)
    outcome = baseline + (treatment - 0.5) * effect + config["noise_sd"] * rng.standard_normal(n)
    return {**{f"X{j+1}": x[:, j].tolist() for j in range(DIMENSION)},
            "A": treatment.tolist(), "Y": outcome.tolist()}

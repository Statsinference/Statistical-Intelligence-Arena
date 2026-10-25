"""Observed-only draws from GRF Figure 2 mean-shift design."""
from __future__ import annotations
import math
import numpy as np


def validate(config: dict) -> None:
    if config.get("dimension") != 40:
        raise ValueError("The registered source design requires dimension=40.")
    q = config.get("quantile")
    if not isinstance(q, (float, int)) or not math.isfinite(q) or not 0 < q < 1:
        raise ValueError("quantile must be finite and in (0,1).")
    x = config.get("x_query")
    if not isinstance(x, list) or len(x) != 40 or any(
            not isinstance(v, (int, float)) or not math.isfinite(v) or not -1 <= v <= 1 for v in x):
        raise ValueError("x_query must contain 40 finite coordinates in [-1,1].")
    shift = config.get("mean_shift")
    if not isinstance(shift, (int, float)) or not math.isfinite(shift):
        raise ValueError("Invalid mean_shift.")


def generate(config: dict, n: int, seed: int) -> dict:
    validate(config)
    if isinstance(n, bool) or not isinstance(n, int) or n < 1:
        raise ValueError("n must be a positive integer.")
    rng = np.random.Generator(np.random.PCG64(seed))
    x = rng.uniform(-1.0, 1.0, size=(n, 40))
    epsilon = rng.standard_normal(n)
    y = config["mean_shift"] * (x[:, 0] > 0) + epsilon
    observed = {f"X{j+1}": x[:, j].tolist() for j in range(40)}
    observed["Y"] = y.tolist()
    return observed

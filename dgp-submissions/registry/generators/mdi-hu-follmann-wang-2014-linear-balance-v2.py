"""Observed-data implementation of Hu, Follmann & Wang (2014), Section 4, simulation 1."""
import math
import random


def _expit(value):
    if value >= 0.0:
        return 1.0 / (1.0 + math.exp(-value))
    e = math.exp(value)
    return e / (1.0 + e)


def generate(config, n, seed):
    if isinstance(n, bool) or not isinstance(n, int) or n < 1:
        raise ValueError("n must be a positive integer")
    sx = float(config["covariate_sd"])
    sy = float(config["outcome_noise_sd"])
    b = [float(v) for v in config["outcome_coefficients"]]
    a = float(config["observation_logit_coefficient"])
    placeholder = float(config["missing_outcome_placeholder"])
    if not (math.isfinite(sx) and sx > 0.0 and math.isfinite(sy) and sy > 0.0):
        raise ValueError("standard deviations must be positive and finite")
    if len(b) != 2 or not all(math.isfinite(v) for v in b + [a, placeholder]):
        raise ValueError("invalid coefficients or placeholder")
    rng = random.Random(seed)
    result = {f"X{j}": [] for j in range(1, 11)}
    result["R"] = []
    result["Y_observed"] = []
    for _ in range(n):
        x = [rng.gauss(0.0, sx) for _ in range(10)]
        y = b[0] * x[0] + b[1] * x[1] + rng.gauss(0.0, sy)
        r = int(rng.random() < _expit(a * x[0]))
        for j, value in enumerate(x, start=1):
            result[f"X{j}"].append(value)
        result["R"].append(r)
        result["Y_observed"].append(y if r else placeholder)
    return result

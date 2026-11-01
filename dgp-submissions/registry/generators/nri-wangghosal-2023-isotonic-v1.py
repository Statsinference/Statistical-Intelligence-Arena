"""Observed-data generator for Wang and Ghosal (2023), Section 5.2: bivariate isotonic regression.

X1, X2 are independent Uniform(0, 1); Y = f_k(X1, X2) + epsilon with epsilon ~ Normal(0, sigma^2),
sigma = 1. Only observed columns X1, X2, Y are returned; no oracle, latent or noiseless column is
exported (the regression function value itself is never written into the returned table).
"""
import math
import random

SUPPORT_MIN = 0.0
SUPPORT_MAX = 1.0
SOURCE_CURVES = ("f1", "f2", "f3", "f4", "f5")


def validate(config):
    if not isinstance(config, dict):
        raise ValueError("config must be a parameter object")
    for key in ("curve", "noise_sd", "query_x1", "query_x2"):
        if key not in config:
            raise ValueError("missing config key: " + key)
    if config["curve"] not in SOURCE_CURVES:
        raise ValueError("curve must be one of " + ", ".join(SOURCE_CURVES))
    if not math.isfinite(float(config["noise_sd"])) or float(config["noise_sd"]) <= 0:
        raise ValueError("noise_sd must be finite and positive")
    for key in ("query_x1", "query_x2"):
        value = float(config[key])
        if not math.isfinite(value) or not SUPPORT_MIN <= value <= SUPPORT_MAX:
            raise ValueError("query coordinate must lie in [0, 1]: " + key)


def mean_function(curve, x1, x2):
    """Regression function f_k of Section 5.2, evaluated pointwise."""
    total = x1 + x2
    if curve == "f1":
        return total ** 2
    if curve == "f2":
        return math.sqrt(total)
    if curve == "f3":
        return x1 * x2
    if curve == "f4":
        return math.exp(total)
    if curve == "f5":
        return math.exp(x1 * x2)
    raise ValueError("unknown curve: " + str(curve))


def generate(config, n, seed):
    validate(config)
    if isinstance(n, bool) or not isinstance(n, int) or n < 1:
        raise ValueError("n must be a positive integer")
    curve = config["curve"]
    sd = float(config["noise_sd"])
    rng = random.Random(seed)
    x1_column, x2_column, y_column = [], [], []
    for _ in range(n):
        x1 = rng.random()
        x2 = rng.random()
        epsilon = rng.gauss(0.0, sd)
        x1_column.append(x1)
        x2_column.append(x2)
        y_column.append(mean_function(curve, x1, x2) + epsilon)
    return {"X1": x1_column, "X2": x2_column, "Y": y_column}

"""Observed-data generator for the Shang--Cheng Case (I) regression law."""
import math
import random


def _validate(config):
    sigma = float(config["sigma"])
    query_z = float(config["query_z"])
    weights = config["mixture_weights"]
    shapes = config["beta_shapes"]
    if not math.isfinite(sigma) or sigma <= 0.0:
        raise ValueError("sigma must be finite and positive")
    if not math.isfinite(query_z) or not 0.0 <= query_z <= 1.0:
        raise ValueError("query_z must lie in [0,1]")
    if len(weights) != 2 or not all(math.isfinite(float(w)) and float(w) >= 0.0 for w in weights):
        raise ValueError("mixture_weights must contain two finite nonnegative values")
    if abs(sum(float(w) for w in weights) - 1.0) > 1e-12:
        raise ValueError("mixture_weights must sum to one")
    if len(shapes) != 2 or any(
        len(pair) != 2 or not all(math.isfinite(float(v)) and float(v) > 0.0 for v in pair)
        for pair in shapes
    ):
        raise ValueError("beta_shapes must contain two positive finite shape pairs")


def _beta_density(z, a, b):
    if z <= 0.0 or z >= 1.0:
        return 0.0
    log_normalizer = math.lgamma(a + b) - math.lgamma(a) - math.lgamma(b)
    return math.exp(log_normalizer + (a - 1.0) * math.log(z) + (b - 1.0) * math.log1p(-z))


def _mean_function(config, z):
    return sum(
        float(weight) * _beta_density(z, float(shape[0]), float(shape[1]))
        for weight, shape in zip(config["mixture_weights"], config["beta_shapes"])
    )


def generate(config, n, seed):
    """Return the two observed columns, with no hidden function-value column."""
    _validate(config)
    if isinstance(n, bool) or not isinstance(n, int) or n < 1:
        raise ValueError("n must be a positive integer")
    rng = random.Random(seed)
    sigma = float(config["sigma"])
    out = {"Z": [], "Y": []}
    for _ in range(n):
        z = rng.random()
        y = _mean_function(config, z) + rng.gauss(0.0, sigma)
        out["Z"].append(z)
        out["Y"].append(y)
    return out

"""Yang--Tokdar arXiv v1, Sec.5.2: inverse-transform sampling, X,Y only."""
import math
import random


def validate(config):
    fixed = {"x_lower": -1.0, "x_upper": 1.0,
             "intercept_coefficient": 3.0, "slope_coefficient": 4.0,
             "quantile_center": 0.5}
    if config.get("x_distribution") != "uniform":
        raise ValueError("Only the source uniform predictor distribution is supported")
    for key, expected in fixed.items():
        value = config.get(key)
        if (isinstance(value, bool) or not isinstance(value, (int, float))
                or value != expected):
            raise ValueError(f"{key} must retain the source value {expected}")
    for key in ("query_x", "quantile_level"):
        value = config.get(key)
        if (isinstance(value, bool) or not isinstance(value, (int, float))
                or not math.isfinite(value)):
            raise ValueError(f"{key} must be a finite number")
    if not -1 <= config["query_x"] <= 1:
        raise ValueError("query_x must be in [-1,1]")
    if not 0 < config["quantile_level"] < 1:
        raise ValueError("quantile_level must be in (0,1)")


def quantile(u, x):
    """Source quantile, with a stable log expression and no tail clipping."""
    if not (0 < u < 1 and -1 <= x <= 1):
        raise ValueError("Quantile evaluation outside the source domain")
    t = u - 0.5
    log_factor = -math.log(u) - math.log1p(-u)
    return (3.0 * t + 4.0 * t * t * x) * log_factor


def generate(config, n, seed):
    validate(config)
    if isinstance(n, bool) or not isinstance(n, int) or n < 0:
        raise ValueError("n must be a nonnegative integer")
    if isinstance(seed, bool) or not isinstance(seed, int):
        raise ValueError("seed must be an integer")
    rng = random.Random(seed)
    out = {"X": [], "Y": []}
    for _ in range(n):
        x = -1.0 + 2.0 * rng.random()
        u = rng.random()
        # random() is in [0,1); reject possible zero rather than clamp it.
        while u == 0.0:
            u = rng.random()
        out["X"].append(x)
        out["Y"].append(quantile(u, x))
    return out

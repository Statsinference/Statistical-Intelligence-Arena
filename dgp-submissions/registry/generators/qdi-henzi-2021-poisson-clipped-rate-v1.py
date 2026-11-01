"""Published equation (26), JRSS-B 83(5), PDF p.19 / journal p.981.
Observable, unjittered X and Y; arXiv v3 p.19 is a historical locator.

Independent Python implementation. No author R code is executed or copied.
The only supported mechanism is the published fixed Uniform/Poisson law.
"""
import math
import random


def validate(config):
    expected = {"x_low": 0.0, "x_high": 10.0,
                "rate_floor": 1.0, "rate_cap": 6.0}
    for key, value in expected.items():
        actual = config[key]
        if isinstance(actual, bool) or not isinstance(actual, (int, float)):
            raise ValueError(f"{key} must be numeric")
        if actual != value:
            raise ValueError(f"{key} must equal the published value {value}")
    for key in ("query_x", "cdf_threshold"):
        value = config[key]
        if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value):
            raise ValueError(f"{key} must be finite numeric")
    if not 0 < config["query_x"] < 10:
        raise ValueError("query_x must lie inside (0,10)")
    if not -100 <= config["cdf_threshold"] <= 100:
        raise ValueError("This scalar oracle supports thresholds in [-100,100]")


def _rate(x, config):
    return min(max(x, config["rate_floor"]), config["rate_cap"])


def _poisson(rate, rng):
    # Product-of-uniforms algorithm: return k when the (k+1)th arrival
    # of a unit-rate Poisson process first exceeds the interval length rate.
    # Fixed source rates are in [1,6], so exp(-rate) cannot underflow.
    cutoff = math.exp(-rate)
    product, count = 1.0, 0
    while product > cutoff:
        product *= rng.random()
        count += 1
    return count - 1


def generate(config, n, seed):
    """Return exactly {'X': list[float], 'Y': list[int]}, each of length n."""
    validate(config)
    if isinstance(n, bool) or not isinstance(n, int) or n < 1:
        raise ValueError("n must be a positive integer")
    if isinstance(seed, bool) or not isinstance(seed, int):
        raise ValueError("seed must be an integer")
    rng = random.Random(seed)
    xs, ys = [], []
    for _ in range(n):
        # Reject the machine endpoint to honor the open source interval.
        u = rng.random()
        while u == 0.0:
            u = rng.random()
        x = config["x_low"] + (config["x_high"] - config["x_low"]) * u
        xs.append(x)
        ys.append(_poisson(_rate(x, config), rng))
    return {"X": xs, "Y": ys}

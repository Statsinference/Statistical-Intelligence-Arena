"""Observed-data generator for the monomial binary-regression DGP."""
import math
import random


def _validate(config):
    if not isinstance(config, dict):
        raise ValueError("config must be a scenario dictionary")
    s = config.get("s")
    x_star = config.get("x_star")
    if isinstance(s, bool) or not isinstance(s, (int, float)) or not math.isfinite(float(s)):
        raise ValueError("s must be finite numeric")
    if not 0.0 <= float(s) < 1.0:
        raise ValueError("s must lie in [0,1), excluding the undefined source endpoint s=1")
    if isinstance(x_star, bool) or not isinstance(x_star, (int, float)) or not math.isfinite(float(x_star)):
        raise ValueError("x_star must be finite numeric")
    if not 0.0 <= float(x_star) <= 1.0:
        raise ValueError("x_star must lie in [0,1]")


def generate(config, n, seed):
    """Return only the observed columns X and Y, each with length n."""
    _validate(config)
    if isinstance(n, bool) or not isinstance(n, int) or n < 1:
        raise ValueError("n must be a positive integer")
    rng = random.Random(seed)
    s = float(config["s"])
    exponent = 1.0 - s
    x_values = []
    y_values = []
    for _ in range(n):
        x = rng.random()
        probability = x ** exponent
        y = int(rng.random() < probability)
        x_values.append(x)
        y_values.append(y)
    return {"X": x_values, "Y": y_values}

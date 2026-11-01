"""Observed-data generator for the kink binary-regression DGP."""
import math
import random


def _validate(config):
    if not isinstance(config, dict):
        raise ValueError("config must be a scenario dictionary")
    s = config.get("s")
    x_star = config.get("x_star")
    if isinstance(s, bool) or not isinstance(s, (int, float)) or not math.isfinite(float(s)):
        raise ValueError("s must be finite numeric")
    if not 0.0 <= float(s) <= 1.0:
        raise ValueError("s must lie in the source grid [0,1]")
    if isinstance(x_star, bool) or not isinstance(x_star, (int, float)) or not math.isfinite(float(x_star)):
        raise ValueError("x_star must be finite numeric")
    if abs(float(x_star) - 0.5) > 1e-15:
        raise ValueError("this contribution fixes the NRI query at x_star=0.5")


def probability(x, s):
    """Piecewise-linear source kink with the declared s=1 endpoint convention."""
    if x <= 0.0:
        return 0.0
    if x >= 1.0:
        return 1.0
    a = 0.2 + 0.8 * s
    if s >= 1.0:
        return 1.0 if x >= 1.0 else 0.2 * x
    if x <= a:
        return 0.2 * x / a
    return 0.2 + 0.8 * (x - a) / (1.0 - a)


def generate(config, n, seed):
    """Return only observed columns X and Y, each with length n."""
    _validate(config)
    if isinstance(n, bool) or not isinstance(n, int) or n < 1:
        raise ValueError("n must be a positive integer")
    rng = random.Random(seed)
    s = float(config["s"])
    x_values = []
    y_values = []
    for _ in range(n):
        x = rng.random()
        y = int(rng.random() < probability(x, s))
        x_values.append(x)
        y_values.append(y)
    return {"X": x_values, "Y": y_values}

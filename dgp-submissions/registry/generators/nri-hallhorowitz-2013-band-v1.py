"""Observed columns X and Y only; the noise draw stays internal and is never exported."""
import math
import random

_FUNCTIONS = ("g1", "g2", "g3")


def sign(x):
    """Section 3 convention: sgn(x) = 1 if x > 0, 0 if x = 0, -1 if x < 0."""
    if x > 0.0:
        return 1.0
    if x < 0.0:
        return -1.0
    return 0.0


def normal_density(t):
    """phi(t) = exp(-t^2/2)/sqrt(2*pi), the standard normal density."""
    return math.exp(-t * t / 2.0) / math.sqrt(2.0 * math.pi)


def mean_function(name, x):
    """The three Section 3 regression functions, evaluated in closed form."""
    if name == "g1":
        return x + 5.0 * normal_density(10.0 * x)
    if name == "g2":
        return math.sin(3.0 * math.pi * x / 2.0) / (1.0 + 18.0 * x * x * (sign(x) + 1.0))
    if name == "g3":
        return math.sin(math.pi * x / 2.0) / (1.0 + 2.0 * x * x * (sign(x) + 1.0))
    raise ValueError("unknown mean function: " + repr(name))


def validate(config):
    if config.get("function") not in _FUNCTIONS:
        raise ValueError("function must be one of g1, g2, g3")
    sigma = float(config["sigma"])
    if not math.isfinite(sigma) or sigma <= 0.0:
        raise ValueError("sigma must be finite and strictly positive")
    low = float(config["support_min"])
    high = float(config["support_max"])
    if not (math.isfinite(low) and math.isfinite(high)) or high <= low:
        raise ValueError("support bounds must be finite with support_min < support_max")
    query = float(config["query_x"])
    if not math.isfinite(query) or not low < query < high:
        raise ValueError("query_x must be finite and strictly inside the declared support")


def generate(config, n, seed):
    if isinstance(n, bool) or not isinstance(n, int) or n < 1:
        raise ValueError("n must be a positive integer")
    validate(config)
    rng = random.Random(seed)
    name = config["function"]
    sigma = float(config["sigma"])
    low = float(config["support_min"])
    high = float(config["support_max"])
    columns = {"X": [], "Y": []}
    for _ in range(n):
        x = rng.uniform(low, high)
        y = mean_function(name, x) + rng.gauss(0.0, sigma)
        columns["X"].append(x)
        columns["Y"].append(y)
    return columns

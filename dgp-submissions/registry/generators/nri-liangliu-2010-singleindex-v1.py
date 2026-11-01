"""Observed-data generator for the Liang-Liu-Li-Tsai model (4.2) regression law."""
import math
import random


def _validate(config):
    sigma = float(config["sigma"])
    beta = float(config["beta"])
    lower = float(config["a"])
    upper = float(config["b"])
    weights = [float(w) for w in config["index_weights"]]
    query = [float(v) for v in config["query_z"]]
    query_x = float(config["query_x"])
    if not math.isfinite(sigma) or sigma <= 0.0:
        raise ValueError("sigma must be finite and positive")
    if not math.isfinite(beta):
        raise ValueError("beta must be finite")
    if not (math.isfinite(lower) and math.isfinite(upper) and lower < upper):
        raise ValueError("a and b must be finite with a < b")
    if len(weights) != 3 or not all(math.isfinite(w) for w in weights):
        raise ValueError("index_weights must contain three finite values")
    if abs(sum(w * w for w in weights) - 1.0) > 1e-9:
        raise ValueError("index_weights must have unit Euclidean norm")
    if len(query) != 3 or not all(math.isfinite(v) and 0.0 <= v <= 1.0 for v in query):
        raise ValueError("query_z must contain three values in [0,1]")
    if query_x not in (0.0, 1.0):
        raise ValueError("query_x must be 0 or 1")


def _link(t, lower, upper):
    """Source sine link eta(t), used on the full generated index support [0,sqrt(3)]."""
    return math.sin((t - lower) * math.pi / (upper - lower))


def generate(config, n, seed):
    """Return the five observed columns, with no hidden index or mean column."""
    _validate(config)
    if isinstance(n, bool) or not isinstance(n, int) or n < 1:
        raise ValueError("n must be a positive integer")
    rng = random.Random(seed)
    sigma = float(config["sigma"])
    beta = float(config["beta"])
    lower = float(config["a"])
    upper = float(config["b"])
    weights = [float(w) for w in config["index_weights"]]
    out = {"Z1": [], "Z2": [], "Z3": [], "X": [], "Y": []}
    for row_index in range(n):
        z1 = rng.random()
        z2 = rng.random()
        z3 = rng.random()
        x = float(row_index % 2)  # Source: odd 1-based row 0, even row 1.
        t = weights[0] * z1 + weights[1] * z2 + weights[2] * z3
        y = _link(t, lower, upper) + beta * x + sigma * rng.gauss(0.0, 1.0)
        out["Z1"].append(z1)
        out["Z2"].append(z2)
        out["Z3"].append(z3)
        out["X"].append(x)
        out["Y"].append(y)
    return out

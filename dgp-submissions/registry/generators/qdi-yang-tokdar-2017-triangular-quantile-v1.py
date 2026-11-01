"""Published JASA Figure 1 (journal p.1108) literal triangular mechanism.

Observed coordinates stay in the published coordinate system. No centering.
Both quantile terms use the same Gaussian rank, not mixture sampling.
"""
from fractions import Fraction
import math
import random


def _finite_numeric(value):
    if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value):
        raise ValueError("Expected a finite numeric configuration value")


def validate(config):
    expected = {
        "triangle_vertices": [[-1.0, 1.0], [-1.0, 2.0], [2.0, -1.0]],
        "normal_means": [0.0, 1.0], "normal_sds": [1.0, 0.2], "paper_n": 1000,
    }
    if set(config) != set(expected) | {"query_x", "query_x_exact", "quantile_level", "quantile_level_exact"}:
        raise ValueError("Unexpected or missing configuration field")
    def numeric_tree(value):
        if isinstance(value, list):
            for item in value:
                numeric_tree(item)
        else:
            _finite_numeric(value)
    for key, value in expected.items():
        numeric_tree(config[key])
        if config[key] != value:
            raise ValueError(key + ": only the published Figure 1 mechanism is supported")
    x, x_exact = config["query_x"], config["query_x_exact"]
    if not isinstance(x, list) or len(x) != 2 or not isinstance(x_exact, list) or len(x_exact) != 2:
        raise ValueError("query_x and query_x_exact need two coordinates")
    if not all(isinstance(v, str) for v in x_exact) or not isinstance(config["quantile_level_exact"], str):
        raise ValueError("Exact query entries must be rational strings")
    try:
        q = [Fraction(v) for v in x_exact]
        tau = Fraction(config["quantile_level_exact"])
    except (ValueError, ZeroDivisionError) as exc:
        raise ValueError("Malformed exact rational query") from exc
    for value, exact in zip(x, q):
        _finite_numeric(value)
        if value != float(exact):
            raise ValueError("Numeric query must agree with its exact rational definition")
    _finite_numeric(config["quantile_level"])
    if config["quantile_level"] != float(tau) or not 0 < tau < 1:
        raise ValueError("Quantile level must match exact value in (0,1)")
    x1, x2 = q
    # All THREE supporting half planes, evaluated exactly for the query.
    if x1 < -1 or 2*x1 + 3*x2 < 1 or x1 + x2 > 1:
        raise ValueError("Query is outside the published triangle")
    return q, tau


def generate(config, n, seed):
    """Return only X1, X2, Y as finite numeric lists of length n."""
    validate(config)
    if isinstance(n, bool) or not isinstance(n, int) or n < 1:
        raise ValueError("n must be a positive integer")
    if isinstance(seed, bool) or not isinstance(seed, int):
        raise ValueError("seed must be an integer")
    rng = random.Random(seed)
    a_vertex, b_vertex, c_vertex = config["triangle_vertices"]
    means, sds = config["normal_means"], config["normal_sds"]
    out = {"X1": [], "X2": [], "Y": []}
    for _ in range(n):
        u, v = rng.random(), rng.random()
        if u + v > 1.0:
            u, v = 1.0-u, 1.0-v
        x1, x2 = [a_vertex[j] + u*(b_vertex[j]-a_vertex[j])
                  + v*(c_vertex[j]-a_vertex[j]) for j in range(2)]
        s = x1 + x2
        a, b = (1.0-s)/3.0, (2.0+s)/3.0
        z = rng.gauss(0.0, 1.0)
        y = a*(means[0] + sds[0]*z) + b*(means[1] + sds[1]*z)
        for name, value in zip(out, (x1, x2, y)):
            out[name].append(value)
    return out

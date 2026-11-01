"""Hall, Wolff & Yao (1999), Section 3.1, Example 1: observed X,Y only."""
import math
import random


def validate(config):
    """Only the published mechanism is supported; verifier queries may vary."""
    fixed = {"amplitude": 2.0, "frequency": 3.1416,
             "x_distribution": "symmetric_triangular", "x_support": [-1.0, 1.0],
             "x_mode": 0.0, "noise_distribution": "symmetric_triangular",
             "noise_support": [-1.0, 1.0], "noise_mode": 0.0}
    for key, expected in fixed.items():
        if config.get(key) != expected:
            raise ValueError(f"{key} differs from the supported source mechanism")
    q = config["query"]
    for key in ("x", "y"):
        if isinstance(q[key], bool) or not isinstance(q[key], (int, float)) or not math.isfinite(q[key]):
            raise ValueError("Query coordinates must be finite numbers")
    if not -1.0 < q["x"] < 1.0:
        raise ValueError("Query x must be inside the positive-density support (-1,1)")


def generate(config, n, seed):
    """Return n iid observed pairs using a local RNG; no global RNG mutation."""
    validate(config)
    if isinstance(n, bool) or not isinstance(n, int) or n < 1:
        raise ValueError("n must be a positive integer")
    if isinstance(seed, bool) or not isinstance(seed, int):
        raise ValueError("seed must be an integer")
    rng = random.Random(seed)
    out = {"X": [], "Y": []}
    for _ in range(n):
        # Difference of independent U(0,1) draws has density 1-|u|.
        # Four separate draws per row also keep X independent of epsilon.
        x = rng.random() - rng.random()
        epsilon = rng.random() - rng.random()
        y = config["amplitude"] * math.sin(config["frequency"] * x) + epsilon
        out["X"].append(x)
        out["Y"].append(y)
    return out

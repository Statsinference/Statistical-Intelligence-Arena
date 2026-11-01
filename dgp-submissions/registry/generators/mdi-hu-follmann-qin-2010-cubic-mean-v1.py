"""Observed-data reconstruction of Section 4's first simulation."""
import math
import random

def expit(x):
    if x >= 0:
        return 1.0 / (1.0 + math.exp(-x))
    e = math.exp(x)
    return e / (1.0 + e)

def generate(config, n, seed):
    if isinstance(n, bool) or not isinstance(n, int) or n < 1:
        raise ValueError("n must be a positive integer")
    sx = float(config["covariate_sd"])
    sy = float(config["outcome_noise_sd"])
    c = [float(v) for v in config["observation_logit_coefficients"]]
    placeholder = float(config["missing_outcome_placeholder"])
    if not (math.isfinite(sx) and sx > 0 and math.isfinite(sy) and sy > 0):
        raise ValueError("standard deviations must be finite and positive")
    if len(c) != 3 or not all(map(math.isfinite, c)) or not math.isfinite(placeholder):
        raise ValueError("invalid observation coefficients or placeholder")
    rng = random.Random(seed)
    out = {key: [] for key in ("X1", "X2", "R", "Y_observed")}
    for _ in range(n):
        x1, x2 = rng.gauss(0, sx), rng.gauss(0, sx)
        y = (x1 + x2)**3 + rng.gauss(0, sy)
        r = int(rng.random() < expit(c[0] + c[1]*x1 + c[2]*x2*x2))
        out["X1"].append(x1)
        out["X2"].append(x2)
        out["R"].append(r)
        out["Y_observed"].append(y if r else placeholder)
    return out

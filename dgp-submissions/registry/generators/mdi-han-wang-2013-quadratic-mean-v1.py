"""Han and Wang (2013), Section 6, first model: observed data only."""
import math
import random

def expit(t):
    if t >= 0:
        return 1 / (1 + math.exp(-t))
    e = math.exp(t)
    return e / (1 + e)

def generate(config, n, seed):
    if isinstance(n, bool) or not isinstance(n, int) or n < 1:
        raise ValueError("n must be a positive integer")
    a = float(config["x_half_width"])
    mean = [float(v) for v in config["outcome_mean_coefficients"]]
    variance = [float(v) for v in config["outcome_variance_coefficients"]]
    logit = [float(v) for v in config["observation_logit_coefficients"]]
    placeholder = float(config["missing_outcome_placeholder"])
    if not (math.isfinite(a) and a > 0 and len(mean)==3 and len(variance)==2 and len(logit)==3
            and variance[0] > 0 and variance[1] >= 0
            and all(map(math.isfinite, mean+variance+logit+[placeholder]))):
        raise ValueError("invalid scenario")
    rng = random.Random(seed)
    out = {k: [] for k in ("X", "R", "Y_observed")}
    for _ in range(n):
        x = rng.uniform(-a,a)
        y = rng.gauss(mean[0]+mean[1]*x+mean[2]*x*x, math.sqrt(variance[0]+variance[1]*x*x))
        r = int(rng.random() < expit(logit[0]+logit[1]*x+logit[2]*x*x))
        out["X"].append(x)
        out["R"].append(r)
        out["Y_observed"].append(y if r else placeholder)
    return out

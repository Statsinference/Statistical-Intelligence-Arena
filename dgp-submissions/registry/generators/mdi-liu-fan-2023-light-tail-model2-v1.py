"""Liu and Fan (2023), Section 3, Example 1: gamma=2.5, c=1, Model 2."""
import math
import random

def generate(config, n, seed):
    if isinstance(n, bool) or not isinstance(n, int) or n < 1:
        raise ValueError("n must be a positive integer")
    gamma = float(config["gamma"])
    c = float(config["noise_scale_c"])
    df = config["chi_square_df"]
    placeholder = float(config["missing_outcome_placeholder"])
    if not (math.isfinite(gamma) and gamma>1 and math.isfinite(c) and c>=0
            and df==4 and config["model"]==2 and math.isfinite(placeholder)):
        raise ValueError("invalid scenario")
    rng = random.Random(seed)
    out = {k: [] for k in ("P", "D", "Y_observed")}
    for _ in range(n):
        p = rng.random()**(1/(gamma-1))
        eta = sum(rng.gauss(0,1)**2 for _ in range(df))
        y = 1-p+c*(eta-4)/math.sqrt(8)
        d = int(rng.random()<p)
        out["P"].append(p)
        out["D"].append(d)
        out["Y_observed"].append(y if d else placeholder)
    return out

import numpy as np

def _expit(x):
    x = np.asarray(x, dtype=float)
    out = np.empty_like(x)
    pos = x >= 0
    out[pos] = 1.0 / (1.0 + np.exp(-x[pos]))
    ex = np.exp(x[~pos])
    out[~pos] = ex / (1.0 + ex)
    return out

def generate(config, n, seed):
    if n < 1:
        raise ValueError("n must be positive")
    rng = np.random.default_rng(seed)
    w1 = rng.uniform(float(config["w1_low"]), float(config["w1_high"]), size=n)
    w2 = rng.binomial(1, float(config["w2_probability"]), size=n)
    lp_a = (float(config["treatment_intercept"]) + float(config["treatment_w1"])*w1 + float(config["treatment_w1w2"])*w1*w2)
    a = rng.binomial(1, _expit(lp_a))
    lp_y = (float(config["outcome_intercept"]) + float(config["outcome_treatment"])*a + float(config["outcome_w1"])*w1 + float(config["outcome_w1w2"])*w1*w2)
    y = rng.binomial(1, _expit(lp_y))
    return {"W1": w1.tolist(), "W2": w2.tolist(), "A": a.tolist(), "Y": y.tolist()}

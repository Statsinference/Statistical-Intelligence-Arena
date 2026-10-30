"""Independent reconstruction of Wang et al. (2021), additive Section 5 law."""
import numpy as np


def probabilities(x, config):
    x = np.asarray(x, dtype=float)
    a, b, e, g = (np.asarray(config[k], dtype=float) for k in ("alpha", "beta", "eta", "gamma"))
    delta = np.tanh(a[0] + a[1]*x)
    q = 1/(1+np.exp(-(b[0]+b[1]*x)))
    op = np.exp(e[0]+e[1]*x)
    pz = 1/(1+np.exp(-(g[0]+g[1]*x)))
    lo, hi = np.maximum(0., -delta), np.minimum(1., 1.-delta)
    # Strictly increasing product equation on the feasible interval.
    for _ in range(60):
        f0 = (lo+hi)/2
        f1 = f0+delta
        residual = f0*f1-op*(1-f0)*(1-f1)
        hi = np.where(residual > 0, f0, hi)
        lo = np.where(residual <= 0, f0, lo)
    f0 = (lo+hi)/2
    return q, pz, f0, f0+delta


def generate(config, n, seed):
    if not isinstance(n, (int, np.integer)) or n < 1:
        raise ValueError("n must be positive integer")
    rng = np.random.default_rng(seed)
    x = rng.uniform(-1., 1., n)
    q, pz, f0, f1 = probabilities(x, config)
    z = rng.binomial(1, pz)
    # CO probability q; AT probability (1-q)*q; remaining NT.
    u = rng.random(n)
    co = u < q
    at = (u >= q) & (u < q+(1-q)*q)
    d = np.where(co, z, at.astype(int))
    py = np.where(co, np.where(d == 1, f1, f0), q)
    y = rng.binomial(1, py)
    return {"X": x.tolist(), "Z": z.tolist(), "D": d.tolist(), "Y": y.tolist()}

"""Observed-data adaptation of Wang & Tchetgen Tchetgen (2018), Section 5."""
import numpy as np


SOURCE_CONFIG = {"alpha": [0.1, 0.5], "beta": [0.0, -0.5],
                 "gamma": [0.1, -0.5], "eta": [-0.5, 1.0],
                 "zeta": [0.0, -1.0], "kappa": 0.1}


def _validate(config):
    if config != SOURCE_CONFIG:
        raise ValueError("Only the audited Section 5 parameter setting is supported")


def baseline_probability(difference, odds_product):
    """Rationalized Eq.(6)/(7); continuous and stable at odds_product=1."""
    d, q = np.asarray(difference), np.asarray(odds_product)
    b = q * (2 - d) + d
    return 2 * q * (1 - d) / (b + np.sqrt(b*b + 4*q*(1-d)*(1-q)))


def conditional_probabilities(x, z, u, config):
    _validate(config)
    a, b, g, e, h = (config[k] for k in ("alpha", "beta", "gamma", "eta", "zeta"))
    delta = np.tanh(a[0] + a[1]*x)
    dd = np.tanh(b[0] + b[1]*x)
    pd = baseline_probability(dd, np.exp(e[0] + e[1]*x)) + z*dd + config["kappa"]*(2*u-1)
    py = baseline_probability(dd*delta, np.exp(h[0] + h[1]*x)) + z*dd*delta + config["kappa"]*(2*u-1)
    pz = 1 / (1 + np.exp(-g[0]-g[1]*x))
    return pz, pd, py


def generate(config, n, seed):
    _validate(config)
    if isinstance(n, bool) or not isinstance(n, int) or n < 0:
        raise ValueError("n must be a nonnegative integer")
    rng = np.random.default_rng(seed)
    x = rng.uniform(0.5, 1, n) * rng.choice([-1, 1], n)
    u = rng.binomial(1, 0.5, n)
    pz, _, _ = conditional_probabilities(x, 0, u, config)
    z = rng.binomial(1, pz)
    _, pd, py = conditional_probabilities(x, z, u, config)
    if np.any((pd < 0) | (pd > 1) | (py < 0) | (py > 1)):
        raise ValueError("Invalid conditional Bernoulli probability; never clipped")
    # Algebraic causal completion: independent D and Y potential-response uniforms.
    d = rng.binomial(1, pd)
    t = np.tanh(config["alpha"][0] + config["alpha"][1]*x)
    _, rd, ry = conditional_probabilities(x, 0, u, config)
    potential0 = ry - t*rd
    potential1 = potential0 + t
    if np.any((potential0 < 0) | (potential0 > 1) | (potential1 < 0) | (potential1 > 1)):
        raise ValueError("Invalid potential-outcome probability; never clipped")
    # One uniform couples Y(0),Y(1); only observed Y=Y(D) is emitted.
    vy = rng.uniform(size=n)
    y = (vy < potential0 + d*t).astype(int)
    return {"X2": x.tolist(), "Z": z.tolist(), "D": d.tolist(), "Y": y.tolist()}

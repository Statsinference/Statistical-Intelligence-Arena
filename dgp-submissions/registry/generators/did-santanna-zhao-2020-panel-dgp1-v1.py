"""Sant'Anna--Zhao (2020), Section 4.1 DGP1; one row per panel unit."""
import math
import numpy as np


# Population moments, NOT moments estimated from the generated sample.
# Var(Ztilde2) uses 120-node Gauss--Hermite integration of sigmoid(-N)^2.
MEAN = np.array([math.exp(0.125), 10.0, 0.21888, 402.0])
SD = np.sqrt([math.exp(0.5)-math.exp(0.25), 0.29337903585809294,
              0.0019832832, 3208.0])


def generate(config, n, seed):
    if config.get("dimension") != 4:
        raise ValueError("This source scenario has exactly four covariates")
    shift = float(config["att_shift"])
    if not math.isfinite(shift):
        raise ValueError("att_shift must be finite")
    rng = np.random.default_rng(seed)
    x = rng.standard_normal((n, 4))
    raw = np.column_stack((np.exp(x[:, 0]/2),
                           10+x[:, 1]*np.exp(-np.logaddexp(0, x[:, 0])),
                           (0.6+x[:, 0]*x[:, 2]/25)**3,
                           (20+x[:, 1]+x[:, 3])**2))
    z = (raw-MEAN)/SD
    f = 210+27.4*z[:, 0]+13.7*z[:, 1:].sum(axis=1)
    score = 0.75*(-z[:, 0]+0.5*z[:, 1]-0.25*z[:, 2]-0.1*z[:, 3])
    d = (rng.random(n) <= np.exp(-np.logaddexp(0, -score))).astype(int)
    v = d*f+rng.standard_normal(n)
    e0 = rng.standard_normal(n)
    e1 = rng.standard_normal((n, 2))
    pre = f+v+e0
    post = 2*f+v+e1[np.arange(n), d]+shift*d
    return {**{f"Z{j+1}": z[:, j].tolist() for j in range(4)},
            "D": d.tolist(), "Y_pre": pre.tolist(), "Y_post": post.tolist()}

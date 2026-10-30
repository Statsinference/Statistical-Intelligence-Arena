"""Choi et al. (2017) Case1B, double censoring on source linear/log scale."""
import numpy as np
from scipy.special import ndtr, ndtri


def generate(config,n,seed):
    if not isinstance(n,(int,np.integer)) or n<1:
        raise ValueError("n must be positive integer")
    rng=np.random.default_rng(seed)
    # Inverse-CDF conditioning is truncation, not winsorization at +/-2.
    bound=config["covariate_truncation"]
    lower,upper=ndtr(-bound),ndtr(bound)
    x=ndtri(lower+(upper-lower)*rng.random((n,5)))
    v1,v2,w1,w2,u=x.T
    delta=rng.normal(size=n)
    eps=rng.normal(size=n)
    d=1+v1+v2+w1+w2+u+delta
    y=1+config["beta"]*d+w1+w2+u+eps
    cy=rng.uniform(0,config["cy"],n)
    cd=rng.uniform(-7,config["cz"],n)
    return {"V1":v1.tolist(),"V2":v2.tolist(),"W1":w1.tolist(),"W2":w2.tolist(),
            "D_observed":np.maximum(d,cd).tolist(),"D_exact":(d>=cd).astype(int).tolist(),
            "Y_observed":np.minimum(y,cy).tolist(),"Y_event":(y<=cy).astype(int).tolist()}

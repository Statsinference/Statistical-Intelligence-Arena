"""Vermeulen and Vansteelandt (2015), Section 4.1, one iid sample."""
import math
import random

def expit(z):
    if z >= 0:
        return 1/(1+math.exp(-z))
    a=math.exp(z)
    return a/(1+a)

def generate(config,n,seed):
    if isinstance(n,bool) or not isinstance(n,int) or n<1:
        raise ValueError("n must be a positive integer")
    mode=config["mode"]
    if mode not in ("quadratic_logistic","quadratic_nonlinear"):
        raise ValueError("invalid source scenario")
    placeholder=float(config["missing_outcome_placeholder"])
    if not math.isfinite(placeholder):
        raise ValueError("nonfinite placeholder")
    rng=random.Random(seed)
    out={k:[] for k in ("X","R","Y_observed")}
    for _ in range(n):
        x=rng.gauss(0,1)
        y=x*x+rng.gauss(0,1)
        z=x if mode=="quadratic_logistic" else -4+1.5*math.sqrt(abs(x))+0.75*x+0.5*abs(x)**1.5
        r=int(rng.random()<expit(z))
        out["X"].append(x)
        out["R"].append(r)
        out["Y_observed"].append(y if r else placeholder)
    return out

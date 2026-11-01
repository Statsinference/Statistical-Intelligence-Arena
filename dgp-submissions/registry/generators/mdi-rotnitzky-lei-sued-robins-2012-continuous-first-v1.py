"""Section 5 first continuous-outcome experiment: observed data only."""
import math
import random

def expit(t):
    if t >= 0:
        return 1/(1+math.exp(-t))
    e = math.exp(t)
    return e/(1+e)

def generate(config,n,seed):
    if isinstance(n,bool) or not isinstance(n,int) or n<1:
        raise ValueError("n must be a positive integer")
    sd=float(config["covariate_sd"])
    noise_sd=float(config["outcome_noise_sd"])
    intercept=float(config["outcome_intercept"])
    slopes=[float(v) for v in config["outcome_coefficients"]]
    selection=[float(v) for v in config["observation_logit_coefficients"]]
    missing=float(config["missing_outcome_placeholder"])
    if not (sd>0 and noise_sd>0 and len(slopes)==4 and len(selection)==4
            and all(map(math.isfinite,[sd,noise_sd,intercept,missing]+slopes+selection))):
        raise ValueError("invalid scenario")
    rng=random.Random(seed)
    out={k:[] for k in ("L1","L2","L3","L4","A","Y_observed")}
    for _ in range(n):
        l=[rng.gauss(0,sd) for _ in range(4)]
        y=intercept+sum(b*x for b,x in zip(slopes,l))+rng.gauss(0,noise_sd)
        a=int(rng.random()<expit(sum(b*x for b,x in zip(selection,l))))
        for j,x in enumerate(l,1):
            out[f"L{j}"].append(x)
        out["A"].append(a)
        out["Y_observed"].append(y if a else missing)
    return out

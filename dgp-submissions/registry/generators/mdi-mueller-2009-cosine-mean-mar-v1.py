"""Müller (2009), Section 6.2 nonlinear mean-response scenario."""
import math
import random

def expit(x):
    return 1/(1+math.exp(-x)) if x>=0 else math.exp(x)/(1+math.exp(x))

def generate(config,n,seed):
    if isinstance(n,bool) or not isinstance(n,int) or n<1:
        raise ValueError('n must be a positive integer')
    if config['mode']!='cosine_logistic':
        raise ValueError('invalid scenario')
    placeholder=float(config['missing_outcome_placeholder'])
    if not math.isfinite(placeholder):
        raise ValueError('nonfinite placeholder')
    rng=random.Random(seed)
    data={k:[] for k in ('X','R','Y_observed')}
    for _ in range(n):
        x=2*rng.random()-1
        y=math.cos(2*x)+rng.gauss(0,1)
        r=int(rng.random()<expit(x))
        data['X'].append(x)
        data['R'].append(r)
        data['Y_observed'].append(y if r else placeholder)
    return data

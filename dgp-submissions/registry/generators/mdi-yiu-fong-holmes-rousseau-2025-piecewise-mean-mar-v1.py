"""Yiu et al. (2025), Section 6.2 missing-data simulation."""
import math
import random

def mean(x):
    if x < -0.5: return (x+2)**2/2
    if x < 0: return x/2+0.875
    if x < 0.5: return -5*(x-0.2)**2+1.075
    return x+0.125

def generate(config,n,seed):
    if isinstance(n,bool) or not isinstance(n,int) or n<1:
        raise ValueError('n must be a positive integer')
    if config['mode']!='piecewise_mar':
        raise ValueError('invalid scenario')
    placeholder=float(config['missing_outcome_placeholder'])
    if not math.isfinite(placeholder):
        raise ValueError('nonfinite placeholder')
    rng=random.Random(seed)
    data={k:[] for k in ('X','R','Y_observed')}
    for _ in range(n):
        x=2*rng.random()-1
        sd=0.2-0.1*math.cos(2*math.pi*x)
        y=mean(x)+rng.gauss(0,sd)
        pi=0.1 if x<0 else 0.9
        r=int(rng.random()<pi)
        data['X'].append(x)
        data['R'].append(r)
        data['Y_observed'].append(y if r else placeholder)
    return data

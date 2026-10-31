"""Section6.1 law; frozen coefficients, local RNG and observed columns only."""
import math
import random

def generate(config,n,seed):
    if not isinstance(config, dict) or 'scenarios' in config: raise ValueError('Pass one selected scenario parameter object, not the whole config.json')
    if isinstance(n, bool) or not isinstance(n, int) or n < 1: raise ValueError('n must be a positive integer')
    if isinstance(n,bool) or not isinstance(n,int) or n<1:
        raise ValueError('n must be positive integer')
    m=len(config['gamma'])
    if m!=100 or len(config['delta'])!=m or len(config['alpha'])!=m:
        raise ValueError('source scenario requires 100 instruments and aligned coefficients')
    if any(not math.isfinite(v) for k in ('gamma','delta','alpha') for v in config[k]):
        raise ValueError('nonfinite coefficients')
    for k in ('var_U','var_eA','var_eY'):
        if not math.isfinite(config[k]) or config[k]<=0:
            raise ValueError('positive finite noise variance required')
    rng=random.Random(seed)
    out={**{f'Z{j+1}':[] for j in range(m)},'A':[],'Y':[]}
    for _ in range(n):
        z=[int(rng.random()<.5)+int(rng.random()<.5) for _ in range(m)]
        u=rng.gauss(0,math.sqrt(config['var_U']))
        ea=rng.gauss(0,math.sqrt(config['var_eA']))
        ey=rng.gauss(0,math.sqrt(config['var_eY']))
        a=math.fsum(v*w for v,w in zip(config['gamma'],z))+config['eta_A']*u+(1+math.fsum(v*w for v,w in zip(config['delta'],z)))*ea
        y=config['beta']*a+math.fsum(v*w for v,w in zip(config['alpha'],z))+config['eta_Y']*u+ey
        for j,v in enumerate(z):out[f'Z{j+1}'].append(v)
        out['A'].append(a); out['Y'].append(y)
    return out

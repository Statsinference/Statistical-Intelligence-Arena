"""Section 5 additive law, with the complete joint map from Supplement S1.

Cells use index 2*d+y, ordered (0,0),(0,1),(1,0),(1,1).
Only x,Z,D,Y are exported. No arbitrary unidentified potential outcomes are sampled.
"""
import math
import random

def _expit(a):
    if a>=0:
        return 1.0/(1.0+math.exp(-a))
    e=math.exp(a)
    return e/(1.0+e)

def _linear(coeff,x):
    return coeff[0]+coeff[1]*x

def _validate(config):
    if len(config['beta_phi'])!=4:
        raise ValueError('four phi parameter vectors required')
    for pair in [config['alpha'],config['eta'],config['gamma'],*config['beta_phi']]:
        if len(pair)!=2 or not all(math.isfinite(float(v)) for v in pair):
            raise ValueError('all coefficient vectors must have two finite entries')
    lo,hi=config['x_bounds']
    if not math.isfinite(lo) or not math.isfinite(hi) or not lo<hi:
        raise ValueError('invalid uniform support')

def observed_probabilities(config,x,z):
    """Return four P(D,Y|x,z) probabilities using the stable closed-form map."""
    if z not in (0,1) or not math.isfinite(x):
        raise ValueError('invalid conditioning values')
    delta=math.tanh(_linear(config['alpha'],x))
    r=math.exp(_linear(config['eta'],x))
    phi=[_expit(_linear(b,x)) for b in config['beta_phi']]
    co=phi[0]; at=(1.0-co)*phi[1]; nt=(1.0-co)*(1.0-phi[1])
    # Rationalized S1 f0 expression, valid also at r=1 without division by r-1.
    root=math.sqrt(delta*delta*(r-1.0)**2+4.0*r)
    q0=2.0*r*(1.0-delta)/(r*(2.0-delta)+delta+root)
    q1=q0+delta
    if not (0<=q0<=1 and 0<=q1<=1):
        raise ArithmeticError('complier outcome probability outside unit interval')
    if z==0:
        cells=[nt*(1-phi[2])+co*(1-q0),nt*phi[2]+co*q0,
               at*(1-phi[3]),at*phi[3]]
    else:
        cells=[nt*(1-phi[2]),nt*phi[2],
               at*(1-phi[3])+co*(1-q1),at*phi[3]+co*q1]
    if min(cells)<0 or max(cells)>1 or abs(math.fsum(cells)-1)>1e-12:
        raise ArithmeticError('invalid observed joint distribution; no clipping is applied')
    return cells

def generate(config,n,seed):
    if not isinstance(config, dict) or 'scenarios' in config: raise ValueError('Pass one selected scenario parameter object, not the whole config.json')
    if isinstance(n, bool) or not isinstance(n, int) or n < 1: raise ValueError('n must be a positive integer')
    _validate(config)
    if isinstance(n,bool) or not isinstance(n,int) or n<1:
        raise ValueError('n must be a positive integer')
    rng=random.Random(seed)
    out={key:[] for key in ('x','Z','D','Y')}
    for _ in range(n):
        x=rng.uniform(*config['x_bounds'])
        z=int(rng.random()<_expit(_linear(config['gamma'],x)))
        cells=observed_probabilities(config,x,z)
        u=rng.random()
        cumulative=0.0
        category=3
        for k,p in enumerate(cells[:-1]):
            cumulative+=p
            if u<cumulative:
                category=k
                break
        d,y=divmod(category,2)
        for key,value in zip(out,(x,z,d,y)):
            out[key].append(value)
    return out

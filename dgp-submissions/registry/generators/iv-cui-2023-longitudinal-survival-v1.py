"""Cui et al. main-text DGP; masked wide output protects future history."""
import numpy as np
from scipy.special import ndtr

def generate(config,n,seed):
    rng=np.random.default_rng(seed)
    t00=rng.exponential(1/config['baseline_hazard'],n)
    eps=rng.normal(0,config['error_sd'],size=(n,4))
    l0=1.5*t00+eps[:,0]
    u0=1.5*t00+eps[:,1]
    z0=rng.binomial(1,ndtr(-.5+.2*l0))
    delta0=ndtr(.2*l0)
    a0=rng.binomial(1,ndtr(.2*l0-.8*u0)*(1-delta0)+z0*delta0)
    l1=l0-u0+1.5*a0+t00+eps[:,2]
    u1=.5*l0-u0+a0+t00+eps[:,3]
    z1=rng.binomial(1,ndtr(-1+.2*l1+.2*a0+.2*z0))
    delta1=ndtr(.2*l1)
    a1=rng.binomial(1,ndtr(.2*l1-.8*u1)*(1-delta1)+z1*delta1)
    q0=np.exp(config['psi']*a0)
    q1=np.exp(config['psi']*a1)
    v=config['visit_time']
    t=np.where(t00<=v*q0,t00/q0,v+(t00-v*q0)/q1)
    censor=np.minimum(rng.uniform(0,config['censor_uniform_max'],n),config['administrative_time'])
    y=np.minimum(t,censor)
    event=(t<=censor).astype(int)
    r1=(y>=v).astype(int)
    return {'L0':l0.tolist(),'Z0':z0.tolist(),'A0':a0.tolist(),
            'R1':r1.tolist(),'L1':(r1*l1).tolist(),'Z1':(r1*z1).tolist(),
            'A1':(r1*a1).tolist(),'Y':y.tolist(),'event':event.tolist()}

"""Source-grounded observed-data generator. SPDX-License-Identifier: Apache-2.0."""
import math
import numpy as np
from scipy.special import expit

SOURCE_CONFIG = {'observation_rule': 'two_independent_samples', 'placeholder': 0.0, 'mechanism': 'songlinear', 'dimension': 4, 'source_n_labeled': 250, 'source_n_unlabeled': 1000, 'rho': 0.5, 'noise_sd': 1.0, 'query_coordinate': 1}

def _validate(config):
    if config != SOURCE_CONFIG:
        raise ValueError('This contribution supports exactly the declared original scenario')

def _allocation(config, n):
    if isinstance(n, bool) or not isinstance(n, int) or n < 2:
        raise ValueError('n must be an integer >=2; it is the total row count')
    total=config['source_n_labeled']+config['source_n_unlabeled']
    return max(1,min(n-1,(n*config['source_n_labeled']+total//2)//total))

def _draw_x(c,n,rng):
    x=rng.normal(size=(n,c['dimension']))
    rho=c['rho']
    for j in range(1,c['dimension']):
        x[:,j]=rho*x[:,j-1]+math.sqrt(1-rho*rho)*x[:,j]
    return x

def _response(x,eps,c):
    return np.mean(np.exp(x+2*np.cos(x)-0.3*eps[:,None])+0.1*np.exp(x+np.sin(x))+2.5*x**3,axis=1)+eps


def generate(config, n, seed):
    _validate(config)
    labeled=_allocation(config,n)
    streams=np.random.SeedSequence(seed).spawn(2)
    rx=np.random.Generator(np.random.PCG64(streams[0]))
    ry=np.random.Generator(np.random.PCG64(streams[1]))
    c=config
    x=_draw_x(c,n,rx)
    observed=_response(x[:labeled],ry.normal(size=labeled),c)
    y=np.zeros(n); y[:labeled]=observed
    r=np.zeros(n,dtype=int); r[:labeled]=1
    out={f'X{j+1}':x[:,j].tolist() for j in range(config['dimension'])}
    out['R']=r.tolist(); out['Y_obs']=y.tolist()
    return out

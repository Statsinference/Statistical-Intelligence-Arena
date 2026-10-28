"""Source-grounded observed-data generator. SPDX-License-Identifier: Apache-2.0."""
import math
import numpy as np
from scipy.special import expit

SOURCE_CONFIG = {'observation_rule': 'two_independent_samples', 'placeholder': 0.0, 'mechanism': 'discrete', 'dimension': 1, 'source_n_labeled': 1000, 'source_n_unlabeled': 9000, 'component_means': [-2.0, 0.0, 4.0], 'noise_sd': 1.0}

def _validate(config):
    if config != SOURCE_CONFIG:
        raise ValueError('This contribution supports exactly the declared original scenario')

def _allocation(config, n):
    if isinstance(n, bool) or not isinstance(n, int) or n < 2:
        raise ValueError('n must be an integer >=2; it is the total row count')
    total=config['source_n_labeled']+config['source_n_unlabeled']
    return max(1,min(n-1,(n*config['source_n_labeled']+total//2)//total))

def _draw_x(c,n,rng):
    return rng.integers(1,4,size=(n,1))

def _response(x,eps,c):
    return np.array(c['component_means'])[x[:,0].astype(int)-1]+c['noise_sd']*eps


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

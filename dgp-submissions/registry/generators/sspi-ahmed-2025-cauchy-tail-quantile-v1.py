"""Source-grounded observed-data generator. SPDX-License-Identifier: Apache-2.0."""
import math
import numpy as np
from scipy.special import expit

SOURCE_CONFIG = {'observation_rule': 'two_independent_samples', 'placeholder': 0.0, 'mechanism': 'tail', 'dimension': 1, 'source_n_labeled': 500, 'source_n_unlabeled': 1000, 'cauchy_scale_offdiagonal': 0.0, 'gamma': 0.0, 'tail_probability': 0.002}

def _validate(config):
    if config != SOURCE_CONFIG:
        raise ValueError('This contribution supports exactly the declared original scenario')

def _allocation(config, n):
    if isinstance(n, bool) or not isinstance(n, int) or n < 2:
        raise ValueError('n must be an integer >=2; it is the total row count')
    total=config['source_n_labeled']+config['source_n_unlabeled']
    return max(1,min(n-1,(n*config['source_n_labeled']+total//2)//total))

def _positive_normals(rng,n):
    x=np.abs(rng.normal(size=n))
    while np.any(x==0):
        mask=x==0
        x[mask]=np.abs(rng.normal(size=int(mask.sum())))
    return x

def _transform(v,denominator):
    # For positive v/denominator, 1-F0(v/denominator)=2*atan(denominator/v)/pi.
    # atan2 avoids cancellation in 1-2*atan(ratio)/pi at extreme ratios.
    return -np.log(2*np.arctan2(denominator,v)/math.pi)


def generate(config, n, seed):
    _validate(config)
    labeled=_allocation(config,n)
    streams=np.random.SeedSequence(seed).spawn(2)
    rx=np.random.Generator(np.random.PCG64(streams[0]))
    ry=np.random.Generator(np.random.PCG64(streams[1]))
    c=config
    denominator=_positive_normals(rx,n)
    auxiliary=_positive_normals(rx,n)
    x=(auxiliary/denominator)[:,None]
    target_numerator=_positive_normals(ry,labeled)
    observed=_transform(target_numerator,denominator[:labeled])
    y=np.zeros(n); y[:labeled]=observed
    r=np.zeros(n,dtype=int); r[:labeled]=1
    out={f'X{j+1}':x[:,j].tolist() for j in range(config['dimension'])}
    out['R']=r.tolist(); out['Y_obs']=y.tolist()
    return out

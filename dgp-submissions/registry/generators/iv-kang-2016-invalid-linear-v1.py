"""Kang et al. JASA model, parameterized by the authors' pinned sisVIVE example."""
import numpy as np
from common import finite,sampling


def validate_config(c):
    if set(c)!={'instrument_count','invalid_count','rho','beta','first_stage','treatment_intercept','outcome_intercept'}:
        raise ValueError('Unexpected configuration keys')
    if c['instrument_count']!=10 or c['invalid_count']!=3:
        raise ValueError('Fixed source design: ten candidate IVs, first three invalid')
    for k in ['rho','beta','first_stage','treatment_intercept','outcome_intercept']: finite(c[k],k)
    if abs(c['rho'])>=1 or c['first_stage']==0: raise ValueError('Nonsingular errors and relevant instruments required')


def generate(config,n,seed):
    validate_config(config); rng=sampling(n,seed)
    z=rng.normal(size=(n,10)); errors=rng.normal(size=(n,2))
    xi=errors[:,0]
    eps=config['rho']*xi+np.sqrt(1-config['rho']**2)*errors[:,1]
    d=config['treatment_intercept']+config['first_stage']*z.sum(axis=1)+xi
    y=config['outcome_intercept']+z[:,:3].sum(axis=1)+config['beta']*d+eps
    return {**{f'Z{j+1}':z[:,j].tolist() for j in range(10)},'D':d.tolist(),'Y':y.tolist()}

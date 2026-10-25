"""Athey--Tibshirani--Wager (2019), Appendix C.2 equation (49)."""
import numpy as np
from common import query, sampling


def validate_config(c):
    if set(c) != {'dimension','signal_dimension','additive','omega','nuisance_scale','effect_scale','query_point'}:
        raise ValueError('Unexpected configuration keys')
    if c['dimension'] != 10 or c['signal_dimension'] not in (2,4):
        raise ValueError('Registered dimensions are p=10, k=2 or 4')
    if type(c['additive']) is not bool or c['omega'] not in (0,1) or c['nuisance_scale'] not in (0,3):
        raise ValueError('Use the source Appendix C.2 parameter grid')
    query(c,10)


def components(x,c):
    k=c['signal_dimension']
    if c['additive']:
        tau=np.maximum(x[:,:k],0).sum(axis=1)
        mu=c['nuisance_scale']*np.maximum(x[:,4:6],0).sum(axis=1)
    else:
        tau=np.maximum(x[:,:k].sum(axis=1),0)
        mu=c['nuisance_scale']*np.maximum(x[:,4:6].sum(axis=1),0)
    return mu,c['effect_scale']*tau


def generate(config,n,seed):
    validate_config(config)
    rng=sampling(n,seed)
    x=rng.normal(size=(n,10))
    eps=rng.normal(size=n)
    z=(rng.random(n)<1/3).astype(int)
    prob=np.exp(-np.logaddexp(0,-config['omega']*eps))
    q=(rng.random(n)<prob).astype(int)
    a=z*q
    mu,tau=components(x,config)
    y=mu+(a-0.5)*tau+eps
    return {**{f'X{j+1}':x[:,j].tolist() for j in range(10)},'Z':z.tolist(),'A':a.tolist(),'Y':y.tolist()}

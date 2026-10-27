import numpy as np

def generate(config,n,seed):
    """One row is one individual with all four observed outcomes. G: a=0,b=1,trt=2."""
    if not isinstance(n,int) or isinstance(n,bool) or n<1: raise ValueError('n must be positive integer')
    probs=np.asarray(config['group_proportions'],dtype=float)
    means=np.asarray(config['untreated_means'],dtype=float)
    effects=np.asarray(config['effects'],dtype=float)
    sd=float(config['noise_sd'])
    if probs.shape!=(3,) or np.any(probs<0) or not np.isclose(probs.sum(),1): raise ValueError('group probabilities')
    if means.shape!=(3,4) or effects.shape!=(4,) or sd<=0 or effects[0]!=0: raise ValueError('invalid four-period no-anticipation design')
    quotas=n*probs
    counts=np.floor(quotas).astype(int)
    order=np.argsort(-(quotas-counts),kind='stable')
    counts[order[:n-int(counts.sum())]]+=1
    group=np.repeat(np.arange(3),counts)
    rng=np.random.default_rng(seed)
    outcomes=means[group]+(group[:,None]==2)*effects+rng.normal(0,sd,(n,4))
    return {'G':group.tolist(),**{f'Y{k+1}':outcomes[:,k].tolist() for k in range(4)}}

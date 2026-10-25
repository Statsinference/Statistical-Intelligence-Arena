"""Shi et al., JASA 2026 supplement J.8 Eq S.25, r=1, no covariates."""
import numpy as np

def generate(config,n,seed):
    if not isinstance(n,int) or n<4: raise ValueError('n must be integer >=4')
    c=config;r=np.random.Generator(np.random.PCG64(seed));t=np.arange(1,n+1)
    a=(t>n//2).astype(int)
    # Rejection sampling preserves the truncated-normal law; no clipping.
    latent=r.normal(c['factor_mean'],c['factor_sd'],n)
    invalid=(latent<=0)|(latent>=1)
    while invalid.any():
        latent[invalid]=r.normal(c['factor_mean'],c['factor_sd'],int(invalid.sum()))
        invalid=(latent<=0)|(latent>=1)
    y=r.poisson(np.exp(latent+c['log_ratio']*a))
    w=r.poisson(latent/np.expm1(1));z=r.poisson(latent/np.expm1(1))
    return {key:value.tolist() for key,value in dict(time=t,A=a,Y=y,W=w,Z=z).items()}

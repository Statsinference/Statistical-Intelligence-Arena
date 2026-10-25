"""Shi et al., JASA 2026 section 4: stationary factors, r=5."""
import numpy as np

def generate(config,n,seed):
    if not isinstance(n,int) or n<4: raise ValueError('n must be integer >=4')
    c=config;r=np.random.Generator(np.random.PCG64(seed));t=np.arange(1,n+1)
    a=(t>n//2).astype(int);k=c['r']
    latent=r.normal(c['factor_mean'],c['factor_sd'],(n,k))
    errors=r.normal(0,c['noise_sd'],(n,1+2*k))
    loading=np.asarray(c['donor_loading'])
    y=latent.sum(axis=1)+errors[:,0]+a*c['effect']
    w=latent*loading+errors[:,1:1+k];z=latent*loading+errors[:,1+k:]
    out=dict(time=t,A=a,Y=y)
    out.update({f'W{j+1}':w[:,j] for j in range(k)})
    out.update({f'Z{j+1}':z[:,j] for j in range(k)})
    return {key:value.tolist() for key,value in out.items()}

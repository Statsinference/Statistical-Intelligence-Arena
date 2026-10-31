"""Deng et al. Section 6.1; independent implementation, pinned arXiv v2."""
import math
import numpy as np
SOURCE = {'model': 2, 'dimension': 500, 'rho': 0.3, 'labeled_reference': 200, 'unlabeled_reference': 1000, 'noise_sd': 1.0, 'target_coordinate': 4}

def validate(config):
    if config != SOURCE:
        raise ValueError("Use the declared fixed scenario; changes require re-deriving truth and metadata")

def generate(config,n,seed):
    validate(config)
    if isinstance(n,bool) or not isinstance(n,int) or n<2:
        raise ValueError("n is total rows and must be an integer >=2")
    cov_seed,noise_seed=np.random.SeedSequence(seed).spawn(2)
    rng=np.random.Generator(np.random.PCG64(cov_seed))
    noise=np.random.Generator(np.random.PCG64(noise_seed))
    d=config['dimension'];rho=config['rho']
    x=rng.normal(size=(n,d))
    for j in range(1,d):x[:,j]=rho*x[:,j-1]+math.sqrt(1-rho*rho)*x[:,j]
    x[:,0]=np.abs(x[:,0])
    nl=max(1,min(n-1,n*config['labeled_reference']//(config['labeled_reference']+config['unlabeled_reference'])))
    z=x[:nl]
    if config['model']==2:
        mu=0.6*(z[:,0]+z[:,1])**2+0.4*z[:,3]**3-z[:,4]+2*z[:,5]
    else:
        mu=0.5*z[:,0]**2+0.8*z[:,2]**3-(z[:,3]-2)**2+2*(z[:,4]+1)**2+2*z[:,5]
        if config['model']==3:
            mu=mu+2*z[:,np.array(config['support_linear'])-1].sum(axis=1)+0.05*z[:,np.array(config['support_cubic'])-1].sum(axis=1)**3
    y=np.zeros(n);y[:nl]=mu+noise.normal(0,1,nl)
    r=np.zeros(n,dtype=int);r[:nl]=1
    out={f'X{j+1}':x[:,j].tolist() for j in range(d)}
    out.update(R=r.tolist(),Y_obs=y.tolist())
    return out

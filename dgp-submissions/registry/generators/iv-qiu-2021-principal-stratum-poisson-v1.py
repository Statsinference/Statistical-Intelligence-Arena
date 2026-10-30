"""Qiu, Tao and Zhou (2021), Section 6 DGP2, no interaction."""
import numpy as np


def generate(config, n, seed):
    if not isinstance(n, (int, np.integer)) or n < 1:
        raise ValueError("n must be positive integer")
    p = int(config["p"])
    rng = np.random.default_rng(seed)
    # Stationary Gaussian AR(1) yields Sigma_jk=sigma0*rho_x^|j-k|.
    x = np.empty((n,p))
    x[:,0] = np.sqrt(config["sigma0"])*rng.normal(size=n)
    rho = config["rho_x"]
    sd = np.sqrt(config["sigma0"]*(1-rho*rho))
    for j in range(1,p):
        x[:,j] = rho*x[:,j-1]+sd*rng.normal(size=n)
    gamma = 1/np.arange(1,p+1,dtype=float)**2
    t = x @ gamma
    pz = 1/(1+np.exp(-t))
    z = rng.binomial(1,pz)
    d0 = t-config["zeta"]+rng.normal(size=n) >= 0
    d1star = t+config["zeta"]+rng.normal(size=n) >= 0
    d1 = d0 | d1star
    d = np.where(z==1,d1,d0).astype(int)
    eps = rng.normal(size=n)
    k11 = rng.poisson(config["lambda11"],n)
    k00 = rng.poisson(config["lambda00"],n)
    y = config["alpha0"]*d+2*t+eps+k11*d0+k00*(~d1)
    observed = {f"X{j+1}":x[:,j].tolist() for j in range(p)}
    observed.update({"Z":z.tolist(),"D":d.tolist(),"Y":y.tolist()})
    return observed

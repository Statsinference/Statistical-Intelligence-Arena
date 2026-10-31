"""AoS §4.1 finite-horizon Markov mediation; one row is a whole subject trajectory."""
import random
def step(s,w,a,mp,rp,ew,er,knock=None):
    mu=[s['alpha1'][j]+s['delta1'][j]*a+sum(s['gamma1'][j][k]*mp[k] for k in range(3))+s['zeta1'][j]*rp for j in range(3)]
    m=[0.,0.,0.]
    for j in range(3):
        m[j]=mu[j]+ew[j]+sum(w[k][j]*(m[k]-mu[k]) for k in range(j))
        if knock==j+1:m[j]=0.
    rr=s['alpha2']+s['delta2']*a+sum(s['gamma2'][j]*mp[j] for j in range(3))+s['zeta2']*rp+sum(s['kappa'][j]*m[j] for j in range(3))+er
    return m,rr
def generate(config,n,seed):
    if isinstance(n,bool) or not isinstance(n,int) or n<1:raise ValueError('n must be positive int')
    rng=random.Random(seed);o={f'{kind}{t:02d}'+(f'_{j}' if kind=='M' else ''):[] for t in range(1,config['T']+1) for kind in ('A','M','R') for j in ((1,2,3) if kind=='M' else (0,))}
    for _ in range(n):
        mp=[0.,0.,0.];rp=0.
        for t,s in enumerate(config['stages'],1):
            a=int(rng.random()<config['p_treatment']);ew=[rng.gauss(0,config['mediator_error_sd']) for _ in range(3)];er=rng.gauss(0,config['outcome_error_sd'])
            m,rr=step(s,config['W'],a,mp,rp,ew,er)
            o[f'A{t:02d}'].append(a)
            for j in range(3):o[f'M{t:02d}_{j+1}'].append(m[j])
            o[f'R{t:02d}'].append(rr)
            mp,rp=m,rr
    return o

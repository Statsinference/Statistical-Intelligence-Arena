import random
def neighbors(i,N,L):return [(i+d)%N for d in range(-L,L+1) if d]
def generate(config,n,seed):
 if not isinstance(config, dict) or 'scenarios' in config: raise ValueError('Pass one selected scenario parameter object, not the whole config.json')
 if isinstance(n, bool) or not isinstance(n, int) or n < 1: raise ValueError('n must be a positive integer')
 c = config
 if n<1 or c['N']!=500 or c['L'] not in (2,3):raise ValueError('selected source network requires N500 and L2/3')
 N=c['N'];nb=[neighbors(i,N,c['L']) for i in range(N)];rng=random.Random(seed)
 out={k:[] for i in range(N) for k in ('Z'+str(i),'D'+str(i),'Y'+str(i))}
 for _ in range(n):
  z=[int(rng.random()<c['z_probability']) for i in range(N)]
  d=[int(c['gamma0'][i]+c['gamma1']*z[i]+(c['gamma2']*sum(z[j] for j in nb[i]) if c['model']==1 else 0)>=0) for i in range(N)]
  y=[c['beta0'][i]+c['beta1'][i]*d[i]+(c['beta2'][i]*sum(d[j] for j in nb[i]) if c['model']==2 else 0) for i in range(N)]
  for i in range(N):
   out['Z'+str(i)].append(z[i]);out['D'+str(i)].append(d[i]);out['Y'+str(i)].append(y[i])
 return out

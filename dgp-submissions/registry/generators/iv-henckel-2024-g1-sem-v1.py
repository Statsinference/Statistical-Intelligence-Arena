import math,random
def generate(config,n,seed):
 if not isinstance(config, dict) or 'scenarios' in config: raise ValueError('Pass one selected scenario parameter object, not the whole config.json')
 if isinstance(n, bool) or not isinstance(n, int) or n < 1: raise ValueError('n must be a positive integer')
 c = config
 if c['error_family'] not in ('gaussian','uniform'): raise ValueError('Unknown error_family')
 if any(not math.isfinite(v) or v <= 0 for v in c['variance'].values()): raise ValueError('Error variances must be finite and positive')
 if n<1:raise ValueError('n must be positive')
 rng=random.Random(seed);out={k:[] for k in ('A','B','C','D','X','M','Y')};b=c['coeff'];v=c['variance']
 for _ in range(n):
  noise={k:(rng.gauss(0,math.sqrt(var)) if c['error_family']=='gaussian' else rng.uniform(-math.sqrt(3*var),math.sqrt(3*var))) for k,var in v.items()}
  a=noise['A'];cv=noise['C'];bv=b['C_B']*cv+noise['B'];dv=b['A_D']*a+b['B_D']*bv+b['Hdx_D']*noise['Hdx']+noise['D']
  x=b['B_X']*bv+b['Hdx_X']*noise['Hdx']+b['Hxy_X']*noise['Hxy']+noise['X'];m=b['X_M']*x+noise['M']
  y=b['X_Y']*x+b['M_Y']*m+b['C_Y']*cv+b['Hxy_Y']*noise['Hxy']+noise['Y']
  for k,value in zip(out,(a,bv,cv,dv,x,m,y)):out[k].append(value)
 return out

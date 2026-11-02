"""Independent official-2024-code-version null mechanism; observed outputs only."""
import numbers
import numpy as np
_EXPECTED = {'scenario': 'official_code_null_id1', 'units': 30, 'clusters': 3, 'cluster_size': 10, 'generated_periods': 99, 'T_pre': 45, 'T_post': 10, 'similarclus': 0, 'hetero': True}

def _validate(config):
    if not isinstance(config,dict) or set(config)!=set(_EXPECTED):
        raise ValueError("Complete registered configuration required")
    for key, expected in _EXPECTED.items():
        value=config[key]
        if type(value) is not type(expected) or value!=expected:
            raise ValueError("Unsupported parameter: "+key)

def _damping(rng, rate):
    damp=np.zeros(99,dtype=bool)
    now=1
    while now<99:
        now+=int(np.floor(rng.exponential(1.0/rate)))
        if now>99:
            break
        duration=int(np.ceil(rng.exponential(3.0)))
        end=min(99,now+duration)
        damp[now-1:end]=True
        now=end
    return damp

def generate(config,n,seed):
    _validate(config)
    if isinstance(n,(bool,np.bool_)) or not isinstance(n,numbers.Integral) or n!=30:
        raise ValueError("n is unit rows and must equal30")
    if isinstance(seed,(bool,np.bool_)) or not isinstance(seed,numbers.Integral) or seed<0:
        raise ValueError("seed must be a nonnegative integer")
    rng=np.random.default_rng(int(seed))
    intercept=rng.uniform(10.0,60.0,size=30)
    time=np.arange(99)
    outcome=intercept[:,None]+time//4+2*(time%4)+5*rng.normal(size=(30,99))
    for group,rate in enumerate((1/10,1/15,1/7)):
        damp=_damping(rng,rate)
        outcome[group*10:(group+1)*10,damp]-=80.0
    outcome=np.maximum(outcome[:,:55],0.0)
    weights=1.0+outcome[:,19:45].mean(axis=1)
    treated=np.zeros(30,dtype=int)
    for group in range(3):
        ids=np.arange(group*10,(group+1)*10)
        treated[rng.choice(ids,p=weights[ids]/weights[ids].sum())]=1
    result={"G":treated.tolist(),"C":np.repeat([1,2,3],10).tolist()}
    for t in range(55):
        name="Y_pre%03d"%(t+1) if t<45 else "Y_post%03d"%(t-44)
        result[name]=outcome[:,t].tolist()
    return result

"""Author-code-version CaseII; observed cells only, no potential coupling."""
import numbers
import numpy as np

def generate(config,n,seed):
    expected={"scenario":"author_code_case2","units":1000,"T_pre":1,"T_post":3}
    if type(config)!=dict or set(config)!=set(expected) or any(type(config[k]) is not type(v) or config[k]!=v for k,v in expected.items()):
        raise ValueError("Only registered N1000 CaseII configuration is supported")
    if isinstance(n,(bool,np.bool_)) or not isinstance(n,numbers.Integral) or n!=1000:
        raise ValueError("n must equal1000 unit rows")
    if isinstance(seed,(bool,np.bool_)) or not isinstance(seed,numbers.Integral) or seed<0:
        raise ValueError("seed must be a nonnegative integer")
    rng=np.random.default_rng(int(seed))
    y=np.empty((1000,4))
    for t in range(4):
        y[:300,t]=rng.normal((3,4,0,1)[t]+(0,2,3,1)[t],1,300)
        y[800:,t]=rng.normal((10,11,10,11)[t],1,200)
        y[300:800,t]=rng.normal((4,6,2,3)[t],1,500)
    return {"G":([1]*300+[0]*700),"C":([0]*300+[1]*500+[2]*200),
            "Y_pre001":y[:,0].tolist(),"Y_post001":y[:,1].tolist(),
            "Y_post002":y[:,2].tolist(),"Y_post003":y[:,3].tolist()}

"""Retrospective joint-normal sampling; the sampling order is not a causal DAG."""
import numpy as np

def generate(config, n, seed):
    if not isinstance(n, int) or n < 1:
        raise ValueError("n must be a positive integer")
    c = config
    rng = np.random.Generator(np.random.PCG64(seed))
    x = rng.normal(c['x_mean'], c['x_sd'], (n, 2))
    a = (rng.random(n) < 1 / (1 + np.exp(x @ c['propensity_coef']))).astype(int)
    zwu = rng.standard_normal((n, 3)) @ np.linalg.cholesky(c['cov_zwu']).T
    zwu += np.asarray(c['mean_zwu']) + a[:, None]*np.asarray(c['a_shift']) + (x @ c['x_coef'])[:, None]
    z, w, u = zwu.T
    # This conditional expectation has no A or Z term by the covariance constraints.
    mw = c['mean_zwu'][1] + x @ c['x_coef'] + c['cov_zwu'][1][2]/c['cov_zwu'][2][2]*(u-c['mean_zwu'][2]-x @ c['x_coef'])
    if c['form'] == 'linear':
        main = x @ c['main_x']
        delta = c['effect_intercept'] + x @ c['effect_x'] + c['effect_w']*mw
    elif c['form'] == 'trigonometric':
        main = np.sum(x*x, axis=1)
        delta = c['effect_intercept'] + np.abs(x[:,0]-1)-np.abs(x[:,1]+1) + (c['effect_w']+np.sin(x[:,0])-2*np.cos(x[:,1]))*mw
    elif c['form'] == 'quadratic':
        main = np.sum(x*x, axis=1)
        delta = c['effect_intercept'] + c['effect_product']*x[:,0]*x[:,1]
    else:
        raise ValueError('unsupported source form')
    error = rng.normal(0, c['noise_scale'], n) if c['noise'] == 'normal' else rng.uniform(-c['noise_scale'], c['noise_scale'], n)
    y = c['intercept'] + main + c['w_coef']*mw + c['omega']*(w-mw) + c['effect_scale']*a*delta + error
    return {**{f'X{j+1}':x[:,j].tolist() for j in range(2)}, 'A':a.tolist(), 'Z':z.tolist(), 'W':w.tolist(), 'Y':y.tolist()}

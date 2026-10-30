"""Independent Python reconstruction of the pinned WIT probability law."""
import numpy as np


def validate(config):
    p = config['p']
    if isinstance(p, bool) or not isinstance(p, int) or p != 21:
        raise ValueError('This contribution requires p=21')
    for key in ('alpha', 'gamma'):
        value = np.asarray(config[key], dtype=float)
        if value.shape != (p,) or not np.isfinite(value).all():
            raise ValueError(key + ' must have 21 finite coefficients')
    for key in ('beta', 'instrument_variance', 'instrument_rho',
                'epsilon_variance', 'eta_variance', 'error_correlation'):
        if isinstance(config[key], bool) or not np.isfinite(config[key]):
            raise ValueError(key + ' must be finite numeric')
    if any(config[key] <= 0 for key in
           ('instrument_variance', 'epsilon_variance', 'eta_variance')):
        raise ValueError('Variances must be positive')
    if abs(config['instrument_rho']) >= 1 or abs(config['error_correlation']) >= 1:
        raise ValueError('Correlations must lie strictly between -1 and 1')


def generate(config, n, seed):
    """Observed Z1..Z21,D,Y only; config is one scenario object."""
    validate(config)
    if isinstance(n, bool) or not isinstance(n, int) or n < 1:
        raise ValueError('n must be a positive integer')
    rng = np.random.Generator(np.random.PCG64(seed))
    p = config['p']
    lag = np.abs(np.arange(p)[:, None] - np.arange(p)[None, :])
    sigma_z = config['instrument_variance'] * config['instrument_rho'] ** lag
    covariance = config['error_correlation'] * np.sqrt(
        config['epsilon_variance'] * config['eta_variance'])
    sigma_e = np.array([[config['epsilon_variance'], covariance],
                        [covariance, config['eta_variance']]])
    z = rng.standard_normal((n, p)) @ np.linalg.cholesky(sigma_z).T
    errors = rng.standard_normal((n, 2)) @ np.linalg.cholesky(sigma_e).T
    d = z @ np.asarray(config['gamma']) + errors[:, 1]
    y = config['beta'] * d + z @ np.asarray(config['alpha']) + errors[:, 0]
    output = {f'Z{j+1}': z[:, j].tolist() for j in range(p)}
    output.update(D=d.tolist(), Y=y.tolist())
    return output

"""Hall--Horowitz (2013), section 3.1, g1: observed X and Y only."""
import math
import random

SOURCE_NOISE_SD = (1.0, 0.5, 0.2)


def validate_config(config):
    """Keep source noise settings; a query selects the scalar inference target."""
    if not isinstance(config, dict) or set(config) != {'query_x', 'noise_sd'}:
        raise ValueError('Expected exactly query_x and noise_sd.')
    for name, value in config.items():
        if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value):
            raise ValueError(name + ' must be a finite real number.')
    if not -1 <= config['query_x'] <= 1:
        raise ValueError('query_x must be in the design support [-1,1].')
    if config['noise_sd'] not in SOURCE_NOISE_SD:
        raise ValueError('noise_sd must be a source setting: 1, 0.5, or 0.2.')


def regression_mean(x):
    return x + 5.0 * math.exp(-50.0 * x * x) / math.sqrt(2.0 * math.pi)


def generate(config, n, seed):
    """Draw n IID pairs; RNG is local and no oracle column is returned."""
    validate_config(config)
    if isinstance(n, bool) or not isinstance(n, int) or n <= 0:
        raise ValueError('n must be a positive integer.')
    if isinstance(seed, bool) or not isinstance(seed, int):
        raise ValueError('seed must be an integer.')
    rng = random.Random(seed)
    covariates = [rng.uniform(-1.0, 1.0) for _ in range(n)]
    errors = [rng.gauss(0.0, config['noise_sd']) for _ in range(n)]
    outcomes = [regression_mean(x) + error for x, error in zip(covariates, errors)]
    return {'X': covariates, 'Y': outcomes}

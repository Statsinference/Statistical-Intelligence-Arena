"""Observed columns for Wang & Yang (2007) Example 6.2: d=30 additive + heteroscedastic noise.

Only observed variables are returned. The conditional mean, the noise scale and the
query point are population quantities held in truth.py; none of them is emitted as a
column. Standard library only, so the smoke check runs on any Python 3.10+.
"""
import math
import random

SOURCE_FREQUENCY = math.pi / 2.5  # sin(pi * X / 2.5) in Example 6.2
SOURCE_SIGMA0 = 0.1
SOURCE_DIMENSION = 30
SOURCE_BOUND = 2.5
# Example 6.2 sets sigma(X) = sigma0 * sqrt(d)/2 * (5-exp(L))/(5+exp(L)).
# The divisor 2 is outside the square root: the typeset display is \frac{\sqrt{d}}{2},
# not \sqrt{d/2}. Decided from reprint glyph coordinates and embedded font widths; see card.md.
SIGMA_ROOT_D_DIVISOR = 2.0


def validate(config):
    dimension = config["dimension"]
    if not isinstance(dimension, int) or isinstance(dimension, bool) or dimension < 1:
        raise ValueError("dimension must be a positive integer")
    for key in ("sigma0", "truncation_bound", "sin_frequency_scale", "noise_sd"):
        value = config[key]
        if not isinstance(value, (int, float)) or isinstance(value, bool) or not math.isfinite(value):
            raise ValueError(key + " must be finite")
    if config["sigma0"] <= 0 or config["truncation_bound"] <= 0 or config["noise_sd"] <= 0:
        raise ValueError("sigma0, truncation_bound and noise_sd must be positive")
    query = config["query"]
    if not isinstance(query, (list, tuple)) or len(query) != dimension:
        raise ValueError("query must have exactly `dimension` coordinates")
    if not all(isinstance(v, (int, float)) and not isinstance(v, bool) and math.isfinite(v) for v in query):
        raise ValueError("query coordinates must be finite numbers")


def _truncated_normal(rng, bound):
    """Rejection resampling from N(0,1) until |x| <= bound. Same RNG stream, hence reproducible."""
    while True:
        value = rng.gauss(0.0, 1.0)
        if -bound <= value <= bound:
            return value


def sigma_function(x_row, sigma0, dimension, root_divisor=SIGMA_ROOT_D_DIVISOR):
    """sigma(X) = sigma0 * sqrt(d)/2 * (5 - exp(L)) / (5 + exp(L)), L = mean_alpha |X_alpha|."""
    ell = math.fsum(abs(v) for v in x_row) / dimension
    e = math.exp(ell)
    return sigma0 * math.sqrt(dimension) / root_divisor * (5.0 - e) / (5.0 + e)


def generate(config, n, seed):
    """Rows are overlapping windows of one long i.i.d. covariate stream.

    We interpret the displayed Example 6.2 lag subscripts as one shared stream:
    Y_t = sum_{alpha=1}^{d} sin(pi X_{t-alpha}/2.5) + sigma(X) eps_t, where
    X_t^T = {X_{t-1}, ..., X_{t-d}} are taken from one sequence of i.i.d. truncated
    standard normals. Because row t reads lags 1..d of that single sequence, consecutive
    rows share d-1 coordinates: the sample is serially dependent (which is why the
    paper's theory needs alpha-mixing), even though every coordinate is marginally i.i.d.

    That explicitly declared interpretation is implemented here. One stream Z_0..Z_{n+d-2} is drawn, and the row for
    time T = t + d is (Z_{T-1}, ..., Z_{T-d}), i.e. column X_alpha holds X_{T-alpha}.
    Rows whose time indices differ by at least d are independent; rows closer than that
    are not, so consecutive length-d blocks are still dependent; see verify.py for
    exact signal overlap counts and conditional innovation variance.
    """
    validate(config)
    if isinstance(n, bool) or not isinstance(n, int) or n < 1:
        raise ValueError("n must be a positive integer")
    dimension = config["dimension"]
    bound = float(config["truncation_bound"])
    frequency = float(config["sin_frequency_scale"])
    sigma0 = float(config["sigma0"])
    noise_sd = float(config["noise_sd"])
    rng = random.Random(seed)
    names = ["X" + str(i) for i in range(1, dimension + 1)]
    out = {name: [] for name in names}
    out["Y"] = []
    stream = [_truncated_normal(rng, bound) for _ in range(n + dimension - 1)]
    for t in range(n):
        # Row t is time index T = t + dimension; column X_alpha holds X_{T-alpha}.
        row = [stream[t + dimension - alpha] for alpha in range(1, dimension + 1)]
        mean = math.fsum(math.sin(frequency * value) for value in row)
        y = mean + sigma_function(row, sigma0, dimension) * rng.gauss(0.0, noise_sd)
        for name, value in zip(names, row):
            out[name].append(value)
        out["Y"].append(y)
    return out

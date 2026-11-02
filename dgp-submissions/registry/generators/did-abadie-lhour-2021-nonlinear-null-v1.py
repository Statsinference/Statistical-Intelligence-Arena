"""M01 observed unit-wide panel. No estimator, hidden label or global RNG."""
import math
import random

COLUMNS = ("G", "X1", "X2", "X3", "X4", "Y_pre", "Y_post")
SAMPLE_RULE = "n1=min(n-1,max(1,floor(n/5+0.5)));n0=n-n1"
FROZEN = {
    "p": 4, "r": 2, "a": 0.1, "b": 0.9, "h": 0.1,
    "error_sd": 1, "periods": 2, "treatment_effect": 0,
    "baseline_n": 500, "baseline_n1": 100, "baseline_n0": 400,
}


def _validate_config(config):
    if not isinstance(config, dict):
        raise ValueError("config must be a selected scenario dictionary")
    for key, expected in FROZEN.items():
        actual = config.get(key)
        if (not isinstance(actual, (int, float)) or isinstance(actual, bool)
                or not math.isfinite(actual) or actual != expected):
            raise ValueError(f"Frozen M01 parameter {key} must equal {expected}")
    if config.get("sample_size_rule") != SAMPLE_RULE:
        raise ValueError("Unrecognized sample-size policy")
    if config.get("nonbaseline_sample_status") != "sample_size_extension_not_paper_table4":
        raise ValueError("Nonbaseline sample sizes must be labelled extensions")


def group_counts(n):
    if not isinstance(n, int) or isinstance(n, bool) or n < 2:
        raise ValueError("n must be an integer number of units, at least 2")
    n1 = min(n - 1, max(1, math.floor(n / 5 + 0.5)))
    return n1, n - n1


def _normalization(config):
    a, b, r, p = (config[key] for key in ("a", "b", "r", "p"))
    first = (b ** (r + 1) - a ** (r + 1)) / ((b - a) * (r + 1))
    second = (b ** (2 * r + 1) - a ** (2 * r + 1)) / ((b - a) * (2 * r + 1))
    variance = p * (second - first * first)
    if not math.isfinite(variance) or variance <= 0:
        raise ValueError("Treated-population signal variance must be positive")
    return math.sqrt(variance)


def generate(config, n, seed):
    """n counts units. Only n=500 is the published fixed-size baseline."""
    _validate_config(config)
    n1, n0 = group_counts(n)
    if not isinstance(seed, int) or isinstance(seed, bool):
        raise ValueError("seed must be an integer")
    rng = random.Random(seed)
    p, r, a, b, h = (config[key] for key in ("p", "r", "a", "b", "h"))
    scale = _normalization(config)

    # X is sampled once per unit and shared by both periods.
    covariates = []
    for i in range(n):
        if i < n1:
            x = [a + (b - a) * rng.random() for _ in range(p)]
        else:
            x = [math.sqrt((a - h) + (b - a + 2 * h) * rng.random())
                 for _ in range(p)]
        covariates.append(x)
    means = [sum(xj ** r for xj in x) / scale for x in covariates]
    # Fresh errors in period 2; same conditional mean, no treatment term.
    pre_errors = [rng.gauss(0, config["error_sd"]) for _ in range(n)]
    post_errors = [rng.gauss(0, config["error_sd"]) for _ in range(n)]

    result = {"G": [1] * n1 + [0] * n0}
    for j in range(p):
        result[f"X{j + 1}"] = [x[j] for x in covariates]
    result["Y_pre"] = [mu + e for mu, e in zip(means, pre_errors)]
    result["Y_post"] = [mu + e for mu, e in zip(means, post_errors)]

    # These checks inspect this actual table. verify(config) does not.
    if tuple(result) != COLUMNS or any(len(v) != n for v in result.values()):
        raise AssertionError("Observed columns or requested row count changed")
    if sum(result["G"]) != n1 or result["G"].count(0) != n0:
        raise AssertionError("Actual group counts violate allocation rule")
    for i, x in enumerate(covariates):
        lo, hi = (a, b) if result["G"][i] else (0, 1)
        if not all(lo <= value <= hi for value in x):
            raise AssertionError("Covariate outside group-specific support")
        for label, errors in (("Y_pre", pre_errors), ("Y_post", post_errors)):
            if result[label][i] != means[i] + errors[i]:
                raise AssertionError("Within-row unit/period pairing changed")
    if not all(math.isfinite(v) for col in result.values() for v in col):
        raise AssertionError("Nonfinite observation")
    return result

"""Observed-only Ferman Table 1 panel, approved fixed J=10/T0=20 cell."""
import math
from random import Random

COLUMNS = ("G",) + tuple(f"Y_pre_{k:02d}" for k in range(1, 21)) + ("Y_post_01",)
FROZEN = {
    "J": 10, "N": 11, "T0": 20, "T1": 1, "K": 2, "rho": 0.5,
    "alpha": 0, "factor_innovation_variance": 0.75,
    "factor_initial_variance": 1, "error_variance": 1,
    "donors_type1": 5, "donors_type2": 5, "post_effect": 0, "burn_in": 0,
    "representation": "unit_wide_22_observed_columns",
    "sample_size_policy": "strict_n_equals_11",
}


def _validate(config):
    if not isinstance(config, dict) or set(config) != set(FROZEN):
        raise ValueError("Use the complete registered M11 scenario without extra parameters")
    for key, expected in FROZEN.items():
        value = config[key]
        if isinstance(expected, str):
            valid = value == expected
        else:
            valid = (isinstance(value, (int, float)) and not isinstance(value, bool)
                     and math.isfinite(value) and value == expected)
        if not valid:
            raise ValueError(f"Frozen M11 parameter {key} must equal {expected!r}")


def generate(config, n, seed):
    """n is exactly eleven units, not number of periods or independent worlds."""
    _validate(config)
    if not isinstance(n, int) or isinstance(n, bool) or n != 11:
        raise ValueError("M11 requires n=11: one treated unit and ten donors")
    if not isinstance(seed, int) or isinstance(seed, bool):
        raise ValueError("seed must be an integer")
    rng = Random(seed)
    factors = []
    for _ in range(2):
        state = rng.gauss(0, math.sqrt(config["factor_initial_variance"]))
        path = []
        for _ in range(21):
            state = config["alpha"] + config["rho"] * state + rng.gauss(
                0, math.sqrt(config["factor_innovation_variance"]))
            path.append(state)
        factors.append(path)
    panel = []
    for i in range(n):
        # Source: treated and first five donors belong to factor type one.
        factor = factors[0 if i <= 5 else 1]
        observed = [factor[s] + rng.gauss(0, math.sqrt(config["error_variance"]))
                    for s in range(21)]
        if i == 0:
            observed[20] += config["post_effect"]
        panel.append(observed)
    output = {"G": [1] + [0] * 10}
    for k in range(1, 21):
        output[f"Y_pre_{k:02d}"] = [row[k - 1] for row in panel]
    output["Y_post_01"] = [row[20] for row in panel]
    if tuple(output) != COLUMNS or any(len(column) != n for column in output.values()):
        raise AssertionError("Observed schema, time mapping or unit count changed")
    if output["G"] != [1] + [0] * 10:
        raise AssertionError("Treatment/donor assignment changed")
    if not all(math.isfinite(value) for column in output.values() for value in column):
        raise AssertionError("Nonfinite observation")
    return output

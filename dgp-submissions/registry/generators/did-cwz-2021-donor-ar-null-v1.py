"""M12: observed unit-wide donor-combination panel, fixed source scenarios."""
import math
import random

COLUMNS = ("G",) + tuple(f"Y_pre_{t:02d}" for t in range(1, 21)) + ("Y_post_01",)
FROZEN = {
    "J": 20, "T0": 20, "T_post": 1, "rho_epsilon": 0.6, "rho_u": 0.6,
    "innovation_variance": 0.64, "initial_variance": 1,
    "factor_variance": 1, "theta_T": 0,
}


def _validate_config(config):
    if not isinstance(config, dict) or set(config) != set(FROZEN) | {"weight_scheme"}:
        raise ValueError("Expected exactly the frozen M12 scientific parameters and weight_scheme")
    for name, expected in FROZEN.items():
        value = config[name]
        if (not isinstance(value, (int, float)) or isinstance(value, bool)
                or not math.isfinite(value) or value != expected):
            raise ValueError(f"Frozen M12 parameter {name} must equal {expected}")
    for name in ("J", "T0", "T_post"):
        if not isinstance(config[name], int):
            raise ValueError(f"{name} must be an integer")
    if config["weight_scheme"] not in ("W1", "W2", "W3", "W4"):
        raise ValueError("weight_scheme must be one of the four source-defined scenarios")


def _source_weights(scheme):
    if scheme == "W1":
        return [1 / 20] * 20
    if scheme == "W2":
        return [1 / 3] * 3 + [0.0] * 17
    if scheme == "W3":
        return [-1 / 20] * 20
    if scheme == "W4":
        return [1.0, -1.0] + [0.0] * 18
    raise ValueError("Unknown source weight scenario")


def _ar_series(rng, periods, rho, innovation_sd):
    # Source R function draws innovations, then an independent N(0,1) start.
    innovations = [rng.gauss(0.0, innovation_sd) for _ in range(periods)]
    previous = rng.gauss(0.0, 1.0)
    values = []
    for innovation in innovations:
        previous = rho * previous + innovation
        values.append(previous)
    return values  # initial draw is not observed; no additional burn-in


def generate(config, n, seed):
    """Return exactly n=21 unit rows in one jointly generated 21-period panel."""
    _validate_config(config)
    if not isinstance(n, int) or isinstance(n, bool) or n != 21:
        raise ValueError("M12 requires n=21 units (one treated plus 20 donors); no extension approved")
    if not isinstance(seed, int) or isinstance(seed, bool):
        raise ValueError("seed must be an integer")
    rng = random.Random(seed)
    periods = config["T0"] + config["T_post"]
    f1 = [rng.gauss(0.0, 1.0) for _ in range(periods)]
    f2 = [rng.gauss(0.0, 1.0) for _ in range(periods)]
    innovation_sd = math.sqrt(config["innovation_variance"])
    donors = []
    for slot in range(1, config["J"] + 1):
        residual = _ar_series(rng, periods, config["rho_epsilon"], innovation_sd)
        loading = slot / config["J"]
        donors.append([loading + f1[t] + loading * f2[t] + residual[t]
                       for t in range(periods)])
    extra_residual = _ar_series(rng, periods, config["rho_u"], innovation_sd)
    weights = _source_weights(config["weight_scheme"])
    treated = [sum(w * donor[t] for w, donor in zip(weights, donors)) + extra_residual[t]
               for t in range(periods)]
    treated[-1] += config["theta_T"]
    panel = [treated] + donors
    result = {"G": [1] + [0] * config["J"]}
    for t in range(config["T0"]):
        result[f"Y_pre_{t + 1:02d}"] = [unit[t] for unit in panel]
    result["Y_post_01"] = [unit[-1] for unit in panel]

    if tuple(result) != COLUMNS or any(len(column) != n for column in result.values()):
        raise AssertionError("Observed-only panel columns or unit count changed")
    if result["G"].count(1) != 1 or result["G"].count(0) != 20:
        raise AssertionError("Fixed treated/donor allocation changed")
    if not all(math.isfinite(value) for col in result.values() for value in col):
        raise AssertionError("Nonfinite observed value")
    return result

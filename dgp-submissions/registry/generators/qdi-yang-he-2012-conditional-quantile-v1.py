"""Yang & He (2012), published p.1114, Models 1--4; observed data only."""
import math
import random


def _validate(config):
    keys = ("x_df", "z_probability", "z_multiplier", "error_normal_mean",
            "error_normal_sd", "scale_intercept", "scale_x")
    for key in keys:
        v = config[key]
        if isinstance(v, bool) or not isinstance(v, (int, float)) or not math.isfinite(v):
            raise ValueError(key + " must be a finite number")
    coefficients = config["location_coefficients"]
    if len(coefficients) != 3 or not all(
            isinstance(v, (int, float)) and not isinstance(v, bool) and math.isfinite(v)
            for v in coefficients):
        raise ValueError("location_coefficients must contain three finite numbers")
    if config["x_df"] <= 0 or config["error_normal_sd"] <= 0:
        raise ValueError("Degrees of freedom and normal SD must be positive")
    if not 0 < config["z_probability"] < 1 or config["z_multiplier"] <= 0:
        raise ValueError("Both Z support points must have positive probability")
    if config["scale_intercept"] <= 0 or config["scale_x"] < 0:
        raise ValueError("The error scale must be positive for all X >= 0")
    if config["error_distribution"] not in ("normal", "lognormal"):
        raise ValueError("Unsupported error distribution")


def generate(config, n, seed):
    """Return only X, Z, Y as numeric lists; n iid observations, local RNG."""
    _validate(config)
    if isinstance(n, bool) or not isinstance(n, int) or n < 1:
        raise ValueError("n must be a positive integer")
    if isinstance(seed, bool) or not isinstance(seed, int):
        raise ValueError("seed must be an integer")
    rng = random.Random(seed)
    out = {name: [] for name in ("X", "Z", "Y")}
    a, bx, bz = config["location_coefficients"]
    for _ in range(n):
        # Chi-square(df) = Gamma(shape=df/2, scale=2); source df=2.
        x = rng.gammavariate(config["x_df"] / 2.0, 2.0)
        z = config["z_multiplier"] * int(rng.random() < config["z_probability"])
        latent_normal = rng.gauss(config["error_normal_mean"], config["error_normal_sd"])
        e = math.exp(latent_normal) if config["error_distribution"] == "lognormal" else latent_normal
        scale = config["scale_intercept"] + config["scale_x"] * x
        y = a + bx * x + bz * z + scale * e
        if not math.isfinite(y):
            raise ValueError("Non-finite generated response; no clipping or resampling is performed")
        out["X"].append(x)
        out["Z"].append(z)
        out["Y"].append(y)
    return out

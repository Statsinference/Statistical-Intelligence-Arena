"""Observed rows of the two-level varying-coefficient cluster model. No truth column."""
import math
import random

INDIVIDUAL_DIM = 3
CLUSTER_DIM = 2
COLUMNS = ("cluster", "U", "X1", "X2", "X3", "Z1", "Z2", "Y")


def alpha_population(u):
    """alpha_0(u): Section 5 sets all three components to sin(2*pi*u)."""
    value = math.sin(2.0 * math.pi * u)
    return (value, value, value)


def alpha_first_loading(u):
    """alpha_1(u), the loading of Z_i1 in A(u)."""
    value = math.cos(2.0 * math.pi * u)
    return (value, value, value)


def alpha_second_loading(u):
    """alpha_2(u), the loading of Z_i2 in A(u)."""
    value = math.sin(math.pi * u)
    return (value, value, value)


def cluster_coefficient(u):
    """beta(u): the coefficient vector applied to the cluster covariates Z_i."""
    value = math.sin(2.0 * math.pi * u)
    return (value, value)


def intercept(u):
    """beta_0(u), the outcome intercept, included per the Section 5 prescription."""
    return math.sin(2.0 * math.pi * u)


def cluster_random_coefficient(u, z, effect):
    """a_i(u) = alpha_0(u) + A(u) Z_i + e_i with A(u) = (alpha_1(u), alpha_2(u))."""
    base, first, second = alpha_population(u), alpha_first_loading(u), alpha_second_loading(u)
    z1, z2 = z
    return tuple(base[k] + first[k] * z1 + second[k] * z2 + effect[k]
                 for k in range(INDIVIDUAL_DIM))


def conditional_mean(u, x, z, effect):
    """E[y_ij | X_ij, Z_i, U_ij, e_i], the noise-free part of the outcome."""
    slope = cluster_random_coefficient(u, z, effect)
    loading = cluster_coefficient(u)
    return (intercept(u) + sum(x[k] * slope[k] for k in range(INDIVIDUAL_DIM))
            + z[0] * loading[0] + z[1] * loading[1])


def validate(config):
    for key in ("sigma", "random_effect_var", "query_u",
                "cluster_size_base", "cluster_size_scale"):
        if key not in config:
            raise ValueError("missing source parameter: " + key)
        if not math.isfinite(float(config[key])):
            raise ValueError(key + " must be finite")
    if len(config["query_x"]) != 3 or len(config["query_z"]) != 2:
        raise ValueError("complete query needs three X and two Z coordinates")
    if not all(math.isfinite(float(v)) for v in config["query_x"] + config["query_z"]):
        raise ValueError("query coordinates must be finite")
    if config["sigma"] <= 0:
        raise ValueError("sigma must be positive")
    if config["random_effect_var"] < 0:
        raise ValueError("random_effect_var must be nonnegative")
    if not 0 <= config["query_u"] <= 1:
        raise ValueError("query_u must lie in [0,1]")
    if config["cluster_size_base"] < 1 or config["cluster_size_scale"] < 0:
        raise ValueError("cluster size rule needs base >= 1 and nonnegative scale")


def generate(config, n, seed):
    validate(config)
    if isinstance(n, bool) or not isinstance(n, int) or n < 1:
        raise ValueError("n must be a positive integer")
    rng = random.Random(seed)
    sigma = float(config["sigma"])
    effect_sd = math.sqrt(float(config["random_effect_var"]))
    base = float(config["cluster_size_base"])
    scale = float(config["cluster_size_scale"])
    # Lower end of the source support for n_i = floor(|2*xi| + 6) with xi ~ N(0,1).
    minimum = max(1, int(base))
    out = {name: [] for name in COLUMNS}
    identifier = 0
    remaining = n
    while remaining > 0:
        identifier += 1
        if remaining < 2 * minimum:
            # The budget cannot hold one more drawn cluster plus a complete final one,
            # so the final cluster takes the remaining rows; remaining >= minimum here.
            size = remaining
        else:
            size = int(scale * abs(rng.gauss(0.0, 1.0)) + base)
            if size < minimum:
                size = minimum
            if remaining - size < minimum:
                # Keep the final cluster complete rather than truncating a drawn one.
                size = remaining
        if size < 1:
            raise ValueError("degenerate cluster size")
        z = tuple(rng.gauss(0.0, 1.0) for _ in range(CLUSTER_DIM))
        effect = tuple(rng.gauss(0.0, effect_sd) for _ in range(INDIVIDUAL_DIM))
        for _ in range(size):
            u = rng.random()
            x = tuple(rng.gauss(0.0, 1.0) for _ in range(INDIVIDUAL_DIM))
            y = conditional_mean(u, x, z, effect) + rng.gauss(0.0, sigma)
            for name, value in zip(COLUMNS, (identifier, u, x[0], x[1], x[2],
                                             z[0], z[1], y)):
                out[name].append(value)
        remaining -= size
    return out

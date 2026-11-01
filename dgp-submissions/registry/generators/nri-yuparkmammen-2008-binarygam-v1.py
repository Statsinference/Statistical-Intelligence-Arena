"""Observed-data generator for Yu, Park & Mammen (2008), Section 5.

Covariate distribution j=1 (independent components, each a standard normal truncated
to [-1, 1]) with response model i=1 (Bernoulli) or i=2 (Poisson). Only the observed
columns X1, X2, Y are returned: no probability, latent or oracle column is exported.
"""
import math
import random

FAMILIES = ("bernoulli", "poisson")
SOURCE_DISTRIBUTION = "truncated_standard_normal_independent"
COLUMNS = ("X1", "X2", "Y")


def expit(value):
    """Numerically stable logistic transform; the verifier re-derives it independently."""
    if value >= 0.0:
        return 1.0 / (1.0 + math.exp(-value))
    v = math.exp(value)
    return v / (1.0 + v)


def linear_predictor(x1, x2, config):
    """eta(x) = sin(pi x1) + 0.5 [x2 + sin(pi x2)], the source generator's predictor."""
    pi = config["eta_frequency"]
    return (config["eta_first_component_coefficient"] * math.sin(pi * x1)
            + config["eta_second_component_coefficient"] * (x2 + math.sin(pi * x2)))


def conditional_mean(x1, x2, config):
    """m(x) = E[Y | X = x] under the scenario's link."""
    eta = linear_predictor(x1, x2, config)
    if config["family"] == "bernoulli":
        return expit(eta)
    return math.exp(eta)


def validate(config):
    if config["family"] not in FAMILIES:
        raise ValueError("family must be one of " + ", ".join(FAMILIES))
    if config["covariate_distribution"] != SOURCE_DISTRIBUTION:
        raise ValueError("only the source covariate distribution j=1 is implemented")
    if float(config["covariate_correlation"]) != 0.0:
        raise ValueError("the implemented distribution j=1 has independent components")
    low, high = float(config["truncation_min"]), float(config["truncation_max"])
    if not math.isfinite(low) or not math.isfinite(high) or low >= high:
        raise ValueError("truncation bounds must be finite and ordered")
    for key in ("eta_frequency", "eta_first_component_coefficient",
                "eta_second_component_coefficient"):
        if not math.isfinite(float(config[key])):
            raise ValueError(key + " must be finite")
    for key in ("query_x1", "query_x2"):
        value = float(config[key])
        if not math.isfinite(value) or not low <= value <= high:
            raise ValueError(key + " must lie inside the covariate support")


def _truncated_normal(rng, low, high):
    """Rejection sampling of one N(0,1) draw conditioned on [low, high]."""
    while True:
        value = rng.gauss(0.0, 1.0)
        if low <= value <= high:
            return value


def _bernoulli(rng, probability):
    return 1 if rng.random() < probability else 0


def _poisson(rng, rate):
    """Knuth product method; the source rates here stay below 6, so it is exact and fast."""
    if rate <= 0.0:
        return 0
    limit = math.exp(-rate)
    count = 0
    product = 1.0
    while True:
        product *= rng.random()
        if product <= limit:
            return count
        count += 1


def generate(config, n, seed):
    """Return observed columns only: dict[str, list[number]], length n per column."""
    validate(config)
    if isinstance(n, bool) or not isinstance(n, int) or n < 1:
        raise ValueError("n must be a positive integer")
    rng = random.Random(seed)
    low, high = float(config["truncation_min"]), float(config["truncation_max"])
    family = config["family"]
    x1_column, x2_column, y_column = [], [], []
    for _ in range(n):
        x1 = _truncated_normal(rng, low, high)
        x2 = _truncated_normal(rng, low, high)
        mean = conditional_mean(x1, x2, config)
        if family == "bernoulli":
            y = _bernoulli(rng, mean)
        else:
            y = _poisson(rng, mean)
        x1_column.append(x1)
        x2_column.append(x2)
        y_column.append(y)
    return {"X1": x1_column, "X2": x2_column, "Y": y_column}

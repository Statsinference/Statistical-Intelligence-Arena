"""DGP collection areas, including a separate legacy mixed-design bucket.

These are catalog categories, not claims that the current benchmark evaluator
supports every target, dimension, dependence structure, or study design.
"""
from __future__ import annotations

DOMAINS = {
    'ate': 'ATE — Average Treatment Effect',
    'cate': 'CATE — Conditional Average Treatment Effect',
    'mediation': 'Mediation — Direct and Indirect Effects',
    'iv': 'IV — Instrumental Variables',
    'proximal': 'Proximal Causal Inference',
    'did': 'DiD — Difference-in-Differences',
    'synthetic_control': 'Synthetic Control',
    'nonparametric_regression': 'Nonparametric Regression',
    'quantile': 'Quantile Inference',
    'semi_supervised': 'Semi-Supervised Inference',
    'missing_data': 'Missing Data',
}

_ALIASES = {
    # Keep historical values in the legacy bucket; do not infer a design.
    'did_sc': 'did_sc',
    'did_/_synthetic_control': 'did_sc',
    'difference_in_differences': 'did',
    'difference_in_difference': 'did',
    'synthetic_control_method': 'synthetic_control',
    'nri': 'nonparametric_regression',
    'nonparametric': 'nonparametric_regression',
    'nonparametric_regression_inference': 'nonparametric_regression',
    'nonparametric_regression_estimation': 'nonparametric_regression',
    'qr': 'quantile', 'qdi': 'quantile', 'quantile_distribution': 'quantile', 'quantile_regression': 'quantile',
    'quantile_inference': 'quantile', 'quantile_distribution_inference': 'quantile',
    'quantile_and_distribution_inference': 'quantile',
    'semi_supervised_inference': 'semi_supervised',
    'semi_supervised_learning': 'semi_supervised',
    'semisupervised': 'semi_supervised', 'ssl': 'semi_supervised',
    'ssi': 'semi_supervised',
    'missing': 'missing_data', 'missing_data_inference': 'missing_data',
    'missingness': 'missing_data', 'mdi': 'missing_data',
}


def to_domain(value: str | None) -> str | None:
    if value is None:
        return None
    s = ' '.join(str(value).strip().split())
    key = s.lower().replace('-', '_').replace(' ', '_')
    if key in DOMAINS:
        return key
    if key in _ALIASES:
        return _ALIASES[key]
    for domain, label in DOMAINS.items():
        if s.casefold() == label.casefold():
            return domain
    return None


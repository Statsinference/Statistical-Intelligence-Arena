"""The six official StatsArena causal-inference task families.

The submitter chooses ONE primary family; extraction may suggest secondary
family tags. A human reviewer confirms the final scientific classification.
"""
from __future__ import annotations

DOMAINS = {
    'ate': 'ATE — Average Treatment Effect',
    'cate': 'CATE — Conditional Average Treatment Effect',
    'mediation': 'Mediation — Direct and Indirect Effects',
    'iv': 'IV — Instrumental Variables',
    'proximal': 'Proximal Causal Inference',
    'did_sc': 'DiD / Synthetic Control',
}

# Accepted form-label equivalents and pre-existing package family identifiers.
def to_domain(value: str | None) -> str | None:
    if value is None:
        return None
    s = ' '.join(str(value).strip().split())
    key = s.lower().replace('-', '_').replace(' ', '_')
    if key in DOMAINS:
        return key
    for domain, label in DOMAINS.items():
        if s.casefold() == label.casefold():
            return domain
    return None



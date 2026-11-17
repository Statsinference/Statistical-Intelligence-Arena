"""Source-bound catalog placement for eleven legacy mixed-family submissions.

The SHA-256 is of the submitted ZIP, not an endorsement of its scientific
content. A changed ZIP is not automatically classified. Unknown mixed-family
submissions are routed to human review rather than guessed.
"""
LEGACY_DESIGNS = {
    'did-abadie-lhour-2021-nonlinear-null-v1': (
        '12ed713f0ef5464720af0223e5b3d34990ed3f244f0525ab5eaf2a093f130fdf',
        'synthetic_control',
        'Two-period treated-group panel from a penalized synthetic-control study; the design may also be used for DiD.'),
    'did-cwz-2021-donor-ar-null-v1': (
        '8159cdd3fa3d3c7da42557353657a93418df0e4e3e745fb6ee083f9b6a182146',
        'synthetic_control', 'Treated-unit and donor panel for counterfactual/synthetic controls.'),
    'did-ferman-2021-two-factor-null-v1': (
        '3dcd9582d7ce5b7b8851217464fdacbf5079de20dec7a2c8b9c4c6ad6103d314',
        'synthetic_control', 'Treated-unit and donor panel for a synthetic-control estimator.'),
    'did-karmakar-2025-code-truncated-cluster-null-v1': (
        '15e2a04225ae67a2a87a5e9420bb7d02449b0fd2c4da6bcb92f43921d798facb',
        'synthetic_control', 'Cluster panel adapted from a penalized synthetic-control study.'),
    'did-shi-2026-poisson-proxy-logrr-v1': (
        'dfdeecac2dea05aadb91108e7efe8ef598a20088cfc7699d9f0084420b37a61a',
        'synthetic_control', 'Proxy and donor panel for proximal synthetic control; the submitted estimand is a log mean ratio, not ATT.'),
    'did-santanna-zhao-2020-panel-dgp1-v1': (
        'b9defbcbdc8290f7cf489d5227113adc705be56fb7feb187cc3d99aea399f908',
        'did', 'Two-period panel for doubly robust difference-in-differences.'),
    'did-shaikh-toulis-2021-conditional-first-adopter-null-v1': (
        'b61ea6041845141104c0b1a6d95e0838b951b9aa3f24545900c5ec8c2556a77e',
        'did', 'Staggered-adoption randomization-test DGP, not verified as DiD; its conditional first-adopter target requires scientific review.'),
    'did-ye-2024-bracketing-v1': (
        '9fde097a2af389c55cd7feb78f53b5039142a6290d8c0d3fbed1ab2b7acbb410',
        'did', 'Three-group multi-period design for DiD bracketing.'),
    'did-ye-2024-code-case2-gaussian-bracketing-v1': (
        '07d3e2c046e15f2f255d12c4f2f91a364eff217de9ec31f3743404e1193acdd6',
        'did', 'Three-group design for DiD bracketing with nonparallel trends.'),
    'did-zhao-cui-2025-bridge-iv-v1': (
        'f6fe23488549481c09b46d1bfe5335042b0ff3fe07500ff98ade848a9a78654d',
        'did', 'Instrumented DiD with bridge confounding; the submitted target is ATE.'),
    'did-zhao-cui-2025-instrumented-v1': (
        '65686f84277b4595b16f5dcbb7dce5b03e6d8798e084e88a524ed7073770b953',
        'did', 'Instrumented DiD; the submitted target is ATE.'),
}


def legacy_design(record_id, zip_sha256):
    """Return an exactly source-bound placement, otherwise require review."""
    item = LEGACY_DESIGNS.get(record_id)
    return item[1:] if item and zip_sha256 and item[0] == zip_sha256 else None

# Publication labels and DGP keywords

The Contributing paper list, Registry index, and domain lists display each article
as **Paper title (venue)**. This suffix is derived from the submitted
`source.venue`, with known venue names in the citation used only as a fallback.
UI aliases include JASA, JRSSB, AoS, JoE, ICML, and NeurIPS. Biometrika is already
short and is retained. An unreported venue is not guessed or assigned a journal.
Full citations and original venue text remain in the scientific JSON.

## Keywords describe a DGP, not a paper

The **Keywords** column precedes **Generator.py**. When a paper contributes
multiple mechanisms, numbered DGPs, keyword groups, and generators correspond
one-to-one in the same order. Different mechanisms are not merged into a
paper-wide set of properties.

Existing `collection.json.properties` fields already supply most tags:

| Submitted field | Positive label |
|---|---|
| `interactions: true` | Interactions |
| `nonlinear: true` | Nonlinearity |
| `high_dimensional: true` | High-dimensionality |
| `interference: true` | Interference |
| `effect_heterogeneity: true` | Effect heterogeneity |
| `heteroskedasticity: true` | Heteroskedasticity |
| `panel_data: true` | Panel data |
| `longitudinal: true` | Longitudinal |
| `weak_overlap: true` | Weak overlap |
| `heavy_tailed_noise: true` | Heavy-tailed noise |

`nonlinear: false` produces **Linearity**. Missing fields mean unknown, not false.
Only real JSON booleans are flags, not strings such as `"false"` or the number 1.

Effect heterogeneity may also come from an explicit description of the mechanism
in its submitted name or property notes, such as "heterogeneous treatment effects"
or "X1 and X2 modify treatment effect". It is never inferred merely because the
paper studies CATE, a DGP contains interactions, or multiple scenarios exist.
Heteroskedasticity and effect heterogeneity are distinct labels.

**Interference and high-dimensionality require explicit positive declarations.**
The parser does not interpret "no interference" as interference, and it does not
infer high dimensionality from the number of variables. Shared latent factors,
within-person dependence, and panels are not automatically labeled interference.
The existing high_dimensional=false declarations are respected.

Nonlinearity applies to the submitted **whole mechanism**. A nonlinear propensity
or link function can coexist with a linear outcome or bridge; the tag does not
assert that every equation is nonlinear.

## Optional additional source keywords

Contributors may optionally add `properties.keywords`, a list of short English
labels, without replacing the existing submission format. Known aliases are
standardized; other plain English labels such as "Invalid instruments" remain
source-provided descriptions. An explicit false flag vetoes a conflicting
positive keyword. Neither a missing tag nor successful parsing certifies a
scientific absence or presence; all records retain their review status.

`registry/catalog.json` stores the derived `venue_abbreviation`, `keywords`, and
`keyword_evidence` fields. Each evidence entry records a source field, its
submitted value or exact supporting phrase, and the extraction method. The raw
DGP JSON, source ZIP, equations, parameters, true values, and generator bytes
are not modified to add these display labels.

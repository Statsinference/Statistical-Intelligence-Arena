# Structured ZIP format · no LLM required

Student sends **one `.zip` archive**. Each DGP mechanism inside it must have a `collection.json` and `config.json`. `schema.csv` and `source_audit.json` are strongly recommended. `generator.py`, `truth.py`, and `checks/report.json` are optional and NEVER executed by intake.

```text
student.zip/
  my-dgp-1/
    collection.json        # source, family, generating equations, estimand
    config.json            # scenarios & parameter settings
    schema.csv             # observed variables
    source_audit.json      # evidence/changes
    checks/report.json     # optional checked per-scenario truth
  my-dgp-2/
    collection.json
    config.json
```

**Display titles:** `collection.json.title` must be in English for new submissions. If a source uses another language, provide `title_en` as an English display title and retain `title` unchanged as the original text. The Registry automatically uses the English title for the clickable DGP Mechanism link and detail-page heading. Legacy source titles are preserved verbatim in the JSON record. No AI/API translation is performed.

Minimal `collection.json` example (values illustrative):

```json
{
  "contribution_id": "sample-ate-001",
  "family": "ate",
  "kind": "synthetic_dgp",
  "title": "Simple randomized ATE",
  "source": {"citation": "Example et al., 2024", "url": "https://doi.org/10.1000/example", "locator": "Sec. 4, Simulation 1"},
  "equations": ["X ~ N(0, 1)", "A ~ Bernoulli(0.5)", "Y = 1 + 2*A + X + epsilon; epsilon ~ N(0, 1)"],
  "estimand": {"definition": "ATE = E[Y(1)-Y(0)]"},
  "truth": {"reference_value": 2, "method": "Direct intervention contrast"},
  "sampling": "IID units"
}
```

Matching `config.json`:

```json
{"scenarios": {"original": {"n": 500}}}
```

Real submissions must use the *actual* paper citation, exact source location, faithful formulas and scenario-specific truth if available. If the true value is not known, do not invent it. A machine-valid submission does not mean a scientifically accepted result.

The parser reads `collection.json.family` automatically. Supported primary areas are `ate`, `cate`, `mediation`, `iv`, `proximal`, `did_sc`, `nonparametric_regression`, `quantile`, `semi_supervised`, and `missing_data`. The current `did_sc` area combines DiD and synthetic control; identify the actual design in the submission. Unknown family values are flagged for manual classification.

**Archive security:** no submitted Python is executed, all entries are path-checked, archives over 25 MiB or 120 MiB expanded size are rejected, and duplicate DGP IDs block automatic indexing.

## Optional LaTeX equations (recommended)

GitHub renders math in Registry detail pages with standard `$$ ... $$` blocks. No LLM or API key is needed.

For reliable, publication-quality math, an entry in `collection.json`'s `equations` list may be an object with both the original text and a verified LaTeX expression:

```json
{
  "equations": [
    {
      "expression": "A|X ~ Bernoulli(p(X))",
      "latex": "A\\mid X\\sim\\operatorname{Bernoulli}(p(X))"
    },
    {
      "expression": "Y=2A+X1+ε",
      "latex": "Y=2A+X_1+\\varepsilon"
    }
  ]
}
```

Existing submissions containing plain strings remain valid. The Registry applies conservative formatting to recognizable notation such as Greek letters, subscripts, normals, and numeric covariance matrices, while leaving unsupported prose unchanged. Every detail page preserves the **exact original source equations** in an expandable section for scientific review.

Rendering is not mathematical validation: the author/reviewer must confirm that LaTeX exactly matches the source paper. An unknown true value must stay unknown.

## Latent variables (optional explicit metadata)

To make latent-variable identification complete rather than heuristic, contributors may include an **optional** `latent_variables` list in `collection.json`:

```json
"latent_variables": [
  {"name": "U", "role": "unmeasured_confounder", "dimension": 1}
]
```

For existing ZIPs without this key, the intake parser conservatively collects **latent-variable candidates** from explicit stochastic declarations in `equations` and preserves evidence. These candidates require scientific review; a missing candidate does not prove there are no latent variables. An explicitly provided empty list is distinguishable from missing metadata. `generator.py` is never executed by the intake workflow. Existing ZIPs remain valid and can be re-indexed without re-uploading.


## Paper Title and downloadable source generator

The paper list displays the **paper title only**. If available, specify
`collection.json.source.title` (or `paper_title`) to avoid parsing the title
from a bibliographic citation. Full citations stay in the individual DGP detail
records.

Every DGP with an existing `generator.py` member in its ZIP receives a
corresponding **Generator.py** link in the domain lists and paper tables. The
intake copies the exact UTF-8 source bytes to
`registry/generators/<contribution_id>.py`. This source file is **never run**
by GitHub Actions and may require other files/dependencies from the submitted
ZIP before it can generate data independently. If no valid source is present,
the table shows an em dash rather than an invented link.


## English-only detail page (original scientific content preserved)

The browsable DGP detail page is rendered in English. For new source ZIPs,
supply an optional \`english_display\` object inside \`collection.json\`, for example:

```json
{
  "english_display": {
    "locator": "Section 4, simulation 1, PDF pp. 10-11",
    "equations": [
      {"latex": "X\\sim\\mathcal{N}(0,1)"},
      {"latex": "A\\mid X\\sim\\mathrm{Bernoulli}(0.5)"}
    ],
    "assumptions": ["Independent observations; randomized binary treatment"],
    "estimand": "ATE = E[Y(1)-Y(0)]"
  }
}
```

When supplying \`equations\`, give one display entry per source equation
entry, in the same order, so that none of the mechanism is inadvertently
omitted. Use \`latex\` and optional English \`notes\` for each item.
The source \`equations\` and all original-language metadata remain unchanged
in the extracted JSON and uploaded ZIP.

Without English fields, a source-language sentence is not silently translated
or reinterpreted. The detail page displays an English "translation pending"
message linked to the raw scientific JSON. Curated English transcriptions for
earlier submissions are maintained separately in \`english_details.json\`,
not embedded in DGP parsing code.

Numeric covariance matrices are rendered as multiline LaTeX
\`bmatrix\` arrays with explicit \`&\` column and \`\\\` row separators.

# Upload a structured DGP ZIP here

**[Open GitHub's ZIP upload screen](https://github.com/Statsinference/stats-inference-arena/upload/main/dgp-submissions/incoming)** to upload exactly one `.zip` file, then commit to `main` if permitted.

You do not need an Issue, another website, a model/API key, or a manual JSON form. GitHub Actions automatically reads the existing `collection.json` files within the ZIP and infers the research area.

- Valid: a ZIP with at least one `collection.json`, matching `config.json` and DGP equations.
- One ZIP may include many DGP folders; the tested Proximal example has 10.
- Max 25 MiB per ZIP when uploading through GitHub's website.
- Keep the ZIP as one file (do **not** unzip it in `incoming/`).

After submitting, open [Actions](https://github.com/Statsinference/stats-inference-arena/actions/workflows/dgp-submissions.yml) and then [six-area registry](../registry/INDEX.md). The result is a **draft** awaiting scientific review.

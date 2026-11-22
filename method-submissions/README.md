# Method submissions

[View submitted methods](received/README.md) · [Submit a method](https://github.com/Statsinference/Statistical-Intelligence-Arena/issues/new?template=method-submission.yml)

Authors with repository access can submit a method link, research domain and completed Markdown checklist in a private GitHub issue. Use the [method submission guide](../website/method-submissions/README.md) to prepare the materials. Contact a maintainer if you need access.

The submission sync workflow copies valid submissions into `method-submissions/received/` and updates the list above. It runs after issue changes, on a schedule and on manual dispatch. Integration checks are stored separately in `checks/`.

The workflow reads issues in this repository using its built-in Actions token. Each submission remains available for maintainer review.

The earlier `service/` backend is unused by this GitHub-native flow. No Vercel deployment, personal access token or Turnstile key is required.

# Method submissions

[View submitted methods](received/README.md) · [Public intake](https://github.com/Statsinference/statsinference.github.io/issues?q=is%3Aissue+in%3Atitle+%22%5BMethod+submission%5D%22)

Authors submit a Hugging Face model link through **Submit your method** on the website and confirm it on GitHub. Submitted links are public in the website repository; this research repository keeps its existing visibility.

The submission sync workflow copies confirmed links into `method-submissions/received/` and updates the list above. It runs every ten minutes, on workflow updates, and on manual dispatch. GitHub may delay scheduled runs. Integration checks are stored separately in `checks/` and do not appear as genuine submissions.

The workflow uses a pinned and SHA-256-verified copy of the public intake parser. It reads public issues and writes only this submission folder using this repository's built-in Actions token. It does not read, change, publish or execute any DGP or submitted model.

The earlier `service/` backend is unused by this GitHub-native flow. No Vercel deployment, personal access token or Turnstile key is required.

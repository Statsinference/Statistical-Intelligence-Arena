# Private method submissions

[Open the internal submission list](https://github.com/Statsinference/stats-inference-arena/issues?q=is%3Aissue+in%3Atitle+%22%5BMethod+submission%5D%22)

Each accepted website submission creates one issue in **this private repository**, titled `[Method submission] owner/model`. Only accounts with access to this repository can view the list. Close an issue after reviewing it. Submitting does not automatically run a model or publish a leaderboard result.

## Activation status

The button and Hugging Face form are implemented. **External intake is not active until the service is deployed and the public configuration is enabled.** No credentials have been supplied or committed. The form must stay disabled until a real private-inbox test succeeds.

## One-time deployment

1. Deploy this repository to a separate Vercel project with root directory `method-submissions/service`, framework preset **Other**, Node.js 22. Leave the existing GitHub Pages website and its deployment unchanged. Do not deploy the repository root or any research files.
2. Create a GitHub fine-grained token restricted to **Statsinference/stats-inference-arena** with **Issues: read and write** and the mandatory metadata-read permission. No contents, Actions, administration or other repository access is needed. Complete organization approval if required. Store it only in the Vercel environment as `GITHUB_SUBMISSIONS_TOKEN`.
3. Create a Cloudflare Turnstile widget allowing only `statsinference.github.io`. Store its private secret in Vercel as `TURNSTILE_SECRET_KEY`; its public sitekey goes in the website config. The server validates the hostname and `method_submit` action. Never place either secret in GitHub source, a browser, an issue, a URL, or chat.
4. In the public website repository, edit **only** `assets/submission-config.json`: set `endpoint` to the production `https://YOUR-PROJECT.vercel.app/api/submit`, set `turnstileSiteKey` to the widget's public sitekey, and set `enabled` to `true`. The placeholder is not an endpoint; use the actual deployment address. Ensure production deployment protection permits browser POST/OPTIONS requests.
5. Submit one clearly marked test model link from the real website. Confirm a private issue was created, the submitter receives only a receipt, and a logged-out visitor cannot read the issue/list. Close the test issue. Run `npm test` for isolated API tests; these do not constitute a live integration test.

Configure a production rate-limit rule for POST `/api/submit` in the hosting firewall (for example, 5 requests per minute per client IP), and monitor abuse. CORS is not authentication; Turnstile verification is mandatory. Hosting providers may retain infrastructure logs; this service does not log submission bodies or credentials. The inbox inherits this repository's access: keep it Private and review collaborator access. The handler refuses new writes if the repository is not private, but cannot protect old issues after an administrator makes the repository public.

## Scope

The service accepts a Hugging Face **model** URL (optionally `/tree/revision`) and the currently selected research domain. Query parameters, credentials, non-Hugging-Face URLs, datasets and Spaces are rejected. It never follows, downloads or executes submitted links. It exposes no endpoint for listing or reading private submissions. No public issues/PRs, no forwarding to the website repository, and no changes to the DGP collection workflow.

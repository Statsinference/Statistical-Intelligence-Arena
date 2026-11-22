# Direct website submissions

## Status

The receiver and ten domain-specific collection lists are implemented. The website form is prepared on `feature/direct-domain-submissions` in `Statsinference/statsinference.github.io`. **The receiver has not been deployed or given a GitHub write credential, and the new form is not enabled on the live website.** Existing Issue-based intake remains unchanged until this direct route is tested end to end.

The requested flow is: choose one top-level research domain, paste a Hugging Face model link, submit on the website. No submitter GitHub account, Issue or pull request. No subdomains. The receiver uses the team's server-side credential to append a link, UTC receipt time and receipt identifier to `method-submissions/received/<domain>/README.md`. [Browse the legacy list folders](received/).

## One-time activation by a maintainer

1. Connect a backend host such as Vercel. Import this repository into a separate API project, with root directory `method-submissions/service`, framework preset Other and Node.js 22. Do not deploy the research repository root or move the existing GitHub Pages website.
2. Create a GitHub fine-grained token restricted to **Statsinference/stats-inference-arena** with **Contents: read and write** and metadata read. Complete organization approval when required. Store it only as the server environment variable `GITHUB_SUBMISSIONS_TOKEN`. Set `SUBMISSIONS_ENABLED=true`. The old Issues-only token is not sufficient. Do not put credentials in source, URLs, public config or chat. GitHub token permissions apply to repository contents, not a path; the service itself restricts writes to the fixed domain list paths.
3. Allow anonymous POST/OPTIONS requests to the production `/api/submit` route. Configure a hosting firewall rate limit before enabling the public form (for example 5 POST requests per 10 minutes per client IP). The service also imposes request-size limits, duplicate suppression, an instance-local burst limit and a durable maximum of 50 new entries per domain per UTC day. The local burst limit alone is not a distributed rate limiter.
4. In the website feature branch, set `assets/submission-config.json` to `{"enabled":true,"mode":"direct","endpoint":"ACTUAL_HTTPS_ENDPOINT_ENDING_IN_/api/submit"}`. The text here is not an endpoint. Use the actual deployment URL. Bump only the submission JS/CSS cache versions in `index.html`.
5. Submit the owner's existing public model link using a browser with no GitHub authentication. Confirm that the selected domain's README really contains the row before merging the website branch. A successful local mock or GET health check is not proof of live writes.

Only one GitHub file is written per submission. The API uses the current content SHA, retries concurrent conflicts, preserves existing validated rows, and treats duplicate domain/link pairs as the same receipt. It returns success only when GitHub confirms the file commit, or when the same link is already stored. The receiver never creates Issues, downloads a submitted model, runs its code, changes repository visibility, or writes to DGP/baseline/leaderboard files. The existing Issue archive and synchronization workflow do not modify the nested domain folders.

## Tests

Run `npm test` inside `method-submissions/service`. The 24 local tests use injected mock storage and cover all ten domains, duplicate and concurrent submissions, URL/schema/path validation, corrupted-list protection, unavailable credentials, quotas and failure acknowledgements. No live submissions were made by these tests. The frontend was separately checked locally for no GitHub redirects, actual selected-domain payload, failure recovery, unchanged leaderboard data and 320/390/768/1440px layouts.

The health endpoint returns only `ok` and `configured`, not credentials or stored submissions. CORS restricts browser origins but is not authentication. Hosting providers may retain infrastructure logs; the handler does not log submissions or credentials.

Official setup references: GitHub repository contents API and Vercel project/environment configuration.

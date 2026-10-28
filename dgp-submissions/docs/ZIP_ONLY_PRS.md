# ZIP-only contributions through a private fork

## Contributor workflow

The repository remains private. Outside collaborators need Read access, not Write
access to the upstream repository. An administrator must enable private forking
at the organization and repository levels before this route is available.

1. Fork `Statsinference/stats-inference-arena` into an allowed account.
2. In your fork, upload a structured ZIP to `dgp-submissions/incoming/`.
3. Open a pull request targeting `Statsinference/stats-inference-arena:main`.
4. Wait for **DGP ZIP-only** and the review preview; fix failures in your fork.
5. A maintainer reviews and merges. No automatic merge is configured.

Use a simple ZIP filename containing letters, digits, periods, hyphens or
underscores, beginning with a letter or digit. One PR can submit several ZIPs.
There is a 25 MiB limit per compressed file. Files must be placed directly in
`incoming/`, not a new nested directory. Existing ZIPs can be updated, but such
updates need the same human review as new submissions.

## What is checked

The complete Git diff against the PR's merge base is inspected, without path
filtering. Only additions and modifications of regular, non-executable `.zip`
files in `dgp-submissions/incoming/` pass. README changes, parser changes,
tests/workflow edits, generated catalog edits, deletions, renames, symlinks,
submodules and non-ZIP blobs fail. Unknown or incomplete diffs fail closed.

The trusted parser then validates the uploaded archives and produces a preview.
A failure in one of THIS PR's ZIPs fails the check, even when the tolerant main
intake would retain an earlier valid version. An unrelated old bad ZIP does not
by itself block the PR. Passing these checks is not scientific approval.

## Trust and merge boundary

The gate runs on `pull_request_target` using the base repository's workflow and
base commit. It fetches PR objects without checking out the PR. Only approved
ZIP blobs are copied into an ephemeral preview workspace. Submitted Python,
workflows, build files, dependency lists and generators are never executed.
The PR job has read-only repository contents permission and only adds commit
statuses. It cannot push code or merge. A new PR commit triggers a new check;
its verdict is attached to the exact checked SHA, not to a previously reviewed
version. A changed head or base invalidates the review and requires a rerun.

This ZIP-only policy applies to all PRs targeting main; there is no automatic
exemption for author names, association labels or contributor-controlled data.
Maintainer code changes require a separate, deliberate maintenance process.

## Administrator setup (not configured by committing these files)

- Organization Settings → Member privileges → Repository forking: permit private
  forks where permitted by your organization/enterprise policy.
- Repository Settings → General → Features: select **Allow forking**.
- Keep outside collaborators at **Read**. Do not grant upstream Write just to
  upload data.
- Where the repository plan supports private branch protection/rulesets, require
  a PR, at least one maintainer approval and the **DGP ZIP-only** status check
  on `main`. Restrict bypasses; dismiss stale approvals or require latest-push
  approval. Select this check from GitHub Actions when configuring its source.
- Do not enable sending secrets or write tokens to ordinary fork `pull_request`
  jobs. The trusted base gate above handles submission review itself.

Without required status checks, a red check is a warning, not an absolute block
on a maintainer pressing Merge. Read-only contributors still cannot merge into
upstream. Do not merge red, missing, stale or incomplete results. A plan or
organization policy may require an administrator to enable the required-check
feature. Keep the repository private; public visibility is not needed here.

After an approved merge, the existing main-only publisher updates Contributing
and the Registry. Main README, benchmark website and core code remain separate.

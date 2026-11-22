# Leaderboard source

The private research repository holds the leaderboard source in [`website/`](../website/). The import preserves the exact deployed tree and commit history through [`356e6cf`](https://github.com/Statsinference/statsinference.github.io/commit/356e6cf7dcdb371bb5b55e9e46130b200725b907), including the six benchmark cards, result summaries, contribution forms and checks. [`site/`](../site/) contains the earlier demo and its downloads.

## Preview and publish

Preview the leaderboard from the repository root.

```sh
python -m http.server 8000 --bind 127.0.0.1 --directory website
```

Open [the local leaderboard](http://127.0.0.1:8000/) after starting the server.

The [live leaderboard](https://statsinference.github.io/) is published by GitHub Pages from the [deployment repository](https://github.com/Statsinference/statsinference.github.io). Maintain `website/` in the private repository. Submit data proposals and method issues there through the [contribution guide](../CONTRIBUTING.md).

To deploy a reviewed revision from the private repository, publish only the `website/` subtree to the deployment repository's `main` branch.

```sh
git subtree push --prefix=website https://github.com/Statsinference/statsinference.github.io.git main
```

## Previous repository records

- Continue review in the private repository at [PR #32](https://github.com/Statsinference/Statistical-Intelligence-Arena/pull/32) and [PR #33](https://github.com/Statsinference/Statistical-Intelligence-Arena/pull/33). The original proposal files and commit authors are preserved.
- [Git history bundle](archive/leaderboard/public-pages-history.bundle) contains all 26 branch heads and the available pull request refs, including the submitted commits for PRs #8 and #9.
- [GitHub discussion snapshot](archive/leaderboard/github-discussions.json) contains the eight pull requests and issue #3, including their states, descriptions, changed files and recorded discussions at capture time. PRs #8 and #9 were open at capture time and await review.
- [Repository inventory](archive/leaderboard/github-repository-inventory.json) records deployment and workflow metadata. The [Actions archive](archive/leaderboard/statarena-pages-actions.zip) includes the available logs and build artifacts with a [SHA-256 checksum](archive/leaderboard/statarena-pages-actions.sha256).

To browse a submission from the archived Git refs, clone the bundle into a separate directory.

```sh
git clone --mirror docs/archive/leaderboard/public-pages-history.bundle statarena-pages-archive.git
git --git-dir=statarena-pages-archive.git show refs/pull/9/head
```

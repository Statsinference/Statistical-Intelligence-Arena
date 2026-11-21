# Publishing a reviewed mediation result

After checking the submission and its version, score its complete predictions CSV with the private mediation v1.0 grader. Save the grader's aggregate JSON on the maintainer's machine. From the website repository root, use the archived issue and that score to prepare the public result. Substitute the actual issue filename and score path.

```sh
python method-submissions/approve_mediation.py method-submissions/received/issue-000123.json /path/to/official-score.json --family other
```

Choose `pfn` for an RFN-family entry or `other` for another estimator. Review the change to `data/mediation-reviewed.json` and publish it to the website's main branch through the usual Git review. Pages then displays the method in the [mediation leaderboard](https://statsinference.github.io/#domain=mediation). Repeating the command for the same issue updates its existing result.

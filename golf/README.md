ARC Code Golf Submission

Contents
- `submission/`: 400 self-contained, minified solver files (one per competition taskNNN).
- `tools/`: tiny utilities to validate, smoke-test, package, and evaluate.
- `submission.zip`: packaged archive of the files in `submission/`.
 - `report.txt`: per-task length and estimated score summary generated at submission time.

Quick Start
- Validate: `make -C golf validate`
- Smoke test: `make -C golf smoke`
- Package: `make -C golf package` (writes `golf/submission.zip`)
- Submission: `make -C golf submission` (validate + package + write `golf/report.txt`)
- Evaluate: place the competition dataset under `data/google-code-golf-2025/` (as extracted from the zip), then `make -C golf eval`

Notes
- Files are self-contained: no imports, a single `solve_<hexid>(I)` per file, end with `return O`.
- Evaluation uses the competition task order (`taskNNN.json`), not ARC AGI hex IDs.
- For code golf scoring based on archive size, use `make -C golf submission` to produce both the zip and a checked-in report.

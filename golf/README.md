ARC Code Golf Submission

Contents
- submission/: 400 self-contained, minified solver files (one per ARC training task).
- tools/: tiny utilities to validate, smoke-test, package, and (optionally) evaluate.
- submission.zip: packaged archive of the files in submission/.

Quick Start
- Validate: `make -C golf validate`
- Smoke test: `make -C golf smoke`
- Package: `make -C golf package` (writes golf/submission.zip)
- Evaluate (optional): place dataset under `data/arc_agi_1/` and run `make -C golf eval`

Notes
- Files are self-contained: no imports, one `solve_<id>(I)` per file, end with `return O`.
- Evaluation requires ARC AGI data at `data/arc_agi_1/{training,evaluation}`.
- For code golf scoring based on archive size, use the provided `package` target.


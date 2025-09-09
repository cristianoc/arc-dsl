#!/usr/bin/env python3
import re
import sys
from pathlib import Path


def validate_file(path: Path):
    s = path.read_text(encoding='utf-8', errors='ignore')
    issues = []
    if path.suffix != '.py':
        issues.append('not a .py file')
    # Imports are allowed if from the stdlib; enforced separately by import-check.
    defs = re.findall(r'^def\s+solve_([0-9a-f]{8})\(I\):', s, re.M)
    if len(defs) != 1:
        issues.append(f'{len(defs)} solver defs (expected 1)')
    if not re.search(r'\n\s*return\s+O\s*\n', s):
        issues.append('missing return O')
    if re.search(r'\b(dsl|solvers|arc_types|constants|main|tests)\b', s):
        issues.append('references external module')
    if not re.search(r'def\s+solve_[0-9a-f]{8}\(I\):[\s\S]*?\n\s*return\s+O\b', s):
        issues.append('missing or malformed solver body/return')
    return defs[0] if defs else None, issues


def main():
    if len(sys.argv) < 2:
        print('Usage: validate.py <submission_dir>')
        sys.exit(2)
    subdir = Path(sys.argv[1])
    py_files = sorted(subdir.glob('*.py'))
    seen = {}
    failures = []
    for p in py_files:
        tid, issues = validate_file(p)
        if issues:
            failures.append((p.name, issues))
        if tid:
            if tid in seen and seen[tid] != p.name:
                failures.append((p.name, [f'duplicate solver id {tid}, also in {seen[tid]}']))
            seen[tid] = p.name
    print(f'Files: {len(py_files)}  Unique solver IDs: {len(seen)}')
    if failures:
        print(f'Failures: {len(failures)}')
        for name, issues in failures[:50]:
            print('-', name, '->', '; '.join(issues))
        sys.exit(1)
    print('All files validated successfully.')


if __name__ == '__main__':
    main()

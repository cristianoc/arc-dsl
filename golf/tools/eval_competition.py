#!/usr/bin/env python3
import json
import re
import sys
from pathlib import Path


def load_solver(text: str):
    ns = {}
    exec(compile(text, '<solver>', 'exec'), ns)
    for k in ns:
        if re.match(r'^solve_[0-9a-f]{8}$', k):
            return ns[k]
    return None


def main():
    if len(sys.argv) < 3:
        print('Usage: eval_competition.py <submission_dir> <competition_dir>')
        sys.exit(2)
    subdir = Path(sys.argv[1])
    compdir = Path(sys.argv[2])
    assert compdir.exists(), f'missing {compdir}'

    tasks = sorted(p for p in compdir.glob('task*.json'))
    total = len(tasks)
    solved = 0
    errors = 0
    mismatches = 0
    failures = []

    ast = lambda g: tuple(tuple(r) for r in g)

    for i, t in enumerate(tasks, 1):
        base = t.stem  # e.g., task123
        py = subdir / f'{base}.py'
        if not py.exists():
            failures.append((base, 'missing solver file'))
            mismatches += 1
            continue
        code = py.read_text(encoding='utf-8', errors='ignore')
        solver = load_solver(code)
        if solver is None:
            failures.append((base, 'no solver function'))
            mismatches += 1
            continue
        data = json.loads(t.read_text())
        ok = True
        try:
            extra = data.get('arc-gen', [])
            for e in data['train'] + data['test'] + extra:
                I = ast(e['input'])
                O = ast(e['output'])
                P = solver(I)
                if P != O:
                    ok = False
                    break
        except Exception as e:
            ok = False
            errors += 1
            failures.append((base, f'error: {type(e).__name__}: {e}'))
        if ok:
            solved += 1
        else:
            mismatches += 1

        # Periodic progress update (every 20 tasks)
        if i % 20 == 0 or i == total:
            print(f'Progress: {i}/{total} solved={solved} errors={errors} mismatches={mismatches}')

    print(f'Competition eval: total={total} solved={solved} errors={errors} mismatches={mismatches}')
    if failures:
        print('First 20 failures:')
        for rec in failures[:20]:
            print(rec)


if __name__ == '__main__':
    main()

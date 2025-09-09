#!/usr/bin/env python3
import re
import sys
from pathlib import Path


def grids():
    G1 = tuple((0, 0, 0) for _ in range(3))
    G2 = (
        (0, 0, 0, 0, 0),
        (0, 0, 0, 0, 0),
        (0, 0, 2, 0, 0),
        (0, 0, 0, 0, 0),
        (0, 0, 0, 0, 0),
    )
    G3 = (
        (0, 0, 0, 0, 0),
        (0, 2, 2, 0, 0),
        (0, 2, 2, 0, 0),
        (0, 0, 0, 3, 0),
        (0, 0, 0, 3, 0),
    )
    G4 = (
        (0, 0, 0, 0, 0),
        (0, 5, 0, 0, 0),
        (0, 5, 0, 7, 7),
        (0, 5, 0, 0, 0),
        (0, 0, 0, 0, 0),
    )
    G5 = (
        (4, 4, 4, 4, 4, 4),
        (4, 0, 0, 0, 0, 4),
        (4, 0, 0, 2, 0, 4),
        (4, 0, 0, 0, 0, 4),
        (4, 4, 4, 4, 4, 4),
        (0, 0, 0, 0, 0, 0),
    )
    return [G1, G2, G3, G4, G5]


def load_solver(text: str):
    ns = {}
    exec(compile(text, '<solver>', 'exec'), ns)
    for k in ns:
        if re.match(r'^solve_[0-9a-f]{8}$', k):
            return ns[k]
    return None


def main():
    if len(sys.argv) < 2:
        print('Usage: smoke.py <submission_dir>')
        sys.exit(2)
    subdir = Path(sys.argv[1])
    tests = grids()
    oks = 0
    total = 0
    failures = []
    for p in sorted(subdir.glob('*.py')):
        total += 1
        try:
            solver = load_solver(p.read_text(encoding='utf-8', errors='ignore'))
            if solver is None:
                failures.append((p.name, 'no solver function'))
                continue
            ran = False
            for g in tests:
                try:
                    out = solver(g)
                    ok = (
                        isinstance(out, tuple)
                        and out
                        and all(isinstance(r, tuple) for r in out)
                        and all(isinstance(v, int) for r in out for v in r)
                    )
                    if ok:
                        oks += 1
                        ran = True
                        break
                except Exception as e:
                    last_err = f'{type(e).__name__}: {e}'
            if not ran:
                failures.append((p.name, last_err if 'last_err' in locals() else 'failed'))
        except Exception as e:
            failures.append((p.name, f'load error: {type(e).__name__}: {e}'))
    print(f'Tried {total} solvers across {len(tests)} grids. OK: {oks}. Failures: {total-oks}.')
    for fn, s in failures[:40]:
        print(fn, '->', s)


if __name__ == '__main__':
    main()


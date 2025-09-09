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
            return k.split('_', 1)[1], ns[k]
    return None, None


def main():
    if len(sys.argv) < 3:
        print('Usage: evaluate.py <submission_dir> <arc_root_dir>')
        sys.exit(2)
    subdir = Path(sys.argv[1])
    root = Path(sys.argv[2])
    train = root / 'training'
    evald = root / 'evaluation'
    assert train.exists(), f'missing {train}'
    assert evald.exists(), f'missing {evald}'

    solvers = {}
    for p in sorted(subdir.glob('*.py')):
        tid, fn = load_solver(p.read_text(encoding='utf-8', errors='ignore'))
        if tid and fn:
            solvers[tid] = fn
    print(f'Loaded solvers: {len(solvers)}')

    def ast(g):
        return tuple(tuple(r) for r in g)

    def run_split(d: Path, name: str):
        files = sorted(d.glob('*.json'))
        totals = {'total': len(files), 'covered': 0, 'solved': 0, 'errors': 0, 'mismatches': 0}
        failures = []
        for f in files:
            tid = f.stem
            if tid not in solvers:
                continue
            totals['covered'] += 1
            data = json.loads(f.read_text())
            exs = [(ast(e['input']), ast(e['output'])) for e in data['train']] + [
                (ast(e['input']), ast(e['output'])) for e in data['test']
            ]
            fn = solvers[tid]
            ok = True
            try:
                for I, O in exs:
                    if fn(I) != O:
                        ok = False
                        break
            except Exception as e:
                totals['errors'] += 1
                failures.append((tid, 'error', type(e).__name__, str(e)))
            else:
                if ok:
                    totals['solved'] += 1
                else:
                    totals['mismatches'] += 1
                    failures.append((tid, 'mismatch', '', ''))
        print(f"{name}: total={totals['total']} covered={totals['covered']} solved={totals['solved']} errors={totals['errors']} mismatches={totals['mismatches']}")
        return failures

    f1 = run_split(train, 'train')
    f2 = run_split(evald, 'eval')
    if f1 or f2:
        print('First 20 failures:')
        for rec in (f1 + f2)[:20]:
            print(rec)


if __name__ == '__main__':
    main()


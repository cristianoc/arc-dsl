#!/usr/bin/env python3
import ast
import sys
from pathlib import Path


def top_module(name: str) -> str:
    return name.split('.', 1)[0]


def main():
    subdir = Path(sys.argv[1]) if len(sys.argv) > 1 else Path('submission')
    files = sorted(subdir.glob('*.py'))
    if not files:
        print(f'No .py files found in {subdir}')
        sys.exit(1)

    stdlib = set(getattr(sys, 'stdlib_module_names', ()))
    # Fallback if not available (older Python): allow no imports beyond builtins
    if not stdlib:
        stdlib = set(('sys', 'math', 'itertools', 'functools', 'collections', 're', 'json', 'heapq', 'bisect', 'array', 'statistics'))

    bad = []
    for p in files:
        tree = ast.parse(p.read_text(encoding='utf-8', errors='ignore'), filename=str(p))
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    mod = top_module(alias.name)
                    if mod not in stdlib:
                        bad.append((p.name, f'import {alias.name}'))
            elif isinstance(node, ast.ImportFrom):
                if node.level and node.level > 0:
                    bad.append((p.name, f'relative import from {"."*node.level}{node.module or ""}'))
                else:
                    mod = top_module(node.module or '')
                    if mod and mod not in stdlib:
                        bad.append((p.name, f'from {node.module} import ...'))

    if bad:
        print('Non-standard-library imports detected:')
        for fn, desc in bad:
            print('-', fn, '->', desc)
        sys.exit(1)
    else:
        print('All imports (if any) are from the Python Standard Library.')


if __name__ == '__main__':
    main()


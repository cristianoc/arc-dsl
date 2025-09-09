#!/usr/bin/env python3
import sys
import zipfile
from pathlib import Path


def main():
    if len(sys.argv) < 3:
        print('Usage: package.py <submission_dir> <output_zip>')
        sys.exit(2)
    subdir = Path(sys.argv[1])
    out = Path(sys.argv[2])
    files = sorted(p for p in subdir.glob('*.py'))
    if not files:
        print('No .py files found to package')
        sys.exit(1)
    with zipfile.ZipFile(out, 'w', compression=zipfile.ZIP_DEFLATED) as z:
        for p in files:
            z.write(p, arcname=p.name)
    print(f'Wrote {len(files)} files to {out}')


if __name__ == '__main__':
    main()


#!/usr/bin/env python3
import sys
from pathlib import Path


def main():
    subdir = Path(sys.argv[1]) if len(sys.argv) > 1 else Path('submission')
    out_path = Path(sys.argv[2]) if len(sys.argv) > 2 else None
    files = sorted(subdir.glob('task*.py'))
    if not files:
        print(f'No solver files found in {subdir}')
        sys.exit(1)

    rows = []
    total_score = 0
    for p in files:
        size = p.stat().st_size  # bytes
        score = max(1, 2500 - size)
        total_score += score
        rows.append((p.name, size, score))

    # Summary stats
    sizes = [s for _, s, _ in rows]
    lines = []
    lines.append('Per-task length and score:')
    for name, size, score in rows:
        lines.append(f'{name}\t{size} bytes\t{score} points')
    lines.append('---')
    lines.append(f'Files: {len(rows)}  min: {min(sizes)}  max: {max(sizes)}  avg: {sum(sizes)//len(sizes)} bytes')
    lines.append(f'Estimated total score: {total_score}')

    text = '\n'.join(lines) + '\n'
    # Print to stdout
    sys.stdout.write(text)
    # Optionally write to file
    if out_path is not None:
        out_path.write_text(text, encoding='utf-8')


if __name__ == '__main__':
    main()

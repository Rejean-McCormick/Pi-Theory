from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]
problems = []
for p in root.rglob('*'):
    if not p.is_file():
        continue
    try:
        str(p.relative_to(root)).encode('ascii')
    except UnicodeEncodeError:
        problems.append(f'non-ASCII filename: {p.relative_to(root)}')
    if p.suffix.lower() == '.md':
        text = p.read_text(encoding='utf-8')
        try:
            text.encode('ascii')
        except UnicodeEncodeError:
            problems.append(f'non-ASCII Markdown content: {p.relative_to(root)}')
        if '\\\\[' in text or '\\\\]' in text or '\\\\(' in text or '\\\\)' in text:
            problems.append(f'fragile TeX delimiter: {p.relative_to(root)}')

if problems:
    print('\n'.join(problems))
    raise SystemExit(1)
print('OK: ASCII-safe filenames and Markdown content; no fragile TeX delimiters found.')

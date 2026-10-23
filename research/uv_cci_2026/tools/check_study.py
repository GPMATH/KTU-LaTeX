#!/usr/bin/env python3
"""Conservative static integrity checks; does NOT certify bibliographic truth."""
from pathlib import Path
from collections import Counter
import csv
import re
import sys

p = Path(__file__).resolve().parents[1]
bib = (p / 'references.bib').read_text(encoding='utf-8')
keys = re.findall(r'@\w+\s*\{\s*([^,\s]+)\s*,', bib)
counts = Counter(keys)
duplicates = sorted(k for k,v in counts.items() if v > 1)
inputs = [p/'report.tex', *sorted((p/'chapters').glob('*.tex'))]
cited = set()
for filepath in inputs:
    txt = filepath.read_text(encoding='utf-8')
    for raw in re.findall(r'\\cite(?:p|t|alt|alp|author|year)?(?:\[[^]]*\])*\{([^}]+)\}', txt):
        cited.update(s.strip() for s in raw.split(',') if s.strip())
missing = cited - set(keys)
with (p/'sources/source_catalog.csv').open(encoding='utf-8', newline='') as file:
    catalog = list(csv.DictReader(file))
cat_keys = [r['key'] for r in catalog]
problems=[]
if duplicates: problems.append('Duplicate BibTeX keys: '+', '.join(duplicates))
if missing: problems.append('Undefined citations: '+', '.join(sorted(missing)))
if set(cat_keys) != set(keys): problems.append('Source catalog keys do not match BibTeX keys')
if len(cat_keys) != len(set(cat_keys)): problems.append('Duplicate catalog keys')
if len(keys) < 30: problems.append('Unexpectedly small bibliography')
if problems:
    print('\n'.join('ERROR: '+x for x in problems), file=sys.stderr)
    sys.exit(1)
print(f'OK: {len(keys)} bibliography entries, {len(cited)} cited keys, {len(inputs)-1} chapter files')
print('NOTE: Check primary-source bibliographic identity and evidence before submission.')

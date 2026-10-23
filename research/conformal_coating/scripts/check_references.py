#!/usr/bin/env python3
"""Basic, dependency-free BibTeX integrity check for this research workspace.

Not a bibliographic authenticity validator: verify DOIs and claims independently.
"""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
BIB = ROOT / "references.bib"
files = [ROOT / "report.tex", *(ROOT / "chapters").glob("*.tex")]
bib = BIB.read_text(encoding="utf-8")
entry_pattern = re.compile(r"@\w+\s*[{(]\s*([^,\s]+)\s*,", re.I)
keys = entry_pattern.findall(bib)
dupes = sorted({key for key in keys if keys.count(key) > 1})
citations = set()
for tex_file in files:
    tex = tex_file.read_text(encoding="utf-8")
    for match in re.finditer(r"\\cite(?:p|t|alt|alp|author|year)?(?:\[[^\]]*\])*\{([^}]+)\}", tex):
        citations.update(k.strip() for k in match.group(1).split(","))
missing = sorted(citations - set(keys))
errors = []
if not keys:
    errors.append("No BibTeX references found.")
if dupes:
    errors.append(f"Duplicate citation keys: {', '.join(dupes)}")
if missing:
    errors.append(f"Citations missing from bibliography: {', '.join(missing)}")
if errors:
    print("\n".join("ERROR: " + msg for msg in errors), file=sys.stderr)
    sys.exit(1)
print(f"OK: {len(keys)} BibTeX entries, {len(citations)} distinct cited keys.")
print("NOTE: Metadata and cited claims still require independent verification.")

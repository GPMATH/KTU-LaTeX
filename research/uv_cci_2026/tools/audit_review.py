#!/usr/bin/env python3
"""Audit compiled PDF against annotated reviewer copy."""
import csv
import re
from pathlib import Path
import fitz

ROOT=Path(__file__).resolve().parents[3]
original=fitz.open(ROOT/"main - Copy.pdf")
revised=fitz.open(ROOT/"main.pdf")
text="\n".join(p.get_text(sort=True) for p in revised)
def words(t):
    return re.findall(r"[a-z0-9]+",re.sub(r"(?<=\w)-\s+(?=\w)","",t.lower()))
all_words=words(text)
haystack=" "+" ".join(all_words)+" "
records=[]
for n,page in enumerate(original,1):
    for ann in (page.annots() or []):
        comment=(ann.info.get("content") or "").strip()
        if not comment:
            continue
        affected=" ".join(w[4] for w in page.get_text("words",sort=True) if fitz.Rect(w[:4]).intersects(ann.rect))
        remove=bool(re.match(r"^\s*(remove|remov\s*e|rewmove|r3move)\b",comment,re.I) or "fully remove section 9" in comment.lower())
        tokens=words(affected)
        if remove and len(tokens)>=8:
            grams=[" ".join(tokens[i:i+8]) for i in range(len(tokens)-7)]
            overlap=sum((" "+g+" ") in haystack for g in grams)/len(grams)
        else:
            overlap=None
        records.append((n,comment,remove,overlap))
banned=["Vidas Raudonis","Valdas Grigali","complementary modality","Research gaps, recommended experiments and conclusions","Literature search strategy and evidence appraisal","Research working manuscript","Supplementary research instruments and source audit","Companion structured files","Source access and interpretation notes","Search-log outline","Technical acceptance checklist","Auditable bibliography inventory","Initial source inventory"]
required=["Rytis Augustauskas","Literature review","Mechanisms of protection and material variability"]
checks={q:q.lower() in text.lower() for q in banned+required}
catalog=ROOT/"research/uv_cci_2026/sources/source_catalog.csv"
count=sum(1 for _ in csv.DictReader(catalog.open(encoding="utf-8-sig")))
removals=[r for r in records if r[2]]
short=sum(r[3] is None for r in removals)
overlap=[r for r in removals if r[3] is not None and r[3]>=.2]
lines=["# Review audit","",
"Compiled final PDF compared with source PDF annotations. This is an automated text check, not a substitute for visual inspection of short selected phrases.","",
f"- Original pages: {len(original)}; revised pages: {len(revised)}",
f"- Annotation notes inspected: {len(records)}; removal notes: {len(removals)}",
f"- Short/ambiguous removals requiring manual visual inspection: {short}",
f"- Longer removals with potential text overlap requiring review: {len(overlap)}",
f"- Source catalog rows (retained as companion data, not printed): {count}","","## Critical checks","",
"| Text check | Result |","|---|---|"]
lines.extend(f"| Remove {q} | {'FAIL' if checks[q] else 'PASS'} |" for q in banned)
lines.extend(f"| Keep {q} | {'PASS' if checks[q] else 'FAIL'} |" for q in required)
lines.extend(["","## Reviewer annotation audit","","| Original page | Note (shortened) | Automatic verdict |","|---|---|---|"])
for n,comment,remove,overlapval in records:
    shortnote=re.sub(r"\s+"," ",comment)[:60].replace("|","/")
    verdict=("REWRITE / meaning check" if not remove else
        "MANUAL: short highlight" if overlapval is None else
        f"REVIEW: {overlapval:.0%} overlap" if overlapval>=.2 else
        "PASS: no substantial eight-word overlap")
    lines.append(f"| {n} | {shortnote} | {verdict} |")
lines.extend(["","## Caveats","","Short snippets, selection boundaries and paraphrased material cannot be proven absent by the automated phrase test. Review manually. This report does not validate the truth of scientific references, images or experiments."])
out=ROOT/"research/uv_cci_2026/REVIEW_AUDIT.md"
out.write_text("\n".join(lines)+"\n",encoding="utf-8")
print(f"AUDIT: {len(records)} notes; {len(removals)} removals; {short} short; {len(overlap)} longer potential overlaps")
if any(checks[q] for q in banned): raise SystemExit("Forbidden text remains")
if any(not checks[q] for q in required): raise SystemExit("Required text missing")
if count!=58: raise SystemExit("Source catalog count no longer matches original evidence register")
if not any(re.search(r"2\.\s*Literature review\s+2\.1\.\s*Mechanisms of protection", p.get_text(sort=True), re.S) for p in list(revised)[6:]):
    raise SystemExit("Literature review is blank, not section 2, or has no real subsection text")
if len(records)<100: raise SystemExit("Annotation count unexpectedly low")
if re.search(r"\bA\.\s*Supplementary research instruments", text):
    raise SystemExit("Appendix A is still included in the final PDF")

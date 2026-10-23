# UV PCB conformal-coating inspection — research workspace

This branch is derived from `main` after the shared Zotero setup was documented in [ZOTERO.md](../../ZOTERO.md). It is a **research scaffold**, not a completed literature review and not a claim that the Zotero desktop library has been connected.

## Scope

- 70 × 70 mm PCB; an ~80 × 80 mm field of view is a starting design assumption.
- 365 nm UVA excitation **only if the specific coating fluoresces adequately**; the camera should generally measure visible emission, not only reflected UVA.
- Compare classical fluorescence segmentation, learned segmentation, and a registration/reference-aware hybrid.
- Collect ground truth and split by **physical board and lot**, never by repeated images alone.
- Target an inexpensive CPU production computer, benchmarking the **entire** inspection cycle.
- Protect personnel from UV; do not expose proprietary production images or PCB designs through this public repository without written clearance.

## Files

- `report.tex` — independent LaTeX research report (the root KTU template is untouched).
- `chapters/` — introductory scope, evidence review framework, experimental protocol.
- `references.bib` — **starter literature examples**, currently **not** an export from Zotero.
- `sources/evidence_matrix.csv` — one row per primary source, with verification status.
- `sources/search_log.csv` — reproducible database/search log.
- `sources/dataset_register.csv` — sample-level data traceability.
- `scripts/check_references.py` — light bibliography and citation-key integrity checks.

## Zotero integration

See [shared Zotero guide](../../ZOTERO.md). Create a Zotero collection called **UV PCB Conformal Coating Inspection**. Add papers only after verifying metadata via the publisher/Crossref. Export the collection as BibTeX to **`research/conformal_coating/references.bib`**, preserving keys already cited in LaTeX (Better BibTeX for Zotero offers stable-key auto-export). Commit only reference metadata; keep publisher PDFs in Zotero, not the public GitHub repository.

The starter references are general segmentation/anomaly-detection methods, not evidence that these models work for conformal coating. Source-specific performance assertions belong in the evidence matrix after full-text reading.

## Build

From the repository root (important for the inherited `ktu_thesis_style.sty`):

```bash
python3 research/conformal_coating/scripts/check_references.py
latexmk -pdf -interaction=nonstopmode -halt-on-error -jobname=coating-report research/conformal_coating/report.tex
```

If building manually, run `pdflatex` → `bibtex coating-report` → `pdflatex` twice. LaTeX outputs in the repository root when using the above command; they are ignored by the research-specific `.gitignore` entries only when placed under `research/conformal_coating`. Prefer `latexmk -outdir=research/conformal_coating/build -pdf -interaction=nonstopmode -halt-on-error research/conformal_coating/report.tex` if the toolchain handles its relative inputs and bibliography paths.

## Project decisions / acceptance gates

1. Freeze the coating chemistry, imaging modality and minimum actionable defect size before claiming optical adequacy.
2. Publish a traceable source-search protocol and a vetted evidence matrix before writing literature claims.
3. Define defect taxonomy, operator ground truth and leakage-free PCB/lot splits before model training.
4. Freeze test-set thresholds before evaluating candidate algorithms; report uncertainty and confidence intervals.
5. Review employer confidentiality/IP and research ethics before releasing any photos or dataset.
6. Keep journal article claims strictly limited to reproducible, experimentally supported results.

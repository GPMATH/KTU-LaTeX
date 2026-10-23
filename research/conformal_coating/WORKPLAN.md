# Research workflow and milestone tracker

> This repository currently has GitHub Issues disabled. Use this file and the draft pull request as the research task board until Issues/Projects are enabled by the repository owner. Update checkboxes in commits and maintain a source-of-truth evidence matrix.

## M1. References and Zotero

- [ ] Confirm access to actual Zotero desktop library (separate from GitHub).
- [ ] Create a dedicated collection for UV conformal-coating inspection.
- [ ] Export stable-key BibTeX to `research/conformal_coating/references.bib`.
- [ ] Screen 50–80 candidate sources with exact search queries and inclusion criteria.
- [ ] Verify the 30–50 strongest sources, distinguishing full text from abstract only.
- [ ] Enter evidence into `sources/evidence_matrix.csv`, keeping direct coating studies separate from general computer-vision methods.
- [ ] Investigate publicly downloadable labeled UV coating datasets and licenses.

**Gate:** Every literature claim has a traceable primary source and verification status.

## M2. Optical design, safety, and data collection

- [ ] Confirm actual conformal-coating fluorescence under chosen 365 nm illumination.
- [ ] Determine filter and camera spectral response; document lens, FOV and repeatability.
- [ ] Create UV-safe enclosure, suitable shields and interlock.
- [ ] Define defect taxonomy, keep-out/required masks, and independent ground truth.
- [ ] Define unique specimen IDs and board/lot-disjoint train/validation/test splits.
- [ ] Confirm image-release permissions; restrict proprietary data.

**Gate:** repeatable capture protocol and frozen sample-level dataset rules.

## M3. Algorithms and experiments

- [ ] Implement classical CV registration/threshold baseline.
- [ ] Implement U-Net (or similar lightweight) standalone segmentation baseline.
- [ ] Implement reference-aware hybrid pipeline as an experimental candidate.
- [ ] Freeze acceptance thresholds on validation data before running final evaluation.
- [ ] Evaluate small defects, lighting variation, false acceptance/rejection and confidence intervals.
- [ ] Benchmark complete cycle latency on CPU-class production PC.

**Gate:** reproducible comparison and ablation results with negative cases.

## M4. KTU report and scientific publication

- [ ] Replace scaffolding chapters with evidence-based critical writing.
- [ ] Preserve KTU template compatibility; verify supervisor-specific formatting.
- [ ] Compile LaTeX and inspect PDF, references, figures and tables.
- [ ] Draft a journal paper only when an experimentally supported contribution is established.
- [ ] Document data/code availability constraints and limitations.

**Gate:** citations checked, methodology reproducible, no unsupported novelty or production claims.

## Repo automation

- **Enabled by branch:** `.github/workflows/research-reference-check.yml`, which checks duplicate BibTeX citation keys and undefined LaTeX citations.
- **Not yet implemented:** reproducible CI LaTeX/PDF build, quality review of publication metadata and live Zotero synchronization.
- **Not automated by GitHub:** human full-text literature verification, experimental ground truth, company data approvals.

## Local workflow

```bash
git checkout main
git pull --ff-only origin main
git fetch origin
git switch research/uv-conformal-coating-inspection
git pull --ff-only origin research/uv-conformal-coating-inspection
python3 research/conformal_coating/scripts/check_references.py
```

Work from this research branch. Open a pull request into `main` when the work is ready; do not merge unreviewed research into the reusable template.

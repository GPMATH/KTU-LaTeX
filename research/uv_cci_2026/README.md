# UV PCB conformal-coating inspection: KTU literature review and methodology

**Status (2026-10-23):** Evidence-grounded research working manuscript, not a completed systematic full-text review or experimental validation. **No Zotero connection is required.** This self-contained project was created on branch `research/uv-cci-comprehensive-study-2026`, derived directly from `main`. The root KTU template remains intact.

## Deliverable and scope

- `report.tex`: LaTeX entry point including a KTU-compatible style (`ktu_thesis_style.sty` from the repository root).
- `chapters/`: nine research chapters, covering research questions, source methodology, coating/UV physics, prior work and systems, AI and datasets, original architecture, experimental design, statistics/deployment, and conclusions; appendix includes a complete source index.
- `references.bib`: 58 externally verifiable source records from publisher, standards, industrial-vendor and official dataset pages. Refer to CSV source catalog for access status; some conference journal metadata and authors need further full-text bibliographic checking.
- `sources/source_catalog.csv`: source IDs, publication links, direct/transfer classification, abstract/full-text/official source status and caveats.
- `sources/evidence_matrix.csv`: initial critical matrix of findings and evidence gaps. Missing results are explicitly blank, not guessed.
- `sources/search_log.csv`: thematic search log and search dates; this is **not** a completed PRISMA flow diagram.
- `sources/experiment_plan.csv`: planned imaging, segmentation, robustness and edge inference experiments.
- `sources/dataset_register_template.csv`: specimen/lot/capture split fields to prevent leakage.

## What is already known

The literature already includes UV coating bubble detection using CNN and transfer learning (Lee et al., 2021), UV brightness selection (Choi et al., 2024), modified YOLOv8 bubble detection (Wang et al., 2025) and coverage/capillary/dewetting classification (Patel et al., 2026). Reference planning and multi-angle UV illumination are established commercial features. Hence **neither the use of CNNs nor generic CAD/image-reference comparison is novel**. The proposal tests the marginal value of calibrated fluorescence, reference-region semantics, uncertainty-aware review and cost/CPU performance on **70×70 mm PCBs**.

Fluorescence indicates coating presence/coverage under defined optical conditions; without calibration and independent depth metrology it does **not** prove coating thickness, adhesion, cure or hidden-side coverage. Public standard previews do not establish numerical pass/fail rules.

## Compile on Linux/macOS with TeX Live

From the **repository root**:

```bash
python3 research/uv_cci_2026/tools/check_study.py
latexmk -pdf -interaction=nonstopmode -halt-on-error research/uv_cci_2026/report.tex
```

or run `pdflatex`, `bibtex`, `pdflatex`, `pdflatex`. Required TeX packages include `natbib`, `tikz`, `pgfplots`, `longtable`, `mfirstuc`, `tocloft`, `microtype`, `amssymb` and `pdflscape`. Run from the root to resolve `ktu_thesis_style.sty` and citation paths. The paper uses the repository's existing **natbib + unsrtnat** style; verify compliance with KTU supervisor's final citation specification.

Build output (`report.pdf`) is generated, not manually maintained in source control. GitHub Actions creates a PDF artifact.

## Scientific workflow and confidentiality

1. Expand the primary full-text evidence review and correct any incomplete venue/author metadata, retaining URLs/DOIs and reported limitations.
2. Confirm actual conformal-coating UV excitation/emission and document filter/sensor response.
3. Capture approved repeated images under controlled lighting, ground truth and board/lot-disjoint splits; never push employer confidential datasets into this **public** GitHub repository.
4. Benchmark (A) corrected classical CV, (B) learned segmentation, (C) registered reference-aware hybrid against the **same held-out physical PCBs**.
5. Measure false accepts, false rejects, defect-size sensitivity, confidence intervals, performance drift, total inference cycle time, cost and operational limitations.
6. Publish any novel method only if its additional value is experimentally shown.

See `chapters/07_experimental_method.tex`, `08_statistics_deployment.tex` and `sources/experiment_plan.csv` for test gates. See root `ZOTERO.md` if Zotero synchronization is desired **later**; the project currently depends only on Git and BibTeX.

# Zotero → BibTeX → KTU LaTeX

This repository uses **BibTeX + natbib**, configured in `ktu_thesis_style.sty`, with numbered citations and the `unsrtnat` bibliography style. Zotero is a reference manager, **not** a GitHub database connection: export references from Zotero as a `.bib` file, then commit that export. Avoid checking in Zotero's local SQLite database or copyrighted PDFs.

## One-time setup

1. Install [Zotero](https://www.zotero.org/download/) and Zotero Connector, and add your real, verified research papers.
2. In Zotero, create one collection per project and deduplicate records before exporting.
3. Right-click a collection → **Export Collection…** → **BibTeX**; save the export in `research/uv_cci_2026/references.bib` for this study.
4. For ongoing exports, Zotero's export dialog may support a "Keep updated" option in some versions; alternatively use Better BibTeX for Zotero for **stable citation keys** and automatic export (third-party extension). Verify that the extension is compatible with your Zotero version.
5. Commit the exported `.bib` to GitHub. Cite its entries by citation key with `\\citep{key}` or `\\citet{key}`, and configure `\\bibliography{path/to/references}` (omit the `.bib` extension).

## Branch bibliography

The root document `main.tex` already uses:

```tex
\bibliography{research/uv_cci_2026/references}
```

Export updated records to this bibliography, preserving the citation keys used by the research chapters. The existing KTU style and BibTeX configuration remain in use.

The bibliography formatting is currently provided by `\\bibliographystyle{unsrtnat}` in `ktu_thesis_style.sty`. It is numeric and ordered by citation appearance, but confirm that it satisfies your **specific KTU supervisor/journal's** citation requirements before submission. Do not add `biblatex`/Biber without also replacing the template's natbib/BibTeX configuration.

## Compile

Run from the repository root:

```bash
pdflatex -interaction=nonstopmode main.tex
bibtex main
pdflatex -interaction=nonstopmode main.tex
pdflatex -interaction=nonstopmode main.tex
```

Or use `latexmk -pdf main.tex` if available.

## Quality and provenance

- Check each DOI against the publisher and record whether you read the full text or only the abstract.
- Do not equate PCB copper/solder defect datasets with UV conformal-coating datasets.
- Split training and testing by physical PCB, not by individual photos of the same board.
- Never commit unpublished company PCB layouts, restricted production images or licensed PDFs to this public repository without permission.
- Zotero/ChatGPT desktop connectivity is separate from this GitHub-based BibTeX workflow. No live Zotero sync or Zotero account access is implied by these instructions.

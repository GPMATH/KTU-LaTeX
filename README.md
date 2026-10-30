# UV PCB conformal-coating inspection

This branch contains a scientific literature review and proposed experimental methodology for PCB conformal-coating inspection using UV fluorescence, classical computer vision and AI. It uses the existing unofficial Kaunas University of Technology LaTeX template.

[Open the generated document: main.pdf](main.pdf).

## Repository contents

- `main.tex`: primary document entry point, including the KTU cover, manuscript status and abstract, contents, lists of figures and tables, research chapters, appendix and bibliography.
- `variables.tex`: document title, author, supervisors and other cover metadata.
- `TitlePage.tex` and `ktu_thesis_style.sty`: existing KTU title page and document formatting.
- `PageSecond.tex` and `PageThird.tex`: optional reusable KTU front-matter templates.
- `images/ktu-ikona.pdf`: KTU logo used on the cover.
- `research/uv_cci_2026/chapters/`: the study's chapter sources.
- `research/uv_cci_2026/references.bib`: the study bibliography.
- `research/uv_cci_2026/sources/`: source catalog, evidence matrix, search log and research planning files.

See the [study guide](research/uv_cci_2026/README.md) for scope, source-access limitations and experimental plans. This is a research working manuscript; it does not report completed inspection experiments.

## Build main.pdf

Run from the repository root with a LaTeX installation:

```bash
python research/uv_cci_2026/tools/check_study.py
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

Alternatively, run `latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex`.

The output is `main.pdf` in the repository root. Temporary LaTeX files are ignored by Git. The document uses the existing `natbib` and `unsrtnat` bibliography setup.

## Reference management

The study is self-contained and does not require a live Zotero connection. For optional Zotero exports and citation-key management, see [ZOTERO.md](ZOTERO.md). Export this study's references to `research/uv_cci_2026/references.bib`.

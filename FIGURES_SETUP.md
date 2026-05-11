# Guide: Adding Figures to the Literature Review PDF

## Why Photos Are Not Showing

The figures are **not showing** in the PDF because the actual image files are **missing from the `images/` folder**. The LaTeX document has the proper `\includegraphics` commands ready, but they need actual image files to reference.

## How to Add Figures

The document expects the following image files in the `images/` folder:

| Figure | Filename | Source |
|--------|----------|--------|
| Wickramaratne Figure 3 | `wickramaratne_fig3.png` | https://arxiv.org/pdf/2101.05891#page=4 |
| Wickramaratne Figure 4 | `wickramaratne_fig4.png` | https://arxiv.org/pdf/2101.05891#page=4 |
| Castelo Figure 1 | `castelo_fig1.png` | https://ieeevis.b-cdn.net/vis_2024/pdfs/v-full-1833.pdf#page=1 |
| Khan Figure 1 | `khan_fig1.png` | https://arxiv.org/pdf/2407.15901#page=4 |
| Eastmond Figure 1 | `eastmond_fig1.png` | https://cdn.ncbi.nlm.nih.gov/pmc/blobs/0f5e/9301871/a4ea1f7c955e/NPh-009-041411-g001.jpg |
| Eastmond Figure 2 | `eastmond_fig2.png` | https://cdn.ncbi.nlm.nih.gov/pmc/blobs/0f5e/9301871/aaf61b59f585/NPh-009-041411-g002.jpg |
| Ma Figure 1 | `ma_fig1.png` | https://arxiv.org/pdf/2102.03987#page=4 |
| Ma Figure 2 | `ma_fig2.png` | https://arxiv.org/pdf/2102.03987#page=4 |
| Sharmin Figure 1 | `sharmin_fig1.png` | https://arxiv.org/pdf/2507.13952#page=3 |
| Sharmin Figure 4 | `sharmin_fig4.png` | https://arxiv.org/pdf/2507.13952#page=11 |

### Steps to Add Figures:

1. **Download each figure** from the URLs provided above
2. **Save as PNG files** (or JPG/PDF - all formats are supported by LaTeX)
3. **Place in the `images/` folder** with the filenames listed above
4. **Recompile the PDF** by running one of:
   - PowerShell: `pdflatex -interaction=nonstopmode main.tex`
   - Or use VS Code LaTeX workshop extension (Save file → Auto-compile)

### Alternative: Use Different Formats

If you have the figures in different formats, update the filenames in the LaTeX document accordingly:
- PNG: `\includegraphics{images/wickramaratne_fig3.png}`
- JPG: `\includegraphics{images/wickramaratne_fig3.jpg}`
- PDF: `\includegraphics{images/wickramaratne_fig3.pdf}`

## Current Status

✅ All 10 figure references are ready in the LaTeX code  
❌ Image files not yet downloaded/added to `images/` folder  
❌ When compiled, PDF will show warnings about missing files  

Once you add the image files, the PDF will automatically display them on compilation.

## Troubleshooting

### If PDF still shows "File not found" errors:
- Check filenames match exactly (case-sensitive on Linux/Mac)
- Verify files are in the correct `images/` folder
- Ensure file extensions in LaTeX match actual files

### If images appear but are stretched/distorted:
- Try removing `[width=0.8\textwidth]` from the `\includegraphics` command
- Or adjust the width percentage to fit your needs

### If compilation fails:
- Try running: `pdflatex -interaction=nonstopmode main.tex` twice
- Check the `main.log` file for specific error messages

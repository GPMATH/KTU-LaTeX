# Thesis Revision Report for the fNIRS and Machine Learning Methodology

## Overall assessment

The supervisor’s four criticisms are methodologically well founded, and they match the parts of the uploaded literature review that are currently weakest: the document treats image-based GASF/CNN pipelines too positively, defines an “Oxygenation index” incorrectly, mentions participant-wise splitting only briefly, and does not yet add a dedicated subsection on physiological confound control with short-channel regression. Because the uploaded file is a literature review rather than a full methods chapter, the page-by-page edits below target what is visible in the current PDF, and the same corrections should then be mirrored in the thesis methodology chapter itself. fileciteturn0file0

Current fNIRS best-practice guidance is very clear on three points. First, extracerebral physiology is a major confound, and inadequate correction can cause apparent activation that is not genuinely cortical. Second, fNIRS results depend strongly on preprocessing and analysis choices, so methods must be reported transparently and justified carefully. Third, machine-learning performance in fNIRS is highly sensitive to how data are split, normalised, windowed, and tuned. These are not minor details; they determine whether a model is learning brain-related structure or trivial shortcuts. citeturn29search0turn30search0turn18view0turn29search2

The short-channel issue is especially important. Recent reviews describe short-distance channels as the current gold standard for removing extracerebral systemic activity, note that failure to correct these artefacts can mislead interpretation, and show that short-channel-based correction improves spatial specificity and cortical activation estimates. There is also evidence that short-channel regression improves reproducibility at the single-subject level. citeturn9view0turn29search3turn31search0turn33search0

The oxygenation issue is also substantive, not cosmetic. The modified Beer–Lambert law yields *changes* in oxyhaemoglobin and deoxyhaemoglobin relative to baseline; this is not the same thing as absolute tissue oxygen saturation. Recent CW-NIRS literature explicitly separates Hbdiff from TSI/rSO2 and notes that these approaches are not interchangeable. A ratio such as \( \mathrm{HbO_2}/(\mathrm{HbO_2}+\mathrm{Hb}) \) belongs to saturation metrics; a difference such as \( \Delta \mathrm{HbO} - \Delta \mathrm{HbR} \) is a haemoglobin-difference quantity, not an oxygenation index. citeturn19view0turn21view0turn10search8

The leakage criticism is equally serious. BenchNIRS was created precisely because fNIRS machine-learning papers often lack robust standards and can overclaim generalisation. Its checklist explicitly requires nested cross-validation, test-set isolation, normalisation fitted only on training data, and no overlap between training, validation, and test sets, especially when sliding windows are used. A recent translational EEG review demonstrates the same identity-confounding principle very clearly: segment-based holdout can make models appear excellent while failing on unseen subjects, and a recent 2025 fNIRS driving paper even acknowledges that random split on physiological windows may lead to leakage and inflated performance. citeturn16view0turn6view9turn23view0turn29search2

If you cannot recollect new data before the exam, the safest and most defensible strategy is *not* to make strong cortical-specific or oxygen-saturation claims. Instead, narrow the thesis claims to relative frontal haemodynamic patterns recorded by CW-fNIRS under the stated preprocessing limitations, explicitly acknowledge the absence of short channels if applicable, correct the haemoglobin metric terminology, and rebuild the evaluation pipeline so that leakage cannot inflate the reported accuracy. That would not make the dataset perfect, but it would make the thesis scientifically honest and much easier to defend. citeturn9view0turn8view2turn16view0turn18view0

## What to remove from the current document

The page references below refer to the current uploaded PDF. fileciteturn0file0

**Current page 10: remove Equation (24) and the label “Oxygenation index.”** The expression “\( \mathrm{OI} = \mathrm{HbO_2} - \mathrm{Hb} \)” should be removed entirely. It is not a valid tissue oxygen saturation formula. If you keep that expression, rename it as **haemoglobin difference** or **Hbdiff**, but the better revision is to replace the entire passage with properly defined fNIRS quantities, as described in the next section. This correction is necessary because recent CW-NIRS work distinguishes Hbdiff from TSI and shows that these signal types are not interchangeable, while saturation-type metrics use ratio-based rather than subtraction-based definitions. fileciteturn0file0 citeturn21view0turn10search8turn19view0

**Current page 10: remove Equations (25)–(28) and the note that culminates in “Final resized image input = \(3 \times 224 \times 224\)” if this is being used as support for your own thesis methodology.** In a literature review, you may still mention that *another study* used an image-resizing pipeline, but these equations should not remain in a form that looks like an endorsed methodological template for your thesis. Recent fNIRS models increasingly preserve the signal as a channel-by-time tensor or direct time-series window, rather than forcing it into a generic image-recognition grid. Keeping the 224 × 224 formulation without criticism invites exactly the objection your supervisor raised. fileciteturn0file0 citeturn15view1turn15view0turn26search0

**Current pages 12–13: remove Section 2.6.1 on fMRI-based autism classification and Section 2.6.3 on MRI hippocampal segmentation.** These sections are too far from the actual methodological problem of fNIRS signal validity, and one of the references is also outside your requested five-year window. They dilute the review and occupy space that should instead be used for extracerebral confounds, short-channel regression, wearable haemodynamic signal validity, and leakage-safe evaluation. If you want an adjacent-domain paragraph at all, keep only a very short contextual sentence, not full subsections. fileciteturn0file0 citeturn29search0turn18view0

**Current page 12: strongly consider removing or compressing Section 2.6.2 on ecological and multimodal assessment.** If your thesis is centrally about fNIRS plus machine learning for neurocognitive or mental-health screening, the most valuable “context” is not augmented-reality visual analytics; it is methodological reliability, physiological specificity, and reproducibility. One sentence on ecological validity is enough if you want to retain that idea. fileciteturn0file0 citeturn30search0turn18view0

**Current page 16: remove current references [6] and [7], and probably remove [8] unless you preserve a single short contextual sentence on multimodal ecological assessment.** Reference [6] is from 2020 and is outside your allowed window. Reference [7] is recent enough but methodologically irrelevant to fNIRS signal processing and machine learning on haemodynamic data. Reference [8] is peripheral. Removing them will make room for references that directly answer the supervisor’s criticisms. fileciteturn0file0 citeturn29search0turn29search2

## What to fix in the current document

**Current pages 5–6: revise the tone of Section 2.1 on GASF.** Keep the Wickramaratne and Mahmud paper only as a *historical example* of image-based fNIRS representation, not as a positive justification for your own pipeline. Replace the sentence that presently “helps justify the use of image representations or CNNs as one possible modelling direction” with a sentence stating that image conversion is one exploratory representation strategy reported in the literature, but that any thesis use must preserve fixed window duration and temporal sampling, and must not rely on arbitrary resizing to standard image grids. That repositioning is consistent with modern fNIRS deep-learning work, where direct sequence models and spatiotemporal tensor models are increasingly preferred because they preserve native time structure. fileciteturn0file0 citeturn15view1turn15view0turn26search0

A defensible replacement sentence for that section is this:

> “GASF-based image representations should be treated in this thesis as a literature example rather than a default preprocessing choice. Because fNIRS is natively a multichannel time series, any representation-learning approach adopted here should preserve fixed temporal windows and sampling structure; generic image resizing can alter the physiological time relationships encoded in the data.”

That sentence is partly an inference from how GASF encodes pairwise time-point relations, but it is well aligned with recent fNIRS work that feeds channel-by-time data directly into CNN-LSTM, TCN, or similar spatiotemporal models instead of first forcing the signal into generic image dimensions. citeturn15view1turn15view0turn2search10

**Current page 10: replace the wrong oxygenation block with a correct haemodynamic definitions block.** A strong replacement is:

\[
\Delta A(\lambda)= \mathrm{DPF}\cdot r \cdot \big[\varepsilon_{\mathrm{HbO}}(\lambda)\,\Delta c_{\mathrm{HbO}}+\varepsilon_{\mathrm{HbR}}(\lambda)\,\Delta c_{\mathrm{HbR}}\big]
\]

\[
\mathrm{HbDiff} = \Delta \mathrm{HbO} - \Delta \mathrm{HbR}
\]

\[
\mathrm{HbT} = \Delta \mathrm{HbO} + \Delta \mathrm{HbR}
\]

\[
\mathrm{rSO}_2 \text{ or TSI} = \frac{\mathrm{HbO_2}}{\mathrm{HbO_2}+\mathrm{Hb}} \times 100
\quad \text{only if the instrument/method explicitly estimates saturation}
\]

Then add a short explanatory note saying that this thesis uses **relative concentration changes** \(\Delta \mathrm{HbO}\) and \(\Delta \mathrm{HbR}\) derived from optical density through the modified Beer–Lambert law, and therefore any derived summary metric should be named Hbdiff or HbT unless the hardware and reconstruction method truly provide a saturation estimate. That wording is physiologically correct and directly addresses the supervisor’s criticism. fileciteturn0file0 citeturn19view0turn21view0turn10search8

**Current page 14: expand Section 3.1 so that participant-wise validation becomes a full leakage-control protocol rather than a single cautionary sentence.** Your current wording already says participant-wise splitting is strongly recommended, which is good, but that is no longer enough. You should explicitly state that subject identity must remain confined to one partition only; that hyperparameters must be tuned inside an inner validation loop, not on the test set; that normalisation must be fitted on training data only; and that overlapping sliding windows must never cross partition boundaries. BenchNIRS lists each of these items explicitly, and the broader translational literature shows that segment-based holdout can inflate performance dramatically. fileciteturn0file0 citeturn16view0turn6view9turn23view0

A concise replacement paragraph for current page 14 would be:

> “To prevent optimistic bias, all data partitioning in this thesis is performed at the participant level before any model fitting. Hyperparameter tuning is performed only within inner validation folds, while the outer test fold is reserved exclusively for final evaluation. Any scaling, normalisation, feature selection, or dimensionality reduction is fitted on training data only and then applied to validation and test data. When temporal windowing is used, windows from the same participant are confined to a single partition, and overlapping windows are not permitted to leak across train, validation, and test sets.”

That wording is exactly the kind of detail examiners expect, because it demonstrates that you understand why high scores in physiological time-series classification can be misleading if the split logic is wrong. citeturn16view0turn6view9turn29search2

**Current page 14: strengthen the baseline-model paragraph.** Keep your existing point that simpler models should remain baselines, but make it explicit that the comparison must include at least one linear baseline and one conventional nonlinear baseline. A good minimum set is logistic regression or LDA, linear SVM, RBF-SVM, and random forest. Recent fNIRS studies and the BenchNIRS framework both support baseline comparison as necessary to show whether a deep model truly adds value beyond simpler decision boundaries. fileciteturn0file0 citeturn15view0turn16view0turn2search10

## What to add to strengthen the methodology

**Insert a new subsection after current Section 2.3 on page 8, before the current walking-task section: “Physiological confounds and short-channel regression.”** This is the most important addition in the whole revision. The subsection should explain that extracerebral systemic artefacts arise from scalp blood flow, heart rate, breathing, and other autonomic influences; that these confounds can mimic or mask task-evoked activation; and that short-distance channels are the preferred correction method because they primarily sample superficial tissue. A compact mathematical block is enough:

\[
y_{\text{clean}} = y_{\text{long}} - \alpha y_{\text{short}},
\qquad
\alpha = \frac{\langle y_{\text{short}}, y_{\text{long}} \rangle}{\langle y_{\text{short}}, y_{\text{short}} \rangle}
\]

and a GLM version:

\[
Y = X_{\text{task}}\beta_{\text{task}} + X_{\text{SDC}}\beta_{\text{SDC}} + X_{\text{phys}}\beta_{\text{phys}} + \varepsilon
\]

followed by the explanation that cleaned signals are obtained by removing nuisance-regressor contributions or by using the residual series. Recent fNIRS reviews explicitly describe SSR this way, note that short-distance channels are the gold standard, and recommend GLM-based correction with all available short channels for offline analysis. citeturn9view0turn8view3turn30search0turn31search0

If your dataset was recorded **without** short channels, add a short limitations paragraph immediately after that subsection. State that the absence of short-distance measurements reduces the physiological specificity of the recorded signal and that the analysis therefore cannot fully separate cortical activation from extracerebral systemic activity. Then state the fallback plan: if peripheral physiological channels were recorded, include them as nuisance regressors; if not, use CAR/PCA only as weaker alternatives and describe them explicitly as non-ideal substitutes. That framing is much stronger than pretending the limitation does not exist. citeturn9view0turn13search1turn8view2

**Insert a new subsection near current page 14, either as part of Section 3.1 or as a new subsection directly after it: “Leakage-safe evaluation pipeline.”** This should describe the full train/validation/test logic in prose. If you want to add one original figure, make it a simple three-box pipeline: *subjects split first* → *preprocessing fitted on training only* → *nested validation for tuning* → *final locked test*. BenchNIRS explicitly recommends unseen-subject or unseen-session splits, nested cross-validation, no test-set use during tuning, and no overlap across partitions when using sliding windows. The FRESH reproducibility study further shows that fNIRS outcomes vary materially across pipelines, which makes this level of methodological specification essential rather than optional. citeturn16view0turn29search2turn18view0

**Insert a new subsection either after current Section 2.1 or inside the methods chapter: “Signal representation while preserving temporal structure.”** Here you should explain that the native representation of your data is a multichannel haemodynamic time series, for example \(X \in \mathbb{R}^{C \times T \times K}\), where \(C\) is the number of channels, \(T\) is the number of time samples per window, and \(K\) is the number of chromophores or signal types used. Then state that the thesis will either model this tensor directly or use transformations that preserve its temporal meaning. This is supported by recent fNIRS papers using direct channel-by-time inputs, CNN-LSTM combinations on structured windows, and spatiotemporal convolution/TCN architectures. citeturn15view1turn15view0turn2search10

A simple display equation you can add is:

\[
X \in \mathbb{R}^{C \times T \times K}
\]

with a note such as:

> “In this thesis, all windows are defined in physical time before model training, and the signal is modelled in a representation that preserves the original temporal sampling. This avoids introducing interpolation artefacts from arbitrary resizing to generic image dimensions.”

That final sentence is partly an inference, so say it as your methodological choice rather than as a universal law. It is nevertheless well justified by current fNIRS modelling practice. citeturn15view1turn15view0

**Add original methodological figures rather than importing many paper figures.** The three figures most worth drawing yourself are these:

- a short- versus long-separation geometry schematic;
- a leakage-safe nested subject-wise cross-validation diagram;
- a sequence-preserving input diagram showing channel × time × chromophore data flowing into baseline ML and into a temporal deep model.

Those three figures would do more to answer your supervisor than the current set of borrowed architecture figures, because they defend *your* methodological choices rather than only summarising prior papers. The need for transparent, well-specified methodological reporting is entirely consistent with fNIRS best-practice recommendations. citeturn29search0turn18view0

## Reference audit and updated source set

The current reference list should be revised by *function*, not just by date. The rule should be: keep references that directly support fNIRS preprocessing, haemodynamic interpretation, representation choice, benchmarking, and validation; downgrade or remove references that only provide adjacent-domain filler. The bibliography page in the uploaded file is on the current final page. fileciteturn0file0

**Current reference [1].** Keep only if you want a historical example of GASF in fNIRS, but replace the arXiv entry with the formal conference citation, and do not let it anchor your own methodology. The conference version is acceptable within your five-year window, but it should support a brief literature example, not your central design rationale. citeturn28search14turn28search1

**Current reference [2].** Keep, but replace the arXiv citation with the published 2025 *Computers* journal article. Also note that this very paper acknowledges that prior preprocessing pipelines are often insufficiently documented, which is exactly why it should not be your only justification source for the deep model. citeturn6view4turn23view0

**Current reference [3].** Keep, but replace the arXiv version with the published 2022 *Neurophotonics* review. This is a strong review for framing the deep-learning landscape in fNIRS, but it must be paired with newer sources on confounds and benchmarking. citeturn26search0turn26search1

**Current reference [4].** Keep. It is peer-reviewed, recent, and relevant as an application example. However, do not use it to justify 224 × 224 image resizing in your own methodology. Use it only as a reviewed example of an image-based walking-task pipeline and discuss its limitations explicitly. fileciteturn0file0

**Current reference [5].** Keep only if cognitive-effort modelling is truly central to your thesis. If you retain it, replace the current citation with the 2025 ACM conference version rather than citing it as a 2026 Delaware Journal plus arXiv combination. Also describe it as exploratory and small-sample, not as settled methodological evidence. citeturn27search0turn27search5

**Current references [6] and [7].** Remove. They are either outside your date constraint or methodologically irrelevant to the actual thesis problem. **Current reference [8]** should be removed unless you keep one short contextual sentence on ecological multimodal assessment. fileciteturn0file0

The following recent references are the ones I would add first, because each one directly fixes one of the supervisor’s criticisms:

- **Yücel et al., 2021, *Best practices for fNIRS publications*, Neurophotonics.** Use this for transparent reporting, preprocessing disclosure, and correct description of mBLL-based concentration changes. citeturn29search0turn29search12  
- **Scholkmann et al., 2022, *Systemic physiology augmented functional near-infrared spectroscopy*, Neurophotonics.** Use this for the argument that body physiology must be measured or modelled, not ignored. citeturn29search1turn13search1  
- **Wyser et al., 2022, *Characterizing reproducibility of cerebral hemodynamic responses when applying short-channel regression*, Neurophotonics.** Use this to show that SCR improves reproducibility. citeturn33search0turn33search2  
- **Klein et al., 2023, *Performance comparison of systemic activity correction in functional near-infrared spectroscopy for methods with and without short distance channels*, Neurophotonics.** Use this to support the claim that systemic correction improves signal quality and spatial specificity. citeturn3search5turn29search3  
- **Amendola et al., 2023, *Robustness of tissue oxygenation estimates by continuous wave space-resolved near infrared spectroscopy*, Journal of Biomedical Optics.** Use this only when discussing true saturation-type metrics such as tissue oxygen saturation, not Hbdiff. citeturn34search0turn34search2  
- **Benerradi et al., 2023, *Benchmarking framework for machine learning classification from fNIRS data*, Frontiers in Neuroergonomics.** Use this for nested cross-validation, baseline models, and leakage prevention. citeturn29search2turn16view0  
- **Qin et al., 2024, *Classification Algorithm for fNIRS-based Brain Signals Using Convolutional Neural Network with Spatiotemporal Feature Extraction Mechanism*, Neuroscience.** Use this as a recent example of modelling channel-by-time structure directly. citeturn15view1  
- **Klein, 2024, *Optimizing spatial specificity and signal quality in fNIRS*, Frontiers in Neuroergonomics.** Use this for short-distance geometry, SSR equations, nuisance-regression logic, and the statement that insufficient preprocessing can make a system run on noise. citeturn30search0turn9view0  
- **Brookshire, 2024, *Data leakage in deep learning studies of translational EEG*, Frontiers in Neuroscience.** Use this for the general identity-confounding principle with segmented physiological signals. citeturn6view9  
- **An et al., 2025, *Functional near-infrared spectroscopy short-channel regression improves cortical activation estimates of working memory load*, Neurophotonics.** Use this to answer the supervisor’s short-regression criticism directly. citeturn31search0turn31search3  
- **Yücel et al., 2025, *fNIRS reproducibility varies with data quality, analysis pipelines, and researcher experience*, Communications Biology.** Use this to justify why your revised methodology must be more explicit and standardised. citeturn18view0turn18view1  
- **Paternoster and Seiberl, 2022, *Comparison of Different Approaches Estimating Skeletal Muscle Oxygen Consumption Using CW-NIRS*, Applied Sciences.** Use this narrowly to support the distinction between TSI and Hbdiff as different signal constructs. citeturn21view0  

## Paste-ready replacement text

The most useful exam-oriented revision is to add a short, precise methodological block that addresses physiological validity, temporal integrity, and leakage control all at once. The paragraph below is written in a thesis style and can be inserted either into the methodology chapter or, in shortened form, into the literature review after the current deep-learning section.

> **Suggested paragraph on physiological validity:**  
> “Because fNIRS measurements are susceptible to extracerebral systemic activity, the present study treats physiological confound control as a core preprocessing step rather than as an optional refinement. Optical density signals are first converted to relative concentration changes in oxyhaemoglobin and deoxyhaemoglobin using the modified Beer–Lambert law. When short-distance channels are available, they are incorporated as nuisance regressors to reduce superficial systemic contamination; when they are unavailable, this limitation is stated explicitly and alternative regressors are treated as weaker substitutes. Consequently, the present thesis interprets \(\Delta\mathrm{HbO}\), \(\Delta\mathrm{HbR}\), Hbdiff, and HbT as relative haemodynamic quantities and avoids describing Hbdiff as tissue oxygen saturation or oxygenation index.” citeturn19view0turn9view0turn21view0turn31search0

> **Suggested paragraph on signal representation:**  
> “The input to the classifier is defined as a multichannel haemodynamic time series rather than a generic image. Fixed-duration windows are created in physical time, preserving sampling structure and channel organisation. This design is preferred because current fNIRS deep-learning studies increasingly use sequence-preserving or spatiotemporal tensor representations, allowing temporal and spatial structure to be learned directly without arbitrary resizing to image-recognition grids.” citeturn15view1turn15view0turn2search10

> **Suggested paragraph on leakage-safe evaluation:**  
> “To avoid inflated performance estimates, all model evaluation is performed with subject-wise partitioning. Training, validation, and test sets are separated at the participant level before any normalisation, feature selection, or hyperparameter tuning. Hyperparameters are selected only within inner validation folds, while the outer test fold is used once for final evaluation. If windowing is applied, windows from a given participant are confined to a single partition, and overlapping windows are not permitted to cross partition boundaries.” citeturn16view0turn6view9turn23view0

If you need one additional short limitations statement for the exam, add this after the methods section:

> **Suggested limitations sentence:**  
> “In the absence of direct short-distance measurements, the present study cannot claim fully cortical-specific activation and should therefore be interpreted as an analysis of task-related frontal haemodynamic patterns with possible extracerebral contamination.” citeturn8view2turn9view0

If you implement the revisions above, the thesis will move from a generic “deep learning on fNIRS” narrative to a much more defensible methodology: one that clearly distinguishes relative haemodynamic measures from absolute oxygenation metrics, acknowledges extracerebral contamination, preserves temporal structure, and prevents train–test leakage. Those are exactly the places where the current text is most vulnerable and exactly the places where recent fNIRS literature is strongest. citeturn29search0turn29search2turn30search0turn18view0



I also copied this from chatgpt Sources

Activity · 1h 21m

Citations · 20

•

1
main.pdf

main.pdf
pubmed.ncbi.nlm.nih.gov
pubmed.ncbi.nlm.nih.gov

2
https://pubmed.ncbi.nlm.nih.gov/33442557/
https://pubmed.ncbi.nlm.nih.gov/33442557/

12
https://pubmed.ncbi.nlm.nih.gov/35832785/
https://pubmed.ncbi.nlm.nih.gov/35832785/

13
https://pubmed.ncbi.nlm.nih.gov/35265732/
https://pubmed.ncbi.nlm.nih.gov/35265732/

15
https://pubmed.ncbi.nlm.nih.gov/37465166/
https://pubmed.ncbi.nlm.nih.gov/37465166/

18
https://pubmed.ncbi.nlm.nih.gov/40852333/
https://pubmed.ncbi.nlm.nih.gov/40852333/
frontiersin.org
frontiersin.org

3
https://www.frontiersin.org/journals/neuroergonomics/articles/10.3389/fnrgo.2024.1286586/full
https://www.frontiersin.org/journals/neuroergonomics/articles/10.3389/fnrgo.2024.1286586/full

8
https://www.frontiersin.org/journals/neuroinformatics/articles/10.3389/fninf.2024.1320189/full
https://www.frontiersin.org/journals/neuroinformatics/articles/10.3389/fninf.2024.1320189/full

16
https://www.frontiersin.org/journals/neuroergonomics/articles/10.3389/fnrgo.2023.994969/full
https://www.frontiersin.org/journals/neuroergonomics/articles/10.3389/fnrgo.2023.994969/full

17
https://www.frontiersin.org/journals/neuroscience/articles/10.3389/fnins.2024.1373515/full
https://www.frontiersin.org/journals/neuroscience/articles/10.3389/fnins.2024.1373515/full
openfnirs.org
openfnirs.org

4
https://openfnirs.org/2024/01/01/modified-beer-lambert-law/
https://openfnirs.org/2024/01/01/modified-beer-lambert-law/
hanbnrd.gitlab.io
hanbnrd.gitlab.io

5
https://hanbnrd.gitlab.io/benchnirs/
https://hanbnrd.gitlab.io/benchnirs/
mdpi.com
mdpi.com

6
https://www.mdpi.com/2076-3417/12/5/2272
https://www.mdpi.com/2076-3417/12/5/2272

9
https://www.mdpi.com/2073-431X/14/2/73
https://www.mdpi.com/2073-431X/14/2/73

20
https://www.mdpi.com/2077-0383/12/8/2776
https://www.mdpi.com/2077-0383/12/8/2776
sciencedirect.com
sciencedirect.com

7
https://www.sciencedirect.com/science/article/abs/pii/S0306452224000617
https://www.sciencedirect.com/science/article/abs/pii/S0306452224000617
spiedigitallibrary.org
spiedigitallibrary.org

10
https://www.spiedigitallibrary.org/journals/neurophotonics/volume-9/issue-4/041411/Deep-learning-in-fNIRS-a-review/10.1117/1.NPh.9.4.041411.full
https://www.spiedigitallibrary.org/journals/neurophotonics/volume-9/issue-4/041411/Deep-learning-in-fNIRS-a-review/10.1117/1.NPh.9.4.041411.full

14
https://www.spiedigitallibrary.org/journals/neurophotonics/volume-10/issue-1/013503/Performance-comparison-of-systemic-activity-correction-in-functional-near-infrared/10.1117/1.NPh.10.1.013503.short
https://www.spiedigitallibrary.org/journals/neurophotonics/volume-10/issue-1/013503/Performance-comparison-of-systemic-activity-correction-in-functional-near-infrared/10.1117/1.NPh.10.1.013503.short
dl.acm.org
dl.acm.org

11
https://dl.acm.org/doi/full/10.1145/3747327.3764901
https://dl.acm.org/doi/full/10.1145/3747327.3764901
nature.com
nature.com

19
https://www.nature.com/articles/s42003-025-08412-1
https://www.nature.com/articles/s42003-025-08412-1
Sources scanned · 360

pmc.ncbi.nlm.nih.gov
pmc.ncbi.nlm.nih.gov
Optimizing short-channel regression in fNIRS - PMC


by Y Lemaire · 2026 — A central issue in fNIRS data analysis concerns the optimal use of short separation channels (SCs) for removing systemic physiological noise; although it is ...Read more

Best practices for fNIRS publications - PMC


by MA Yücel · 2021 · Cited by 684 — The purpose of this paper is to offer researchers guidelines on how to report fNIRS studies in a comprehensive, transparent, and accessible way.Read more

Data Leakage in Deep Learning for Alzheimer's Disease ...


by VM Young · 2025 · Cited by 10 — Low risk of data leakage: Studies were examined for the use of appropriate subject-wise splitting across training, validation, and test sets.Read more

Robustness of tissue oxygenation estimates by continuous ...


by C Amendola · 2023 · Cited by 17 — We studied the accuracy and robustness of SRS NIRS. We investigated the errors in retrieving hemodynamic parameters, in particular tissue oxygen saturation.Read more

Benchmarking framework for machine learning classification ...


by J Benerradi · 2023 · Cited by 20 — We present an open-source benchmarking framework, BenchNIRS, to establish a best practice machine learning methodology to evaluate models applied to fNIRS data.Read more

Personalized Stress Detection Using Biosignals from Wearables


by M Bolpagni · 2024 · Cited by 68 — This scoping review aims to provide an overview of the models used for personalized stress detection and the available datasets for training. Simultaneously, it ...Read more

Block-Wise Domain Adaptation for Workload Prediction ... - PMC


by J Wang · 2025 — In this work, we study the problem of classification of cognitive workload levels from fNIRS data. Methods have been proposed to employ deep ...Read more

Transformer-based deep learning model for predicting fNIRS ...


by S Guglielmini · 2025 — Transformer-based models accurately reconstruct extracerebral hemodynamic signals from long-separation fNIRS data, providing a virtual ...Read more

The application of fNIRS in studies on occupational workload


by R Gemmerich · 2025 · Cited by 6 — In brief, fNIRS is an imaging technique indirectly measuring brain activity by using near-infrared light (650–1,000 nm) absorbed by hemoglobin in the brain to ...Read more

Empirical comparison of deep learning models for fNIRS pain ...


by RF Rojas · 2024 · Cited by 35 — In this paper, an empirical comparative study of deep learning approaches for the objective assessment of pain is presented. The motivation to utilise deep ...Read more

Functional near-infrared spectroscopy short-channel ... - PMC


by J An · 2025 · Cited by 1 — Functional near-infrared spectroscopy short-channel regression improves cortical activation estimates of working memory load. Jiahui An ...Read more

Modified Beer-Lambert law for blood flow - PMC


by WB Baker · 2014 · Cited by 387 — We develop and validate a Modified Beer-Lambert law for blood flow based on diffuse correlation spectroscopy (DCS) measurements.Read more

Effects of Processing Methods on fNIRS Signals Assessed ...


by M Izzetoglu · 2020 · Cited by 75 — Most fNIRS system applications use modified Beer-Lambert law (MBLL) to convert the intensity measurements to hemodynamic changes in Hb and HbO2 which ...Read more

Near-Infrared Spectroscopy (NIRS) in Traumatic Brain Injury ...


by M Roldán · 2021 · Cited by 109 — This review investigates the main applications of NIRS in TBI monitoring and presents a thorough revision of those applications on oxygenation and ...

Investigation of Confounding Factors in Measuring Tissue ...


by Z Kovacsova · 2018 · Cited by 31 — The aim of the study is to use broadband NIRS SRS data to investigate the effects on the calculation of TOI of different parameters.Read more

Comparative assessment of healthy tissue oxygenation using ...


by M El Masry · 2025 · Cited by 7 — Comparative assessment of healthy tissue oxygenation using near-infrared ... Near-Infrared spectroscopy imaging for assessing skin and wound ...Read more

A NIRS-Based Technique for Monitoring Brain Tissue ... - PMC


by J Gutierrez-Martinez · 2024 · Cited by 7 — This study explores the potential of fNIRS signals to assess brain tissue in chronic stroke patients along with rehabilitation therapy.Read more

Evaluation of hyperspectral NIRS for quantitative ... - PMC - NIH


by M Kewin · 2019 · Cited by 36 — Hyperspectral NIRS (HS NIRS) is an inexpensive, quantitative modality that can measure tissue optical properties and oxygen saturation (StO2) by differential ...Read more

Haemoglobin oxygen saturation as a biomarker - PMC - NIH


by DA Boas · 2011 · Cited by 160 — In this paper, we first review when haemoglobin oxygen saturation does work as a robust indicator, and then detail when and why it fails for assessing brain ...Read more

The Effect on Cerebral Tissue Oxygenation Index of Changes ...


by MM Tisdall · 2009 · Cited by 87 — A variety of near-infrared spectroscopy devices can be used to make noninvasive measurements of cerebral tissue oxygen saturation (ScO2).

Systemic physiology augmented functional near-infrared ...


by F Scholkmann · 2022 · Cited by 100 — SPA-fNIRS enables to study the embodied brain by linking the brain with the physiological state of the entire body, allowing novel insights into their complex ...Read more

Deep learning in fNIRS: a review - PMC


by C Eastmond · 2022 · Cited by 158 — Deep learning (DL) methodologies have demonstrated fast and accurate performances in data processing and classification tasks across many biomedical fields.Read more

The Use of Functional Near-Infrared Spectroscopy to ... - PMC


by CE Barrett · 2019 · Cited by 10 — Graphs of mean changes in PFC hemoglobin concentration relative to a 10-s baseline period demonstrate relative differences in HBO and HBR as a function of group ...Read more

Systematic review of fNIRS studies reveals inconsistent ... - PMC


by KT Kinder · 2022 · Cited by 71 — Our review revealed five general practices for reporting fNIRS chromophores: (1) HbO only, (2) HbR only, (3) HbO and HbR, (4) correlation-based signal ...Read more

Comparing fNIRS signal qualities between approaches ... - PMC


by X Zhou · 2020 · Cited by 99 — Functional near-infrared spectroscopy (fNIRS) is a non-invasive technique used to measure changes in oxygenated (HbO) and deoxygenated (HbR) hemoglobin, related ...Read more

Machine Learning Techniques to Predict Mental Health ... - PMC


by U Madububambachu · 2024 · Cited by 107 — This study aims to investigate the potential of machine learning in predicting mental health conditions among college students.Read more

Artificial Intelligence in Psychiatry: A Review of Biological and ...


by İ Baydili · 2025 · Cited by 54 — This review explores recent advancements in AI applications within psychiatry, focusing on EEG and ECG data analysis, speech analysis, natural language ...Read more

Identifying neuroimaging biomarkers for anxiety in emerging ...


by S Huang · 2026 — Compared to fMRI, fNIRS is more suitable for measuring the brain's intrinsic spontaneous activation, owing to its high motion tolerance (up to 30 mm ...Read more

DL-QC-fNIRS: a deep learning tool for automated quality ...


by S Guglielmini · 2025 — Cross-validation performance of four CNN architectures on dataset 2 (10-fold subject-wise validation). Metrics are reported as mean ± standard deviation.

The impact of cross-validation choices on pBCI classification ...


by F Schroeder · 2025 · Cited by 4 — Varoquaux et al. (2017) showed that leave-one-sample-out cross-validation schemes can inflate accuracy metrics due to temporal dependencies, ...Read more

A Deep-Learning Empowered, Real-Time Processing Platform ...


by Y Xia · 2025 · Cited by 5 — This study proposes a real-time processing system for fNIRS/DOT that integrates baseline calibration, denoising autoencoder (DAE) based MA correction model ...Read more

Improved performance of fNIRS-BCI by stacking of deep ...


by J Akhter · 2025 · Cited by 3 — In this study hand gripping data is acquired using fNIRS neuroimaging system, preprocessing is performed using nirsLAB and features extraction ...

The present and future use of functional near‐infrared ... - PMC


by P Pinti · 2018 · Cited by 1619 — In this review we aim to provide a comprehensive and state‐of‐the‐art review of fNIRS basics, technical developments, and applications.Read more

Conditional-GAN Based Data Augmentation for Deep ... - PMC


by SD Wickramaratne · 2021 · Cited by 63 — A Deep Learning Based Ternary Task Classification System Using Gramian Angular Summation Field in Fnirs Neuroimaging Data. arXiv preprint arXiv:2101.05891 ...Read more

Optimizing spatial specificity and signal quality in fNIRS - PMC


by F Klein · 2024 · Cited by 58 — It highlights the potential challenges in improving spatial specificity and signal quality, discusses possible options to overcome these challenges,Read more

Characterizing reproducibility of cerebral hemodynamic ... - PMC


by DG Wyser · 2022 · Cited by 34 — We investigated the effect of short-channel regression (SCR) as an approach to obtain fNIRS measurements with higher reproducibility on a single ...Read more

Short-channel regression in functional near-infrared ... - PMC


by D Wyser · 2020 · Cited by 118 — We conclude that short-channel regression is most effective when assuming heterogeneous hemodynamics, in particular when combining spatial- and frequency- ...Read more

Hemodynamic correlates of fluctuations in neuronal excitability


by Z Cai · 2022 · Cited by 10 — The relationship between task-related hemodynamic activity and brain excitability is poorly understood in humans as it is technically challenging to combine ...

biorxiv.org
biorxiv.org
Optimizing short-channel regression in fNIRS: an empirical ...


28 May 2025 — A central issue in fNIRS data analysis concerns the removal of systemic physiological noise, particularly through the use of short separation ...Read more

Performance comparison of systemic activity correction in ...


12 Oct 2022 — All correction methods were found to improve signal quality and enhance spatial specificity as compared with the uncorrected data.Read more

Performance comparison of systemic activity correction in ...


1 Apr 2022 — However, fNIRS signals are typically highly contaminated by systemic activity (SA) artifacts and, if not properly corrected, NFB or BCIs run the ...Read more

Optimizing short-channel regression in fNIRS: an empirical ...


24 Nov 2025 — The present study aims to address this issue by systematically evaluating different strategies to use SC information for systemic signal removal ...Read more

Optimizing short-channel regression in fNIRS


24 Nov 2025 — channels (SC) to remove systemic physiological noise. 20. Aim: We aim to evaluate and compare methods of SC regression as implemented in. 21.Read more

Oxygenated hemoglobin signal provides greater predictive ...


by R Luke · 2021 · Cited by 17 — We demonstrate that the fNIRS signal generated by oxygenated hemoglobin provides greater information about the brain state related to the experimental ...

Evaluating the reliability of functional near-infrared ...


20 Jan 2026 — (2024). Optimizing spatial specificity and signal quality in fNIRS-based real-time applications. Frontiers in Neuroergonomics , 5, 1286586.

Robustness of time domain near infrared spectroscopy to ...


25 Jul 2024 — Our findings consistently demonstrate that skin pigmentation has a negligible effect on time domain near infrared spectroscopy results.Read more

frontiersin.org
frontiersin.org
Optimizing spatial specificity and signal quality in fNIRS


by F Klein · 2024 · Cited by 58 — Reflecting the changes in blood flow and oxygenation of the brain, hemodynamic signals are captured using methods such as fMRI and fNIRS and ...Read more

Data leakage in deep learning studies of translational EEG


by G Brookshire · 2024 · Cited by 71 — In the literature review, we find that the majority of translational DNN-EEG studies suffer from data leakage due to data from individual subjects appearing in ...Read more

Unleashing the potential of fNIRS with machine learning


by H Khan · 2024 · Cited by 28 — In this study, we explore the potential of using functional near-infrared spectroscopy (fNIRS) signals in conjunction with modern machine-learning techniques.Read more

Visualization and workload with implicit fNIRS-based BCI


by M Russell · 2025 · Cited by 1 — We trained and tested a first prototype example of a memory prosthesis leveraging a real-time implicit fNIRS-based BCI interface.Read more

Fetal Hemoglobin and Tissue Oxygenation Measured With ...


by E Pritišanac · 2021 · Cited by 48 — Tissue oxygenation measured with near-infrared spectroscopy (NIRS) during neonatal intensive care is directly affected by hemoglobin concentration.

Fast estimation of adult cerebral blood content and ...


by DJF Cohen · 2023 · Cited by 9 — This report presents a fast method for accurate estimation of adult cerebral blood content and oxygenation from hyperspectral time resolved NIRS (trNIRS) data.Read more

Benchmarking framework for machine learning ...


by J Benerradi · 2023 · Cited by 20 — We present an open-source benchmarking framework, BenchNIRS, to establish a best practice machine learning methodology to evaluate models applied to fNIRS data.

Empirical comparison of deep learning models for fNIRS ...


by R Fernandez Rojas · 2024 · Cited by 35 — In this study, we aim to expand previous studies by exploring the use of deep learning models Convolutional Neural Network (CNN), Long Short-Term Memory (LSTM) ...Read more

Functional near-infrared spectroscopy as a diagnostic aid ...


by S Zhang · 2025 · Cited by 1 — The fNIRS technology has been widely utilized to detect biomarkers and evaluate cognitive impairments in various mental disorders. For instance, in major ...Read more

The application of fNIRS in studies on occupational workload


by R Gemmerich · 2025 · Cited by 6 — Functional near-infrared spectroscopy effectively detects neural correlates of occupational workload and provides objective insights into ...Read more

Machine learning and deep learning applied to EEG ...


by A De Giacomo · 2026 · Cited by 1 — Peer-reviewed articles published between 2019 and 2024. Focus on the application of EEG and/or fNIRS techniques to identify neurophysiological biomarkers in ASD ...Read more

The impact of interactive motor-cognitive dual tasking on ...


by X Li · 2025 · Cited by 12 — This study aimed to explore how varying levels of interactive motor-cognitive dual task difficulty affect brain activation, functional connectivity (FC), and ...Read more

Conditional-GAN Based Data Augmentation for Deep ...


by SD Wickramaratne · 2021 · Cited by 63 — fNIRS can be used for task classification, a crucial part of functioning with Brain-Computer Interfaces (BCIs). fNIRS data are multidimensional and complex, ...Read more

A systematic review of functional near-infrared ...


by Y Huang · 2025 — Abstract. Precision in assessing neurological function after stroke is key to optimizing the efficacy of rehabilitation.Read more

Neurotechnology and Systems Neuroergonomics


Published on 05 Jun 2024. Optimizing spatial specificity and signal quality in fNIRS: an overview of potential challenges and possible options for improving ...

and in-hospital near-infrared-spectroscopy (NIRS) ...


by S Schnaubelt · 2025 · Cited by 1 — Feasibility of absolute cerebral tissue oxygen saturation during cardiopulmonary resuscitation. Crit Care Lond Engl. (2013) 17:R36. doi: 10.1186/cc12546.Read more

Effects of Systemic Physiology on Mapping Resting-State ...


by A Abdalmalak · 2022 · Cited by 70 — Our results show that by removing systemic physiology, fNIRS can reproduce resting-state networks often reported with functional magnetic resonance imaging ( ......

spiedigitallibrary.org
spiedigitallibrary.org
DL-QC-fNIRS: a deep learning tool for automated quality ...


by S Guglielmini · 2026 — To prevent data leakage and address inter-subject variability, we employed a subject-wise stratified protocol, ensuring that all samples ...Read more

Functional near-infrared spectroscopy short-channel ...


by J An · 2025 · Cited by 1 — In summary, we aimed to demonstrate that SCR improves fNIRS sensitivity and statistical robustness in well-controlled cognitive paradigms where ...Read more

Transformer-based deep learning model for predicting ...


by S Guglielmini · 2025 — The underlying assumption is that long channels lacking strong coherence with proximal short channels are likely contaminated by artifacts, ...Read more

Performance comparison of systemic activity correction in ...


by F Klein · 2023 · Cited by 34 — All correction methods were found to improve signal quality and enhance spatial specificity as compared with the uncorrected data.Read more

High-density multidistance fNIRS enhances detection of ...


by JE Anderson · 2025 · Cited by 5 — This study provides a statistical comparison of HD and sparse fNIRS performance to inform array selection in future research. Approach. We ...Read more

Noninvasive monitoring of fetal tissue oxygenation level ...


by Z Guo · 2025 — Tissue oxygenation level is usually assessed by the ratio of oxygenated hemoglobin (HbO2 HbO 2 ) and deoxygenated hemoglobin (Hb) concentration ...Read more

a powerful approach to study the embodied human brain


by F Scholkmann · 2022 · Cited by 99 — SPA-fNIRS enables to study the embodied brain by linking the brain with the physiological state of the entire body, allowing novel insights into their complex ...Read more

Systemic physiology augmented functional near-infrared ...


by S Guglielmini · 2022 · Cited by 27 — Aim: In our exploratory study, we extended classical fNIRS hyperscanning by adding systemic physiological measures to obtain systemic physiology ...Read more

Transformer-based deep learning model for predicting ...


by S Guglielmini · 2025 — the spatial and temporal dependencies inherent in fNIRS time series, outperforming recurrent architectures known to struggle with long-range ...Read more

Comparison of functional activation responses from the ...


by PPS Mohammad · 2021 · Cited by 6 — Aim: We explore the differences between CW-NIRS and multi-distance FD-NIRS by comparing measurements of functional activation in the human auditory cortex.Read more

Deep learning in fNIRS: a review


by C Eastmond · 2022 · Cited by 159 — ... Neurophotonics 9(4), 041411 (20 July 2022). https://doi.org/10.1117/1.NPh.9.4.041411. Received: 26 January 2022; Accepted: 22 June 2022; Published: 20 July 2022.

Best practices for fNIRS publications


by MA Yücel · 2021 · Cited by 684 — Our paper has been designed to provide guidelines to help enhance the reliability, repeatability, and traceability of reported fNIRS studies and encourage best ...

Performance comparison of systemic activity correction in ...


by F Klein · 2023 · Cited by 34 — Skip to main content.

Functional near-infrared spectroscopy short-channel ...


by J An · 2025 · Cited by 1 — Functional near-infrared spectroscopy short-channel regression improves cortical activation estimates of working memory load ... Schönhammer ...Read more

Robustness of tissue oxygenation estimates by continuous ...


by C Amendola · 2023 · Cited by 17 — We studied the accuracy and robustness of SRS NIRS. We investigated the errors in retrieving hemodynamic parameters, in particular tissue oxygen saturation.Read more

mdpi.com
mdpi.com
The Influence of Extracerebral Tissue on Continuous Wave ...


by N Eleveld · 2023 · Cited by 21 — We conclude that extracerebral tissue indeed influences NIRS measurements, although the evidence (ie, correlation) for this influence varies considerably ...Read more

Advancing Cognitive Load Detection in Simulated Driving ...


by MA Khan · 2025 — A sliding window approach was applied to the time-series fNIRS data to capture short-term fluctuations in brain activation. The data were analyzed using EEGNet, ...Read more

From Biosignals to Bedside: A Review of Real-Time Edge ...


by M Oloko-Oba · 2026 — First, leakage via preprocessing and window overlap. When windows overlap heavily, adjacent segments can be near duplicates. Randomly splitting at the window ...Read more

Enhancing Cognitive Workload Classification Using ...


by MA Khan · 2025 · Cited by 15 — (3) The study demonstrates that fNIRS signals can be effectively utilized for automatic cognitive load classification. (4) The performance of the proposed ...Read more

Reference Values of Regional Oxygen Saturation (rSO 2 ) ...


by A Lubkowska · 2024 · Cited by 9 — Near-infrared spectroscopy (NIRS) is a non-invasive method for monitoring the availability and use of oxygen by tissues, first introduced in ...Read more

Assessment of Microcirculatory Dysfunction by Measuring ...


by J Sato · 2024 · Cited by 3 — We measured subcutaneous regional tissue oxygen saturation (rSO2) with near-infrared spectroscopy (NIRS), which can assess microcirculation in patients with ...Read more

An SPA-fNIRS Study


by F Scholkmann · 2022 · Cited by 14 — Our study demonstrates the usefulness and necessity of the SPA-fNIRS approach to gain insights into the individual variability of hemodynamic responses ...Read more

Functional Near-Infrared Spectroscopy Analysis of ...


by CS Park · 2024 · Cited by 1 — This study applied functional near-infrared spectroscopy (fNIRS) to analyze the changes in cerebral oxygen saturation (COS) and hemoglobin (Hb) concentrationsRead more

Comparison of Different Approaches Estimating Skeletal ...


by FK Paternoster · 2022 · Cited by 5 — This shows that at least five different ways (O2Hb, HHb, Hbdiff, Hbmean, and TSI) to estimate the muscle oxygen consumption using CW-NIRS ...Read more

Machine Learning Models to Predict Individual Cognitive ...


by W Chen · 2025 · Cited by 8 — By integrating fNIRS and eye-tracking data, this study aims to offer a more accurate, data-driven approach to cognitive load measurement, moving beyond ...Read more

A High-Accuracy and Interpretable Decoding Method for ...


by Q Han · 2025 · Cited by 3 — To assess the generalization ability of the TopoTempNet model on unseen subjects, this study adopts the Leave-One-Subject-Out Cross-Validation (LOSO-CV) ...Read more

Exploring Effects of Mental Stress with Data Augmentation ...


by MNA Khan · 2025 · Cited by 4 — fNIRS has been used to investigate a variety of brain activity, such as cognitive and motor processes [5,6,7,8]. fNIRS is being used more often ...

Continuous Monitoring of Muscle Oxygenation in ...


by E Peikon · 2025 · Cited by 1 — This study aimed to validate a non-invasive wearable sensor capable of measuring muscle oxygen saturation (SmO2) using continuous-wave near-infrared ...Read more

Exploring New Horizons: fNIRS and Machine Learning in ...


by A Morales-Cervantes · 2025 — To move beyond model benchmarking and provide interpretable insight from the fNIRS data, we conducted a two-step feature-level analysis: (i) a supervised ...Read more

Evaluating the Impact of Windowing Techniques on Fourier ...


by NP Martono · 2024 · Cited by 13 — This study evaluated the impact of different windowing techniques applied to Fourier transform-preprocessed ECG signals on the classification accuracy of deep ...R...

researchgate.net
researchgate.net
Short-separation regression incorporated diffuse optical ...


3 May 2023 — The benefits are marginal at small brain activation. Conclusions The SS-DOT model improves the fNIRS image reconstruction quality.Read more

(PDF) Data Leakage in Deep Learning for Alzheimer's ...


2 Sept 2025 — This scoping review investigates whether methodological flaws, particularly data leakage, systematically inflates performance metrics, and ...Read more

(PDF) Deep learning in fNIRS: a review


Conclusions: The application of DL techniques to fNIRS studies has shown to mitigate many of the hurdles present in fNIRS studies such as lengthy data ...Read more

Advancing Cognitive Load Detection in Simulated Driving ...


4 Aug 2025 — A sliding window approach was applied to the time-series fNIRS data to capture short-term fluctuations in brain activation. The data were ...Read more

(PDF) Personalized Stress Detection Using Biosignals from ...


by M Bolpagni · 2024 · Cited by 67 — This paper presents a scoping review of personalized stress detection models using wearable technology.Read more

(PDF) Mental workload classification using convolutional ...


9 Dec 2023 — This study was to investigate the potential use of convolutional neural networks (CNNs) based on functional near-infrared spectroscopy (fNIRS)- ...Read more

Transformer-based deep learning model for predicting ...


19 Jan 2026 — Approach We trained the model on a resting-state fNIRS dataset (69 subjects) with paired short- and long-separation recordings. Dual-wavelength ...Read more

(PDF) Robust Mental Workload Classification Under Noisy ...


6 May 2026 — This study investigates robust mental workload classification under noisy fNIRS signal conditions by leveraging advanced machine learning ...Read more

(PDF) Short-channel regression in functional near-infrared ...


In particular, we highlight that short-channel regression is more effective when combining multiple scalp regressors and when MWs are additionally included.Read more

Performance comparison of systemic activity correction in ...


12 Oct 2022 — Performance comparison of systemic activity correction in functional near-infrared spectroscopy for methods with and without short distance ...Read more

Modified Beer's Law – historical perspectives and ...


This manuscript focuses on the development of quantitative absorption laws of light energy, from the inception of Bouguer Law to Beer's Law, to gain a ...Read more

Comparison of frequency-domain and continuous-wave ...


18 Feb 2020 — Although FD-NIRS devices have technical advantages over CW-NIRS devices, FD-NIRS devices may overestimate true cerebral oxygenation and their ...Read more

Near-infrared spectroscopy: A methodology-focused review


Changes in tissue oxygenation index (TOI) were registered based on spatially resolved spectroscopy and calculated as [O 2 Hb]/([O 2 Hb] + [HHb]) × 100 (Pellicer ...Read more

Fetal Hemoglobin and Tissue Oxygenation Measured With ...


13 Aug 2021 — Near-infrared spectroscopy enables the measurement of regional cerebral tissue oxygen saturation (rScO2) and in combination with measurements of ...

(PDF) Review of recent advances in frequency-domain ...


12 Jun 2023 — Over the past several decades, near-infrared spectroscopy (NIRS) has become a popular research and clinical tool for non-invasively ...Read more

(PDF) Benchmarking framework for machine learning ...


3 Mar 2023 — The BenchNIRS framework, using a robust methodology with nested cross-validation, enables researchers to optimise models and evaluate them ...

Typical time course of the NIRS variables ([Hb02], [HbR], ...


We used near-infrared spectroscopy (NIRS) to study noninvasively the influence of aging on changes in the local concentration of oxygenated hemoglobin ([HbO2]), ...Read more

Can O2 saturation assessed through NIRS present ...


22 Mar 2016 — I am computing O2 saturation levels as the rate between HbO and HbT (HbO/HbT) recorded through fNIRS. While most of the outputs range between 0-1, I have ...

(PDF) Measuring tissue hemodynamics and oxygenation ...


23 Apr 2026 — Continuous-wave near-infrared spectroscopy and imaging enable tissue hemodynamics and oxygenation to be determined non-invasively.Read more

Reference Ranges for Cerebral Tissue Oxygen Saturation ...


1 Sept 2015 — Non-invasive monitoring of the brain with near-infrared spectroscopy (NIRS) during immediate transition after birth is of growing interest.Read more

Systemic physiology augmented functional near-infrared ...


9 May 2022 — The study revealed that eye contact leads to significant synchronization of spontaneous activity of the brain and body physiology. Our study is ...Read more

Advancing Functional Near-Infrared Spectroscopy (fNIRS) ...


18 Mar 2026 — This review paper highlights transformer architectures in fNIRS-based studies, with a particular focus on advanced modifications in key stages ...Read more

(PDF) Enhancing Cognitive Workload Classification Using ...


10 Feb 2025 — Functional near-infrared spectroscopy (fNIRS) is employed as a non-invasive method to monitor functional brain activation by capturing ...Read more

Deep Learning Forecast of Perceptual Load Using fNIRS ...


5 May 2026 — In this paper, we present a novel approach to forecasting perceptual load in demanding piloting tasks, based on neurophysiological response data.Read more

A typical example of raw HbO, HbR, and HbT data (Subject ...


Functional near-infrared spectroscopy (fNIRS) is used to detect concentration changes of oxy-hemoglobin and deoxy-hemoglobin in the human brain.Read more

Applications of Functional Near-Infrared Spectroscopy ...


1 Jul 2025 — fNIRS is an effective tool for enhancing cognitive performance, observing neurological adaptations, and understanding the acute and chronic effects of exercise.Read more

(PDF) The potential of machine learning in diagnosing ...


4 Jun 2025 — We aim to explore the application of machine learning (ML) and deep learning (DL) algorithms in the diagnosis of neurological and psychiatric diseases.Read more

Diagnostic machine learning applications on clinical ...


This review provides an overview of research on psychiatric diseases ... (fNIRS) Signals in Schizophrenia and Bipolar Disorder Using Deep Learning Methods.Read more

(PDF) Balanced Leave-One-Subject-Out Cross- Validation ...


2 May 2026 — We address this question using leave-one-subject- out cross-validation (LOSO CV) to simulate inclusion of test data from future subjects.Read more

[PDF] Deep learning in fNIRS: a review - ResearchGate


Neurophotonics. 041411-1. Oct-Dec 2022. Vol. 9(4). Downloaded From: https://www.spiedigitallibrary.org/journals/Neurophotonics on 21 Jul 2022. Terms of Use ...

Learning based motion artifacts processing in fNIRS: a mini ...


8 Nov 2023 — This paper provides a concise review of learning-based motion artifacts (MA) processing methods in functional near-infrared spectroscopy ...

Hybrid Deep Learning Model to Estimate Cognitive Effort ...


29 Apr 2026 — The result shows that the hybrid CNN-GRU gives better performance with 78.36\% training accuracy and 73.08\% test accuracy than other models. We ...Read more

(PDF) Estimating Cognitive Effort from Functional Near ...


18 Jul 2025 — PreprintPDF Available. Estimating Cognitive Effort from Functional Near-Infrared Spectroscopy (fNIRS) Signals using Machine Learning. July 2025.Read more

Naturalistic fNIRS assessment reveals decline in executive ...


Naturalistic fNIRS assessment reveals decline in executive function and altered prefrontal activation following social media use in college students. Springer ...Read more

(PDF) Conditional-GAN Based Data Augmentation for ...


PDF | Functional near-infrared spectroscopy (fNIRS) is a neuroimaging technique used for mapping the functioning human cortex. fNIRS can be widely used.

Optimizing spatial specificity and signal quality in fNIRS


18 Sept 2024 — ... reliability of real-time applications. September 2024. DOI:10.13140/RG.2.2.27553.21605. Conference: fNIRS 2024. Authors: Franziska Klein at Carl ...Read more

(PDF) Functional near-infrared spectroscopy short-channel ...


ArticlePDF Available. Functional near-infrared spectroscopy short-channel regression improves cortical activation estimates of working memory load. SPIE, the ...Read more

A Functional Near-Infrared Spectroscopy (fNIRS) and ...


3 Apr 2026 — Our study showed that working memory load during a visuospatial n-back task influenced behavioral and electrophysiological indices. Even if the ...Read more

Quantitative Analysis of Tissue Oxygenation Variability ...


4 Aug 2025 — Robustness of tissue oxygenation estimates by continuous wave space-resolved near infrared spectroscopy. J. Biomed. Opt. 28 (7),. 075002 (2023).Read more

Single Source-Detector Separation Approach to Calculate ...


8 May 2026 — Single Source-Detector Separation Approach to Calculate Tissue Oxygen Saturation Using Continuous Wave Near-Infrared Spectroscopy. January ...Read more

semanticscholar.org
semanticscholar.org
Comparison of frequency-domain and continuous-wave ...


Although FD-NIRS devices may overestimate true cerebral oxygenation and their benefits might not outweigh the usability of the more clinically viable ...

Tissue oxygenation monitor using NIR spatially resolved ...


A broadband multi-distance approach to measure tissue oxygen saturation with continuous wave near-infrared spectroscopy ... A novel algorithm, broadband spatially ...Read more

Systemic physiology augmented functional near-infrared ...


Continuous coloured light altered human brain haemodynamics and oxygenation assessed by systemic physiology augmented functional near-infrared spectroscopy.Read more

Cross-correlation between HbO and HbR as an effective ...


This paper presents a cross-correlation between HbO and HbR as a feature that can determine the dynamic noise of fNIRS. The general linear model (GLM) as a ...

Improving the diagnostic accuracy for major depressive ...


Improving the diagnostic accuracy for major depressive disorder using machine learning algorithms integrating clinical and near-infrared spectroscopy data.Read more

Deep learning in fNIRS: a review - Semantic Scholar


Deep learning in fNIRS: a review · Condell Eastmond, Aseem Pratap Subedi, +1 author. X. Intes · Published in Neurophotonics 31 January 2022 · Computer Science, ...

[PDF] A Deep Learning Based Ternary Task Classification ...


The proposed method converts the raw fNIRS time series data into an image using Gramian Angular Summation Field and a Deep Convolutional Neural Network ...

[PDF] Optimizing spatial specificity and signal quality in fNIRS


DOI:10.3389/fnrgo.2024.1286586; Corpus ID: 270302339. Optimizing spatial specificity and signal quality in fNIRS: an overview of potential challenges and ...Read more

[PDF] Functional near-infrared spectroscopy short-channel ...


Functional near-infrared spectroscopy short-channel regression improves cortical activation estimates of working memory load · Jiahui An, Pulkit Goyal, +1 authorRead more

re.public.polimi.it
re.public.polimi.it
Assessment of fNIRS Signal Processing Pipelines


by A Bonilauri · 2022 · Cited by 41 — The block average of the hemodynamic response function was compared with generalized linear model fitting. Maps of significant activa- tion/ ...Read more

link.springer.com
link.springer.com
Monitoring tissue oxygenation index using near‐infrared ...


by J Tsukuda · 2021 · Cited by 10 — Tissue oxygenation index (TOI) using the near infrared spectroscopy (NIRS) has been demonstrated as a useful indicator to predict return of ...

Reconstructing damaged fNIRS signals with a generative ...


by Y Zhi · 2024 · Cited by 7 — Here, we proposed a generative deep learning approach to recover damaged fNIRS signals in one or more measurement channels.Read more

Near-Infrared Spectroscopy (NIRS) | Springer Nature Link


by M El-Dib · 2025 — Near-infrared spectroscopy (NIRS) is a non-invasive technique that can measure tissue oxygen saturation in organs such as the brain, kidney, and intestine.Read more

Applications of artificial intelligence in mental health


by A Wajid · 2025 · Cited by 6 — This systematic literature review (SLR) critically examines peer-reviewed studies on the applications of AI technologies in mental health to ...Read more

The potential of machine learning in diagnosing neurological ...


by C Ricetti · 2025 · Cited by 5 — 1 offers a general overview of the use of machine learning algorithms to diagnose both neurological and psychiatric diseases. Section 2 contains ...Read more

Functional connectivity in whole-brain and network analysis ...


by S Wu · 2025 · Cited by 2 — A leave-one-out cross-validation procedure [11, 13, 43] was used to evaluate the classifier, utilizing a set of 52 feature vectors extracted ...Read more

fnirs.org
fnirs.org
Publications Highlights – May 2022 to February 2023


1 May 2022 — Publications Highlights – May 2022 to February 2023 · fNIRS papers posted on Facebook and Twitter (#fNIRS) · Neurophotonics latest issues · From ...Read more

Best practices for fNIRS publications


5 Jul 2021 — The best practices paper provides guidelines to help increase the reproducibility, reliability and traceability of our work through presenting ...Read more

Sa-106-fNIRS Short Channel Regression Improves ...


1 Jan 2024 — Sa-106-fNIRS Short Channel Regression Improves Cortical Activation Estimates of Working Memory Load. By s.monterohdz in sfNIRS2024-Session-2 ...Read more

Confounding effects – The Society for functional Near Infrared Spectroscopy


Total lines: 140

Neurophotonics


Neurophotonics covers advances in optical technology applicable to study of the brain and their impact on the basic and clinical neuroscience applications.Read more

fNIRS publications on PubMed: May 1, 2022


16 Mar 2023 — Oxyhemoglobin and deoxyhemoglobin concentration changes (?HbO2 and ?HbR, respectively) were recorded in the ipsilateral and contralateral ...Read more

fNIRS publications on PubMed: January 1, 2022 - April 30, ...


... hemoglobin difference (Hbdiff) changes during post-exercise piano performance using functional near-infrared spectroscopy (fNIRS). The results indicate that ...Read more

fNIRS publications on PubMed: July 1, 2021


1 Jan 2022 — OBJECTIVE: This study aims to understand the neural and hemodynamic responses during general anesthesia in order to develop a comprehensive ...

arxiv.org
arxiv.org
Hybrid Deep Learning Model to Estimate Cognitive Effort ...


29 May 2025 — This study estimates cognitive effort (CE) based on functional near- infrared spectroscopy (fNIRS) data and performance scores using a hybrid deep learning ( ...Read more

Rethinking the Ability of Deep Learning in fNIRS to Exclude ...


28 Feb 2024 — The data are then segmented with a sliding window approach (3-second window size and 1-second step size) [7] , and underwent normalization.Read more

Combining Facial Videos and Biosignals for Stress ...


10 Jan 2026 — Signals are temporally aligned, cleaned to ensure monotonic timestamps, and segmented into non-overlapping 9 s windows. Report issue for ...Read more

Real-World fNIRS-Based Brain-Computer Interfaces


by M Ghalavand · 2025 · Cited by 1 — This study investigates the classification of rest and task states during a realistic, interactive tennis simulation using fNIRS signals and a ...Read more

Real-World fNIRS-Based Brain-Computer Interfaces


15 May 2025 — This study provides a systematic comparison of machine learning methodologies for classifying rest and task states from fNIRS signals in a ...Read more

[2407.15901] Enhancing Cognitive Workload Classification ...


by MA Khan · 2024 · Cited by 15 — Functional near-infrared spectroscopy (fNIRS) is employed as a non-invasive method to monitor functional brain activation by capturing changes ...Read more

CCNet: Criss-Cross Attention for Semantic Segmentation


https://arxiv.org/abs/1811.11721

Hybrid Deep Learning Model to Estimate Cognitive Effort ...


3 Apr 2025 — This study estimates cognitive effort (CE) based on functional near-infrared spectroscopy (fNIRS) data and performance scores using a hybrid ...Read more

Calibration of Deep Learning Classification Models in fNIRS


20 Mar 2024 — [11] proposed a transformer-based classification network (fNIRS-T), to enhances network representation capabilities by exploring spatial-level ...Read more

A Scoping Review of Functional Near-Infrared ...


28 Oct 2025 — Functional Near-Infrared Spectroscopy (fNIRS) has emerged as a valuable tool to investigate cognitive and emotional processes during learning.Read more

Deep Learning in fNIRS: A review


by C Eastmond · 2022 · Cited by 158 — Results: Of the 63 papers considered in this review, 32 report a comparative study of deep learning techniques to traditional machine learning techniques where ...

Deep Learning in fNIRS: A review


https://arxiv.org/abs/2201.13371

Calibration of Deep Learning Classification Models in fNIRS


https://arxiv.org/abs/2402.15266

Hybrid Deep Learning Model to Estimate Cognitive Effort from fNIRS Signals in Educational Game Playing


https://arxiv.org/abs/2504.13883

Hybrid Deep Learning Model to Estimate Cognitive Effort ...


by S Sharmin · 2025 · Cited by 3 — The aim of this study is to estimate cognitive effort during educa- tional tasks by analyzing fNIRS-derived hemodynamic responses and predicted ...Read more

A Deep Learning Based Ternary Task Classification System Using Gramian Angular Summation Field in fNIRS Neuroimaging Data


https://arxiv.org/abs/2101.05891

A Deep Learning Based Ternary Task Classification ...


by SD Wickramaratne · 2021 · Cited by 40 — The proposed system uses a Convolutional Neural Network system to classify. Gramian Angular Summation Field images generated using only fNIRS ...Read more

A neuroergonomics model to evaluating nuclear power plants operators' performance under heat stress driven by ECG time-frequency spectrums and fNIRS prefrontal cortex network: a CNN-GAT fusion model


https://arxiv.org/abs/2404.02439

Discriminative Correlation Filter with Channel and Spatial Reliability


https://arxiv.org/abs/1611.08461

3D Gaussian Splatting for Real-Time Radiance Field Rendering


https://arxiv.org/abs/2308.04079

Deep-learning-enabled Brain Hemodynamic Mapping Using Resting-state fMRI


https://arxiv.org/abs/2204.11669

Dual-slope imaging of cerebral hemodynamics with frequency-domain near-infrared spectroscopy


https://arxiv.org/abs/2207.14761

sciencedirect.com
sciencedirect.com
Near-Infrared Spectroscopy (NIRS) for Cerebral and Tissue ...


by J Ali · 2022 · Cited by 115 — This review analyzes the published data and provides the clinician a comprehensive account of the perioperative utility of NIRS in cardiac, vascular and ...Read more

EEG–fNIRS signal integration for motor imagery ...


by ME Seno · 2025 · Cited by 2 — The specific normalization formula is as follows:(9) A − data [ i , : , t ] = fNIRS [ i , : , t ] − mean ( fNIRS [ i , : , t ] ) std ( fNIRS [ i , : , t ] ) ...Read more

A two-phase approach for leak detection and localization in ...


by M Adraoui · 2024 · Cited by 25 — This paper presents a novel two-phase approach for leak detection and localization in water distribution systems using wavelet decomposition and machine ...Read more

Real time detection of cognitive load using fNIRS: A deep ...


by S Karmakar · 2023 · Cited by 60 — fNIRS is a non-invasive tool for monitoring functional brain activation that records changes in oxygenated hemoglobin (HbO) and deoxygenated hemoglobin (HbR) ...Read more

Fast noniterative data analysis method for frequency ...


by J Kim · 2022 · Cited by 7 — By using the microscopic Beer–Lambert law (MBL), we propose a fast and effective analysis method for retrieving the absorption coefficient ...Read more

Correcting physiological noise in whole-head functional ...


by F Zhang · 2021 · Cited by 48 — An automated denoising method is developed for whole-head fNIRS recordings. Removal of noise is based on long-/short-separation channels and auxiliary ...Read more

Functional near Infrared Spectroscopy - an overview


Specifically, it measures the degree of tissue oxygen saturation and changes in hemoglobin volume using near-infrared light (Ferrari et al., 2004). Near ...Read more

Hemodynamics and vascular oxygenation measured at the ...


by S Guglielmini · 2025 · Cited by 5 — In our SPA-fNIRS study we found that changes in breathing affected hemodynamics and oxygenation in both the extracerebral and cerebral tissue layers of the ...Read more

Classification Algorithm for fNIRS-based Brain Signals ...


by Y Qin · 2024 · Cited by 16 — We proposed an end-to-end hybrid neural network for feature extraction of fNIRS. The method utilizes a spatial–temporal convolutional layer for automatic ...Read more

FCS-TPNet: Fusion of fNIRS chromophore signals to ...


by L Yang · 2025 · Cited by 3 — In the graph learning stage, we construct temporal-spatial graph representation and employ dynamic graph convolution to learn advanced spatial patterns. Finally ...Read more

Applications of functional near-infrared spectroscopy ...


by C Peng · 2021 · Cited by 61 — This review investigates studies that have applied fNIRS to investigate neonatal brain function. fNIRS permits a deeper understanding of neonatal brain function ...Read more

A cross-task fNIRS framework for multi-class mental health ...


by MB Yang · 2026 · Cited by 1 — This study demonstrates that integration of fNIRS with adaptive machine learning approaches provides a scalable and interpretable framework for mental health ...Read more

Diagnosis of mental disorders using machine learning


by CM Sharma · 2024 · Cited by 35 — This study presents a bibliometric analysis and review of the research, published over the last 10 years.Read more

Hybrid EEG-fNIRS decoding with dynamic graph ...


by H Wang · 2025 · Cited by 30 — Moreover, the leave-one-subject-out testing shows that the proposed method is superior to that of the current state-of-the-art methods, like hybrid EEGNet, ...Read more

Deep Learning Approach for Finger Tapping Classification


by O Zulfiqar · 2025 — This study examines the process of classifying finger tapping data that consists of five classes with the help of fNIRS signals and compares the four deep ...

An fNIRS representation and fNIRS-scales multimodal ...


by S Cheng · 2024 · Cited by 14 — Wickramaratne et al. [28] has more closely linked fNIRS and GAF and classified different brain activity states. The classification accuracy of the GAF ...

Functional near infrared spectroscopy for brain ...


by V Akila · 2023 · Cited by 11 — This research aims to analyze the connectivity between different regions of the brain using graph theory and hence the geometrical association of brain ...Read more

A state-of-the-art review of scientific, industrial, and ...


by AL Sousa · 2026 — Building on previous research, this study conducts a revision on three key branches of water leakage detection and localization analysis. First, it presents a ...Read more

nirx.net
nirx.net
Beyond the Brain: Physiological Signals in fNIRS Research


4 Jun 2025 — In fNIRS, there are two primary approaches to measuring systemic influences: short-distance detectors capture extracerebral systemic signals ...Read more

thejcn.com
thejcn.com
Functional Near-Infrared Spectroscopy as a Personalized ...


by Z Phillips V · 2023 · Cited by 32 — This review covers the contribution of fNIRS to the personalized goals of digital healthcare in neurology by identifying two major trends that drive current ...Read more

discovery.ucl.ac.uk
discovery.ucl.ac.uk
A Novel Approach to Monitor Tissue Oxygen Saturation with ...


by Z Kovacsova · 2020 · Cited by 2 — The project is focused on the development of a novel algorithm to recover oxygenation with broadband near-infrared spectroscopy (NIRS). The ...Read more

Best practices for fNIRS publications - UCL Discovery


by MA Yücel · 2021 · Cited by 684 — Our paper has been designed to provide guidelines to help enhance the reliability, repeatability, and traceability of reported fNIRS studies.

openfnirs.org
openfnirs.org
Physiological interference & short-separation regression


Neurophotonics Center, Boston University. fNIRS Workshop, November 6-8 ... Obtain external measures of this systemic physiology and regress from NIRS data.Read more

Modified Beer-Lambert Law


1 Jan 2024 — A common approach to measuring changes in the tissue absorption using continuous waves methods is based on a generalization of Beer-Lambert law.Read more

Systemic physiology augmented functional near-infrared ...


1 Jan 2024 — Definition: Systemic physiology augmented functional near-infrared spectroscopy (SPA-NIRS) is a method that uses fNIRS data in combination ...Read more

medrxiv.org
medrxiv.org
Diagnostic Machine Learning Applications on Clinical ...


25 Sept 2023 — This review provides an overview of research on psychiatric diseases by using fNIRS and ML. Article search was carried out and 45 studies were evaluated.Read more

hanbnrd.gitlab.io
hanbnrd.gitlab.io
A benchmarking framework for improving machine learning ...


In this thesis, we will explore machine learning with fNIRS, its standards and best practices, its benchmarks on popular tasks, and its novel approaches, under ...Read more

BenchNIRS 1.7.1 documentation - Johann Benerradi - GitLab


Below is a proposed checklist of recommendations toward best practices for machine learning with fNIRS ( BenchNIRS provides an API for the checked items).

fNIRS • Mental workload assessment


A set of 30 fNIRS and ECG features proposed in this paper enables the classification of different levels of cognitive load on n-back task using the support ...Read more

nature.com
nature.com
Multimodal EEG–fNIRS classification as a clinical tool for ...


by I Tahir · 2026 — This study examines the use of a multimodal approach combining electroencephalography (EEG) and functional near-infrared spectroscopy (fNIRS) to ...Read more

Evaluation of fNIRS signal components elicited by ...


by P Reddy · 2021 · Cited by 43 — The most direct techniques that utilize short SDS channels are the least squares adaptive filters and regression modelling. Although these ...Read more

fNIRS reproducibility varies with data quality, analysis ...


by MA Yücel · 2025 · Cited by 22 — Short separation regression improves statistical significance and better localizes the hemodynamic response obtained by near-infrared ...Read more

Quantitative analysis of tissue oxygenation variability ...


by APP Rad · 2025 · Cited by 5 — This study aimed to characterize baseline regional tissue oxygen saturation (rSO2) across 17 anatomical landmarks in healthy adults and to ...Read more

Reliability of brain metrics derived from a Time-Domain ...


by J Dubois · 2024 · Cited by 10 — Results demonstrated high reliability in resting state features including hemoglobin concentrations, head tissue light attenuation, amplitude of ...Read more

Functional near-infrared spectroscopy for the detection of ...


by JL Gómez-Sirvent · 2025 — In the subject-independent approach, a leave-one-subject-out cross-validation was performed. For each iteration, one participant was held ...Read more

A functional near-infrared spectroscopy study on the ...


by C Geissler · 2023 · Cited by 14 — fNIRS results indicated reduced mental load after saving, confirming the assumption that saving triggers cognitive offloading.Read more

The role of cerebral oxygenation in pediatric lower ...


by M Lacerenza · 2025 · Cited by 2 — Robustness of tissue oxygenation estimates by continuous wave Space-Resolved near infrared spectroscopy. J. Biomed. Opt. 28 https://doi.org ...Read more

biyoklinikder.org
biyoklinikder.org
Comparison of Machine Learning Algorithms for Yes/No ...


by S Erdoğan · 2024 · Cited by 2 — In contrast, fNIRS is less expensive, has greater tolerance to motion artifacts, and allows for better mobility [5]. The majority of fNIRS-based BCI studies ...Read more

pubs.aip.org
pubs.aip.org
Biosignal-integrated robotic systems with emerging trends in ...


Review Article| February 21 2024 Biosignal-integrated robotic systems with emerging trends in visual interfaces: A systematic reviewRead more

opg.optica.org
opg.optica.org
CGAN-rIRN: a data-augmented deep learning approach to ...


The proposed CGAN-rIRN approach improves the single-trial accuracy for mental arithmetic and mental singing tasks in both the data augmentation and classifier.Read more

Review of recent advances in frequency-domain near- ...


by X Zhou · 2023 · Cited by 48 — Spatially resolved spectroscopy (SRS) can be used to estimate absolute tissue oxygen saturation ... oxygenation monitor using NIR spatially resolved spectroscopy ...Read more

Investigating the effect of limited spectral information on ...


by G Leadley · 2024 · Cited by 11 — This paper investigates the theoretical capability of near-infrared spectroscopy (NIRS) systems to accurately measure changes in the ...Read more

artinis.com
artinis.com
Publication overview 2024 - fNIRS studies with our devices


6 Feb 2025 — We are happy to share, that in 2024 an increased number of papers were published using our devices to measure brain activity.Read more

Tissue Saturation Index (TSI) - Absolute oxygenation ...


27 Oct 2022 — Tissue Saturation Index (TSI) is an absolute measure for the local tissue oxygenation in tissue beneath the sensor.

spectroscopyonline.com
spectroscopyonline.com
Deep Learning Model Improves Detection of Mild Cognitive ...


New deep learning model using full fNIRS time-series data was able to diagnose mild cognitive impairment (MCI) with over 93% ...Read more

repository.cam.ac.uk
repository.cam.ac.uk
Artifact Management for Cerebral Near-Infrared Spectroscopy ...


by T Bergmann · 2024 · Cited by 5 — The objective of this review is to comprehensively examine the literature on existing artifact management methods for cerebral NIRS signals recorded in animals ...Read more

papers.ssrn.com
papers.ssrn.com
1 A standardized and reproducible fNIRS ...


The pipeline starts from data standardization and metadata completeness, proceeds through objective quality control, optical density (OD) conversion, motion ...Read more

direct.mit.edu
direct.mit.edu
Multimodal fNIRS–EEG sensor fusion: Review of data- ...


Our review indicates that while many studies incorporate robust artifact handling for EEG, confounder correction in fNIRS remains limited to filtering or motion ...Read more

eprints.whiterose.ac.uk
eprints.whiterose.ac.uk
A Real-Time Machine Learning Module for Motion Artifact ...


by R Ercan · 2024 · Cited by 2 — This study trains a Support Vector Machine (SVM) algorithm and proposes a hardware design approach based on an FPGA to achieve the first real-time fNIRS motion ...Read more

udspace.udel.edu
udspace.udel.edu
Hybrid Deep Learning Model to Estimate Cognitive Effort from ...


by S Sharmin · 2025 · Cited by 3 — In this work, by applying a Convolutional. Neural Network- Gated Recurrent Unit (CNN-GRU) DeepNet model to estimate performance from fNIRS ...Read more

pubmed.ncbi.nlm.nih.gov
pubmed.ncbi.nlm.nih.gov
Functional near-infrared spectroscopy short-channel ...


by J An · 2025 · Cited by 1 — Functional near-infrared spectroscopy short-channel regression improves cortical activation estimates of working memory load. Neurophotonics. 2025 Jul;12(3): ...Read more

Benchmarking framework for machine learning ...


by J Benerradi · 2023 · Cited by 20 — We present an open-source benchmarking framework, BenchNIRS, to establish a best practice machine learning methodology to evaluate models applied to fNIRS data.Read more

a powerful approach to study the embodied human brain


by F Scholkmann · 2022 · Cited by 100 — SPA-fNIRS enables to study the embodied brain by linking the brain with the physiological state of the entire body, allowing novel insights into their complex ...Read more

Deep learning in fNIRS: a review - PubMed - NIH


by C Eastmond · 2022 · Cited by 158 — Deep learning in fNIRS: a review. Neurophotonics. 2022 Oct;9(4):041411. doi: 10.1117/1.NPh.9.4.041411. Epub 2022 Jul 20. Authors. Condell Eastmond , Aseem ...

Best practices for fNIRS publications - PubMed - NIH


by MA Yücel · 2021 · Cited by 684 — Best practices for fNIRS publications. Neurophotonics. 2021 Jan;8(1):012101. doi: 10.1117/1.NPh.8.1.012101. Epub 2021 Jan 7. Authors. Meryem A ...

Performance comparison of systemic activity correction in ...


by F Klein · 2023 · Cited by 34 — Performance comparison of systemic activity correction in functional near-infrared spectroscopy for methods with and without short distance channels · Authors.Read more

Optimizing spatial specificity and signal quality in fNIRS


by F Klein · 2024 · Cited by 58 — ... improving the reliability of real-time applications. Front Neuroergon. 2024 Jun 5:5:1286586. doi: 10.3389/fnrgo.2024.1286586. eCollection 2024. Author.Read more

Characterizing reproducibility of cerebral hemodynamic ...


by DG Wyser · 2022 · Cited by 34 — We report, for the first time, that fNIRS measurements are reproducible on a single-subject level using our optoHIVE fNIRS system and that SCR improves ...Read more

Robustness of tissue oxygenation estimates by continuous ...


by C Amendola · 2023 · Cited by 17 — We studied the accuracy and robustness of SRS NIRS. We investigated the errors in retrieving hemodynamic parameters, in particular tissue oxygen saturation.Read more

how robust are the different calculation methods against ...


by F Scholkmann · 2014 · Cited by 107 — Continuous-wave near-infrared spectroscopy and imaging enable tissue hemodynamics and oxygenation to be determined non-invasively.

pdfs.semanticscholar.org
pdfs.semanticscholar.org
Functional near-infrared spectroscopy short-channel ...


by J An · Cited by 1 — short-channel regression improves cortical activation estimates of working memory load. Jiahui An ,a Pulkit Goyal ,b Andreas R. Luft,c,d and ...Read more

hal.science
hal.science
Optimizing short-channel regression in fNIRS


20 Nov 2025 — Figure 6: Full short-channel availability ... recovered qualitatively similar activation patterns in the occipital cortex across both.Read more

The fNIRS Reproducibility Study Hub (FRESH)


by MA Yücel · 2024 · Cited by 26 — short-channel measurements as proxies for systemic physiology, which can greatly ... best practice recommendations (19,39), common data ...Read more

cris.maastrichtuniversity.nl
cris.maastrichtuniversity.nl
Performance comparison of systemic activity correction in ...


by F Klein · 2023 · Cited by 34 — Performance comparison of systemic activity correction in functional near-infrared spectroscopy for methods with and without short distance channels · Overview ...Read more

sites.bu.edu
sites.bu.edu
Publications | MindLights Lab


Short separation channel location impacts the performance of short channel regression in NIRS. NeuroImage, 59(3), 2518-2528. https://doi.org/10.1016/j ...Read more

nimrobotics.github.io
nimrobotics.github.io
Preprocessing functional Near Infrared Spectroscopy ...


28 Jun 2025 — This law relates the changes in optical density to the concentration changes of hemoglobin in the brain. Beer-Lambert Law. Beer-Lambert Law ...Read more

utsouthwestern.elsevierpure.com
utsouthwestern.elsevierpure.com
Modified beer-lambert law for blood flow


The modified Beer-Lambert law for flow accurately recovered these flow changes using only a single delay-time in the intensity auto-correlation function curve.Read more

springermedizin.de
springermedizin.de
Frequency-domain vs continuous-wave near-infrared ...


Therefore, the aim of this study was to compare the abilities of a continuous-wave (CW) NIRS device with a similarly clinically viable NIRS device utilising a ...Read more

academia.edu
academia.edu
Comment on the modified Beer–Lambert law for scattering ...


We present a concise overview of the modified Beer-Lambert law, which has been extensively used in the literature of near-infrared spectroscopy (NIRS) of ...

ui.adsabs.harvard.edu
ui.adsabs.harvard.edu
Modified Beer-Lambert law for blood flow


by WB Baker · 2015 · Cited by 387 — The modified Beer-Lambert law for flow accurately recovered these flow changes using only a single delay-time in the intensity auto-correlation function curve.Read more

europepmc.org
europepmc.org
Absolute quantification of cerebral tissue oxygen saturation ...


by Z Kovacsova · 2021 · Cited by 36 — Our aim is to improve the performance of oximetry through the development of a novel algorithm to calculate StO2 with continuous-wave (CW) NIRS ...Read more

Near-Infrared Spectroscopy (NIRS) of Muscle HbO 2 and ...


by EM Nemoto · 2021 · Cited by 6 — The aim of this study was to examine the relationship between muscle hemoglobin oxygen (HbO2) and myoglobin (MbO2) desaturation using NIRS combined with venous ...

lu.lv
lu.lv
Beer–Lambert law for optical tissue diagnostics


by I Oshina · 2021 · Cited by 367 — Significance: Beer–Lambert law (BLL) is a widely used tool for contact and remote determi- nation of absorber concentration in various media, ...Read more

opennirs.org
opennirs.org
I0 I ε, [C] d


To approach the widely used Modified-Beer Lambert Law (MBLL), the unmodified Beer-. Lambert Law (BLL) will be briefly introduced and then expanded.Read more

intechopen.com
intechopen.com
Monitoring Brain Activities Using fNIRS to Avoid Stroke


by YH Chen · 2022 · Cited by 4 — Beer-Lambert law defines the relationship between attenuation and the attenuating species' concentration and the optical path length [6]. For the near-infrared ...Read more

sm-hs.eu
sm-hs.eu
Near-infrared spectroscopy as an index of brain and tissue ...


This review provides a synopsis of the mode of operation, current limitations and confounders, clinical applications, and potential future uses of such NIRS ...Read more

clinicsearchonline.org
clinicsearchonline.org
Can near Infrared Spectroscopy Links Pharmacological ...


by F Crespi · 2025 · Cited by 1 — NIRS is indeed a non-ionizing technique that can be used to monitor oxygen saturation in the living tissue as well as changes in oxygenation of haemoglobin.

pure-oai.bham.ac.uk
pure-oai.bham.ac.uk
Functional near infrared spectroscopy using spatially resolved ...


by JD Veesa · 2019 · Cited by 19 — The typical method used is spa- tially resolved spectroscopy (SRS), which is shown to recover tissue oxygenation index (TOI) based on gradient of light.Read more

cdn.amegroups.cn
cdn.amegroups.cn
Comparing near-infrared spectroscopy—measured cerebral


by Y Ma · 2022 · Cited by 10 — In this study, we evaluated the evidence on the validity of NIRS and the interchangeability between NIRS and common invasive approaches by exploring the ...Read more

anaesthetics.ukzn.ac.za
anaesthetics.ukzn.ac.za
Near-Infrared Spectroscopy: Potential Clinical Benefits in ...


by SM Cohn · 2007 · Cited by 80 — In summary, NIRS technology facilitates continuous, noninvasive, and accurate monitoring of tissue oxygen saturation and can interrogate tissues by using light.Read more

aetna.com
aetna.com
Near-Infrared (NIR) Spectroscopy - Medical Clinical Policy ...


This Clinical Policy Bulletin addresses near-infrared (NIR) spectroscopy and near-infrared intravascular ultrasound.Read more

cureus.com
cureus.com
A Systematic Review and Meta-Analysis


by KM El-Atawi · 2023 · Cited by 3 — This systematic review and meta-analysis aimed to assess the utility of near-infrared spectroscopy (NIRS) in predicting the perinatal ...

iovs.arvojournals.org
iovs.arvojournals.org
Absolute Quantification of Oxygenated Hemoglobin within the ...


by MA McIntosh · 2010 · Cited by 69 — This study is the first to demonstrate absolute quantification of HbO and Hb concentrations in the visual cortex with functional changes in hemoglobin ...

upcommons.upc.edu
upcommons.upc.edu
“hDOS”: an automated hybrid diffuse optical device for real- ...


by M Zanoletti · 2025 — hDOS integrates time-domain near-infrared spectroscopy, diffuse correlation spectros- copy, and pulse oximetry to assess both tissue oxygenation and perfusion.Read more

youtube.com
youtube.com
Simplifying machine learning for fNIRS: implementation and ...


Johan will talk about some best practice on evaluating models and applying machine learning to F near.

lightning.ai
lightning.ai
BenchNIRS Workshop


27 Dec 2024 — Hands-on machine learning with fNIRS using the BenchNIRS Python framework.

frontiersin.figshare.com
frontiersin.figshare.com
Item - Data_Sheet_1_Benchmarking framework for machine ...


2 Mar 2023 — We present an open-source benchmarking framework, BenchNIRS, to establish a best practice machine learning methodology to evaluate models ...

neuroergonomicsconference.um.ifi.lmu.de
neuroergonomicsconference.um.ifi.lmu.de
Benchmarking Framework for Machine Learning with fNIRS


by J Benerradi — Our framework presents the machine learning fNIRS community with a challenge platform akin to other benchmarking datasets such as CIFAR-10 and MNIST (Krizhevsky ...

github.com
github.com
HanBnrd/BenchNIRS: Benchmarking framework for ...


A checklist of recommendations towards best practices for machine learning with fNIRS can be found here. We welcome contributions from the community in ...

Time-series-classification-1dCNN


It makes the 1D CNN a powerful tool for analyzing time-series data which has spatial characteristics only in one dimension. An external file that holds a ...Read more

wzhlearning/fNIRS-Transformer: Transformer-based ...


Transformer-based fNIRS Classification. Paper: Transformer Model for Functional Near-Infrared Spectroscopy Classification - wzhlearning/fNIRS-Transformer.

ul.qucosa.de
ul.qucosa.de
Effects of Different Hemoglobin Levels on Near-Infrared ...


by A Delis · 2023 · Cited by 15 — Abstract. Background: Near-infrared spectroscopy (NIRS) is a com- monly used technique to evaluate tissue oxygenation and.Read more

pure.qub.ac.uk
pure.qub.ac.uk
Physiologic determinants of near-infrared spectroscopy ...


by N Cody · 2024 · Cited by 10 — The purpose of this study was to assess the contribution of routinely measured physiologic parameters to tissue oxygen saturation measured by NIRS. DESIGN: An ...Read more

zora.uzh.ch
zora.uzh.ch
a powerful approach to study the embodied human brain - ZORA


Publication: Systemic physiology augmented functional near-infrared spectroscopy: a powerful approach to study the embodied human brain · Date · Citations.Read more

Systemic physiology augmented functional near-infrared ...


Significance: Functional near-infrared spectroscopy (fNIRS) enables measuring the brain activity of two subjects while they interact, i.e., ...Read more

Functional near-infrared spectroscopy short-channel ... - ZORA


by J An · 2025 · Cited by 1 — Functional near-infrared spectroscopy short-channel regression improves cortical activation estimates of working memory load ... Publisher DOI.Read more

Characterizing reproducibility of cerebral hemodynamic ...


Characterizing reproducibility of cerebral hemodynamic responses when applying short-channel regression in functional near-infrared spectroscopy ... (2022).Read more

A review on continuous wave functional near-infrared ...


by U Wolf · 2014 · Cited by 2467 — Such free post-processing tools can be used with most instruments. • Instruments D1, D2 and D17 can optionally measure tissue oxygen saturation ...Read more

boris-portal.unibe.ch
boris-portal.unibe.ch
Systemic physiology augmented functional near-infrared ...


by FV Scholkmann · 2022 · Cited by 97 — Systemic physiology augmented functional near-infrared spectroscopy: a powerful approach to study the embodied human brain.Read more

Systemic physiology augmented functional near-infrared ...


by S Guglielmini · 2022 · Cited by 27 — Brain and body activity was measured continuously by SPA-fNIRS. Results: Our study shows that making eye contact for a prolonged time causes significant changes ...Read more

Best practices for fNIRS publications


by MA Yücel · Cited by 651 — Some specifics of the fNIRS signal must be considered when designing the experimental para- digm. For example, the dominance of physiological confounds in fNIRS ...Read more

Characterizing reproducibility of cerebral hemodynamic ...


by DG Wyser · 2022 · Cited by 34 — Aim: We investigated the effect of short-channel regression (SCR) as an approach to obtain. fNIRS measurements with higher reproducibility on a ...Read more

facebook.com
facebook.com
Systemic physiology augmented functional near


19 Apr 2022 — Our new paper: Systemic physiology augmented functional near- infrared spectroscopy hyperscanning: a first evaluation investigating entrainment ...Read more

our outlook paper on SPA-fNIRS!


• an improved understanding of fNIRS signals, • to avoid erroneous interpretations of fNIRS signals and • to study the embodied brain · Ist ...Read more

Dear fNIRS Community I would like to recommend a ...


Dear fNIRS Community I would like to recommend a method that increases the spatial resolution of fNIRS by almost 3 times with just an ...

Our new paper: Characterizing reproducibility of cerebral ...


14 Mar 2022 — Our new paper: Characterizing reproducibility of cerebral hemodynamic responses when applying short-channel regression in functional near ...Read more

neuroinsight.net
neuroinsight.net
fNIRS NIRS Publications 2022 Neuroscience - NeuroInsight


Brain and body physiology between subjects NIRS fNIRS. Guglielmini, S., Bopp, G., Marcar, V. L., Scholkmann, F., & Wolf, M. (2022). Systemic physiology ...Read more

antoniahamilton.com
antoniahamilton.com
Non-invasive optical imaging of brain function with fNIRS


by P Pinfi · Cited by 13 — We conclude by discussing the open challenges that still need to be addressed as the field moves toward more naturalistic investigations of brain functioning.Read more

d-nb.info
d-nb.info
Reconstructing damaged fNIRS signals with a generative ...


by Y Zhi · 2025 · Cited by 7 — Here, we pro- posed a generative deep learning approach to recover damaged fNIRS signals in one or more measurement channels. The model captured ...Read more

scispace.com
scispace.com
Transformer Model for Functional Near-Infrared ...


31 May 2022 — TL;DR: In this article , the authors proposed an end-to-end network based on Transformer for functional near-infrared spectroscopy (fNIRS) ...Read more

measuring-tissue-hemodynamics-and-oxygenation-by- ...


1 Apr 2014 — Measuring tissue hemodynamics and oxygenation by continuous-wave functional near-infrared spectroscopy— how robust are the different calculation.Read more

peerj.com
peerj.com
Technology investigation on time series classification and ...


by Y Tong · 2022 · Cited by 38 — Time series appear in many scientific fields and are an important type of data. The use of time series analysis techniques is an essential ...

dl.acm.org
dl.acm.org
Procedural Skill Assessment Using Raw fNIRS Signals


by A Subedi — The model processes raw fNIRS time-series data, where each trial is represented as a sequence of measurements across multiple fNIRS channels. In the first, ...Read more

Pain Assessment Using Multi-Kernel-FCN-LSTM and ...


13 Oct 2025 — The study involved different fNIRS haemoglobin measures, including HbO2, HHb, HT and HbDiff, evaluated using DL and ML algorithms. We performed ...Read more

Exploring Machine Learning Approaches for Classifying ...


This paper explores different approaches and configurations for classifying Mental Workload (MWL) from a continuous HCI task, to identify and understand ...Read more

Hybrid Deep Learning Model to Estimate Cognitive Effort ...


by S Sharmin · 2025 · Cited by 3 — This study estimates cognitive effort based on functional near-infrared spectroscopy data and performance scores using a hybrid DeepNet ...

Hybrid Deep Learning Model to Estimate Cognitive Effort ...


by S Sharmin · 2025 · Cited by 3 — This study estimates cognitive effort based on functional near-infrared spectroscopy data and performance scores using a hybrid DeepNet ...Read more

Hybrid Deep Learning Model to Estimate Cognitive Effort ...


by S Sharmin · 2025 · Cited by 3 — ACM Reference Format: Shayla Sharmin and Roghayeh Leila Barmaki. 2025. Hybrid Deep Learn- ing Model to Estimate Cognitive Effort from fNIRS ...Read more

germain-forestier.info
germain-forestier.info
Deep Learning For Time Series Classification Using New ...


by A Ismail-Fawaz · 2022 · Cited by 69 — In this field, state-of-the-art architectures rely on convolution neural networks that learn one dimensional filters in order to capture patterns allowing to ...Read more

journals.plos.org
journals.plos.org
Improved performance of fNIRS-BCI by stacking of deep ...


by J Akhter · 2025 · Cited by 3 — fNIRS' ability to track changes in concentration of oxy and deoxy hemoglobin signal, has a comparatively improved temporal resolution as ...Read more

academic.oup.com
academic.oup.com
658 Analysis of cerebral blood volume and flow changes in ...


by BS Park · 2024 — This study investigated cerebral blood volume (CBV) and cerebral blood flow (CBF) during hemodialysis using functional near-infrared ...Read more

royalsocietypublishing.org
royalsocietypublishing.org
From lab to life: challenges and perspectives of fNIRS for ...


by F Klein · 2024 · Cited by 49 — This review is aimed at researchers from different fields who seek to exploit the unique capabilities of fNIRS for neurofeedback. It carefully ...Read more

medscimonit.com
medscimonit.com
Functional Near-Infrared Spectroscopy in Schizophrenia ...


2 Sept 2025 — ABSTRACT:This review comprehensively examines the application and progress of functional near-infrared spectroscopy (fNIRS) in schizophrenia ...

journals.sagepub.com
journals.sagepub.com
Utility of Functional Near-infrared Spectroscopy (fNIRS) in ...


by S Karna — This review aims to systematically examine: (a) the utility of fNIRS in distinguishing individuals with depression from healthy individuals; (b) ...Read more

granthbrennermd.medium.com
granthbrennermd.medium.com
The Brain-Mind Gap: How fNIRS Technology Could Bridge ...


Research demonstrates that fNIRS can detect treatment response patterns before symptomatic improvement becomes apparent. A systematic review of ...Read more

clinical-practice-and-epidemiology-in-mental-health.com
clinical-practice-and-epidemiology-in-mental-health.com
Machine Learning Techniques to Predict ...


by U Madububambachu · 2024 · Cited by 107 — Fried et al. introduced the possibility of using Deep Learning (DL) methods not only to predict and diagnose specific mental health disorders ...Read more

ouci.dntb.gov.ua
ouci.dntb.gov.ua
CGAN-rIRN: a data-augmented deep learning approach to ...


The proposed fully data-driven hybrid deep learning approach paves a promising way to improve the classification performance of volitional control fNIRS-BCI.Read more

Hybrid Deep Learning Model to Estimate Cognitive Effort ...


Publication type. Proceedings Article ; DOI. 10.1145/3747327.3764901 ; Journal. 2025, Companion Proceedings of the 27th International Conference on Multimodal ...Read more

nottingham-repository.worktribe.com
nottingham-repository.worktribe.com
Exploring Machine Learning Approaches for Classifying ...


Functional Near-Infrared Spectroscopy (fNIRS) has shown promise for being potentially more suitable (than e.g. EEG) for brain-based Human Computer Interact.

Benchmarking framework for machine learning classification ...


Methods: We present an open-source benchmarking framework, BenchNIRS, to establish a best practice machine learning methodology to evaluate models applied to ...Read more

habcentral.habcommunity.com
habcentral.habcommunity.com
Can fNIRS and Machine Learning Revolutionize ...


29 Dec 2025 — fNIRS-based machine learning reliably differentiates UD, BD, and HC at the group level. Whole-brain integration yields superior performance, ...Read more

techrxiv.org
techrxiv.org
Calibration of Deep Learning Classification Models in fNIRS


Through this letter, we hope to emphasize the critical role of calibration in fNIRS research and argue for enhancing the reliability of deep learning-based ...Read more

themoonlight.io
themoonlight.io
[Papierüberprüfung] Calibration of Deep Learning ...


This paper investigates the calibration of deep learning models used for classifying functional near-infrared spectroscopy (fNIRS) data.

spj.science.org
spj.science.org
Cross-Subject Emotion Recognition Brain–Computer ...


by X Si · 2023 · Cited by 66 — Table 3 shows the leave-one-out-subject cross-validation results for all methods on our fNIRS dataset. Our proposed method outperforms these models by about 16% ...Read more

cs.tufts.edu
cs.tufts.edu
Taming fNIRS-based BCI Input for Better Calibration and ...


They report average classifcation accuracy of over 70% on distinguishing mental arithmetic versus idle state, outperforming alternative pipelines including ...Read more

journals.infinite-science.de
journals.infinite-science.de
On the impact of feature reduction on leave- one-subject- ...


by MP Pauli · 2023 · Cited by 1 — The results show that the mean classification accuracies at validation sets have been found to be 90.8±0.8% for the standard CV and 86.4± 11.0% for the LOSO-CV.Read more

mednexus.org
mednexus.org
Improvement of classification accuracy of functional near- ...


by O Asadi · 2025 · Cited by 6 — This study aimed to address this challenge by employing the common spatial pattern (CSP) algorithm to reduce input dimensions for support vector machine (SVM)

linkedin.com
linkedin.com
Deep Learning for fNIRS and EEG Signal Classification


F-M FACS 6.0 marks a decisive epistemological shift beyond classical models by systematically linking facial expression, neural activation, and ...Read more

ayazlab.com
ayazlab.com
Publications


Exploring social impairment in those with opioid use disorder: linking impulsivity, childhood trauma, and the prefrontal cortex.

ruizlab.org
ruizlab.org
Deep Learning Forecast of Cognitive Workload Using ...


fNIRS neuroimaging was used to collect high-resolution neurophysiological data for exploring and forecasting cognitive workload using a collection of deep ...Read more

scholar.google.com
scholar.google.com
Sajila Wickramaratne


A deep learning based ternary task classification system using gramian angular summation field in fNIRS neuroimaging data. SD Wickramaratne, MS Mahmud. 2020 ...Read more

Franziska Klein


Optimizing spatial specificity and signal quality in fNIRS: an overview of potential challenges and possible options for improving the reliability of real-time ...Read more

digitalcommons.wustl.edu
digitalcommons.wustl.edu
"Best practices for fNIRS publications" by Meryem A. Yücel, ...


by MA Yücel · 2021 · Cited by 684 — Best practices for fNIRS publications ; Document Type. Open Access Publication ; DOI. 10.1117/1.NPh.8.1.012101 ; Rights and Permissions. Meryem A. Yücel, Alexander ...

publications.polymtl.ca
publications.polymtl.ca
Best practices for fNIRS publications - PolyPublie


by MA Yücel · 2021 · Cited by 684 — (2021). Best practices for fNIRS publications. Neurophotonics, 8(1), 012101 (34 pages). https://doi.org/10.1117/1.nph.8.1.012101. APA 7 (HTML) ...

gitlab.com
gitlab.com
BenchNIRS - Johann Benerradi


Project information: Benchmarking framework for machine learning with fNIRS. https://doi.org/10.3389/fnrgo.2023.994969Read more

fnirs2024.fnirs.org
fnirs2024.fnirs.org
Posters – Sunday 15th


Su-038, Optimizing spatial specificity and signal quality in fNIRS: An overview of potential challenges and possible options for improving reliability in real- ...

jiahuian.com
jiahuian.com
fNIRS Biomarkers of Mental Workload | Jiahui An


... short-channel regression improves cortical activation estimates of working memory load. An, J., Schönhammer, J., Luft, A., et al. Neurophotonics, 2025. DOI ...Read more

visualize.jove.com
visualize.jove.com
Functional near-infrared spectroscopy short-channel ...


3 Dec 2020 — Short-channel regression (SCR) improves functional near-infrared spectroscopy (fNIRS) measurements for working memory (WM) tasks.Read more

zenodo.org
zenodo.org
Robustness of tissue oxygenation estimates by continuous ...


18 Feb 2025 — ... Robustness of tissue oxygenation estimates by continuous wave space-resolved near infrared spectroscopy" ... DOI Badge. DOI. 10.5281/zenodo ...Read more

vascovid.eu
vascovid.eu
PUBLICATIONS


Robustness of tissue oxygenation estimates by continuous wave space-resolved near infrared spectroscopy. Journal of Biomedical Optics. 17.07.2023.Read more

scienceon.kisti.re.kr
scienceon.kisti.re.kr
[논문]Robustness of tissue oxygenation estimates by ...


Robustness of tissue oxygenation estimates by continuous wave space-resolved near infrared spectroscopy 원문보기. Journal of biomedical optics, v.28 no.7 ...Read more

nih.gov
nih.gov
A Quantitative Comparison of Overlapping and Non ... - PMC


by A Dehghani · 2019 · Cited by 199 — In this paper, we analyze the impact of overlapping sliding windows on the performance of Human Activity Recognition systems with different evaluation ...Read mor...

jihyuncindyhur.github.io
jihyuncindyhur.github.io
Mapping fNIRS to fMRI with Neural Data Augmentation and ...


by J Hur · 2020 · Cited by 5 — To utilize data augmentation and machine learning to build such model. To improve the plausibility of fNIRS as a potential surrogate of fMRI.Read more

ethz.ch
ethz.ch
DL-QC-fNIRS: a deep learning tool for automated quality control ...


Significance: In functional near-infrared spectroscopy (fNIRS) research, ensuring signal quality is a critical preprocessing step.

pw.edu.pl
pw.edu.pl
Machine learning-based filtering system for fNIRS signals ...


by M PELC · 2025 — Abstract. This paper presents a preliminary study delving into the application of machine learning-based methods for optimizing parameter.Read more

uzh.ch
uzh.ch
Characterizing reproducibility of cerebral hemodynamic ...


by DG Wyser · 2022 · Cited by 34 — Aim: We investigated the effect of short-channel regression (SCR) as an approach to obtain. fNIRS measurements with higher reproducibility on a ...Read more

Best practices for fNIRS publications


by MA Yücel · 2021 · Cited by 684 — analysis of fNIRS data.84 Previous work proved that short-separation regression decreases the trial-to-trial variability of the hemodynamic response85 and ...Read m...

wiley.com
wiley.com
Changes in transcranial near‐infrared spectroscopy (NIRS) ...


by KM Lanning · 2023 · Cited by 7 — NIRS is a noninvasive, continuous and validated method to measure variation in regional cerebral oxygen saturation (rSO2). Transcranial NIRS utilizes self- ...Read...

Motor Imagery Classification Using fNIRS Brain Signals: A ...


21 Mar 2025 — We then employed sliding window technology [30] to extract local features from each channel and capture the temporal dynamics of the signal.Read more

inspirehep.net
inspirehep.net
Functional near-infrared spectroscopy for the detection of ...


by JL Gómez-Sirvent · 2025 — This section reviews previous studies on QML for brain signal processing and classical machine learning methods in the context of fNIRS signal analysis. QML for ...Read mo...

elsevierpure.com
elsevierpure.com
Data leakage in deep learning studies of translational EEG


by G Brookshire · 2024 · Cited by 71 — A growing number of studies apply deep neural networks (DNNs) to recordings of human electroencephalography (EEG) to identify a range of disorders.Read more

Connector sources scanned

No connector sources scanned

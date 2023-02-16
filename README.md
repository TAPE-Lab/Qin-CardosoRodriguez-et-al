[![DATA](https://zenodo.org/badge/DOI/10.5281/zenodo.7586958.svg)](https://doi.org/10.5281/zenodo.7586958)

# A Single-cell Perturbation Landscape of Colonic Stem Cell Polarisation

This repository contains Python and R scripts used to generate the figures presented in Qin & Cardoso Rodriguez et. al., _A Functional Single-cell Landscape of Colonic Stem Cell Polarisation_ (DOI to be updated).

Subsampled versions of some objects are already provided within this repository to facilitate running the notebooks. Otherwise, full datasets exceeding GitHub's file size limit are generally archived in [Zenodo](), with some available upon request.

## Overview

An overview of all the samples generated in this study can be found at: <https://github.com/TAPE-Lab/Qin-CardosoRodriguez-et-al/blob/main/Metadata/ExperimentalConditions.ipynb>, while the folders in this repository are organised by figures. 

More specifically:

- `/Figure1_S1-S2` - scRNA-seq - data integration, cell-type-specific analysis, and epithelia focus analysis (incl. clustering, gene signature analysis, differential abundance analysis, entropy analysis, and RNA velocity analysis)
    - `IntegrationDR_epifibmac.ipynb`: Figure 1B.
    - `emdPCA_DE_Epithelia.ipynb`: Figure 1C, Figure S1B.
    - `emdPCA_DE_Fibroblasts.ipynb`: Figure 1C, Figure S1C.
    - `emdPCA_DE_Mcrophages.ipynb`: Figure 1C, Figure S1D.
    - `Main_INTepi.ipynb`: Figure 1D-I, Figure S2B-E.
    - `Velocity.ipynb`: Figure 1E, Figure S2D.
    - `Signatures.ipynb`: Figure S2A.

- `/Figure2_3-S3_S4` - Mass cytometry (MC) - 'WENR Permutation'.
    - Notebooks split by experiment.
        - `/WENR Permutation`: Figures 2 & 3, S3 & S4
        - `/WNT-EGF Competition`: Figure S4C-F.

- `/Figure4-S5` - scRNA-seq & MC - cell-cell communication analysis, i.e., CellChat analysis & 'CellChat Follow-up'.
    - Notebooks split by experiment.
        - `CCommunications.ipynb`: scRNA-seq analysis for Figure 4A, Figure 4B, Figure S5A-C.
        - `/CellChat Follow-up`: MC analysis for Figure 4D, Figure S5D-F.

- `/Figure5-S6` - MC - Cue-signal-response array, i.e., 'Signal Perturbation'.
    - Notebooks for Figure 5 and Figure S5.

- `/Figure6-S7` - Single-cell valley-ridge (VR) landscape.

## Data Availability

- Raw scRNA-seq data and BioSample metadata have been deposited at Sequence Read Archive (SRA) (<https://www.ncbi.nlm.nih.gov/bioproject/PRJNA883610>).
- Raw and processed MC data are available as a Community Cytobank project(<https://community.cytobank.org/cytobank/experiments#project-id=1460>).
- Aligned scRNA-seq count matrices, spliced/unspliced RNA count matrices, integrated Seurat objects, integrated MC dataframes, and
  Houdini project files can be accessed at Zenodo (<https://doi.org/10.5281/zenodo.7586958>).

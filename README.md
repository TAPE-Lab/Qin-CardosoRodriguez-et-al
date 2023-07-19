[![bioRxiv:10.1101/2023.02.15.528008](https://img.shields.io/badge/bioRxiv-10.1101%2F2023.02.15.528008-B31B1B.svg)](https://doi.org/10.1101/2023.02.15.528008) <!-- B31B1B is the colour for bioRxiv -->
[![zenodo:10.5281/zenodo.7586958](https://img.shields.io/badge/Zenodo-10.5281%2Fzenodo.7586957-4B81BE.svg)](https://doi.org/10.5281/zenodo.7586957) <!-- 4B81BE is the colour for Zenodo -->

# A Single-cell Perturbation Landscape of Colonic Stem Cell Polarisation

This repository contains Python and R scripts used to generate the figures presented in Qin & Cardoso Rodriguez et. al., [_A Functional Single-cell Landscape of Colonic Stem Cell Polarisation_](https://doi.org/10.1101/2023.02.15.528008).

Subsampled versions of some objects are already provided within this repository to facilitate running the notebooks. Otherwise, full datasets exceeding GitHub's file size limit are generally archived in [Zenodo](https://doi.org/10.5281/zenodo.7586958), with some available upon request.

## Overview

An overview of all the samples generated in this study can be found [here](https://github.com/TAPE-Lab/Qin-CardosoRodriguez-et-al/blob/main/Metadata/ExperimentalConditions.ipynb), while the folders in this repository are organised by figures.

More specifically:

- `/Figure1_S1` - scRNA-seq - data integration, cell-type-specific analysis, and epithelia focus analysis (incl. clustering, gene signature analysis, differential abundance analysis, entropy analysis, and RNA velocity analysis)
  - `IntegrationDR_epifibmac.ipynb`: Figure 1B.
  - `emdPCA_DE_Epithelia.ipynb`: Figure 1C, Figure S1B.
  - `emdPCA_DE_Fibroblasts.ipynb`: Figure 1C, Figure S1C.
  - `emdPCA_DE_Mcrophages.ipynb`: Figure 1C, Figure S1D.
  - `Main_INTepi.ipynb`: Figure 1D-I, Figure S2E.
  - `Velocity.ipynb`: Figure 1E, Figure S1H-I.
  - `fib-signatures.ipynb`: Figure S1B.
  - `cellchat_cd34-focus.ipynb`: Figure S1C.

- `/Figure2_S2` - scRNA-seq - gene signature correlation analysis and integrative analysis with published human data.
  - `Signatures.ipynb`: Figure 2.
  - X: Figure S2A.
  - `CMS.ipynb`: Figure S2C-D.
  - X: Figure S2E-F.

- `/Figure3-4_S3-S4` - Mass cytometry (MC) - 'WENR Permutation'.
  - Notebooks split by experiment.
    - `/WENR Permutation`: Figures 3 & 4, S3 & S4
    - `/WNT-EGF Competition`: Figure S4C-F.
    - `/Ligand Time-course`: Figure S4H-I.

- `/Figure5_S5` - scRNA-seq & MC - cell-cell communication analysis, i.e., CellChat analysis & 'CellChat Follow-up'.
  - Notebooks split by experiment.
    - `CCommunications.ipynb`: scRNA-seq analysis for Figure 5A, Figure 5B, Figure S5A-C, Figure S4G.
    - `CMS_CellChat.ipynb`: Figure S5D.
    - `/CellChat Follow-up`: MC analysis for Figure 5D, Figure S5D-H.

- `/Figure6_S6` - MC - Cue-signal-response array, i.e., 'Signal Perturbation'.
  - Notebooks for Figure 6 and Figure S6.

- `/Figure7_S7` - Single-cell valley-ridge (VR) landscape.

## Data Availability

- Raw scRNA-seq data and BioSample metadata have been deposited at [Sequence Read Archive (SRA)](https://www.ncbi.nlm.nih.gov/bioproject/PRJNA883610).
- Raw and processed MC data are available as a [Community Cytobank project](https://community.cytobank.org/cytobank/experiments#project-id=1460).
- Aligned scRNA-seq count matrices, spliced/unspliced RNA count matrices, integrated Seurat objects, integrated MC dataframes, and
  Houdini project files can be accessed at [Zenodo](https://doi.org/10.5281/zenodo.7586957).

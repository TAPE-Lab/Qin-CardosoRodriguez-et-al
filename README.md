# A Functional Single-cell Landscape of Colonic Stem Cell Polarisation

[WORK IN PROGRESS]

This repository contains Python and R scripts used to generate the figures presented in Qin & Cardoso Rodriguez et. al., _A Functional Single-cell Landscape of Colonic Stem Cell Polarisation_ (DOI to be updated).

# Overview

An overview of all the samples generated in this study can be found at: <https://github.com/TAPE-Lab/Qin-CardosoRodriguez-et-al/blob/main/Metadata/ExperimentalConditions.html>, while the folders in this repository are organised by figures. More specifically:

- `/Figure1-S1` - scRNA-seq - data integration and cell-type-specific analysis.

  - Notebooks split by cell-types.
    - `Epithelia.ipynb`: Figure 1C, Figure S1B.
    - `Fibroblasts.ipynb`: Figure 1C, Figure S1C.
    - `Macrophages.ipynb`: Figure 1C, Figure S1D.
    - `IntegrationDR.ipynb`: Figure 1B.
  - TODO (FC): a note book for data preprocessing and integration?

- `/Figure2-S2` - scRNA-seq - epithelia focus analysis (incl. clustering, gene signature analysis, differential abundance analysis, entropy analysis, and RNA velocity analysis).

  - Notebooks split by analysis.
    - `IntegrationDR.ipynb`: Figure 2A, Figure S2B(?).
    - `Entropy.ipynb`: Figure 2B.
    - `DA.ipynb`: Figure 2C-E.
    - `ClustersDE.ipynb`: Figure 2F.
    - `Signatures.ipynb`: Figure S2A.
    - `Velocity.ipynb`: Figure S2C, S2D.
    - TODO (FC): could you please double-check and make sure my references to the figures are correct? Thanks.

- `/Figure3_4-S3_S4` - Mass cytometry (MC) - 'WENR Permutation'.

  - Notebooks split by experiment.
    - `/WENR Permutation`: Figures 3 & 4, S3 & S4
    - `/WNT-EGF Competition`: Figure S4C-F.

- `/Figure5-S5` - scRNA-seq & MC - cell-cell communication analysis, i.e., CellChat analysis & 'CellChat Follow-up'.

  - Notebooks split by experiment.
    - `CCommunications.ipynb`: scRNA-seq analysis for Figure 5A, Figure 5B, Figure S5A-C.
    - `/CellChat Follow-up`: MC analysis for Figure 5D, Figure S5D-F.

- `/Figure6-S6` - MC - Cue-signal-response array, i.e., 'Signal Perturbation'.

  - Notebooks for Figure 6 and Figure S6.

- `/Figure7` - Single-cell valley-ridge (VR) landscape.

# Data Availability

- Raw scRNA-seq data has been deposited in the sequence read archive (SRA) under the accession PRJNA883610.
- The integrated Seurat object of the scRNA-seq experiment, the integrated dataframes for MC analysis, and the Houdini project files can be accessed at Zenodo (<https://doi.org/10.5281/zenodo.7586958>).
- Raw and processed MC data and illustrations are available as a Community Cytobank project (<https://community.cytobank.org/cytobank/experiments\#\linebreak> project-id=1460).

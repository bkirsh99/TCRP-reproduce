### Bianca Kirsh | 1003756893 | Winter 2023

### MBP 1413H - Biomedical Applications of Artificial Intelligence
# *Full Reproducibility of Computational Research: Myth or Reality?* 

This project aims to reproduce the study [Few-shot learning creates predictive models of drug response that translate from high-throughput screens to individual patients (*Nat Cancer* 2021)](https://www.nature.com/articles/s43018-020-00169-2#data-availability), which describes a transfer learning algorithm for drug response predictions in cancer.

The authors' original codebase can be accessed [here](https://github.com/idekerlab/TCRP/) and the refactored codebase can be accessed [here](https://github.com/shfong/tcrp-reproduce).

This codebase contains the instructions, data, and code required to reproduce and replicate the figures from **Challenge 1** of the original study, which investigated the transfer of CRISPR (1a) and drug (1b) response models for prediction in the context of a new tissue.

## Table of Contents
1. [Directory Structure](#2-directory-structure)
2. [Datasets Documentation](#3-datasets-documentation)
3. [Step-by-Step Running Guide](#5-step-by-step-running-guide)

     3.1. [Overview](#31-overview)
     
     3.2. [Installation Instructions](#32-installation-instructions)
     
     3.3. [Data Preprocessing](#33-installation-instructions)
     
     3.4. [Model Building](#34-model-building)
     
     3.5. [Performace Assessment](#35-performance-assessment)
     
6. [Sample Run](#6-sample-run)

## 1. Directory Structure

```
.
├── tcrp_model
│   ├── data
|   |   ├── input
|   |   ├── output
|   |   |   ├── cell_line_lists
|   |   |   ├── drug_feature
|   |   |   └── runs
|   |   ├── fewshot_data
|   |   └── results
|   ├── pipelines
│   │   ├── data_preparation
│   │   ├── model
│   │   └── baselines
│   ├── model_comparisons
|   └── sample
├── requirements.txt
└── README.md

```

## 2. Datasets Documentation
All datasets required to reproduce this study are contained within the *./tcrp_model/data/input.* The exact link to each input file is provided as a commented-out line of code in the preprocessing Jupyter Notebooks in *./tcrp_model/pipelines/data_preparation.*

| Dataset | Source | Description | Version | Download Link |
| ----------- | ----------- | ----------- | ----------- | ----------- |
CRISPR screening | DepMap | High-throughput CRISPR screening of ~17,700 gene disruptions across 341 cancer cell lines | Achilles Avana Public 17Q4 v2 |[link](https://depmap.org/portal/download/all/?releasename=Achilles+Avana+Public+17Q4+v2) |
Drug sensitivity | GDSC1000 | High-throughput drug screening of 255 anti-cancer drugs across 1,001 cancer cell lines| GDSC1 |[link](https://www.cancerrxgene.org/downloads/bulk_download)|
Expression features|CCLE||||

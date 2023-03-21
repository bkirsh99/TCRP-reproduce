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

| Directory | Contents |
| ----------- | ----------- |
| *data* | Folder containing input datasets |
*data_preparation* | Folder containing raw input datasets and preprocessing script for generating feature and label files|
| *model* | Folder containing scripts for neural network training and prediction|
| *pipelines* | Folder containing scripts for creating and submitting slurm jobs|
| *model_comparisons*| Scripts for analyzing the performance of different models (baseline, linear, KNN, RF)|
|*example_data*| Example training and testing data for the drug Sorafenib as an example

## 2. Datasets Documentation
All datasets required to reproduce this study are contained within *data/inputs.* They were sourced from [ORCESTRA](https://www.orcestra.ca), an online platform for orchestrating and reproducing multimodal pharmacogenomic data, where they were reprocessed and re-annotated by the [Haibe-Kains Lab](https://bhklab.ca) to maximize overlap with other pharmacogenomic datasets.

| Dataset | Source | Description | Version | Publication | Download Link | File Name in *data_preparation/* |
| ----------- | ----------- | ----------- | ----------- | ----------- | ----------- | ----------- |
CRISPR screening | DepMap | CERES-corrected CRISPR gene disruption scores |?| | ?|
Drug sensitivity | GDSC1000 | Area under the dose–response curve (AUC) scores across all the screened compounds and cell lines||[link](https://www.cancerrxgene.org/gdsc1000/GDSC1000_WebResources//Data/suppData/TableS4B.xlsx)||

## 3. Step-by-Step Running Guide

### 3.1. Overview

Once the input features are generated, we will build our translation of cellular response prediction (TCRP) model as well as a collection of baseline learning models to predict the growth responses of cell lines. The baseline models will be trained by conventional learning approaches, including Random Forest (RF), Neural Network (NN), K-Nearest Neighbors (KNN), and Linear Regression (LR). The TCRP model will be trained by a two-phase design as depicted below:

<img src="images/Figure1_github-01.png" alt="Model overview" width="60%"/>

### 3.1. Installation Instructions

Execute this to install all the dependencies:

```pip install -r requirements.txt```
Once the raw datasets are downloaded, task-specific features and labels on which subsequent steps are dependent must be generated using the jupyter notebook *data_preparation/process_sanger_drug_cell_line.ipynb*.


**Step 1.** Edit the following variables in data_preparation/process_sanger_drug_cell_line.ipynb:

- data_dir: Absolute path to input data directory  
- exp_data_file: Absolute path to input data directory  
- mutation_data_file = data_dir + 'OmicsSomaticMutations.csv'
- cell_line_detail_file: Absolute path to
drug_target_file = data_dir + 'drug_target_list.txt'


### 4.1. Overview
**Step 1.** 

**Step 2.** Edit the following variables in *pipelines/prepare_complete_run.py*:
- run_mode: Choose between "tcrp" or "baseline"
- run_name: Specify a name for your run (e.g., "yymmdd_drug-baseline-models")
- 


```
usage: generate_MAML_job_cv.py [--run_name RUN_NAME] [--drug_list_file DRUG_LIST_FILE] [--job_id JOB_ID] [--job JOB]
                
```


------

It trains the few-shot model for a fixed number of episodes, with periodic evalution on the validation set, followed by testing on the test set.

Note that all the results reported are based on training for a fixed number of epochs, and then evaluating using the best model found using the validation set.

Please see utils/io_utils.py for all the arguments and their default values. Here are some sufficient examples:

python train.py --help will print the help for all the necessary arguments:

1. Phase I: Pretraining
In the ‘pretraining’ phase, the model is exposed to a variety of different predefined contexts, each of which is represented by numerous training samples.


### 4.2. Phase II: Few-shot Learning
In the ‘few-shot learning’ phase, the model is presented with a new context not seen previously, and further learning is performed on a small number of new samples. 

Please prepare the feature and label files for the target domain in the same folder used for pre-training. Use the option ‘-feature_dic’ to specify the name of the folder. These names can be changed in the ‘load_data’ and ‘load_data_PDTC’ functions in the util.py file. 

## 5. Sample Run

An example file, ‘Sorafenib_tissue_map.pkl’, is included in the *data/* folder. Please use option ‘-tissue_list’ to specify the file to use.
Please also prepare a ‘task list’ file to store the detailed information of each sub-task in the pre-training phase. It is a Python dictionary stored in a pickle file. The key of that dictionary is the name of the sub-task, which should be the same as the feature and label file. For example, if the sub-task is called ‘lung’, then the corresponding feature and label files should be ‘lung_Sorafenib_feature.npy’ and ‘large_Sorafenib_label.npy’, respectively. 

## 6. Model Comparisons 


## Instructions
### 1) Data Gathering
- **CRISPR gene disruption labels:** CERES-corrected single-gene disruption scores from DepMap (https://depmap.org/portal). 
- **Drug response labels:** Area under the dose-response curve (AUCs) values for all screened cell-line/drug combinations from the GDSC1000 website (https://www.cancerrxgene.org/gdsc1000/GDSC1000_WebResources//Data/suppData/TableS4B.xlsx).
- **Protein–protein interaction (PPI)  data:** Union of PathwayCommons (https://www.pathwaycommons.org/archives/PC2/v11/PathwayCommons11.All.hgnc.txt.gz) and CORUM databases
-**Drug target and pathway information:** Table S1G from the original GDSC1000 paper (https://www.cell.com/cms/10.1016/j.cell.2016.06.017/attachment/3e295c33-119c-44d7-bbf6-90bfa3c62af7/mmc2)
1) Download data from DepMap (https://depmap.org/portal/download/all/):
- Achilles Avana Public 17Q4 v2 All Files
2) Generate the transformed data with data_preparation/process_sanger_drug_cell_line.ipynb. This notebook will generate a series of pickled files and numpy compressed files that the following steps will be dependent on.

### 2) Data Preparation


### 3) Pre-Training

For the pre-training phase, please prepare the feature and label files for each task in the same folder. For the few-shot learning phase, please prepare the feature and label files for the target domain in the same folder used for pre-training. Use the option ‘-feature_dic’ to specify the name of the folder. These names can be changed in the ‘load_data’ and ‘load_data_PDTC’ functions in the util.py file. An example file, ‘Sorafenib_tissue_map.pkl’, is included in the data/ folder. Please use option ‘-tissue_list’ to specify the file to use.
Please also prepare a ‘task list’ file to store the detailed information of each sub-task in the pre-training phase. It is a Python dictionary stored in a pickle file. The key of that dictionary is the name of the sub-task, which should be the same as the feature and label file. For example, if the sub-task is called ‘lung’, then the corresponding feature and label files should be ‘lung_Sorafenib_feature.npy’ and ‘large_Sorafenib_label.npy’, respectively. 

## References

Ma J, Fong SH, Luo Y., Bakkenist CJ, Shen JP, Mourragui S, Wessels LFA, Hafner M, Sharan R, Peng J, Ideker T.  Few-shot learning creates predictive models of drug response that translate from high-throughput screens to individual patients. Nat Cancer. 2021 Feb;2(2):233-244. doi: 10.1038/s43018-020-00169-2. Epub 2021 Jan 25. PMID: 34223192 [Pubmed](https://pubmed.ncbi.nlm.nih.gov/34223192/)




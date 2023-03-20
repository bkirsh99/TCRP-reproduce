### Bianca Kirsh | 1003756893 | Winter 2023

### MBP 1413H - Biomedical Applications of Artificial Intelligence
# *Full Reproducibility of Computational Research: Myth or Reality?* 

This project aims to reproduce the study [Few-shot learning creates predictive models of drug response that translate from high-throughput screens to individual patients (*Nat Cancer* 2021)](https://www.nature.com/articles/s43018-020-00169-2#data-availability), which describes a transfer learning algorithm for drug response predictions in cancer.

The authors' original codebase can be accessed [here](https://github.com/idekerlab/TCRP/) and the refactored codebase can be accessed [here](https://github.com/shfong/tcrp-reproduce). This codebase contains the instructions, data, and code required to reproduce **challenge 1** of the original study (transfer of CRISPR and drug response models for prediction in the context of a new tissue).

## Table of contents
1. [Installation Instructions](#-1-installation-instructions)
2. [Directory Structure](#2-directory-structure)
3. [Data Gathering](#3-data-gathering)
4. [Data Preprocessing](#4-data-preprocessing)
5. [Running Instructions](#5-general-running-instructions)     

     5.1. [Phase I: Pretraining](#51-phase-i:-pretraining)
     
     5.2. [Phase II: Fewshot Learning](#52-phase-ii:-fewshot-learning)
     
6. [Sample Run](#6-sample-run)
7. [Model Comparisons](#7-model-comparisons)

## 1. Installation Instructions

Execute this to install all the dependencies:

```pip install -r requirements.txt```

## 2. Directory Structure

| Directory | Contents |
| ----------- | ----------- |
| *data_preparation* | Script to preprocess datasets for generating feature and label files|
| *model* | Scripts for neural network training and prediction|
| *pipelines* | Scripts for implementing multiple steps of model building|
| *model_comparisons*| Scripts for analyzing the performance of different models (baseline, linear, KNN, RF)|
|*example_data*| Example training and testing data for the drug Sorafenib as an example

## 3. Data Gathering

The datasets and original download links are listed below, alongside the path to the file location in :

| Dataset | Download Link | Release Version | Location|
| ----------- | ----------- | ----------- | ----------- |
| CERES-corrected CRISPR gene disruption scores | https://depmap.org/portal  | ?| |
| GDSC1000 AUC values|https://www.cancerrxgene.org/gdsc1000/GDSC1000_WebResources//Data/suppData/TableS4B.xlsx| `filelists/flowers/images`      | |
|| https://www.kaggle.com/hassiahk/stanford-cars-dataset-full | `filelists/cars/images`         | |
| Stanford Dogs    | https://www.kaggle.com/jessicali9530/stanford-dogs-dataset | `filelists/dogs/images`         | |
| FGVC - Aircrafts | https://www.kaggle.com/seryouxblaster764/fgvc-aircraft     | `filelists/aircrafts/images`    | |
| MiniImageNet     | https://www.kaggle.com/arjunashok33/miniimagenet           | `filelists/miniImagenet/images` | |

## 3. Data Preprocessing
Once the raw data are downloaded, pickled files and numpy compressed files on which subsequent steps are dependent can be generated using the jupyter notebook data_preparation/process_sanger_drug_cell_line.ipynb.

## 4. Running Instructions
Once the input features are generated, we will build our translation of cellular response prediction (TCRP) model. This model consists of a neural network trained by a two-phase design, as outlined by the schematic below:

<img src="images/Figure1_github-01.png" alt="Model overview" width="60%"/>

First, use the *pipelines/prepare_complete_run.py* file to produce slurm submission scripts for generating the TCRP and baseline models. You must specify the run_mode ("tcrp" or "baseline") and run_name


```
usage: generate_MAML_job_cv.py [--run_name RUN_NAME] [--drug_list_file DRUG_LIST_FILE] [--job_id JOB_ID] [--job JOB]
                
```

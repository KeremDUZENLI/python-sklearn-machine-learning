# Stochastic Data Mining of VR Heritage Reconstructions via Élő-Based Pairwise Comparisons

A clean, modular data pipeline designed to extract, cluster, and predict the perceived realism ("Élő" scores) of VR heritage reconstructions using binary software metadata and cross-cohort behavioral comparisons.

## 🔍 Project Overview

1. **Database & Data Extraction (`main_dataset.ipynb`)**
   - Containerized PostgreSQL environments for two separate study cohorts.
   - Extracts user demographics, match win-rates, and cross-cohort Élő volatility.
2. **Data Preparation**
   - Tokenizes and one-hot encodes metadata (focus, site type, platform, device, techniques, software).
   - Dynamically filters out rare features via sparsity distribution analysis.
3. **Clustering**
   - Computes optimal perceptual tiers ($k=4$) using the Elbow Method and Davies-Bouldin Index.
   - Maps continuous Élő scores into distinct Realism Clusters.
4. **Supervised Learning (`main_old_v2.ipynb` & `main_new.ipynb`)**
   - Evaluates feature significance via ANOVA F-tests.
   - Employs Stratified 5-Fold Cross-Validation across 7 classifiers (GaussianNB, LogisticRegression, DecisionTree, RandomForest, SVM(RBF), k-NN, MLP).

## 📁 Repository Structure

```text
└── python-sklearn-machine-learning
    ├── data
    │   ├── db_new/               # PostgreSQL dumps for Student cohort
    │   ├── db_old/               # PostgreSQL dumps for General cohort
    │   ├── dataset_new.csv
    │   ├── dataset_old_v1.csv
    │   ├── dataset_old_v2.csv    # Mapped to match new dataset IDs
    │   └── map.json
    ├── exports
    │   ├── dataset_csv/          # Extracted demographics, win-rates, master datasets
    │   └── dataset_figures/      # Academic plots (Sparsity, K-Means, Scatter)
    ├── docker-compose.yml        # PostgreSQL database orchestration
    ├── main_dataset.ipynb        # DB Connection, EDA, and Visualization
    ├── main_new.ipynb            # ML Pipeline for Student Cohort
    ├── main_old_v1.ipynb         # Legacy Pipeline
    ├── main_old_v2.ipynb         # ML Pipeline for General Cohort
    ├── requirements.txt
    ├── .gitignore
    ├── LICENSE
    └── README.md
```

## ⚙️ Getting Started

1. **Initialize the Databases (Docker)**

```bash
docker-compose build --no-cache
docker-compose up
```

```bash
postgres_test > Create > Database
> Database name      : dataset_old_v1

dataset_old_v1 > Tools > Restore
> Backup file        : dump-postgres_...
> Extra command args : --clean
```

_Do the same for others_

2. **Create the virtual environment (Python 3.13.5)**

```bash
py -3.13 -m venv .env
```

```bash
.\.env\Scripts\activate
```

3. **Install dependencies**

```bash
python -m pip install --upgrade pip setuptools
```

```bash
pip install -r requirements.txt
```

4. **Launch Jupyter**

```bash
python -m ipykernel install --user --name=env_python_sklearn --display-name "Python 3.13.5 (sklearn)"
```

```bash
jupyter lab
```

_Ensure you select `Python 3.13.5 (sklearn)` as your kernel in JupyterLab._

## 📊 Key Findings

- **Perceptual Tiers:** Both the Elbow method and Davies-Bouldin Index confirm exactly $K=4$ distinct realism clusters.
- **Demographic Volatility:** The Gen Z Student cohort demonstrated significantly wider Élő variance (1198 to 1908) compared to the General Public (1210 to 1799), mathematically proving digital-natives are harsher visual critics.
- **The Machine Learning Ceiling:** Stratified Cross-Validation reveals a predictive accuracy ceiling of **~32%** (SVM RBF), proving that visual realism is driven by artist execution and optimization, not binary software flags.

## LICENCE

This project is released under the [MIT License](LICENSE).

© 2025 Kerem DÜZENLİ

## DISCLAIMER

This repository is intended **only for educational and research purposes**.

## SUPPORT MY PROJECTS

If you find this resource valuable and would like to help support my education and doctoral research, please consider treating me to a cup of coffee (or tea) via Revolut.

<div align="center">
  <a href="https://revolut.me/krmdznl" target="_blank">
    <img src="https://img.shields.io/badge/Support%20My%20Projects-Donate%20via%20Revolut-orange?style=for-the-badge" alt="Support my projects via Revolut" />
  </a>
</div> <br>

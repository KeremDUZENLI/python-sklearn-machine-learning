# Stochastic Data Mining of VR Heritage Reconstructions via Élő-Based Pairwise Comparisons

A lightweight Python/Scikit‑Learn project to predict perceived realism (“Élő” scores) of VR heritage reconstructions from scene metadata.

## 🔍 Project Overview

1. **Data preparation**
   - Convert raw lists into CSV
   - One‑hot encode metadata (focus, site type, platform, device, techniques, software)
   - Filter out rare features

2. **Clustering**
   - Generate elbow plot (`data/K_MEAN.png`)
   - Assign each scene to one of 3 Élő clusters (low/medium/high)

3. **Feature scoring**
   - VarianceThreshold + ANOVA F‑test to rank one‑hot flags
   - Aggregate scores by feature group (device, platform, etc.)

4. **Supervised learning**
   - Split into train/test (stratified by cluster)
   - Train & evaluate 7 classifiers (GaussianNB, LogisticRegression, DecisionTree, RandomForest, SVM(RBF), k‑NN, MLP)
   - Report accuracy & wall‑clock time

## 📁 Repository Structure

```
└── python-sklearn-machine-learning
    ├── data
    │   ├── source
    │   │   ├──
    │   ├──
    ├── models
    │   ├── models_ml.py
    │   └── scores_feat.py
    ├── schema
    │   └── config.py
    ├── tests
    │   └── verifier.py
    ├── tools
    │   ├── tools_csv.py
    │   ├── tools_df.py
    │   └── tools_print.py
    ├── .gitignore
    ├── LICENSE
    ├── main.py
    ├── .gitignore
    ├── LICENSE
    ├── main.py
    └── README.md
```

## ⚙️ Getting Started

1. **Create the virtual environment using Python 3.13.5**

   ```bash
   py -3.13 -m venv .env
   ```

2. **Activate the environment**

   ```bash
   .\.env\Scripts\activate
   ```

3. **Update pip**

   ```bash
   python -m pip install --upgrade pip
   ```

4. **Update setuptools**

   ```bash
   pip install --upgrade setuptools
   ```

5. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

## 📝 Jupyter Notebook

1. **Register Python Environment**

   ```bash
   python -m ipykernel install --user --name=env_python_sklearn --display-name "Python 3.13.5 (sklearn)"
   ```

2. **Launch Jupyter**

   ```bash
   jupyter lab
   ```

3. **Change Kernel**

   ```bash
   Change kernel in Jupyterlab (Select after choosing the .ipynb file) =
   Kernel → Change Kernel →
   ```

- Generates CSVs, prints summaries
- Saves `data/K_MEAN.png`
- Trains models and prints results

---

## 📊 Key Findings

- **Elbow plot**: $K=3$ clusters
- **Top ANOVA features**: `device_hmd`, `platform_ar`, `sr_unity`, …
- **Best classifier**: SVM (RBF) — \~47 % accuracy

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

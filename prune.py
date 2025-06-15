import pandas as pd
from sklearn.model_selection   import train_test_split
from sklearn.preprocessing     import LabelEncoder
from sklearn.feature_selection import SelectKBest, f_classif

# 1) Configuration
DATA_PATH       = 'data/DATA_cluster3.csv'
PVALUE_CUTOFF   = 0.05   # features with p-value > this are uninformative
F_SCORE_CUTOFF  = 1.0    # features with F-score < this are very weak

# 2) Load and split
def load_and_split(path):
    df = pd.read_csv(path)
    X  = df.drop(['elo', 'cluster'], axis=1)
    y  = LabelEncoder().fit_transform(df['cluster'])
    return train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)

# 3) Score features
def score_features(X_tr, y_tr):
    selector = SelectKBest(score_func=f_classif, k='all')
    selector.fit(X_tr, y_tr)
    return pd.DataFrame({
        'feature': X_tr.columns,
        'f_score': selector.scores_,
        'p_value': selector.pvalues_
    }).sort_values('f_score')

# 4) Identify uninformative features
def list_uninformative(df_scores, p_thresh, f_thresh):
    mask = (df_scores['p_value'] > p_thresh) | (df_scores['f_score'] < f_thresh)
    return df_scores[mask]

# 5) Main
X_tr, X_te, y_tr, y_te = load_and_split(DATA_PATH)
scores = score_features(X_tr, y_tr)

print("\nAll features scored (lowest F-score first):")
print(scores.to_string(index=False))

uninfo = list_uninformative(scores, PVALUE_CUTOFF, F_SCORE_CUTOFF)
print(f"\n\nFeatures with p-value > {PVALUE_CUTOFF} OR F-score < {F_SCORE_CUTOFF}:")
for feat in uninfo['feature']:
    print(f"  • {feat}")

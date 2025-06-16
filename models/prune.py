import pandas as pd
from sklearn.model_selection   import train_test_split
from sklearn.preprocessing     import LabelEncoder
from sklearn.feature_selection import SelectKBest, f_classif

from env.config                import COLUMN_MAP


DATA_PATH      = 'data/DATA_cluster3.csv'
TEST_SIZE      = 0.2
RANDOM_STATE   = 42


df = pd.read_csv(DATA_PATH)
X = df.drop(['elo','cluster'], axis=1)
y = LabelEncoder().fit_transform(df['cluster'])
X_tr, X_te, y_tr, y_te = train_test_split(
    X, y, test_size=TEST_SIZE, stratify=y, random_state=RANDOM_STATE
)

selector = SelectKBest(score_func=f_classif, k='all').fit(X_tr, y_tr)
scores_df = pd.DataFrame({
    'feature' : X_tr.columns,
    'f_score' : selector.scores_,
    'p_value' : selector.pvalues_,
})

freq = X_tr.sum().rename('frequency')

full_df = (
    scores_df
    .set_index('feature')
    .join(freq)
    .reindex(COLUMN_MAP) 
    .dropna()
    .reset_index()
)

# 5) Tidy print
print("\nFeature  |  F-score   |  p-value   |  freq(1's in train)\n" + "-"*50)
print(full_df.to_string(
    index=False,
    formatters={
      'f_score'   : '{:8.2f}'.format,
      'p_value'   : '{:8.3f}'.format,
      'frequency' : '{:8d}'.format
    }
))

# 6) Keep top‑k F‑scores
k = 20
selector_k = SelectKBest(f_classif, k=k).fit(X_tr, y_tr)
mask_k     = selector_k.get_support()
topk_feats = X_tr.columns[mask_k]

print(f"\nTop {k} features by F-score:")
print("-" * 40)
for feat, score in zip(X_tr.columns[mask_k], selector_k.scores_[mask_k]):
    print(f"  {feat:<40} {score:6.2f}")
print()
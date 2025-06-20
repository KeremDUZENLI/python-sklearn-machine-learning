from sklearn.pipeline          import Pipeline
from sklearn.feature_selection import VarianceThreshold, SelectKBest, f_classif

from sklearn.preprocessing     import LabelEncoder
from sklearn.model_selection   import train_test_split

import pandas as pd


def split_dataset(df, test_size, random_state, column_drop, column_label):
    X = df.drop(column_drop, axis=1)
    y = LabelEncoder().fit_transform(df[column_label])
    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=test_size,
        stratify=y,
        random_state=random_state
    )
    return X_train, X_test, y_train, y_test


def compute_feature_scores(X_train, y_train):
    pipe = Pipeline([
        ('var', VarianceThreshold()),
        ('skb', SelectKBest(f_classif, k='all'))
    ])
    pipe.fit(X_train, y_train)

    mask  = pipe.named_steps['var'].get_support()
    feats = X_train.columns[mask]
    skb   = pipe.named_steps['skb']

    rows = []
    for feat, f, p in zip(feats, skb.scores_, skb.pvalues_):
        rows.append({
            'feature':   feat,
            'f_score':    f,
            'p_value':    p,
            'frequency':  int(X_train[feat].sum()),
        })

    return pd.DataFrame(rows)


def aggregate_groups(df_scores, columns_metadata):
    rows = []
    for grp, (mapping, _) in columns_metadata.items():
        feature_keys = list(mapping.keys())
        sub = df_scores[df_scores['feature'].isin(feature_keys)]
        if not sub.empty:
            rows.append({
                'feature':         grp,
                'f_score_mean':    sub['f_score'].mean(),
                'p_value_mean':    sub['p_value'].mean(),
                'frequency_total': int(sub['frequency'].sum()),
            })
    return pd.DataFrame(rows)

import pandas as pd
from sklearn.pipeline            import Pipeline
from sklearn.model_selection     import train_test_split
from sklearn.preprocessing       import LabelEncoder
from sklearn.feature_selection   import VarianceThreshold, SelectKBest, f_classif


def rank_features(df, columns_onehot, random_state, test_size):
    X = df.drop(['elo','cluster'], axis=1)
    y = LabelEncoder().fit_transform(df['cluster'])

    X_tr, _, y_tr, _ = train_test_split(
        X, y,
        test_size=test_size,
        stratify=y,
        random_state=random_state
    )
    
    kept_cols, f_scores, p_values = _select_and_score(X_tr, y_tr)
    X_tr_clean                    = X_tr.loc[:, kept_cols]
    valid_columns_onehot          = [column for column in columns_onehot if column in kept_cols]   
    
    df_results = (pd.DataFrame({
        'feature': kept_cols,
        'f_score': f_scores,
        'p_value': p_values,
        }).set_index('feature')
    )

    frequency = X_tr_clean.sum().rename('frequency')
    df_scores = (
        df_results
        .join(frequency)
        .loc[valid_columns_onehot]
        .reset_index()
    )

    return df_scores


def rank_groups(df, columns_group):
    rows = []
    for grp, prefix in columns_group.items():
        group_df = df[df['feature'].str.startswith(prefix)]
        if not group_df.empty:
            f_mean = group_df['f_score'].mean()
            p_mean = group_df['p_value'].mean()
            freq_sum = group_df['frequency'].sum()
            rows.append((grp, f_mean, p_mean, freq_sum))
    return (
        pd.DataFrame(
            rows,
            columns=['feature', 'f_score_mean', 'p_value_mean', 'frequency_total']
        )
        .sort_values('f_score_mean', ascending=False)
        .reset_index(drop=True)
    )


def _select_and_score(X_train, y_train):
    pipeline = Pipeline([
        ('var', VarianceThreshold(threshold=0.0)),           # 'var' removes any zero-variance columns
        ('skb', SelectKBest(score_func=f_classif, k='all')), # 'skb' computes f_classif on the remaining ones
    ])
    pipeline.fit(X_train, y_train)

    var_mask  = pipeline.named_steps['var'].get_support()
    kept_cols = X_train.columns[var_mask]

    skb       = pipeline.named_steps['skb']
    f_scores  = skb.scores_
    p_values  = skb.pvalues_

    return kept_cols, f_scores, p_values

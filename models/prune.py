import pandas as pd
from sklearn.pipeline            import Pipeline
from sklearn.model_selection     import train_test_split
from sklearn.preprocessing       import LabelEncoder
from sklearn.feature_selection   import VarianceThreshold, SelectKBest, f_classif


def rank_features(df, columns_onehot, random_state, test_size, top_n):
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

    scores_df = pd.DataFrame({
        'feature': kept_cols,
        'f_score': f_scores,
        'p_value': p_values,
    })

    frequency = X_tr_clean.sum().rename('frequency')
    full_df   = (
        scores_df
        .set_index('feature')
        .join(frequency)
        .reindex(valid_columns_onehot)
        .dropna()
        .reset_index()
    )

    _print_table_ranking(full_df)
    _print_table_ranking_top_n(full_df, top_n)


def _print_table_ranking(df):
    rows = [(row['feature'], row['f_score'], row['p_value'], int(row['frequency']))
            for _, row in df.iterrows()]

    feat_w = max(len(feat) for feat, *_ in rows + [('Feature',)]) + 2
    f_w    = max(len(f"{f:0.2f}") for _, f, _, _ in rows + [(None, 0.0,0,0)]) + 2
    p_w    = max(len(f"{p:0.3f}") for *_, p, _ in rows + [(None,0.0,0.0,0)]) + 2
    freq_w = max(len(str(freq)) for *_, freq in rows + [(None,0.0,0.0,0,0)]) + 2

    header = (f"{'Feature':<{feat_w}} | "
              f"{'F-score':>{f_w}} | "
              f"{'p-value':>{p_w}} | "
              f"{'Freq':>{freq_w}}")
    separator = '─' * len(header)

    print("\n" + header)
    print(separator)

    for feat, f_score, p_value, freq in rows:
        print(f"{feat:<{feat_w}} | "
              f"{f_score:>{f_w}.2f} | "
              f"{p_value:>{p_w}.3f} | "
              f"{freq:>{freq_w}d}")


def _print_table_ranking_top_n(df, top_n):
    top_features = df.nlargest(top_n, 'f_score')['feature'].tolist()
    df_top = df[df['feature'].isin(top_features)]

    rows = [(row.feature, row.f_score) for row in df_top.itertuples()]

    feat_w = max(len(feat) for feat, _ in rows + [('Feature', '')]) + 2
    f_w    = max(len(f"{f:0.2f}") for _, f in rows + [(None, 0.0)]) + 2

    header = f"{'Feature':<{feat_w}} | {'F-score':>{f_w}}"
    separator = '─' * len(header)

    print(f"\n\nTop {top_n} features by F-score:")
    print(header)
    print(separator)

    for feat, f_score in rows:
        print(f"{feat:<{feat_w}} | {f_score:>{f_w}.2f}")


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

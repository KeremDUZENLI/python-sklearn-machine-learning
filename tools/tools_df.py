import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


def filter_rare_features(df, columns_metadata, min_freq):
    for base, (mapping_dict, is_list) in columns_metadata.items():
        if not is_list:
            continue

        for col in mapping_dict.keys():
            if col in df.columns and df[col].sum() < min_freq:
                df.drop(columns=[col], inplace=True)

    return df


def create_df_binary(df, columns_metadata):
    for column, (mapping, is_list) in columns_metadata.items():
        if column in df.columns:
            df = _create_rows_onehot(df, column, mapping, is_list)

    ordered_cols = []
    for column, (mapping, _) in columns_metadata.items():
        ordered_cols.extend([flag for flag in mapping.keys() if flag in df.columns])

    return df[ordered_cols]


def create_df_cluster(df, elos, k_values, random_state):
    df = _add_column_elo(df, elos)
    
    if isinstance(k_values, int):
        return _add_column_cluster(df, k_values, random_state)
    
    df_clustered = {}
    for k in k_values:
        df_clustered[k] = _add_column_cluster(df, k, random_state)
    return df_clustered


def _create_rows_onehot(df, column, mapping, is_list=True):
    flags = {}
    for column_flag, label in mapping.items():
        if is_list:
            flags[column_flag] = df[column].apply(lambda lst: int(label in lst))
        else:
            flags[column_flag] = df[column].apply(lambda x: int(x == label))
    return pd.concat([df, pd.DataFrame(flags, index=df.index)], axis=1)


def _add_column_elo(df, elos):
    if len(df) != len(elos):
        raise ValueError(f"len(ROWS) {len(df)} != len(ELOS) {len(elos)}")
    
    df = df.copy()
    df['elo'] = elos
    return df


def _add_column_cluster(df, k, random_state):
    km = _get_k_means(k, random_state)
    km.fit(df[['elo']])
    labels = km.labels_

    centers = km.cluster_centers_.flatten()
    order = centers.argsort()
    remap = {original: new + 1 for new, original in enumerate(order)}

    df = df.copy()
    df['cluster'] = [f"cluster_{remap[label]}" for label in labels]
    return df


def _get_k_means(k, random_state):
    return KMeans(n_clusters=k, random_state=random_state)


def plot_k_means(path_output, elos, k_max, random_state):
    X = np.array(elos).reshape(-1, 1)
    k_values = list(range(1, k_max))
    
    inertias = []
    for k in k_values:
        k_mean = _get_k_means(k, random_state).fit(X)
        inertias.append(k_mean.inertia_)

    plt.figure(figsize=(8, 4))
    plt.plot(k_values, inertias, marker='o')
    plt.xticks(k_values)
    plt.xlabel('Number of Clusters (k)')
    plt.ylabel('Inertia')
    plt.title('Elbow Method for Optimal Number of Clusters')
    plt.tight_layout()
    plt.savefig(path_output)
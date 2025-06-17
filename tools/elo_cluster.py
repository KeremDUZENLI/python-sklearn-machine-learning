import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
  
       
def create_df_clustered(df, elos, random_state, k_values):
    df = _add_column_elo(df, elos)
    
    df_clustered = {}
    for k in k_values:
        df_clustered[k] = _add_column_cluster(df, k, random_state)
    return df_clustered


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


def plot_k_means(path_output, elos, random_state, k_values):
    X = np.array(elos).reshape(-1, 1)
    
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
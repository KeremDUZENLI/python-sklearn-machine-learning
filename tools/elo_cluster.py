from sklearn.cluster import KMeans

 
def create_csv_clustered(df, path_output_prefix, elos, k_values):
    df = _add_column_elo(df, elos)
    for k in k_values:
        df_clustered = _add_column_cluster(df, k)
        _print_summary_cluster(df_clustered, k)
        _save_csv_clustered(df_clustered, k, path_output_prefix)


def _add_column_elo(df, elos):
    if len(df) != len(elos):
        raise ValueError(f"len(ROWS) {len(df)} != len(ELOS) {len(elos)}")
    
    df = df.copy()
    df['elo'] = elos
    return df


def _add_column_cluster(df, k):
    km = KMeans(n_clusters=k, random_state=42)
    km.fit(df[['elo']])
    labels = km.labels_

    centers = km.cluster_centers_.flatten()
    order = centers.argsort()
    remap = {original: new + 1 for new, original in enumerate(order)}

    df = df.copy()
    df['cluster'] = [f"cluster_{remap[label]}" for label in labels]
    return df


def _print_summary_cluster(df, k):
    print(f"\n=== cluster_{k} ===")
    summary = df.groupby('cluster')['elo'].agg(['min', 'max', 'count'])
    
    for cluster_name, row in summary.iterrows():
        print(f"{cluster_name}: min={row['min']}, max={row['max']}, {row['count']} items")


def _save_csv_clustered(df, k, path_prefix):
    filename = f"{path_prefix}_{k}.csv"
    df.to_csv(filename, index=False)
    print(f"{filename} created.\n")

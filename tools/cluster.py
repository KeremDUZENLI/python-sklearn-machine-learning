import pandas as pd
from sklearn.cluster import KMeans
from data._DATA_ import ELOS


K_MIN  = 3
K_MAX  = 10
SOURCE = 'data/DATA_onehot.csv'
OUTPUT = 'data/DATA_cluster'

def load_csv(path):
    return pd.read_csv(path)

def add_elos(df):
    if len(df) != len(ELOS):
        raise ValueError(f"Row count ({len(df)}) != len(ELOS) ({len(ELOS)})")
    df = df.copy()
    df['elo'] = ELOS
    return df

def cluster_elos(df, k):
    X = df[['elo']].values
    km = KMeans(n_clusters=k, random_state=42).fit(X)
    labels = km.labels_

    centers = km.cluster_centers_.flatten()
    order = centers.argsort()
    remap = {orig: new+1 for new, orig in enumerate(order)}

    df2 = df.copy()
    df2['cluster'] = [f"cluster_{remap[l]}" for l in labels]
    return df2

def export_clusters(df_with_elo, ks, output):
    for k in ks:
        dfk = cluster_elos(df_with_elo, k)

        print(f"cluster_{k}")
        grouped = dfk.groupby(f'cluster')['elo'].agg(['min','max','count'])
        for cl, row in grouped.iterrows():
            print(f"{cl}: min={row['min']}, max={row['max']}, {row['count']} items")

        filename = f"{output}{k}.csv"
        dfk.to_csv(filename, index=False)
        print(f"{filename} created\n")


df = load_csv(SOURCE)
df = add_elos(df)
export_clusters(df, range(K_MIN, K_MAX), OUTPUT)

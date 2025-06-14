import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from data.DATA import ELOS


K = 3
MAX_K = 10

X = np.array(ELOS).reshape(-1, 1)
inertias = []
ks = list(range(1, MAX_K + 1))
for k in ks:
    km = KMeans(n_clusters=k, random_state=42).fit(X)
    inertias.append(km.inertia_)

plt.figure(figsize=(8, 4))
plt.plot(ks, inertias, marker='o')
plt.xticks(ks)
plt.xlabel('Number of Clusters (k)')
plt.ylabel('Inertia')
plt.title('Elbow Method for Optimal Number of Clusters')
plt.tight_layout()
plt.savefig('output/method_elbow.png')

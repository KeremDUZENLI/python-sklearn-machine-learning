import re
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt

# 5. Path to your DATA.py file containing the tuples
file_path = 'DATA/DATA.py'
with open(file_path, 'r') as f:
    lines = f.readlines()

# 6. Regex to match tuples and capture ELO
pattern = re.compile(
    r"^(?P<prefix>\s*\(\s*\d+\s*,.*?,\s*)(?P<elo>\d+)(,\s*'cluster_\d+')?(?P<suffix>\s*\)\s*,?\s*)$"
)

# 7. K-means clustering on ELO
X = np.array(elos).reshape(-1, 1)
kmeans = KMeans(n_clusters=K, random_state=42).fit(X)
labels = kmeans.labels_
centers = kmeans.cluster_centers_.flatten()
order = np.argsort(centers)
label_map = {orig: new+1 for new, orig in enumerate(order)}

# 8. Compute and print cluster ranges
ranges = {}
for lab, val in zip(labels, elos):
    cl = label_map[lab]
    ranges.setdefault(cl, []).append(val)
for cl in sorted(ranges):
    vals = ranges[cl]
    count = len(ranges[cl])
    print(f"cluster_{cl}: min={min(vals)}, max={max(vals)}, {count} items")

# 9. Update file lines in-place with both new ELO and cluster labels
out_lines = []
idx = 0
for line in lines:
    m = pattern.match(line)
    if m:
        elo_val = elos[idx]
        cluster_label = f"'cluster_{label_map[labels[idx]]}'"
        new_line = f"{m.group('prefix')}{elo_val}, {cluster_label}{m.group('suffix')}"
        out_lines.append(new_line)
        idx += 1
    else:
        out_lines.append(line)

# 10. Write back to file
with open(file_path, 'w') as f:
    f.writelines(out_lines)
print(f"✅ Updated {idx} ELO and cluster entries successfully.")

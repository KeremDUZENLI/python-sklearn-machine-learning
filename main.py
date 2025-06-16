from data._DATA_       import ROWS, ELOS
from schema.config     import HEADER, COLUMNS_ONEHOT, COLUMNS_METADATA
from tools.tools_csv   import create_csv, read_csv
from tools.elo_cluster import create_csv_clustered
from tools.onehot      import create_csv_binary
from tools.utils       import print_summary


K_MIN  = 3
K_MAX  = 10

PATH_DATA_        = 'data/DATA_.csv'
PATH_DATA_BINARY  = 'data/DATA_BINARY.csv'
PATH_DATA_CLUSTER = 'data/DATA_CLUSTER'


# create DATA_.csv
create_csv(PATH_DATA_, HEADER, ROWS)

# create DATA_BINARY.csv
df = read_csv(PATH_DATA_, COLUMNS_METADATA)
create_csv_binary(df, PATH_DATA_BINARY, COLUMNS_METADATA, COLUMNS_ONEHOT)

# verify the datasets
df = read_csv(PATH_DATA_, COLUMNS_METADATA)
print_summary(df, COLUMNS_METADATA)

# create CLUSTERS
df       = read_csv(PATH_DATA_BINARY)
k_values = list(range(K_MIN, K_MAX + 1))
create_csv_clustered(df, PATH_DATA_CLUSTER, ELOS, k_values)

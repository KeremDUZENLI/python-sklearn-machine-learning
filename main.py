from data._DATA_       import ROWS, ELOS
from schema.config     import HEADER, COLUMNS_ONEHOT, COLUMNS_METADATA
from tools.tools_csv   import create_csv, read_csv
from tools.elo_cluster import plot_kmeans, create_csv_clustered
from tools.onehot      import create_csv_binary
from tools.utils       import print_summary
from models.prune      import rank_features


K_MIN  = 3
K_MAX  = 10

RANDOM_STATE = 42
TEST_SIZE = 0.2
TOP_N = 20

PATH_PLOT         = 'data/_.png'
PATH_DATA_        = 'data/DATA_.csv'
PATH_DATA_BINARY  = 'data/DATA_BINARY.csv'
PATH_DATA_CLUSTER = 'data/DATA_CLUSTER'
PATH_DATA_PRUNE   = 'data/DATA_CLUSTER_3.csv'


# # create DATA_.csv
# create_csv(PATH_DATA_, HEADER, ROWS)

# # create DATA_BINARY.csv
# df = read_csv(PATH_DATA_, COLUMNS_METADATA)
# create_csv_binary(df, PATH_DATA_BINARY, COLUMNS_METADATA, COLUMNS_ONEHOT)

# # verify the datasets
# df = read_csv(PATH_DATA_, COLUMNS_METADATA)
# print_summary(df, COLUMNS_METADATA)

# # plot k_means
# plot_kmeans(PATH_PLOT, ELOS, K_MAX, RANDOM_STATE)

# # create CLUSTERS
# df = read_csv(PATH_DATA_BINARY)
# create_csv_clustered(df, PATH_DATA_CLUSTER, K_MIN, K_MAX, RANDOM_STATE)

# pruning
df = read_csv(PATH_DATA_PRUNE)
rank_features(df, COLUMNS_ONEHOT, RANDOM_STATE, TEST_SIZE, TOP_N)

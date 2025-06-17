from data._DATA_       import ROWS, ELOS
from schema.config     import HEADER, COLUMNS_ONEHOT, COLUMNS_METADATA, COLUMNS_GROUP
from tools.tools_csv   import convert_list_csv, save_csv, read_csv
from tools.tools_print import print_summary, print_summary_cluster, print_df_scores, print_df_scores_group
from tools.elo_cluster import create_df_clustered, plot_k_means
from tools.onehot      import create_df_binary
from tools.rank        import rank_features, rank_groups


K            = 3
K_MAX        = 10
RANDOM_STATE = 42
TEST_SIZE    = 0.2

PATH_PLOT         = 'data/_.png'
PATH_DATA_        = 'data/DATA_.csv'
PATH_DATA_BINARY  = 'data/DATA_BINARY.csv'
PATH_DATA_CLUSTER = 'data/DATA_CLUSTER.csv'


# plot k_means
plot_k_means(PATH_PLOT, ELOS, K_MAX, RANDOM_STATE)

# create DATA_.csv
convert_list_csv(PATH_DATA_, HEADER, ROWS)

# verify DATA_.csv
df = read_csv(PATH_DATA_, COLUMNS_METADATA)
print_summary(df, COLUMNS_METADATA)

# create DATA_BINARY.csv
df = read_csv(PATH_DATA_, COLUMNS_METADATA)
df_binary = create_df_binary(df, COLUMNS_METADATA, COLUMNS_ONEHOT)
save_csv(PATH_DATA_BINARY, df_binary)

# verify DATA_BINARY.csv
df = read_csv(PATH_DATA_BINARY)
print_summary(df, COLUMNS_GROUP)

# create DATA_CLUSTER.csv
df = read_csv(PATH_DATA_BINARY)
df_clustered = create_df_clustered(df, ELOS, K, RANDOM_STATE)
save_csv(PATH_DATA_CLUSTER, df_clustered)
print_summary_cluster(df_clustered)

# verify DATA_CLUSTER.csv
df = read_csv(PATH_DATA_CLUSTER)
print_summary(df, COLUMNS_GROUP)

# rank DATA_CLUSTER.csv
df = read_csv(PATH_DATA_CLUSTER)
df_scores = rank_features(df, COLUMNS_ONEHOT, RANDOM_STATE, TEST_SIZE)
print_df_scores(df_scores, COLUMNS_GROUP)
print_df_scores(df_scores, COLUMNS_GROUP, 20)

# rank groups DATA_CLUSTER.csv
df = read_csv(PATH_DATA_CLUSTER)
df_scores = rank_features(df, COLUMNS_ONEHOT, RANDOM_STATE, TEST_SIZE)
df_groups = rank_groups(df_scores, COLUMNS_GROUP)
print_df_scores_group(df_groups, COLUMNS_GROUP)
print_df_scores_group(df_groups, COLUMNS_GROUP, 5)

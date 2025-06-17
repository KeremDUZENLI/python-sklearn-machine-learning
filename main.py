from data._DATA_       import ROWS, ELOS
from schema.config     import HEADER, COLUMNS_ONEHOT, COLUMNS_METADATA, COLUMNS_GROUP
from tools.tools_csv   import convert_list_csv, save_csv, read_csv
from tools.tools_print import print_summary, print_summary_cluster, print_df_scores
from tools.elo_cluster import create_df_clustered, plot_k_means
from tools.onehot      import create_df_binary
from tools.rank        import rank_features


K_MIN        = 3
K_MAX        = 10
TOP_N        = 20
TEST_SIZE    = 0.2
RANDOM_STATE = 42

PATH_PLOT         = 'data/_.png'
PATH_DATA_        = 'data/DATA_.csv'
PATH_DATA_BINARY  = 'data/DATA_BINARY.csv'
PATH_DATA_CLUSTER = 'data/DATA_CLUSTER'
PATH_DATA_RANK    = 'data/DATA_CLUSTER_3.csv'


# # plot k_means
# k_values = list(range(1, K_MAX))
# plot_k_means(PATH_PLOT, ELOS, RANDOM_STATE, k_values)

# # create DATA_.csv
# convert_list_csv(PATH_DATA_, HEADER, ROWS)

# # verify DATA_.csv
# df = read_csv(PATH_DATA_, COLUMNS_METADATA)
# print_summary(df, COLUMNS_METADATA)

# # create DATA_BINARY.csv
# df = read_csv(PATH_DATA_, COLUMNS_METADATA)
# df_binary = create_df_binary(df, COLUMNS_METADATA, COLUMNS_ONEHOT)
# save_csv(PATH_DATA_BINARY, df_binary)

# verify DATA_BINARY.csv
df = read_csv(PATH_DATA_BINARY)
print_summary(df, COLUMNS_GROUP)

# # create DATA_CLUSTER_3.csv
# k_values = [3]
# df = read_csv(PATH_DATA_BINARY)
# df_clustered = create_df_clustered(df, ELOS, RANDOM_STATE, k_values)

# for k, df_clustered in df_clustered.items():
#     print_summary_cluster(df_clustered, k)
#     save_csv(PATH_DATA_CLUSTER, df_clustered, k)

# rank DATA_CLUSTER3.csv
df = read_csv(PATH_DATA_RANK)
df_scores = rank_features(df, COLUMNS_ONEHOT, RANDOM_STATE, TEST_SIZE)
print_df_scores(df_scores, COLUMNS_GROUP)
print_df_scores(df_scores, COLUMNS_GROUP, TOP_N)

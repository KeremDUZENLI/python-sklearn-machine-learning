from data._DATA_        import ROWS, ELOS
from schema.config      import HEADER, COLUMNS_METADATA

from models.scores_feat import split_dataset, compute_feature_scores, aggregate_groups
from models.models_ml   import evaluate_models

from tools.tools_df     import create_df_binary, create_df_cluster, plot_k_means
from tools.tools_csv    import convert_list_csv, save_csv, read_csv, keep_columns_csv
from tools.tools_print  import print_summary, print_cluster_range, print_scores, print_models


# Parameters
K            = 3
K_MAX        = 10
TEST_SIZE    = 0.2
RANDOM_STATE = 42

# Paths
PATH_PLOT             = 'data/_.png'
PATH_DATA_            = 'data/DATA_.csv'
PATH_DATA_BINARY      = 'data/DATA_BINARY.csv'
PATH_DATA_CLUSTER     = 'data/DATA_CLUSTER.csv'
PATH_DATA_FILTER      = 'data/DATA_FILTER.csv'
PATH_DATA_RANK_SCORES = 'data/DATA_RANK_SCORES.csv'
PATH_DATA_RANK_GROUPS = 'data/DATA_RANK_GROUPS.csv'
PATH_DATA_RESULTS     = 'data/DATA_RESULTS.csv'


# # 1. Convert list to csv
# df_ = convert_list_csv(HEADER[:-2], ROWS)
# save_csv(df_, PATH_DATA_)

# # 2. One-hot encoding
# df_binary = create_df_binary(read_csv(PATH_DATA_, COLUMNS_METADATA), COLUMNS_METADATA)
# save_csv(df_binary, PATH_DATA_BINARY)

# # 3. Clustering
# df_cluster = create_df_cluster(read_csv(PATH_DATA_BINARY), ELOS, K, RANDOM_STATE)
# save_csv(df_cluster, PATH_DATA_CLUSTER)

# # 4. Prepare dataset
# X_train, X_test, y_train, y_test = split_dataset(
#     df           = read_csv(PATH_DATA_CLUSTER), 
#     test_size    = TEST_SIZE, 
#     random_state = RANDOM_STATE, 
#     column_drop  = ['elo', 'cluster'], 
#     column_label = 'cluster'
# )

# # 5. Rank features
# df_rank_scores = compute_feature_scores(X_train, y_train)
# save_csv(df_rank_scores, PATH_DATA_RANK_SCORES)

# # 6. Rank groups
# df_rank_groups = aggregate_groups(df_rank_scores, COLUMNS_METADATA)
# save_csv(df_rank_groups, PATH_DATA_RANK_GROUPS)

# # 7. Filter columns
# column_keep = ['study_focus', 'platform', 'device'] + ['elo','cluster']
# df_filter = keep_columns_csv(read_csv(PATH_DATA_CLUSTER), COLUMNS_METADATA, column_keep)
# save_csv(df_filter, PATH_DATA_FILTER)

# # 8. Run models
# X_train, X_test, y_train, y_test = split_dataset(
#     df           = read_csv(PATH_DATA_FILTER), 
#     test_size    = TEST_SIZE, 
#     random_state = RANDOM_STATE, 
#     column_drop  = ['elo', 'cluster'], 
#     column_label = 'cluster'
# )
# results = evaluate_models(X_train, X_test, y_train, y_test)
# df_results = convert_list_csv(['model', 'accuracy', 'time'], results)
# save_csv(df_results, PATH_DATA_RESULTS)



# ##### RESULTS #####
# plot_k_means(PATH_PLOT, ELOS, K_MAX, RANDOM_STATE)

# print_summary(read_csv(PATH_DATA_, COLUMNS_METADATA), COLUMNS_METADATA)
# print_summary(read_csv(PATH_DATA_BINARY), COLUMNS_METADATA)
# print_summary(read_csv(PATH_DATA_CLUSTER), COLUMNS_METADATA)

# print_cluster_range(read_csv(PATH_DATA_CLUSTER))

# print_scores(
#     df             = read_csv(PATH_DATA_RANK_SCORES), 
#     columns        = ['feature', 'f_score', 'p_value', 'frequency'],
#     sort_by        = None,
#     threshold_p    = 0.35,
#     threshold_freq = None,
#     top_n          = None,
# )
# print_scores(
#     df             = read_csv(PATH_DATA_RANK_GROUPS),
#     columns        = ['feature', 'f_score_mean', 'p_value_mean', 'frequency_total'],
#     sort_by        = None,
#     threshold_p    = 0.35,
#     threshold_freq = None,
#     top_n          = None,
# )
# print_models(
#     df      = read_csv(PATH_DATA_RESULTS),
#     columns = ['model','accuracy','time'],
#     sort_by = 'accuracy',
# )

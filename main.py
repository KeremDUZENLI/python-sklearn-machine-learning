from data._DATA_       import ROWS, ELOS
from schema.config     import HEADER, COLUMNS_METADATA
from tools.tools_csv   import convert_list_csv, save_csv, read_csv, keep_columns_csv
from tools.tools_print import print_summary, print_cluster_range, print_scores
from tools.elo_cluster import create_df_clustered, plot_k_means
from tools.onehot      import create_df_binary
from tools.rank        import split_train, compute_feature_scores, aggregate_groups
from models.models     import evaluate_models


# Parameters
K            = 3
K_MAX        = 10
TEST_SIZE    = 0.2
RANDOM_STATE = 42

# Paths
PATH_PLOT         = 'data/_.png'
PATH_DATA_        = 'data/DATA_.csv'
PATH_DATA_BINARY  = 'data/DATA_BINARY.csv'
PATH_DATA_CLUSTER = 'data/DATA_CLUSTER.csv'
PATH_DATA_FILTER  = 'data/DATA_FILTER.csv'


# 1. Elbow plot for clustering
plot_k_means(PATH_PLOT, ELOS, K_MAX, RANDOM_STATE)

# 2. Export raw CSV
convert_list_csv(PATH_DATA_, HEADER, ROWS)

# 3. Summarize raw data
print_summary(read_csv(PATH_DATA_, COLUMNS_METADATA), COLUMNS_METADATA)

# 4. One-hot encoding
df_binary = create_df_binary(read_csv(PATH_DATA_, COLUMNS_METADATA), COLUMNS_METADATA)
save_csv(df_binary, PATH_DATA_BINARY)
print_summary(df_binary, COLUMNS_METADATA)

# 5. Clustering
df_cluster = create_df_clustered(df_binary, ELOS, K, RANDOM_STATE)
save_csv(df_cluster, PATH_DATA_CLUSTER)
print_summary(df_cluster, COLUMNS_METADATA)
print_cluster_range(df_cluster)

# 6. Prepare dataset
X_train, X_test, y_train, y_test = split_train(
    read_csv(PATH_DATA_CLUSTER), 
    TEST_SIZE, 
    RANDOM_STATE, 
    ['elo', 'cluster'], 
    'cluster'
)

# 7. Rank features
df_scores  = compute_feature_scores(X_train, y_train)
print_scores(
    df             = df_scores, 
    columns        = ['feature', 'f_score', 'p_value', 'frequency'],
    sort_by        = None,
    threshold_p    = 0.35,
    threshold_freq = None,
    top_n          = None,
)

# 8. Rank groups
df_groups = aggregate_groups(df_scores, COLUMNS_METADATA)
print_scores(
    df             = df_groups,
    columns        = ['feature', 'f_score_mean', 'p_value_mean', 'frequency_total'],
    sort_by        = None,
    threshold_p    = 0.35,
    threshold_freq = None,
    top_n          = None,
)

# 9. Filter columns
column_keep = ['study_focus', 'platform', 'device'] + ['elo','cluster']
df = keep_columns_csv(read_csv(PATH_DATA_CLUSTER), COLUMNS_METADATA, column_keep)
save_csv(df, PATH_DATA_FILTER)

# 10. Run models
X_train, X_test, y_train, y_test = split_train(
    read_csv(PATH_DATA_FILTER), 
    TEST_SIZE, 
    RANDOM_STATE, 
    ['elo', 'cluster'], 
    'cluster'
)

results = evaluate_models(X_train, X_test, y_train, y_test)
print(f"\n{'Model':<40} │ {'Accuracy (%)':<20} │ {'Time (s)':<10}")
print('─' * 80)
for name, acc, elapsed in results:
    print(f"{name:<40} │ {acc:<20.3f} │ {elapsed:<10.3f}")

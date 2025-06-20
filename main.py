from data.source.DB     import ROWS, ELOS
from schema.config      import HEADER, COLUMNS_METADATA

from models.scores_feat import split_dataset, compute_feature_scores, aggregate_groups
from models.models_ml   import evaluate_models

from tools.tools_df     import filter_rare_features, create_df_binary, create_df_cluster, plot_k_means
from tools.tools_csv    import convert_list_csv, save_csv, read_csv, keep_columns_csv
from tools.tools_print  import print_anomaly, print_summary, print_cluster_range, print_scores, print_models


# Parameters
K            = 3
K_MAX        = 10
MIN_FREQ     = 10
TEST_SIZE    = 0.2
RANDOM_STATE = 42

# Paths
PATH_PLOT                    = 'data/K_MEAN.png'
PATH_DATA_                   = 'data/DATA_.csv'
PATH_DATA_BINARY             = 'data/DATA_BINARY.csv'
PATH_DATA_CLUSTER            = 'data/DATA_CLUSTER.csv'

PATH_DATA_FEATURES_SCORES = 'data/DATA_FEATURES_SCORES.csv'
PATH_DATA_FEATURES_FILTER = 'data/DATA_FEATURES_FILTER.csv'
PATH_DATA_FEATURES_RESULT = 'data/DATA_FEATURES_RESULT.csv'

PATH_DATA_GROUPS_SCORES   = 'data/DATA_GROUPS_SCORES.csv'
PATH_DATA_GROUPS_FILTER   = 'data/DATA_GROUPS_FILTER.csv'
PATH_DATA_GROUPS_RESULT   = 'data/DATA_GROUPS_RESULT.csv'


# 1. Convert list to csv
df_ = convert_list_csv(HEADER[:-2], ROWS)
save_csv(df_, PATH_DATA_)
print_summary(read_csv(PATH_DATA_, COLUMNS_METADATA), COLUMNS_METADATA)
print_anomaly(read_csv(PATH_DATA_, COLUMNS_METADATA), COLUMNS_METADATA)


# 2. One-hot encoding
df_binary = create_df_binary(read_csv(PATH_DATA_, COLUMNS_METADATA), COLUMNS_METADATA)
df_rares  = filter_rare_features(df_binary, COLUMNS_METADATA, MIN_FREQ)
save_csv(df_rares, PATH_DATA_BINARY)
print_summary(read_csv(PATH_DATA_BINARY), COLUMNS_METADATA)


# 3. Calculate k-mean
plot_k_means(PATH_PLOT, ELOS, K_MAX, RANDOM_STATE)


# 4. Clustering
df_cluster = create_df_cluster(read_csv(PATH_DATA_BINARY), ELOS, K, RANDOM_STATE)
save_csv(df_cluster, PATH_DATA_CLUSTER)
print_summary(read_csv(PATH_DATA_CLUSTER), COLUMNS_METADATA)
print_cluster_range(read_csv(PATH_DATA_CLUSTER))


# 5. Split dataset
X_train, X_test, y_train, y_test = split_dataset(
    df           = read_csv(PATH_DATA_CLUSTER), 
    test_size    = TEST_SIZE, 
    random_state = RANDOM_STATE, 
    column_drop  = ['elo', 'cluster'], 
    column_label = 'cluster'
)


# 6.1. Compute features score
df_rank_scores = compute_feature_scores(X_train, y_train)
save_csv(df_rank_scores, PATH_DATA_FEATURES_SCORES)

print_scores(
    df             = read_csv(PATH_DATA_FEATURES_SCORES), 
    columns        = ['feature', 'f_score', 'p_value', 'frequency'],
    sort_by        = None,
    threshold_f    = 1,
    threshold_p    = None,
    threshold_freq = None,
    top_n          = None,
)


# 6.2. Filter features columns
column_keep_features = [
    'sf_visualization', 
    'sf_reconstruction', 
    'hst_sub_architectural_asset', 
    'hst_sub_artifact',
    'hst_sub_fortification',
    'platform_vr',
    'platform_ar',
    'device_hmd',
    'device_pc',
    'tech_image_based',
    'tech_geospatial',
    'tech_sub_photogrammetry',
    'tech_sub_sfm',
    'sd_agisoft_metashape',
    'sd_leica_cyclone',
    'sm_autodesk_3ds_max',
    'sr_unity',
] + [
    'elo',
    'cluster',
]
df_filter = keep_columns_csv(read_csv(PATH_DATA_CLUSTER), COLUMNS_METADATA, column_keep_features)
save_csv(df_filter, PATH_DATA_FEATURES_FILTER)
print_summary(read_csv(PATH_DATA_FEATURES_FILTER), COLUMNS_METADATA)


# 6.3. Run models for features
X_train, X_test, y_train, y_test = split_dataset(
    df           = read_csv(PATH_DATA_FEATURES_FILTER), 
    test_size    = TEST_SIZE, 
    random_state = RANDOM_STATE, 
    column_drop  = ['elo', 'cluster'], 
    column_label = 'cluster'
)
results = evaluate_models(X_train, X_test, y_train, y_test)
df_results = convert_list_csv(['model', 'accuracy', 'time'], results)
save_csv(df_results, PATH_DATA_FEATURES_RESULT)

print_models(
    df      = read_csv(PATH_DATA_FEATURES_RESULT),
    columns = ['model','accuracy','time'],
    sort_by = 'accuracy',
)




# 7.1. Compute groups score
df_rank_groups = aggregate_groups(df_rank_scores, COLUMNS_METADATA)
save_csv(df_rank_groups, PATH_DATA_GROUPS_SCORES)

print_scores(
    df             = read_csv(PATH_DATA_GROUPS_SCORES),
    columns        = ['feature', 'f_score_mean', 'p_value_mean', 'frequency_total'],
    sort_by        = None,
    threshold_f    = 1,
    threshold_p    = None,
    threshold_freq = None,
    top_n          = None,
)


# 7.2. Filter groups columns
column_keep_groups = [
    'study_focus', 
    'platform', 
    'device', 
    'technique', 
    'software_data', 
    'software_render',
] + [
    'elo',
    'cluster',
]
df_filter = keep_columns_csv(read_csv(PATH_DATA_CLUSTER), COLUMNS_METADATA, column_keep_groups)
save_csv(df_filter, PATH_DATA_GROUPS_FILTER)
print_summary(read_csv(PATH_DATA_GROUPS_FILTER), COLUMNS_METADATA)


# 7.3. Run models for groups
X_train, X_test, y_train, y_test = split_dataset(
    df           = read_csv(PATH_DATA_GROUPS_FILTER), 
    test_size    = TEST_SIZE, 
    random_state = RANDOM_STATE, 
    column_drop  = ['elo', 'cluster'], 
    column_label = 'cluster'
)
results = evaluate_models(X_train, X_test, y_train, y_test)
df_results = convert_list_csv(['model', 'accuracy', 'time'], results)
save_csv(df_results, PATH_DATA_GROUPS_RESULT)

print_models(
    df      = read_csv(PATH_DATA_GROUPS_RESULT),
    columns = ['model','accuracy','time'],
    sort_by = 'accuracy',
)

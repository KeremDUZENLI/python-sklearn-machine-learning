def print_df_scores(df):
    rows = [(row['feature'], row['f_score'], row['p_value'], int(row['frequency']))
            for _, row in df.iterrows()]

    feat_w = max(len(feat) for feat, *_ in rows + [('Feature',)]) + 2
    f_w    = max(len(f"{f:0.2f}") for _, f, _, _ in rows + [(None, 0.0,0,0)]) + 2
    p_w    = max(len(f"{p:0.3f}") for *_, p, _ in rows + [(None,0.0,0.0,0)]) + 2
    freq_w = max(len(str(freq)) for *_, freq in rows + [(None,0.0,0.0,0,0)]) + 2

    header = (f"{'Feature':<{feat_w}} | "
              f"{'F-score':>{f_w}} | "
              f"{'p-value':>{p_w}} | "
              f"{'Freq':>{freq_w}}")
    separator = '─' * len(header)

    print("\n" + header)
    print(separator)

    for feat, f_score, p_value, freq in rows:
        print(f"{feat:<{feat_w}} | "
              f"{f_score:>{f_w}.2f} | "
              f"{p_value:>{p_w}.3f} | "
              f"{freq:>{freq_w}d}")


def print_df_scores_top_n(df, top_n):   
    df_top = df.nlargest(top_n, 'f_score')[['feature','f_score']]
    rows = [(row.feature, row.f_score) for row in df_top.itertuples()]

    feat_w = max(len(feat) for feat, _ in rows + [('Feature', '')]) + 2
    f_w    = max(len(f"{f:0.2f}") for _, f in rows + [(None, 0.0)]) + 2

    header = f"{'Feature':<{feat_w}} | {'F-score':>{f_w}}"
    separator = '─' * len(header)

    print(f"\nTop {top_n} features by F-score:")
    print(header)
    print(separator)

    for feat, f_score in rows:
        print(f"{feat:<{feat_w}} | {f_score:>{f_w}.2f}")


def print_summary_cluster(df, k):
    print(f"\n=== cluster_{k} ===")
    summary = df.groupby('cluster')['elo'].agg(['min', 'max', 'count'])
    
    for cluster_name, row in summary.iterrows():
        print(f"{cluster_name}: min={row['min']}, max={row['max']}, {row['count']} items")
          

def print_summary(df, columns_metadata=None):
    total_rows = len(df)

    if isinstance(columns_metadata, dict):
        if all(isinstance(v, tuple) for v in columns_metadata.values()):
            for column, (label_map, is_list) in columns_metadata.items():
                if column not in df.columns:
                    continue
                rows = _get_summary_rows(df, label_map, column, is_list)
                _print_table(f"{column} ({total_rows} rows)", rows)

        else:
            for group_name, prefix in columns_metadata.items():
                other_prefixes = [
                    p for k, p in columns_metadata.items()
                    if k != group_name and p.startswith(prefix)
                ]

                selected_columns = [
                    col for col in df.columns
                    if col.startswith(prefix) and not any(col.startswith(p) for p in other_prefixes)
                ]

                if not selected_columns:
                    continue

                rows = _get_summary_rows_binary(df, selected_columns)
                _print_table(f"{group_name} ({total_rows} rows)", rows)


def _print_table(title, rows):
    print(f"\n=== {title} ===")
    
    if not rows:
        print("NO DATA")
        return

    label_width = max(len(label) for label, _, _ in rows) + 2
    count_width = max(len(str(count)) for _, count, _ in rows) + 2
    percent_width = len("Percent (%)") + 2

    print(f"{'Category':<{label_width}} | {'Count':>{count_width}} | {'Percent (%)':>{percent_width}}")
    print('─' * (label_width + count_width + percent_width + 6))

    for label, count, percent in rows:
        print(f"{label:<{label_width}} |  {count:<{count_width}} | {percent:<{percent_width}.2f}")


def _get_summary_rows(df, label_map, column, is_list):
    rows = []
    for _, label in label_map.items():
        count = df[column].apply(lambda x: label in x if is_list else x == label).sum()
        percent = (count / len(df)) * 100
        rows.append((label, count, percent))
    return rows


def _get_summary_rows_binary(df, columns):
    total_rows = len(df)
    return [
        (col, df[col].sum(), (df[col].sum() / total_rows) * 100)
        for col in columns
    ]


# def print_summary(df, columns_metadata=None):
#     total_rows = len(df)

#     if isinstance(columns_metadata, dict) and all(
#         isinstance(v, tuple) for v in columns_metadata.values()
#     ):
#         for column, (mapping, is_list) in columns_metadata.items():
#             if column not in df.columns:
#                 continue
#             rows = _get_summary_rows(df, mapping, column, is_list)
#             _print_table(f"{column} ({total_rows} rows)", rows)

#     elif isinstance(columns_metadata, dict):
#         columns_group = columns_metadata

#         for group_name, prefix in columns_group.items():
#             other_prefixes = [p for k, p in columns_group.items() if k != group_name and p.startswith(prefix)]
#             one_hot_cols = [
#                 column for column in df.columns
#                 if column.startswith(prefix) and not any(column.startswith(p) for p in other_prefixes)
#             ]

#             if not one_hot_cols:
#                 continue

#             rows = _get_binary_summary_rows(df, one_hot_cols)
#             _print_table(f"{group_name} ({total_rows} rows)", rows)


# def _get_summary_rows(df, mapping, column, is_list):
#     rows = []
#     for _, label in mapping.items():
#         count = df[column].apply(lambda x: label in x if is_list else x == label).sum()
#         percent = count / len(df) * 100
#         rows.append((label, count, percent))
#     return rows


# def _get_binary_summary_rows(df, columns):
#     rows = []
#     total_rows = len(df)
#     for column in columns:
#         count = df[column].sum()
#         percent = count / total_rows * 100
#         rows.append((column, count, percent))
#     return rows


# def _print_table(title, rows):
#     print(f"\n=== {title} ===")
    
#     if not rows:
#         print("NO DATA")
#         return

#     label_width = max(len(label) for label, _, _ in rows) + 2
#     count_width = max(len(str(count)) for _, count, _ in rows) + 2
#     percent_width = len("Percent (%)") + 2

#     print(f"{'Category':<{label_width}} | {'Count':>{count_width}} | {'Percent (%)':>{percent_width}}")
#     print('─' * 100)

#     for label, count, percent in rows:
#         print(f"{label:<{label_width}} |  {count:<{count_width}.0f} | {percent:<{percent_width}.2f}")

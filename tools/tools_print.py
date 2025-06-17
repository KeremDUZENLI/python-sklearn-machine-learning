def print_summary(df, columns_metadata=None):
    total_rows = len(df)
    headers = ["Category", "Count", "Percent (%)"]

    if isinstance(columns_metadata, dict):
        if all(isinstance(v, tuple) for v in columns_metadata.values()):
            for column, (label_map, is_list) in columns_metadata.items():
                if column not in df.columns:
                    continue
                title = f"{column} ({total_rows} rows)"
                rows = _get_summary_rows(df, label_map, column, is_list)
                _print_table(title, headers, rows)

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

                title = f"{group_name} ({total_rows} rows)"
                rows = _get_summary_rows_binary(df, selected_columns)
                _print_table(title, headers, rows)


def print_summary_cluster(df, k):
    print(f"\n=== cluster_{k} ===")
    summary = df.groupby('cluster')['elo'].agg(['min', 'max', 'count'])
    
    for cluster_name, row in summary.iterrows():
        print(f"{cluster_name}: min={row['min']} | max={row['max']} | {row['count']} items")


def print_df_scores(df, top_n=None):
    if top_n:
        subset = df.nlargest(top_n, 'f_score')
        title  = f"Top {top_n} features by F-score:"
    else:
        subset = df
        title  = "All features by F-score:"

    rows = []
    for _, r in subset.iterrows():
        rows.append((
            r['feature'],
            f"{r['f_score']:.2f}",
            f"{r['p_value']:.3f}",
            int(r['frequency'])
        ))

    headers = ["Feature", "F-score", "p-value", "Freq"]
    _print_table(title, headers, rows)
    

def _print_table(title, headers, rows):
    widths = _compute_column_widths(headers, rows)
    header_line = " | ".join(headers[i].ljust(widths[i]) for i in range(len(headers)))
    separator = '─' * len(header_line)

    print(f"\n{title}")
    print(header_line)
    print(separator)
    for row in rows:
        line = []
        for i, cell in enumerate(row):
            cell_str = str(cell)
            line.append(cell_str.ljust(widths[i]))
        print(" | ".join(line))


def _get_summary_rows(df, label_map, column, is_list):
    rows = []
    for _, label in label_map.items():
        count = df[column].apply(lambda x: label in x if is_list else x == label).sum()
        percent = round((count / len(df)) * 100, 2)
        rows.append((label, count, percent))
    return rows


def _get_summary_rows_binary(df, columns):
    total_rows = len(df)
    rows = []
    for col in columns:
        count   = df[col].sum()
        percent = round((count / total_rows) * 100, 2)
        rows.append((col, count, percent))
    return rows


def _compute_column_widths(headers, rows):
    col_widths = [len(h) for h in headers]
    for row in rows:
        for i, cell in enumerate(row):
            col_widths[i] = max(col_widths[i], len(str(cell)))
    return [w + 2 for w in col_widths]

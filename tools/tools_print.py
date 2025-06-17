def print_summary(df, columns_metadata=None):
    header = ["Category", "Count", "Percent (%)"]

    if not isinstance(columns_metadata, dict):
        return
    
    first_val = next(iter(columns_metadata.values()))
    if isinstance(first_val, tuple):
        for column_name, (label_map, is_list) in columns_metadata.items():
            if column_name not in df.columns:
                continue
            rows = _get_summary_rows(df, label_map, column_name, is_list)
            _print_table(column_name, header, rows)
    else:
        for group_name, prefix in columns_metadata.items():
            other_prefixes = [
                p for k, p in columns_metadata.items()
                if k != group_name
            ]
            selected = [
                col for col in df.columns
                if col.startswith(prefix)
                and not any(col.startswith(op) for op in other_prefixes)
            ]
            if not selected:
                continue

            rows = _get_summary_rows(df, binary_columns=selected)
            _print_table(group_name, header, rows)


def print_summary_cluster(df, k=None):
    print(f"\n=== cluster_{k} ===")
    summary = df.groupby('cluster')['elo'].agg(['min', 'max', 'count'])
    
    for cluster_name, row in summary.iterrows():
        print(f"{cluster_name}: min={row['min']} | max={row['max']} | {row['count']} items")


def print_df_scores(df, columns_group=None, top_n=None):
    header = ["Feature", "F-score", "P-value", "Frequency"]

    if top_n:
        session   = f"Top {top_n} features by F-score"
        top_feats = set(df.nlargest(top_n, 'f_score')['feature'])
        working   = df[df['feature'].isin(top_feats)]
    else:
        session = "All features by F-score"
        working = df
    print(f"\n\n\n======================== {session} ========================", end="")

    if not columns_group:
        rows = _get_score_rows(
            working,
            ["feature", "f_score", "p_value", "frequency"]
        )
        _print_table("", header, rows)
        return

    for group_name, prefix in columns_group.items():
        grp_df = working[working['feature'].str.startswith(prefix)]
        if grp_df.empty:
            continue
        rows = []
        for _, r in grp_df.iterrows():
            rows.append((
                r['feature'],
                f"{r['f_score']:.2f}",
                f"{r['p_value']:.3f}",
                int(r['frequency'])
            ))
        _print_table(group_name, header, rows)
    

def print_df_scores_group(df, columns_group=None, top_n=None):
    header = ["Feature", "F-score", "P-value", "Frequency"]

    if top_n:
        session = f"Top {top_n} groups by mean F-score"
        working = df.head(top_n)
    else:
        session = "All groups by mean F-score"
        working = df
    print(f"\n\n\n======================== {session} ========================", end="")

    rows = []
    if not columns_group:
        rows = _get_score_rows(
            working,
            ["feature", "f_score_mean", "p_value_mean", "frequency_total"]
        )
    else:
        subset = working[working['feature'].isin(columns_group)]
        rows = _get_score_rows(
            subset,
            ["feature", "f_score_mean", "p_value_mean", "frequency_total"]
        )

    _print_table("", header, rows)


def _print_table(title, header, rows):
    widths = _compute_column_widths(header, rows)
    header_line = " | ".join(header[i].ljust(widths[i]) for i in range(len(header)))
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


def _get_summary_rows(df, label_map=None, column=None, is_list=False, binary_columns=None):
    rows = []
    total = len(df)

    if binary_columns:
        for col in binary_columns:
            count = df[col].sum()
            percent = round(count / total * 100, 2)
            rows.append((col, count, percent))

    elif label_map and column:
        for _, label in label_map.items():
            if is_list:
                count = df[column].apply(lambda x: label in x).sum()
            else:
                count = (df[column] == label).sum()
            percent = round(count / total * 100, 2)
            rows.append((label, count, percent))

    return rows


def _get_score_rows(df, columns):
    rows = []
    for _, r in df.iterrows():
        row = []
        for col in columns:
            val = r[col]
            if isinstance(val, float):
                if "p_value" in col:
                    row.append(f"{val:.3f}")
                else:
                    row.append(f"{val:.2f}")
            elif isinstance(val, int):
                row.append(str(val))
            else:
                row.append(str(val))
        rows.append(tuple(row))
    return rows


def _compute_column_widths(headers, rows):
    col_widths = [len(h) for h in headers]
    for row in rows:
        for i, cell in enumerate(row):
            col_widths[i] = max(col_widths[i], len(str(cell)))
    return [w + 2 for w in col_widths]

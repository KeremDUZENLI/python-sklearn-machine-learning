from tests.verifier import check_anomaly

         
def print_anomaly(df, columns_metadata):
    _print_title("Config vs Data Features")
    header = ["issue"]
    anomalies = check_anomaly(df, columns_metadata)
    
    if not anomalies:
        print("\nNO ANOMALIES\n")
        return

    for column, features in anomalies.items():
        rows = [[feature] for feature in features]
        _print_table(column, header, rows)


def print_summary(df, columns_metadata):
    _print_title("Summary of the Dataset")
    header = ["category", "count", "percent"]

    total = len(df)
    for column, (mapping, is_list) in columns_metadata.items():
        rows = []

        if column in df.columns:
            for label in mapping.values():
                count = df[column].apply(lambda x: label in x).sum() if is_list else (df[column] == label).sum()
                rows.append((label, count, round(count / total * 100, 2)))
        else:
            for column_binary in mapping:
                if column_binary in df.columns:
                    count = df[column_binary].sum()
                    rows.append((column_binary, count, round(count / total * 100, 2)))

        if rows:
            _print_table(column, header, rows)


def print_cluster_range(df, k=None):
    _print_title(f"cluster{k or ''}")
    print()

    summary = df.groupby('cluster')['elo'].agg(['min', 'max', 'count'])
    for cluster, row in summary.iterrows():
        print(f"{cluster}: min={row['min']} | max={row['max']} | {row['count']} items")


def print_scores(df, columns, sort_by=None, threshold_f=None, threshold_p=None, threshold_freq=None, top_n=None):    
    _print_title(f"Top items sort by {sort_by}" if top_n else "All features")
    
    if sort_by:
        df = df.sort_values(by=sort_by, ascending=False)
        
    if threshold_f:
        column_f = columns[1]
        df = df[df[column_f] >= threshold_f]

    if threshold_p:
        column_filter = columns[2]
        df = df[df[column_filter] <= threshold_p]

    if threshold_freq:
        column_freq = columns[3]
        df = df[df[column_freq] >= threshold_freq]

    if top_n:
        df = df.head(top_n)

    rows = _get_rows_score(df, columns)
    _print_table("", columns, rows)

    
def print_models(df, columns, sort_by=None):
    _print_title("Model Evaluation Results")

    if sort_by:
        df = df.sort_values(by=sort_by, ascending=False)

    rows = _get_rows_score(df, columns)
    _print_table("", columns, rows)


def _get_rows_score(df, columns):
    rows = []
    for _, row in df.iterrows():
        formatted = []
        for col in columns:
            val = row[col]
            if isinstance(val, float):
                formatted.append(f"{val:.2f}")
            else:
                formatted.append(str(val))
        rows.append(tuple(formatted))
    return rows


def _print_table(title, header, rows):
    col_widths = _compute_column_width(header, rows)
    header_line = " | ".join(header[i].ljust(col_widths[i]) for i in range(len(header)))
    
    print(f"\n{title}")
    print(header_line)
    print("─" * len(header_line))
    for row in rows:
        line = " | ".join(str(cell).ljust(col_widths[i]) for i, cell in enumerate(row))
        print(line)


def _compute_column_width(headers, rows):
    widths = [len(h) for h in headers]
    for row in rows:
        for i, cell in enumerate(row):
            widths[i] = max(widths[i], len(str(cell)))
    return [w + 2 for w in widths]


def _print_title(title):
    print(f"\n\n\n================== {title} ==================", end="")

def print_summary(df, columns_metadata):
    header = ["Category", "Count", "Percent (%)"]

    for group_name, (mapping, is_list) in columns_metadata.items():
        if is_list:
            columns_binary = [col for col in mapping.keys() if col in df.columns]
            if not columns_binary:
                continue
            rows = _get_rows_summary(df, columns_binary=columns_binary)
        else:
            if group_name not in df.columns:
                continue
            rows = _get_rows_summary(df, column_order=mapping, column_name=group_name, is_list=False)

        _print_table(group_name, header, rows)
     

def print_cluster_range(df, k=None):
    print(f"\n=== cluster_{k or ''} ===")
    summary = df.groupby('cluster')['elo'].agg(['min', 'max', 'count'])
    for cluster, row in summary.iterrows():
        print(f"{cluster}: min={row['min']} | max={row['max']} | {row['count']} items")

   
def print_scores(df, columns, sort_by=None, threshold_p=None, threshold_freq=None, top_n=None):
    title = f"Top items sort by {sort_by}" if top_n else "All features"
    print(f"\n\n\n================== {title} ==================", end="")
    
    if sort_by:
        df = df.sort_values(by=sort_by, ascending=False)

    if threshold_p:
        column_filter = columns[-2]
        df = df[df[column_filter] <= threshold_p]

    if threshold_freq:
        column_freq = columns[-1]
        df = df[df[column_freq] >= threshold_freq]

    if top_n:
        df = df.head(top_n)

    rows = _get_rows_score(df, columns)
    _print_table("", columns, rows)
       
        
def print_models(results):
    title = "Model Evaluation Results"
    print(f"\n\n\n================== {title} ==================", end="")

    header = ['Model', 'Accuracy (%)', 'Time (s)']
    rows   = [(name, f"{acc:.3f}", f"{elapsed:.3f}") for name, acc, elapsed in results]
    _print_table("", header, rows)


def _get_rows_summary(df, column_order=None, column_name=None, is_list=False, columns_binary=None):
    total = len(df)
    
    rows = []
    if columns_binary:
        for col in columns_binary:
            count = df[col].sum()
            percent = round(count / total * 100, 2)
            rows.append((col, count, percent))

    elif column_order and column_name:
        for _, label in column_order.items():
            if is_list:
                count = df[column_name].apply(lambda x: label in x).sum()
            else:
                count = (df[column_name] == label).sum()
            percent = round(count / total * 100, 2)
            rows.append((label, count, percent))
            
    return rows


def _get_rows_score(df, columns):
    rows = []
    for _, row in df.iterrows():
        formatted = []
        for col in columns:
            val = row[col]
            if isinstance(val, float):
                formatted.append(f"{val:.3f}" if "p_value" in col else f"{val:.2f}")
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

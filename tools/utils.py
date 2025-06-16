def print_summary(df, columns_metadata):
    total_rows = len(df)

    for column, (mapping, is_list) in columns_metadata.items():
        if column not in df.columns:
            continue

        rows = []
        for _, label in mapping.items():
            if is_list:
                count = df[column].apply(lambda items: label in items).sum()
            else:
                count = (df[column] == label).sum()
                
            percent = count / total_rows * 100
            rows.append((label, count, percent))

        _print_table(f"{column} ({total_rows} rows)", rows)


def _print_table(title, rows):
    if not rows:
        print(f"\n=== {title} ===")
        print("NO DATA")
        return

    label_width = max(len(label) for label, _, _ in rows) + 2
    count_width = max(len(str(count)) for _, count, _ in rows) + 2
    percent_width = len("Percent (%)") + 2

    print(f"\n=== {title} ===")
    print(f"{'Category':<{label_width}} | {'Count':>{count_width}} | {'Percent (%)':>{percent_width}}")
    print('─' * 100)

    for label, count, percent in rows:
        print(f"{label:<{label_width}} |  {count:<{count_width}.0f} | {percent:<{percent_width}.2f}")

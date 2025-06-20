def check_anomaly(df, columns_metadata):
    anomalies = {}
    list_cols = [col for col, (_, is_list) in columns_metadata.items() if is_list]

    for col in list_cols:
        if col not in df.columns:
            anomalies[col] = ["[Missing column]"]
            continue

        valid_values = set(columns_metadata[col][0].values())
        found = {item for row in df[col] for item in row}
        unexpected = sorted(found - valid_values)
        if unexpected:
            anomalies[col] = unexpected

    return anomalies

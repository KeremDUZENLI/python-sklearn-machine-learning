import json, csv
import pandas as pd


def convert_list_csv(path_output, header, rows):
    with open(path_output, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(header)
        for row in rows:
            serialized_row = [_serialize(cell) for cell in row]
            writer.writerow(serialized_row)


def save_csv(df, path_output, k=None):
    filename = f"{path_output}_{k}.csv" if k is not None else path_output
    df.to_csv(filename, index=False, encoding='utf-8')


def read_csv(path_input, columns_metadata=None):
    df = pd.read_csv(path_input)

    if columns_metadata:
        for column, (_, is_list) in columns_metadata.items():
            if is_list and column in df.columns:
                df[column] = df[column].fillna('[]').apply(_parse)
    return df


def keep_columns_csv(df, columns_metadata, columns_keep):
    keep_columns = []           
    for key in columns_keep:
        if key in df.columns:
            keep_columns.append(key)
        if key in columns_metadata:
            mapping, _ = columns_metadata[key]
            for column in mapping:
                if column in df.columns:
                    keep_columns.append(column)

    keep_columns = list(dict.fromkeys(keep_columns))
    return df[keep_columns]


def drop_columns_csv(df, columns_metadata, columns_drop):           
    drop_columns = []
    for key in columns_drop:
        if key in df.columns:
            drop_columns.append(key)
        if key in columns_metadata:
            mapping, _ = columns_metadata[key]
            for column in mapping:
                if column in df.columns:
                    drop_columns.append(column)

    drop_columns = list(dict.fromkeys(drop_columns))
    return df.drop(columns=drop_columns, errors='ignore')


def _serialize(cell):
    return json.dumps(cell, ensure_ascii=False) if isinstance(cell, list) else cell


def _parse(cell):
    try:
        data = json.loads(cell)
        return data if isinstance(data, list) else []
    except json.JSONDecodeError:
        return []

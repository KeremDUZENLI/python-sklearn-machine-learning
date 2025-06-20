import json
import pandas as pd

          
def convert_list_csv(header, rows):
    serialized_rows = [[_serialize(cell) for cell in row] for row in rows]
    return pd.DataFrame(serialized_rows, columns=header)


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


def keep_columns_csv(df, columns_metadata, column_keep):
    keep = []           
    for key in column_keep:
        if key in df.columns:
            keep.append(key)
        if key in columns_metadata:
            mapping, _ = columns_metadata[key]
            for column in mapping:
                if column in df.columns:
                    keep.append(column)

    keep = list(dict.fromkeys(keep))
    return df[keep]


def drop_columns_csv(df, columns_metadata, column_drop):           
    drop = []
    for key in column_drop:
        if key in df.columns:
            drop.append(key)
        if key in columns_metadata:
            mapping, _ = columns_metadata[key]
            for column in mapping:
                if column in df.columns:
                    drop.append(column)

    drop = list(dict.fromkeys(drop))
    return df.drop(columns=drop, errors='ignore')


def _serialize(cell):
    return json.dumps(cell, ensure_ascii=False) if isinstance(cell, list) else cell


def _parse(cell):
    try:
        data = json.loads(cell)
        return data if isinstance(data, list) else []
    except json.JSONDecodeError:
        return []

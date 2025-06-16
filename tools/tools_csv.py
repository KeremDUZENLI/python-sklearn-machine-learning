import json, csv
import pandas as pd


def create_csv(path_output, header, rows):
    with open(path_output, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(header)
        for row in rows:
            serialized_row = [_serialize(cell) for cell in row]
            writer.writerow(serialized_row)


def read_csv(path_input, columns_metadata=None):
    df = pd.read_csv(path_input, dtype=str)
    if columns_metadata:
        for column, (_, is_list) in columns_metadata.items():
            if is_list and column in df.columns:
                df[column] = df[column].fillna('[]').apply(_parse)
    return df


def _serialize(cell):
    return json.dumps(cell, ensure_ascii=False) if isinstance(cell, list) else cell


def _parse(cell):
    try:
        data = json.loads(cell)
        return data if isinstance(data, list) else []
    except json.JSONDecodeError:
        return []

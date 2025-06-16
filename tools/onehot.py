import pandas as pd


def create_csv_onehot(df, path_output, columns_onehot, columns_metadata):
    for column, (mapping, is_list) in columns_metadata.items():
        if column in df.columns:
            df = _create_rows_onehot(df, column, mapping, is_list)

    df_final = _keep_ordered_columns(df, columns_onehot)
    df_final.to_csv(path_output, index=False, encoding='utf-8')

def _create_rows_onehot(df, column, mapping, is_list=True):
    flags = {}
    for column_flag, label in mapping.items():
        if is_list:
            flags[column_flag] = df[column].apply(lambda lst: int(label in lst))
        else:
            flags[column_flag] = df[column].apply(lambda x: int(x == label))
    return pd.concat([df, pd.DataFrame(flags, index=df.index)], axis=1)

def _keep_ordered_columns(df, columns_onehot):
    return df[[column for column in columns_onehot if column in df.columns]]

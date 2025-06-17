import pandas as pd


def create_df_binary(df, columns_metadata, columns_onehot=None):
    for column, (mapping, is_list) in columns_metadata.items():
        if column in df.columns:
            df = _create_rows_onehot(df, column, mapping, is_list)

    if columns_onehot:
        df = _keep_ordered_columns(df, columns_onehot)

    return df


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

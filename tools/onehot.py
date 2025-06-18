import pandas as pd


def create_df_binary(df, column_order):
    for column, (mapping, is_list) in column_order.items():
        if column in df.columns:
            df = _create_rows_onehot(df, column, mapping, is_list)

    ordered_cols = []
    for column, (mapping, _) in column_order.items():
        ordered_cols.extend([flag for flag in mapping.keys() if flag in df.columns])

    return df[ordered_cols]


def _create_rows_onehot(df, column, mapping, is_list=True):
    flags = {}
    for column_flag, label in mapping.items():
        if is_list:
            flags[column_flag] = df[column].apply(lambda lst: int(label in lst))
        else:
            flags[column_flag] = df[column].apply(lambda x: int(x == label))
    return pd.concat([df, pd.DataFrame(flags, index=df.index)], axis=1)

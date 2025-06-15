import json
import pandas as pd
from config.config import STUDY_FOCUS_MAP, HISTORICAL_SITE_TYPE_MAP, HISTORICAL_SITE_TYPE_SUB_MAP, PLATFORM_MAP, DEVICE_MAP, TECHNIQUE_MAP, TECHNIQUE_SUB_MAP, SOFTWARE_DATA_MAP, SOFTWARE_MODELING_MAP, SOFTWARE_RENDER_MAP, COLUMN_MAP


SOURCE = 'data/DATA.csv'
OUTPUT = 'data/DATA_onehot.csv'
PARSE_COLUMNS = [
    # 'id', 'order', 'year', 'country',
    # 'study_focus', 'historical_site_type', 'historical_site_type_sub',
    'platform', 'device', 'technique', 'technique_sub',
    'software_data', 'software_modeling', 'software_render',
]

def parse_json(cell):
    try:
        parsed = json.loads(cell)
        if isinstance(parsed, list):
            return parsed
    except Exception:
        pass
    return []

def load_csv(path):
    df = pd.read_csv(path, dtype=str)
    for col in PARSE_COLUMNS:
        if col in df.columns:
            df[col] = df[col].fillna('[]').apply(parse_json)
    return df

def onehot(df, column, mapping, is_list=True):
    flags = {}
    for flag_col, target in mapping.items():
        if is_list:
            flags[flag_col] = df[column].apply(lambda lst: int(target in lst))
        else:
            flags[flag_col] = df[column].apply(lambda x: int(x == target))

    return pd.concat([df, pd.DataFrame(flags, index=df.index)], axis=1)

def organise_columns(df):
    return df[[c for c in COLUMN_MAP if c in df.columns]]


df = load_csv(SOURCE)
df = onehot(df , 'study_focus'              , STUDY_FOCUS_MAP              , False)
df = onehot(df , 'historical_site_type'     , HISTORICAL_SITE_TYPE_MAP     , False)
df = onehot(df , 'historical_site_type_sub' , HISTORICAL_SITE_TYPE_SUB_MAP , False)
df = onehot(df , 'platform'                 , PLATFORM_MAP)
df = onehot(df , 'device'                   , DEVICE_MAP)
df = onehot(df , 'technique'                , TECHNIQUE_MAP)
df = onehot(df , 'technique_sub'            , TECHNIQUE_SUB_MAP)
df = onehot(df , 'software_data'            , SOFTWARE_DATA_MAP)
df = onehot(df , 'software_modeling'        , SOFTWARE_MODELING_MAP)
df = onehot(df , 'software_render'          , SOFTWARE_RENDER_MAP)
df_final = organise_columns(df)

df_final.to_csv(OUTPUT, index=False, encoding='utf-8')

import json
import pandas as pd

from config.config import (
    STUDY_FOCUS_MAP,
    HISTORICAL_SITE_TYPE_MAP,
    HISTORICAL_SITE_TYPE_SUB_MAP,
    PLATFORM_MAP,
    DEVICE_MAP,
    TECHNIQUE_MAP,
    TECHNIQUE_SUB_MAP,
    SOFTWARE_DATA_MAP,
    SOFTWARE_MODELING_MAP,
    SOFTWARE_RENDER_MAP,
)

SOURCE = 'data/DATA.csv'

GROUPS = {
    'study_focus'              : (STUDY_FOCUS_MAP,              False),
    'historical_site_type'     : (HISTORICAL_SITE_TYPE_MAP,     False),
    'historical_site_type_sub' : (HISTORICAL_SITE_TYPE_SUB_MAP, False),
    'platform'                 : (PLATFORM_MAP,                 True),
    'device'                   : (DEVICE_MAP,                   True),
    'technique'                : (TECHNIQUE_MAP,                True),
    'technique_sub'            : (TECHNIQUE_SUB_MAP,            True),
    'software_data'            : (SOFTWARE_DATA_MAP,            True),
    'software_modeling'        : (SOFTWARE_MODELING_MAP,        True),
    'software_render'          : (SOFTWARE_RENDER_MAP,          True),
}

def parse_json(cell):
    try:
        lst = json.loads(cell)
        if isinstance(lst, list):
            return lst
    except:
        pass
    return []

df = pd.read_csv(SOURCE, dtype=str)
total = len(df)

# parse only the JSON‐list columns
for col, (_, is_list) in GROUPS.items():
    if is_list and col in df.columns:
        df[col] = df[col].fillna('[]').apply(parse_json)

for col, (mapping, is_list) in GROUPS.items():
    if col not in df.columns:
        continue

    # Gather counts & percents
    rows = []
    for key, label in mapping.items():
        if is_list:
            cnt = df[col].apply(lambda lst: label in lst).sum()
        else:
            cnt = (df[col] == label).sum()
        pct = cnt / total * 100
        rows.append((label, cnt, pct))

    # Compute column widths
    label_width = max(len(lbl) for lbl,_,_ in rows) + 2
    cnt_width   = max(len(str(cnt)) for _,cnt,_ in rows) + 2
    pct_width   = len("Percent") + 2

    # Header
    print(f"\n=== {col} ({total} rows) ===")
    hdr = f"{'Category':<{label_width}} | {'Count':>{cnt_width}} | {'Percent (%)':>{pct_width}}"
    print(hdr)
    print('─' * len(hdr))

    # Rows
    for label, cnt, pct in rows:
        print(f"{label:<{label_width}} |  {cnt:<{cnt_width}d} | {pct:<{pct_width}.2f}")

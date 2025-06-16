import pandas as pd
from env.schema    import GROUPS
from utils.utils   import load_csv


SOURCE = 'data/DATA.csv'

parse_columns = [col for col, (_, is_list) in GROUPS.items() if is_list]
df = load_csv(SOURCE, parse_columns)  

total = len(df)

for col, (mapping, is_list) in GROUPS.items():
    if col not in df.columns:
        continue

    rows = []
    for key, label in mapping.items():
        if is_list:
            cnt = df[col].apply(lambda lst: label in lst).sum()
        else:
            cnt = (df[col] == label).sum()
        pct = cnt / total * 100
        rows.append((label, cnt, pct))

    # formatting
    label_w = max(len(lbl) for lbl,_,_ in rows) + 2
    cnt_w   = max(len(str(cnt)) for _,cnt,_ in rows) + 2
    pct_w   = len("Percent") + 2

    print(f"\n=== {col} ({total} rows) ===")
    hdr = f"{'Category':<{label_w}} | {'Count':>{cnt_w}} | {'Percent (%)':>{pct_w}}"
    print(hdr)
    print('─' * len(hdr))
    for label, cnt, pct in rows:
        print(f"{label:<{label_w}} |  {cnt:<{cnt_w}d} | {pct:<{pct_w}.2f}")

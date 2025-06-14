import sys
import os
import csv, json

# ───────────────────────────────────────────────────────────
script_dir   = os.path.dirname(__file__)
project_root = os.path.abspath(os.path.join(script_dir, os.pardir))
if project_root not in sys.path:
    sys.path.insert(0, project_root)
# ───────────────────────────────────────────────────────────
  
from data.DATA import ROWS


OUTPUT_1 = 'data/DATA.csv'
OUTPUT_2 = 'data/DATA_elo.csv'
HEADER = [
    'id', 'order', 'year', 'country', 
    'study_focus', 'historical_site_type', 'historical_site_type_sub', 
    'platform', 'device', 'technique', 'technique_sub', 
    'software_data', 'software_modeling', 'software_render'
]

def serialize_cell(cell):
    if isinstance(cell, list):
        return json.dumps(cell, ensure_ascii=False)
    return cell

def merge_rows_with_elo(rows, elos):
    if len(rows) != len(elos):
        raise ValueError("ROWS and ELOS must be the same length")
    merged = []
    for row, elo in zip(rows, elos):
        merged.append(tuple(row) + (elo,))
    return merged

def write_csv(output_path, header, rows):
    with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(header)

        for row in rows:
            serialized_row = [serialize_cell(cell) for cell in row]
            writer.writerow(serialized_row)

write_csv(OUTPUT_1, HEADER, ROWS)

# with_elo = merge_rows_with_elo(ROWS, ELOS)
# write_csv(OUTPUT_2, HEADER, with_elo)

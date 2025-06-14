import csv, json
from data.DATA import ROWS


OUTPUT = 'data/DATA.csv'
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

def write_csv(output_path, header, rows):
    with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(header)

        for row in rows:
            serialized_row = [serialize_cell(cell) for cell in row]
            writer.writerow(serialized_row)

write_csv(OUTPUT, HEADER, ROWS)

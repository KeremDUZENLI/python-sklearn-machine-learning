import os
import json
import pandas as pd


SOURCE = 'data/DATA.csv'
OUTPUT = 'data/DATA_binary.csv'

def parse_json_list(cell):
    try:
        parsed = json.loads(cell)
        if isinstance(parsed, list):
            return parsed
    except Exception:
        pass
    return [] if pd.isna(cell) else [cell]


def load_data(path):
    df = pd.read_csv(path, dtype=str)
    HEADER = [
        'id', 'order', 'year', 'country', 
        'study_focus', 'historical_site_type', 'historical_site_type_sub', 
        'platform', 'device', 'technique', 'technique_sub', 
        'software_data', 'software_modeling', 'software_render'
    ]
    
    for column in HEADER:
        if column in df.columns:
            df[column] = df[column].apply(parse_json_list)

    return df

def add_techniques_sub_flags(df):
    subgroup_map = {
        'Sub_3D_Scanning': {
            'Laser Scanning', 'RGB-D Imaging', 'Real-Time Volumetric Capture'
        },
        'Sub_Image_Based_Techniques': {
            'Photogrammetry', 'Spherical Imaging', 'Image-Based Modelling (IBM)',
            'Structure from Motion (SfM)', 'UAV Aerial Imaging', 'Multi-View Stereo (MVS)'
        },
        'Sub_Geospatial_Techniques': {
            'Geographic Information System (GIS)', 'Global Navigation Satellite System (GNSS)',
            'Digital Elevation Models (DEM)', 'Visual-Inertial SLAM', 'Beacon Localization'
        },
        'Sub_Modeling_Reconstruction': {
            '3D Modeling', 'BIM (Building Information Modeling)',
            'HBIM (Historical Building Information Modeling)', 'Archaeological Data Integration',
            'Stratigraphic Mapping', 'Virtual Anastylosis'
        },
        'Sub_Data_Processing': {
            'Semantic Data Extraction', '3D Texturing',
            'Texture Mapping', 'Range-Based Modeling (RBM)', 'HDR Imaging'
        }
    }

    for column in subgroup_map:
        df[column] = 0

    for idx, subs in df['TechniqueSub'].items():
        present = set(subs)
        for col, members in subgroup_map.items():
            if present & members:
                df.at[idx, col] = 1
    return df

def one_hot_from_list(df, column, prefix):
    unique = set(x for cell in df[column] for x in cell)
    for item in unique:
        safe = item.replace(' ', '_').replace('-', '_').replace('(', '').replace(')', '')
        col = f"{prefix}_{safe}"
        df[col] = df[column].apply(lambda lst: int(item in lst))
    return df

def add_main_technique_flags(df):
    mains = [
        '3D_scanning', 'image_based_techniques',
        'geospatial_techniques', 'modeling', 'data_processing'
    ]
    for tech in mains:
        safe = tech.replace(' ', '_').replace('&', 'and')
        col = f"tech_{safe}"
        df[col] = df['technique'].apply(lambda lst: int(tech in lst))
    return df

def flatten_software_columns(df):
    for col in ['software_data', 'software_modeling', 'software_render']:
        if col in df.columns:
            df[col] = df[col].apply(lambda lst: ';'.join(lst))
    return df

def reorder_columns(df):
    first     = ['order','year','country','study_focus','historical_site_type','historical_site_type_sub']
    platform  = sorted([c for c in df if c.startswith('platform_')])
    device    = sorted([c for c in df if c.startswith('device_')])
    tech_main = sorted([c for c in df if c.startswith('tech_')])
    sub       = ['sub_3D_scanning','sub_image_based_techniques','sub_geospatial_techniques','sub_modeling','sub_data_processing']
    software  = ['software_data','software_modeling','software_render']

    cols = [c for c in first + platform + device + tech_main + sub + software if c in df.columns]
    return df[cols]

# 1) Load and parse
df = load_data(SOURCE)

# 2) Transformations
df = add_techniques_sub_flags(df)
df = one_hot_from_list(df, 'Platform', prefix='Platform')
df = one_hot_from_list(df, 'Device',   prefix='Device')
df = add_main_technique_flags(df)
df = flatten_software_columns(df)
df = reorder_columns(df)

# 3) Save out
os.makedirs(os.path.dirname(OUTPUT), exist_ok=True)
df.to_csv(OUTPUT, index=False, encoding='utf-8')
print(f"✅ Wrote {len(df)} rows to {OUTPUT}")

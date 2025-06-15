import json
import pandas as pd


SOURCE = 'data/DATA.csv'
OUTPUT = 'data/DATA_onehot.csv'
PARSE_COLUMNS = [
    'platform', 'device', 'technique', 'technique_sub',
    'software_data', 'software_modeling', 'software_render'
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

def onehot_study_focus(df):
    flag_map = {
        'study_focus_restoration'    : 'Restoration',
        'study_focus_visualization'  : 'Visualization',
        'study_focus_reconstruction' : 'Reconstruction',
    }
    for flag_col, value in flag_map.items():
        df[flag_col] = df['study_focus'].apply(lambda x: int(x == value))
    return df

def onehot_historical_site_type(df):
    flag_map = {
        'historical_site_type_archaeological_site' : 'Archaeological Site',
        'historical_site_type_artistic_feature'    : 'Artistic Feature',
        'historical_site_type_building'            : 'Building',
        'historical_site_type_natural_space'       : 'Natural Space',
    }
    for flag_col, value in flag_map.items():
        df[flag_col] = df['historical_site_type'].apply(lambda x: int(x == value))
    return df

def onehot_historical_site_type_sub(df):
    flag_map = {
        'hst_sub_landbased'    : 'LandBased',
        'hst_sub_underwater'   : 'Underwater',
        
        'hst_sub_architectural_asset' : 'ArchitecturalAsset',
        'hst_sub_artifact'            : 'Artifact',
        
        'hst_sub_fortification' : 'Fortification',
        'hst_sub_religious'     : 'Religious',
        'hst_sub_urbanspace'    : 'UrbanSpace',
        
        'hst_sub_cave'          : 'Cave',
    }
    for flag_col, value in flag_map.items():
        df[flag_col] = df['historical_site_type_sub'].apply(lambda x: int(x == value))
    return df


def onehot_platform(df):
    flag_map = {
        'platform_vr' : 'VR',
        'platform_ar' : 'AR',
        'platform_mr' : 'MR',
        'platform_xr' : 'XR',
    }
    for flag_col, value in flag_map.items():
        df[flag_col] = df['platform'].apply(lambda lst: int(value in lst))
    return df

def onehot_device(df):
    flag_map = {
        'device_hmd'               : 'HMD',
        'device_pc'                : 'PC',
        'device_mobile'            : 'Mobile',
        'device_immersive_display' : 'Immersive Display',
    }
    for flag_col, value in flag_map.items():
        df[flag_col] = df['device'].apply(lambda lst: int(value in lst))
    return df

def onehot_technique(df):
    flag_map = {
        'tech_3d_scanning'            : '3D Scanning',
        'tech_image_based_techniques' : 'Image-Based Techniques',
        'tech_geospatial_techniques'  : 'Geospatial Techniques',
        'tech_modeling'               : 'Modeling & Reconstruction',
        'tech_data_processing'        : 'Data Processing'
    }
    for flag_col, value in flag_map.items():
        df[flag_col] = df['technique'].apply(lambda lst: int(value in lst))
    return df

def onehot_technique_sub(df):
    subgroup_map = {
        'sub_3d_scanning': {
            'Laser Scanning', 
            'RGB-D Imaging', 
            'Real-Time Volumetric Capture'
        },
        'sub_image_based_techniques': {
            'Photogrammetry', 
            'Spherical Imaging', 
            'Image-Based Modelling (IBM)',
            'Structure from Motion (SfM)', 
            'UAV Aerial Imaging', 
            'Multi-View Stereo (MVS)'
        },
        'sub_geospatial_techniques': {
            'Geographic Information System (GIS)', 
            'Global Navigation Satellite System (GNSS)',
            'Digital Elevation Models (DEM)', 
            'Visual-Inertial SLAM', 
            'Beacon Localization'
        },
        'sub_modeling': {
            '3D Modeling', 
            'BIM (Building Information Modeling)',
            'HBIM (Historical Building Information Modeling)', 
            'Archaeological Data Integration',
            'Stratigraphic Mapping', 
            'Virtual Anastylosis'
        },
        'sub_data_processing': {
            'Semantic Data Extraction', 
            '3D Texturing',
            'Texture Mapping', 
            'Range-Based Modeling (RBM)', 
            'HDR Imaging'
        }
    }
    for newcol in subgroup_map:
        df[newcol] = 0
    for idx, subs in df['technique_sub'].items():
        for newcol, members in subgroup_map.items():
            if set(subs) & members:
                df.at[idx, newcol] = 1
    return df

def onehot_software(df):
    flag_map = {
        'software_data'     : 'software_data',
        'software_modeling' : 'software_modeling',
        'software_render'   : 'software_render',
    }
    for flag_col, source_col in flag_map.items():
        df[flag_col] = df[source_col].apply(lambda lst: int(bool(lst)))
    return df

def reorder(df):
    # head                     = ['id', 'order', 'year', 'country']
    study_focus              = ['study_focus_restoration', 'study_focus_visualization', 'study_focus_reconstruction']
    historical_site_type     = ['historical_site_type_archaeological_site', 'historical_site_type_artistic_feature', 'historical_site_type_building', 'historical_site_type_natural_space']
    historical_site_type_sub = ['hst_sub_landbased', 'hst_sub_underwater', 'hst_sub_architectural_asset', 'hst_sub_artifact', 'hst_sub_fortification', 'hst_sub_religious', 'hst_sub_urbanspace', 'hst_sub_cave']
    platform                 = ['platform_vr', 'platform_ar', 'platform_mr', 'platform_xr']
    device                   = ['device_hmd', 'device_pc', 'device_mobile', 'device_immersive_display']
    technique                = ['tech_3d_scanning', 'tech_image_based_techniques', 'tech_geospatial_techniques', 'tech_modeling', 'tech_data_processing']
    technique_sub            = ['sub_3d_scanning', 'sub_image_based_techniques', 'sub_geospatial_techniques', 'sub_modeling', 'sub_data_processing']
    # software_data = 
    # software_modeling = 
    # software_render = 
    software                 = ['software_data', 'software_modeling', 'software_render']
    
    all_cols = study_focus + historical_site_type + historical_site_type_sub + platform + device + technique + technique_sub + software
    return df[[c for c in all_cols if c in df.columns]]


df = load_csv(SOURCE)
df = onehot_study_focus(df)
df = onehot_historical_site_type(df)
df = onehot_historical_site_type_sub(df)
df = onehot_platform(df)
df = onehot_device(df)
df = onehot_technique(df)
df = onehot_technique_sub(df)
df = onehot_software(df)
df_final = reorder(df)

df_final.to_csv(OUTPUT, index=False, encoding='utf-8')

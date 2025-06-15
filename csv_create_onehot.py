import json
import pandas as pd


STUDY_FOCUS_MAP = {
    'sf_restoration'    : 'Restoration',
    'sf_visualization'  : 'Visualization',
    'sf_reconstruction' : 'Reconstruction',
}

HISTORICAL_SITE_TYPE_MAP = {
    'hst_archaeological_site' : 'Archaeological Site',
    'hst_artistic_feature'    : 'Artistic Feature',
    'hst_building'            : 'Building',
    'hst_natural_space'       : 'Natural Space',
}

HISTORICAL_SITE_TYPE_SUB_MAP = {
    # Archaeological Site
    'hst_sub_landbased'  : 'LandBased',
    'hst_sub_underwater' : 'Underwater',
    
    # Artistic Feature
    'hst_sub_architectural_asset' : 'ArchitecturalAsset',
    'hst_sub_artifact'            : 'Artifact',
    
    # Building
    'hst_sub_fortification' : 'Fortification',
    'hst_sub_religious'     : 'Religious',
    'hst_sub_urbanspace'    : 'UrbanSpace',
    
    # Natural Space
    'hst_sub_cave' : 'Cave',
}

PLATFORM_MAP = {
    'platform_vr' : 'VR',
    'platform_ar' : 'AR',
    'platform_mr' : 'MR',
    'platform_xr' : 'XR',
}

DEVICE_MAP = {
    'device_hmd'               : 'HMD',
    'device_pc'                : 'PC',
    'device_mobile'            : 'Mobile',
    'device_immersive_display' : 'Immersive Display',
}

TECHNIQUE_MAP = {
    'tech_3d_scanning'     : '3D Scanning',
    'tech_image_based'     : 'Image-Based Techniques',
    'tech_geospatial'      : 'Geospatial Techniques',
    'tech_modeling'        : 'Modeling & Reconstruction',
    'tech_data_processing' : 'Data Processing'
}

TECHNIQUE_SUB_MAP = {
    # 3D Scanning
    'tech_sub_laser_scanning'                  : 'Laser Scanning',
    'tech_sub_rgbd_imaging'                    : 'RGB-D Imaging',
    'tech_sub_volumetric_capture'              : 'Real-Time Volumetric Capture',
    
    # Image-Based Techniques
    'tech_sub_photogrammetry'                  : 'Photogrammetry',
    'tech_sub_spherical'                       : 'Spherical Imaging',
    'tech_sub_ibm'                             : 'Image-Based Modelling (IBM)',
    'tech_sub_sfm'                             : 'Structure from Motion (SfM)',
    'tech_sub_uav'                             : 'UAV Aerial Imaging',
    'tech_sub_mvs'                             : 'Multi-View Stereo (MVS)',
    
    # Geospatial Techniques
    'tech_sub_gis'                             : 'Geographic Information System (GIS)',
    'tech_sub_gnss'                            : 'Global Navigation Satellite System (GNSS)',
    'tech_sub_dem'                             : 'Digital Elevation Models (DEM)',
    'tech_sub_slam'                            : 'Visual-Inertial SLAM',
    'tech_sub_beacon_localization'             : 'Beacon Localization',
    
    # Modeling & Reconstruction
    'tech_sub_3d'                              : '3D Modeling',
    'tech_sub_bim'                             : 'BIM (Building Information Modeling)',
    'tech_sub_hbim'                            : 'HBIM (Historical Building Information Modeling)',
    'tech_sub_sm'                              : 'Stratigraphic Mapping',
    'tech_sub_anastylosis'                     : 'Virtual Anastylosis',
    'tech_sub_adi'                             : 'Archaeological Data Integration',
    
    # Data Processing
    'tech_sub_semantic_data_extraction'        : 'Semantic Data Extraction',
    'tech_sub_3d_texturing'                    : '3D Texturing',
    'tech_sub_texture_mapping'                 : 'Texture Mapping',
    'tech_sub_rbm'                             : 'Range-Based Modeling (RBM)',
    'tech_sub_hdr_imaging'                     : 'HDR Imaging',
    'tech_sub_archaeological_interpretation'   : 'Archaeological Interpretation',
}

SOFTWARE_DATA_MAP = {
    'sd_autodesk_recap'        : 'Autodesk ReCap',
    'sd_autodesk_mudbox'       : 'Autodesk Mudbox',
    'sd_agisoft_metashape'     : 'Agisoft Metashape',
    'sd_reality_capture'       : 'Reality Capture',
    'sd_context_capture'       : 'Context Capture',
    'sd_pix4d_capture'         : 'PIX4D Capture',
    'sd_leica_cyclone'         : 'Leica Cyclone',
    'sd_dstretch'              : 'Dstretch',
    'sd_arcgis'                : 'ArcGIS',
    'sd_faro_scene'            : 'Faro Scene',
    'sd_focus_scene'           : 'Focus Scene',
    'sd_processing'            : 'Processing',
    'sd_australis_photometric' : 'Australis Photometric',
    'sd_affinity'              : 'Affinity',
    'sd_polycam'               : 'Polycam',
    'sd_graphos'               : 'GRAPHOS',
    'sd_catia'                 : 'CATIA',
    'sd_qgis'                  : 'QGIS',
    'sd_mysql'                 : 'MySQL',
}

SOFTWARE_MODELING_MAP = {
    'sm_autodesk_autocad' : 'Autodesk AutoCAD',
    'sm_autodesk_3ds_max' : 'Autodesk 3ds Max',
    'sm_autodesk_maya'    : 'Autodesk Maya',
    'sm_autodesk_revit'   : 'Autodesk Revit',
    'sm_autodesk_remake'  : 'Autodesk Remake',
    'sm_sketchup'         : 'SketchUp',
    'sm_rhinoceros'       : 'Rhinoceros',
    'sm_blender'          : 'Blender',
    'sm_archicad'         : 'ArchiCAD',
    'sm_maxon_cinema4d'   : 'Maxon Cinema4D',
    'sm_zbrush'           : 'ZBrush',
    'sm_meshlab'          : 'Meshlab',
    'sm_meshmixer'        : 'Meshmixer',
    'sm_ramsete'          : 'Ramsete',
    'sm_simlab'           : 'SIMLAB',
}

SOFTWARE_RENDER_MAP = {
    'sr_unity'            : 'Unity',
    'sr_unreal_engine'    : 'Unreal Engine',
    'sr_vray'             : 'V-Ray',
    'sr_lumion'           : 'Lumion',
    'sr_enscape'          : 'Enscape',
    'sr_twinmotion'       : 'Twinmotion',
    'sr_sketchfab'        : 'Sketchfab',
    'sr_maxwhere'         : 'MaxWhere',
    'sr_vuforia'          : 'Vuforia',
    'sr_gimp'             : 'Gimp',
    'sr_easyar'           : 'EasyAR',
    'sr_pano2vr'          : 'Pano2VR',
    'sr_augment'          : 'Augment',
    'sr_three_js'         : 'Three.js',
    'sr_middlevr'         : 'MiddleVR',
    'sr_renderman'        : 'RenderMan',
    'sr_shapespark'       : 'Shapespark',
    'sr_fb360_encoder'    : 'FB360 Encoder',
    'sr_kolor_panotour'   : 'Kolor Panotour',
    'sr_world_creator_2'  : 'World Creator 2',
}


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

def onehot(df, column, mapping, is_list=True):
    flags = {}
    for flag_col, target in mapping.items():
        if is_list:
            flags[flag_col] = df[column].apply(lambda lst: int(target in lst))
        else:
            flags[flag_col] = df[column].apply(lambda x: int(x == target))

    return pd.concat([df, pd.DataFrame(flags, index=df.index)], axis=1)

def organise_columns(df):
    head                         = ['id', 'order', 'year', 'country']
    
    study_focus                  = ['study_focus']
    study_focus_map              = list(STUDY_FOCUS_MAP.keys())
    
    historical_site_type         = ['historical_site_type']
    historical_site_type_map     = list(HISTORICAL_SITE_TYPE_MAP.keys())
    
    historical_site_type_sub     = ['historical_site_type_sub']
    historical_site_type_sub_map = list(HISTORICAL_SITE_TYPE_SUB_MAP.keys())
    
    platform                     = ['platform']
    platform_map                 = list(PLATFORM_MAP.keys())
    
    device                       = ['device']
    device_map                   = list(DEVICE_MAP.keys())
    
    technique                    = ['technique']
    technique_map                = list(TECHNIQUE_MAP.keys())
    
    technique_sub                = ['technique_sub']
    technique_sub_map            = list(TECHNIQUE_SUB_MAP.keys())
    
    software_data                = ['software_data']
    software_data_map            = list(SOFTWARE_DATA_MAP.keys())
    
    software_modeling            = ['software_modeling']
    software_modeling_map        = list(SOFTWARE_MODELING_MAP.keys())
    
    software_render              = ['software_render']
    software_render_map          = list(SOFTWARE_RENDER_MAP.keys())
    
    all_cols = (
        # head + 
        
        # study_focus + 
        study_focus_map +
        
        # historical_site_type + 
        historical_site_type_map + 
        
        # historical_site_type_sub + 
        historical_site_type_sub_map + 
        
        # platform + 
        platform_map + 
        
        # device + 
        device_map +
        
        # technique + 
        technique_map + 
        
        # technique_sub + 
        technique_sub_map +
        
        # software_data + 
        software_data_map +
        
        # software_modeling + 
        software_modeling_map + 
        
        # software_render
        software_render_map
    )
    return df[[c for c in all_cols if c in df.columns]]


df = load_csv(SOURCE)
df = onehot(df, 'study_focus'              , STUDY_FOCUS_MAP              , False)
df = onehot(df, 'historical_site_type'     , HISTORICAL_SITE_TYPE_MAP     , False)
df = onehot(df, 'historical_site_type_sub' , HISTORICAL_SITE_TYPE_SUB_MAP , False)
df = onehot(df, 'platform'                 , PLATFORM_MAP)
df = onehot(df, 'device'                   , DEVICE_MAP)
df = onehot(df, 'technique'                , TECHNIQUE_MAP)
df = onehot(df, 'technique_sub'            , TECHNIQUE_SUB_MAP)
df = onehot(df, 'software_data'            , SOFTWARE_DATA_MAP)
df = onehot(df, 'software_modeling'        , SOFTWARE_MODELING_MAP)
df = onehot(df, 'software_render'          , SOFTWARE_RENDER_MAP)
df_final = organise_columns(df)

df_final.to_csv(OUTPUT, index=False, encoding='utf-8')

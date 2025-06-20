HEADER = [
    'id', 'order', 'year', 'country', 
    'study_focus', 'historical_site_type', 'historical_site_type_sub', 
    'platform', 'device', 'technique', 'technique_sub', 
    'software_data', 'software_modeling', 'software_render',
    'elo', 'cluster'
]

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
    'sd_autodesk_meshmixer'    : 'Autodesk Meshmixer',
    'sd_agisoft_metashape'     : 'Agisoft Metashape',
    'sd_trimble_business'      : 'Trimble Business Center',
    'sd_trimble_realworks'     : 'Trimble RealWorks',
    'sd_reality_capture'       : 'Reality Capture',
    'sd_context_capture'       : 'Context Capture',
    'sd_cloudcompare'          : 'CloudCompare',
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
    'sd_world_creator_2'       : 'World Creator 2',
    'sd_mesh_buildup_wizard'   : 'Mesh Buildup Wizard',
    'sd_riegl_riscan'          : 'Riegl RiScan',
    'sd_3df_zephyr'            : '3DF Zephyr',
    'sd_arcmap'                : 'ArcMap',
    'sd_dynamo'                : 'Dynamo',
    'sd_geomagic'              : 'Geomagic',
    'sd_ptgui'                 : 'PTGui',
    'sd_matlab'                : 'MATLAB',
    'sd_mongodb'               : 'MongoDB',
}

SOFTWARE_MODELING_MAP = {
    'sm_autodesk_autocad' : 'Autodesk AutoCAD',
    'sm_autodesk_3ds_max' : 'Autodesk 3ds Max',
    'sm_autodesk_maya'    : 'Autodesk Maya',
    'sm_autodesk_revit'   : 'Autodesk Revit',
    'sm_autodesk_remake'  : 'Autodesk Remake',
    'sm_archicad'         : 'ArchiCAD',
    'sm_blender'          : 'Blender',
    'sm_sketchup'         : 'SketchUp',
    'sm_rhinoceros'       : 'Rhinoceros',
    'sm_maxon_cinema4d'   : 'Maxon Cinema4D',
    'sm_zbrush'           : 'ZBrush',
    'sm_meshlab'          : 'Meshlab',
    'sm_meshmixer'        : 'Meshmixer',
    'sm_ramsete'          : 'Ramsete',
    'sm_simlab'           : 'SIMLAB',
    'sm_3dreshaper'       : '3DReshaper',
    'sm_fuenta_nueva'     : 'Fuente Nueva',
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
    'sr_arkit'            : 'ARKit',
    'sr_verge3d'          : 'Verge3D',
}

COLUMNS_METADATA = {
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

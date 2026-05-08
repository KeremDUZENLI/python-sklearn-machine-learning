import csv


ROWS = [
    # id, 0_order, 1_year, 2_country, 3_study_focus, 4_historical_site_type, 5_historical_site_type_sub, 6_platform, 7_device, 8_technique, 9_technique_sub, 10_software_data, 11_software_modeling, 12_software_render
    (1, 2, 2023, 'Latvia', 'Restoration', 'Building', 'Fortification', ['VR'], ['HMD'], ['3D Scanning', 'Image-Based Techniques', 'Modeling & Reconstruction'], ['Laser Scanning', 'Photogrammetry', 'HBIM (Historical Building Information Modeling)'], ['PIX4D Capture', 'Leica Cyclone', 'Context Capture'], ['ArchiCAD'], ['Unity', 'Unreal Engine']), 
    (2, 5, 2017, 'Cyprus', 'Visualization', 'Archaeological Site', 'LandBased', ['VR'], ['HMD'], ['Image-Based Techniques', 'Modeling & Reconstruction'], ['Photogrammetry', '3D Modeling'], ['Agisoft Metashape'], [], ['Unity']), 
    (3, 6, 2020, 'France', 'Reconstruction', 'Archaeological Site', 'LandBased', ['VR'], ['HMD'], ['Image-Based Techniques', 'Modeling & Reconstruction'], ['Photogrammetry', '3D Modeling', 'Archaeological Interpretation'], ['Agisoft Metashape'], ['Autodesk 3ds Max'], ['V-Ray', 'Unity']), 
    (4, 8, 2020, 'Italy', 'Reconstruction', 'Building', 'UrbanSpace', ['VR'], ['HMD'], ['3D Scanning', 'Image-Based Techniques', 'Modeling & Reconstruction'], ['Laser Scanning', 'Photogrammetry', 'Image-Based Modelling (IBM)', 'Virtual Anastylosis'], ['Agisoft Metashape'], ['Autodesk 3ds Max'], ['Unreal Engine']), 
    (5, 9, 2021, 'Greece', 'Reconstruction', 'Building', 'Religious', ['VR'], ['PC'], ['Image-Based Techniques', 'Geospatial Techniques'], ['Photogrammetry', 'Structure from Motion (SfM)', 'UAV Aerial Imaging', 'Geographic Information System (GIS)'], ['Agisoft Metashape'], ['SketchUp'], ['Unity']), 
    (6, 13, 2018, 'Italy', 'Reconstruction', 'Artistic Feature', 'Artifact', ['AR'], ['Mobile'], ['Image-Based Techniques', 'Modeling & Reconstruction'], ['Photogrammetry', '3D Modeling'], ['Agisoft Metashape'], ['Meshmixer'], ['Unity', 'EasyAR']), 
    (7, 14, 2021, 'Czechia', 'Visualization', 'Building', 'Fortification', ['VR'], ['HMD', 'PC', 'Mobile'], ['Image-Based Techniques', 'Modeling & Reconstruction'], ['Photogrammetry', '3D Modeling'], ['ArcGIS'], ['Blender'], ['Unity']), 
    (8, 15, 2016, 'Italy', 'Visualization', 'Archaeological Site', 'LandBased', ['AR'], ['Mobile'], ['Image-Based Techniques'], ['Photogrammetry'], ['ArcGIS'], ['Blender'], ['Unity']), 
    (9, 19, 2022, 'Greece', 'Visualization', 'Natural Space', 'Cave', ['VR'], ['HMD'], ['3D Scanning', 'Image-Based Techniques'], ['Laser Scanning', 'Photogrammetry'], ['Faro Scene'], ['Blender'], ['Unity']), 
    (10, 20, 2023, 'Italy', 'Visualization', 'Archaeological Site', 'LandBased', ['VR'], ['HMD'], ['Image-Based Techniques'], ['Photogrammetry'], ['Reality Capture'], [], ['Unreal Engine']), 
    (11, 23, 2020, 'Spain', 'Reconstruction', 'Building', 'Religious', ['VR'], ['HMD'], ['Image-Based Techniques'], ['Photogrammetry'], ['Dstretch'], ['Blender'], ['Unity']), 
    (12, 31, 2016, 'Indonesia', 'Visualization', 'Archaeological Site', 'LandBased', ['AR'], ['HMD'], ['Image-Based Techniques'], ['Photogrammetry'], ['Agisoft Metashape'], ['Autodesk Remake'], ['Unity']), 
    (13, 36, 2019, 'Iraq', 'Visualization', 'Building', 'Fortification', ['VR'], ['HMD'], ['3D Scanning', 'Modeling & Reconstruction'], ['Laser Scanning', '3D Modeling'], ['Processing'], ['Meshlab'], ['Unity']), 
    (14, 40, 2019, 'USA', 'Visualization', 'Natural Space', 'Cave', ['VR'], ['HMD'], ['Image-Based Techniques'], ['Photogrammetry'], ['Agisoft Metashape'], [], ['Unity']), 
    (15, 41, 2015, 'South Korea', 'Visualization', 'Building', 'Religious', ['VR'], ['HMD'], ['3D Scanning', 'Modeling & Reconstruction'], ['Laser Scanning', '3D Modeling'], ['Australis Photometric'], ['Autodesk 3ds Max'], ['Unity']), 
    (16, 47, 2021, 'Italy', 'Visualization', 'Archaeological Site', 'LandBased', ['VR'], ['PC', 'Mobile'], ['Image-Based Techniques'], ['Photogrammetry', 'Structure from Motion (SfM)'], ['Agisoft Metashape'], [], ['Three.js']), 
    (17, 48, 2022, 'Spain', 'Visualization', 'Building', 'Religious', ['VR'], ['HMD'], ['Image-Based Techniques', 'Modeling & Reconstruction'], ['Photogrammetry', 'HBIM (Historical Building Information Modeling)'], ['Autodesk ReCap', 'Agisoft Metashape'], ['Autodesk Revit'], ['Unreal Engine']), 
    (18, 50, 2024, 'Greece', 'Visualization', 'Building', 'Religious', ['VR'], ['HMD'], ['Image-Based Techniques'], ['Photogrammetry'], ['Context Capture'], ['Blender'], ['Unreal Engine']), 
    (19, 52, 2021, 'Greece', 'Visualization', 'Building', 'Religious', ['XR'], ['HMD'], ['3D Scanning', 'Image-Based Techniques'], ['Real-Time Volumetric Capture', 'Photogrammetry'], ['Agisoft Metashape'], [], ['Unity']), 
    (20, 55, 2018, 'Hungary', 'Reconstruction', 'Building', 'Religious', ['VR'], ['HMD'], ['3D Scanning', 'Image-Based Techniques'], ['Laser Scanning', 'UAV Aerial Imaging'], [], [], ['MaxWhere']), 
    (21, 57, 2023, 'Italy', 'Visualization', 'Building', 'Fortification', ['VR'], ['HMD'], ['Image-Based Techniques', 'Modeling & Reconstruction'], ['Photogrammetry', '3D Modeling'], ['Agisoft Metashape'], ['Blender'], ['Unity']), 
    (22, 58, 2024, 'Greece', 'Visualization', 'Archaeological Site', 'LandBased', ['MR'], ['HMD'], ['Geospatial Techniques', 'Modeling & Reconstruction'], ['Geographic Information System (GIS)', '3D Modeling'], ['MySQL'], ['Blender'], ['Unity']), 
    (23, 71, 2017, 'Saudi Arabia', 'Visualization', 'Archaeological Site', 'LandBased', ['VR'], ['HMD'], ['3D Scanning', 'Image-Based Techniques', 'Modeling & Reconstruction'], ['Laser Scanning', 'Photogrammetry', 'Structure from Motion (SfM)', '3D Modeling'], [], ['Autodesk Revit'], ['Unity']), 
    (24, 80, 2023, 'Brazil', 'Visualization', 'Archaeological Site', 'LandBased', ['AR'], ['Mobile'], ['3D Scanning', 'Image-Based Techniques'], ['Laser Scanning', 'Photogrammetry', 'UAV Aerial Imaging'], ['Agisoft Metashape'], ['SketchUp'], ['Unity']), 
    (25, 83, 2015, 'Spain', 'Reconstruction', 'Archaeological Site', 'LandBased', ['AR'], ['Mobile'], ['Image-Based Techniques', 'Modeling & Reconstruction'], ['Photogrammetry', 'Structure from Motion (SfM)', '3D Modeling'], ['Agisoft Metashape'], ['Blender'], []), 
    (26, 84, 2023, 'Italy', 'Visualization', 'Archaeological Site', 'LandBased', ['VR'], ['PC'], ['3D Scanning', 'Image-Based Techniques', 'Modeling & Reconstruction'], ['Laser Scanning', 'Photogrammetry', '3D Modeling'], ['Agisoft Metashape'], ['Blender'], ['Verge3D']), 
    (27, 90, 2021, 'Italy', 'Reconstruction', 'Archaeological Site', 'LandBased', ['VR'], ['HMD'], ['3D Scanning', 'Image-Based Techniques', 'Modeling & Reconstruction'], ['Laser Scanning', 'Photogrammetry', '3D Modeling'], ['Agisoft Metashape'], ['Blender'], ['Unity']), 
    (28, 92, 2022, 'Spain', 'Visualization', 'Archaeological Site', 'LandBased', ['VR'], ['Immersive Display'], ['Image-Based Techniques'], ['Photogrammetry'], ['GRAPHOS'], [], ['Pano2VR']), 
    (29, 97, 2023, 'Egypt', 'Visualization', 'Archaeological Site', 'LandBased', ['MR'], ['HMD', 'Immersive Display'], ['3D Scanning', 'Image-Based Techniques', 'Modeling & Reconstruction'], ['Laser Scanning', 'Photogrammetry', '3D Modeling'], ['Polycam'], ['Autodesk Revit'], ['Unity']), 
    (30, 99, 2020, 'USA', 'Visualization', 'Building', 'UrbanSpace', ['VR'], ['HMD'], ['3D Scanning', 'Image-Based Techniques', 'Modeling & Reconstruction'], ['Laser Scanning', 'Photogrammetry', 'UAV Aerial Imaging', '3D Modeling'], ['Agisoft Metashape', 'Leica Cyclone'], ['Autodesk 3ds Max'], ['Unity']), 
    (31, 105, 2022, 'China', 'Visualization', 'Archaeological Site', 'LandBased', ['VR'], ['HMD'], ['3D Scanning', 'Image-Based Techniques'], ['Laser Scanning', 'Photogrammetry'], [], ['Autodesk 3ds Max', 'Autodesk Maya', 'ZBrush'], ['Unity']), 
    (32, 114, 2022, 'Italy', 'Reconstruction', 'Building', 'Religious', ['VR'], ['HMD', 'PC', 'Mobile'], ['3D Scanning', 'Image-Based Techniques', 'Modeling & Reconstruction'], ['Laser Scanning', 'Photogrammetry', 'Structure from Motion (SfM)', '3D Modeling'], ['Autodesk ReCap', 'Agisoft Metashape', 'Reality Capture'], ['Maxon Cinema4D'], ['Unreal Engine', 'Pano2VR']), 
    (33, 115, 2017, 'China', 'Visualization', 'Building', 'Fortification', ['VR'], ['HMD', 'PC', 'Mobile'], ['3D Scanning', 'Image-Based Techniques', 'Modeling & Reconstruction'], ['Laser Scanning', 'Photogrammetry', '3D Modeling'], ['Agisoft Metashape', 'Reality Capture'], ['Blender', 'Rhinoceros'], ['Unreal Engine', 'ARKit']), 
    (34, 116, 2024, 'UK', 'Restoration', 'Artistic Feature', 'Artifact', ['VR'], ['HMD', 'PC', 'Mobile'], ['Image-Based Techniques', 'Modeling & Reconstruction'], ['Photogrammetry', '3D Modeling'], ['Agisoft Metashape'], ['Blender'], ['Unreal Engine', 'Three.js']), 
    (35, 117, 2020, 'Taiwan', 'Reconstruction', 'Archaeological Site', 'LandBased', ['AR'], ['Mobile'], ['Image-Based Techniques'], ['Photogrammetry'], ['Autodesk ReCap', 'Agisoft Metashape', '3DF Zephyr'], [], ['Augment', 'Sketchfab']), 
    (36, 118, 2022, 'China', 'Visualization', 'Building', 'Religious', ['VR', 'AR'], ['HMD', 'Mobile'], ['3D Scanning', 'Image-Based Techniques'], ['Laser Scanning', 'Photogrammetry', 'UAV Aerial Imaging'], ['Focus Scene'], ['Autodesk 3ds Max', 'Autodesk AutoCAD'], ['Unity', 'Vuforia']), 
    (37, 119, 2022, 'Romania', 'Reconstruction', 'Archaeological Site', 'LandBased', ['VR', 'AR', 'MR'], ['HMD', 'Mobile'], ['Image-Based Techniques', 'Modeling & Reconstruction'], ['Photogrammetry', '3D Modeling'], ['Autodesk Mudbox'], ['Autodesk 3ds Max'], ['RenderMan']), 
    (38, 127, 2023, 'Kazakhstan', 'Visualization', 'Archaeological Site', 'LandBased', ['VR'], ['PC'], ['3D Scanning'], ['Laser Scanning'], ['Faro Scene', 'Trimble RealWorks', 'Reality Capture'], [], []), 
    (39, 136, 2020, 'Romania', 'Visualization', 'Archaeological Site', 'LandBased', ['VR'], ['HMD', 'PC'], ['3D Scanning', 'Image-Based Techniques'], ['Laser Scanning', 'Photogrammetry'], ['CATIA'], ['Autodesk 3ds Max'], ['Unity']), 
    (40, 137, 2023, 'Italy', 'Reconstruction', 'Archaeological Site', 'LandBased', ['XR'], ['HMD', 'Mobile'], ['Image-Based Techniques', 'Modeling & Reconstruction'], ['Photogrammetry', 'HBIM (Historical Building Information Modeling)'], ['Agisoft Metashape'], ['Autodesk Revit'], []), 
    (41, 143, 2016, 'Peru', 'Visualization', 'Archaeological Site', 'LandBased', ['AR'], ['Mobile'], ['Image-Based Techniques'], ['Photogrammetry'], [], [], []), 
    (42, 151, 2024, 'India', 'Visualization', 'Natural Space', 'Cave', ['VR'], ['HMD'], ['3D Scanning', 'Image-Based Techniques', 'Modeling & Reconstruction'], ['Laser Scanning', 'Photogrammetry', '3D Modeling'], ['Autodesk ReCap', 'Agisoft Metashape'], ['Blender'], []), 
    (43, 158, 2023, 'Poland', 'Reconstruction', 'Archaeological Site', 'LandBased', ['VR'], ['HMD'], ['3D Scanning', 'Image-Based Techniques'], ['Laser Scanning', 'Photogrammetry'], ['Autodesk ReCap', 'Leica Cyclone', 'CloudCompare', '3DF Zephyr'], ['Rhinoceros'], ['Enscape']), 
    (44, 167, 2024, 'Syria', 'Reconstruction', 'Building', 'UrbanSpace', ['VR'], ['HMD'], ['Image-Based Techniques', 'Modeling & Reconstruction'], ['Photogrammetry', '3D Modeling'], [], ['Blender'], ['Unity']), 
    (45, 169, 2017, 'Spain', 'Restoration', 'Artistic Feature', 'Artifact', ['VR'], ['Mobile'], ['3D Scanning', 'Image-Based Techniques'], ['Laser Scanning', 'Photogrammetry'], ['Autodesk ReCap', 'Agisoft Metashape'], ['Blender', 'Rhinoceros'], ['Unity']), 
    (46, 176, 2022, 'South Korea', 'Visualization', 'Building', 'Religious', ['VR'], ['HMD'], ['3D Scanning', 'Modeling & Reconstruction'], ['Laser Scanning', '3D Modeling'], ['Mesh Buildup Wizard'], [], []), 
    (47, 178, 2022, 'Italy', 'Visualization', 'Building', 'UrbanSpace', ['VR'], ['HMD'], ['Image-Based Techniques', 'Modeling & Reconstruction'], ['Photogrammetry', '3D Modeling'], [], ['Blender', 'Autodesk AutoCAD', 'Ramsete'], ['FB360 Encoder']), 
    (48, 180, 2024, 'Portugal', 'Reconstruction', 'Building', 'Religious', ['VR'], ['HMD', 'PC'], ['3D Scanning', 'Image-Based Techniques', 'Modeling & Reconstruction'], ['Laser Scanning', 'Photogrammetry', 'HBIM (Historical Building Information Modeling)'], [], ['Autodesk Revit'], ['Shapespark']), 
    (49, 182, 2018, 'Turkiye', 'Visualization', 'Archaeological Site', 'LandBased', ['VR'], ['HMD'], ['3D Scanning', 'Image-Based Techniques', 'Geospatial Techniques'], ['Laser Scanning', 'Structure from Motion (SfM)', 'Geographic Information System (GIS)'], ['Agisoft Metashape', 'ArcGIS'], ['Blender'], ['Unity', 'MiddleVR']), 
    (50, 190, 2020, 'Belgium', 'Visualization', 'Building', 'Fortification', ['VR'], ['HMD'], ['3D Scanning', 'Image-Based Techniques'], ['Laser Scanning', 'Photogrammetry', 'Structure from Motion (SfM)'], ['Leica Cyclone', 'Trimble Business Center', 'Context Capture', 'Reality Capture'], ['Blender'], ['Unity']), 
    (51, 192, 2023, 'Italy', 'Visualization', 'Archaeological Site', 'LandBased', ['VR'], ['HMD'], ['3D Scanning', 'Image-Based Techniques', 'Geospatial Techniques'], ['Laser Scanning', 'Structure from Motion (SfM)', 'UAV Aerial Imaging', 'Global Navigation Satellite System (GNSS)'], ['Agisoft Metashape', 'Leica Cyclone', 'Autodesk ReCap', 'Reality Capture'], ['Autodesk AutoCAD'], []), 
    (52, 194, 2024, 'Morocco', 'Visualization', 'Building', 'Religious', ['XR'], ['HMD'], ['3D Scanning', 'Geospatial Techniques', 'Modeling & Reconstruction', 'Data Processing'], ['Laser Scanning', 'Beacon Localization', 'HBIM (Historical Building Information Modeling)', 'Semantic Data Extraction'], ['Leica Cyclone', 'Dynamo', 'MongoDB'], ['Autodesk Revit', 'SIMLAB'], ['Unity']), 
    (53, 195, 2022, 'Italy', 'Visualization', 'Building', 'Religious', ['VR', 'AR', 'MR'], ['HMD', 'PC', 'Mobile'], ['3D Scanning', 'Image-Based Techniques'], ['Laser Scanning', 'Photogrammetry'], ['Faro Scene', 'Autodesk ReCap', 'Agisoft Metashape', 'MATLAB'], ['Blender'], ['Unity', 'Unreal Engine', 'Vuforia']), 
    (54, 196, 2023, 'Italy', 'Visualization', 'Artistic Feature', 'ArchitecturalAsset', ['VR'], ['HMD'], ['Image-Based Techniques', 'Modeling & Reconstruction'], ['Photogrammetry'], ['Agisoft Metashape'], ['ZBrush'], ['Unreal Engine']), 
    (55, 198, 2023, 'Syria', 'Reconstruction', 'Building', 'Religious', ['VR', 'AR'], ['HMD', 'PC', 'Mobile'], ['Image-Based Techniques', 'Modeling & Reconstruction'], ['Photogrammetry', 'Structure from Motion (SfM)', 'Multi-View Stereo (MVS)', '3D Modeling'], ['Agisoft Metashape', 'Autodesk Meshmixer'], ['Blender'], ['Unity', 'Sketchfab']), 
    (56, 201, 2017, 'Italy', 'Reconstruction', 'Building', 'Religious', ['VR', 'AR'], ['HMD', 'Mobile'], ['Image-Based Techniques'], ['Photogrammetry'], ['Agisoft Metashape'], ['Blender'], []), 
    (57, 204, 2017, 'Turkiye', 'Reconstruction', 'Archaeological Site', 'LandBased', ['VR', 'AR'], ['HMD', 'Immersive Display'], ['3D Scanning', 'Image-Based Techniques'], ['Laser Scanning', 'Photogrammetry', 'Structure from Motion (SfM)'], ['Agisoft Metashape'], [], []), 
    (58, 212, 2015, 'Peru', 'Visualization', 'Archaeological Site', 'LandBased', ['AR'], ['Mobile'], ['Image-Based Techniques'], ['Photogrammetry', 'Structure from Motion (SfM)'], ['Agisoft Metashape'], [], []), 
    (59, 215, 2022, 'USA', 'Reconstruction', 'Archaeological Site', 'LandBased', ['VR'], ['HMD'], ['3D Scanning', 'Geospatial Techniques'], ['RGB-D Imaging', 'Visual-Inertial SLAM'], [], ['Meshlab', 'ZBrush'], ['Unity']), 
    (60, 217, 2020, 'Greece', 'Visualization', 'Archaeological Site', 'LandBased', ['AR'], ['Mobile'], ['Image-Based Techniques', 'Modeling & Reconstruction'], ['Photogrammetry', '3D Modeling'], ['PIX4D Capture'], [], ['Three.js']), 
    (61, 218, 2016, 'Romania', 'Visualization', 'Artistic Feature', 'Artifact', ['VR', 'AR'], ['HMD', 'Mobile'], ['3D Scanning', 'Image-Based Techniques', 'Modeling & Reconstruction'], ['Laser Scanning', 'Photogrammetry', '3D Modeling'], [], [], ['Unity']), 
    (62, 220, 2015, 'Greece', 'Reconstruction', 'Archaeological Site', 'LandBased', ['AR', 'MR'], ['HMD', 'Mobile'], ['Image-Based Techniques', 'Geospatial Techniques'], ['Photogrammetry', 'Structure from Motion (SfM)', 'Geographic Information System (GIS)'], ['Agisoft Metashape'], ['Blender', 'Autodesk 3ds Max'], ['Unity']), 
    (63, 228, 2023, 'Italy', 'Visualization', 'Archaeological Site', 'LandBased', ['VR', 'AR'], ['Immersive Display'], ['3D Scanning', 'Image-Based Techniques', 'Modeling & Reconstruction'], ['Laser Scanning', 'Photogrammetry', '3D Modeling', 'BIM (Building Information Modeling)'], ['Leica Cyclone', 'Agisoft Metashape'], ['Blender', 'Autodesk Revit'], ['Unity', 'Unreal Engine', 'Twinmotion']), 
    (64, 231, 2017, 'Italy', 'Visualization', 'Archaeological Site', 'LandBased', ['VR'], ['HMD'], ['Image-Based Techniques', 'Modeling & Reconstruction'], ['Photogrammetry', '3D Modeling'], ['Agisoft Metashape'], [], []), 
    (65, 237, 2019, 'Italy', 'Visualization', 'Archaeological Site', 'LandBased', ['VR', 'AR'], ['HMD'], ['Image-Based Techniques'], ['Photogrammetry', 'Structure from Motion (SfM)'], ['Agisoft Metashape'], ['Meshlab'], ['Unity']), 
    (66, 246, 2020, 'Turkiye', 'Visualization', 'Natural Space', 'Cave', ['VR'], ['HMD'], ['3D Scanning', 'Image-Based Techniques'], ['Laser Scanning', 'Photogrammetry'], ['Riegl RiScan', 'PTGui', 'Autodesk ReCap'], ['Autodesk 3ds Max'], ['Unity', 'Lumion']), 
    (67, 247, 2021, 'Iran', 'Visualization', 'Artistic Feature', 'ArchitecturalAsset', ['VR', 'AR'], ['HMD', 'Mobile'], ['3D Scanning', 'Image-Based Techniques'], ['Laser Scanning', 'Photogrammetry'], ['Agisoft Metashape'], ['Maxon Cinema4D'], []), 
    (68, 251, 2021, 'Spain', 'Reconstruction', 'Archaeological Site', 'LandBased', ['VR', 'AR'], ['HMD', 'Mobile'], ['3D Scanning', 'Image-Based Techniques'], ['Laser Scanning', 'Photogrammetry', 'UAV Aerial Imaging'], ['Autodesk ReCap', 'Leica Cyclone'], ['Autodesk Revit', 'Rhinoceros', 'SketchUp'], ['Lumion', 'Enscape']), 
    (69, 254, 2015, 'Italy', 'Reconstruction', 'Archaeological Site', 'LandBased', ['VR'], ['HMD', 'Mobile'], ['Image-Based Techniques', 'Geospatial Techniques', 'Modeling & Reconstruction'], ['Photogrammetry', 'Geographic Information System (GIS)', '3D Modeling'], ['QGIS'], ['Autodesk Maya'], ['Unity']), 
    (70, 256, 2020, 'Czechia', 'Reconstruction', 'Archaeological Site', 'LandBased', ['VR'], ['HMD', 'Mobile'], ['Geospatial Techniques', 'Modeling & Reconstruction'], ['Geographic Information System (GIS)', '3D Modeling'], ['QGIS'], ['Autodesk AutoCAD', 'SketchUp'], ['Lumion']), 
    (71, 263, 2020, 'Egypt', 'Restoration', 'Building', 'Fortification', ['VR'], ['HMD'], ['3D Scanning', 'Modeling & Reconstruction'], ['Laser Scanning', '3D Modeling', 'HBIM (Historical Building Information Modeling)'], ['ArcGIS', 'ArcMap'], [], ['Lumion', 'Kolor Panotour']), 
    (72, 268, 2024, 'Italy', 'Restoration', 'Building', 'UrbanSpace', ['VR'], ['HMD'], ['3D Scanning', 'Image-Based Techniques', 'Modeling & Reconstruction'], ['Laser Scanning', 'Photogrammetry', 'HBIM (Historical Building Information Modeling)'], ['Autodesk ReCap', 'Leica Cyclone'], ['Autodesk Revit'], []), 
    (73, 282, 2019, 'Canada', 'Visualization', 'Archaeological Site', 'Underwater', ['VR'], ['HMD'], ['Image-Based Techniques'], ['Image-Based Modelling (IBM)'], ['Agisoft Metashape'], ['ZBrush'], ['Unreal Engine']), 
    (74, 287, 2019, 'Italy', 'Restoration', 'Natural Space', 'Cave', ['VR'], ['HMD'], ['3D Scanning', 'Image-Based Techniques', 'Geospatial Techniques'], ['Laser Scanning', 'Photogrammetry', 'Global Navigation Satellite System (GNSS)'], ['Leica Cyclone', 'Agisoft Metashape'], ['3DReshaper', 'Autodesk AutoCAD'], ['Unity']), 
    (75, 299, 2017, 'Georgia', 'Visualization', 'Archaeological Site', 'LandBased', ['VR', 'AR'], ['HMD', 'Mobile'], ['Image-Based Techniques'], ['Photogrammetry', 'Spherical Imaging'], ['Affinity'], [], ['Unity']), 
    (76, 305, 2017, 'Italy', 'Reconstruction', 'Archaeological Site', 'LandBased', ['VR', 'AR'], ['HMD', 'Mobile'], ['Image-Based Techniques', 'Modeling & Reconstruction'], ['Photogrammetry', 'Archaeological Interpretation'], ['Agisoft Metashape', 'QGIS'], ['Blender'], ['Gimp']), 
    (77, 310, 2024, 'Cyprus', 'Visualization', 'Archaeological Site', 'Underwater', ['VR'], ['HMD'], ['Image-Based Techniques', 'Geospatial Techniques'], ['Photogrammetry', 'Structure from Motion (SfM)', 'Geographic Information System (GIS)'], ['Agisoft Metashape'], ['Blender'], ['Unreal Engine']), 
    (78, 317, 2018, 'Italy', 'Visualization', 'Archaeological Site', 'LandBased', ['VR', 'AR'], ['HMD', 'Immersive Display'], ['3D Scanning', 'Image-Based Techniques', 'Modeling & Reconstruction'], ['Laser Scanning', 'Photogrammetry', '3D Modeling'], ['Leica Cyclone'], [], ['Unity']), 
    (79, 320, 2022, 'Italy', 'Restoration', 'Archaeological Site', 'LandBased', ['VR', 'AR'], ['HMD', 'PC', 'Mobile'], ['3D Scanning', 'Image-Based Techniques', 'Modeling & Reconstruction'], ['Laser Scanning', 'Photogrammetry', 'UAV Aerial Imaging', 'HBIM (Historical Building Information Modeling)'], ['Agisoft Metashape', 'Autodesk ReCap', 'PTGui'], ['Autodesk Revit'], ['Unity']), 
    (80, 321, 2018, 'Spain', 'Visualization', 'Archaeological Site', 'LandBased', ['VR'], ['HMD', 'PC', 'Mobile'], ['Image-Based Techniques', 'Modeling & Reconstruction', 'Data Processing'], ['Photogrammetry', 'Image-Based Modelling (IBM)', 'Virtual Anastylosis', '3D Texturing', 'Range-Based Modeling (RBM)'], ['Agisoft Metashape'], ['Blender', 'Autodesk AutoCAD'], []), 
    (81, 325, 2019, 'Jordan', 'Visualization', 'Building', 'Religious', ['AR'], ['PC', 'Mobile'], ['3D Scanning', 'Image-Based Techniques', 'Geospatial Techniques'], ['Laser Scanning', 'Photogrammetry', 'Multi-View Stereo (MVS)', 'Digital Elevation Models (DEM)', 'Geographic Information System (GIS)'], ['Agisoft Metashape', 'Faro Scene', 'ArcGIS'], ['Blender', 'Autodesk AutoCAD'], ['Unity']), 
    (82, 326, 2019, 'Italy', 'Visualization', 'Building', 'Religious', ['VR', 'AR'], ['HMD', 'PC', 'Mobile'], ['Image-Based Techniques', 'Modeling & Reconstruction', 'Data Processing'], ['Photogrammetry', 'Stratigraphic Mapping', '3D Texturing'], ['Agisoft Metashape'], ['Blender', 'ZBrush', 'Autodesk AutoCAD'], ['Unity', 'Kolor Panotour']), 
    (83, 329, 2022, 'Italy', 'Visualization', 'Building', 'Religious', ['VR', 'MR'], ['HMD', 'PC'], ['3D Scanning', 'Image-Based Techniques', 'Data Processing'], ['Laser Scanning', 'Photogrammetry', 'HDR Imaging'], ['Reality Capture'], ['Rhinoceros'], ['Unreal Engine', 'Twinmotion']), 
    (84, 333, 2021, 'Qatar', 'Visualization', 'Building', 'Fortification', ['VR'], ['HMD', 'PC'], ['3D Scanning', 'Image-Based Techniques', 'Modeling & Reconstruction'], ['Laser Scanning', 'Photogrammetry', 'Structure from Motion (SfM)', '3D Modeling'], ['Agisoft Metashape', 'Geomagic'], ['Blender', 'Autodesk AutoCAD'], ['Unreal Engine']), 
    (85, 334, 2023, 'Switzerland', 'Visualization', 'Archaeological Site', 'LandBased', ['VR'], ['HMD', 'PC'], ['Image-Based Techniques', 'Data Processing'], ['Photogrammetry', 'Structure from Motion (SfM)', 'Texture Mapping'], ['Agisoft Metashape'], ['Blender'], ['Unity']), 
    (86, 335, 2024, 'Jordan', 'Reconstruction', 'Archaeological Site', 'LandBased', ['VR'], ['HMD'], ['Image-Based Techniques'], ['Photogrammetry'], ['Agisoft Metashape'], [], ['Unreal Engine']), 
    (87, 337, 2023, 'Ethiopia', 'Reconstruction', 'Archaeological Site', 'LandBased', ['VR'], ['HMD'], ['3D Scanning', 'Image-Based Techniques'], ['Laser Scanning', 'Photogrammetry'], ['QGIS', 'World Creator 2'], ['Blender'], ['Unreal Engine']), 
    (88, 338, 2022, 'Italy', 'Reconstruction', 'Building', 'Fortification', ['VR'], ['HMD'], ['Image-Based Techniques', 'Modeling & Reconstruction'], ['Photogrammetry', '3D Modeling'], ['Agisoft Metashape'], ['Blender'], ['Unity']), 
    (89, 339, 2024, 'Italy', 'Visualization', 'Natural Space', 'Cave', ['VR'], ['HMD'], ['Image-Based Techniques'], ['Photogrammetry'], ['Reality Capture'], [], ['Unreal Engine']), 
    (90, 340, 2019, 'Italy', 'Visualization', 'Archaeological Site', 'Underwater', ['VR'], ['HMD'], ['Image-Based Techniques'], ['Photogrammetry'], ['Agisoft Metashape', 'QGIS'], ['Autodesk 3ds Max'], ['Unreal Engine']), 
    (91, 351, 2023, 'Greece', 'Visualization', 'Building', 'Fortification', ['VR', 'AR'], ['HMD', 'Mobile'], ['3D Scanning', 'Image-Based Techniques'], ['Laser Scanning', 'Photogrammetry', 'UAV Aerial Imaging'], [], [], ['Unity']), 
    (92, 356, 2020, 'Spain', 'Visualization', 'Archaeological Site', 'LandBased', ['VR'], ['HMD'], ['Image-Based Techniques'], ['Photogrammetry'], ['Agisoft Metashape'], ['Fuente Nueva'], ['Unreal Engine'])
]

ELOS = [
    1526, 1448, 1637, 1568, 1210, 1281, 1557, 1505, 1716, 1670,
    1552, 1294, 1414, 1407, 1691, 1447, 1526, 1707, 1415, 1567,
    1495, 1438, 1382, 1259, 1572, 1358, 1416, 1364, 1663, 1441,
    1273, 1738, 1248, 1687, 1612, 1488, 1402, 1750, 1489, 1669,
    1357, 1563, 1591, 1646, 1458, 1591, 1680, 1411, 1330, 1443,
    1505, 1655, 1466, 1468, 1402, 1654, 1432, 1531, 1263, 1529,
    1227, 1466, 1500, 1279, 1550, 1540, 1551, 1211, 1728, 1646,
    1447, 1545, 1363, 1592, 1441, 1670, 1421, 1418, 1582, 1799,
    1343, 1346, 1616, 1610, 1477, 1638, 1487, 1493, 1479, 1436,
    1611, 1631
]


def map_elos_to_csv(filepath: str) -> list:
    lookup = {
        (str(r[2]), r[3], r[4], r[5], r[6], ";".join(r[7])): elo 
        for r, elo in zip(ROWS, ELOS)
    }
    mapped_elos = []
    
    with open(filepath, mode='r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) < 7:
                continue
                
            signature = (row[1], row[2], row[3], row[4], row[5], row[6])
            mapped_elos.append(lookup.get(signature, '0000'))
            
    return mapped_elos


result = map_elos_to_csv('data/dataset.old.csv')
print(result)
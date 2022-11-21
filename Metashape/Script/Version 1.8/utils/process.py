# Insect photogrammetry processing script
# Metashape verison 1.8
#
# Code written by Ernst Herb
#----------------------------------------


# Function: Process Start
def process(Metashape, doc, chunk, Time):

    # Align Photos
    chunk.matchPhotos(downscale = Time, generic_preselection = True, reference_preselection = True, filter_stationary_points = True, keypoint_limit = 250000, tiepoint_limit = 250000, keep_keypoints = False, guided_matching = False)
    doc.save()

    chunk.alignCameras()
    doc.save()

    # Optimize Cameras
    chunk.optimizeCameras(fit_f = True, fit_cx = False, fit_cy = False, fit_b1 = False, fit_b2 = False, fit_k1 = False, fit_k2 = False, fit_k3 = False, fit_k4 = False, fit_p1 = False, fit_p2 = False, fit_corrections = False, adaptive_fitting = False, tiepoint_covariance = False)

    # Build Depth Map
    chunk.buildDepthMaps(downscale = 1, filter_mode = Metashape.MildFiltering)
    doc.save()

    # Build Model

    # Following line would be commonly used but not in case when tweaks have to be added
    # chunk.buildModel(face_count = Metashape.HighFaceCount, source_data = Metashape.DepthMapsData)

    task = Metashape.Tasks.BuildModel()
    task["ooc_surface_blow_up"] = "0.95"
    task["ooc_surface_blow_off"] = "0.95"
    task.face_count = Metashape.HighFaceCount
    task.source_data = Metashape.DepthMapsData
    task.apply(chunk)

    doc.save()

    # Smooth Model
    chunk.smoothModel(strength = 2, fix_borders = False, preserve_edges = False)
    doc.save()

    # Build Texture
    chunk.buildUV(page_count = 1, texture_size = 4096)
    doc.save()

    chunk.buildTexture(texture_size = 4096, ghosting_filter = True)
    doc.save()

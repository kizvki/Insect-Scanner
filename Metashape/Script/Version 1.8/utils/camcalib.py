# Insect photogrammetry processing script
# Metashape verison 1.8
#
# Code written by Ernst Herb
#----------------------------------------


# Function: Import reference
def imp_camcalib(Metashape, chunk, calib, sensor, calibFolder, CamCalibration):

    calib.load(path = calibFolder + "\\" + CamCalibration + ".xml", format = Metashape.CalibrationFormatXML)

    for sensor in chunk.sensors: # Apply Calibration to all Cameras
        sensor.user_calib = calib
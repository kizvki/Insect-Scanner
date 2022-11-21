# Insect photogrammetry processing script
# Metashape verison 1.8
#
# Code written by Ernst Herb
#----------------------------------------

import Metashape

# --------------------------------------------------------------
# Simplifing variables

doc = Metashape.Document()
chunk = doc.addChunk()
camera = chunk.cameras  
sensor = Metashape.Sensor
calib = Metashape.Calibration()

# --------------------------------------------------------------
# Import reference

calibFolder = "C:\InsectScanner\Data\Calibration"

# Camera Position Reference
referenceFilename = "CamPos_Vel3"

# Camera Calibration
CamCalibration = "CamCalibration_Vel3"

# --------------------------------------------------------------
# Coordinate System

crs1 = Metashape.CoordinateSystem('LOCAL_CS["Local Coordinates (mm)",LOCAL_DATUM["Local Datum",0],UNIT["millimetre",0.001,AUTHORITY["EPSG","1025"]]]')
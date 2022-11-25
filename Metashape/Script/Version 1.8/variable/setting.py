# Insect photogrammetry processing script
# Metashape verison 1.8
#
# Code written by Ernst Herb
#----------------------------------------

import Metashape

# --------------------------------------------------------------
# Set script written for metashape version

version = "1.8"

# --------------------------------------------------------------
# Folder structure

foldersec = "" #Security that checks if the selected folder contains this name to prevent selecting wrong folder, else leave it an empty string

imgfolder = "edof" #Select the name of the image folder, which only works if the image folder is placed inside of the selected output folder

# --------------------------------------------------------------
# Import reference

calibFolder = "C:\InsectScanner\Data\Calibration"

# Camera Position Reference
referenceFilename = "CamPos"

# Camera Calibration
CamCalibration = "CamCalibration"

# --------------------------------------------------------------
# Coordinate System

crs1 = Metashape.CoordinateSystem('LOCAL_CS["Local Coordinates (mm)",LOCAL_DATUM["Local Datum",0],UNIT["millimetre",0.001,AUTHORITY["EPSG","1025"]]]')
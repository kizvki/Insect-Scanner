# Insect photogrammetry processing script
# Metashape verison 1.8
#
# Code written by Ernst Herb
#----------------------------------------

import Metashape
import os, sys, time
import utils
import variable

# Checking Compatibility

utils.check_compatibility(Metashape)

# Simplifing variables
doc = variable.doc
chunk = variable.chunk
camera = variable.camera
sensor = variable.sensor
calib = variable.calib

start_time = time.time() #Start Time for script duration calculation

# --------------------------------------------------------------
# Define Parameter in Code (reference path, camera path)

calibFolder = variable.calibFolder

# Camera Position Reference
referenceFilename = variable.referenceFilename

# Camera Calibration
CamCalibration = variable.CamCalibration

# --------------------------------------------------------------
# Set Path

# Select output folder

output_folder = utils.output_folder(Metashape)

# Image folder

image_folder = utils.image_folder(output_folder)

# Saving doc with images loaded in chunk

photos = utils.find_files(image_folder, [".png", ".jpg", ".jpeg", ".tif", ".tiff"])
file_name = os.path.basename(os.path.normpath(output_folder))

doc.save(output_folder + '/Model/' + file_name + '.psx')

chunk.addPhotos(photos) # Adds Photos to Chunk

doc.save()
print(str(len(chunk.cameras)) + " images loaded")

# --------------------------------------------------------------
# Calibration

#Import Camera Calibration

utils.imp_camcalib(Metashape, chunk, calib, sensor, calibFolder, CamCalibration)

#Define Coordinatesystem

chunk.crs = variable.crs1

#Import Reference

utils.imp_reference(Metashape, doc, chunk, calibFolder, referenceFilename, variable.crs1)

print("reference imported")

# --------------------------------------------------------------
# Process Start

utils.process(Metashape, doc, chunk, 0) # 0=Better Quality/Longer Times 1=Lower Quality/Faster

# --------------------------------------------------------------
# Script time info

print("Script finished in {:.2f} seconds".format(time.time() - start_time))

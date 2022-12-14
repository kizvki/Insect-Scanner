# Insect photogrammetry processing script
# Metashape verison 1.8
#
# Code written by Ernst Herb
#
# Multi process script
#----------------------------------------

import Metashape
import os, sys, time
import utils
import variable

# Checking Compatibility
utils.check_compatibility(Metashape)

start_time = time.time() #Start Time for script duration calculation

# --------------------------------------------------------------
# Define Parameter in Code (reference path, camera path)

calibFolder = variable.calibFolder

# Camera Position Reference
referenceFilename = variable.referenceFilename

# Camera Calibration
CamCalibration = variable.CamCalibration

# --------------------------------------------------------------
# Process Input Selection

process_amount = Metashape.app.getInt(label = "Select the amount to process", value = 1)

print("{} will be processed".format(process_amount))

# --------------------------------------------------------------
# Set Path Loop

count = 0

output_folder = []
file_name = [None]*process_amount
image_folder = []

for i in range(process_amount):
    
    # Select output folder

    output_folder_add = utils.output_folder(Metashape)

    output_folder.append(output_folder_add)

    print(output_folder)

    file_name[count] = os.path.basename(os.path.normpath(output_folder[count]))

    # Select image folder

    image_folder_add = utils.image_folder(output_folder[count])

    image_folder.append(image_folder_add)

    print(image_folder)
    
    count += 1

# --------------------------------------------------------------
# Process loop

count2 = 0

for i in range(process_amount):
    photos = utils.find_files(image_folder[count2], [".png", ".jpg", ".jpeg", ".tif", ".tiff"])

    doc = Metashape.Document() # Simplifing variables

    doc.save(output_folder[count2] + '/Model/' + file_name[count2] + '.psx')

    # Simplifing variables
    chunk = doc.addChunk()
    camera = chunk.cameras  
    sensor = Metashape.Sensor
    calib = Metashape.Calibration()

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
    # Process
    
    utils.process(Metashape, doc, chunk, 0) # 0=Better Quality/Longer Times 1=Lower Quality/Faster
    print("Process [{}] Done".format(count2+1))
    
    count2 += 1

# --------------------------------------------------------------
# Script time info

print("Script finished in {:.2f} seconds".format(time.time() - start_time))

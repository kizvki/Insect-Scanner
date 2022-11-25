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

output_folder = [None]*process_amount
file_name = [None]*process_amount
image_folder = [None]*process_amount

for i in range(process_amount):
    
    # Select output folder
    
    Metashape.app.messageBox("Process [{}] | Select output folder:".format(count+1))
    
    output_folder[count] = Metashape.app.getExistingDirectory("Select output folder:")

    file_name[count] = os.path.basename(os.path.normpath(output_folder[count]))

    if (variable.foldersec not in file_name[count]): # Checks if selected output folder contains foldersec
        raise Exception("Unrecognized folder. Please select folder {}".format(variable.foldersec))

    # Select image folder

    image_folder[count] = output_folder[count] + '/edof' # Image folder relative to output folder
    if (len(image_folder[count]) == 0):
        raise Exception("No images found")
    
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

# Insect photogrammetry processing script
# Metashape verison 1.8
#
# Code written by Ernst Herb
#
# Multi process script
#----------------------------------------

import Metashape
import os, sys, time
import glob
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
# Select Folder that contains all Projects

Metashape.app.messageBox("Select folder with projects:")
    
output_folder = Metashape.app.getExistingDirectory("Select folder with projects:")

project_folder_list = glob.glob(output_folder + "/" + variable.foldersec + "*", recursive = True)

image_folder_list = [x + '/' + variable.imgfolder for x in project_folder_list] #Adds to the project path the image folder to get image folder path

#Process amount gets defined
process_amount = len(project_folder_list)

print("{} will be processed".format(process_amount))

# --------------------------------------------------------------
# Process loop

count2 = 0

for i in range(process_amount):
    photos = utils.find_files(image_folder_list[count2], [".png", ".jpg", ".jpeg", ".tif", ".tiff"])

    file_name = os.path.basename(os.path.normpath(project_folder_list[count2]))

    doc = Metashape.Document() # Simplifing variables

    doc.save(project_folder_list[count2] + '/Model/' + file_name + '.psx')

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

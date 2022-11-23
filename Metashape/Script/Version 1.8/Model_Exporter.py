# Insect photogrammetry processing script
# Metashape verison 1.8
#
# Code written by Ernst Herb
#
# Export all model in subfolder
#----------------------------------------

import Metashape
import os, sys, time
import glob
from pathlib import Path
import utils
import variable

# Checking Compatibility

utils.check_compatibility(Metashape)

start_time = time.time() #Start Time for script duration calculation

# --------------------------------------------------------------
# Select output folder

Metashape.app.messageBox("Select folder with projects:")
    
output_folder = Metashape.app.getExistingDirectory("Select folder with projects:")

project_files_list = glob.glob(output_folder + "/*/Model/ETHZ-ENT*.psx", recursive = True) #Get project files

count = 0

for i in range(len(project_files_list)):
    
    Project = project_files_list[count] # Extracts project path
    
    Project_Path = os.path.dirname(os.path.abspath(Project)) # Extracts project path without file name
    
    file_name = Path(Project).stem # Extracts only Project name without extension
    
    doc = Metashape.Document()
    
    doc.open(Project)
    
    chunk = doc.chunk
    
    crs1 = Metashape.CoordinateSystem('LOCAL_CS["Local Coordinates (mm)",LOCAL_DATUM["Local Datum",0],UNIT["millimetre",0.001,AUTHORITY["EPSG","1025"]]]')
    
    chunk.exportModel(path=Project_Path + '/' + file_name + '.obj', binary=True, precision=6, texture_format = Metashape.ImageFormatPNG, save_texture=True, save_uv=True, save_normals=True, save_colors=True, save_alpha=True, colors_rgb_8bit=True, format=Metashape.ModelFormatOBJ, crs = crs1)
    
    count += 1

# --------------------------------------------------------------
# Script time info



print("{} models exported".format(len(project_files_list)))

print("Script finished in {:.2f} seconds".format(time.time() - start_time))

print('Processing finished, results saved to ' + output_folder)

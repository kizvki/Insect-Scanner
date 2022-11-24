# Insect photogrammetry processing script
# Metashape verison 1.8
#
# Code written by Ernst Herb
#----------------------------------------

import os
import variable

# Function: Set output folder
def output_folder(Metashape):
    
    Metashape.app.messageBox("Select output folder:")
        
    output_folder = Metashape.app.getExistingDirectory("Select output folder:")
    
    file_name = os.path.basename(os.path.normpath(output_folder))

    if (variable.foldersec not in file_name): # Checks if selected output folder contains foldersec
        raise Exception("Unrecognized folder. Please select folder {}".format(variable.foldersec))
        
    return output_folder
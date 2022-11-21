# Insect photogrammetry processing script
# Metashape verison 1.8
#
# Code written by Ernst Herb
#----------------------------------------

import os

# Function: Set output folder
def output_folder(Metashape):
    
    Metashape.app.messageBox("Select output folder:")
        
    output_folder = Metashape.app.getExistingDirectory("Select output folder:")
    
    file_name = os.path.basename(os.path.normpath(output_folder))

    if ('ETHZ-ENT' not in file_name): # Checks if selected output folder contains ETHZ-ENT
        raise Exception("Unrecognized folder. Please select folder ETHZ-ENT")
        
    return output_folder
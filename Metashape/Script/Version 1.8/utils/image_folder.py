# Insect photogrammetry processing script
# Metashape verison 1.8
#
# Code written by Ernst Herb
#----------------------------------------

import variable

# Function: Set image folder
def image_folder(output_folder):
    image_folder = output_folder + '/' + variable.imgfolder # Image folder relative to output folder
    if (len(image_folder) == 0):
        raise Exception("No images found")
    return image_folder
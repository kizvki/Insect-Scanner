# Insect photogrammetry processing script
# Metashape verison 1.8
#
# Code written by Ernst Herb
#----------------------------------------


# Function: Set image folder
def image_folder(output_folder):
    image_folder = output_folder + '/edof' # Image folder relative to output folder
    if (len(image_folder) == 0):
        raise Exception("No images found")
    return image_folder
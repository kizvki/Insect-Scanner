# Insect photogrammetry processing script
# Metashape verison 1.8
#
# Code written by Ernst Herb
#----------------------------------------

import variable

# Function: Checking Compatibility
def check_compatibility(Metashape):
    compatible_major_version = variable.version
    found_major_version = ".".join(Metashape.app.version.split('.')[:2])
    if found_major_version != compatible_major_version:
        raise Exception("Incompatible Metashape version: Metashape is running on version {}. Script is written for version {}".format(found_major_version, compatible_major_version))
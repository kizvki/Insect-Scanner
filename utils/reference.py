# Insect photogrammetry processing script
# Metashape verison 1.8
#
# Code written by Ernst Herb
#----------------------------------------


# Function: Import reference
def imp_reference(Metashape, doc, chunk, calibFolder, referenceFilename, crs1):

    chunk.importReference(path = calibFolder + "\\" + referenceFilename + ".txt", format = Metashape.ReferenceFormatCSV, columns = "nxyz[XYZ]", delimiter = " ", crs = crs1, skip_rows = 1, ignore_labels = False, create_markers = False)

    chunk.updateTransform()

    doc.save()
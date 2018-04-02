# Lesson 1
from arcpy import env


env.workspace = r"C:\Users\Skenny02\Documents\ArcGIS\Projects\ArcPyPro_Class_1\ArcPyPro_Class_1.gdb"
env.overwriteOutput = True
spot = env.workspace
print (spot)


import arcpy
mappp = arcpy.mp.ArcGISProject(r"C:\Users\Skenny02\Documents\ArcGIS\Projects\ArcPyPro_Class_1\ArcPyPro_Class1.aprx")
whichMaps = mappp.listMaps() # get a list of maps matchign the filter

for m in whichMaps:
  print(m.name)


lesson1 = project.listMaps("ArcPy Pro Lesson 1")[0]
layersss = lesson1.listLayers()
for lll in layersss:
    print(lll.name)

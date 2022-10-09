>>> topic = "Geographic Information Systems"
>>> topic.count("i")
----------------------------------------------------------------------------------
>>> mytext = "GIS is cool"
>>> print mytext.lower( )
----------------------------------------------------------------------------------
>>> mytext = "GIS is cool"
>>> print mytext.upper( 
----------------------------------------------------------------------------------
>>> mytext = "GIS is cool"
>>> print mytext.title( 
----------------------------------------------------------------------------------
>>> mystring = "Geographic Information Systems"
>>> mystring[11:22]
----------------------------------------------------------------------------------
>>> mystring = "Geographic Information Systems"
>>> mystring.find("Info")
----------------------------------------------------------------------------------
>>> mystring = "Geographic Information Systems"
>>> mystring.find("info")
----------------------------------------------------------------------------------
>>> list_gis = ["Geographic", "Information", "Systems"]
>>> string_gis = " "
>>> string_gis.join(list_gis)
'Geographic Information Systems'
----------------------------------------------------------------------------------
>>> pythonstring = "Geoprocessing using Python scripts"
>>> pythonlist = pythonstring.split(" ")
>>> pythonlist
['Geoprocessing', 'using', 'Python', 'scripts']
----------------------------------------------------------------------------------
>>> mytext = "Commenting scripts is good"
>>> mytext.strip("Cdo")
'mmenting scripts is g'
----------------------------------------------------------------------------------
>>> mytext = "Commenting scripts is good"
>>> mytext.rstrip("Cdo")
'Commenting scripts is g'
----------------------------------------------------------------------------------
>>> mygis = "Geographic Information Systems"
>>> mygis.replace("Systems", "Science")
'Geographic Information Science'
----------------------------------------------------------------------------------
>>> myfile = "streams.shp"
>>> myfile.replace(".shp", "")
'streams'
----------------------------------------------------------------------------------
>>> temp = 100
>>> print "The temperature is {0} degrees".format(temp)
The temperature is 100 degrees
----------------------------------------------------------------------------------
>>> username = "Paul"
>>> password = "surf$&9*"
>>> print "{0}'s password is {1}".format(username, password)
Paul's password is surf$&9*
----------------------------------------------------------------------------------
>>> cities.sort(reverse = True)
>>> print cities
['Eugene', 'Denver', 'Cleveland', 'Baltimore', 'Austin']
>>> cities.sort
>>> print cities
['Austin', 'Baltimore', 'Cleveland', 'Denver', 'Eugene']
----------------------------------------------------------------------------------
>>> cities = ["Austin", "Baltimore", "Cleveland", "Denver", "Eugene"]
>>> del cities[2]
>>> cities
['Austin', 'Baltimore', 'Denver', 'Eugene']
----------------------------------------------------------------------------------
>>> list1 = [1, 2, 3, 4]
>>> list2 = [11, 12, 13, 14]
>>> list1.extend(list2)
>>> list1
[1, 2, 3, 4, 11, 12, 13, 14]
----------------------------------------------------------------------------------
>>> mylist = ["The", "quick", "fox", "jumps", "over", "the", "lazy",
"dog"]
>>> mylist.index("the")
5
----------------------------------------------------------------------------------
import win32com.client
gp = win32com.client.Dispatch("esriGeoprocessing.GpDispatch.1")---------------------------------------------------------------------------

----------------------------------------------------------------------------------
import arcpy
arcpy.env.workspace = "C:/Data/study.gdb"
buffer = arcpy.Buffer_analysis("str", "str_buf", "100 METERS")
count = arcpy.GetCount_management(buffer).getOutput(0)
print str(count)
----------------------------------------------------------------------------------
arcpy.ImportToolbox("sampletools.tbx", mytools)
----------------------------------------------------------------------------------
import arcpy
tools = arcpy.ListTools("*_analysis")
for tool in tools:
print arcpy.Usage(tool)
----------------------------------------------------------------------------------
import arcpy
prjfile = "C:/Data/myprojection.prj"
spatialref = arcpy.SpatialReference(prjfile)
----------------------------------------------------------------------------------
import arcpy
prjfile = "C:/Data/streams.prj"
spatialref = arcpy.SpatialReference(prjfile)
myref = spatialref.name
print myref
----------------------------------------------------------------------------------
import arcpy
out_path = "C:/Data"
out_name = "lines.shp"
prjfile = "C:/Data/streams.prj"
spatialref = arcpy.SpatialReference(prjfile)
arcpy.CreateFeatureclass_management(out_path, out_name, "POLYLINE", "",
"", "", spatialref)
----------------------------------------------------------------------------------
import arcpy
from arcpy import env
env.cellSize = 30
----------------------------------------------------------------------------------
count = arcpy.GetMessageCount( )
print arcpy.GetMessage(count-1)
----------------------------------------------------------------------------------
print arcpy.GetMaxSeverity()
----------------------------------------------------------------------------------
import arcpy
arcpy.env.workspace = "C:/Data"
result = arcpy.GetCount_management("streams.shp")
count = result.messageCount
print result.getMessage(count-1)
----------------------------------------------------------------------------------
import arcview
----------------------------------------------------------------------------------
if arcpy.CheckProduct("arcinfo") == "Available":
----------------------------------------------------------------------------------
import arcpy
print arcpy.ProductInfo( )
----------------------------------------------------------------------------------
import arcpy
from arcpy import env
env.workspace = "C:/Data"
if arcpy.CheckExtension("3D") == "Available":
arcpy.CheckOutExtension("3D")
arcpy.Slope_3d("dem", "slope", "DEGREES")
arcpy.CheckInExtension("3D")
else:
print "3D Analyst license is unavailable."
----------------------------------------------------------------------------------
import arcpy
arcpy.env.workspace = "C:/Data"
infc = "streams.shp"
clipfc = "study.shp"
outfc = "streams_clip.shp"
desc = arcpy.Describe(clipfc)
type = desc.shapeType
if type == "Polygon":
arcpy.Clip_analysis(infc, clipfc, outfc)
else:
print "The clip features are not polygons."
----------------------------------------------------------------------------------
import arcpy
element = "C:/Data/study.gdb/final"
desc = arcpy.Describe(element)
print "Dataset type: " + desc.datasetType

----------------------------------------------------------------------------------
import arcpy
arcpy.env.workspace = "C:/Data/study.gdb"
element = "roads"
desc = arcpy.Describe(element)
print "Data type: " + desc.dataType
print "File path: " + desc.path
print "Catalog path: " + desc.catalogPath
print "File name: " + desc.file
print "Base name: " + desc.baseName
print "Name: " + desc.name

----------------------------------------------------------------------------------
import arcpy
from arcpy import env
env.workspace = "C:/Data"
tifflist = arcpy.ListRasters("", "TIF")
for tiff in tifflist:
arcpy.BuildPyramids_management(tiff)
----------------------------------------------------------------------------------
import arcpy
from arcpy import env
env.workspace = "C:/Data"
fieldlist = arcpy.ListFields("roads.shp")
for field in fieldlist:
print "{0} is a type of {1} with a length of {2}".format(field.name,
field.type, field.length)
----------------------------------------------------------------------------------
import arcpy
from arcpy import env
env.workspace = "C:/Data/study.gdb"
fcs = arcpy.ListFeatureClasses( )
fcs.sort( )
print fcs
fcs.sort(reverse = True)
print fcs
----------------------------------------------------------------------------------
import arcpy
install = arcpy.GetInstallInfo( )
for key in install:
print "{0}: {1}".format(key, install[key])
----------------------------------------------------------------------------------
arcpy.da.InsertCursor(in_table, field_names)
arcpy.da.SearchCursor(in_table, field_names, {where_clause}, {spatial_
reference}, {explore_to_points})
arcpy.da.UpdateCursor(in_table, field_names, {where_clause}, {spatial_
reference}, {explore_to_points})
----------------------------------------------------------------------------------
import arcpy
fc = "C:/Data/study.gdb/roads"
cursor = arcpy.da.SearchCursor(fc, ["STREETNAME"])
for row in cursor:
print "Streetname = {0}".format(row[0])
----------------------------------------------------------------------------------
import arcpy
fc = "C:/Data/study.gdb/roads"
cursor = arcpy.da.InsertCursor(fc, ["STREETNAME"])
cursor.insertRow(["NEW STREET"])
----------------------------------------------------------------------------------
cursor = arcpy.da.InsertCursor(fc, ["STREETNAME"])
x = 1
while x <= 5:
cursor.insertRow(["NEW STREET"])
x += 1
----------------------------------------------------------------------------------
import arcpy
fc = "C:/Data/study.gdb/zones"
cursor = arcpy.da.UpdateCursor(fc, ["ACRES", "SHAPE_AREA"])
for row in cursor:
row[0] = row[1] / 43560
cursor.updateRow(row)
----------------------------------------------------------------------------------
import arcpy
fc = "C:/Data/study.gdb/roads"
cursor = arcpy.da.UpdateCursor(fc, ["STREETNAME"])
for row in cursor:
if row[0] == "MAIN ST":
 cursor.deleteRow()
----------------------------------------------------------------------------------
import arcpy
fc = "C:/Data/study.gdb/roads"
cursor = arcpy.da.UpdateCursor(fc, ["STREETNAME"])
for row in cursor:
if row[0] == "MAIN ST":
 cursor.deleteRow( )
del row
del cursor
----------------------------------------------------------------------------------
import arcpy
fc = "C:/Data/study.gdb/roads"
cursor = arcpy.da.SearchCursor(fc, ["NAME", "CLASSCODE"], '"CLASSCODE" =
1')
for row in cursor:
print row[0]
del row
del cursor
----------------------------------------------------------------------------------
import arcpy
fc = "C:/Data/zipcodes.shp"
fieldname = "CITY"
delimfield = arcpy.AddFieldDelimiters(fc, fieldname)
cursor = arcpy.da.SearchCursor(fc, ["NAME", "CLASSCODE"], delimfield + "
= 'LONGWOOD'")
for row in cursor:
print row[0]
del row
del cursor
----------------------------------------------------------------------------------
import arcpy
infc = "C:/Data/zipcodes.shp"
fieldname = "CITY"
outfc = "C:/Data/zip_select.shp"
delimfield = arcpy.AddFieldDelimiters(infc, fieldname)
arcpy.Select_analysis(infc, outfc, delimfield + " = 'LONGWOOD'")
----------------------------------------------------------------------------------
import arcpy
import os
from arcpy import env
env.workspace = "C:/Data"
outworkspace = "C:/Data/test/study.gdb"
fclist = arcpy.ListFeatureClasses( )
for shapefile in fclist:
fcname = arcpy.Describe(shapefile).basename
newfcname = arcpy.ValidateTableName(fcname)
outfc = os.path.join(outworkspace, newfcname)
arcpy.CopyFeatures_management(shapefile, outfc)
----------------------------------------------------------------------------------
import arcpy
fc = "C:/Data/roads.shp"
fieldname = arcpy.ValidateFieldName("NEW%^")
arcpy.AddField_management(fc, fieldname, "TEXT", "", "", 12)
----------------------------------------------------------------------------------
import arcpy
from arcpy import env
env.workspace = "C:/Data"
unique_name = arcpy.CreateUniqueName("buffer.shp")
arcpy.Buffer_analysis("roads.shp", unique_name, "100 FEET")
----------------------------------------------------------------------------------
import arcpy
from arcpy import env
env.workspace = "C:/Data/study.gdb"
fc = "roads"
fullname = arcpy.ParseTableName(fc)
namelist = fullname.split(", ")
databasename = namelist[0]
ownername = namelist[1]
fcname = namelist[2]
print databasename
print ownername
print fcname
----------------------------------------------------------------------------------
f = open("C:/Data/mytext.txt")
while True:
char = f.read(1)
if not char: break
<function>
f.close()
----------------------------------------------------------------------------------
f = open("C:/Data/mytext.txt")
while True:
line = f.readline( )
if not line: break
<function>
f.close()
----------------------------------------------------------------------------------
input = open("C:/Data/coordinates.txt")
output = open("C:/Data/coordinates_clean.txt", "w")
for line in input:
str = line.replace("ID: ", "")
str = str.replace(", Latitude:", "")
str = str.replace(", Longitude:", "")
output.write(str)
input.close( )
output.close( )
----------------------------------------------------------------------------------
import arcpy
fc = "C:/Data/roads.shp"
cursor = arcpy.da.SearchCursor(fc, ["SHAPE@LENGTH"])
length = 0
for row in cursor:
length += row[0]
print length
----------------------------------------------------------------------------------
import arcpy
fc = "C:/Data/hospitals.shp"
cursor = arcpy.da.SearchCursor(fc, ["SHAPE@XY"])
for row in cursor:
x, y = row[0]
print("{0}, {1}".format(x,y))
----------------------------------------------------------------------------------
import arcpy
from arcpy import env
env.workspace = "C:/Data"
fc = "roads.shp"
cursor = arcpy.da.SearchCursor(fc, ["OID@", "SHAPE@"])
for row in cursor:
print("Feature {0}: ".format(row[0]))
for point in row[1].getPart(0):
 print("{0}, {1}".format(point.X, point.Y))
----------------------------------------------------------------------------------
import arcpy
from arcpy import env
env.workspace = "C:/Data"
fc = "roads.shp"
cursor = arcpy.SearchCursor(fc, ["OID@", "SHAPE@"])
for row in cursor:
print("Feature {0}: ".format(row[0]))
partnum = 0
for part in row[1]:
 print("Part {0}:".format(partnum))
 for point in part:
 print("{0}, {1}".format(point.X, point.Y))
 partnum += 1
----------------------------------------------------------------------------------
for point in part:
if point:
 print("{0}, {1}".format(point.Y, point.Y))
else:
 print "Interior Ring"
partnum += 1 
----------------------------------------------------------------------------------
import arcpy, fileinput, string
from arcpy import env
env.overwriteOutput = True
infile = "C:/Data/points.txt"
fc = "C:/Data/newpoly.shp"
arcpy.CreateFeatureclass_management("C:/Data", fc, "Polygon")
----------------------------------------------------------------------------------
cursor = arcpy.da.InsertCursor(fc, ["SHAPE@"])
array = arcpy.Array( )
point = arcpy.Point( )
----------------------------------------------------------------------------------
for line in fileinput.input(infile):
point.ID, point.X, point.Y = line.split( )
----------------------------------------------------------------------------------
import arcpy, fileinput, os
from arcpy import env
env.workspace = "C:/Data"
infile = "C:/Data/points.txt"
fc = "newpoly.shp"
arcpy.CreateFeatureclass_management("C:/Data", fc, "Polygon")
cursor = arcpy.da.InsertCursor(fc, ["SHAPE@"])
array = arcpy.Array( )
point = arcpy.Point( )
for line in fileinput.input(infile):
point.ID, point.X, point.Y = line.split( )
array.add(point)
polygon = arcpy.Polygon(array)
cursor.insertRow([polygon])
fileinput.close( )
del cursor
----------------------------------------------------------------------------------
import arcpy
fc = "C:/Data/hospitals.shp"
prjfile = "C:/projections/GCS_NAD_1983.prj"
spatialref = arcpy.SpatialReference(prjfile)
cursor = arcpy.da.SearchCursor(fc, ["SHAPE@"], "", spatialref)
----------------------------------------------------------------------------------
for row in cursor:
point = row[0]
output.write(str(point.X) + " " + str(point.Y) + "\n")
----------------------------------------------------------------------------------
import arcpy
from arcpy import env
env.workspace = "C:/Data"
fc = "hospitals.shp"
prjfile = "C:/Projections/GCS_NAD_1983.prj"
spatialref = arcpy.SpatialReference(prjfile)
cursor = arcpy.da.SearchCursor(fc, ["SHAPE@"], "", spatialref)
output = open("result.txt", "w")
for row in cursor:
point = row[0]
output.write(str(point.X) + " " + str(point.Y) + "\n")
output.close( )
----------------------------------------------------------------------------------
import arcpy
from arcpy import env
env.workspace = "C:/Data"
coordlist = [[17.0, 20.0], [125.0, 32.0], [4.0, 87.0]]
pointlist = []
for x, y in coordlist:
point = arcpy.Point(x,y)
pointgeometry = arcpy.PointGeometry(point)
pointlist.append(pointgeometry)
arcpy.Buffer_analysis(pointlist, "buffer.shp", "10 METERS")
----------------------------------------------------------------------------------
import arcpy
fc = "C:/Data/roads.shp"
geolist = arcpy.CopyFeatures_management(fc, arcpy.Geometry( ))
length = 0
for geometry in geolist:
length += geometry.length
print "Total length: " + length
----------------------------------------------------------------------------------
import arcpy
from arcpy import env
env.workspace = "C:/raster"
raster = "landcover.tif"
desc = arcpy.Describe(raster)
print desc.dataType
print desc.bandCount
print desc.compressionType
----------------------------------------------------------------------------------
import arcpy
from arcpy import env
env.workspace = "C:/raster"
rasterband = "landcover.tif"
desc = arcpy.Describe(raster)
print desc.meanCellHeight
print desc.meanCellWidth
print desc.pixelType
spatialref = desc.spatialReference
print spatialref.name
print spatialref.linearUnitName
----------------------------------------------------------------------------------
import arcpy
from arcpy import env
env.workspace = "C:/raster"
rasterband = "img.tif/Band_1"
desc = arcpy.Describe(rasterband)
print desc.meanCellHeight
print desc.meanCellWidth
print desc.pixelType
----------------------------------------------------------------------------------
import arcpy
from arcpy.sa import *
elevraster = arcpy.Raster("C:/raster/elevation")
outraster = Slope(elevraster)
----------------------------------------------------------------------------------
import arcpy
from arcpy.sa import *
f1 = arcpy.Raster("C:/raster/factor1")
f2 = arcpy.Raster("C:/raster/factor2")
f3 = arcpy.Raster("C:/raster/factor3")
temp1raster = Plus(f1, f2)
temp2raster = Plus(temp1raster, f3)
outraster = Divide(temp2raster, "3")
outraster.save("C:/raster/final")
----------------------------------------------------------------------------------
import arcpy
from arcpy.sa import *
f1raster = arcpy.Raster("C:/raster/factor1")
f2raster = arcpy.Raster("C:/raster/factor2")
f3raster = arcpy.Raster("C:/raster/factor3")
outraster = (f1 + f2 + f3) / 3
outraster.save("C:/raster/final")
----------------------------------------------------------------------------------
import arcpy
from arcpy import env
from arcpy.sa import *
elevfeet = arcpy.Raster("C:/raster/elevation")
elevmeter = elevfeet * 0.3048
env.cellsize = 30
env.mask = "C:/raster/studyarea.shp"
elevrasterclip = ApplyEnvironment(elevmeter)
elevrasterclip.save("C:/raster/dem30_m")
----------------------------------------------------------------------------------
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/raster"
myremap = RemapValue([["Barren", 1], ["Mixed Forest", 4], ["Coniferous
Forest", 0], ["Cropland", 2], ["Grassland", 3], ["Shrub", 3], ["Water",
0]])
outreclass = Reclassify("landuse", "S_VALUE", myremap)
outreclass.save("C:/raster/lu_recl")
----------------------------------------------------------------------------------
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = ("C:/raster")
myremap = RemapRange([[1, 1000, 0], [1000, 2000, 1], [2000, 3000, 2],
[3000, 4000, 3]])
outreclass = Reclassify("elevation", "TYPE", myremap)
outreclass.save("C:/raster/elev_recl")
----------------------------------------------------------------------------------
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/raster"
mynbr = NbrRectangle(5, 5, "CELL")
outraster = FocalStatistics("landuse", mynbr, "VARIETY")
outraster.save("C:/raster/lu_var")
----------------------------------------------------------------------------------
import arcpy, scipy
from arcpy.sa import *
inRaster = arcpy.Raster("C:/raster/myraster")
my_array = RasterToNumPyArray(inRaster)
outarray = scipy.<module>.<function>(my_array)
outraster = NumPyArrayToRaster(outarray)
outraster.save("C:/raster/result")
----------------------------------------------------------------------------------
import arcpy
dataset = "C:/map/boundary.shp"
spatialRef = arcpy.Describe(dataset).spatialReference
mapdoc = arcpy.mapping.MapDocument("C:/map/final.mxd")
for df in arcpy.mapping.ListDataFrames(mapdoc):
df.spatialReference = spatialRef
df.scale = 24000
df.panToExtent(lyr.getExtent( ))
df.zoomToSelectedFeatures( )
del mapdoc
----------------------------------------------------------------------------------
import arcpy
myDoc = arcpy.mapping.MapDocument("CURRENT")
dflist = arcpy.mapping.ListDataFrames(mapdoc)
lyrlist = arcpy.mapping.ListLayers(mapdoc, "", dflist[0])
for lyr in lyrlist:
lyr.showLabels = True
del lyrlist
----------------------------------------------------------------------------------
import arcpy
myDoc = arcpy.mapping.MapDocument("CURRENT")
lyrlist = arcpy.mapping.ListLayers(mapdoc)
for lyr in lyrlist:
if lyr.name == "hospitals":
 lyr.showLabels = True
del lyrlist
----------------------------------------------------------------------------------
import arcpy
myDoc = arcpy.mapping.MapDocument("CURRENT")
dflist = arcpy.mapping.ListDataFrames(mapdoc)
lyrlist = arcpy.mapping.ListLayers(mapdoc, "", dflist[0])
for lyr in lyrlist:
if lyr.supports("SHOWLABELS") == True:
 lyr.showLabels = True
del lyrlist
----------------------------------------------------------------------------------
import arcpy
mapdoc = arcpy.mapping.MapDocument("CURRENT")
brokenlist = arcpy.mapping.ListBrokenDataSources(mapdoc)
for lyr in brokenlist:
print lyr.name
lyr.dataSource
del mapdoc
----------------------------------------------------------------------------------
import arcpy
mapdoc = arcpy.mapping.MapDocument("CURRENT")
mapdoc.findAndReplaceWorkspacePaths("C:/mydata", "C:/newdata")
mapdoc.save( )
del mapdoc
----------------------------------------------------------------------------------
import arcpy
mapdoc = arcpy.mapping.MapDocument("C:/mydata/project.mxd")
mapdoc.replaceWorkspaces("C:/mydata/shapes", "SHAPEFILE_WORKSPACE",
"C:/mydata/database.gdb", "FILEGDB_WORKSPACE")
mapdoc.save( )
del mapdoc
----------------------------------------------------------------------------------
import arcpy
mapdoc = arcpy.mapping.MapDocument("C:/mydata/project.mxd")
lyrlist = arcpy.mapping.ListLayers(mapdoc):
for lyr in lyrlist:
if lyr.supports("DATASOURCE"):
 if lyr.dataSource == "C:/mydata/database.gdb/hospitals":
lyr.findAndReplaceWorkspacePath("database.gdb", "newdata.
gdb")
mapdoc.save( )
del mapdoc
----------------------------------------------------------------------------------
import arcpy
mapdoc = arcpy.mapping.MapDocument("C:/mydata/project.mxd")
lyrlist = arcpy.mapping.ListLayers(mapdoc):
for lyr in lyrlist:
if lyr.supports("DATASOURCE"):
 if lyr.dataSource == "C:/mydata/hospitals.shp":
lyr.replaceDataSource("C:/mydata/hospitals.shp", "SHAPEFILE_
WORKSPACE", "C:/mydata/newhospitals.shp")
mapdoc.save( )
del mapdoc
----------------------------------------------------------------------------------
import arcpy
mapdoc = arcpy.mapping.MapDocument(r"C:\mydata\project.mxd")
elemlist = arcpy.mapping.ListLayoutElements(mapdoc)
for elem in elemlist:
print elem.name & " " & elem.type
del mapdoc
----------------------------------------------------------------------------------
import arcpy
mapdoc = arcpy.mapping.MapDocument("C:/mydata/project.mxd")
title = arcpy.mapping.ListLayoutElements(mapdoc, "TEXT_ELEMENT")[0]
title.text = "New Study Area"
mapdoc.save( )
del mapdoc
----------------------------------------------------------------------------------
import arcpy
mapdoc = arcpy.mapping.MapDocument("CURRENT")
elemlist = arcpy.mapping.ListLayoutElements(mapdoc, "PICTURE_ELEMENT")
for elem in elemlist:
if elem.name == "photo1":
 elem.sourceImage = "C:/myphotos/newimage.jpg"
mapdoc.save( )
del mapdoc
----------------------------------------------------------------------------------
import arcpy
mapdoc = arcpy.mapping.MapDocument("CURRENT")
df = arcpy.mapping.ListDataFrames(mapdoc)[0]
lyr1 = arcpy.mapping.Layer("C:/mydata/Streets.lyr")
lyr2 = arcpy.mapping.Layer("C:/mydata/Ortho.lyr")
legend = arcpy.mapping.ListLayoutElements(mxd, "LEGEND_ELEMENT")[0]
legend.autoAdd = True
arcpy.mapping.AddLayer(df, lyr1, "BOTTOM")
legend.autoAdd = False
arcpy.mapping.AddLayer(df, lyr2, "BOTTOM")
mapdoc.save( )
del mapdoc
----------------------------------------------------------------------------------
import arcpy
mapdoc = arcpy.mapping.MapDocument("C:/project/study.mxd")
arcpy.mapping.ExportToJPEG(mapdoc, "C:/project/final.jpg", "", "", "",
600)
del mapdoc
----------------------------------------------------------------------------------
import arcpy
pdfpath = "C:/project/MapBook.pdf"
pdfdoc = arcpy.mapping.PDFDocumentCreate(pdfpath)
pdfdoc.appendPages("C:/project/Cover.pdf")
pdfdoc.appendPages("C:/project/Map1.pdf")
pdfdoc.appendPages("C:/project/Map2.pdf")
pdfdoc.saveAndClose( )
del pdfdoc
----------------------------------------------------------------------------------
import arcpy
pdfpath = "C:/project/MapBook.pdf"
pdfdoc = arcpy.mapping.PDFDocumentCreate(pdfpath)
mapdoc = arcpy.mapping.MapDocument("C:/project/Maps.mxd")
mapdoc.dataDrivenPages.exportToPDF("C:/project/Maps.pdf")
pdfdoc.appendPages("C:/project/Cover.pdf")
pdfdoc.appendPages("C:/project/Maps.pdf")
pdfdoc.saveAndClose( )
del mapdoc
----------------------------------------------------------------------------------
class LicenseError(Exception):
pass
import arcpy
from arcpy import env
try:
if arcpy.CheckExtension("3D") == "Available":
 arcpy.CheckOutExtension("3D")
else:
 raise LicenseError
env.workspace = "C:/raster"
arcpy.Slope_3d("elevation", "slope")
except LicenseError:
print "3D license is unavailable"
except:
print arcpy.GetMessages(2)
finally:
arcpy.CheckInExtension("Spatial")
----------------------------------------------------------------------------------
try:
import arcpy
import traceback
##multiple lines of code here
except:
tb = sys.exc_info( )[2]
tbinfo = traceback.format_tb(tb)[0]
pymsg = "PYTHON ERRORS:\nTraceback info:\n" + tbinfo + "\nError
Info:\n" + str(sys.exc_info( )[1])
msgs = "ArcPy ERRORS:\n" + arcpy.GetMessages(2) + "\n"
arcpy.AddError(pymsg)
arcpy.AddError(msgs)
----------------------------------------------------------------------------------
import arcpy
fc = arcpy.GetParameterAsText(0)
result = arcpy.GetCount_management(fc)
fcount = int(result.getOutput(0))
if fcount == 0:
arcpy.AddError(fc + " has no features.")
else:
arcpy.AddMessage(fc + " has " + str(fcount) + " features.")
----------------------------------------------------------------------------------
import arcpy
infc = arcpy.GetParameterAsText(0)
outfc = arcpy.GetParameterAsText(1)
if arcpy.Exists(outfc):
arcpy.AddIDMessage("Error", 12, outfc)
else:
arcpy.CopyFeatures_management(infc, outfc)
----------------------------------------------------------------------------------
import arcpy
import os
from arcpy import env
env.workspace = arcpy.GetParameterAsText(0)
outworkspace = arcpy.GetParameterAsText(1)
fclist = arcpy.ListFeatureClasses( )
fcount = len(fclist)
arcpy.SetProgressor("step", "Copying shapefiles to geodatabase...", 0,
fcount, 1)
for fc in fclist:
arcpy.SetProgressorLabel("Copying " + fc + "...")
fcdesc = arcpy.Describe(fc)
outfc = os.path.join(outworkspace, fcdesc.baseName)
arcpy.CopyFeatures_management(fc, outfc)
arcpy.SetProgressorPosition( )
arcpy.ResetProgressor()
----------------------------------------------------------------------------------
import arcpy
import os
import sys
from arcpy import env
scratchws = env.scratchWorkspace
scriptpath = sys.path[0]
toolpath = os.path.dirname(scriptpath)
if not env.scratchWorkspace:
scratchws = os.path.join(toolpath, "Scratch/scratch.gdb")
----------------------------------------------------------------------------------

----------------------------------------------------------------------------------

----------------------------------------------------------------------------------

----------------------------------------------------------------------------------

----------------------------------------------------------------------------------

----------------------------------------------------------------------------------

----------------------------------------------------------------------------------

----------------------------------------------------------------------------------

----------------------------------------------------------------------------------

----------------------------------------------------------------------------------

----------------------------------------------------------------------------------

----------------------------------------------------------------------------------

----------------------------------------------------------------------------------

----------------------------------------------------------------------------------

----------------------------------------------------------------------------------

----------------------------------------------------------------------------------

----------------------------------------------------------------------------------

----------------------------------------------------------------------------------

----------------------------------------------------------------------------------

----------------------------------------------------------------------------------

----------------------------------------------------------------------------------

----------------------------------------------------------------------------------

----------------------------------------------------------------------------------

----------------------------------------------------------------------------------

----------------------------------------------------------------------------------

----------------------------------------------------------------------------------

----------------------------------------------------------------------------------

----------------------------------------------------------------------------------

----------------------------------------------------------------------------------

----------------------------------------------------------------------------------

----------------------------------------------------------------------------------

----------------------------------------------------------------------------------

----------------------------------------------------------------------------------

----------------------------------------------------------------------------------

----------------------------------------------------------------------------------

----------------------------------------------------------------------------------

----------------------------------------------------------------------------------

----------------------------------------------------------------------------------

----------------------------------------------------------------------------------

----------------------------------------------------------------------------------

----------------------------------------------------------------------------------

----------------------------------------------------------------------------------

----------------------------------------------------------------------------------

----------------------------------------------------------------------------------

----------------------------------------------------------------------------------

----------------------------------------------------------------------------------

----------------------------------------------------------------------------------

----------------------------------------------------------------------------------

----------------------------------------------------------------------------------

----------------------------------------------------------------------------------

----------------------------------------------------------------------------------

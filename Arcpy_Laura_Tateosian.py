>>> import arcpy
>>> arcpy.env.overwriteOutput = True
---------------------------------------------------------------------------------

>>> import sys
>>> sys.path

----------------------------------------------------------------------

>>> import os
>>> os.listdir('C:/gispy/data/ch02')

----------------------------------------------------------------------

>>> arcpy.Exists('C:/gispy/data/ch05/park.shp')

----------------------------------------------------------------------

>>> arcpy.env.workspace = 'C:/gispy/data/ch06/'
>>> inputRaster = 'getty_rast'
>>> outputFile = 'output.txt'
>>> arcpy.RasterToASCII_conversion(inputRaster, outputFile)

----------------------------------------------------------------------

>>> arcpy.env.overwriteOutput = True
>>> arcpy.Buffer_analysis('C:/gispy/data/ch06/park.shp','parkBuffer.shp', 0.25 miles')

----------------------------------------------------------------------

data = 'C:/gispy/data/ch06/data1.shp'
fieldName = 'result'
expr = 5
arcpy.CalculateField_management(data, fieldName, expr, 'PYTHON')

----------------------------------------------------------------------
                          
expr = '2*!measure! - !coverage!'
arcpy.CalculateField_management(data, fieldName, expr,'PYTHON')

----------------------------------------------------------------------

data = 'C:/gispy/data/ch06/special_regions.shp'
fieldName = 'PolyArea'
expr = '!shape.area!'
arcpy.CalculateField_management(data, fieldName, expr,'PYTHON')
                          
----------------------------------------------------------------------

>>> inputFiles = ['park.shp', 'special_regions.shp', 'workzones.shp']
>>> arcpy.Merge_management(inputFiles, 'mergedData.shp')
                          
----------------------------------------------------------------------

>>> inputFiles = 'park.shp;special_regions.shp;workzones.shp'
>>> arcpy.Merge_management(inputFiles, 'mergedData2.shp')

----------------------------------------------------------------------

>>> vt = arcpy.ValueTable()
>>> vt.addRow('park.shp')
>>> vt.addRow('special_regions.shp')
>>> vt.addRow('workzones.shp')
>>> arcpy.Merge_management(vt, 'mergedData3.shp')

----------------------------------------------------------------------

>>> inputFiles = [['park.shp', 2], ['special_regions.shp', 2],['workzones.shp',1]]
>>> arcpy.Intersect_analysis(inputFiles, 'intersectData.shp')

----------------------------------------------------------------------

>>> vt = arcpy.ValueTable()
>>> vt.addRow('park.shp 2')
>>> vt.addRow('special_regions.shp 2')
>>> vt.addRow('workzones.shp 1')
>>> arcpy.Intersect_analysis(vt, 'intersectData.shp')

----------------------------------------------------------------------

>>> arcpy.env.workspace = 'C:/gispy/data/ch06/'
>>> arcpy.env.overwriteOutput = True
>>> # Use default values for the last 6 args .
>>> arcpy.PolygonNeighbors_analysis('park.shp', 'PN.dbf')
>>> # Another way to use default values for the last 6 args .
>>> arcpy.PolygonNeighbors_analysis('park.shp', 'PN.dbf', ' # ',' #',' #', ' #', ' #', ' #') 

----------------------------------------------------------------------

# avgNearNeighbor.py
# Purpose: Analyze crime data to determine if spatial
# patterns are statistically significant.
import arcpy
arcpy.env.workspace = 'C:/gispy/data/ch06'
annResult = arcpy.AverageNearestNeighbor_stats('points.shp',
 'Euclidean Distance')
print 'Average Nearest Neighbor Output'
print 'Nearest neighbor ratio: {0}'.format(annResult.getOutput(0))
print 'z-score: {0}'.format(annResult.getOutput(1))
print 'p-value: {0}'.format(annResult.getOutput(2))
print 'Expected Mean Distance: {0}'.format(annResult.getOutput(3))
print 'Observed Mean Distance: {0}'.format(annResult.getOutput(4))

----------------------------------------------------------------------
>>> import arcpy
>>> arcpy.env.workspace = 'C:/gispy/data/ch06/'
>>> arcpy.env.overwriteOutput = True
>>> inRast = 'getty_rast'
>>> arcpy.CheckOutExtension('Spatial') u'CheckedOut'
>>> outputRast = arcpy.sa.SquareRoot(inRast)
>>> outputRast.save()
>>> outputRast
----------------------------------------------------------------------   

# computeRastEquation.py
# Purpose: Calculate 5 * 'getty_rast' - 2
import arcpy
arcpy.env.overwriteOutput = True
arcpy.env.workspace = 'C:/gispy/data/ch06/rastSmall.gdb'
arcpy.CheckOutExtension('Spatial')
outRast1 = arcpy.sa.Times(5, 'dataRast')
outRast2 = arcpy.sa.Minus(outRast1, 2)
outRast2.save('equationRast')
del outRast1, outRast2 
                      
----------------------------------------------------------------------

>>> rastObj = arcpy.Raster('dataRast')
>>> outRast = 5*rastObj - 2
>>> outRast.save('equationRast2')
>>> del outRast
                          
----------------------------------------------------------------------   

>>> r1 = arcpy.Raster('out1')
>>> r2 = arcpy.Raster('out2')
>>> r3 = arcpy.Raster('out3')
>>> outRast = (5*r1*r2*r3)/2
>>> outRast.save('output')
>>> del outRast
                          
----------------------------------------------------------------------

>>> myData = 'C:/gispy/data/ch06/xyData.txt'
>>> arcpy.MakeXYEventLayer_management(myData, 'x','y','tmpLayer')
                          
----------------------------------------------------------------------   

>>> countRes = arcpy.GetCount_management('tmpLayer')
>>> countRes.getOutput(0)
                          
---------------------------------------------------------------------- 

>>> fireDamage = 'special_regions.shp'
>>> fireBuffer = fireDamage[:-4] + 'Buffer.shp'
>>> fireBuffer
                          
----------------------------------------------------------------------   

#buffer_clip.py (hard-coded version)
# Purpose: Buffer a zone and use it to clip another file
# Input: No arguments needed.
import arcpy
arcpy.env.overwriteOutput = True
arcpy.env.workspace = 'C:/gispy/data/ch06'
outDir = 'C:/gispy/scratch/'
# Set buffer params
fireDamage = 'special_regions.shp'
fireBuffer = outDir + fireDamage[:-4] + 'Buffer.shp'
bufferDist = '1 mile'
# Set clip params
park = 'park.shp'
clipOutput = outDir + park[:-4] + 'DamageBuffer.shp'
arcpy.Buffer_analysis(fireDamage, fireBuffer,bufferDist)
print '{0} created.'.format(fireBuffer)
arcpy.Clip_analysis(park, fireBuffer, clipOutput)
print '{0} created.'.format(clipOutput)
                          
----------------------------------------------------------------------

# addLengthField.py
# Purpose: Add a field containing polygon lengths to the shapefile.
# Usage: No arguments needed.
import arcpy
arcpy.env.workspace = 'C:/gispy/data/ch06'
inputFile = 'special_regions.shp'
fieldName = 'Length'                          
arcpy.AddField_management(inputFile, fieldName, 'FLOAT')
arcpy.CalculateField_management(inputFile, fieldName,'!shape.length!', 'PYTHON')
                          
----------------------------------------------------------------------   

# callInventory.py
# Purpose: Call the inventory tool.
import arcpy
arcpy.env.workspace = 'C:/gispy/sample_scripts/ch06'
inputDir = 'C:/gispy/data/ch06/'
arcpy.ImportToolbox('customTools.tbx')
arcpy.Inventory_custom(inputDir, 'SUMMARY_ONLY', 'summaryFile.txt')
                          
----------------------------------------------------------------------

# boundingGeom.py
 # Purpose: Find the minimum bounding geometry of a set of features.
 import arcpy
 arcpy.env.overwriteOutput = True
 arcpy.env.workspace = 'C:/gispy/data/ch07'
 inputFeatures = 'park.shp'
 outputFeatures = 'boundingBoxes.shp'
 arcpy.MinimumBoundingGeometry_management(inputFeatures,outputFeatures)

----------------------------------------------------------------------   

 # boundingGeomV2.py (soft-coded using arcpy)
 # Purpose: Find the minimum bounding geometry of a set of features.
 # Usage: workspace, input_features, output_features
 # Example: C:/gispy/data/ch07 park.shp boundingBoxes.shp
 import arcpy
 arcpy.env.overwriteOutput = True
 arcpy.env.workspace = arcpy.GetParameterAsText(0)
 inputFeatures = arcpy.GetParameterAsText(1)
 outputFeatures = arcpy.GetParameterAsText(2)
 arcpy.MinimumBoundingGeometry_management(inputFeatures,outputFeatures)
                          
----------------------------------------------------------------------

 # boundingGeomV3.py (soft-coded using sys)
 # Purpose: Find the minimum bounding geometry of a set of features.
 # Usage: workspace, input_features, output_features
 # Example: C:/gispy/data/ch07 park.shp boundingBoxes.shp
 import arcpy, sys
 arcpy.env.overwriteOutput = True
 arcpy.env.workspace = sys.argv[1]
 inputFeatures = sys.argv[2]
 outputFeatures = sys.argv[3]
 arcpy.MinimumBoundingGeometry_management(inputFeatures,outputFeatures)

----------------------------------------------------------------------   

 # argSpacing.py
 # Purpose: Print the number of incoming user
 # arguments and the first 2 arguments.
 import arcpy
 numArgs = arcpy.GetArgumentCount()
 print 'Number of user arguments: {0}'.format(numArgs)
 print 'The first argument: {0}'.format(arcpy.GetParameterAsText(0))
 print 'The second argument: {0}'.format(arcpy.GetParameterAsText(1))
                          
-----------------------------------------------------------------
>>> import os
>>> inFile = 'C:/gispy/data/ch07/park.shp'
>>> # Get only the file name.
>>> fileName = os.path.basename(inFile)
>>> fileName
                          
----------------------------------------------------------------------
>>> # Get only the path .
>>> filePath = os.path.dirname(inFile)
>>> filePath
-----------------------------------------------------------------
>>> # Join the arguments into a valid file path .
>>> fullPath = os.path.join(filePath, fileName)
>>> fullPath
                          
----------------------------------------------------------------------
# copyFile.py
 # Purpose: Copy a file.
 # Usage: source_full_path_file_name, destination_directory
 # Example: C:/gispy/data/ch07/park.shp C:/gispy/scratch/
 # The C:/gispy/scratch directory must already exist
 # for this example to work.
 import arcpy, os
 inputFile = arcpy.GetParameterAsText(0)
 outputDir = arcpy.GetParameterAsText(1)
 baseName = os.path.basename(inputFile)
 outputFile = os.path.join(outputDir, baseName)
 arcpy.Copy_management(inputFile, outputFile)
 print 'inputFile =', inputFile
 print 'outputDir =', outputDir
 print
 print 'baseName =', baseName
 print 'outputFile = ', outputFile

-----------------------------------------------------------------
# compact.py
 # Purpose: Compact a file
 # Usage: Full path file name of an mdb file.
 # Example: C:/gispy/data/ch07/cities.mdb
 import arcpy, os
 # Get user input and extract base file name.
 fileName = arcpy.GetParameterAsText(0)
 baseName = os.path.basename(fileName)
 # Check size
 size = os.path.getsize(fileName)
 print '{0} file size before compact: {1} bytes.'.format(baseName,
 size)
 # Compact the file
 arcpy.Compact_management(fileName)
 # Check size
 size = os.path.getsize(fileName)
 print '{0} file size AFTER compact: {1} bytes'.format(b aseName,size) 
                          
----------------------------------------------------------------------

# scriptPath.py
 # Purpose: List the files in the current directory.
 # Usage: No user arguments needed.
 import os
 # Get the script location
 scriptPath = os.path.abspath(__file__)
 scriptDir = os.path.dirname(scriptPath)
 print '{0} contains the following files:'.format(scriptDir)
 print os.listdir(scriptDir)
                          
-----------------------------------------------------------------
arcpy.GetParameterAsText(index)
sys.argv
os.path.dirname(fileName)
os.path.basename(fileName)
os.path.splitext(fileName)
os.path.abspath(path)
                          
----------------------------------------------------------------------

if classType == 'major highway' or classType == 'river' or \
classType == 'stream' or classType == 'bridge':
                          print classType, '--',FID
else:
                          print 'Other--', FID
                          
-----------------------------------------------------------------

specialTypes = ['highway', 'river', 'stream', 'bridge']
if classType in specialTypes:
print classType, '--',FID
else:
print 'Other--', FID
                          
                          
---------------------------------------------------------------------- 

specialTypes = ['highway', 'river', 'stream', 'bridge']
if classType not in specialTypes:
print classType, '--', FID

-----------------------------------------------------------------

>>> whereClause1 = 'RECNO >= 400'
>>> type(whereClause1)
<type 'str'>
                          
                          
----------------------------------------------------------------------

 # where_clause1.py
 # Purpose: Select features with high reclassification numbers.
 # Usage: No arguments needed.
 import arcpy
 arcpy.env.workspace = 'C:/gispy/data/ch09'
 inputFile = 'park.shp'
 whereClause = 'RECNO >= 400'
 arcpy.Select_analysis(inputFile, 'C:/gispy/scratch/out.shp', whereClause)
                          
-----------------------------------------------------------------

whereClause3 = "COVER = 'orch'"
                          
----------------------------------------------------------------------

>>> fieldName = 'COVER'
>>> fieldValue = 'orch'
>>> whereClause5 = "{0} = '{1}'".format(fieldName, fieldValue)
>>> whereClause5
"COVER = 'orch'"
                          
-----------------------------------------------------------------

# where_clause2.py
# Purpose: Extract raster features by attributes based on
# user input.
# Usage: fieldName fieldValue
# Example input: COUNT 6000
import arcpy, sys
arcpy.env.workspace = 'C:/gispy/data/ch09'
arcpy.CheckOutExtension('Spatial')
inputRast = 'getty_rast'
fieldName = sys.argv[1]
fieldValue = sys.argv[2]
whereClause = '{0} > {1}'.format(fieldName, fieldValue)
outputRast = arcpy.sa.ExtractByAttributes(inputRast, whereClause)
outputRast.save('C:/gispy/scratch/attextract')
del outputRast 
                          
----------------------------------------------------------------------

>>> maxArea = 20000
>>> coverType = 'woods'
>>> whereClause = "Shape_area < {0} AND \
COVER ='{1}'".format(maxArea, coverType)
>>> arcpy.SelectLayerByAttribute_management(tmp,'NEW_SELECTION',whereClause)

-----------------------------------------------------------------

# describeRaster.py
# Purpose: Report the format of raster input file.
# Usage: workspace, raster_dataset
# Example: C:/gispy/data/ch09 getty.tif
import arcpy
arcpy.env.workspace = arcpy.GetParameterAsText(0)
data = arcpy.GetParameterAsText(1)
desc = arcpy.Describe(data)
if desc.dataType == 'RasterDataset':
print 'Image format: {0}'.format(desc.format)
                          
----------------------------------------------------------------------

>>> desc = arcpy.Describe('C:/gispy/data/ch09/getty.tif')
>>> desc.dataType
u'RasterDataset'
>>> if desc.shapeType == 'Polyline' and \
dsc.dataType in ['FeatureClass', 'Shapefile']:
                          
-----------------------------------------------------------------

# smoothLineCompound.py
# Usage: workspace, features_with_line_geometry
# Example 1: C:/gispy/data/ch09 trails.shp
# Example 2: C:/gispy/data/ch09 park.shp
import arcpy
arcpy.env.overwriteOutput = True
arcpy.env.workspace = arcpy.GetParameterAsText(0)
data = arcpy.GetParameterAsText(1)

outFile = 'C:/gispy/scratch/smoothOut'
desc = arcpy.Describe(data)
if desc.dataType in ['FeatureClass' ,'ShapeFile'] and desc.shapeType == 'Polyline':
 result = arcpy.SmoothLine_cartography(data, outFile,'BEZIER_INTERPOLATION')
 print 'Smooth line created {0}.'.format(result.getOutput(0))
                          
----------------------------------------------------------------------

# smoothLineNested.py
# Usage: workspace, features_with_line_geometry
# Example 1: C:/gispy/data/ch09 trails.shp
# Example 2: C:/gispy/data/ch09 park.shp
# Example 3: C:/gispy/data/ch09 getty.tif
import arcpy arcpy.env.overwriteOutput = True
arcpy.env.workspace =arcpy.GetParameterAsText(0)
data = arcpy.GetParameterAsText(1)
outFile = 'C:/gispy/scratch/output'
desc = arcpy.Describe(data)
if desc.dataType in ['FeatureClass' ,'ShapeFile']:
if desc.shapeType == 'Polyline':
 result = arcpy.SmoothLine_cartography(data, outFile,'BEZIER_INTERPOLATION')
 print 'Smooth line created {0}.'.format(result.getOutput(0))
else:
 print 'Warning: shape type is {0}. Smooth Line only workson Polyline shape types. '.format( desc.shapeType)
else:
print "Warning: Input data type must be 'FeatureClass' or 'ShapeFile'."
print 'Input dataType:', desc.dataType
                          
-----------------------------------------------------------------

# scriptPathOptionalv1.py
# Purpose: List the files in the given directory or
# the current directory.
# Usage: {directory_path}
import sys, os
if len(sys.argv) == 2:
 workingDir = sys.argv[1]
else:
 # Get the script location
 scriptPath = os.path.abspath(__file__)
 workingDir = os.path.dirname(scriptPath)
print '{0} contains the following files:'.format(workingDir)
print os.listdir(workingDir)
                          
                          
---------------------------------------------------------------------- 

# scriptPathOptionalv2.py
# Purpose: List the files in the given directory or
# the current directory.
# Usage: {directory_path}
import arcpy, os
if arcpy.GetParameterAsText(0):
 workingDir = arcpy.GetParameterAsText(0)
else:
 # Get the script location
 scriptPath = os.path.abspath( __ file__)
workingDir = os.path.dirname(scriptPath)
print '{0} contains the following files:'.format(workingDir)
print os.listdir(workingDir)
                          
-----------------------------------------------------------------

# distanceConvertv1.py
# Purpose: Converts km to miles and vice versa.
# Usage: numerical_distance, unit_of_measure
# Example: 5 km
import sys
dist = float(sys.argv[1]) # Cast string to float
unit = sys.argv[2]
mileList = ['mi','mi.','mile','miles']
if unit.lower() in mileList:
 output = dist*1.6
 print '{0} {1} is equivalent to {2} kilometers(s).'.format(dist, unit, output)
else:
 output = dist*.62
 print '{0} {1} is equivalent to {2} mile(s).'.format(dist, unit, output)
                          
----------------------------------------------------------------------

# distanceConvertv2.py
# Purpose: Converts km to miles and vice versa.
# Usage: numerical_distance, {unit_of_measure}
# Example: 5 km
import sys
numArgs = len(sys.argv)
# If no user arguments are given, exit the script and warn the user.
if numArgs == 1:
 print 'Usage: numeric_distance {distance_unit (mi or km)}'
 print 'Example: 5 km'
 sys.exit(0) # exit the script
# If only one user argument is given, set the unit to miles.
if numArgs < 3:
 unit = 'miles'
 print '''Warning: No distance unit provided.
 Assuming input is in miles.'''
else:
 # Get the unit provided by the user
 unit = sys.argv[2]
# Get the numeric distance (cast string to float).
dist = float(sys.argv[1])
# Perform conversion.
mileList = ['mi','mi.','mile','miles']
if unit.lower() in mileList:
 output=dist*1.6
 print '{0} {1} is equivalent to {2} kilometers(s).'.format(dist, unit, output)
else:
 output = dist*.62
 print '{0} {1} is equivalent to {2} mile(s).'.format(dist, unit, output)
                          
-----------------------------------------------------------------

>>> myDir = 'C:/gispy/data/ch09/happyGoat'
>>> os.path.exists(myDir)
False
>>> os.mkdir(myDir)
>>> os.path.exists(myDir)
True
>>> os.mkdir(myDir)
                          
----------------------------------------------------------------------

if not os.path.exists(myDir):
 os.mkdir(myDir) 

-----------------------------------------------------------------

# copyFilev2.py
# Purpose: Copy a file.
# Usage: source_directory destination_directory file_to_backup
# Example: C:/gispy/data/ch09/ C:/gispy/scratch/backup park.shp
# The example works even if the C:/gispy/scratch/backup
# directory doesn't exist yet.
import arcpy, os
arcpy.env.workspace = arcpy.GetParameterAsText(0)
outputDir = arcpy.GetParameterAsText(1)
fileToCopy = arcpy.GetParameterAsText(2)
if not os.path.exists( outputDir ):
 os.mkdir( outputDir )
outputFile = os.path.join(outputDir, fileToCopy)
arcpy.Copy_management( fileToCopy, outputFile )
print 'source =', os.path.join(arcpy.env.workspace, fileToCopy)
print 'destination =', outputFile
                          
----------------------------------------------------------------------

>>> outPath = 'C:/gispy/data/ch09/'
>>> gdbName = 'happyHorse.gdb'
>>> if not arcpy.Exists(outPath + gdbName):
... arcpy.CreateFileGDB_management(outPath, gdbName)                          
-----------------------------------------------------------------

1 # normalRastsLoop.py
 2 # Purpose: Create 3 raster containing random values .
 3
 4 import arcpy
 5 arcpy.env.workspace = 'C:/gispy/data/ch10'
 7 arcpy.env.overwriteOutput = True
 8 arcpy.CheckOutExtension('Spatial')
 9
10 n = 1
11 while n < 4:
12 outputName = 'out{0}'.format(n)
13 tempRast = arcpy.sa.CreateNormalRaster()
14 tempRast.save(outputName)
15 n = n + 1
16 del tempRast
17 print 'Normal raster creation complete.' 

                          
----------------------------------------------------------------------

 1 # point2Line.py
 2 # Purpose: Create a set of line features from a
 3 # set of point features in a list .
 4 import arcpy
 5 arcpy.env.workspace = 'C:/gispy/data/ch10'
 6 arcpy.env.overwriteOutput = True
 7
 8 theFiles = ['data1.shp', 'data2.shp','data3.shp','data4.shp']
 9 for currentFile in theFiles:
10 # Remove file extension from the current name.
11 baseName = currentFile[:-4]
12 # Create unique output name. E.g., 'data1Line.shp'.
13 outName = baseName + 'Line.shp'
14 arcpy.PointsToLine_management(currentFile,outName)
15 print '{0} created.'.format(outName)                         
-----------------------------------------------------------------
# bufferLoopRange.py
# Purpose: Buffer a park varying buffer distances from 1 to 5 miles .
import arcpy
arcpy.env.workspace = 'C:/gispy/data/ch10'
arcpy.env.overwriteOutput = True
inName = 'park.shp'
for num in range(1, 6):
# Set buffer distance based on num ('1 miles', '2 miles', ...)
distance = '{0} miles'.format(num)
# Set output name ('buffer1.shp', 'buffer2.shp', ...)
outName = 'buffer{0}.shp'.format(num)
arcpy.Buffer_analysis(inName, outName, distance)
print '{0} created.'.format(outName)
                          
----------------------------------------------------------------------

# copyLoop.py
# Purpose: Make a copy of each ASCII .txt extension file .
import arcpy, os
arcpy.env.workspace = 'C:/gispy/data/ch10'
outDir = 'C:/gispy/scratch/'
theFiles = os.listdir(arcpy.env.workspace)
for fileName in theFiles:
if fileName.endswith('.txt'):
 outName = outDir + fileName[:-4] + 'V2.txt'
 arcpy.Copy_management(fileName, outName)
 print '{0} created.'.format(outName)
                          
-----------------------------------------------------------------
>>> import os
>>> theDir = 'C:/gispy/data/ch10/pics'
>>> # os.listdir returns a list of the files
>>> theFiles = os.listdir(theDir)
>>> for fileName in theFiles:
... print os.path.exists(fileName) 

>>> fullName = os.path.join(theDir, fileName)
>>> os.path.exists(fullName)                         
                          
----------------------------------------------------------------------

# printModTime.py
# Purpose: For each file, print the time of most
# recent modification .
# Input: No arguments required .
import os, datetime
theDir = 'C:/gispy/data/ch10/pics'
theFiles = os.listdir(theDir)
for f in theFiles:
 fullName = os.path.join(theDir, f)
 # Get the modification time.
 print os.path.getmtime(fullName)
                          
-----------------------------------------------------------------

# listStuff.py
# Purpose: Use arcpy to list workspaces and tables .
import arcpy
arcpy.env.workspace = 'C:/gispy/data/ch11'
print '---Workspaces---'
workspaces = arcpy.ListWorkspaces()
for wspace in workspaces:
 print wspace
print '\n---Tables---'
tables = arcpy.ListTables()
for table in tables:
 print table
                          
---------------------------------------------------------------------- 

# listFields.py
# Purpose: List attribute table field properties.
import arcpy
arcpy.env.workspace = 'C:/gispy/data/ch11/'
fields = arcpy.ListFields('park.shp')
for fieldObject in fields:
 print 'Name: {0}'.format(fieldObject.name)
 print 'Length: {0}'.format(fieldObject.length)
 print 'Type: {0}'.format(fieldObject.type)
 print 'Editable: {0}'.format(fieldObject.editable)
 print 'Required: {0}\n'.format(fieldObject.required)
                          
-----------------------------------------------------------------

>>> # List all coverage, geodatabase, TIN, Raster, and CAD datasets.
>>> datasets = arcpy.ListDatasets('out*', 'GRID')
>>> for data in datasets:
... arcpy.Delete_management(data)
                          
----------------------------------------------------------------------                           

# batchBuffer.py
# Purpose: Buffer each feature class in the workspace .
import arcpy, os
arcpy.env.overwriteOutput = True
arcpy.env.workspace = 'C:/gispy/data/ch11/'
# GET a list of feature classes
fcs = arcpy.ListFeatureClasses()
for fc in fcs:
 # SET the output variable .
 fcBuffer = os.path.splitext(fc)[0] + 'Buffer.shp'
 # Call Buffer (Analysis) tool
 arcpy.Buffer_analysis(fc, fcBuffer, '1 mile')
 print '{0} created.'.format(fcBuffer)
                          
-----------------------------------------------------------------

# batchBufferv2.py
# Purpose: Buffer each feature class in the workspace and
# place output in a different workspace .
import arcpy, os
arcpy.env.overwriteOutput = True
# SET workspaces
arcpy.env.workspace = 'C:/gispy/data/ch11/'
outDir = 'C:/gispy/scratch/buffers'
if not os.path.exists(outDir):
 os.mkdir(outDir)
#GET a list of feature classes
fcs = arcpy.ListFeatureClasses()
for fc in fcs:
 # SET the output variable
 outName = os.path.splitext(fc)[0] + '_buffer.shp'
 fcBuffer = os.path.join(outDir, outName)
 # Call buffer tool
 arcpy.Buffer_analysis(fc, fcBuffer, '1 mile')
 print '{0} created in {1}.'.format(fcBuffer, outDir)
                          
----------------------------------------------------------------------

# tableLister.py
# Purpose: Create shapefiles from 'stations*' xy tables ,
# connect the points, and then find then
# intersection of the lines .
# Usage: workspace_containing_tables
# Example: C:/gispy/data/ch11/trains
import arcpy, os, sys
arcpy.env.workspace = sys.argv[1]
arcpy.env.overwriteOutput = True
tables = arcpy.ListTables('stations*', 'dBASE')
tempPoints = 'temporaryPointLayer'
for table in tables:
 # SET the output variable .
 lineFile = os.path.splitext(table)[0] + 'Line'
 # CALL geoprocessing tools .
 arcpy.MakeXYEventLayer_management(table, 'POINT_X',
 'POINT_Y', tempPoints)
 arcpy.PointsToLine_management(tempPoints, lineFile)
 print '\t{0}/{1} created.'.format(arcpy.env.workspace, lineFile)
# GET the list of lines and intersect the lines .
lineList = arcpy.ListFeatureClasses('stations*Line*')
arcpy.Intersect_analysis(lineList,'hubs','#', '0.5 mile', 'POINT')
print '{0}/hubs created.'.format(arcpy.env.workspace)
                          
-----------------------------------------------------------------

>>> listA = ['FID', 'Shape', 'COVER', 'RECNO']
>>> listB = [field.lower() for field in listA] # List comprehension
>>> listB
['fid', 'shape', 'cover', 'recno']
                          
----------------------------------------------------------------------

>>> listA = range(1,6)
>>> listA
[1, 2, 3, 4, 5]
>>> listB = [i*2 for i in listA]
>>> listB
[2, 4, 6, 8, 10]
                          
-----------------------------------------------------------------

>>> IDlist = ['000004', '000345', '003000', '000860']
>>> IDlist = [ID.lstrip('0') for ID in IDlist]
>>> IDlist
['4', '345', '3000', '860']
                          
----------------------------------------------------------------------

# argPrint.py
# Purpose: Print args with built-in enumerate function .
# Usage: Any arguments .
# Example input: 500 miles
import sys
for index, arg in enumerate(sys.argv):
 print 'Argument {0}: {1}'.format(index, arg)

-----------------------------------------------------------------

# point2LineV2.py (a modification of 'points2Line.py' from Ch. 10)
# Purpose: Use the enumerate function in the loop to create
# unique output names based on a number.
# Usage: No arguments needed.
import arcpy
arcpy.env.workspace = 'C:/gispy/data/ch12'
arcpy.env.overwriteOutput = True
outDir = 'C:/gispy/scratch/'
dFiles = ['data1.shp', 'data2.shp','data3.shp','data4.shp']
for index, currentFile in enumerate(dFiles):
 # Create a unique output names, 'Line1.shp,', 'Line2.shp' ...
 outputName = 'Line{0}.shp'.format(index)
 arcpy.PointsToLine_management(currentFile,
 outDir + outputName)
 print outputName
                          
----------------------------------------------------------------------

>>> listA = ['FID', 'Shape', 'COVER', 'RECNO']
>>> listB = ['OID', 'Geometry', 'String']
>>> zip(listA,listB)
[('FID', 'OID'), ('Shape', 'Geometry'), ('COVER', 'String')]
                          
-----------------------------------------------------------------

# walkPics.py
# Purpose: Demonstrate the os.walk function .
import os
myDir = 'C:/gispy/data/ch12/pics'
for root, dirs, files in os.walk(myDir):
 print 'root = {0}'.format(root)
 print 'dirs = {0}'.format(dirs)
 print 'files = {0}\n'.format(files)
                          
----------------------------------------------------------------------

# walkTXT.py
# Purpose: Walk and print the full path file names of
# 'txt' extension files in the input directory .
# Usage: input_directory
# Example: C:/gispy/data/ch12/wTest
import arcpy, os, sys
mydir = sys.argv[1]
for root, dirs, files in os.walk(mydir):
 arcpy.env.workspace = root
 for f in files:
 if f.endswith('.shp'):
 # Print the full path file name of f
 print '{0}/{1}'.format(root,f)
                          
-----------------------------------------------------------------

# osWalkBuffer.py
# Purpose: Walk and buffer the point shapefiles .
# Usage: input_directory output_directory
# Example: C:/gispy/data/ch12/wTest C:/gispy/scratch
import arcpy, os, sys
rootDir = sys.argv[1]
outDir = sys.argv[2]
arcpy.env.overwriteOutput = True
for root, dirs, files in os.walk(rootDir):
 arcpy.env.workspace = root
 fcs = arcpy.ListFeatureClasses('*', 'POINT')
 for f in fcs:
 # Set output name and perform geoprocessing on f
 outfile = outDir + '/' + os.path.splitext(f)[0] + \
 'buffer.shp'
 arcpy.Buffer_analysis(f, outfile, '1 mile')
 print '{0}/{1} buffer ouput: {2}'.format(root, f, outfile)
                          
---------------------------------------------------------------------- 

# buggyCode1.py
import os, sys
outputDir = os.path.dirname(sys.argv[1]) + '\outputFiles/
if not os.path.exists(outputDir)
 os.mkdir(outputDir)
                          
-----------------------------------------------------------------

# buggyFreq.py
# Purpose: Find frequency of each value in each string field.
import arcpy
arcpy.env.overwriteOutput = True
arcpy.env.workspace = 'C:/gispy/data/ch13/smallTest.gdb'
featureList = arcpy.ListFeatureClasses()
for inputFile in featureList:
 fields = arcpy.ListFields(inputFile, '*', 'String')
 for field in fields:
 fieldName = field.name
 outTable = inputFile + fieldName + 'freq'
 arcpy.Frequency_analysis(inputFile, outTable, fieldName)
 print 'Output table created: {0}'.format(outTable)
                          
----------------------------------------------------------------------                           

 # multRast.py
 import arcpy, sys
 # Set multiplication factor
 factor = float(sys.argv[1])
 arcpy.env.overwriteOutput = True
 arcpy.env.worspace = 'C:/gispy/data/ch14/rastTester.gdb'
 arcpy.CheckOutExtension('Spatial')
 # Get raster list & multiply each by a factor.
 rasterList = arcpy.ListRasters()
 for rasterImage in rasterList:
 rasterObj = arcpy.Raster(rasterImage)
 rastMult = rasterObj * factor
 rastMult.save(rasterImage + '_out')
 del rastMult
                          
-----------------------------------------------------------------

# doubleMyNumber.py
import sys
try:
 number = float(sys.argv[1])
 product = 2*number
 print 'The doubled number is {0}'.format(product)
except:
 print 'An error occurred.'
 print 'Please enter a numerical argument.'
print 'Good bye!'
                          
----------------------------------------------------------------------

# slopeTry.py
import sys
rise = sys.argv[1]
run = sys.argv[2]
try:
 print 'Rise: {0} Run: {1}'.format(rise, run)
 slope = float(rise)/float(run)
 print 'Slope = rise/run'
except ZeroDivisionError:
 slope = 'Undefined (line is vertical)'
except ValueError:
 print 'Usage: <numeric rise> <numeric run>'
 slope = 'Not found'
print 'Slope:', slope                          

-----------------------------------------------------------------

>>> inputFile = 'C:/gispy/data/ch14/cover.shp'
>>> count = arcpy.GetCount_management(inputFile)
>>> print arcpy.GetMessages() 
                          
----------------------------------------------------------------------

>>> arcpy.GetMessageCount()
                          
-----------------------------------------------------------------

print arcpy.GetMessage (arcpy.GetMessageCount() - 1)
                          
----------------------------------------------------------------------

# bufferTry.py
 import arcpy, sys, os
 arcpy.env.overwriteOutput = True
 try:
inputFile = sys.argv[1]
buff = os.path.splitext(inputFile)[0] + 'Buff.shp'
arcpy.Buffer_analysis(inputFile, buff, '1 mile')
print '{0} created.'.format(buff)
 except arcpy.ExecuteError:
print arcpy.GetMessages()
 except IndexError:
print 'Usage: <full path shapefile name>

-----------------------------------------------------------------

# bufferLoopTry.py
 # Purpose: Buffer the feature classes in a workspace.
 # Usage: No arguments needed.
 import arcpy, os
 arcpy.env.overwriteOutput = True
 arcpy.env.workspace = 'C:/gispy/data/ch14'
 outDir = 'C:/gispy/scratch/'
 fcs = arcpy.ListFeatureClasses()
 distance = '500 meters'
 for fc in fcs:
 outFile = outDir + os.path.splitext(fc)[0] + 'Buff.shp'
 try:
 arcpy.Buffer_analysis(fc, outFile, distance)
 print 'Created: {0}'.format(outFile)
 except arcpy.ExecuteError:
 print arcpy.GetMessage(2)                         
                          
----------------------------------------------------------------------

# bufferTry.py
 import arcpy, sys, os
 arcpy.env.overwriteOutput = True
 try:
inputFile = sys.argv[1]
buff = os.path.splitext(inputFile)[0] + 'Buff.shp'
arcpy.Buffer_analysis(inputFile, buff, '1 mile')
print '{0} created.'.format(buff)
 except arcpy.ExecuteError:
print arcpy.GetMessages()
 except IndexError:
print 'Usage: <full path shapefile name>
                          
-----------------------------------------------------------------

 # bufferLoopDistTry.py
 # Purpose: Buffer the input file by the given distance.
 # Usage: input_filename numeric_distance
 # Example input: C:/gispy/data/ch14/cover.shp 3
 import arcpy, sys, os
 arcpy.env.workspace = os.path.dirname(sys.argv[1])
 fc = os.path.basename(sys.argv[1])
 outDir = 'C:/gispy/scratch/'
 arcpy.env.overwriteOutput = False
 maxDist = float(sys.argv[2])
 i = 1
 while i <= maxDist:
 try:
 outFile = outDir + os.path.splitext(fc)[0] + str(i) + \
 'Buff.shp'
 distance = str(i) + ' miles'
 arcpy.Buffer_analysis(fc, outFile, distance)
 print 'Created: ', outFile
 except arcpy.ExecuteError:
 print arcpy.GetMessage(3)
 i = i + 1
                          
----------------------------------------------------------------------

import sys, arcpy
if len(sys.argv) > 1:
 arcpy.env.workspace = sys.argv[1]
else:
 arcpy.env.workspace = 'C:/gispy/data/ch14'
for rast in arcpy.ListRasters():
 print rast                         
-----------------------------------------------------------------

import sys, arcpy
try:
 arcpy.env.workspace = sys.argv[1]
except IndexError:
 arcpy.env.workspace='C:/gispy/data/ch14'
for rast in arcpy.ListRasters():
 print rast
                          
---------------------------------------------------------------------- 

import sys, arcpy
try:
 arcpy.env.workspace = sys.argv[1]
except IndexError:
 print 'Usage: <input workspace>'
 sys.exit(0)
for rast in arcpy.ListRasters():
 print rast
                          
-----------------------------------------------------------------

def printBird():
 print """
 ,,, ::.
 <*~) ;;
 ( @}//
 ''
 """ 
                          
----------------------------------------------------------------------                           

# deleteFCS.py
 # Purpose: Clear workspace of unwanted files.
 # Usage: No arguments needed.
 import arcpy
 arcpy.env.workspace = 'C:/gispy/data/ch15/scratch'
 def delBuffFCS():
 '''Delete feature classes with names containing "Buff".'''
 fcs = arcpy.ListFeatureClasses('*Buff*')
 for fc in fcs:
 arcpy.Delete_management(fc)
 print '{0} deleted.'.format(fc)
 def delNamedFCS(delString):
 '''Delete feature classes with names containing delString.'''
 wildcard = '*{0}*'.format(delString)
 fcs = arcpy.ListFeatureClasses(wildcard)
 for fc in fcs:
 arcpy.Delete_management(fc)
 print '{0} deleted.'.format(fc)
 delBuffFCS()
 delNamedFCS('Out') 
-----------------------------------------------------------------

# excerpt from batchBuff.py
def batchBuffer(workspace, featType, outSuffix, buffDistance):
 '''For a given workspace, buffer each
 feature class of a given feature type.'''
 arcpy.env.workspace = workspace
 fcs = arcpy.ListFeatureClasses('*', featType)
 for fc in fcs:
 fcParts = os.path.splitext(fc)
 outputName = fcParts[0] + outSuffix + fcParts[1]
 try:
 arcpy.Buffer_analysis(fc, outputName, buffDistance)
 print '{0} created.'.format(outputName)
 except:
 print 'Buffering {0} failed.'.format(fc)

batchBuffer('C:/gispy/data/ch15', 'Polygon', 'Buff', '1 mile')                      
----------------------------------------------------------------------

# setEnv1.py
import arcpy
def setEnviron1():
 arcpy.env.workspace = 'C:/gispy/data/ch15'
 arcpy.env.overwriteOutput = True
setEnviron1()
-------------------------
# setEnv2.py
import arcpy
def setEnviron2(workspace, overwriteVal):
 arcpy.env.workspace = workspace
 arcpy.env.overwriteOutput = overwriteVal
wSpace = 'C:/gispy/data/ch15/tester.gdb'
overwrite = False
setEnviron2(wSpace, overwrite)

-----------------------------------------------------------------

# setEnv3.py
import arcpy, sys
wSpace = sys.argv[1]
overwrite = sys.argv[2]
def setEnviron3(workspace, overwriteVal):
 arcpy.env.workspace = workspace
 arcpy.env.overwriteOutput = overwriteVal
setEnviron3(wSpace, overwrite)
                          
----------------------------------------------------------------------

def setEnviron4(workspace, overwriteVal = True):
 arcpy.env.workspace = workspace
 arcpy.env.overwriteOutput = overwriteVal
-----------------------------------------------------------------

# excerpt from fieldHandler.py
import arcpy
def getFieldNames(data):
 '''Get a list of field names.'''
 fields = arcpy.ListFields(data)
 fnames = [f.name for f in fields]
 return fnames
                          
----------------------------------------------------------------------

# (but the intersection output is not deleted since this line
# of code is placed after the 'return' statement).
import arcpy
arcpy.env.workspace = 'C:/gispy/data/ch15/tester.gdb'
arcpy.env.overwriteOutput = True
def countIntersection(dataList):
 '''Calculate the number of features in the intersection.'''
 tempData = 'intersectOut'
 arcpy.Intersect_analysis(dataList, tempData)
 res = arcpy.GetCount_management(tempData)
 print '{0} created.'.format(tempData)
 return int(res.getOutput(0))
 #uh-oh! The deletion is not going to happen.
 arcpy.Delete_management(tempData)
 print '{0} deleted.'.format(tempData)
inputData = ['schools','workzones']
count = countIntersection(inputData)
print 'There are {0} intersections.'.format(count)

-----------------------------------------------------------------

if __name__== '__main__':
 print '\nIn listManager.py, test string2List: '
 theString = 'z;x;y'
theList = string2List(';' , theString)
print '{0} -> {1}'.format(theString,theList)
print 'Zowee!'
                          
----------------------------------------------------------------------

>>> import time
>>> time.ctime()
>>>time.sleep(10)                       
-----------------------------------------------------------------

>>> import datetime
>>> dt = datetime.datetime(1999, 12 ,31, 23, 59)
>>> dt
datetime.datetime(1999, 12, 31, 23, 59)
>>> dt.hour
                          
----------------------------------------------------------------------

>>> # Create a cursor
>>> fc = 'C:/gispy/data/ch17/fires.shp'
>>> cursor = arcpy.da.SearchCursor (fc, ['FireName', 'FID'])
>>> row = cursor.next()
>>> row
(u'MEADOW', 0)
>>> row[0]
u'MEADOW'
>>> row[1]
0
                          
-----------------------------------------------------------------

>>> # Create a cursor with access to ALL the fields.
>>> cursor = arcpy.da.SearchCursor( fc, '*')
>>> cursor.fields
                          
---------------------------------------------------------------------- 

 # printTableExclude.py
 # Purpose: Print the names of the non-geometry non-OID type
 # fields in the input file and the value of these
 # fields for each record.
 # Usage: No script arguments required.
 import arcpy
def excludeFields(table, types=[]):
 '''Return a list of fields minus those with
 specified field types'''
 fieldNames = []
 fds = arcpy.ListFields(table)
 for f in fds:
 if f.type not in types:
 fieldNames.append(f.name)
 return fieldNames
 fc = 'C:/gispy/data/ch17/fires.shp'
 excludeTypes = ['Geometry', 'OID']
 fields = excludeFields(fc, excludeTypes)
 with arcpy.da.SearchCursor(fc, fields) as cursor:
 print cursor.fields
 for row in cursor:
 print row
del cursor
                          
-----------------------------------------------------------------

>>> fds = arcpy.ListFields('C:/gispy/data/ch17/park.shp')
>>> [f.name for f in fds]
[u'FID', u'Shape', u'COVER', u'RECNO']
>>> [f.type for f in fds]
[u'OID', u'Geometry', u'String', u'Double']
                          
----------------------------------------------------------------------                           

>>> cursor = arcpy.da.SearchCursor (parkData, [ 'SHAPE@'])
>>> row = cursor.next()
>>> row[0].type
'polygon'
>>> row[0].area
600937.0921638225
>>> row[0].centroid
<Point (2131483.24062, 191220.538898, #, #)>
>>> row[0].firstPoint
<Point (2131312.35816, 190450.120062, #, #)>
>>> row[0].area
600937.0921638225
        
-----------------------------------------------------------------

import arcpy
fc = 'C:/gispy/data/ch17/fires.shp'
fields = ['FireName']
cursor = arcpy.da.SearchCursor(fc, fields)
for row in cursor:
 print row[0]
del cursor
                          
----------------------------------------------------------------------

 # searchNprint.py
 # Purpose: Print each fire name in a file.
 import arcpy, traceback
 try:
 cursor = arcpy.da.SearchCursor (fc, ['FireName'])
 for row in cursor:
 print row[0]
 del cursor
 except:
 print 'An error occurred'
 traceback.print_exc()
 del cursor 

-----------------------------------------------------------------

 # updateValues.py
 # Purpose: Modify the fire type value and the fire
 # name in each record.
 # Usage: No script arguments needed.
 import arcpy, traceback
 fc = 'C:/gispy/data/ch17/firesCopy.shp'
 fields = ['FireType_P', 'FireName']
 cursor = arcpy.da.UpdateCursor(fc, fields)
     try:
         for row in cursor:
 # Make changes to the list of values in 'row'
 # Example: 13->15
         row[0] = row[0] + 2
 # Example: LITTLE CRK->Little Crk
         row[1] = row[1].title()
 # Update the table (otherwise changes won't be saved)
         cursor.updateRow(row)
         print 'Updated {0} and {1}'.format(row[0], row[1])
 except:
         print 'An error occurred'
         traceback.print_exc()
del cursor 
                          
----------------------------------------------------------------------

# deleteRows.py
 # Purpose: Delete the first x rows.
 # Usage: No script arguments required.
 import arcpy, traceback
 fc = 'C:/gispy/data/ch17/firesCopy.shp'
 field = 'FID'
 x = 7
 try:
     cursor = arcpy.da.UpdateCursor(fc, [field])
 # Delete the first x rows
     for row in cursor:
         if row[0] < x:
 # Delete this row
         cursor.deleteRow()
         print 'Deleted row {0}'.format(row[0])
 del cursor
 except:
         print 'An error occurred.'
         traceback.print_exc()
         del cursor
        
-----------------------------------------------------------------

# insertRow.py
 # Purpose: Insert a new row without geometry.
 # Usage: No script arguments needed.
 import arcpy, traceback
 # Create an insert cursor
 fc = 'C:/gispy/data/ch17/firesCopy.shp'
 fields = ['FireId','CalendarYe']
 try:
 cursor = arcpy.da.InsertCursor(fc, fields)
 # Create a list with FireId=513180 & CalendarYr=2009
 newRecord =[513180, 2009]
 # Insert the row (otherwise no change would occur)
 cursor.insertRow(newRecord )
 print 'Record inserted.'
 del cursor
 except:
 print 'An error occurred.'
 traceback.print_exc()
 del cursor
                          
----------------------------------------------------------------------

# insertRows.py
# Purpose: Insert multiple rows without geometry.
# Usage: No script arguments needed.
import arcpy, traceback
fc = 'C:/gispy/data/ch17/firesCopy.shp'
# Find the current fire numbers.
try:
 fields = ['FireNumber']
 cursor = arcpy.da.SearchCursor(fc, fields)
 fireNumbers = [row[0] for row in cursor]
 print '{0} fire numbers found.'.format(len(fireNumbers))
 del cursor
except:
 print 'An error occurred in the search.'
 traceback.print_exc()
 del cursor 

-----------------------------------------------------------------

# Insert 5 new fires for year 2015.
try:
 fields.append('CalendarYe')
 cursor = arcpy.da.InsertCursor(fc, fields)
 # Find the max value in list and increment by 1
 fireNum = max(fireNumbers) + 1
 for i in range(5):
 # Create a row with unique fire number & year=2015
 newRow = [fireNum, 2015]
 fireNum = fireNum + 1
 # Insert the row.
 cursor.insertRow(newRow)
 print '''New row created with \
 fire {0} and year = {1}.'''.format(
 newRow[0], newRow[1])
 del cursor
except:
 print 'An error occurred in the insertion.'
 traceback.print_exc()
 del cursor
                          
----------------------------------------------------------------------

>>> myPoint = arcpy.Point(-70.1, 42.07)
>>> myPoint
<Point (-70.1, 42.07, #, #)>
        
-----------------------------------------------------------------

>>> x = 2134000
>>> y = 179643
>>> a = arcpy.Point(x,y)
>>> x = 2147000
>>> y = 163267
>>> b = arcpy.Point(x,y)
>>> myArray = arcpy.Array([a,b])
>>> # Create a line with an Array object that has points.
>>> line = arcpy.Polyline(myArray)
>>> line.length
poly = arcpy.Polygon(myArray)) 
----------------------------------------------------------------------

# insertPoint.py
 # Purpose: Insert a point with a Geometry object.
 # Usage: No script arguments needed.
 import arcpy, traceback
 fc = 'C:/gispy/data/ch17/firesCopy.shp'
 try:
 ic = arcpy.da.InsertCursor(fc, ['FireId', 'SHAPE@XY'])
# Create a point with x = -70.1 and y = 42.07
 # to be used for the Shape field.
 myPoint = arcpy.Point(-70.1, 42.07)
 # Create a row list with FireId=500000 and the new point.
 newRow =[500000, myPoint]
 # Insert the new row.
 ic.insertRow(newRow)
 print 'New row inserted.'
 del ic
 except:
 print 'An error occurred.'
 traceback.print_exc()
 del cursor
        
-----------------------------------------------------------------

# insertPolygon.py
# Insert cursor polygon example.
import arcpy, traceback
# Create 3 point objects for the triangle
a = arcpy.Point(2134000, 179643)
b = arcpy.Point(2147000, 163267)
c = arcpy.Point(2131327, 167339)
# Create an array, needed for creating a polygon
myArray = arcpy.Array([a,b,c])
# Create a polygon.
poly = arcpy.Polygon(myArray)
fc = 'C:/gispy/data/ch17/aggCopy.shp' 
try:
 # Create an insert cursor
 cursor = arcpy.da.InsertCursor(fc, ['SHAPE@', 'Id'])
 # Create row list
 newRow = [poly, 333]
 # Insert the new row.
 # It's automatically given an FID one greater
 # than the largest existing one.
 cursor.insertRow(newRow)
 print 'Polygon inserted.'
 del cursor
except:
 print 'An error occurred.'
 traceback.print_exc()
 del cursor                          
---------------------------------------------------------------------- 

>>> query1 = "SizeClass = 'A'" # Fires of size class A.
>>> query2 = "FireName <> 'MEADOW'" # Fires not named MEADOW.
>>> query3 = 'FID > 6' # Fires with ID greater than 6 .
>>> query4 = "StartTime = date '2000-01-06'" # After Jan.6,2000
        
-----------------------------------------------------------------

# sqlQueryCursor.py
 # Purpose: Use a SQL query to select specific records.
 # Usage: No script arguments needed.
 import arcpy, traceback
 fc = 'C:/gispy/data/ch17/fires.shp'
 # Create the where_clause
 query = "SizeClass = 'A'"
 try:
 sc = arcpy.da.SearchCursor(fc, ['CalendarYe'], query)
 for row in sc:
 print row[0],
 del sc
 except:
 print 'An error occurred.'
 traceback.print_exc()
 del cursor
                          
----------------------------------------------------------------------                           
# whereClauseWithVar.py
 # Purpose: Use a SQL query to select specific
 # records based on user arguments.
 # Example: C:/gispy/data/ch17/fires.shp FID FireName
 import arcpy, sys, traceback
 fc = sys.argv[1]
 numericField = sys.argv[2]
 fieldToPrint = sys.argv[3]
 query = '{0} > 6'.format(numericField) # string formatting
 try:
 with arcpy.da.SearchCursor(fc, [fieldToPrint],
 query) as cursor:
 recordList = [row[0] for row in cursor]
 del cursor
 print recordList
 except:
 print 'An error occurred.'
 traceback.print_exc()
 del cursor
---------------------------------------------------------------
        
dictionaryName = {key1 : value1, key2 : value2, key3 : value3}
                
---------------------------------------------------------------

# weekdays.py
weekdayDict = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday',
3: 'Thursday', 4:'Friday'}
day = weekdayDict[num]
print 'Weekday: {0}'.format(day)
        
---------------------------------------------------------------

>>> weather['S3'] = [33,40]
>>> weather
{'S3': [33, 40], 'S2': [25, 30, 40], 'S1': [15, 20]}
        
---------------------------------------------------------------

>>> update = [i + 1 for i in weather['S1']]
>>> weather['S1'] = update
        
---------------------------------------------------------------

>>> key = 'cslouis'
>>> if key in roomDict
... print roomDict[key]
... else:
... 'No {0} key found.'.format(key)
...
'No cslouis key found.'
        
---------------------------------------------------------------
>>> roomDict.keys()
>>> roomDict.values()
>>> roomDict.items()
---------------------------------------------------------------
        
>>> for k in newVocab.keys():
... print k
>>> for v in newVocab.values():
... print v
>>> for k, v in newVocab.items():
... print k, ':', v
        
---------------------------------------------------------------
>>> for k in weather.keys():
... weather[k].append(0)
---------------------------------------------------------------
>>> for v in weather.values():
... print sum(v)/len(v)
---------------------------------------------------------------

>>> for k, v in roomDict.items():
... room = str(v)
... if room.startswith('4'):
... print '{0}, room {1}'.format(k,v)
        
---------------------------------------------------------------

# healthyLiving.py
# Purpose: Collect user preferences; only keep most recent responses.
topics = ['fruit','fruit','fruit',
 'veg','veg','veg','exercise','park']
favDict = {} # Create empty dictionary
for topic in topics:
 question = 'What is your favorite {0}?'.format(topic)
 answer = raw_input(question)
 favDict[topic] = answer # Add or update item
print favDict

#If condition

for topic in topics:
 question = 'What is your favorite {0}?'.format(topic)
 answer = raw_input(question)
 if key not in roomDict :
 favDict[topic] = answer # Add item (only 1st responses recorded) 
---------------------------------------------------------------

 # healthyLivingV2.py
 # Purpose: Collect user preferences; keep all responses.
 topicList = ['fruit','fruit','fruit',
 'veg','veg','veg','exercise','park']
 topDict = {} # Create empty dictionary
 for topic in choiceList:
 question = "What is your favorite {0}?".format(topic)
 answer = raw_input(question)
 if topic not in topDict:
 # Add a new item to the dictionary.
 topDict[topic] = [answer]
 else:
 # Update an item by adding to an item's list.
 topDict[topic].append(answer)
print 'topDict {0}'.format(topDict)
        
---------------------------------------------------------------

# healthyLivingV2.py
 # Purpose: Collect user preferences; keep all responses.
 topicList = ['fruit','fruit','fruit',
 'veg','veg','veg','exercise','park']
 topDict = {} # Create empty dictionary
 for topic in choiceList:
 question = "What is your favorite {0}?".format(topic)
 answer = raw_input(question)
 if topic not in topDict:
 # Add a new item to the dictionary.
 topDict[topic] = [answer]
 else:
 # Update an item by adding to an item's list.
 topDict[topic].append(answer)
print 'topDict {0}'.format(topDict)
        
---------------------------------------------------------------

# fileDates.py
 # Purpose: Collect filenames and modification dates in a dictionary.
 import os, time
 inputDir = 'C:/gispy/data/ch18/smallDir'
 fileList = os.listdir(inputDir)
 fileDict = {}
 for f in fileList:
 epochNum = os.path.getmtime(inputDir + '/' + f)
 modTime = time.ctime(epochNum)
 fileDict[f] = modTime
print fileDict
        
---------------------------------------------------------------
# areaMedian.py
import arcpy, numpy
fc = 'C:/gispy/data/ch18/parkAreas.shp'
idField = 'FID'
areaField = 'F_AREA'
areasDict = {}
 # Populate dictionary with id:area items.
sc = arcpy.da.SearchCursor(fc, [idField, areaField])
for row in sc:
        fid = row[0]
        area = row[1]
        areasDict[fid] = area
del sc
 
 # Find the median area.
areas = areasDict.values()
medianArea = numpy.median(areas)
print 'Median area: {0}'.format(medianArea)
 # Find the polygons with values close to median.
sqft = 400
print 'Polygons close to median:'
for k, v in areasDict.items():
        if medianArea - sqft < v < medianArea + sqft:
        print '{0}: {1}, {2}: {3}'.format(idField, k, areaField, v) 

---------------------------------------------------------------
import arcpy, numpy
arcpy.env.workspace = r'D:\DataforArcObject'
fc = 'Building'
d = {}
sc = arcpy.da.SearchCursor(fc, ['AgeBuilding', 'PolyArea'])
for row in sc:
    cover = row[0]
    area = row[1]
    if d.has_key(cover):
        d[cover].append(area)
    else:
        d[cover] = [area]
        
del sc
for k, v in d.items():
    median = numpy.median(v)
    print '''Polygons with cover '{0}' have \
 median area {1}'''.format(k, median)
 

for k, v in d.items():
...     median = numpy.sum(v)
...     print '''Polygons with cover '{0}' have\
Total area {1}'''.format(k, median)

---------------------------------------------------------------

>>> with open('C:/gispy/data/ch19/poem.txt', 'r') as f:
... print f.read() 
        
---------------------------------------------------------------
>>> f = open('C:/gispy/data/ch19/poem.txt', 'r')
>>> f.read()
>>> f.close()
---------------------------------------------------------------
>>> f = open('C:/gispy/data/ch19/sneeze.txt', 'w')
>>> f.write('haa')
>>> f.write('choo')
>>> f.close()
---------------------------------------------------------------
>>> f = open('C:/gispy/data/ch19/sneeze.txt', 'w')
>>> f.write('snork\nsniffle\n')
>>> f.write('haaack\n')
>>> f.write('*sigh*')
>>> f.close()
---------------------------------------------------------------
>>> f = open('C:/gispy/data/ch19/sneeze.txt', 'w')
>>> csv = ','.join(['glug', 'gulp', 'erp'])
>>> f.write(csv)
>>> f.write('\n')
>>> lines = '\n'.join(['ack', 'hmmm', 'sniff'])
>>> f.write(lines)
>>> f.close()        
---------------------------------------------------------------
# safeFileRead.py
import os, sys
infile = sys.argv[1]
try:
 f = open(infile, 'r'
 print f.read()
 f.close()
except IOError:
 print "{0} doesn't exist or can't be opened.".format(infile)
---------------------------------------------------------------

>>> import os
>>> os.path.isfile('C:/gispy/data/ch19/poem.txt')
True
>>> os.getcwd()         
---------------------------------------------------------------

# parseTable.py
 # Purpose: Parse numeric values in a tabular text file.
 cap = 5
 infile = 'C:/gispy/data/ch19/report.txt'
 try:
 with open(infile, 'r') as f:
 for line in f:
 # String to list of strings.
 lineList = line.split()
 # String items to float items.
 nums = [float(i) for i in lineList]
 # First col is ID, rest are data values.
 ID = nums[0]
 data = nums[1:]
 # Cap the data values at 5.
 for index, val in enumerate(data):
 if val > cap:
 data[index] = cap
 # Count and sum the values and report the results.
 count = len(data)
 total = sum(data)
print 'ID: {0} Sum: {1} Count {2}'.format(ID, total, count)
print 'Data: {0}'.format(data)
 except IOError:
 print "{0} doesn't exist or can't be opened.".format(infile)
        
---------------------------------------------------------------

# cfactor.py
# Purpose: Read a text file contents into a dictionary.
factorDict = {}
infile = 'C:/gispy/data/ch19/cfactors.txt'
 try:
with open(infile, 'r') as f:
f.readline()
 for line in f:
 line = line.split('=')
 factor = int(line[0])
label = line[1].rstrip()
 factorDict[factor] = label
 print factorDict
 except IOError:
 print "{0} doesn't exist.".format(infile)
---------------------------------------------------------------
>>> mylist = ['a','b','c','d']
>>> mylist.index('c')
---------------------------------------------------------------

# fieldIndex.py
 # Purpose: Find the index of a field name in a text
 # file with space separated fields in the first row.
 infile = 'C:/gispy/data/ch19/cfactors.txt'
 fieldName = 'Label'
def getIndex(delimString, delimiter, name):
 '''Get position of item in a delimited string'''
 delimString = delimString.strip()
 lineList = delimString.split(delimiter)
 index = lineList.index(name)
 return index
with open(infile, 'r') as f:
 line = f.readline()
 ind = getIndex(line, ' ', fieldName)
 print '{0} has index {1}'.format(fieldName, ind)
---------------------------------------------------------------

# cfactorModify.py
 # Purpose: Demonstrate reading and writing files.
 import os
 infile = 'C:/gispy/data/ch19/cfactors.txt'
 baseN = os.path.basename(infile)
 outfile = 'C:/gispy/scratch/' + os.path.splitext(baseN)[0] + 'v2.txt'
 try:
 #OPEN the input and output files.
 with open(infile, 'r') as fin:
 with open(outfile, 'w') as fout:
 #READ/MODIFY/WRITE the first line.
 line = fin.readline()
 line = line.replace(' ',',')
 fout.write(line)
 #FOR the remaining lines.
 for line in fin:
          #MODIFY the line.
 line = line.replace('=', ',')
 #WRITE to output.
 fout.write(line)
 print '{0} created.'.format(outfile)
 except IOError:
 print "{0} doesn't exist.".format(infile)
---------------------------------------------------------------

# removeHeader.py
 # Purpose: Remove header rows.
 import os
 headers = 2
 infile = 'C:/gispy/data/ch19/eyeTrack.csv'
 baseN = os.path.basename(infile)
 outfile = 'C:/gispy/scratch/' + os.path.splitext(baseN)[0] \
 + 'v2.txt'
 try:
 with open(infile, 'r') as fin:
 with open(outfile, 'w') as fout:
 #READ header lines, but don't write them.
 for i in range(headers):
 fin.readline()
 #READ and WRITE the remaining lines.
 for line in fin:
 fout.write(line)
 print '{0} created.'.format(outfile)
 except IOError:
 print "{0} doesn't exist.".format(infile)
          
---------------------------------------------------------------

# Excerpt from sample script 'removeRecords.py'
 # REMOVE selected lines (only write acceptable lines)
 # READ and WRITE field names
 fieldNameLine = fin.readline()
 fout.write(fieldNameLine)
 # FIND field indices
 sep = ','
 findex1 = getIndex(fieldNameLine, sep, 'FPOGX')
 findex2 = getIndex(fieldNameLine, sep, 'FPOGY')
 # FOR the remaining lines:
 for line in fin:
 lineList = line.split(sep)
 v1 = float(lineList[findex1])
 v2 = float(lineList[findex2])
 # IF condition is TRUE, write this record.
 if v1 > 0 and v2 > 0:
 fout.write(line)
          
---------------------------------------------------------------

>>> fields = ['FireId', 'Org', 'State', 'FireType', 'Protection']
>>> index = 2
>>> fields.pop(index)
'State'
>>> fields
['FireId', 'Org', 'FireType', 'Protection']
          
---------------------------------------------------------------

# Excerpt from sample script 'removeColumns.py'
 # REMOVE named columns (only write valid columns)
 removeFields = ['LPCX','LPCY', 'RPCX', 'RPCY',
 'LGX', 'LGY', 'RGX', 'RGY']
def removeItems(indexList, delimiter, delimString):
 '''Remove items at given indices in a delimited string'''
 lineList = delimString.split(delimiter)
 indexList.sort(reverse = True)
 for i in indexList:
 lineList.pop(i)
 lineString = delimiter.join(lineList)
 return lineString
 ###code to OPEN files and READ past header omitted###
 # READ field names.
 fieldNamesLine = fin.readline()
 # DETERMINE field indices.
 rfIndex = []
 for field in removeFields:
 index = getIndex(fieldNamesLine, sep, field)
 rfIndex.append(index)
 # REMOVE items with these indices and WRITE the line.
 line = removeItems(rfIndex, sep, fieldNamesLine)
 fout.write(line)
 # READ/MODIFY/WRITE the remaining lines.
 for line in fin:
 line = removeItems(rfIndex, sep, line)
 fout.write(line)

---------------------------------------------------------------
>>> import pickle
>>> f = open('C:/gispy/data/ch19/gherkin.txt', 'w')
>>> pickle.dump(2.71828,f)
>>> pickle.dump(['FireId', 'Org', 'FireType'],f)
>>> f.close()
---------------------------------------------------------------
>>> f2 = open('C:/gispy/data/ch19/gherkin.txt', 'r')
>>> thing1 = pickle.load(f2)
>>> thing1
2.71828 
---------------------------------------------------------------
>>> thing2 = pickle.load(f2)
>>> thing2
['FireId', 'Org', 'FireType']
>>> type(thing2)
<type 'list'>
>>> f2.close()
---------------------------------------------------------------

# writeSimpleHTML.py
 mystr = '''<!DOCTYPE html>
 <html>
 <body>
 <h1>Asian Elephant</h1>
 <img src="../data/ch20/pics/lakshmi.jpg" alt="elephant">
 </body>
 </html>
 '''
 htmlFile = 'C:/gispy/scratch/output.html'
 outf = open(htmlFile, 'w')
 outf.write(mystr)
 outf.close()
print '{0} created.'.format(htmlfile)
          
---------------------------------------------------------------

# writeSimpleHTML2.py
 # Purpose: Write HTML page in 3 parts.
 # Usage: workspace title image_path
 # Example input:
# C:/gispy/scratch "Asian Elephant" ../data/ch20/pics/lakshmi.jpg
import os, sys
 workspace = sys.argv[1]
 title = sys.argv[2]
 image = sys.argv[3]
 beginning = '''<!DOCTYPE html>
 <html>
 <body>'''
 middle = '''
 <h1>{0}</h1>
 <img src='{1}' >\n'''.format(title, image)
 end = ''' </body>
 </html>
 '''
 htmlfile = workspace + '/output2.html'
 with open(htmlfile,'w') as outf:
 outf.write(beginning)
 outf.write(middle)
 outf.write(end)
print '{0} created.'.format(htmlfile)
          
---------------------------------------------------------------

 # excerpt from printHTMLList.py
 def python2htmlList(myList, listType):
 '''Convert a Python list to HTML list.
 For example, convert [rast1,rast2] to:
 <ul>
 <li>rast1</li>
 <li>rast2</li>
 </ul>
 '''
 # Wrap items in item tags.
 htmlItems = ['<li>' + str(item) + '</li>' for item in myList]
 # Join the item list into a string with a line break
 # after each item .
 itemsString = '''\n '''.join(htmlItems)
# Wrap the string of items in the list tag.
 htmlList = '''
 <{0}>
 {1}
 </{0}>
 '''.format(listType, itemsString)
 return htmlList 
---------------------------------------------------------------

>>> rasts = [u'elev', u'landcov', u'soilsid', u'getty_cover']
>>> htmlList = python2htmlList(rasts, 'ul')
>>> print htmlList
          
---------------------------------------------------------------

# getLinks.py
 # Purpose: Read and print the links in an html file.
 import sys
 basedir = 'C:/gispy/'
 mPath = 'data/ch20/htmlExamplePages/elephant2.html'
 sys.path.append(basedir + 'sample_scripts/ch20')
 import BeautifulSoup
 # Read the HTML file contents.
 with open(basedir + mPath, 'r') as infile:
 # Create a soup object and find all the hyperlinks.
 soup = BeautifulSoup.BeautifulSoup(infile)
 linkTags = soup.findAll('a')
 # Print each hyperlink reference.
 for linkTag in linkTags:
 print 'Link: {0}'.format(linkTag['href'])
          
---------------------------------------------------------------

import urllib2
url = 'http://www.google.com'
response = urllib2.urlopen(url)
contents = response.read()
response.close()
print len(contents)
          
---------------------------------------------------------------

# fetchZip.py
 # Purpose: Fetch a zip file and place it in an output directory.
 import os, urllib2
 def fetchZip(url, outputDir):
 '''Fetch binary web content located at 'url'
 and write it in the output directory'''
 response = urllib2.urlopen(url)
 binContents = response.read()
 response.close()
 # Save zip file to output dir (write it in 'wb' mode).
 outFileName = outputDir + os.path.basename(url)
 with open(outFileName,'wb') as outf:
 outf.write(binContents)
 outputDir = 'C:/gispy/scratch/'
 theURL = 'file:///C:/gispy/data/ch20/getty.zip'
 fetchZip( theURL, outputDir )
 print'{0}{1} created.'.format(outputDir, os.path.basename(theURL))
          
---------------------------------------------------------------

# extractFiles.py
# Purpose: Extract files from an archive;
# Place the files into an output directory.
# Usage: No script arguments
import os, zipfile
def unzipArchive(archiveName, dest):
 '''Extract files from an archive
 and save them in the destination directory'''
 print 'Unzip {0} to {1}'.format( archiveName, dest )
 # Get a Zipfile object.
 with zipfile.ZipFile(archiveName, 'r') as zipObj:
 zipObj.extractall(dest)
 # Report the list of files extracted from the archive.
 archiveList = zipObj.namelist()
 for fileName in archiveList:
 print ' Extract file: {0} ...'.format(fileName)
 print 'Extraction complete.'
archive = 'park.zip'
baseDir = 'C:/gispy/'
archiveFullName = baseDir + 'data/ch20/' + archive
destination = baseDir + 'scratch/' + \
 os.path.splitext(archive)[0] + '/'
if not os.path.exists(destination):
 os.makedirs(destination)
unzipArchive(archiveFullName, destination)
          
---------------------------------------------------------------

 # parseKMLrestaurants.py
 # Purpose: Print KML placemark names and descriptions.
 import sys
 baseDir = 'C:/gispy/'
 sys.path.append(baseDir +'sample_scripts/ch20')
 import BeautifulSoup
 fileName = baseDir + 'data/ch20/restaurants.kml'
 # Get the KML soup.
 with open(fileName, 'r') as kmlCode:
 soup = BeautifulSoup.BeautifulSoup(kmlCode)
 # Print the names and descriptions.
 names = soup.findAll('name')
 descriptions = soup.findAll('description')
 for name, description in zip(names, descriptions):
 print name.contents[0]
 print '\t{0}'.format(description.contents)
          
---------------------------------------------------------------
# Excerpt from restaurantKML2shp.py...
 coordinates = soup.findAll('coordinates')
 names = soup.findAll('name')
 descriptions = soup.findAll('description')
 # Populate the shapefile.
 with arcpy.da.InsertCursor( fc, [ 'SHAPE@XY' ] + fieldNames ) as ic:
 for c,n,d in zip(coordinates, names, descriptions):
 # Get field values.
 [x, y, z] = c.contents[0].split(',')
 myPoint = arcpy.Point(x, y)
 name = n.contents[0]
 blurb = d.contents[0]
 scoreString = d.contents[2]
 scoreList = scoreString.split(':')
 score = float(scoreList[1])
 # Put row values in a list & insert the new row.
 newRow = [myPoint, name, blurb, score]
 ic.insertRow(newRow))
        
---------------------------------------------------------------

def calculateCost(trail_ID, vegetation, length):
...     rate = 1000
...     if vegetation[trail_ID] == 'barren':
...          rate = 800
...     elif vegetation[trail_ID] == 'some bare ground':
...          rate = 900
...     cost = length[trail_ID]*rate
...     return cost


---------------------------------------------------------------

# excerpt from trailExample.py
class Trail:
'''Pedestrian path.
Properties:
 ID A unique identifier
 length: Length in kilometers
 vegetation: Plant growth on the trail
'''
def __init__(self, tid, theLength, theVegetation):
 '''Initialize trail properties.'''
 self.ID = tid
 self.length = theLength
 self.vegetation = theVegetation
def calculateCost(self):
 '''Calculate maintenance costs based
 on vegetation and length.'''
rate = 1000
 if self.vegetation == 'barren':
 rate = 800
 elif self.vegetation == 'some bare ground':
 rate = 900
 cost = self.length*rate
 return cost
def reportInfo(self):
 '''Print trail properties'''
 print 'ID: {0}'.format(self.ID)
 print 'Length: {0}'.format(self.length)
 print 'Vegetation: {0}'.format(self.vegetation)
        
---------------------------------------------------------------

# excerpt from trailExample.py
 data = 'C:/gispy/data/ch21/trails.txt'
 trailDict = {}
 with open(data, 'r') as f:
 # Read each line.
 for line in f:
 # Strip '\n' from the end and split the line.
 line = line.strip()
 lineList = line.split(',')
 tID = int(lineList[0])
 tLength = float(lineList[1])
 tVeg = lineList[2]
# Create a Trail object.
 theTrail = Trail(tID, tLength, tVeg)
 # Add the Trail object to the dictionary.
 trailDict[traID] = theTrail
        
---------------------------------------------------------------

# functionalTrailDelete.py
trailList = [ 1, 2, 5, 10, 15]
trailVegetation = {1: 'barren', 2: 'some bare ground',
5: 'stunted vegetation', 10: 'barren', 15: 'over-grown'}
trailLength = {1: 2.3, 2: 5.0, 15: 4.2, 10: 1.6, 5: 20.0}
# Determine which trails to delete.
longT = []
for k, v in trailLength.items():
 if v > 10:
 longT.append(k)
# Delete the long trails and each corresponding properties.
for i in longT:
 trailList.remove(i)
 del trailLength[i]
 del trailVegetation[i]
        
---------------------------------------------------------------

# highwayInfo.py
 # Purpose: Define a highway class.
 class Highway:
 '''
 Major road class.
 Properties:
 name None-numerical road name.
 length Length based on a network dataset.
 travelTime Estimated time it takes to travel the
 full length of this highway.
 '''
 def __init__(self, name, length, tTime):
 '''Initialize a Highway object.'''
 self.name = name
 self.length = length
 self.travelTime = tTime
 def calculateAvgSpeed(self):
 '''Calculate the average speed.'''
 avgSpeed = self.length/float(self.travelTime)
 return avgSpeed
 def getOrientation( self, number ):
'''Determine highway orientation based on the hwy number.'''
 if number%2 == 1: # if the number is odd...
 orientation = 'NS'
 else: # else the number is even.
 orientation = 'EW'
 return orientation
 def report(self):
 '''Print highway properties.'''
 print
 print '''{0} Highway'''

---------------------------------------------------------------

# handleHighways.py
 # Purpose: Demonstrate using a class defined in a separate
 # user-defined module.
 # Usage: No arguments needed, but highwayInfo.py must be in
 # the same directory.
 import highwayInfo
 myHwy = highwayInfo.Highway('Pacific Highway', 496, 5)
 spdLimit = myHwy.calculateAvgSpeed()
 orient = myHwy.getOrientation(5)
 print 'Avg travel speed: {0} km/hr'.format(spdLimit)
 print 'Orientation: {0}'.format(orient)
 
---------------------------------------------------------------
        
# getFileName.py
# Purpose: Get a shapefile name from the user and print the shape type.
import tkFileDialog, arcpy
fc = tkFileDialog.askopenfilename(filetypes=[('shapefiles','*.shp')],
 title='Choose a SHAPEFILE that defines the STATISTICAL ZONES')
print 'fc = {0}'.format(fc)
desc = arcpy.Describe(fc)
print 'Shape type = {0}'.format(desc.shapeType)
        
---------------------------------------------------------------

fname = tkFileDialog.asksaveasfilename(initialfile='output.txt',
title='Save output as...')
arcpy.Copy_management('C:/gispy/data/ch22/precip.txt', fname)
        
---------------------------------------------------------------

# askDirectory.py
# Purpose: Get a directory from the user and set the workspace.
import tkFileDialog, arcpy
arcpy.env.workspace = tkFileDialog.askdirectory(initialdir='C:/',
title='Select the FOLDER containing Landuse RASTERS')
print 'Workspace = {0}'.format(arcpy.env.workspace)
        
---------------------------------------------------------------

>>> t = ('shapefiles','*.shp')
>>> fname1 = tkFileDialog.askopenfilename(filetypes=[t])
        
---------------------------------------------------------------

>>> fname2 = tkFileDialog.askopenfilename(
filetypes=[('csv (Comma delimited)','*.csv'),
('Text Files','*.txt')] )
        
---------------------------------------------------------------
>>> fname3 = tkFileDialog.askopenfilename(initialdir = 'C:/gispy')
---------------------------------------------------------------
>>> fname4 = tkFileDialog.askopenfilename(initialfile = 'bogus.shp')
---------------------------------------------------------------

# excerpt from fileDialogOptions.py
# Purpose: Vary file dialog options to get file and directory
# names from user and print the results.
fnames = tkFileDialog.askopenfilename(
 title='Test multiple selections allowed', multiple=True)
files = fnames.split()
print 'Name list:'
for fname in files: # for each file selected by the user
 print ' {0}'.format(fname)
        
---------------------------------------------------------------

import tkFileDialog, Tkinter
tkObj = Tkinter.Tk()
inputDir = tkFileDialog.askdirectory(parent=tkObj)
tkObj.destroy()
        
---------------------------------------------------------------
 # askAndDestroy.py
 # Purpose: Get a directory from the user
 # and suppress the default Tk window.
 import tkFileDialog, Tkinter
 # Get a tk object
 fatherWilliam = Tkinter.Tk()
 # Hide the tk window
 fatherWilliam.withdraw()
 inputDir = tkFileDialog.askopenfilename(parent=fatherWilliam)
 # Destroy the tk window
fatherWilliam.destroy() 
---------------------------------------------------------------

fobject = tkFileDialog.askopenfile(
 filetypes=[('shapefiles','*.shp')],
 initialfile='data.txt', title='Open a data file...')
firstLine = fobject.readline()
fobject.close()
        
---------------------------------------------------------------

myTitle = 'Select an output file name'
with tkFileDialog.asksaveasfile(title=myTitle) as ofile:
 ofile.write('I like tkFileDialog')

        
---------------------------------------------------------------        

# textLister.py
# Purpose: Print the text file (.txt) names in the directory.
import arcpy, os
myDir = r'C:\gispy\data\ch23\smallDir'
fileList = os.listdir(myDir)
for f in fileList:
 if f.endswith(".txt"):
 print f
arcpy.AddMessage('And I like pie!')

---------------------------------------------------------------
arcpy.AddMessage('And I like pie!')        
---------------------------------------------------------------
>>> import arcpy
>>> message = 'And I like pie!'
>>> print message
And I like pie!
>>> arcpy.AddMessage(message)
---------------------------------------------------------------
def printArc(message):
 '''Print message for Script Tool and standard output.'''
 print message
 arcpy.AddMessage(message)
---------------------------------------------------------------
import arcpy, os
def printArc(message):
 '''Print message for Script Tool and standard output.'''
 print message
 arcpy.AddMessage(message)
myDir = r'C:\gispy\data\ch23\smallDir'
# Lists all the files in the given directory .
fileList = os.listdir(myDir)
myMessage = 'Directory {0} contains {1} files.'.format(myDir,
 len(fileList))
---------------------------------------------------------------

# Usage: workspace datatype (raster, feature class,
# or other) wildcard
# Sample input: C:/gispy/data/ch23/rastTester.gdb raster _out
import arcpy, os, sys
def printArc(message):
 '''Print message for Script Tool and standard output.'''
 print message
 arcpy.AddMessage(message)
arcpy.env.workspace = sys.argv[1]
fType = sys.argv[2]
wildcard = sys.argv[3]
substring = '*{0}*'.format(wildcard)
if fType == 'raster':
 data = arcpy.ListRasters(substring)
elif fType == 'feature class':
 data = arcpy.ListFeatureClasses(substring)
else:
 entireDir = os.listdir(arcpy.env.workspace)
 data = []
 for d in entireDir:
 if d.endswith(wildcard):
 data.append(d)
for d in data:
 try:
 arcpy.Delete_management(d)
printArc( '{0}/{1} deleted.'.format(arcpy.env.workspace, d))
 except arcpy.ExecuteError:
 printArc( arcpy.GetMessages())
        
---------------------------------------------------------------
        
# buffer1.py
 # Purpose: Buffer a hard-coded file and send the result
 # to a Script Tool.
 import arcpy
 arcpy.env.overwriteOutput = True
 fileToBuffer = 'C:/gispy/data/ch23/smallDir/randpts.shp'
 distance = '500 meters'
 outputFile = 'C:/gispy/scratch/randptsBuffer.shp'
 arcpy.Buffer_analysis(fileToBuffer, outputFile, distance)
 arcpy.SetParameterAsText(0, outputFile)
        
---------------------------------------------------------------

# buffer2.py
 # Purpose: Buffer an input file by an input distance
 # and send the result to a Script Tool.
 import arcpy, os, sys
 arcpy.env.overwriteOutput = True
 fileToBuffer = sys.argv[1]
 distance = sys.argv[2]
 arcpy.env.workspace = os.path.dirname(fileToBuffer)
 outputFile ='C:/gispy/scratch/Buff'
 arcpy.Buffer_analysis(fileToBuffer, outputFile, distance)
 arcpy.SetParameterAsText(2, outputFile)
        
---------------------------------------------------------------

# multiIn.py
 # Purpose: Parse a semicolon delimited input string.
 # Usage: semicolon_delimited_string
 import reportSTargs, sys
 inputString = sys.argv[1]
 reportSTargs.printArc('Input string: {0}'.format(inputString))
 inputList = inputString.split(';')
 for i in inputList:
 reportSTargs.printArc ('Input file: {0}'.format(i))
        
---------------------------------------------------------------
# bufferAll.py
 # Purpose: Buffer all the feature classes in an input folder by
 # the input distance and send the output file names to
 # the Script Tool.
 # Usage: working_directory linear_unit
 # Sample input: C:/gispy/data/ch23/smallDir "0.2 miles"
 import arcpy, reportSTargs, sys
 arcpy.env.overwriteOutput = True
 arcpy.env.workspace = sys.argv[1]
 distance = sys.argv[2]
 fcs = arcpy.ListFeatureClasses()
 outList =[]
 for fc in fcs:
 reportSTargs.printArc('Processing: {0}'.format(fc))
 outputFile = fc[:-4] + 'Out.shp'
 try:
 arcpy.Buffer_analysis(fc, outputFile, distance)
 reportSTargs.printArc('Created {0}'.format(outputFile))
 outList.append(outputFile)
 except arcpy.ExecuteError:
 reportSTargs.printArc(arcpy.GetMessages())
 results = ";".join(outList)
 reportSTargs.printArc(results)
 arcpy.SetParameterAsText(2, results)        
---------------------------------------------------------------

# getFeatures.py
 # Purpose: Copy the digitized feature set input into a shapefile
 # and send this to the Script Tool as output.
 import arcpy, sys
 arcpy.env.overwriteOutput = True
 fs = sys.argv[1]
 outputFeat = 'C:/gispy/scratch/getFeaturesOutput.shp'
 arcpy.CopyFeatures_management(fs, outputFeat)
 arcpy.SetParameterAsText(1, outputFeat)
        
---------------------------------------------------------------
 # regional.py
# Purpose: Print the names of states in the input region.
 import arcpy,reportSTargs, sys
 region = sys.argv[1]
 inf = 'C:/gispy/data/ch23/USA/USA_States_Generalized.shp'
 fields = ['SUB_REGION', 'STATE_NAME']
 sc = arcpy.da.SearchCursor(inf, fields)
 reportSTargs.printArc('\n--States in {0}--'.format(region))
 for row in sc:
 if row[0] == region:
 reportSTargs.printArc(row[1])
 reportSTargs.printArc('\n')
del sc
---------------------------------------------------------------

 # combineFields.py
 # Purpose: Create a new field that is the sum of two existing fields.
 import arcpy, sys
 dataset = sys.argv[1]
 field1 = sys.argv[2]
 field2 = sys.argv[3]
 newfield = sys.argv[4]
 arcpy.AddField_management(dataset, newfield)
 expression = '!{0}!+!{1}!'.format(field1, field2)
 arcpy.CalculateField_management(dataset, newfield,
 expression, 'PYTHON')
 arcpy.SetParameterAsText(4,dataset)
        
---------------------------------------------------------------
# feature2point.py
 # Purpose: Find the centroids of the input polygons.
 import arcpy, sys
 arcpy.env.overwriteOutput = True
 inputFile = sys.argv[1]
 outputFile = 'C:/gispy/scratch/Points.shp'
 # Find points based on the input.
 arcpy.FeatureToPoint_management(inputFile, outputFile)
 # Return the results to the tool.
 arcpy.SetParameterAsText(1, outputFile)        
---------------------------------------------------------------

# Excerpt from defaultProgressor.py
 ws = arcpy.env.workspace
 message = """Delete '{0}' files from {1}""".format(wildcard,ws)
 arcpy.SetProgressor('default', message)
 time.sleep(3)
 printArc(message)
 for d in data:
 try:
 arcpy.SetProgressorLabel('Deleting {0}'.format(d))
 arcpy.Delete_management(d)
printArc('{0}/{1} deleted'.format(ws, d))
 time.sleep(3)
 except arcpy.ExecuteError:
 printArc(arcpy.GetMessages())
        
---------------------------------------------------------------

 # Excerpt from stepProgressor.py
 # Initialize the progressor.
 message = """Preparing to delete '{0}' files \
 from {1}""".format(wildcard, arcpy.env.workspace)
 arcpy.SetProgressor('step', message, 0, len(data))
 time.sleep(3)
 printArc(message)
 for d in data:
 try:
 # Update progress label
 arcpy.SetProgressorLabel('Deleting {0}'.format(d))
 arcpy.Delete_management(d)
printArc('{0}/{1} deleted'.format(arcpy.env.workspace, d))
 time.sleep(3)
 except arcpy.ExecuteError:
 printArc(arcpy.GetMessages())
 # Update progress bar percent.
 arcpy.SetProgressorPosition()
        
---------------------------------------------------------------

 # Setting an error message
 def updateMessages(self):
 """Modify the messages created by internal validation for
 each tool parameter. This method is called after
 internal validation."""
 if self.params[0].altered:
 if self.params[0].value <= 0:
 self.params[0].setErrorMessage("Please specify \
 a positive number.")
 return

---------------------------------------------------------------

class ToolValidator(object):
 """Class for validating a tool's parameter values and
controlling the behavior of the tool's dialog."""
 def __init__(self):
 """Setup arcpy and the list of tool parameters."""
 self.params = arcpy.GetParameterInfo()
 def initializeParameters(self):
 """Refine the properties of a tool's parameters. This method is
 called when the tool is opened."""
 return
 def updateParameters(self):
"""Modify the values and properties of parameters before
internal validation is performed. This method is called
whenever a parameter has been changed."""
 return
 def updateMessages(self):
"""Modify the messages created by internal validation
for each tool parameter. This method is called after
internal validation."""
 return
        
---------------------------------------------------------------
def __init__ (self):
 self.params = arcpy.GetParameterInfo()
---------------------------------------------------------------
def initializeParameters(self):
 """Assign parameter categories."""
 numParams = len(self.params)
 for index in range(numParams):
 if index < numParams/3.0:
 self.params[index].category = 'A. Really important!'
 elif index < (2*numParams)/3.0:
 self.params[index].category = 'B. If you have time.'
 else:
 self.params[index].category = "C. Meh. Don't bother."
 return
---------------------------------------------------------------
import arcpy
 class Toolbox(object):
 def __init__(self):
 '''Define the toolbox (name of the toolbox is the
 name of the '.pyt' file).'''
 self.label = 'Toolbox'
 self.alias = ''
 # List of tool classes associated with this toolbox
 self.tools = [Tool]
 class Tool(object):
 def __init__(self):
 '''Define the tool (tool name is the name of the class).'''
 self.label = 'Tool'
 self.description = ''
 self.canRunInBackground = False
 def getParameterInfo(self):
 '''Define parameter definitions'''
 params = None
 return params
 def isLicensed(self):
 '''Set whether tool is licensed to execute.'''
 return True
 def updateParameters(self, parameters):
 '''Modify parameters before internal validation. Called
 whenever a parameter has been changed.'''
 return
 def updateMessages(self, parameters):
 '''Modify messages created by internal validation. Called
 after internal validation.'''
 return
 def execute(self, parameters, messages):
 '''The source code of the tool.'''
 return
---------------------------------------------------------------

myParam = arcpy.Parameter()
myParam.name = 'My_precious'        
---------------------------------------------------------------

def getParameterInfo(self):
 '''Set up the parameters and return
 the list of Parameter objects.'''
 # 1_Select_a_workspace_containing_rasters
 param1 = arcpy.Parameter()
 param1.name = '1_Select_a_workspace_containing_rasters'
param1.displayName = '1. Select a workspace \
containing rasters:'
 param1.parameterType = 'Required'
 param1.direction = 'Input'
 param1.datatype = 'Workspace'
 param1.filter.list = ["Local Database"]
 # 2_Select_rasters_within_the_workspace
 param2 = arcpy.Parameter()
 param2.name = '2_Select_rasters_within_the_workspace'
param2.displayName = '2. Select rasters within \
 the workspace:'
 param2.parameterType = 'Required'
 param2.direction = 'Input'
 param2.datatype = 'String'
 param2.multiValue = True
 param2.filter.list = []
 return [param1, param2]
        
---------------------------------------------------------------
 def isLicensed(self):
"""Prevent the tool from running if the Spatial Analyst extension
 is not available."""
 if arcpy.CheckExtension('Spatial') == 'Available':
 return True # tool can be executed
 else:
 return False # tool can not be executed
---------------------------------------------------------------
def updateParameters(self, parameters):
 '''Initialize raster list.'''
 if parameters[0].altered:
 arcpy.env.workspace = parameters[0].value
 rasts = arcpy.ListRasters() 
if rasts:
 parameters[1].filter.list = rasts
 else:
 parameters[1].filter.list = []
 return
def updateMessages(self, parameters):
 '''Check for rasters.'''
 if parameters[0].altered:
 if not parameters[1].filter.list:
 parameters[0].setErrorMessage('This directory does not \
contain any rasters.')
 return      
---------------------------------------------------------------
---------------------------------------------------------------

---------------------------------------------------------------

---------------------------------------------------------------

---------------------------------------------------------------
---------------------------------------------------------------

---------------------------------------------------------------

---------------------------------------------------------------        


---------------------------------------------------------------
---------------------------------------------------------------

---------------------------------------------------------------

---------------------------------------------------------------

---------------------------------------------------------------
---------------------------------------------------------------

---------------------------------------------------------------

---------------------------------------------------------------

---------------------------------------------------------------
---------------------------------------------------------------

---------------------------------------------------------------

---------------------------------------------------------------

---------------------------------------------------------------
---------------------------------------------------------------

---------------------------------------------------------------

---------------------------------------------------------------


---------------------------------------------------------------
---------------------------------------------------------------

---------------------------------------------------------------

---------------------------------------------------------------

---------------------------------------------------------------
---------------------------------------------------------------

---------------------------------------------------------------

---------------------------------------------------------------

        
---------------------------------------------------------------
---------------------------------------------------------------

---------------------------------------------------------------

---------------------------------------------------------------

---------------------------------------------------------------
---------------------------------------------------------------

---------------------------------------------------------------

---------------------------------------------------------------        



---------------------------------------------------------------
---------------------------------------------------------------

---------------------------------------------------------------

---------------------------------------------------------------

---------------------------------------------------------------
---------------------------------------------------------------

---------------------------------------------------------------

---------------------------------------------------------------

---------------------------------------------------------------
---------------------------------------------------------------

---------------------------------------------------------------

---------------------------------------------------------------

---------------------------------------------------------------
---------------------------------------------------------------

---------------------------------------------------------------

---------------------------------------------------------------


---------------------------------------------------------------
---------------------------------------------------------------

---------------------------------------------------------------

---------------------------------------------------------------

---------------------------------------------------------------
---------------------------------------------------------------

---------------------------------------------------------------

---------------------------------------------------------------

        
---------------------------------------------------------------
---------------------------------------------------------------

---------------------------------------------------------------

---------------------------------------------------------------

---------------------------------------------------------------
---------------------------------------------------------------

---------------------------------------------------------------

---------------------------------------------------------------        



---------------------------------------------------------------
---------------------------------------------------------------

---------------------------------------------------------------

---------------------------------------------------------------

---------------------------------------------------------------
---------------------------------------------------------------

---------------------------------------------------------------

---------------------------------------------------------------

---------------------------------------------------------------
---------------------------------------------------------------

---------------------------------------------------------------

---------------------------------------------------------------

---------------------------------------------------------------
---------------------------------------------------------------

---------------------------------------------------------------

---------------------------------------------------------------


---------------------------------------------------------------
---------------------------------------------------------------

---------------------------------------------------------------

---------------------------------------------------------------

---------------------------------------------------------------
---------------------------------------------------------------

---------------------------------------------------------------

---------------------------------------------------------------

        
---------------------------------------------------------------
---------------------------------------------------------------

---------------------------------------------------------------

---------------------------------------------------------------

---------------------------------------------------------------
---------------------------------------------------------------

---------------------------------------------------------------

---------------------------------------------------------------        



---------------------------------------------------------------
---------------------------------------------------------------

---------------------------------------------------------------

---------------------------------------------------------------

---------------------------------------------------------------
---------------------------------------------------------------

---------------------------------------------------------------

---------------------------------------------------------------

---------------------------------------------------------------
---------------------------------------------------------------

---------------------------------------------------------------

---------------------------------------------------------------

---------------------------------------------------------------
---------------------------------------------------------------

---------------------------------------------------------------

---------------------------------------------------------------


---------------------------------------------------------------
---------------------------------------------------------------

---------------------------------------------------------------

---------------------------------------------------------------

---------------------------------------------------------------
---------------------------------------------------------------

---------------------------------------------------------------

---------------------------------------------------------------

        
---------------------------------------------------------------
---------------------------------------------------------------

---------------------------------------------------------------

---------------------------------------------------------------

---------------------------------------------------------------
---------------------------------------------------------------

---------------------------------------------------------------

---------------------------------------------------------------        



---------------------------------------------------------------
---------------------------------------------------------------

---------------------------------------------------------------

---------------------------------------------------------------

---------------------------------------------------------------
---------------------------------------------------------------

---------------------------------------------------------------

---------------------------------------------------------------

---------------------------------------------------------------
---------------------------------------------------------------

---------------------------------------------------------------

---------------------------------------------------------------

---------------------------------------------------------------
---------------------------------------------------------------

---------------------------------------------------------------

---------------------------------------------------------------


---------------------------------------------------------------
---------------------------------------------------------------

---------------------------------------------------------------

---------------------------------------------------------------

---------------------------------------------------------------
---------------------------------------------------------------

---------------------------------------------------------------

---------------------------------------------------------------

        
---------------------------------------------------------------
---------------------------------------------------------------

---------------------------------------------------------------

---------------------------------------------------------------

---------------------------------------------------------------
---------------------------------------------------------------

---------------------------------------------------------------

---------------------------------------------------------------        



---------------------------------------------------------------
---------------------------------------------------------------

---------------------------------------------------------------

---------------------------------------------------------------

---------------------------------------------------------------
---------------------------------------------------------------

---------------------------------------------------------------

---------------------------------------------------------------

---------------------------------------------------------------
---------------------------------------------------------------

---------------------------------------------------------------

---------------------------------------------------------------

---------------------------------------------------------------
---------------------------------------------------------------

---------------------------------------------------------------

---------------------------------------------------------------


---------------------------------------------------------------
---------------------------------------------------------------

---------------------------------------------------------------

---------------------------------------------------------------

---------------------------------------------------------------
---------------------------------------------------------------

---------------------------------------------------------------

---------------------------------------------------------------

        
---------------------------------------------------------------
---------------------------------------------------------------

---------------------------------------------------------------

---------------------------------------------------------------

---------------------------------------------------------------
---------------------------------------------------------------

---------------------------------------------------------------

---------------------------------------------------------------        


---------------------------------------------------------------
---------------------------------------------------------------

---------------------------------------------------------------

---------------------------------------------------------------

---------------------------------------------------------------
---------------------------------------------------------------

---------------------------------------------------------------

---------------------------------------------------------------

---------------------------------------------------------------
---------------------------------------------------------------

---------------------------------------------------------------

---------------------------------------------------------------

---------------------------------------------------------------
---------------------------------------------------------------

---------------------------------------------------------------

---------------------------------------------------------------


---------------------------------------------------------------
---------------------------------------------------------------

---------------------------------------------------------------

---------------------------------------------------------------

---------------------------------------------------------------
---------------------------------------------------------------

---------------------------------------------------------------

---------------------------------------------------------------

        
---------------------------------------------------------------
---------------------------------------------------------------

---------------------------------------------------------------

---------------------------------------------------------------

---------------------------------------------------------------
---------------------------------------------------------------

---------------------------------------------------------------

---------------------------------------------------------------        

        

import arcpy, os, sys
from arcpy import mapping
from arcpy import mapping, da
from arcpy import *
--------------------------------------------------------------------------------------
>>> sys.path.append("C:\\Projects\\Requests")
>>> sys.path
--------------------------------------------------------------------------------------
sqlStatement = "NAME = '71 IB' AND BUS_SIGNAG = 'Ferry Plaza'"
arcpy.Select_analysis(Bus_Stops, Inbound71, sqlStatement)
--------------------------------------------------------------------------------------
filePath1 = r"C:\Projects\Inbound71_400ft_buffer"
filePath2 = r"C:\Projects\CensusBlocks2010"
arcpy.Intersect_analysis(filePath1 + " #;" + filePath2 + " #",
Intersect71Census, "ALL", "", "INPUT")
--------------------------------------------------------------------------------------
>>> filePath1 = r"C:\Projects\Inbound71_400ft_buffer"
>>> filePath2 = r"C:\Projects\CensusBlocks2010"
>>> inputString = filePath1 + " #;" + filePath2 + " #"
>>> print inputString

--------------------------------------------------------------------------------------
>>> origString = "This string has as a placeholder %s"
>>> newString = origString % "and this text was added"
>>> print newString
--------------------------------------------------------------------------------------
with arcpy.da.SearchCursor(Intersect71Census, ["STOPID","POP10"]) as
cursor:
for row in cursor:
busStopID = row[0]
pop10 = row[1]
if busStopID not in dataDictionary.keys():
dataDictionary[busStopID] = [pop10]
else:
dataDictionary[busStopID].append(pop10)

--------------------------------------------------------------------------------------
with open(r'C:\Projects\Output\Averages.csv', 'wb') as csvfile:
csvwriter = csv.writer(csvfile, delimiter=',')
for busStopID in dataDictionary.keys():
popList = dataDictionary[busStopID]
averagePop = sum(popList)/len(popList)
data = [busStopID, averagePop]
csvwriter.writerow(data)
--------------------------------------------------------------------------------------
# Import arcpy module
import arcpy
import csv
# Local variables:
Bus_Stops = r"C:\Projects\PacktDB.gdb\SanFrancisco\Bus_Stops"
CensusBlocks2010 = r"C:\Projects\PacktDB.gdb\SanFrancisco\CensusBlocks2010"
Inbound71 = r"C:\Projects\PacktDB.gdb\Chapter3Results\Inbound71"
Inbound71_400ft_buffer =
r"C:\Projects\PacktDB.gdb\Chapter3Results\Inbound71_400ft_buffer"
Intersect71Census =
r"C:\Projects\PacktDB.gdb\Chapter3Results\Intersect71Census"
# Process: Select
arcpy.Select_analysis(Bus_Stops,
Inbound71,
"NAME = '71 IB' AND BUS_SIGNAG = 'Ferry Plaza'")
# Process: Buffer
arcpy.Buffer_analysis(Inbound71,
Inbound71_400ft_buffer,
"400 Feet", "FULL", "ROUND", "NONE", "")
# Process: Intersect
arcpy.Intersect_analysis("{0} #;{1}
#".format(Inbound71_400ft_buffer,CensusBlocks2010),
Intersect71Census, "ALL", "", "INPUT")
dataDictionary = {}
with arcpy.da.SearchCursor(Intersect71Census, ["STOPID","POP10"]) as
cursor:
for row in cursor:
busStopID = row[0]
pop10 = row[1]
if busStopID not in dataDictionary.keys():
dataDictionary[busStopID] = [pop10]
else:
dataDictionary[busStopID].append(pop10)
with open(r'C:\Projects\Output\Averages2.csv', 'wb') as csvfile:
spamwriter = csv.writer(csvfile, delimiter=',')
for busStopID in dataDictionary.keys():
popList = dataDictionary[busStopID]
averagePop = sum(popList)/len(popList)
data = [busStopID, averagePop]
spamwriter.writerow(data)
print "Data Analysis Complete"
--------------------------------------------------------------------------------------
def secondFunction(number):
'this function multiples numbers by 3'
if type(number) == type(1) or type(number) == type(1.0):
return number *3
>>> secondFunction(4.0)
--------------------------------------------------------------------------------------
def thirdFunction(number, multiplier=3):
'this function multiples numbers by 3'
if type(number) == type(1) or type(number) == type(1.0):
return number *multiplier
>>>thirdFunction(4)

--------------------------------------------------------------------------------------
bufferDist = 400
buffDistUnit = "Feet"
lineName = '71 IB'
busSignage = 'Ferry Plaza'
sqlStatement = "NAME = '{0}' AND BUS_SIGNAG = '{1}'"
def selectBufferIntersect(selectIn,selectOut,bufferOut,intersectIn,
intersectOut, sqlStatement, bufferDist, buffDistUnit, lineName,
busSignage):
'a function to perform a bus stop analysis'
arcpy.Select_analysis(selectIn, selectOut,
sqlStatement.format(lineName, busSignage))
arcpy.Buffer_analysis(selectOut, bufferOut, "{0}
{1}".format(bufferDist), "FULL", "ROUND", "NONE", "")
arcpy.Intersect_analysis("{0} #;{1} #".format(bufferOut, intersectIn),
intersectOut, "ALL", "", "INPUT")
return intersectOut
--------------------------------------------------------------------------------------
def createResultDic(resultFC):
'search results of analysis and create results dictionary'
dataDictionary = {}
with arcpy.da.SearchCursor(resultFC, ["STOPID","POP10"]) as cursor:
for row in cursor:
busStopID = row[0]
pop10 = row[1]
if busStopID not in dataDictionary.keys():
dataDictionary[busStopID] = [pop10]
else:
dataDictionary[busStopID].append(pop10)
return dataDictionary
--------------------------------------------------------------------------------------
def createCSV(dictionary, csvname):
'a function takes a dictionary and creates a CSV file'
with open(csvname, 'wb') as csvfile:
csvwriter = csv.writer(csvfile, delimiter=',')
for busStopID in dictionary.keys():
popList = dictionary[busStopID]
averagePop = sum(popList)/len(popList)
data = [busStopID, averagePop]
csvwriter.writerow(data)
--------------------------------------------------------------------------------------
# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------
--
# 8662_Chapter4Modified1.py
# Created on: 2014-04-22 21:59:31.00000
# (generated by ArcGIS/ModelBuilder)
# Description:
# Adjusted by Silas Toms
# 2014 05 05
# -------------------------------------------------------------------------
--
# Import arcpy module
import arcpy
import csv
# Local variables:
Bus_Stops = r"C:\Projects\PacktDB.gdb\SanFrancisco\Bus_Stops"
CensusBlocks2010 = r"C:\Projects\PacktDB.gdb\SanFrancisco\CensusBlocks2010"
Inbound71 = r"C:\Projects\PacktDB.gdb\Chapter3Results\Inbound71"
Inbound71_400ft_buffer =
r"C:\Projects\PacktDB.gdb\Chapter3Results\Inbound71_400ft_buffer"
Intersect71Census =
r"C:\Projects\PacktDB.gdb\Chapter3Results\Intersect71Census"
bufferDist = 400
lineName = '71 IB'
busSignage = 'Ferry Plaza'
def selectBufferIntersect(selectIn,selectOut,bufferOut,intersectIn,
intersectOut, bufferDist,lineName, busSignage ):
arcpy.Select_analysis(selectIn,
selectOut,
"NAME = '{0}' AND BUS_SIGNAG =
'{1}'".format(lineName, busSignage))
arcpy.Buffer_analysis(selectOut,
bufferOut,
"{0} Feet".format(bufferDist),
"FULL", "ROUND", "NONE", "")
arcpy.Intersect_analysis("{0} #;{1} #".format(bufferOut,intersectIn),
intersectOut, "ALL", "", "INPUT")
return intersectOut
def createResultDic(resultFC):
dataDictionary = {}
with arcpy.da.SearchCursor(resultFC,
["STOPID","POP10"]) as cursor:
for row in cursor:
busStopID = row[0]
pop10 = row[1]
if busStopID not in dataDictionary.keys():
dataDictionary[busStopID] = [pop10]
else:
dataDictionary[busStopID].append(pop10)
return dataDictionary
def createCSV(dictionary, csvname):
with open(csvname, 'wb') as csvfile:
csvwriter = csv.writer(csvfile, delimiter=',')
for busStopID in dictionary.keys():
popList = dictionary[busStopID]
averagePop = sum(popList)/len(popList)
data = [busStopID, averagePop]
csvwriter.writerow(data)
analysisResult = selectBufferIntersect(Bus_Stops,Inbound71,
Inbound71_400ft_buffer,CensusBlocks2010,Intersect71Census,
bufferDist,lineName, busSignage )
dictionary = createResultDic(analysisResult)
createCSV(dictionary,r'C:\Projects\Output\Averages.csv')
print "Data Analysis Complete"                     
--------------------------------------------------------------------------------------
def selectBufferIntersect(selectIn,selectOut,bufferOut,intersectIn,
intersectOut, bufferDist,lineName, busSignage ):
arcpy.Select_analysis(selectIn,
selectOut,
"NAME = '{0}' AND BUS_SIGNAG =
'{1}'".format(lineName, busSignage))
arcpy.Buffer_analysis(selectOut,
bufferOut,
"{0} Feet".format(bufferDist),
"FULL", "ROUND", "NONE", "")
arcpy.Intersect_analysis("{0} #;{1} #".format(bufferOut,intersectIn),
intersectOut, "ALL", "", "INPUT")
return intersectOut
--------------------------------------------------------------------------------------
def formatSQLIN(dataList, sqlTemplate):
'a function to generate a SQL statement'
sql = sqlTemplate #"OBJECTID IN "
step = "("
for data in dataList:
step += str(data)
sql += step + ")"
return sql
def formatSQL(dataList, sqlTemplate):
'a function to generate a SQL statement'
sql = ''
for count, data in enumerate(dataList):
if count != len(dataList)-1:
sql += sqlTemplate.format(data) + ' OR '
else:
sql += sqlTemplate.format(data)
return sql
>>> dataVals = [1,2,3,4]
>>> sqlOID = "OBJECTID = {0}"
>>> sql = formatSQL(dataVals, sqlOID)
>>> print sql                      
--------------------------------------------------------------------------------------
def formatSQL2(dataList, sqlTemplate, operator=" OR "):
'a function to generate a SQL statement'
sql = ''
for count, data in enumerate(dataList):
if count != len(dataList)-1:
sql += sqlTemplate.format(data) + operator
else:
sql += sqlTemplate.format(data)
return sql
>>> sql = formatSQL2(dataVals, sqlOID," AND ")
>>> print sql
--------------------------------------------------------------------------------------
def formatSQLMultiple(dataList, sqlTemplate, operator=" OR "):
'a function to generate a SQL statement'
sql = ''
for count, data in enumerate(dataList):
if count != len(dataList)-1:
sql += sqlTemplate.format(*data) + operator
else:
sql += sqlTemplate.format(*data)
return sql
--------------------------------------------------------------------------------------
def formatIntersect(features):
'a function to generate an intersect string'
formatString = ''
for count, feature in enumerate(features):
if count != len(features)-1:
formatString += feature + " #;"
else:
formatString += feature + " #"
return formatString
>>> shpNames = ["example.shp","example2.shp"]
>>> iString = formatIntersect(shpNames)
>>> print iString
--------------------------------------------------------------------------------------
def createResultDic(resultFC, key, values):
dataDictionary = {}
fields = [key]
fields.extend(values)
with arcpy.da.SearchCursor(resultFC, fields) as cursor:
for row in cursor:
busStopID = row[0]
data = row[1:]
if busStopID not in dataDictionary.keys():
dataDictionary[busStopID] = [data]
else:
dataDictionary[busStopID].append(data)
return dataDictionary
--------------------------------------------------------------------------------------
def createResultDic(resultFC, key, values):
dataDic = {}
fields = []
if type(key) == type((1,2)) or type(key) == type([1,2]):
fields.extend(key)
length = len(key)
else:
fields = [key]
length = 1
fields.extend(values)
with arcpy.da.SearchCursor(resultFC, fields) as cursor:
for row in cursor:
busStopID = row[:length]
data = row[length:]
if busStopID not in dataDictionary.keys():
dataDictionary[busStopID] = {}
for counter,field in enumerate(values):
if field not in dataDictionary[busStopID].keys():
dataDictionary[busStopID][field] = [data[counter]]
else:
dataDictionary[busStopID][field].append(data[counter])
return dataDictionary
>>> rFC = r'C:\Projects\PacktDB.gdb\Chapter3Results\Intersect71Census'
>>> key = 'STOPID'
>>> values = 'HOUSING10','POP10'
>>> dic = createResultDic(rFC, key, values)
>>> dic[1122023]                      
--------------------------------------------------------------------------------------
csvname = r'C:\Projects\Output\Averages.csv'
dataKey = 'STOPID'
fields = 'HOUSING10','POP10'
dictionary = createResultDic(Intersect71Census, dataKey, fields)
header = [dataKey]
for field in fields:
header.append(field)
createCSV(header,csvname, 'wb' )
for counter, busStop in enumerate(dictionary.keys()):
datakeys = dictionary[busStop]
averages = [busStop]
for key in datakeys:
data = datakeys[key]
average = sum(data)/len(data)
averages.append(average)
createCSV(averages,csvname)
--------------------------------------------------------------------------------------
# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------
--
# 8662_Chapter4Modified2.py
# Created on: 2014-04-22 21:59:31.00000
# (generated by ArcGIS/ModelBuilder)
# Description:
# Adjusted by Silas Toms
# 2014 04 23
# -------------------------------------------------------------------------
--
# Import arcpy module
import arcpy
import csv
Bus_Stops = r"C:\Projects\PacktDB.gdb\SanFrancisco\Bus_Stops"
CensusBlocks2010 = r"C:\Projects\PacktDB.gdb\SanFrancisco\CensusBlocks2010"
Inbound71 = r"C:\Projects\PacktDB.gdb\Chapter4Results\Inbound71"
Inbound71_400ft_buffer =
r"C:\Projects\PacktDB.gdb\Chapter4Results\Inbound71_400ft_buffer"
Intersect71Census =
r"C:\Projects\PacktDB.gdb\Chapter4Results\Intersect71Census"
bufferDist = 400
bufferUnit = "Feet"
lineNames = [('71 IB', 'Ferry Plaza'),('71 OB','48th Avenue')]
sqlTemplate = "NAME = '{0}' AND BUS_SIGNAG = '{1}'"
intersected = [Inbound71_400ft_buffer, CensusBlocks2010]
dataKey = 'NAME','STOPID'
fields = 'HOUSING10','POP10'
csvname = r'C:\Projects\Output\Averages.csv'
def formatSQLMultiple(dataList, sqlTemplate, operator=" OR "):
'a function to generate a SQL statement'
sql = ''
for count, data in enumerate(dataList):
if count != len(dataList)-1:
sql += sqlTemplate.format(*data) + operator
else:
sql += sqlTemplate.format(*data)
return sql
def formatIntersect(features):
'a function to generate an intersect string'
formatString = ''
for count, feature in enumerate(features):
if count != len(features)-1:
formatString += feature + " #;"
else:
formatString += feature + " #"
return formatString
def createResultDic(resultFC, key, values):
dataDictionary = {}
fields = []
if type(key) == type((1,2)) or type(key) == type([1,2]):
fields.extend(key)
length = len(key)
else:
fields = [key]
length = 1
fields.extend(values)
with arcpy.da.SearchCursor(resultFC, fields) as cursor:
for row in cursor:
busStopID = row[:length]
data = row[length:]
if busStopID not in dataDictionary.keys():
dataDictionary[busStopID] = {}
for counter,field in enumerate(values):
if field not in dataDictionary[busStopID].keys():
dataDictionary[busStopID][field] = [data[counter]]
else:
dataDictionary[busStopID][field].append(data[counter])
return dataDictionary
def createCSV(data, csvname, mode ='ab'):
with open(csvname, mode) as csvfile:
csvwriter = csv.writer(csvfile, delimiter=',')
csvwriter.writerow(data)
sql = formatSQLMultiple(lineNames, sqlTemplate)
print 'Process: Select'
arcpy.Select_analysis(Bus_Stops,
Inbound71,
sql)
print 'Process: Buffer'
arcpy.Buffer_analysis(Inbound71,
Inbound71_400ft_buffer,
"{0} {1}".format(bufferDist, bufferUnit),
"FULL", "ROUND", "NONE", "")
iString = formatIntersect(intersected)
print iString
print 'Process: Intersect'
arcpy.Intersect_analysis(iString,
Intersect71Census, "ALL", "", "INPUT")
print 'Process Results'
dictionary = createResultDic(Intersect71Census, dataKey, fields)
print 'Create CSV'
header = [dataKey]
for field in fields:
header.append(field)
createCSV(header,csvname, 'wb' )
for counter, busStop in enumerate(dictionary.keys()):
datakeys = dictionary[busStop]
averages = [busStop]
for key in datakeys:
data = datakeys[key]
average = sum(data)/len(data)
averages.append(average)
createCSV(averages,csvname)
print "Data Analysis Complete"                      
--------------------------------------------------------------------------------------
csvname = "C:\Projects\Output\StationLocations.csv"
headers = 'Bus Line Name','Bus Stop ID', 'X','Y'
createCSV(headers, csvname, 'wb')
sql = "(NAME = '71 IB' AND BUS_SIGNAG = 'Ferry Plaza') OR (NAME = '71 OB'
AND BUS_SIGNAG = '48th Avenue')"
with arcpy.da.SearchCursor(Bus_Stops,['NAME', 'STOPID', 'SHAPE@XY'], sql)
as cursor:
for row in cursor:
linename = row[0]
stopid = row[1]
locationX = row[2][0]
locationY = row[2][1]
locationY = row[2][1]
data = linename, stopid, locationX, locationY
createCSV(data, csvname)                      
--------------------------------------------------------------------------------------
spatialReference = arcpy.SpatialReference(4326)
sql = "(NAME = '71 IB' AND BUS_SIGNAG = 'Ferry Plaza') OR (NAME = '71 OB'
AND BUS_SIGNAG = '48th Avenue')"
dataList = []
with arcpy.da.SearchCursor(Bus_Stops, ['NAME','STOPID','SHAPE@XY'], sql,
spatialReference) as cursor:
for row in cursor:
linename = row[0]
stopid = row[1]
locationX = row[2][0]
locationY = row[2][1]
data = linename, stopid, locationX, locationY
if data not in dataList:
dataList.append(data)
csvname = "C:\Projects\Output\StationLocations.csv"
headers = 'Bus Line Name','Bus Stop ID', 'X','Y'
createCSV(headers, csvname, 'wb')
for data in dataList:                      
--------------------------------------------------------------------------------------
sql = "OBJECTID = 1"
with arcpy.da.SearchCursor(Bus_Stops,
['STOPID','NAME', 'OID@'],
sql) as cursor:
for row in cursor:
--------------------------------------------------------------------------------------
sql = "NAME LIKE '71%'"
with arcpy.da.UpdateCursor(Bus_Stops, ['NAME'],sql),) as cursor:
for row in cursor:
lineName = row[0]
newName = lineName.replace('71','75')
row[0] = newName
--------------------------------------------------------------------------------------
sql = 'OBJECTID < 5'
with arcpy.da.UpdateCursor(Bus_Stops, [ 'OID@', 'SHAPE@'],sql) as cursor:
for row in cursor:
row[1] = arcpy.Point(5999783.78657, 2088532.563956)

--------------------------------------------------------------------------------------
sql = 'OBJECTID < 5'
with arcpy.da.UpdateCursor(Bus_Stops, [ 'OID@', 'SHAPE@XY'],sql) as cursor:
for row in cursor:
row[1] =(5999783.786500007, 2088532.5639999956)
--------------------------------------------------------------------------------------
sql = 'OBJECTID < 5'
with arcpy.da.UpdateCursor(Bus_Stops, [ 'OID@', 'SHAPE@JSON'],sql) as
cursor:
for row in cursor:
print row
row[1] = u'{"x":5999783.7865000069, "y":2088532.5639999956,
"spatialReference":{"wkid":102643}}'
--------------------------------------------------------------------------------------
sql = 'OBJECTID < 2'
Bus_Stops = r'C:\Projects\PacktDB.gdb\Bus_Stops'
with arcpy.da.UpdateCursor(Bus_Stops,
['OID@',
'SHAPE@XY'],sql) as cursor:
for row in cursor:
--------------------------------------------------------------------------------------
Bus_Stops = r'C:\Projects\PacktDB.gdb\TestBusStops'
insertCursor = arcpy.da.InsertCursor(Bus_Stops, ['SHAPE@','NAME','STOPID'])
coordinatePair = (6001672.5869999975, 2091447.0435000062)
newPoint = arcpy.Point(*coordinatePair)
dataList = [newPoint,'NewStop1',112121]
insertCursor.insertRow(dataList)
del insertCursor

--------------------------------------------------------------------------------------
Bus_Stops = r'C:\Projects\PacktDB.gdb\TestBusStops'
listOfLists = [[(6002672.58675, 2092447.04362),'NewStop2',112122],
[(6003672.58675, 2093447.04362),'NewStop3',112123],
[(6004672.58675, 2094447.04362),'NewStop4',112124]
]
with arcpy.da.InsertCursor(Bus_Stops,
['SHAPE@',
'NAME',
'STOPID']) as iCursor:
for dataList in listOfLists:
newPoint = arcpy.Point(*dataList[0])
dataList[0] = newPoint
--------------------------------------------------------------------------------------
listOfPoints = [(6002672.58675, 2092447.04362),
(6003672.58675, 2093447.04362),
(6004672.58675, 2094447.04362)
]
line = 'New Bus Line'
lineID = 12345
busLine = r'C:\Projects\PacktDB.gdb\TestBusLine'
insertCursor = arcpy.da.InsertCursor(busLine, ['SHAPE@',
'LINE', 'LINEID'])
lineArray = arcpy.Array()
for pointsPair in listOfPoints:
newPoint = arcpy.Point(*pointsPair)
lineArray.add(newPoint)
newLine = arcpy.Polyline(lineArray)
insertData = newLine, line, lineID

--------------------------------------------------------------------------------------
listOfPoints = [(6002672.58675, 2092447.04362),
(6003672.58675, 2093447.04362),
(6004672.58675, 2093447.04362),
(6004672.58675, 2091447.04362)
]
polyName = 'New Polygon'
polyID = 54321
blockPoly = r'C:\Projects\PacktDB.gdb\Chapter5Results\TestPolygon'
insertCursor = arcpy.da.InsertCursor(blockPoly, ['SHAPE@', 'BLOCK',
'BLOCKID'])
polyArray = arcpy.Array()
for pointsPair in listOfPoints:
newPoint = arcpy.Point(*pointsPair)
polyArray.add(newPoint)
newPoly = arcpy.Polygon(polyArray)
insertData = newPoly, polyName, polyID
insertCursor.insertRow(insertData)
--------------------------------------------------------------------------------------
>>> Point = arcpy.Point(4,5)
>>> point1 = arcpy.Point(4,5)
>>> Point.equals(point1)
True
>>> Point.contains(point1)
True
>>> Point. crosses(point1)
False
>>> Point.overlaps(point1)
False
>>> Point.disjoint(point1)
False
>>> Point.within(point1)
True
>>> point.X, Point.Y
(4.0, 5.0)

--------------------------------------------------------------------------------------
>>> Point = arcpy.Point(4,5)
>>> point1 = arcpy.Point(7,9)
>>> Array = arcpy.Array()
>>> Array.add(point)
>>> Array.add(point1)
--------------------------------------------------------------------------------------
>>> Point = arcpy.Point(4,5)
>>> point1 = arcpy.Point(7,9)
>>> pList = [Point,point1]
>>> Array = arcpy.Array()
>>> Array.extend(pList)

--------------------------------------------------------------------------------------
>>> Point = arcpy.Point(4,5)
>>> point1 = arcpy.Point(7,9)
>>> point2 = arcpy.Point(11,13)
>>> pList = [Point,point1]
>>> Array = arcpy.Array()
>>> Array.extend(pList)
>>> Array.replace(1,point2)
>>> point3 = arcpy.Point(17,15)
>>> Array.insert(2,point3)
--------------------------------------------------------------------------------------
>>> Point = arcpy.Point(4,5)
>>> point1 = arcpy.Point(7,9)
>>> pList = [Point,point1]
>>> Array = arcpy.Array()
>>> Array.extend(pList)
>>> pLine = arcpy.Polyline(Array)
--------------------------------------------------------------------------------------
>>> pLine.firstPoint
<Point (4.0, 5.0, #, #)>
>>> pLine.lastPoint
<Point (7.0, 9.0, #, #)>
pLine.getPart()
<Array [<Array [<Point (4.0, 5.0, #, #)>, <Point (7.0, 9.0, #, #)>]>]>
>>> pLine.trueCentroid
<Point (5.5, 7.0, #, #)>
>>> pLine.length
5.0
>>> pLine.pointCount
--------------------------------------------------------------------------------------
>>> bufferOfLine = pLine.buffer(10)
>>> bufferOfLine.area
413.93744395
>>> bufferOfLine.contains(pLine)
True
>>> newPoint = arcpy.Point(25,19)
>>> pLine.distanceTo(newPoint)
20.591260281974
--------------------------------------------------------------------------------------
>>> nPoint = pLine.positionAlongLine(3)
>>> nPoint.firstPoint.X, nPoint.firstPoint.Y
(5.8, 7.4)>>> pPoint = pLine.positionAlongLine(.5,True)
>>> pPoint.firstPoint.X,pPoint.firstPoint.Y
(5.5, 7.0)
--------------------------------------------------------------------------------------
>>> import arcpy
>>> point1 = arcpy.Point(12,16)
>>> point2 = arcpy.Point(14, 18)
>>> point3 = arcpy.Point(11, 20)
>>> Array = arcpy.Array()
>>> Points = [point1,point2,point3]
>>> Array.extend(points)
>>> Polygon = arcpy.Polygon(array)
>>> arcpy.CopyFeatures_management(polygon, r'C:\Projects\Polygon.shp')
<Result 'C:\\Projects\\Polygon.shp'>
--------------------------------------------------------------------------------------
import arcpyPoint = arcpy.Point(6004548.231,2099946.033)
point1 = arcpy.Point(6008673.935,2105522.068)
point2 = arcpy.Point(6003351.355,2100424.783)Array = arcpy.Array()
Array.add(point1)
Array.add(point)
array.add(point2)
Polygon = arcpy.Polygon(array, 2227)
buffPoly = Polygon.buffer(50)
features = [Polygon,buffPoly]
arcpy.CopyFeatures_management(features,
r'C:\Projects\Polygons.shp')
spatialRef = arcpy.SpatialReference(4326)
polygon4326 = Polygon.projectAs(spatialRef)
arcpy.CopyFeatures_management(polygon4326,
r'C:\Projects\polygon4326.shp')
--------------------------------------------------------------------------------------
import arcpy
cen2010 = r'C:\Projects\ArcPy.gdb\SanFrancisco\CensusBlocks2010'
blockPolys = arcpy.CopyFeatures_management(cen2010,
arcpy.Geometry())
--------------------------------------------------------------------------------------
# Generate 400 foot buffers around each bus stop
import arcpy,csv
busStops = r"C:\Projects\PacktDB.gdb\SanFrancisco\Bus_Stops"
censusBlocks2010 = r"C:\Projects\PacktDB.gdb\SanFrancisco\CensusBlocks2010"
sql = "NAME = '71 IB' AND BUS_SIGNAG = 'Ferry Plaza'"
dataDic = {}
with arcpy.da.SearchCursor(busStops, ['NAME','STOPID','SHAPE@'], sql) as
cursor:
for row in cursor:
linename = row[0]
stopid = row[1]
shape = row[2]
dataDic[stopid] = shape.buffer(400), linename
--------------------------------------------------------------------------------------
# Intersect census blocks and bus stop buffers
processedDataDic = {} = {}
for stopid in dataDic.keys():
values = dataDic[stopid]
busStopBuffer = values[0]
linename = values[1]
blocksIntersected = []
with arcpy.da.SearchCursor(censusBlocks2010,
['BLOCKID10','POP10','SHAPE@']) as cursor:
for row in cursor:
block = row[2]
population = row[1]
blockid = row[0]
if busStopBuffer.overlaps(block) ==True:
interPoly = busStopBuffer.intersect(block,4)
data = row[0],row[1],interPoly, block
blocksIntersected.append(data)
processedDataDic[stopid] = values, blocksIntersected        
--------------------------------------------------------------------------------------
# Create an average population for each bus stop
dataList = []
for stopid in processedDataDic.keys():
allValues = processedDataDic[stopid]
popValues = []
blocksIntersected = allValues[1]
for blocks in blocksIntersected:
popValues.append(blocks[1])
averagePop = sum(popValues)/len(popValues)
busStopLine = allValues[0][1]
busStopID = stopid
finalData = busStopLine, busStopID, averagePop
dataList.append(finalData)
--------------------------------------------------------------------------------------
# Generate a spreadsheet with the analysis results
def createCSV(data, csvname, mode ='ab'):
with open(csvname, mode) as csvfile:
csvwriter = csv.writer(csvfile, delimiter=',')
csvwriter.writerow(data)
csvname = "C:\Projects\Output\StationPopulations.csv"
headers = 'Bus Line Name','Bus Stop ID', 'Average Population'
createCSV(headers, csvname, 'wb')
for data in dataList:
createCSV(data, csvname)
--------------------------------------------------------------------------------------
dataList = []
for stopid in processedDataDic.keys():
allValues = processedDataDic[stopid]
popValues = []
blocksIntersected = allValues[1]
for blocks in blocksIntersected:
pop = blocks[1]
totalArea = blocks[-1].area
interArea = blocks[-2].area
finalPop = pop * (interArea/totalArea)
popValues.append(finalPop)
averagePop = round(sum(popValues)/len(popValues),2)
busStopLine = allValues[0][1]
busStopID = stopid
finalData = busStopLine, busStopID, averagePop
dataList.append(finalData)        
--------------------------------------------------------------------------------------
#Chapter 7.py
import arcpy, csv
busStops = arcpy.GetParameterAsText(0)
censusBlocks2010 = arcpy.GetParameterAsText(1)
censusBlockField = arcpy.GetParameterAsText(2)
csvname = arcpy.GetParameterAsText(3)
headers = arcpy.GetParameterAsText(4).split(',')
sql = arcpy.GetParameterAsText(5)
keyfields = arcpy.GetParameterAsText(6).split(';')
dataDic = {}
censusFields = ['BLOCKID10',censusBlockField, 'SHAPE@']
if "SHAPE@" not in keyfields:
keyfields.append("SHAPE@")
arcpy.AddMessage(busStops)
arcpy.AddMessage(censusBlocks2010)
arcpy.AddMessage(censusBlockField)
arcpy.AddMessage(csvname)
arcpy.AddMessage(sql)
arcpy.AddMessage(keyfields)
--------------------------------------------------------------------------------------
import arcpy, csv
busStops = arcpy.GetParameterAsText(0)
censusBlocks2010 = arcpy.GetParameterAsText(1)
censusBlockField = arcpy.GetParameterAsText(2)
csvname = arcpy.GetParameterAsText(3)
headers = arcpy.GetParameterAsText(4).split(',')
sql = arcpy.GetParameterAsText(5)
keyfields = arcpy.GetParameterAsText(6).split(';')
dataDic = {}
censusFields = [ 'BLOCKID10',censusBlockField,'SHAPE@']
if "SHAPE@" not in keyfields:
keyfields.append("SHAPE@")
arcpy.AddMessage(busStops)
arcpy.AddMessage(censusBlocks2010)
arcpy.AddMessage(censusBlockField)
arcpy.AddMessage(csvname)
arcpy.AddMessage(sql)
arcpy.AddMessage(keyfields)
x = 0
with arcpy.da.SearchCursor(busStops, keyfields, sql) as cursor:
for row in cursor:
stopid = x
shape = row[-1]
dataDic[stopid] = []
dataDic[stopid].append(shape.buffer(400))
dataDic[stopid].extend(row[:-1])
x+=1
processedDataDic = {}
for stopid in dataDic.keys():
values = dataDic[stopid]
busStopBuffer = values[0]
blocksIntersected = []
with arcpy.da.SearchCursor(censusBlocks2010, censusFields) as cursor:
for row in cursor:
block = row[-1]
population = row[1]
blockid = row[0]
if busStopBuffer.overlaps(block) ==True:
interPoly = busStopBuffer.intersect(block,4)
data = population,interPoly, block
blocksIntersected.append(data)
processedDataDic[stopid] = values, blocksIntersected
dataList = []
for stopid in processedDataDic.keys():
allValues = processedDataDic[stopid]
popValues = []
blocksIntersected = allValues[-1]
for blocks in blocksIntersected:
pop = blocks[0]
totalArea = blocks[-1].area
interArea = blocks[-2].area
finalPop = pop * (interArea/totalArea)
popValues.append(finalPop)
averagePop = round(sum(popValues)/len(popValues),2)
busStopLine = allValues[0][1]
busStopID = stopid
finalData = busStopLine, busStopID, averagePop
dataList.append(finalData)
def createCSV(data, csvname, mode ='ab'):
with open(csvname, mode) as csvfile:
csvwriter = csv.writer(csvfile, delimiter=',')
csvwriter.writerow(data)
headers.insert(0,"ID")
createCSV(headers, csvname, 'wb')
for data in dataList:
createCSV(data, csvname)        
--------------------------------------------------------------------------------------
import arcpy
mxdPath = 'C:\Projects\MXDs\Chapter8\BrokenLinks.mxd'
mxdObject = arcpy.mapping.MapDocument(mxdPath)
brokenLinks = arcpy.mapping.ListBrokenDataSources(mxdObject)
for link in brokenLinks:
print link.name, link.dataSource
--------------------------------------------------------------------------------------
oldPath = r'C:\Projects\MXDs\Data'
newPath = r'C:\Projects'
mxdObject.findAndReplaceWorkspacePaths(oldPath,newPath)
mxdObject.save()
--------------------------------------------------------------------------------------
oldPath = r'C:\Projects\MXDs\Data'
oldType = 'SHAPEFILE_WORKSPACE'
newPath = r'C:\Projects'
newType = 'FILEGDB_WORKSPACE'
mxdObject.replaceWorkspaces(oldPath,oldType,newPath,newType)
mxdObject.save()


--------------------------------------------------------------------------------------
import arcpy
layerDic = {'Bus_Stops':[r'C:\Projects\OldDataPath', r'C:\Projects'],
'stclines_streets': [r'C:\Projects\OtherPath', r'C:\Projects']}
mxdPath = r'C:\Projects\MXDs\Chapter8\BrokenLinks.mxd'
mxdObject = arcpy.mapping.MapDocument(mxdPath)
brokenLinks = arcpy.mapping.ListBrokenDataSources(mxdObject)
for layer in brokenLinks:
oldPath, newPath = layerDic[layer.name]
layer.findAndReplaceWorkspacePath(oldPath, newPath )
mxdObject.save()
--------------------------------------------------------------------------------------
import arcpy, glob, os
oldPath = r'C:\Projects\MXDs\Data'
newPath = r'C:\Projects'
folderPath = r'C:\Projects\MXDs\Chapter8'
mxdPathList = glob.glob(os.path.join(folderPath, '*.mxd'))
for path in mxdPathList:
mxdObject = arcpy.mapping.MapDocument(mxdPath)
mxdObject.findAndReplaceWorkspacePaths(oldPath,newPath)
mxdObject.save()
--------------------------------------------------------------------------------------
import arcpy, glob, os
mxdFolder = r'C:\Projects\MXDs\Chapter8'
pdfFolder = r'C:\Projects\PDFs\Chapter8'
mxdPathList = glob.glob(os.path.join(mxdFolder, '*.mxd'))
for mxdPath in mxdPathList:
mxdObject = arcpy.mapping.MapDocument(mxdPath)
arcpy.mapping.ExportToPDF(mxdObject,
os.path.join(pdfFolder,
basepath(
mxdPath.replace('mxd','pdf')
)))
--------------------------------------------------------------------------------------
import arcpy, os
dirpath = os.path.dirname
basepath = os.path.basename
Bus_Stops = r"C:\Projects\SanFrancisco.gdb\Bus_Stops"
selectedBusStop =
r'C:\Projects\SanFrancisco.gdb\Chapter8Results\SelectedBusStop'
selectedStopBuffer =
r'C:\Projects\SanFrancisco.gdb\Chapter8Results\SelectedStopBuffer'
CensusBlocks2010 = r"C:\Projects\SanFrancisco.gdb\CensusBlocks2010"
selectedBlock =
r'C:\Projects\SanFrancisco.gdb\Chapter8Results\SelectedCensusData'
pdfFolder = r'C:\Projects\PDFs\Chapter8\Map_{0}'
bufferDist = 400
sql = "(NAME = '71 IB' AND BUS_SIGNAG = 'Ferry Plaza')"
mxdObject = arcpy.mapping.MapDocument("CURRENT")
dataFrame = arcpy.mapping.ListDataFrames(mxdObject, "Layers")[0]
elements = arcpy.mapping.ListLayoutElements(mxdObject)
for el in elements:
if el.type =="TEXT_ELEMENT":
if el.text == 'Title Element':
titleText = el
elif el.text == 'Subtitle Element':
subTitleText = el
arcpy.MakeFeatureLayer_management(CensusBlocks2010, 'blocks_lyr')
layersList = arcpy.mapping.ListLayers(mxdObject,"",dataFrame)
layerStops = layersList[0]
layerCensus = layersList[1]
layerBuffer = layersList[2]
layerBlocks = layersList[3]
if layerBlocks.dataSource != selectedBlock:
layerBlocks.replaceDataSource(dirpath(dirpath(layerBlocks.dataSource)),
'FILEGDB_WORKSPACE',basepath(selectedBlock))
if layerStops.dataSource != selectedBusStop:
layerStops.replaceDataSource(dirpath(dirpath(layerStops.dataSource)),
'FILEGDB_WORKSPACE',basepath(selectedBusStop))
if layerBuffer.dataSource != selectedStopBuffer:
layerBuffer.replaceDataSource(dirpath(dirpath(layerBuffer.dataSource)),
'FILEGDB_WORKSPACE',basepath(selectedStopBuffer))
layerStops.visible = True
layerBuffer.visible = True
layerCensus.visible = False
with arcpy.da.SearchCursor(Bus_Stops,['SHAPE@','STOPID','NAME',
'BUS_SIGNAG' ,'OID@','SHAPE@XY'],sql)
for row in cursor:
stopPointGeometry = row[0]
stopBuffer = stopPointGeometry.buffer(bufferDist)
with arcpy.da.UpdateCursor(layerBlocks,['OID@']) as dcursor:
for drow in dcursor:
dcursor.deleteRow()
arcpy.SelectLayerByLocation_management('blocks_lyr', 'intersect',
stopBuffer, "", "NEW_SELECTION")
with arcpy.da.SearchCursor('blocks_lyr',['SHAPE@','POP10','OID@'])
as bcursor:
inCursor = arcpy.da.InsertCursor(selectedBlock,
['SHAPE@','POP10'])
for drow in bcursor:
data = drow[0],drow[1]
inCursor.insertRow(data)
del inCursor
with arcpy.da.UpdateCursor(selectedBusStop,['OID@']) as dcursor:
for drow in dcursor:
dcursor.deleteRow()
inBusStopCursor = arcpy.da.InsertCursor(selectedBusStop,['SHAPE@'])
data = [row[0]]
inBusStopCursor.insertRow(data)
del inBusStopCursor
with arcpy.da.UpdateCursor(selectedStopBuffer,['OID@']) as dcursor:
for drow in dcursor:
dcursor.deleteRow()
inBufferCursor = arcpy.da.InsertCursor(selectedStopBuffer,
['SHAPE@'])
data = [stopBuffer]
inBufferCursor.insertRow(data)
del inBufferCursor
layerStops.name = "Stop #{0}".format(row[1])
arcpy.RefreshActiveView()
dataFrame.extent = arcpy.Extent(row[-1][0]-1200,row[-1][1]-1200,
row[-1][0]+1200,row[-1][1]-1200)
subTitleText.text = "Route {0}".format(row[2])
titleText.text = "Bus Stop {0}".format(row[1])
outPath = pdfFolder.format( str(row[1])+ "_" + str(row[-2])) +
'.pdf'
print outPath
arcpy.mapping.ExportToPDF(mxdObject,outPath)
titleText.text = 'Title Element'
subTitleText.text = 'Subtitle Element'
arcpy.RefreshActiveView()
--------------------------------------------------------------------------------------
import arcpy, os
Bus_Stops = r"C:\Projects\SanFrancisco.gdb\Bus_Stops"
selectedBusStop =
r'C:\Projects\SanFrancisco.gdb\Chapter8Results\SelectedBusStop'
selectedStopBuffer =
r'C:\Projects\SanFrancisco.gdb\Chapter8Results\SelectedStopBuffer'
CensusBlocks2010 = r"C:\Projects\SanFrancisco.gdb\CensusBlocks2010"
selectedBlock =
r'C:\Projects\SanFrancisco.gdb\Chapter8Results\SelectedCensusData'
pdfFolder = r'C:\Projects\PDFs\Chapter8\Map_{0}'
bufferDist = 400
sql = "(NAME = '71 IB' AND BUS_SIGNAG = 'Ferry Plaza')"
--------------------------------------------------------------------------------------
mxdObject = arcpy.mapping.MapDocument("CURRENT")
dataFrame = arcpy.mapping.ListDataFrames(mxdObject, "Layers")[0]
elements = arcpy.mapping.ListLayoutElements(mxdObject)
for el in elements:
if el.type =="TEXT_ELEMENT":
if el.text == 'Title Element':
titleText = el
elif el.text == 'Subtitle Element':
subTitleText = el

--------------------------------------------------------------------------------------
arcpy.MakeFeatureLayer_management(CensusBlocks2010, 'blocks_lyr')
layersList = arcpy.mapping.ListLayers(mxdObject,"",dataFrame)
layerStops = layersList[0]
layerCensus = layersList[1]
layerBuffer = layersList[2]
layerBlocks = layersList[3]
--------------------------------------------------------------------------------------

if layerBlocks.dataSource != selectedBlock:
layerBlocks.replaceDataSource(dirpath(dirpath(layerBlocks.dataSource)),
'FILEGDB_WORKSPACE',basepath(selectedBlock))
if layerStops.dataSource != selectedBusStop:
layerStops.replaceDataSource(dirpath(dirpath (layerStops.dataSource)),
'FILEGDB_WORKSPACE',basepath(selectedBusStop))
if layerBuffer.dataSource != selectedStopBuffer:
layerBuffer.replaceDataSource(dirpath( dirpath(layerBuffer.dataSource)),
'FILEGDB_WORKSPACE',basepath(selectedStopBuffer))
--------------------------------------------------------------------------------------
with arcpy.da.SearchCursor(Bus_Stops,['SHAPE@','STOPID','NAME',
'BUS_SIGNAG' ,'OID@','SHAPE@XY'],sql)
as cursor:
for row in cursor:
stopPointGeometry = row[0]
stopBuffer = stopPointGeometry.buffer(bufferDist)
with arcpy.da.UpdateCursor(layerBlocks,['OID@']) as
dcursor:
for drow in dcursor:
dcursor.deleteRow()
--------------------------------------------------------------------------------------

arcpy.SelectLayerByLocation_management('blocks_lyr', 'intersect',
stopBuffer, "", "NEW_SELECTION")
with arcpy.da.SearchCursor('blocks_lyr', ['SHAPE@',
'POP10','OID@']) as bcursor:
inCursor = arcpy.da.InsertCursor(selectedBlock,['SHAPE@',
'POP10'])
for drow in bcursor:
data = drow[0],drow[1]
inCursor.insertRow(data)
del inCursor
--------------------------------------------------------------------------------------
with arcpy.da.UpdateCursor(selectedBusStop,['OID@']) as dcursor:
for drow in dcursor:
dcursor.deleteRow()
inBusStopCursor = arcpy.da.InsertCursor(selectedBusStop,['SHAPE@'])
data = [row[0]]
inBusStopCursor.insertRow(data)
del inBusStopCursor
with arcpy.da.UpdateCursor(selectedStopBuffer,['OID@']) as dcursor:
for drow in dcursor:
dcursor.deleteRow()
inBufferCursor = arcpy.da.InsertCursor(selectedStopBuffer,['SHAPE@'])
data = [stopBuffer]
inBufferCursor.insertRow(data)
del inBufferCursor
--------------------------------------------------------------------------------------
layerStops.name = "Stop #{0}".format(row[1])
dataFrame.extent = arcpy.Extent(row[-1][0]-1200,row[-1][1]-1200,
row[-1][0]+1200,row[-1][1]-1200)
subTitleText.text = "Route {0}".format(row[2])
titleText.text = "Bus Stop {0}".format(row[1])
arcpy.RefreshActiveView()
--------------------------------------------------------------------------------------
outPath = pdfFolder.format(str(row[1])+"_"+ str(row[-2]))+'.pdf'
arcpy.mapping.ExportToPDF(mxdObject,outPath)
titleText.text = 'Title Element'
subTitleText.text = 'Subtitle Element'
arcpy.RefreshActiveView()
--------------------------------------------------------------------------------------
import arcpy
mxdPath = r'C:\Projects\MXDs\Chapter9\MapDocument1.mxd'
mxdObject = arcpy.mapping.MapDocument(mxdPath)
dataFrame = arcpy.mapping.ListDataFrames(mxdObject, "Layers")[0]
layersList = arcpy.mapping.ListLayers(mxdObject,"",dataFrame)
print layersList
--------------------------------------------------------------------------------------
layersList = arcpy.mapping.ListLayers(mxdObject,"",dataFrame)
busStops = layersList[0]
busStops.definitionQuery = "NAME = '71 IB' AND BUS_SIGNAG = 'Ferry Plaza'"
--------------------------------------------------------------------------------------
import arcpy
bufferDist = 400
mxdPath = r'C:\Projects\MXDs\Chapter9\MapDocument1.mxd'
mxdObject = arcpy.mapping.MapDocument(mxdPath)
dataFrame= arcpy.mapping.ListDataFrames(mxdObject, "Layers")[0]
layersList = arcpy.mapping.ListLayers(mxdObject,"",dataFrame)
busStops = layersList[0]
defQuery = "NAME = '71 IB' AND BUS_SIGNAG = 'Ferry Plaza'"
busStops.definitionQuery = defQuery
idList =[]
with arcpy.da.SearchCursor(busStops,['OID@']) as cursor:
for row in cursor:
idList.append(row[0])
for oid in idList:
newQuery = "OBJECTID = {0}".format(oid)
print newQuery
busStops.definitionQuery = newQuery
with arcpy.da.SearchCursor(busStops,
['SHAPE@','STOPID','NAME','BUS_SIGNAG','OID@','SHAPE@XY']) as cursor:
for row in cursor:
stopPointGeometry = row[0]
stopBuffer = stopPointGeometry.buffer(bufferDist)
--------------------------------------------------------------------------------------
import arcpy
bufferDist = 400
mxdPath = r'C:\Projects\MXDs\Chapter9\MapDocument1.mxd'
mxdObject = arcpy.mapping.MapDocument(mxdPath)
dataFrame = arcpy.mapping.ListDataFrames(mxdObject,
"Layers")[0]
layersList = arcpy.mapping.ListLayers(mxdObject,"",dataFrame)
busStops = layersList[0]
censusBlocks = layersList[3]
sql = "NAME = '71 IB' AND BUS_SIGNAG = 'Ferry Plaza'"
with arcpy.da.SearchCursor(busStops,['SHAPE@', 'STOPID', 'NAME',
'BUS_SIGNAG','OID@'],sql) as cursor:
for row in cursor:
bus Query = 'OBJECTID = {0}'.format(row[-1])
busStops.definitionQuery = bus Query
stopPointGeometry = row[0]
stop Buffer = stopPointGeometry. Buffer(bufferDist)
arcpy.SelectLayerByLocation_management(censusBlocks,'intersect',stopBuffer,
"","NEW_SELECTION")
blockList = []
with arcpy.da.SearchCursor(censusBlocks,
['OID@']) as bcursor:
for brow in bcursor:
blockList.append(brow[0])
newQuery = 'OBJECTID IN ('for COUNTER, oid in enumerate(blockList):
if COUNTER < len(blockList)-1:
newQuery += str(oid) + ','
else:
newQuery += str(oid)+ ')'
print newQuery
--------------------------------------------------------------------------------------
censusBlocks.definitionQuery = newQuery
dataFrame.extent = censusBlocks.getExtent()
arcpy.SelectLayerByAttribute_management(censusBlocks,
"CLEAR_SELECTION")
--------------------------------------------------------------------------------------
import arcpy
arcpy.env.overwriteOutput = 1
bufferDist = 400
pdfFolder = r'C:\Projects\PDFs\Chapter9\Map_{0}'
mxdPath = r'C:\Projects\MXDs\Chapter9\MapDocument1.mxd'
mxdObject = arcpy.mapping.MapDocument(mxdPath)
dataFrame = arcpy.mapping.ListDataFrames(mxdObject,"Layers")[0]
elements = arcpy.mapping.ListLayoutElements(mxdObject)
for el in elements:
if el.type =="TEXT_ELEMENT":
if el.text == 'Title Element':
titleText = el
elif el.text == 'Subtitle Element':
subTitleText = el
layersList = arcpy.mapping.ListLayers(mxdObject,
"",dataFrame)
busStops = layersList[0]
bufferLayer = layersList[2]
censusBlocks = layersList[4]
sql = "NAME = '71 IB' AND BUS_SIGNAG = 'Ferry Plaza'"
with arcpy.da.SearchCursor(busStops,['SHAPE@',
'STOPID',
'NAME',
'BUS_SIGNAG',
'OID@'],sql) as cursor:
for row in cursor:
busQuery = 'OBJECTID = {0}'.format(row[-1])
busStops.definitionQuery = busQuery
stopPointGeometry = row[0]
stopBuffer = stopPointGeometry.buffer(bufferDist)
arcpy.CopyFeatures_management(stopBuffer,r"C:\Projects\Output\400Buffer.shp
")
bufferLayer.replaceDataSource(r"C:\Projects\Output",
"SHAPEFILE_WORKSPACE",
"400Buffer")
arcpy.SelectLayerByLocation_management(censusBlocks,
'intersect',
stopBuffer,
"",
"NEW_SELECTION")
blockList = []
with arcpy.da.SearchCursor(censusBlocks,
['OID@']) as bcursor:
for brow in bcursor:
blockList.append(brow[0])
--------------------------------------------------------------------------------------
newQuery = 'OBJECTID IN ('
for COUNTER, oid in enumerate(blockList):
if COUNTER < len(blockList)-1:
newQuery += str(oid) + ','
else:
newQuery += str(oid)+ ')'
print newQuery
censusBlocks.definitionQuery = newQuery
dataFrame.extent = censusBlocks.getExtent()
arcpy.SelectLayerByAttribute_management(censusBlocks,
"CLEAR_SELECTION")
dataFrame.scale = dataFrame.scale * 1.1
arcpy.RefreshActiveView()
subTitleText.text = "Route {0}".format(row[2])
titleText.text = "Bus Stop {0}".format(row[1])
outPath = pdfFolder.format( str(row[1])) + '.pdf'
print outPath
arcpy.mapping.ExportToPDF(mxdObject,outPath)
titleText.text = 'Title Element'
subTitleText.text = 'Subtitle Element'
censusBlocks.definitionQuery = ''
busStops.definitionQuery = ''
--------------------------------------------------------------------------------------
def createCSV(data, csvname, mode ='ab'):
'creates a csv file'
import csv
with open(csvname, mode) as csvfile:
csvwriter = csv.writer(csvfile, delimiter=',')
csvwriter.writerow(data)
del csv
--------------------------------------------------------------------------------------
def nonIntersect(poly1,poly2):
'returns area of non-intersect between two polygons'
if poly1.overlaps(poly2) == True:
return poly1.difference(poly2)
else:
return poly1
--------------------------------------------------------------------------------------
def generatePoints(fc, pop,constrant, workspace='in_memory'):
'generate random points'
import os, arcpy
arcpy.CreateRandomPoints_management(workspace, fc,
constrant, "", pop, "")
return os.path.join(workspace, fc)
--------------------------------------------------------------------------------------
# Import the necessary modules
import arcpy, os
from common.useful import nonIntersect, generatePoints,createCSV
# Add an overwrite statement
arcpy.env.overwriteOutput = True
# Define the data inputs
busStops = r'C:\Projects\SanFrancisco.gdb\SanFrancisco\Bus_Stops'
parks = r'C:\Projects\SanFrancisco.gdb\SanFrancisco\RPD_Parks'
censusBlocks =
r'C:\Projects\SanFrancisco.gdb\SanFrancisco\CensusBlocks2010'
csvName = r'C:\Projects\Output\Chapter10Analysis.csv'
# Create the spreadsheet in memory and add field headers
headers = 'Line Name','Stop ID', 'Total Population Served'
createCSV(headers,csvName,mode='wb')
# Copy the census block data into a feature layer
arcpy.MakeFeatureLayer_management(censusBlocks,'census_lyr')
# Copy the park data geometries into a list and union them allparkGeoms =
arcpy.CopyFeatures_management(parks,arcpy.Geometry())
parkUnion = parkGeoms[0]
for park in parkGeoms[1:]:
parkUnion = parkUnion.union(park)
# Create a search cursor to iterate the bus stop data
sql = "NAME = '71 IB' AND BUS_SIGNAG = 'Ferry Plaza'"
with arcpy.da.SearchCursor(busStops, ['NAME','STOPID','SHAPE@'],sql) as
cursor:
for row in cursor:
lineName = row[0]
stopID = row[1]
stop = row[2]
busBuf = stop.buffer(400)
# Select census blocks that intersect the bus buffer
arcpy.SelectLayerByLocation_management("census_lyr","intersect",
busBuf,'','NEW_SELECTION')
# Use a second Cursor to find the selected population
totalPopulation = 0
with arcpy.da.SearchCursor("census_lyr",['SHAPE@','POP10',
'BLOCKID10']) as ncursor:
for nrow in ncursor:
block = nrow[0]
checkedBlock = nonIntersect(block, parkUnion)
blockName = nrow[2]
population = nrow[1]
if population != 0:
points = generatePoints("PopPoints",
population,checkedBlock)
pointsGeoms =
arcpy.CopyFeatures_management(points,arcpy.Geometry())
pointsUnion = pointsGeoms[0]
for point in pointsGeoms[1:]:
pointsUnion = pointsUnion.union(point)
pointsInBuffer=busBuf.intersect(pointsUnion, 1)
intersectedPoints = pointsInBuffer.pointCount
totalPopulation += intersectedPoints
# Add the tallied data to the spreadsheet
data = lineName, stopID, totalPopulation
print 'data written', data
createCSV(data, csvName)
#Start the spreadsheet to see the results
os.startfile(csvName)

import arcpy, os
from common.useful import nonIntersect
from common.useful import generatePoints
from common.useful import formatSQLMultiple
from common.useful import nonIntersectcreateCSV                              
--------------------------------------------------------------------------------------
def generateXLS(indatas, sheetName, fileName):
import xlwt
workbook = xlwt.Workbook()
sheet = workbook.add_sheet(sheetName)
for YCOUNTER, data in enumerate(indatas):
for XCOUNTER, value in enumerate(data):
sheet.write(YCOUNTER, XCOUNTER, value)
workbook.save(fileName)
--------------------------------------------------------------------------------------
import arcpy, os
from common.useful import nonIntersect, generatePoints, generateXLS
arcpy.env.overwriteOutput = True
busStops = r'C:\Projects\PacktDB.gdb\SanFrancisco\Bus_Stops'
parks = r'C:\Projects\PacktDB.gdb\SanFrancisco\RPD_Parks'
censusBlocks = r'C:\Projects\PacktDB.gdb\SanFrancisco\CensusBlocks2010'
xlsName = r'C:\Projects\Output\Chapter10Analysis.xls'
headers = 'Line Name','Stop ID', 'Total Population Served'
indatas = [headers]
arcpy.MakeFeatureLayer_management(censusBlocks,'census_lyr')parkGeoms =
arcpy.CopyFeatures_management(parks,arcpy.Geometry())
parkUnion = parkGeoms[0]
for park in parkGeoms[1:]:
parkUnion = parkUnion.union(park)
sql = "NAME = '71 IB' AND BUS_SIGNAG = 'Ferry Plaza'"
with arcpy.da.SearchCursor(busStops, ['NAME','STOPID',
'SHAPE@'],sql) as cursor:
for row in cursor:
lineName = row[0]
stopID = row[1]
stop = row[2]
busBuf = stop.buffer(400)
arcpy.SelectLayerByLocation_management("census_lyr","intersect",busBuf,'','
NEW_SELECTION')
totalPopulation = 0
with arcpy.da.SearchCursor("census_lyr", ['SHAPE@','POP10',
'BLOCKID10']) as ncursor:
for nrow in ncursor:
block = nrow[0]
checkedBlock = nonIntersect(block, parkUnion)
blockName = nrow[2]
population = nrow[1]
if population != 0:
points =
generatePoints("PopPoints",population,checkedBlock)
pointsGeoms = arcpy.CopyFeatures_management(points,arcpy.Geometry())
pointsUnion = pointsGeoms[0]
for point in pointsGeoms[1:]:
pointsUnion = pointsUnion.union(point)
pointsInBuffer = busBuf.intersect(pointsUnion,1)
intersectedPoints = pointsInBuffer.pointCount
totalPopulation += intersectedPoints
data = lineName, stopID, totalPopulation
indatas.append(data)
generateXLS(indatas, "Results", xlsName)
os.startfile(xlsName)                                       
--------------------------------------------------------------------------------------
import arcpy
arcpy.CheckOutExtension("Network")
busStops = r'C:\Projects\PacktDB.gdb\Chapter11Results\BusStops'
networkDataset = r'C:\Projects\PacktDB.gdb\Chapter11Results\street_network'
networkLayer = "streetRoute"
impedance = "Length"
routeFile = "C:\Projects\Layer\{0}.lyr".format(networkLayer)
arcpy.MakeRouteLayer_na(networkDataset,
networkLayer, impedance)
print 'layer created'
sql = "NAME = '71 IB' AND BUS_SIGNAG = 'Ferry Plaza'"
with arcpy.da.SearchCursor(busStops,['SHAPE@', 'STOPID'],sql) as cursor:
for row in cursor:
stopShape = row[0]
print row[1]
arcpy.AddLocations_na(networkLayer,'Stops',stopShape, "", "")
arcpy.Solve_na(networkLayer,"SKIP")
arcpy.SaveToLayerFile_management(networkLayer,routeLayerFile,"RELATIVE")
print 'finished'
--------------------------------------------------------------------------------------
import arcpy
arcpy.CheckOutExtension("Network")
busStops = r'C:\Projects\SanFrancisco.gdb\SanFrancisco\Bus_Stops
networkDataset =
r'C:\Projects\SanFrancisco.gdb\Chapter11Results\street_network'
networkLayer = "streetRoute"
impedance = "Length"
routeLayerFile = "C:\Projects\Layer\
{0}_2.lyr".format(networkLayer)arcpy.na.MakeRouteLayer(networkDataset,
networkLayer,impedance)
print 'layer created'
sql = "NAME = '71 IB' AND BUS_SIGNAG = 'Ferry Plaza'"
with arcpy.da.SearchCursor(busStops,['SHAPE@','STOPID'],sql) as cursor:
for row in cursor:
stopShape = row[0]
print row[1]
arcpy.na.AddLocations(networkLayer,'Stops', stopShape, "", "")
arcpy.na.Solve(networkLayer,"SKIP")
arcpy.management.SaveToLayerFile(networkLayer,routeLayerFile,"RELATIVE")
print 'finished'
--------------------------------------------------------------------------------------
import arcpy
arcpy.CheckOutExtension("Spatial")
busStops = r'C:\Projects\PacktDB.gdb\SanFrancisco\Bus_Stops'
sanFranciscoHoods =
r'C:\Projects\PacktDB.gdb\SanFrancisco\SFFind_Neighborhoods'
sfElevation = r'C:\Projects\PacktDB.gdb\sf_elevation'
somaGeometry = []
sql = "name = 'South of Market'"
with arcpy.da.SearchCursor(sanFranciscoHoods,['SHAPE@XY'],sql,None, True)
as cursor:
for row in cursor:
X = row[0][0]
Y = row[0][1]
somaGeometry.append(arcpy.Point(X,Y))
somaElev = arcpy.sa.ExtractByPolygon(sfElevation,somaGeometry,"INSIDE")
somaOutPath = sfElevation.replace('sf_elevation','SOMA_elev')
somaElev.save(somaOutPath)
print 'extraction finished'
--------------------------------------------------------------------------------------
somaOutPath = sfElevation.replace('sf_elevation','SOMA_elev')
outTimes = arcpy.sa.Times(somaOutPath, 3.28084)
somaFeetOutPath = sfElevation.replace('sf_elevation','SOMA_feet')
outTimes.save(somaFeetOutPath)
--------------------------------------------------------------------------------------
with arcpy.da.SearchCursor(sanFranciscoHoods,['SHAPE@'],sql) as cursor:
for row in cursor:
somaPoly = row[0]
arcpy.MakeFeatureLayer_management(busStops, 'soma_stops')
arcpy.SelectLayerByLocation_management("soma_stops", "INTERSECT",somaPoly)
outStops = r'C:\Projects\PacktDB.gdb\Chapter11Results\SoMaStops'
arcpy.sa.ExtractValuesToPoints("soma_stops",
somaOutFeet,outStops,"INT
--------------------------------------------------------------------------------------
import arcpy
arcpy.CheckOutExtension("Spatial")
arcpy.env.overwriteOutput = True
busStops = r'C:\Projects\PacktDB.gdb\SanFrancisco\Bus_Stops'
sanFranciscoHoods =
r'C:\Projects\SanFrancisco.gdb\SanFrancisco\SFFind_Neighborhoods'
sfElevation = r'C:\Projects\SanFrancisco.gdb\sf_elevation'
somaGeometry = []
sql = "name = 'South of Market'"
with arcpy.da.SearchCursor(sanFranciscoHoods,['SHAPE@XY'],sql,None, True)
as cursor:
for row in cursor:
somaGeometry.append(arcpy.Point(row[0][0],row[0][1]))
somaElev = arcpy.sa.ExtractByPolygon(sfElevation, somaGeometry,"INSIDE")
somaOutput = sfElevation.replace('sf_elevation','SOMA_elev')
somaElev.save(somaOutput)
print 'extraction finished'
somaOutput = sfElevation.replace('sf_elevation','SOMA_elev')
outTimes = arcpy.sa.Times(somaOutput, 3.28084)
somaOutFeet = sfElevation.replace('sf_elevation','SOMA_feet')
outTimes.save(somaOutFeet)
print 'conversion complete'
with arcpy.da.SearchCursor(sanFranciscoHoods,['SHAPE@'],sql) as cursor:
for row in cursor:
somaPoly = row[0]
arcpy.MakeFeatureLayer_management(busStops, 'soma_stops')
arcpy.SelectLayerByLocation_management("soma_stops", "INTERSECT",somaPoly)
outStops = r'C:\Projects\SanFrancisco.gdb\Chapter11Results\SoMaStops'
arcpy.sa.ExtractValuesToPoints("soma_stops",
somaOutFeet,outStops,"INTERPOLATE","VALUE_ONLY")
print 'points generated'
--------------------------------------------------------------------------------------
def returnfieldnames(fc):
import arcpy
fieldnames = [f.name for f in arcpy.ListFields(fc)]
del arcpy
return fieldnames
def returnfieldalias(fc):
import arcpy
fieldalias = [f.aliasName for f in arcpy.ListFields(fc)]
del arcpy
return fieldalias
def returnfieldbasename(fc):
import arcpy
fieldtypes = [f.baseName for f in arcpy.ListFields(fc)]
del arcpy
return fieldtypes
--------------------------------------------------------------------------------------
def returnfieldtypes(fc):
import arcpy
fieldtypes = [f.type for f in arcpy.ListFields(fc)]
del arcpy
return fieldtypes
def returnfieldlength(fc):
import arcpy
fieldlengths = [f.length for f in arcpy.ListFields(fc)]
del arcpy
return fieldlengths
def returnfieldprecision(fc):
import arcpy
fieldprecise = [f.precision for f in arcpy.ListFields(fc)]
del arcpy
return fieldprecise
def returnfieldscale(fc):
import arcpy
fieldscales = [f.scale for f in arcpy.ListFields(fc)]
del arcpy
return fieldscales                               

--------------------------------------------------------------------------------------
def returnfieldsubtypes(fc):
import arcpy
fieldsubdic = {}
subtypes = arcpy.da.ListSubtypes(fc)
for stcode, stdict in subtypes.iteritems():
for stkey in stdict.iterkeys():
if stkey == 'FieldValues':
fields = stdict[stkey]
for field, fieldvals in fields.iteritems():
sub = fieldvals[0]
desc = fieldvals[1]
fieldsubdic[field] = sub, desc
del arcpy
return fieldsubdic
--------------------------------------------------------------------------------------
def returnprojectioncode(fc):
import arcpy
spatial_reference = arcpy.Describe(fc).spatialReference
proj_code = spatial_reference.projectionCode
del arcpy
return proj_code
def returnprojectionname(fc):
import arcpy
spatial_reference = arcpy.Describe(fc).spatialReference
proj_name = spatial_reference.name
del arcpy
return proj_name

--------------------------------------------------------------------------------------
spatialReference = arcpy.SpatialReference(2227)
fileGDB = r"{0}\{1}".format(folderPath,gdbName)
featureDataset = "Chapter12Results"
arcpy.CreateFeatureDataset_management(fileGDB, featureDataset,
spatialReference)
--------------------------------------------------------------------------------------
featureClass = "BufferArea"
geometryType = "POLYGON"
featurePath = r"{0}\{1}".format(fileGDB,featureDataset)
arcpy.CreateFeatureclass_management(featurePath, featureClass,
geometryType)

--------------------------------------------------------------------------------------
fieldName = "STOPID"
fieldAlias = "Bus Stop Identifier"
fieldType = "LONG"
fieldPrecision = 9
featureClassPath = r"{0}\{1}".format(featurePath,featureClass)
arcpy.AddField_management(featureClassPath, fieldName,fieldType,
fieldPrecision,
"", "", fieldAlias)
--------------------------------------------------------------------------------------
fieldName2 = "AVEPOP"
fieldAlias2 = "Average Census Population"
fieldType2 = "FLOAT"
featureClassPath = r"{0}\{1}".format(featurePath,featureClass)
arcpy.AddField_management(featureClassPath, fieldName2, fieldType2, "", "",
"", fieldAlias2)
--------------------------------------------------------------------------------------
arcpy.AddMessage("Beginning Analysis")
insertCursor = arcpy.da.InsertCursor(featureClassPath,['SHAPE@',fieldName,
fieldName2])
arcpy.MakeFeatureLayer_management(censusBlocks2010,"census_lyr")
with arcpy.da.SearchCursor(busStops, ['SHAPE@', busStopField],sql) as
cursor:
for row in cursor:
stop = row[0]
stopID = row[1]
busBuffer = stop.buffer(400)
arcpy.SelectLayerByLocation_management("census_lyr","intersect",busBuffer,'
','NEW_SELECTION')
censusShapes = []
censusPopList = []
with arcpy.da.SearchCursor("census_lyr",
['SHAPE@',censusBlockPopField]) as ncursor:
for nrow in ncursor:
censusShapes.append(nrow[0])
censusPopList.append(nrow[1])
censusUnion = censusShapes[0]
for block in censusShapes[1:]:
censusUnion = censusUnion.union(block)
censusPop = sum(censusPopList)/len(censusPopList)
finalData = (censusUnion,stopID, censusPopulation)
insertCursor.insertRow(finalData)
arcpy.AddMessage("Analysis Complete")
--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------



--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------


--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------


--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------


--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------


--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------



--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------


--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------


--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------


--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------


--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------



--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------


--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------


--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------


--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------


--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------



--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------


--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------


--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------


--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------


--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------



--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------


--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------


--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------


--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------


--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------



--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------


--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------


--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------


--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------


--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------



--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------


--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------


--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------


--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------


--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------



--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------


--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------


--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------


--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------


--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------



--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------


--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------


--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------


--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------


--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------



--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------


--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------


--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------


--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------


--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------



--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------


--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------


--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------


--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------


--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------



--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------


--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------


--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------


--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------


--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------



--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------


--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------


--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------


--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------


--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------



--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------


--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------


--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------


--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------


--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------



--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------


--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------


--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------


--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------


--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------



--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------


--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------


--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------


--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------


--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------



--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------


--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------


--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------


--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------


--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------



--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------


--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------


--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------


--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------


--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------



--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------


--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------


--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------


--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------


--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------



--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------


--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------


--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------


--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------


--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------



--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------


--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------


--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------


--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------


--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------



--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------


--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------


--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------


--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------


--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------



--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------


--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------


--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------


--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------


--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------



--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------


--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------


--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------


--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------


--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------



--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------


--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------


--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------


--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------


--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------



--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------


--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------


--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------


--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------


--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------



--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------


--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------


--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------


--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------


--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------



--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------


--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------


--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------


--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------


--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------



--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------


--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------


--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------


--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------


--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------



--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------


--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------


--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------


--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------


--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------



--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------


--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------


--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------


--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------


--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------


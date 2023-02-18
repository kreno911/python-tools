####! Project was from Rob and not used as the arcgis link does
# not work
#
# elevation2agl.py
#
# Purpose: Converts WGS_1984 MSL to absolute altitude (AGL)
#
# Notes:
#   EPQS grid resolution of the ground is 10 meters
#   GPS accuracy is typically within 5 meters
#   A better absolute altitude is gathered from a radio altimeter.
#
# Example usage:
#    python elevation2agl.py
#
# References:
# view-source:http://tagis.dep.wv.gov/convert/
# http://tagis.dep.wv.gov/arcgis/rest/services/Utilities/Geometry/GeometryServer/project
# https://developers.arcgis.com/javascript/3/jsapi/geometryservice-amd.html
# Projected Coordinate Systems https://developers.arcgis.com/javascript/3/jshelp/pcs.html
#
# https://tasks.arcgisonline.com/arcgis/rest/services/Geometry/GeometryServer/
# https://tasks.arcgisonline.com/arcgis/rest/services/Geometry/GeometryServer/project?inSR=4326&outSR=104223&geometries=%7B%22geometryType%22%3A%22esriGeometryPoint%22%2C%22geometries%22%3A%5B%7B%22x%22%3A-117%2C%22y%22%3A34%7D%5D%7D&transformation=&transformForward=true&f=json
# Input Spatial Reference:    4326 (GCS_WGS_1984)
# Output Spatial Reference: 104223 (GCS_NAD_1983_CORS96)
# Geometries: {"geometryType":"esriGeometryPoint","geometries":[{"x":-117,"y":34}]}
#
# "Without digging into the details, the datum realizations (such as 104223 vs. 4269) are not mathematically identical,
# but for almost any real-world purpose they are so close it doesn't matter. What does matter is that the grid point
# spacing of the 1/3 arc-second data is about 10 meters, and this relatively low resolution elevation interpolation
# -- and other uncertainties inherent in the capture of these data -- overcomes the differences in the datum math models
# by at least two to three orders of magnitude.  See FAQ https://www2.usgs.gov/faq/categories/9865/3624 for more
# discussion on elevation accuracy of the EPQS"..."If you are attempting to improve the positional accuracy of the data,
# then yes, this conversion is unnecessary. Changes in positions will be small relative to the point spacing, and change
# in actual overall accuracy will be insignificant. But it doesn't do any harm, either, and sometimes conversions like
# this are desirable for other reasons...achieving consistency in metadata, or making data friendlier to particular
# software processes, for example." -- USGS TNM Service Desk
#
# ########################################################################################################################
import requests
import json

#######################
# USER INPUT (WGS 1984)
######################
referenceElevation = 1660
msg84_lon = str(-74.5659708)
msg84_lat = str(39.4505594)

#######################################################################################
# Convert from WGS84 to North American Datum 1983 (NAD83) using arcgis geometry service
# (REF: https://nationalmap.gov/epqs/)
#######################################################################################
INPUT_DATUM  = "GCS_WGS_1984:4326"
TARGET_DATUM = "GCS_NAD_1983_CORS96:104223"
payload = {'inSR': INPUT_DATUM.split(":")[1],
                          'outSR': TARGET_DATUM.split(":")[1],
                          'geometries': json.dumps({'geometryType': 'esriGeometryPoint', 'geometries': [{'x':msg84_lon,'y': msg84_lat }]}),
                          'transformation': '',
                          'transformForward': 'true',
                          'f': 'json'}
r = requests.put('https://tasks.arcgisonline.com/arcgis/rest/services/Geometry/GeometryServer/project',
                  params=payload)
print(r.status_code)
# We get 403 - permission error but the page itself needs to be figured out
data = json.loads (r.text)

for rows in data["geometries"]:
    nad83_lon = str(rows['x'])
    nad83_lat = str(rows['y'])

###############
# DETERMINE AGL
###############

# Ground level altitude/elevation above mean sea level
# e.g. http://nationalmap.gov/epqs/pqs.php?x=-74.5659708&y=39.4505594&units=Feet&output=xml
line = requests.get('http://nationalmap.gov/epqs/pqs.php?x=' + nad83_lon + '&y=' + nad83_lat + '&units=Feet&output=xml')
if line == -1000000:
    exit ("service unable to find data at the requested point")
groundLevelAltitude = (str(line.content).split('Elevation>'))[1].split('<')[0]

# Rotorcraft's absolute altitude above ground level (AGL)
absoluteAltitude = referenceElevation - float(groundLevelAltitude)

###################
# PRINT CALCULATION
###################
print("\nDetermining AGL (elevation2agl.py)...")

print("\nExample Inputs...")
print(" WGS_1984 location                              : " + msg84_lon +"," + msg84_lat)
print(" Provided reference elevation (WGS_1984 MSL)    : " + str(referenceElevation) + " feet above MSL")

print("\nGround level calculations...")
print("  NAD_1983 location (used w/ ground level query): " + nad83_lon +"," + nad83_lat)
print("  Gathered ground level altitude                : " + str(groundLevelAltitude) + " feet above MSL")

print("\nAGL Calculations...")
print("  Absolute altitude - above ground level (AGL)  : " + str(absoluteAltitude) + " feet above ground")


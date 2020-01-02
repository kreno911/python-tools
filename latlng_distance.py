#!/usr/bin/python

import sys, math

# Given to lat/long points, find the distance
# This script will take 4 numbers and unit (M/K/N):
#   ./latlng_distance.py 32.9697 -96.80322 29.46786 -98.53506 M
#
# Where: 'M' is statute miles (default)  ##! IS THIS CORRECT
#        'K' is kilometers
#        'N' is nautical miles 

# Miscellaneous 
pi = 3.14159
def deg2rad(deg):
    return deg * pi / 180.0
def rad2deg(rad):
    return rad * 180 / pi

# Calculate distance. All point values must be floats
def distance(lat1, lng1, lat2, lng2, unit):
    theta = lng1 - lng2
    dist = math.sin(deg2rad(lat1)) * math.sin(deg2rad(lat2)) + \
           math.cos(deg2rad(lat1)) * math.cos(deg2rad(lat2)) * \
           math.cos(deg2rad(theta))

    dist = math.acos(dist)
    dist = rad2deg(dist)   # Convert back to degrees
    ##! THIS DOES NOT LOOK RIGHT....NEED TO FIX!!!!
    dist = dist * 60 * 1.1515
    if (unit == "K"):
        dist = dist * 1.609344
    elif (unit == "N"):
        dist = dist * 0.8684

    return dist

if (len(sys.argv) < 5):
    print "Need at least 4 arguments(points), <lat> <long> <lat> <long> <unit>"
    print "    ./latlng_distance.py 32.9697 -96.80322 29.46786 -98.53506 M"
    print "    Unit default to M - meters. K-Kilometer, N-Nautical Miles"
    sys.exit(11)

unit = 'M'
pt1_lat = float(sys.argv[1])
pt1_lng = float(sys.argv[2])
pt2_lat = float(sys.argv[3])
pt2_lng = float(sys.argv[4])

if len(sys.argv) == 6:
    unit = sys.argv[5]

#print pt1_lat, pt1_lng, pt2_lat, pt2_lng, unit

print distance(pt1_lat, pt1_lng, pt2_lat, pt2_lng, unit)


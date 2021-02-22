#!/usr/bin/python

import sys

# Take a file with values like so:
#
# N Lat     W Lon
# 41-57-57.14     087-46-47.73
# 41-57-57.10     087-39-08.47
# ...
# and convert these to decimal.

def convertLatToDec(lat):
    direction = {'N':1, 'S':-1, 'E': 1, 'W':-1}
    lat_parts = lat.split('-')
    # Pick off last char which is the direction
    dir = lat_parts[2][-1]
    lat_parts[2] = lat_parts[2][:-1]  # This actually picks off last char

    return "%s" % str((int(lat_parts[0])+int(lat_parts[1])/60.0+int(float(lat_parts[2]))/3600.0) * direction[dir] )
    
def convertLongToDec(long):
    direction = {'N':1, 'S':-1, 'E': 1, 'W':-1}
    long_parts = long.split('-')
    ln_dir = long_parts[2][-1]
    long_parts[2] = long_parts[2][:-1]

    return "%s" % str((int(long_parts[0])+int(long_parts[1])/60.0+int(float(long_parts[2]))/3600.0) * direction[ln_dir])

if len(sys.argv) != 2:
    print "Please provide file."
    sys.exit(11)

data_file = sys.argv[1]
dataFile = open(data_file)

location = ""
for line in dataFile:
    if line.strip():
        if "ILS" in line:
            parts = line.split()
            location = "%s-%s" % (parts[2],parts[1])
        elif "Lat" in line:
            continue
        else:
            parts2 = line.split()
            lat = convertLatToDec(parts2[2]+"N")
            lon = convertLongToDec(parts2[3]+"W")
            print "%s,%s,%s,%s,%s" % (location,parts2[0],parts2[1],lat, lon)



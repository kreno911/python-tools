#!/usr/bin/python

import sys

# Convert latitude/longitude to the decimal format from the deg/min/sec
# format given in most situations
# Assumed format for lat/long:
#   51-52-16.648N, 176-40-26.743W
def convertLatToDec(lat):
    direction = {'N':1, 'S':-1, 'E': 1, 'W':-1}
    # Remove any ','
    lat_parts = lat.replace(",", "").split('-')
    # Pick off last char which is the direction
    currdir = lat_parts[2][-1]
    lat_parts[2] = lat_parts[2][:-1]  # This actually picks off last char
    #print("%s, [%s]" % (currdir, lat_parts))

    return "%s" % str((int(lat_parts[0])+int(lat_parts[1])/60.0+int(float(lat_parts[2]))/3600.0) * direction[currdir])

def convertLongToDec(long):
    direction = {'N':1, 'S':-1, 'E': 1, 'W':-1}
    long_parts = long.split('-')
    ln_dir = long_parts[2][-1]
    long_parts[2] = long_parts[2][:-1]

    return "%s" % str((int(long_parts[0])+int(long_parts[1])/60.0+int(float(long_parts[2]))/3600.0) * direction[ln_dir])

# cmd counts as an arg
if (len(sys.argv) != 3):
    print ("todec <lat>,<long> [lat|long value in deg/min/sec (51-52-16.648N)]")
    print ("    example: ./latlong_todec.py 51-52-16.648N 176-40-26.743W")
    sys.exit(11)

arg1 = sys.argv[1]
arg2 = sys.argv[2]
#print ("%s, %s" % (arg1,arg2))
print ("(%s,%s)" % (convertLatToDec(arg1), convertLongToDec(arg2)))


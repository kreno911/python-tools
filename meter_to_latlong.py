#!/usr/bin/python

################################################################################
#
# Unit: meter_to_latlong.py
#
# Overview:
#   Script to convert a given point in meters along with a given center point
#   in lat/long (decimal) to their equivalent lat/long in decimal relative to
#   to the center (origin).
#
# Usage: ./meter_to_latlong.py -p "-1606.89,868.83" -o "33.641701553,-84.421684342"
#
################################################################################

import getopt, sys, math

def usage():
    print ("Usage: ./meter_to_latlong.py -p \"mmmm.mm,mmmm,mm\" -o \"mmmm.mm,mmmm,mm\"")
    sys.exit(9)

##
# Take the point in meters and calculate the lat/long for
# that point relative to value from main_map.xml.
# This algorithm was adapted from:
#   http://stackoverflow.com/questions/7477003/calculating-new-longtitude-latitude-from-old-n-meters
##
def convertToLatLong(dx, dy):
    global ORIGIN
    lat, lon = ORIGIN
    r_earth = 6378.0
    pi = 3.14159
    new_latitude = float(lat) + ((float(dy)/1000) / r_earth) * (180.0 / pi);
    new_longitude = float(lon) +  ((float(dx)/1000) / r_earth) * (180.0 / pi)  \
                        / math.cos(float(lat) * pi / 180.0);

    return (new_longitude,new_latitude)

def main(argv):
    global ORIGIN
    # define points
    source_pt_m = ()      # In meters
    ORIGIN = ()           # lat.long decimal
    # Lets make use of the getopt lib
    try:
        # This script requires 4 total arguments, 2 switches, each with arg
        opts, args = getopt.getopt(argv, "o:p:")
        # Make sure we have proper args
        if len(argv) < 4:
            print ("Not enough arguments.")
            usage()
        for opt, arg in opts:
            if opt in ("-p"):
                source_pt_m = arg.split(",")
                print ("Source is: %s, %s" % (source_pt_m[0], source_pt_m[1]))
            if opt in ("-o"):
                ORIGIN = arg.split(",")
                print ("Origin is: %s, %s" % (ORIGIN[0], ORIGIN[1]))
    except getopt.GetoptError as e:
        print (e.msg, "  ", usage())
        sys.exit(11)

    newPoint = convertToLatLong(source_pt_m[0], source_pt_m[1])
    print ("Point: %s,%s with center %s,%s is:\n(%s,%s)" % \
            (source_pt_m[0], source_pt_m[1],ORIGIN[0], ORIGIN[1],\
             newPoint[0], newPoint[1]))

# MAIN
if __name__ == "__main__":
    main(sys.argv[1:])

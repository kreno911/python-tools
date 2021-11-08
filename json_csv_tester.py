import json, csv
#import pandas as pd
from datetime import datetime
import time

#####
#   Test out different JSON and CSV formats which we need to convert.
#
#####

def convert_date(d_str):
    timest = time.localtime(int(d_str)/1000)
    #return datetime.fromtimestamp(timest).strftime('%Y%m%dT%H%M%S')
    return time.strftime('%Y%m%dT%H%M%S', timest)

# proxmity-data-1a.csv cotnains basic FlID/lat/long/time strings from an athena query
# in AWS but could be from any source.
# "FLIGHT","LAT","LONG","TIME"     ##! First line is header
# "N653JS","36.22649431228638","-76.95800542831421","1587572415336"
# "N653JS","36.22649431228638","-76.95800542831421","1587572415336"
# ,"37.623560428619385","-122.37565755844116","1587572415195"
#
# Here we will separate each flight into its points and create a file for each.
# Each file should contain a proximity string for that flight.
# [{"lat":39.852478,"lon":-85.481056,"timeStr":"20190202T024001","prodId":"VIL"},
#       {"lat":39.752478,"lon":-85.581056,"timeStr":"20190202T024001","prodId":"VIL"}]
file_to_process = "test_data/proxmity-data-1b.csv"
print("Processing %s" % file_to_process)
csvData = csv.reader(open(file_to_process))
flights = {}
json_string = "{\"lat\":%.15f,\"lon\":%.15f,\"timeStr\":\"%s\",\"prodId\":\"VIL\"},"
prox_string = "[%s]"
cc = 0
for row in csvData:
    # As seen above some rows have a blank flight id, skip
    if row[0] == "":
        continue
    if not cc == 0:
        #print(row)
        flight_id = row[0]
        # timeStr argument has to be in the format: yyyyMMddTHHmmss
        jline = json_string % (float(row[1]),float(row[2]),convert_date(row[3]))
        if flight_id not in flights:
            flights[flight_id] = []  # Initialize empty list
        flights[flight_id].append(jline)
    cc += 1
    # if cc > 5:
    #     break

# Save each to file
fname = "FL_%s.json"
for key in flights:
    # Generate the full proximity string for flight
    mid_string = ""
    for st in flights.get(key):
        mid_string += st
    print("%s: %s" % (key, prox_string % mid_string[:-1]))
    file_name = fname % key
    with open("/temp/output/" + file_name, "w") as outfile:
        outfile.write(prox_string % mid_string[:-1])

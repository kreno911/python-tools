#####
# This file will take the JSON data from token-secure.py and separate all data into
# yearly files like 2018-data.json, 2019-data.json...
#
# The data comes from the ARGIS server on local network.
#   See outout-temp.out to see the input file and see eon_data_YYYY.json for output.
#####

import json, sys
from datetime import datetime

'''
dumps()	encoding to JSON objects
dump()	encoded string writing on file
loads()	Decode the JSON string
load()	Decode while JSON file read
'''

# General flow
#   1) Read file in
#   2) Pick out stanzas by year
#   3) Store data into yearly files

'''
Sample line from outout-temp.out
{"OBJECTID": 32625, "Region": "ACE", "ReportingLevel": 2, "DisplayUrl": "URL:// test.com/eon/app/Lists/DRA/EditFormChangedToNewform.aspx?ID=32625", "Summary": "STL: EGF3692, E145, GRR-DFW, DECLARED AN EMERGENCY AND DIVERTED TO STL, DUE TO MEDICAL EMERGENCY, A SICK PASSENGER. ACFT LANDED AT 2221Z WITHOUT INCIDENT. 3/4 2221Z", "EventDateTimeUtc": 1236205260000, "EventDateTimeLocal": 1236183660000, "AircraftType": "E145", "ReportingFacility": "ZKC/KIM", "Location": "STL", "EventType": "Medical Emergency", "CreatedDateTime": 1236208884000, "ModifiedDateTime": 1236208884000, "Longitude": -90.37002889, "Latitude": 38.74869722, "EventUtcOffset": null, "EventTimeZoneCity": null, "Tags": null, "Airline": null, "CallSign": null, "NNumber": null, "DepartureAirport": null, "ArrivalAirport": null, "DivertedTo": null, "Pob": null, "InjuryType": null, "InjuriesMinor": null, "InjuriesSerious": null, "Fatalities": null, "DamageType": null, "Uninjured": null, "UnknownInjured": null, "PobUnknown": null, "LastUpdateDate": null, "City": null, "State": null, "Title": null, "Airport": null}
...
...
'''

start_time = datetime.now()
print("Start...(%s)" % datetime.now())

#json_file = "/aprojects/python-tools/outout-prod-full.out"  # Full 450Mb file
json_file = "/TEST_DATA/OUTPUT/outout-temp.out"
# Empty dictionary for our yearly lists
data_dict = {}
jline = ""
file_name_format = "eon_data_%s.json" # %s = year (eon_data_2020.json)
print("Opening: %s" % json_file)
with open(json_file, 'r') as in_file:
    try:
        count = 0
        json_data = json.load(in_file)
        for jline in json_data:
            print("Line: %s" % jline)
            #print("Event time: %s" % jjline['EventDateTimeUtc'])
            event_time = int(jline['EventDateTimeUtc'])
            sys.exit(11)
            # Some time values had (-) times, just skip them
            if event_time < 0:
                print("Bad value: %d" % event_time)
                continue
            thedate = datetime.utcfromtimestamp(event_time/1000.0)
            year = thedate.strftime('%Y')
            # Check if a dictionary of this year exists, if so, append to its list
            # else, create new list and add to this yearly key
            if year not in data_dict:
                print("Adding: %s" % year)
                data_dict[year] = []  # empty list to hold data
            # Add data line
            data_dict[year].append(jjline)

            count += 1
    except Exception as err:
        exception_type, exception_object, exception_traceback = sys.exc_info()
        # tb_lineno - the line in this file where the error occurred
        print ("Error: %s, %s, [%d]" % (str(err), json.dumps(jline), exception_traceback.tb_lineno))

# data2017 = data_dict["2017"]
# for ddata in data2017:
#     print("Line: %s" % ddata)

# Write each year out to a file
for year in data_dict:
    thefile = file_name_format % year
    print("Wrting out %s" % year)
    with open(thefile, 'w') as wr_file:
        for jline in data_dict[year]:
            wr_file.write(json.dumps(jline) + '\n')

print("End...(%s-%s (%d))" % (start_time, datetime.now(), count))
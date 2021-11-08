# Test out secure connections like those that use a certificate
# Test out verify SSL flag

# This particular test file goes out to the FAA GIS server to get its data

'''
The following will list object in the S3 prefix:
    s3 = boto3.client("s3", region_name=os.environ['region'])

    #for p in s3.list_objects(Bucket=os.environ['BUCKET'], Prefix=os.environ['EON_DATA_FILE'])['Contents']:
    for key in s3.list_objects(Bucket=os.environ['BUCKET'], Prefix='eon/safety/raw/json/')['Contents']:
        print(key['Key'])
eon/safety/raw/json/
eon/safety/raw/json/eon_data.json
eon/safety/raw/json/response.json
# Note it also lists the top level prefix...
'''
import json, sys
import requests
from datetime import datetime
import ssl
# Latest urllib for py3
from urllib import request, parse
import csv

# Disable the InsecureRequestWarning with verify=false
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

user = ""

passw = ""
use_prod = False
# Only grab args, not script name
args = list(sys.argv[1:])
for v in range(1, len(args)+1):
    if sys.argv[v] == "--user":
        user = sys.argv[v+1]
    if sys.argv[v] == "--pass":
        passw = sys.argv[v+1]
    if sys.argv[v] == "--prod":
        use_prod = True
# PROD
prod_token_url = "https://mapping.eon.faa.gov/gis/sharing/rest/generateToken"
prod_data_url = "https://gis.eon.faa.gov/arcgis/rest/services/EON/DRAs/MapServer/0"
# DEV
token_url = "https://gis-dev.eon.faa.gov/gis/sharing/rest/generateToken"
data_url = "https://gis-dev.eon.faa.gov/arcgis/rest/services/EON/DRAs/MapServer/0"

# Set prod if we want production data
if use_prod:
    print("Using PROD...")
    token_url = prod_token_url
    data_url = prod_data_url

def get_exceededTransferLimit_flag(eon_data):
    limit_reached = False  # False if not present
    if 'exceededTransferLimit' in eon_data:
        limit_reached = eon_data['exceededTransferLimit']
    return limit_reached

# Exit the system and print error if encountered
def error_check(a_response):
    if a_response.get("error"):
        code = a_response["error"]["code"]
        print("%d, message: %s" % (code, a_response["error"]["message"]))
        sys.exit(11)

# This is the original and should not be modified
def get_data_with_requests(token_url, data_url):
    # Changed from client to referer to get past invalid token error
    # data = {'username': '%s' % user, 'password': '%s' % passw,
    #         'client': 'requestip', 'expiration': '60', 'f': 'pjson'}
    data_r = {'username': '%s' % user, 'password': '%s' % passw,
              'referer': 'localhost', 'expiration': '60', 'f': 'pjson'}
    # Setting verify to False will disable cert checking
    response = requests.post(token_url, data=data_r, verify=False)
    tokens = json.loads(response.text)
    the_token = tokens['token']

    #print("Token: %s" % the_token)

    # Now try to use it
    headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer %s' % the_token}
    ###! %3D = '=', %3E = '>', %3C = '<', %20 = space
    data_count_url = "%s/query?where=1%%3D1&f=pjson&outFields=*&returnCountOnly=true" % data_url
    data_all_url = "%s/query?where=1%3D1&f=pjson&outFields=*" % data_url
    #data_all_url_one_day = "%s/query?where=EventDateTimeUtc %%3E CURRENT_TIMESTAMP - INTERVAL '1' DAY&f=pjson&outFields=Region,CreatedDateTime,EventDateTimeUtc,EventType,Summary" % data_url

    # Append: resultRecordCount=3&resultOffset=1  - to only retrieve 3 results and start at #2 (offset of 1)
    # resultRecordCount will only be as high as maxRecordCount (currently 3000)
    # data_all_url = "%s/query?where=1%%3D1&f=pjson&outFields=*&resultRecordCount=5000" % data_url

    ## Region is AAL only
    # query = "where=Region%3D'AAL'&f=pjson&outFields=Region,CreatedDateTime,EventDateTimeUtc,EventType,Summary"
    # Last days data
    # query = "where=EventDateTimeUtc %3E CURRENT_TIMESTAMP - INTERVAL '1' DAY&f=pjson&outFields=Region,CreatedDateTime,EventDateTimeUtc,EventType,Summary"

    print(data_all_url)
    response = requests.post(data_all_url, headers=headers, verify=False)
    # print("Response: %s" % response.text)
    # ret = response.status_code
    # print(ret)

    # Return data
    return json.loads(response.text)
# end get_data_with_requests - original

def get_data_with_requests_paging(token_url, data_url, offset):
    data_r = {'username': '%s' % user, 'password': '%s' % passw,
              'referer': 'localhost', 'expiration': '60', 'f': 'pjson'}
    # Setting verify to False will disable cert checking
    response = requests.post(token_url, data=data_r, verify=False)
    tokens = json.loads(response.text)
    the_token = tokens['token']
    headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer %s' % the_token}

    # Append: resultRecordCount=3&resultOffset=1  - to only retrieve 3 results and start at #2 (offset of 1)
    # resultRecordCount will only be as high as maxRecordCount (currently 3000)
    data_all_url = "%s/query?where=1%%3D1&f=pjson&outFields=*&resultRecordCount=5000&resultOffset=%d" \
                                        % (data_url,offset)
    # Test for time range
    # 1514764800000 = 1/1/2018 12 AM (UTC)
    # 1546300800000 = 1/1/2019 12 AM (UTC)
    # 1577836800000 = 1/1/2020 12 AM (UTC)
    # 1614000000000 = 2/22/2021
    # null for either value goes to infinity in that direction (b4 2009 - null,1230768000000)
    # This one is all > 1/1/2018
    data_all_url = "%s/query?where=1%%3D1&f=pjson&outFields=*&resultRecordCount=5000&resultOffset=%d&time=1614000000000,null" \
                                        % (data_url,offset)

    ## (951 count - STL)
    # data_all_url = "%s/query?where=Location%%3D'STL'&f=pjson&outFields=*&resultRecordCount=3000&resultOffset=%d" \
    #             % (data_url, offset)
    ## Get ALL
    # data_all_url = "%s/query?where=1%%3D1&f=pjson&outFields=OBJECTID,Region,CreatedDateTime,EventDateTimeUtc&resultRecordCount=3000&resultOffset=%d" \
    #                % (data_url, offset)
    # data_all_url = "%s/query?where=EventDateTimeUtc %%3E CURRENT_TIMESTAMP - INTERVAL '1' DAY&f=pjson&outFields=*&resultRecordCount=5000&resultOffset=%d" \
    #                 % (data_url, offset)

    print("get_data_with_requests_paging: %s" % data_all_url)
    response = requests.post(data_all_url, headers=headers, verify=False)
    eon_data = json.loads(response.text)

    # Write to file
    # with open("outout-raw.json", 'w') as wr_file:
    #     wr_file.write(response.text)
    return eon_data

# Currently maximun # values we can retrieve is 3000, this is the offset we
# use for each request when paging
MAX_OFFSET = 3000
def get_eon_data(token_url, data_url):
    all_the_data = []  # list
    # First query starts at 0 and increments MAX_OFFSET
    current_offset = 0
    while current_offset == 0 or xfer_limit_reached:
        eon_data = get_data_with_requests_paging(token_url, data_url, current_offset)  # Start at 0
        # Check if we were successful
        error_check(eon_data)
        # Add data to list
        for feature in eon_data['features']:
            all_the_data.append(feature['attributes'])
        # Reset the flag, increment the offset and re-query next batch
        xfer_limit_reached = get_exceededTransferLimit_flag(eon_data)
        #print(" Was exceeded xfer limit reached: %s [%d]" % (xfer_limit_reached, current_offset))
        current_offset += MAX_OFFSET

    # count = 0
    # for value in all_the_data:
    #     count += 1
    #     if count > 50:
    #         break
    #     print("Value: %s" % value)
    # Write to file
    print("Writing to file:")
    # with open("outout-temp.json", 'w') as wr_file:
    #     for value in all_the_data:
    #         #print(json.dumps(value))
    #         wr_file.write(json.dumps(value) + '\n')
    print("Count = %d" % len(all_the_data))

    ##! DELETE WHEN DONE
    # Break into yearly files
    data_dict = {}
    for jline in all_the_data:
        #print(json.dumps(jline))
        event_time = int(jline['EventDateTimeUtc'])
        thedate = datetime.utcfromtimestamp(event_time / 1000.0)
        year = thedate.strftime('%Y')
        # Check if a dictionary of this year exists, if so, append to its list
        # else, create new list and add to this yearly key
        if year not in data_dict:
            print("Adding: %s" % year)
            data_dict[year] = []  # empty list to hold data
        # Add data line
        data_dict[year].append(jline)
    file_name_format = "eon_data_%s.json"
    for year in data_dict:
        thefile = file_name_format % year
        with open(thefile, "w") as outfile:
            for line in data_dict[year]:
                outfile.write(json.dumps(line) + '\n')
    print("Done")
    ##! DELETE

'''
If you get a response like: b'[-97,-97,-97,-97,-97]', this means its returning a byte string 
urllib.request.urlopen() returns a bytestream
'''
def get_data_with_urllib(some_url):
    print("Using urllib...", some_url)
    data = "[{\"lat\":39.911798099999999,\"lon\":-105.111249000000001,\"timeStr\":\"20170805T180931\",\"prodId\":\"VIL\"}," \
           "{\"lat\":39.911798099999999,\"lon\":-110.111249000000001,\"timeStr\":\"20170805T181131\",\"prodId\":\"VIL\"}]"
    req = request.Request(some_url, data.encode('utf-8'))
    req.add_header('Content-Type', 'application/json')
    response = request.urlopen(req)
    the_page = response.read().decode('utf-8')
    print("Response: %s" % the_page)

# Get a METAR file
def get_metar_file():
    metar_file = "https://tgftp.nws.noaa.gov/data/observations/metar/cycles/00Z.TXT"
    file_text = request.urlopen(metar_file).read()
    return file_text

#get_eon_data(token_url, data_url)
get_data_with_urllib("http://10.22.169.14:8090/eim/proximityList")

csv_string1 = "[-97,-97]"[1:-1]
csv_string2 = "[44,55,66,77]"[1:-1]
csv_list  = []
csv_list.extend(csv_string1.split(","))
csv_list.extend(csv_string2.split(","))
for row in csv_list:
    print(row)

'''
Saved code:
# When accessing/converting date
            #the_time = feature['attributes']['EventDateTimeUtc']
            # print in human format: 1612203900000 -> 2021-02-01 18:25:00
            #print("   ", datetime.utcfromtimestamp(the_time / 1000.0))
            # print(feature['attributes']['Region'])

'''
# SAMPLE DATA RETURN
'''
DEV
{
   "attributes": {
    "OBJECTID": 35304,
    "Region": "ASO",
    "ReportingLevel": 2,
    "DisplayUrl": "https://c3.eon.faa.gov/eon/app/Lists/DRA/EditFormChangedToNewform.aspx?ID=35304",
    "Summary": "FORT MYERS, FL (FMY): N4918H, C152, INBOUND TO FMY, REPORTED A ROUGH RUNNING ENGINE. LANDED WITHOUT INCIDENT. 4/17 1838Z",
    "EventDateTimeUtc": 1239993480000,
    "EventDateTimeLocal": 1239979080000,
    "AircraftType": "C152",
    "ReportingFacility": "FMY/BECKY/1850Z",
    "Location": "FORT MYERS, FL (FMY)",
    "EventType": "General Aviation Incident",
    "CreatedDateTime": 1239994489000,
    "ModifiedDateTime": 1240024468000,
    "Longitude": -81.86325,
    "Latitude": 26.58661111,
    "EventUtcOffset": null,
    "EventTimeZoneCity": null,
    "Tags": null,
    "Airline": null,
    "CallSign": null,
    "NNumber": null,
    "DepartureAirport": null,
    "ArrivalAirport": null,
    "DivertedTo": null,
    "Pob": null,
    "InjuryType": null,
    "InjuriesMinor": null,
    "InjuriesSerious": null,
    "Fatalities": null,
    "DamageType": null,
    "Uninjured": null,
    "UnknownInjured": null,
    "PobUnknown": null,
    "LastUpdateDate": null,
    "City": null,
    "State": null,
    "Title": null,
    "Airport": null
   },
   "geometry": {
    "x": -81.86322021484375,
    "y": 26.58673095703125
   }
  }
PROD (not updated with new fields yet)
{
   "attributes": {
    "OBJECTID": 32624,
    "Region": "ACE",
    "ReportingLevel": 2,
    "DisplayUrl": "https://c3.eon.faa.gov/eon/app/Lists/DRA/EditFormChangedToNewform.aspx?ID=32624",
    "Summary": "ICT: NWA1195, B757, DTW-LAS, DIVERTED ICT DUE TO A MEDICAL EMERGENCY SICK PASSENGER. ACFT LANDED AT 2306Z WITHOUT INCIDENT. 3/4 2306Z",
    "EventDateTimeUtc": 1236207960000,
    "EventDateTimeLocal": 1236186360000,
    "AircraftType": "B757",
    "ReportingFacility": "ICT ATCT/MC",
    "Location": "ICT",
    "EventType": "Medical Emergency",
    "CreatedDateTime": 1236208506000,
    "ModifiedDateTime": 1236208506000,
    "Longitude": -97.43305556,
    "Latitude": 37.649944439999999,
    "EventUtcOffset": null,
    "EventTimeZoneCity": null,
    "Tags": null
   },
   "geometry": {
    "x": -97.43310546875,
    "y": 37.64990234375
   }
'''

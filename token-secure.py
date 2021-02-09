# Test out secure connections like those that use a certificate
# Test out verify SSL flag

import json, sys
import requests
from datetime import datetime
import ssl
# Latest urllib for py3
from urllib import request
from urllib import parse

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
    token_url = prod_token_url
    data_url = prod_data_url

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

    print("Token: %s" % the_token)

    # Now try to use it
    headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer %s' % the_token}
    ###! %3D = '=', %3E = '>', %3C = '<', %20 = space
    data_count_url = "%s/query?where=1%%3D1&f=pjson&outFields=*&returnCountOnly=true" % data_url
    # data_all_url = "https://gis-dev.eon.faa.gov/arcgis/rest/services/EON/DRAs/MapServer/0/query?where=1%3D1&f=pjson&outFields=*"

    data_all_url = "%s/query?where=EventDateTimeUtc %%3E CURRENT_TIMESTAMP - INTERVAL '1' DAY&f=pjson&outFields=Region,CreatedDateTime,EventDateTimeUtc,EventType,Summary" % data_url
    ## Region is AAL only
    # query = "where=Region%3D'AAL'&f=pjson&outFields=Region,CreatedDateTime,EventDateTimeUtc,EventType,Summary"
    # Last days data
    # query = "where=EventDateTimeUtc %3E CURRENT_TIMESTAMP - INTERVAL '1' DAY&f=pjson&outFields=Region,CreatedDateTime,EventDateTimeUtc,EventType,Summary"

    print(data_all_url)
    response = requests.post(data_all_url, headers=headers, verify=False)
    # print("Response: %s" % response.text)
    # ret = response.status_code
    # print(ret)

    # Grab some data
    eon_data = json.loads(response.text)
    # Check if we were successful
    if eon_data.get("error"):
        code = eon_data["error"]["code"]
        print("%d, messge: %s" % (code, eon_data["error"]["message"]))
        sys.exit(11)

    # with open("outout.out", 'w') as wr_file:
    #     wr_file.write(response.text)
    the_size = len(eon_data['features'])
    count = 0
    for feature in eon_data['features']:
        count += 1
        if count > 5:
            break
        print(feature['attributes'])
        the_time = feature['attributes']['EventDateTimeUtc']
        # print in human format: 1612203900000 -> 2021-02-01 18:25:00
        print("   ", datetime.utcfromtimestamp(the_time / 1000.0))
        # print(feature['attributes']['Region'])
    print("Count = %d" % the_size)

def get_data_with_urllib(token_url, data_url):
    print("using urllib...", token_url)
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    data = {'username': '%s' % user, 'password': '%s' % passw,
            'client': 'requestip', 'expiration': '60', 'f': 'pjson'}
    # Must have the .encode("utf-8") or get "POST should be bytes" error
    response = request.urlopen(token_url, data=parse.urlencode(data).encode("utf-8"), context=ctx)
    tokens = json.loads(response.read())
    the_token = tokens['token']
    print("Token: %s" % the_token)

    headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer %s' % the_token}

# Get a METAR file
def get_metar_file():
    metar_file = "https://tgftp.nws.noaa.gov/data/observations/metar/cycles/00Z.TXT"
    file_text = request.urlopen(metar_file).read()
    return file_text

get_data_with_requests(token_url, data_url)
#get_data_with_urllib(token_url, data_url)

# SAMPLE DATA RETURN
'''
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
'''

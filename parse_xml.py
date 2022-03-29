import xml.etree.ElementTree as ET
import io

# Take the following XML and work with it

XML_STRING = str('<?xml version="1.0" encoding="UTF-8"?><PIREP xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"> <receipt_time>2021-12-22T11:05:00Z</receipt_time> <observation_time>2021-12-22T11:01:00Z</observation_time> <aircraft_ref>LSI517</aircraft_ref> <latitude>45.05</latitude> <longitude>-31.2833</longitude> <altitude_ft_msl>39000</altitude_ft_msl> <temp_c>-45</temp_c> <wind_dir_degrees>265</wind_dir_degrees> <wind_speed_kt>37</wind_speed_kt> <pirep_type>AIREP</pirep_type> <raw_text>ARP LSI517 4503N 03117W 1101 F390 M45 265/37 4500N 03000W 1107 4600N 02000W KT EIGWB DDL XXN 221101 F51A</raw_text> </PIREP>')

#print(XML_STRING)

tree = ET.parse(io.StringIO((XML_STRING)))
root = tree.getroot()

# root.tag says PIREP
# Loop through all elements and print their values
for element in root.iter():
    print("%s = %s" % (element.tag, element.text))

# Get a single value, like observation_time
obs_time = root.find("observation_time").text
print("Obs: %s" % obs_time)

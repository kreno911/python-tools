import jmespath
import json
# To strip out HTML tags
from bs4 import BeautifulSoup

# Print methods this package contains
print(dir(jmespath))

# First open the json file
f = open("/TEST_DATA/json/etop_10_all.json")
# Second read in the JSON data by loading the file
data = json.load(f)
#print(json.dumps(data, indent=4))

'''
JSON with the following structure:
{
    "d": {
        "results": [
            {
                "__metadata": {
...
                "Attachments": false,
                "GUID": "3f8df895-4c06-4902-8828-b62a259b27f9"
            },
            {
                "__metadata": {
...
'''
# Print all fields for the first index
search_string = "d.results[0]"
results = jmespath.search(search_string, data)
#print(json.dumps(results, indent=4))
# Print all the field names, just use the keys function since JSON is just a dictionary
#print(results.keys())

# Print only the first index value for the GUID field
search_string = "d.results[0].GUID"
print(json.dumps(jmespath.search(search_string, data), indent=4))
# Print all GUIDs and length of that set
search_string = "d.results[*].GUID"
results = jmespath.search(search_string, data)
#print(json.dumps(results, indent=4), "Len = %d" % len(results))

# Print more than one field for the first 2 rows of data (zero based)
search_string = "d.results[0:2].[Title,Aircraft_x0020_N_x0020_Number,Engine_x0020_Make_x0020_and_x002]"
results = jmespath.search(search_string, data)
#print(json.dumps(results, indent=4))

##! Copy this to the real program when ready
# Title = Flight Number, Database_x0020_ID = ID Number, ... see note
search_string = "d.results[0:2].[Title,Database_x0020_ID,Aircraft_x0020_N_x0020_Number,Engine_x0020_Make_x0020_and_x002,In_x0020_Flight_x0020_Shutdown_x,ATA_x0020_Code,Body,Corrective_x0020_Action,Comments,Other_x0020_Identifying_x0020_In,POC,Status,PercentComplete,Aircraft_x0020_Cycles,Aircraft_x0020_Hours,Aircraft_x0020_N_x0020_Number,Aircraft_x0020_Serial_x0020_Numb,Author,Editor,AssignedTo,DueDate,Created,Engine_x0020_Cycles,Engine_x0020_Hours,Engine_x0020_Position,Engine_x0020_Serial_x0020_Number,Modified,Loss_x0020_of_x0020_Thrust_x0020,Priority,RelatedItems,TaskGroup,TaskOutcome]"
results = jmespath.search(search_string, data)
print(json.dumps(results, indent=4))
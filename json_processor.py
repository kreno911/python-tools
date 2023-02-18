import json
import jmespath
import csv

print("Testing JSON")

'''
You cannot define like this:
x = { [ {"some-list-values"} ... ] }  
You will get unhashable list value error.
Just do x = [ { "list-values" } ]  (no outer brackets)
'''

# Some test data that we get from the user
request = [
    {"id":1,"airport_code":"PUN","airport_name":"Punia Airport","latitude":59.925597,"longitude":30.3406369},
    {"id":2,"airport_code":"FNR","airport_name":"Funter Bay Seaplane Base","latitude":4.0510564,"longitude":9.7678687},
    {"id":3,"airport_code":"BUA","airport_name":"Buka Airport","latitude":-5.0731807,"longitude":32.6913107},
    {"id":4,"airport_code":"BTT","airport_name":"Bettles Airport","latitude":-26.8268706,"longitude":-65.2705688},
    {"id":5,"airport_code":"AKQ","airport_name":"Gunung Batin Airport","latitude":20.0910963,"longitude":-98.7623874},
    {"id":6,"airport_code":"BOB","airport_name":"Bora Bora Airport","latitude":49.4774391,"longitude":43.8548861}
]

'''
JMES basics:
[] by itself will flatten the results while [*] will keep the structure.
'''

# Do some JMESpath testing first
# Print all AP codes
print(jmespath.search("[*].airport_code", request))
# Note on this [*] was used. If you had "data": ...
# you would use data[*].airport_code...

# Print list of booleans matching AKQ 
print("AKQ [*]:",jmespath.search("[*][airport_code == 'AKQ']", request))
# [[False], [False], [False], [False], [True], [False]]

# Do same as above, but in code
# for b in jmespath.search("[*][airport_code == 'AKQ']", request):
#     print("Value=", b, type(b), b[0], type(b[0]))
#     '''
#     Prints: 
#     Value= [False] <class 'list'> False <class 'bool'>
#     Value= [True] <class 'list'> True <class 'bool'>
#     '''
#     if b[0] == True:
#         print("Found AKQ!!")

# Print the row where airport matches AKQ
print("Row dict with AKQ:", jmespath.search("[?airport_code=='AKQ']", request))
# For above just add: .longitude to get that only OR .[latitude,longitude] to get more
# Print all VALUES for row that matches AKQ
print("Row VALUES only with AKQ:", jmespath.search("[?airport_code=='AKQ'].*", request))
# Print all rows with airport name beginning with B
print("Airport begins w B:", jmespath.search("[?airport_code=='AKQ']", request))

print()
# Get all rows with longitude < 0
#print("Less than 0:", jmespath.search("[*][?longitude < '0.0'].[*]", request))

# Create responses for the request

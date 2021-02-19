
####################################
#   This is the second part dealing with more advanced
#   use of the basics.
#
#   The focus here will mostly on dates and times as 
#   this is what gets most attention on projects.
#
#   WORKING EXAMPLES (for specific uses of these functions)
#       - For pykml look for surfaces_kml_to_gjson.py in work to see a basic use 
#         where I convert a KML file back into GEO Json.
#         Also has - map/dictionary
#
# URLLIB2
#   response = urllib2.urlopen('...')
#   response.getcode() - HTTP response code
#   response.geturl()  - URL used by request
#   response.info()    - Header info along with URL (connection status)

# Python modules (with functions only - no classes):
#   1) create your lib (mylib.py)
#   2) If in same directory as your calling files, just "import mylib"
#   3) If in a subdirectory, "from subdir import mylib"
#
####################################

# Include standard libs
import os, sys, glob, re, shutil, random
# Dates and times stuff
from datetime import datetime, date, timedelta
import time

####
# One big thing that you may need to do, convert a string to a date
# that is in one format and return a date or a string of that date
# in another format. 
#       Convert string to a date: datetime.strptime
#       Convert date into string: adate_obj.strftime("format")
####
def test_date_formats():
    print("Testing date formats...")
    # Formats:
    #   %Y - 4 digit year, %y - 2 digit year
    #   %M - minute, %S - second
    #   %H - 24 hour hour (00-23)
    #   %I - 12 hour clock (01-12), %d day of month (01-31) 
    #   https://www.tutorialspoint.com/python/time_strftime.htm
    today = datetime.now().strftime('%Y%m%d')
    year = datetime.now().strftime('%Y')
    month = datetime.now().strftime('%m')
    day = datetime.now().strftime('%d')
    current_hour = datetime.now().strftime('%H')
    last_hour = "%02d" % (int(current_hour)-1)
    # yesterday's date
    yesterday = (date.today() - timedelta(days=1)).strftime('%Y%m%d')
    myDate = "%s--%s--%s" % (year,month,day)
    print("now() = %s, hour 00 = 12am...(strftime)" % datetime.now())
    print("now(): strftime('%%Y%%m%%d')=%s,hour=%s,yesterday=%s,last hour=%s, Y--M--D=%s" \
        % (today, current_hour, yesterday, last_hour, myDate))
    print("When printing .now() you get this format by default: '2018-05-21 13:13:29.829391'")

    #   https://www.tutorialspoint.com/python/time_strptime.htm
    print("Convert string to date with format...YYYYMMDDHHMM (199911170500) with strptime")
    str = "199911170500"
    dt = datetime.strptime("199911170500", "%Y%m%d%H%M")
    print("199911170500 converted: ", dt)

def testCollections():
    # Other new imports
    from collections import Counter
    print("Testing some advanced collection functions...")
    an_array = [1,1,2,3,2,2,4,5,4,5,4,3,6,2,2]
    # Counter object will return a count dictionary of counts 
    c = Counter(an_array)
    # prints: Counter({2: 5, 4: 3, 1: 2, 3: 2, 5: 2, 6: 1})
    print("Counting numbers obj: ", c)
    # prints: [(2, 5), (4, 3), (1, 2), (3, 2), (5, 2), (6, 1)]
    print("most common output: ", c.most_common())
    # Try on a string list
    a_string_list = ["one","two","one"]
    st = Counter(a_string_list)
    # prints: Counter({'one': 2, 'two': 1})
    print("Counting string list: ", st)
    print("most common output: ", st.most_common())

    # Test an ordered collection
    from collections import OrderedDict
    print("Tesing OrderedDict which keeps order of dictionary inserts")
    ordered = OrderedDict()
    ordered[1] = 'one'
    ordered[2] = 'two'
    ordered[4] = 'four'
    print("OrderedDict: ", ordered)

    print("Test defaultdict which set value not found to 0, normal will throw KeyError")
    from collections import defaultdict
    d = defaultdict(int)
    d[1] = "python"
    d[2] = "java"
    print("Value not in dict is: %s, %d" % (d[3],d[3]))  # prints 0

# Test out a "dynamic map"
#   Function that creates a map of values to booleans
#   used to determine if a particular executable should
#   be monitored.
#   This could be expanded to return, say, locations for
#   a given argument, getExeLocation(exe)...
def get_check_flag(exe):
    return {
        "AGGREGATOR"  : True,
        "ROTORCRAFT"  : True,
        "CIWS"        : True
    }.get(exe, False)   # Return default of False if ! found

#test_date_formats()
# Boolean: %s - True, %d - 1
print("Is CIWS there? %s" % (get_check_flag("CIWS")))
testCollections()

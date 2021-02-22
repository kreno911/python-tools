
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

    print("Testing to get minutes/seconds from two dates")
    # datetime.strptime is used to convert a string into a date object
    then = datetime.strptime("2016-10-09 10:00:00.000000", "%Y-%m-%d %H:%M:%S.%f")
    now  = datetime.strptime("2016-10-09 11:00:00.000000", "%Y-%m-%d %H:%M:%S.%f")
    print("int((now-then).total_seconds())/60: ", int((now-then).total_seconds())/60)    # 60 minutes
    now  = datetime.strptime("2016-10-09 14:00:00.000000", "%Y-%m-%d %H:%M:%S.%f")
    print(int((now-then).total_seconds())/60)    # 240 m
    print(then)                                  # 2016-10-09 10:00:00
    now  = datetime.strptime("2016-10-10 10:00:00.000000", "%Y-%m-%d %H:%M:%S.%f")
    print(int((now-then).total_seconds())/60)    # 1440 (24 hr)
    # Print only parts like up to seconds

    # Set the timestamps of a file (accesstime, modifiedtime)
    a_timestamp = 1562175949        # 2019-07-03 17:45:49
    #os.utime("somefile", (a_timestamp,a_timestamp))

    # Convert a mtime value into a formatted string
    timestamp = os.path.getmtime("python_test_file1.txt") # returns: 1513777689.66
    # Prints: 2018-03-26 07:53:53
    print(datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S'))

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
# Test out file rename/moving
def testFileRename():
    # Move a file to a new name/location
    # First way - does not work across FSs also requires explicit dest filename
    #os.rename("moveme.txt", "i_moved.txt")
    # second way (better since this will move files across disks)
    shutil.move("moveme.txt", "i_moved.txt")
# Test out breaking apart a file name and path
def testFileNameInPath():
    # Pick off filename from path
    a_path = "https://nfdc.faa.gov/webContent/56DaySub/April_30__2015_file.zip"
    # All should print: April_30__2015_file.zip
    print("Getting filename only from: %s" % a_path)
    # Quick way
    print("File at end(basename): ", os.path.basename(a_path))
    # os.path.split way
    head, tail = os.path.split(a_path)
    print("File at end(os.path.split): ", tail)
    # Regular split
    print("File at end(regular split, array): ", a_path.split("/")[-1])
    # Get the base name only (April_30__2015_file)
    print("File basename (no ext): ", os.path.splitext(os.path.basename(a_path))[0])
# Test hash
def testHash():
    import hashlib
    print(hashlib.sha1(os.urandom(32)).hexdigest()[:10]) # 8e4a3f27e9
    # Get an MD5 hash of a file (you have to read it to get a true checksum)
    print("Hash: %s" % hashlib.md5(open("testdir1/1.txt",'rb').read()).hexdigest())
    # The above will match the md5sum linux command 
def testOddOnes():
    print("Using zip to gather x and y values in a straight array.")
    areaPoints = [-34.44,121.22,-77.66,144.44,-55.44,130.55]
    # zip('ABCD', 'xy') --> Ax By
    for i,k in zip(areaPoints[0::2], areaPoints[1::2]):
        print("zip: (%f, %f)" % (float(i), float(k)))

#test_date_formats()
# Boolean: %s - True, %d - 1
print("Is CIWS there? %s" % (get_check_flag("CIWS")))
testOddOnes()
testCollections()
testFileNameInPath()
testHash()

# JSON
# JSON(json) examples
# Requires test.json with two flights defined in it:
## { "flights" : [
## {
##   "flight" : "SW1339",
##   "type"   : "heavy",
##   "departure_ap" : "PHL"
## },
## {
##   "flight" : "UA9992",
##   "type"   : "heavy",
##   "departure_ap" : "JFK"
## }
## ] }
# print "  JSON file tesing..."
# jfile = open("test.json")
# values = json.load(jfile)
# # Print the second flight (UA9992)
# print values['flights'][1]['flight']
# jfile.close()

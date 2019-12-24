
####################################
#   This is the second part dealing with more advanced
#   use of the basics.
#
#   The focus here will mostly on dates and times as 
#   this is what gets most attention on projects.
####################################

# Include standard libs
import os, sys, glob, re, shutil, random
# Dates and times stuff
from datetime import datetime, date, timedelta
import time

def test_formats():
    print("Testing date formats...")
    # Formats:
    #   %Y - 4 digit year, %y - 2 digit year, %H - 24 hour hour (00-23)
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
    print "199911170500 converted: ", dt


test_formats()

#!/usr/bin/python

import argparse, csv
from datetime import datetime
# Used this to allow newlies in help text (dateformat)
import textwrap

###############################
# line_printer:
#   Take a simple CSV file with some data with a date and print only those
#   lines with matching/search criteria.
#
#   Provide a key to fileter out specific values.
#   Provide date range for files that contain a dated field, with a format
#   if necessary.
#   Provide a integer range for integer values that fall within range,
#   inclusive.
#
#   Examples:
#       # Print all lines where column 1 is equal to KDEN
#       # If value is in different column, use --col #
#       ./line_printer.py --file test_data/temp_data.csv --key KDEN
#       # Print out all lines where col 3 has values 22-24 inclusive
#       ./line_printer.py --file test_data/temp_data.csv --col 3 --intrange 22,24
#       # Get lines between dates inclusive where the date field is in column 2
#       # and have format given.
#       ./line_printer.py --file test_data/temp_data.csv --col 2
#             --starttime "2017-07-30 23:51" --endtime "2017-08-12 23:51"
#                               --dateformat "YYYY-mm-dd HH:mm"
#
###############################

parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument("--file",required=True,help=textwrap.dedent('''CSV file to parse.
Only specifying this will just dump the file'''))
# Argument for which column has the value to filter on
parser.add_argument("--col", help="Column number to filter on, default first column (1).", 
            default=1,type=int)
parser.add_argument("--key", help="Filter to key to use when not using timestamps.")
parser.add_argument("--intrange", help="Range in format 'start#,end#' (inclusive).")
# If we specify start time, must specify an end time 
parser.add_argument("--starttime", help="Start time for filter time range. Format default YYYYMMDD. \
        Required when specifying endtime")
parser.add_argument("--endtime", help="End time for filter time range. Format default YYYYMMDD. \
        Required when specifying starttime")
parser.add_argument("--dateformat", help=textwrap.dedent('''Format for timestamp field in data file. 
Examples to use: 
    YYYYmmdd - 20190201 (default)
    YYYY-mm-dd - 2019-02-01
    YYYY-mm-dd HH:mm - 20190-2-01 13:22
    YYYY-mm-dd HH:mm:ss - 20190-2-01 13:22:33
    milli - 1499489592857 (milliseconds) '''))

##
# get_range_tuple
#   Take a csv value parse it out and return the tuple: 10,20
##
def get_range_tuple(arange):
    x = int(arange.split(',')[0])
    y = int(arange.split(',')[1])
    # Return -1,-1 if we have an error like y > x
    return (x,y) if y >= x else (-1,-1)
##
# If key (filter) is set print this line.
# Return True if we printed based on key
##
def key_print(line, key, c):
    if key:
        if line[c-1].upper() == key.upper():
            print (",".join(line))
            return True
    return False
##
# within_date_range
#   Given a date/time, a start time, end time and format, return
#   True if the given date/time arg is within the time range
#   inclusive.
#   Formats supported:
#       YYYYmmdd - %Y%m%d
#       YYYY-mm-dd - %Y-%m-%d
#       YYYY-mm-dd HH:mm - %Y-%m-%d %H:%M
#       YYYY-mm-dd HH:mm:ss - %Y-%m-%d %H:%M:%S
#       milli  - millisecond value - 1499489592857
##
def within_date_range(adate,starttime,endtime,aformat):
    FORMAT_MAP = { "YYYYmmdd":"%Y%m%d",
                   "YYYY-mm-dd":"%Y-%m-%d",
                   "YYYY-mm-dd HH:mm":"%Y-%m-%d %H:%M",
                   "YYYY-mm-dd HH:mm:ss":"%Y-%m-%d %H:%M:%S",
                   "milli":"%Y-%m-%d %H:%M"
                 }
    if aformat == "milli":
        adate = datetime.fromtimestamp(float(adate)/1000).strftime('%Y-%m-%d %H:%M')
    the_date = datetime.strptime(adate,FORMAT_MAP.get(aformat))
    st_dt = datetime.strptime(starttime,FORMAT_MAP.get(aformat))
    en_dt = datetime.strptime(endtime,FORMAT_MAP.get(aformat))
    if the_date >= st_dt and the_date <= en_dt:
        return True     
    else:
        return False

args = parser.parse_args()
if args.intrange:
    the_range = get_range_tuple(args.intrange)
    if the_range[0] == -1:
        parser.error("Your range is incorrect. X must be less than Y for example")
#    print ("Your range is %d to %d" % (the_range[0],the_range[1]))
#if args.col and args.key:
#    print ("You are filtering col %d on key %s" % (args.col,args.key))
#elif args.col:
#    print ("Using column %d" % args.col)
if (args.starttime is None and args.endtime) and \
   (args.endtime is None and args.starttime):
    parser.error("start and end times are needed together.")
if args.dateformat:
#    print ("Date format %s" % args.dateformat)
    d_format = args.dateformat
else:
    d_format = "%Y%m%d"

c = args.col

with open(args.file) as f:
    # Parse each line and take action based on command line switches
    reader = csv.reader(f)
    for line in reader:
        # Skip blanks
        if len(line) == 0:
            continue
        if args.intrange:
            if int(line[c-1]) >= the_range[0] and \
               int(line[c-1]) <= the_range[1]:
                print (",".join(line))
        ##! Add option to print date in human readable (milli)
        elif args.starttime:
            # Column needs to be set correctly. 
            # Search based on time range
            if within_date_range(line[c-1],args.starttime,args.endtime,d_format):
                print (",".join(line))
                ## print get_human_date...
        elif args.key:
            key_print(line, args.key, c)
        # Just print the line
        else:
            print (",".join(line))


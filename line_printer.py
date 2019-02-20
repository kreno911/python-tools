#!/usr/bin/python

import argparse, csv
from datetime import datetime
# Used this to allow newlies in help text (dateformat)
import textwrap

parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument("--file",required=True,help=textwrap.dedent('''CSV file to parse.
Only specifying this will just dump the file'''))
# Argument for which column has the value to filter on
parser.add_argument("--col", help="Column number to filter on, default first column (1).", 
            default=1,type=int)
parser.add_argument("--key", help="Filter to key to use when not using timestamps.")
parser.add_argument("--range", help="Range in format 'start#,end#'.") 
# If we specify start time, must specify an end time 
parser.add_argument("--starttime", help="Start time for filter time range. Format default YYYYMMDD. \
        Required when specifying endtime")
parser.add_argument("--endtime", help="End time for filter time range. Format default YYYYMMDD. \
        Required when specifying starttime")
parser.add_argument("--dateformat", help=textwrap.dedent('''Format to use when specifying timestamps ex: 'yyyy-mm-dd HH:mm'. 
Current supported formats (w example): 
    YYYYmmdd - 20190201 (default)
    YYYY-mm-dd - 20190-2-01
    YYYY-mm-dd HH:mm - 20190-2-01 13:22
    YYYY-mm-dd HH:mm:ss - 20190-2-01 13:22:33'''))
# Store true tells argparse to just store this as a boolean (T/F)
parser.add_argument("--verbose","-v",help="Verbose mode",action="store_true")

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
            print ",".join(line)
            return True
    return False
##
# within_range
#   Given a date/time, a start time, end time and format, return
#   True if the given date/time arg is within the time range
#   inclusive.
#   Formats supported:
#       YYYYmmdd - %Y%m%d
#       YYYY-mm-dd - %Y-%m-%d
#       YYYY-mm-dd HH:mm
#       YYYY-mm-dd HH:mm:ss
##
def within_range(adate,starttime,endtime,aformat):
    the_date = datetime.strptime(adate,'%Y-%m-%d %H:%M')
    st_dt = datetime.strptime(starttime,aformat)
    en_dt = datetime.strptime(endtime,aformat)
    if the_date >= st_dt and the_date <= en_dt:
        return True     
    else:
        return False

args = parser.parse_args()
if args.range:
    the_range = get_range_tuple(args.range)
    if the_range[0] == -1:
        parser.error("Your range is incorrect. X must be less than Y for example")
#    print "Your range is %d to %d" % (the_range[0],the_range[1])
#if args.col and args.key:
#    print "You are filtering col %d on key %s" % (args.col,args.key)
#elif args.col:
#    print "Using column %d" % args.col
if (args.starttime is None and args.endtime) and \
   (args.endtime is None and args.starttime):
    parser.error("start and end times are needed together.")
if args.dateformat:
#    print "Date format %s" % args.dateformat
    d_format = args.dateformat
else:
    d_format = "%Y%m%d"

c = args.col

with open(args.file) as f:
    # Parse each line and take action based on command line switches
    reader = csv.reader(f)
    for line in reader:
        if args.range:
            if int(line[c-1]) >= the_range[0] and \
               int(line[c-1]) <= the_range[1]:
                print ",".join(line)
        elif args.starttime:
            # Column needs to be set correctly. 
            # Search based on time range
            if within_range(line[c-1],args.starttime,args.endtime,d_format):
                print ",".join(line)
            else:
                if args.verbose:
                    print "DATE OUTSIDE:",",".join(line)
        elif args.key:
            key_print(line, args.key, c)
        # Just print the line
        else:
            print ",".join(line)


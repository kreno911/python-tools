#!/usr/bin/python

# Check if a given date is within 5 days of given date 
#
## This will take 2 args, a month and day in that month
## It will use a default of 5 days just for demo.
## ISO format: YYYY-MM-DD

import datetime, sys

if len(list(sys.argv)) < 3:
    print "Need month and day args (./x 10 5): %d" % len(list(sys.argv))
    sys.exit(11)

# Year is set to 2017 at the moment 
numOfDays = 5   # Look before and after by 5 days
month = int(sys.argv[1])
day = int(sys.argv[2])
today = datetime.date.today()
print "Today: %s" % today
margin = datetime.timedelta(days = numOfDays)
withInRange = today - margin <= datetime.date(2017, month, day) <= today + margin

print "Within %s days range: %s" % (numOfDays, withInRange)


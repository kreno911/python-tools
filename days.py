#!/usr/bin/python

import datetime

## ISO format: YYYY-MM-DD

numOfdays = 20
# Generate dates: YYYY-MM-DD for some number of days
for i in range(numOfdays):
   theDate = datetime.date(2015,05,11) + datetime.timedelta(days=i)
   print "Date = %s" % theDate

print "Start date was: 2015,05,11 for %d days" % numOfdays


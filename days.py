#!/usr/bin/python

import datetime

## ISO format: YYYY-MM-DD

numOfdays = 20
# Generate dates: YYYY-MM-DD for some number of days
for i in range(numOfdays):
   # Always use single digit, not 05 as 0# is interpreted as an octal
   theDate = datetime.date(2015,5,11) + datetime.timedelta(days=i)
   print("Date = %s" % theDate)

print("Start date was: 2015,5,11 for %d days" % numOfdays)


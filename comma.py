#!/usr/bin/python

# Add commas to long #s
## Usage: ./comma.py 123456
##      returns: 123,456

import os, sys

# Number needs to be a string, not an int (int not iterable)
def comma(number):
        e = list(number)
        for i in range(len(e))[::-3][1:]:
                e.insert(i+1,",")
        return "".join(e)

if len(sys.argv) < 1:
	print "Please enter a number!"
	sys.exit(11)
	
number = sys.argv[1]
print comma(number)

#!/usr/bin/python

import sys, re

file = open(sys.argv[1])
for line in file:
    # Skip garbage lines we get in the file
    if line.startswith('Property') or line.startswith('Received'):
       continue
    # Pull out timestamp and xml version characters which are on the 
    # same line as the start of the NasFlight
    if re.search(r'^\d{4}', line):
        line = line[61:];
        #print "DATE: ", line.rstrip()
    if line.strip():
        print line.rstrip()


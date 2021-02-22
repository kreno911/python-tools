#! /usr/bin/env python

# Test out what we can do with server stats like CPU usage, disk
# usage, etc...

# NEED TO ADD CPU stats!!!*****************

import os, sys, re
from datetime import timedelta

# Uptime information:
# /proc/uptime contains the uptime of system in seconds and time spent idle
def getUptime():
     try:
         f = open( "/proc/uptime" )
         contents = f.read().split()
         f.close()
     except:
        return "Cannot open uptime file: /proc/uptime"
 
     total_seconds = float(contents[0])
 
     # Helper vars:
     MINUTE  = 60
     HOUR    = MINUTE * 60
     DAY     = HOUR * 24
 
     # Get the days, hours, etc:
     days    = int( total_seconds / DAY )
     hours   = int( ( total_seconds % DAY ) / HOUR )
     minutes = int( ( total_seconds % HOUR ) / MINUTE )
     seconds = int( total_seconds % MINUTE )
 
     # Build up the pretty string (like this: "N days, N hours, N minutes, N seconds")
     string = ""
     if days > 0:
	 # Sneaky way to do a c++ style ternary operator which python does not have
         string += str(days) + " " + (days == 1 and "day" or "days" ) + ", "
     if len(string) > 0 or hours > 0:
         string += str(hours) + " " + (hours == 1 and "hour" or "hours" ) + ", "
     if len(string) > 0 or minutes > 0:
         string += str(minutes) + " " + (minutes == 1 and "minute" or "minutes" ) + ", "
     string += str(seconds) + " " + (seconds == 1 and "second" or "seconds" )
     return string
 
def printUsage(sys):
	disk = os.statvfs(sys)
	totalBytes = float(disk.f_bsize*disk.f_blocks)
	print "total space: %d Bytes = %.2f KBytes = %.2f MBytes = %.2f GBytes" % (totalBytes, totalBytes/1024, totalBytes/1024/1024, totalBytes/1024/1024/1024) 
	totalUsedSpace = float(disk.f_bsize*(disk.f_blocks-disk.f_bfree))
	print "used space: %d Bytes = %.2f KBytes = %.2f MBytes = %.2f GBytes" % (totalUsedSpace, totalUsedSpace/1024, totalUsedSpace/1024/1024, totalUsedSpace/1024/1024/1024) 
	totalAvailSpace = float(disk.f_bsize*disk.f_bfree)
	print "available space: %d Bytes = %.2f KBytes = %.2f MBytes = %.2f GBytes" % (totalAvailSpace, totalAvailSpace/1024, totalAvailSpace/1024/1024, totalAvailSpace/1024/1024/1024) 
	totalAvailSpaceNonRoot = float(disk.f_bsize*disk.f_bavail)
	
	# Print out percentages rounded like '45%'
	return "%s -> %d%s" % (sys, round(totalUsedSpace / totalBytes * 100), '%')

print "Getting uptime and disk usage for /..."
print getUptime()
print printUsage('/')


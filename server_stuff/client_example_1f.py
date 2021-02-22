#! /usr/bin/env python

import socket, sys, os, fcntl, struct, time
import random

# A client to send out data to server

# This simple example goes with server_example_1.py and should not be modified.
# Use this as a template to work off.

weather_strings = [ 'Radar', 'GOES', 'METAR', 'TAF', 'END' ]

if len(sys.argv) != 3 and len(sys.argv) != 4:
	print "You need a machine, port and an optional interface (eth0 default)..."
 	sys.exit(11)

host = sys.argv[1]
port = sys.argv[2]
interface = "eth0"
if len(sys.argv) == 4:
	interface = sys.argv[3]

try:
    sock = socket.socket()
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print "Trying to connect to %s on port %s on interface %s" % (host, port, interface)
    sock.connect((host, int(port)))
except socket.error, msg:
    print 'Failed to create socket. Error code: ' + str(msg[0]) + \
	  ' , Error message : ' + msg[1]
    sys.exit();

while True:
    try:
		data = random.choice(weather_strings)
		print "Sending...", data
		sock.send(data)
		if data == "END":
			break
    
        # close us out
        #sock.close()
		print "Sleeping..."
		time.sleep(5)
    except socket.error, msg:
        print 'Failed to create socket. Error code: ' + str(msg[0]) + \
		    ' , Error message : ' + msg[1]
        sys.exit();
    except KeyboardInterrupt:
		break

print "Goodby..."
sock.close()

#! /usr/bin/env python

import socket, sys, os, fcntl, struct

### This Server really only handles a single client...but it gives much of the basics
### needed to work the real thing.

# This simple example goes with client_example_1.py and should not be modified.
# Use this as a template to work off.

# check that things are running ok, accept a command from outside
# cmd counts as an arg
if len(sys.argv) != 3 and len(sys.argv) != 4:
	print "You need a machine, port and an optional interface (eth0 default)..."
 	sys.exit(11)

host = sys.argv[1]
port = sys.argv[2]
interface = "eth0"
if len(sys.argv) == 4:
	interface = sys.argv[3]

print "Trying %s on port %s on interface %s" % (host, port, interface)

# Start a new socket
sock = socket.socket()
# Switch localhost to the real IP
# This ugly line returns the local IP address of eth0...just pass other names
# if you have a multihomed host (IT DID, IT DOES NOT WORK WITH NEW MINT)
#if host == "127.0.0.1" or host == "localhost":
#	host = 	socket.inet_ntoa(fcntl.ioctl(sock.fileno(), 0x8915, \
#			struct.pack('256s',interface[:15]))[20:24])
print "Server IP : ", host

# If we die, make sure we give up the port so we can restart
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind((host, int(port)))
sock.listen(0)
while True:
   try:
	aConnect, addr = sock.accept()
	print "Connected from: " + str(addr)
	while True:
		data = aConnect.recv(1024)
		if not data:
			# Get this when we hit control-C or client is killed, clean way is below
			print "No data, hit contr-C?"
			break
		print "data = " + str(data.rstrip())
		if data.rstrip() == "END":
			print "Closing..."
			aConnect.send("Goodby\n")
			break
   except KeyboardInterrupt:
	# Capture control-C
	print "Exiting..."
	sys.exit()

   # close the connection 
   aConnect.close()

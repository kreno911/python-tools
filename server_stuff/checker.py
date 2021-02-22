#! /usr/bin/env python

######
##  Program to demo basic server connections from another side/app
##  Test out with ./checker.py localhost 9999
##                nc localhost 9999
#                 <type any message>
#                 close - to close the connection

import socket, sys

# check that things are running ok, accept a command from outside
# cmd counts as an arg
if (len(sys.argv) != 3):
    print "You need a machine and port..."
    sys.exit(11)

host = sys.argv[1]
port = sys.argv[2]

print "Trying %s on port %s" % (host, port)

# Check if port is already being used:
# netstat -ant | grep :8888
# tcp        0      0 127.0.0.1:8888              0.0.0.0:*                   LISTEN
sock = socket.socket()
# If we die, make sure we give up the port so we can restart
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind((host, int(port)))
sock.listen(0)
done = False
while not done:
    aConnect, addr = sock.accept()
    print "Connected from: " + str(addr)
    while True:
        data = aConnect.recv(1024)
        if not data:
            # Get this when we hit control-C, clean way is below
            print "No data, hit contr-C?"
            break
        print "data = " + str(data.rstrip())
        if data.rstrip() == "close":
            print "Closing..."
            aConnect.send("Goodby\n")
            aConnect.close()
            done = True
            break


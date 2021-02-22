#!/usr/bin/python

import socket, sys

if len(sys.argv) < 4:
    print "Need host and port...(%d)" % len(sys.argv)
    sys.exit(11)

host = sys.argv[1]
port = int(sys.argv[2])
message = sys.argv[3]

print "Trying to connect to %s port %s" % (host, port)

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # UDP
sock.sendto(message, (host, port))


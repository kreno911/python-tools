#!/usr/bin/python

import time, socket, sys

# Test out talking with another python app on another processor
# The two of them need to determine who is the primary

# This file goes with test_server_1.py which was a start to see
# if two servers could get a dialogue going

def sendToClient(stuff):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(('localhost', 10000))
	s.send(stuff)
	s.close()

# The main entry to program
def main():
	print "This is server 2..."
	address_stuff = socket.getaddrinfo("localhost", 21)
	#address_stuff = socket.getaddrinfo("192.168.1.201", 21)
	# returns [family, sockettype, proto, name, sockaddress]
	print "   ", address_stuff
	# Create the TCPIP socket
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	# Bind this socket to the local address
	server_address = ('127.0.0.1', 10001)
	print "Starting on port 10001"
	sock.bind(server_address)
	# Start listening
	sock.listen(1)

	while True:
		print "Sending..."
		connection, client_address = sock.accept()
		try:
			while True:
				data = connection.recv(128)
				print "Got: ", data
				if not data:
					print "    No more data on server 2..." 
					break
				else:
					sendData = raw_input("Enter something: ")
					sendToClient(sendData)
					#connection.sendall(data)
		finally:
			# Close the connection
			connection.close()
		# Pause for a bit
		time.sleep(3)

if __name__ == "__main__":
    main()


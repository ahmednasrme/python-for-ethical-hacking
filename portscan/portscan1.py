#!/usr/bin/python
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = raw_input('Enter Host:')
port = int(raw_input('Enter Port:'))

def pscan(port):
	if sock.connect_ex((host,port)):
		print "Port %d is closed" %(port)
	else:
		print "Port %d is Open" %(port)
pscan(port)

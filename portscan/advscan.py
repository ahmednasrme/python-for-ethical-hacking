#!/usr/bin/python

from socket import *
from threading import *
import optparse

def connScan(host,port):
	try:
		sock = socket(AF_INET, SOCK_STREAM)
		sock.connect((host,port))
		print '[+] %d/tcp Open' % port
	except:
		print '[-] %d/tcp Closed' % port
	finally:
		sock.close()

def port_scan(Host,ports):
	try:
		HostIP= gethostbyname(Host)
	except:
		print 'Host Unknown'
	setdefaulttimeout(1)
	for port in ports:
		t = Thread(target = connScan, args = (Host, int(port)))
		t.start()
def main():
	parser = optparse.OptionParser('Usage: '+'-H <Host> -P <Ports>')
	parser.add_option('-H', dest='host', type='string', help='Target Host')
	parser.add_option('-P', dest='ports', type='string', help='Target PortS seperated by comma')
	(options, args) = parser.parse_args()
	host = options.host
	ports = str(options.ports).split(',')
	if (host == None) | (ports[0] == None):
		print parser.usage
		exit()
	port_scan(host,ports)
main()

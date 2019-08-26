#!/usr/bin/python

from socket import *
from threading import *
import optparse
import re

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
		HostIP = gethostbyname(Host)
		print 'Scan IP: ' + HostIP
	except:
		print 'Host Unknown'
	setdefaulttimeout(1)
	for port in ports:
		t = Thread(target = connScan, args = (Host, int(port)))
		t.start()
def main():
	parser = optparse.OptionParser('Usage: '+'-H <Host> -P <Ports> Specific ports seperated by comma, or as range ex: 82-443')
	parser.add_option('-H', dest='host', type='string', help='Target Host')
	parser.add_option('-P', dest='ports', type='string', help='Target PortS seperated by comma')
	(options, args) = parser.parse_args()
	host = options.host
	ports = str(options.ports).split(',')
	if (host == 'None') | (ports[0] == 'None'):
		print parser.usage
		exit()
	elif (len(ports) == 1) and (re.search('[0-9*]-[0-9*]',ports[0]) is not None):
		print 'Scan range:' + ports[0]
		ports = ports[0].split('-')
		ports = range(int(ports[0]),int(ports[1])+1)
	print ports
	port_scan(host,ports)
if __name__ == '__main__':
	main()

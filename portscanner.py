import socket


targets = input('Please Enter the targets to scan, split with , : ')
ports = int(input('Please enter the number of port to scan : '))


def scan_port(ipAddr, port):
	try:
		sock = socket.socket()
		sock.connect((ipAddr, port))
		print('[+] open port ' + str(port))
		sock.close()
	
	except:
		pass

def scan(target, ports):
	print('\n' + 'starting scan for ' + str(target))
	for port in range(1, ports):
		scan_port(target, port)

if ',' in targets:
	for target in targets.split(','):
		scan(target.strip(' '), ports)

else:
	scan(targets, ports)
		

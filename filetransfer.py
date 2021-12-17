import socket
import threading
import os
from time import sleep
import time
import netifaces

def get_broadcast():
	interfaces = netifaces.interfaces()
	for i in interfaces:
		a = netifaces.ifaddresses(i)
		if 2 in a:
			if 'broadcast' in a[2][0]:
				broadcast = a[2][0]['broadcast']
	return broadcast

run = True

def find_hosts():
	hosts = set()
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	sock.settimeout(5)
	sock.bind(('0.0.0.0', 31337))
	last = time.time()
	while time.time() - last < 5:
		try:
			conn, addr = sock.recvfrom(1024)
			if conn == b'7LFTFND':
				if addr not in hosts:
					hosts.add(addr)
					last = time.time()
		except:
			sock.close()
			return list(hosts)

def aknowledge():
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	host, port = get_broadcast(), 31337
	while run:
		sock.sendto(b'7LFTFND', (host, port))
		sleep(1)

aknowledge_thread = threading.Thread(target=aknowledge)
aknowledge_thread.start()

username = input('Enter username: ')

hosts = []

while run:
	command = input(f'[{username}]:').split()
	os.system('clear')
	if len(command) == 0:
		print('Empty command')
	else:
		if command[0] == 'find':
			if len(command) == 1:
				print('Usage: find <options>')
			else:
				if command[1] == 'hosts':
					hosts = find_hosts()
				else:
					print(f'Unknown option: {command[1]}')
		elif command[0] == 'list':
			if len(command) == 1:
				print('Usage: list <options>')
			else:
				if command[1] == 'hosts':
					for i in hosts:
						print(i[0], i[1])
				else:
					print(f'Unkown option: {command[1]}')
		elif command[0] == 'quit':
			run = False
		else:
			print(f'Unkown command: {command[0]}')
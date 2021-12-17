import socket
import threading
import os
from time import sleep

run = True

def find_hosts():
	hosts = set()
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	sock.settimeout(5)
	sock.bind(('0.0.0.0', 31337))
	while True:
		try:
			conn, addr = sock.recv(1024)
			if conn == b'7LFTFND':
				print(addr)
				hosts.add(addr)
		except:
			sock.close()
			return list(hosts)

# factories our next goal -> кориченвый/красноватый форум. сообщение будто на отрывке страницы
# техника основы начала осознания черная обложка *чтобы начать надо* _пустая_ 11 пунктов.->подпунктыпервое - конец базы ... -> ответь на вопрос о чем ты
# 
# для подключнеия к инфрормационному полю достаточно сдивунуть тс
# для увеличения сдвига можно использовать насильную ыиксацию
# 
# проверка.
# книга
# 

def aknowledge():
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	host, port = '127.0.0.1', 31337
	while run:
		print('HI')
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
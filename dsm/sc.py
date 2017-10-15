import socket
import os
import time

sock = socket.socket()
sock.connect(('localhost', 9090)) #213.230.79.176

os.system('cls')
print ("----------------")
print ("--Instructions--")
print ("----------------")
print ("Send me any message you want")
print ("To exit type \"close\"")

file = open("pack/info.json")
pack = file.read()
closecmd = "close"
tempcounter = 0
while True:
	print(">>> ", end='')
	#sock.send(input().encode())
	sock.send(pack.encode())
	time.sleep(5)
	data = sock.recv(1024).decode()
	if data=="close":
		break
	print ("<<<",data)
	tempcounter+=1
	if tempcounter==1:
		break

sock.close()
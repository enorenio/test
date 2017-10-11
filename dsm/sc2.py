import socket
import os
import math
sock = socket.socket()
sock.connect(('192.168.43.167', 9090)) #213.230.79.176

os.system('cls')
print(math.factorial(400000000))
print ("----------------")
print ("--Instructions--")
print ("----------------")
print ("Send my any message you want")
print ("To exit type \"close\"")

while True:
	print(">>> ")
	sock.send(raw_input().decode())
	data = sock.recv(1024).decode()
	if data=="close":
		break
	print ("<<<"+data)
sock.close()


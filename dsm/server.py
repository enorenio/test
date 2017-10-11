import socket

s = socket.socket()         # Create a socket object
host = ''    #private ip address of machine running fedora
port = 9090
s.bind((host, port))

s.listen(5)
c, addr = s.accept()
print ('Got connection from', addr)    #this line never gets printed
while True:
   c.send(raw_input("Server please type: "))
   print ("From Client: ", c.recv(1024))

c.close()
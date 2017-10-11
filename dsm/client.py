import socket

s = socket.socket()
host = '213.230.79.176' 
port = 9090

s.connect((host, port))
while True: 
    print ("From Server: ", s.recv(1024))  #This gets printed after sometime
    s.send(raw_input("Client please type: "))

s.close()   
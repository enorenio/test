import socket
import sys

file = open("info.json")
pack = file.read()

HOST, PORT = "localhost", 9090
#data = " ".join(sys.argv[1:])
data = pack

# Create a socket (SOCK_STREAM means a TCP socket)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect to server and send data
sock.connect((HOST, PORT))
sock.sendall(bytes(data + "\n".encode("utf-8")))

    # Receive data from the server and shut down
received = str(sock.recv(1024).encode("utf-8"))

# print data to console for debug
#print("Sent:     {}".format(data))
#print("Received: {}".format(received))

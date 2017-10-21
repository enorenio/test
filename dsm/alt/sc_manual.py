import socket
import sys

#file = open("../pack/info.json")
#pack = file.read()

HOST, PORT = "localhost", 9090
#data = " ".join(sys.argv[1:])
data = input()

# Create a socket (SOCK_STREAM means a TCP socket)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    # Connect to server and send data
    sock.connect((HOST, PORT))
    sock.sendall(bytes(data + "\n", "utf-8"))
    #sock.sendall(bytes(raw_input().decode(), "utf-8"))
    

    # Receive data from the server and shut down
    received = str(sock.recv(1024), "utf-8")

print("Sent:     {}".format(data))
print("Received: {}".format(received))
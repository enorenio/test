import socket
import json
import configparser

Config = configparser.ConfigParser()
Config.read("config.ini")
port = Config.get("Settings", "Port")

sock = socket.socket()
sock.bind(('', int(port)))
sock.listen(1)
conn, addr = sock.accept()

print ('connected:', addr)

while True:
    data = conn.recv(1024).decode()
    if data:
        j = json.loads(data)
        print (int(j['one']) + int(j['two']) + int(j['three']))
    if data=="close":
        conn.send("The server stopped working, input anything to exit".encode())
        print("closed")
        break
    conn.send(data.encode())
    #print(data)
conn.close()
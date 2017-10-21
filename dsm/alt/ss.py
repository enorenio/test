import socketserver
import json
import configparser
import pymysql

connection=pymysql.connect(host="127.0.0.1", port=3306, user="Renion", passwd="password", db="recvdata", autocommit=True)
cursor = connection.cursor()

Config = configparser.ConfigParser()
Config.read("config.ini")
port = int(Config.get("Settings", "Port"))

class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024)
        self.j = json.loads(self.data.decode())

        #print (int(self.j['one']) + int(self.j['two']) + int(self.j['three']))

        print("{} wrote:".format(self.client_address[0]))
        #for item in self.j:
        print(self.j["Date"])
        print(self.j["IMEI"])
        print(self.j["GEO"]['x'])
        print(self.j["GEO"]['y'])
        #cursor.execute("INSERT INTO datatable (Date, IMEI, GEO) VALUES ("+"'2012-01-01 14:22:13'"+", "+"123451234512345"+", "+"PointFromText(CONCAT('POINT(',1.25,' ',2.35,')'))"+");")
        #UPDATE `datatable` SET `Date`='2012-01-01 14:22:13',`IMEI`=123451234512345,`GEO`=POINT(1,0) WHERE 1
        # MySQL area (all with mistakes)
        try:
            print("--------")
            print(self.j["Date"])
            print("--------")
            cursor.execute("INSERT INTO datatable (Date, IMEI, GEO) VALUES ('"+self.j["Date"]+"', "+self.j["IMEI"]+", "+"PointFromText(CONCAT('POINT(',"+self.j["GEO"]['x']+",' ',"+self.j["GEO"]['y']+",')'))"+");")
            print("try error")
        except:
            print("except error")
        finally:
            print("finally")
            sql_data = cursor.fetchall ()
        # Mysql area end



        # just send back the same data, but upper-cased
        self.request.sendall(self.data.upper())

if __name__ == "__main__":
    HOST, PORT = "localhost", port

    # Create the server, binding to localhost on port 9999
    #with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
    server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)
    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()

    cursor.close ()
    connection.close ()
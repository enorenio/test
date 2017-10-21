import socketserver
import json
import configparser
import pymysql

Config = configparser.ConfigParser()
Config.read("config.ini")
HOST = Config.get("Settings", "HOST")
PORT = int(Config.get("Settings", "PORT"))
MYSQL_HOST = Config.get("Settings", "MYSQL_HOST")
MYSQL_PORT = int(Config.get("Settings", "MYSQL_PORT"))
MYSQL_USER = Config.get("Settings", "MYSQL_USER")
MYSQL_PASS = Config.get("Settings", "MYSQL_PASS")
MYSQL_DB = Config.get("Settings", "MYSQL_DB")

connection=pymysql.connect(host=MYSQL_HOST, port=MYSQL_PORT, user=MYSQL_USER, passwd=MYSQL_PASS, db=MYSQL_DB)



class MyTCPHandler(socketserver.BaseRequestHandler):

    def handle(self):

        self.data = self.request.recv(1024)
        self.j = json.loads(self.data.decode())

        print("{} wrote:".format(self.client_address[0]))

        print(self.j["Date"])
        print(self.j["IMEI"])
        print(self.j["GEO"]['x'])
        print(self.j["GEO"]['y'])
        
        try:
            with connection.cursor() as cursor:
                query = "INSERT INTO datatable (Date, IMEI, GEO) VALUES ('"+self.j["Date"]+"', "+self.j["IMEI"]+", "+"PointFromText(CONCAT('POINT(',"+self.j["GEO"]['x']+",' ',"+self.j["GEO"]['y']+",')'))"+");"
                cursor.execute(query)
            connection.commit()
            sql_data = cursor.fetchone()
        except:
            print("Exception occured. Cannot insert.")
        finally:
            print("asd")
            connection.cursor().close()

        self.request.sendall(self.data)

if __name__ == "__main__":

    server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)

    server.serve_forever()
    connection.close()
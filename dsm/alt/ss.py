import SocketServer
import json
import configparser
import pymysql
import os
import sys
import signal

#signal.signal(signal.SIGINT, exit(0))

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



class MyTCPHandler(SocketServer.BaseRequestHandler):

    def handle(self):

        self.data = self.request.recv(1024)
        self.j = json.loads(self.data.decode())

        #print received data to console for debug

        #print("{} wrote:".format(self.client_address[0]))
        #print(self.j["Date"])
        #print(self.j["IMEI"])
        #print(self.j["GEO"]['x'])
        #print(self.j["GEO"]['y'])
        
        try:
            with connection.cursor() as cursor:
                query = "INSERT INTO datatable (Date, IMEI, GEO) VALUES ("+"NOW()"+", "+self.j["IMEI"]+", "+"PointFromText(CONCAT('POINT(',"+self.j["GEO"]['x']+",' ',"+self.j["GEO"]['y']+",')'))"+");"
                cursor.execute(query)
            connection.commit()
            sql_data = cursor.fetchone()
        except:
            print("Exception occured. Cannot insert query.")
        finally:
            connection.cursor().close()
        #send back data for debug

        self.request.sendall(self.data)

def daemonize (stdin='dev/null', stdout='dev/null', stderr='dev/null'):
	# Perform first fork.
	try:
		pid = os.fork()
		if pid > 0:
			sys.exit(0) # Exit first parent.
	except OSError as e:
		sys.stderr.write("fork #1 failed: (%d) %s\n" % (e.errno, e.strerror))
		sys.exit(1)
	# Decouple from parent environment.
	os.chdir("/")
	os.umask(0)
	os.setsid()
	# Perform second fork.
	try:
		pid = os.fork()
		if pid > 0:
			sys.exit(0) # Exit second parent.
	except OSError as e:
		sys.stderr.write("fork #2 failed: (%d) %s\n" % (e.errno, e.strerror))
		sys.exit(1)
	# The process is now daemonized, redirect standard file descriptors.
	for f in sys.stdout, sys.stderr: f.flush( )
	si = file(stdin, 'r')
	so = file(stdout, 'a+')
	se = file(stderr, 'a+', 0)
	os.dup2(si.fileno( ), sys.stdin.fileno())
	os.dup2(si.fileno( ), sys.stdin.fileno())
	os.dup2(si.fileno( ), sys.stdin.fileno())

if __name__ == "__main__":
    #daemonize(stdout='tmp/stdout.log', stderr='tmp/stderr.log')

	server = SocketServer.TCPServer((HOST, PORT), MyTCPHandler)
	try:
		server.serve_forever()
	except KeyboardInterrupt:
		print ("Bye..")	
		signal.signal(signal.SIGINT, exit(0))
	connection.close()
    

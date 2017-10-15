import pymysql

connection=pymysql.connect(host="127.0.0.1", port=3306, user="Renion", passwd="password", db="recvdata")

cursor = connection.cursor()

cursor.execute("SELECT original FROM datatable") #ALTER TABLE datatabke ADD item INT DEFAULT self.j[item]

sql_data = cursor.fetchall ()

cursor.close ()

connection.close ()

print (sql_data[0][0])




'''
db.query("SELECT original FROM datatable")

r = db.store_result()

print(r.fetch_row())
'''
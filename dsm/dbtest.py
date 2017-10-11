import pymysql

db=pymysql.connect(host="127.0.0.1", port=3306, user="Renion", passwd="toor", db="numbers")
'''
db.query("SELECT spam, eggs, sausage FROM breakfast")

r = db.store_result()
print(r.fetch_row())
'''
c = db.cursor()

query = "INSERT INTO breakfast (spam, eggs, sausage) VALUES (2,2,2)"

c.execute(query)

db.commit()
c.close()
print("ready!")

'''
c.executemany(
      """INSERT INTO breakfast (name, spam, eggs, sausage, price)
      VALUES (%s, %s, %s, %s, %s)""",
      [
      ("Spam and Sausage Lover's Plate", 5, 1, 8, 7.95 ),
      ("Not So Much Spam Plate", 3, 2, 0, 3.95 ),
      ("Don't Wany ANY SPAM! Plate", 0, 4, 3, 5.95 )
      ] )

c.close()
'''
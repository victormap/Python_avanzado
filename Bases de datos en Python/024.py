import pymysql

con = pymysql.connect(user="root", password="", host="127.0.0.1", database="bdpython")

cursor = con.cursor()
cursor.execute("INSERT INTO example (id, data) VALUES ('9', 'dato')")

con.commit()
con.close()
import pymysql

con = pymysql.connect(user="root", password="", host="127.0.0.1", database="bdpython")

cursor = con.cursor()
cursor.execute("CREATE TABLE example (id INT, data VARCHAR(100));")

con.close()
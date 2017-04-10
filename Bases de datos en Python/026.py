import pymysql

con = pymysql.connect(user="root", password="", host="127.0.0.1", database="bdpython")

cursor = con.cursor()
cursor.execute("DELETE FROM `example` WHERE `id`=9;")
con.commit()
cursor.close()
con.close()
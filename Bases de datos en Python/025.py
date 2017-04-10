import pymysql

con = pymysql.connect(user="root", password="", host="127.0.0.1", database="bdpython")

cursor = con.cursor()
cursor.execute("SELECT * FROM example WHERE id=9")

rows = cursor.fetchall()

for row in rows:
    print(row)

cursor.close()
con.close()
import sqlite3

con = sqlite3.connect('pythondb.sqlite')

num = '1'

for row in con.execute("SELECT * FROM 'usuarios' WHERE id=?", num):
    print(row)

con.close()
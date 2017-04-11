import sqlite3

con = sqlite3.connect('pythondb.sqlite')

for row in con.execute("SELECT * FROM 'usuarios'"):
    print(row)

con.close()
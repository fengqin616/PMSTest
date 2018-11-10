import pyodbc

conn = pyodbc.connect('DSN=sqlserver;UID=sa;PWD=das@123')
conn.setencoding(encoding='utf-8')

cursor =conn.cursor()

cursor.execute("SELECT * from vehicles")
for row in cursor:
    print(row)


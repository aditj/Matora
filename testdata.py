import sqlite3

conn = sqlite3.connect('data.db')

print("Connected")
cursor = conn.execute("SELECT COLNAME from DATA")
print(1)
for i in cursor:
    print(i[0])
print(2)
conn.close()

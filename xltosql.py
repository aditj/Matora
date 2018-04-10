import xlrd
book = xlrd.open_workbook('DataIIT1004.xlsx')
s1 = book.sheet_by_index(0)

import sqlite3

conn = sqlite3.connect('data.db')

print "Opened databa"

conn.execute('''CREATE TABLE DATA
         (COLNAME TEXT NOT NULL,
         BRANCH           TEXT    NOT NULL,
         STATE            TEXT     NOT NULL,
         O        INT,
         C        INT,
         Entrance TEXT,
         YEAR INT,
         TYPE TEXT,
         DURATION INT);''')


for j in range(1,936):
    lis = []
    cells = (s1.row_slice(rowx=j, start_colx=1,end_colx = 9))
    for i in cells:
        lis.append(i)

conn.execute("INSERT INTO DATA (COLNAME,BRANCH,STATE,O,C,ENTRANCE,YEAR,TYPE,DURATION) \
      VALUES ( )");
        
    

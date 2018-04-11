import xlrd
book = xlrd.open_workbook('DataIIT1004.xlsx')
s1 = book.sheet_by_index(1)    #on sheet 2

import sqlite3

conn = sqlite3.connect('data.db')

noofrows = 33 #Enter row no of last entry

for j in range(2,noofrows):
	lis = []
	cells = (s1.row_slice(rowx=j, start_colx=1,end_colx = 10))
	for i in cells:
		lis.append(i.value)
	lis[1] = lis[1].strip()
	tup = (tuple(lis))
	
	
	stri  = str(tup)
	print(stri)
	stri = stri.replace('\xa0', '')
	conn.execute("INSERT INTO DATA (COLNAME,BRANCH,STATE,O,C,ENTRANCE,YEAR,TYPE,DURATION) VALUES "+stri + ";");
        
conn.commit()
conn.close()

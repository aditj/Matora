import sqlite3
conn = sqlite3.connect('data.db')
cursor = conn.execute("SELECT * from DATA")
##########################################################
rank = 1000
hs = 'UP'
durationcriteria = True
duration = 4



chances = []
confirm = []

def checkduration(i):
    if durationcriteria:
        if i[8] == duration:
            return True
        else : return False
    else : return True


    
# homestate - 1.2, 
for i in cursor:
    i = list(i)
    
    i.append(1)
    if i[4] > 0.7*rank and i[4] < 1.1 *rank and checkduration(i):
                
        chances.append(i)
    elif i[4] > 1.1*rank and i[4] < 1.35 *rank and checkduration(i) :
        
        confirm.append(i)

for i in confirm:
    print(i)
    

conn.close()

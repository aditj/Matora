#College Displayer With Details
import sqlite3 
conn = sqlite3.connect('data.db')  #use data.db file
cursor = conn.execute("SELECT * from DATA")
##########################################################
<<<<<<< HEAD
rank = 1200
hs = 'UP'
branch = 'chemical'
durationcriteria = True
duration = 4
dura_pref=True  #this is durationpreference 
=======
rank = [1000]   #rank (input by user)  order :jeemains ,jee advanced ,bits

hs = 'UP'       #home state 
durationcriteria = True #duration preference implementation strictly only or not
duration = 4   #duration
dura_pref=True  #this is duration preference 
>>>>>>> d8ef55c4adbf2111ff773b8f367bc2aaa651fbc8
prefferedcollege  =[] #ist of preffered colleges 
chances = []       #all college with a good chance of entrance
confirm = []

def checkduration(i):
    if durationcriteria:
        if i[8] == duration:
            return True
        else : return False
    else : return True
def scorecal(i):
        if "Indian Institute of Technology" in i[0]:
                i[9] *= 1.5
        if "BITS" in i[0]:
                i[9] *= 1.3
        if "National Institute of Technology" in i[0]:
<<<<<<< HEAD
                i[9] *= 1.2
        if dura_pref == True and i[8] == duration:
            i[9]*= 1.2
        if i[2] == hs:
            i[9]*=1.2
	
        if branch.lower() in i[1].lower() :
                i[9] *= 1.2

=======
            i[9] *= 1.2
	
>>>>>>> d8ef55c4adbf2111ff773b8f367bc2aaa651fbc8

            

	
score  = 1  #temp name    
# homestate - 1.2, 
for i in cursor:
    i = list(i)
    
    i.append(1)
    scorecal(i)
    if i[4] > 0.7*rank[0] and i[4] < 1.1 *rank and checkduration(i):
                
        chances.append(i)
    elif i[4] > 1.1*rank[0] and i[4] < 1.35 *rank and checkduration(i) :
        
        confirm.append(i)



for i in confirm:
    print(i)
    

conn.close()

#College Displayer With Details
import sqlite3 
conn = sqlite3.connect('data.db')  #use data.db file
cursor = conn.execute("SELECT * from DATA")
##########################################################

rank = 1200
hs = 'UP'
branch = 'chemical'
durationcriteria = True
duration = 4
dura_pref=True  #this is durationpreference 

ranks = {'Mains':2100, 'Adv' : 1000, 'BITSAT' : 350, 'MUOET' : 40000}   #rank (input by user)  order :jeemains ,jee advanced ,bits



hs = 'UP'       #home state 
durationcriteria = True #duration preference implementation strictly only or not
duration = 4   #duration
dura_pref=True  #this is duration preference 

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

                i[9] *= 1.2
        if dura_pref == True and i[8] == duration:
            i[9]*= 1.2
        if i[2] == hs:
            i[9]*=1.2
	
        if branch.lower() in i[1].lower() :
                i[9] *= 1.2


        


            

	
score  = 1  #temp name    
# homestate - 1.2, 
for i in cursor:
    i = list(i)
    
    i.append(1)
    scorecal(i)
    rank = ranks[i[5]]
    
    if i[4] > 0.7*rank and i[4] < 1.1 *rank and checkduration(i):
                
        chances.append(i)
    elif i[4] > 1.1*rank and i[4] < 1.35 *rank and checkduration(i) :
        
        confirm.append(i)



for i in confirm:
    print(i)
print(123)
for i in chances:
    print(i)
    

conn.close()

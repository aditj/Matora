from flask import Flask,render_template, request
app = Flask(__name__)

from operator import itemgetter
#College Displayer With Details

##########################################################


def checkduration(i,strictdura,duration):
    if strictdura:
        if i[8] == duration:
            return True
        else : return False
    else : return True
def scorecal(i,dura_pref,duration,branch,hs, strictbranch):
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
        if strictbranch:
           
           if branch.lower() not in i[1].lower():
                
                i[9] *= 0
           


def solve(mains,adv,bits,manipal,branch,hs,duration,strictdura,dura_pref,strictbranch):  #branch,hs are str, ranks are int, dura_pref,strictboth are bools, duration int

    ranks = {'Mains':mains, 'Adv' : adv, 'BITSAT' : bits, 'MUOET' : manipal}   #rank (input by user)  order :jeemains ,jee advanced ,bits




    chances = []       #all college with a good chance of entrance
    confirm = []
            


                

            
    score  = 1  #temp name
    import sqlite3 
    conn = sqlite3.connect('data.db')  #use data.db file
    cursor = conn.execute("SELECT * from DATA")
    # homestate - 1.2, </html>
    for i in cursor:
        i = list(i)
        
        i.append(1)
        scorecal(i,dura_pref,duration,branch,hs, strictbranch)
        if i[9] == 0:
            continue
        
        rank = ranks[i[5]]
        if "bits" not in i[0].lower():
            

            if i[4] > 0.7*rank and i[4] < 1.1 *rank and checkduration(i,strictdura,duration)  :
                
                if i[2]=='AI' or i[2] == 'OS':
                    
                    chances.append(i)
                elif i[2] == hs:
                    chances.append(i)
            elif i[4] > 1.1*rank and i[4] < 1.35 *rank and checkduration(i,strictdura,duration) :
                if i[2]=='AI' or i[2] == 'OS':
                    
                    confirm.append(i)
                elif i[2] == hs:
                    confirm.append(i)
        
        else:
             if i[4] < rank + 10 and i[4] > rank - 10 and checkduration(i,strictdura,duration):
                chances.append(i)
             if i[4] < rank - 10 and i[4] > rank - 30 and checkduration(i,strictdura,duration):
                confirm.append(i)



    for i in confirm:
        for j in confirm:
            if i[0] == j[0] and i[1] == j[1] and i!=j:
                    
                    if i[2]=="OS":
                        del confirm[confirm.index(i)]
        
                    else:
                        del confirm[confirm.index(j)]

    for i in chances:
        for j in chances:
            if i[0] == j[0] and i[1] == j[1] and i!=j:
                
                if i[2]=="OS":
                    del chances[chances.index(i)]
                else:
                    del chances[chances.index(j)]

    confirm = sorted(confirm, key=itemgetter(9))
    chances = sorted(chances, key=itemgetter(9))
    confirm = confirm[::-1]
    chances = chances[::-1]

    return confirm,chances




@app.route('/')
def index():
   return render_template("index.html")

@app.route('/', methods=['POST'])
def indexpost():
    main = request.form['main']
    adv = request.form['adv']
    bit = request.form['bit']
    hs = request.form['hs']
    dura = request.form['dura']
    dp = request.form['dp']
    branch = request.form['branch']
    
    ds = request.form['ds']
    bs = request.form['bs']
    
    dp1=True
    ds1=True
    bs1 = True
    if dp=="False":
       dp1=False
    if ds=="False":
       ds1=False
    if bs=="False":
       bs1=False
    
    confirm,chances = solve(int(main),int(adv),int(bit),0,branch,hs,int(dura),ds1,dp1,bs1)
    
    return render_template("results.html",confirm = confirm, chances = chances)
    



if __name__ == '__main__':
   app.run(host='0.0.0.0', port=8082)

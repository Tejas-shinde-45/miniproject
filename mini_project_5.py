import json
class player:
    def __init__(self,name,run,ball):
        self.name=name
        self.run=run
        self.ball=ball
    
    def store(self):
        st=(self.run/self.ball) * 100
        stt=round(st,3)
        dist={}
        dist={"Name":self.name,
              "Runs":self.run,
              "Balls":self.ball,
              }
        dist["strike rate"]=stt
        return dist
liste=[]
Up=int(input("how many player scores runs:"))
for i in range(Up):
    print(f"__________Enter the detial of {i+1} Batsmans_____________")
    n=input("enter the name of the Batsman::")
    r=int(input("Batsman score runs::"))
    b=int(input("Batsman take Balls:"))
    
    p1=player(n,r,b)
    liste.append(p1.store())

#liste['d1','d2','d3','d4']
listenew=liste.sort(key=lambda dist:dist["strike rate"])
        


with open("playersdetails.json","w")as file:
    json.dump(liste,file,indent=4)


print("_______Batsman Detials______")
for i in liste:
    print(i)

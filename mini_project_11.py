import json

class Employee:
    def __init__(self):
        self.liss=[]
    
    def add_empoyee(self):
        n=int(input("enter the employee strenght:"))
        
        for e in range(n):
            dicc={}
            print("--" * 30)
            eid = int(input("enter the employee id:"))
            ename= input("emplyee name::")
            erole=input("enter the employee role::")
            salary= int(input("enter the salary if the employee:"))
            date=int(input("enter the date ::"))
            status=input("employee Present of Absent")
            dicc['eid']= eid
            dicc['ename'] =ename
            dicc['erole'] = erole
            dicc['salary']=salary
            dicc['date'] = date
            dicc['status']=status.capitalize()
            self.liss.append(dicc)
            return self.liss

    def check_attendance(self):
        for dicc in self.liss:
            if dicc["status"] == "Present":
                print(f" On {dicc['date']}, {dicc['ename']} was {dicc['status']}.")   
            else:
                print("employee not present")
    
    def tax_reduction(self,per):
        for dicc in self.liss:
            if dicc['salary'] >=20000:
                tax= (dicc['salary'] * per )/ 100
                news=dicc['salary'] - tax
                i=0
                print(f"total salary of{i+1} is :{news}")
                dicc["ns"]=news
                i+=1
            else:
                print("employee salary is no enough")

    def display(self):
        for emp in self.liss:
            print("employee id is:",emp['eid'])
            print("employee name is :",emp['ename'])
            print("employee role is:",emp['erole'])
            print("employee salary is :",emp['salary'])
            print("employee new salary is ",emp['ns'])

    def show_detail(self):
        self.display()

   

ep=Employee()
ep.add_empoyee()
ep.check_attendance()
ep.tax_reduction(7)
ep.show_detail()
with open("employee.json","w")as file:
    json.dump(ep.liss,file,indent=4)
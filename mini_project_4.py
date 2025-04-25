import json

class student:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def store(self):
        dicte={"name":self.name,
               "age":self.age,
               "gender":self.gender}
        return dicte
lieste=[]
cnt=int(input("How many student do you want in the book: "))
for i in range(cnt):
    print(f"__________Enter the detial of {i+1} candidate")
    n=input("enter the name of the student:")
    a=int(input("enter the age of the student:"))
    g=input("enter the gender of the student:")
    

    b1=student(n,a,g)
    lieste.append(b1.store())
    
with open("student.json","w")as file:
    json.dump(lieste,file,indent=4)
    
print("\nAll User Information saved to 'students.json'")

print("\nAll User Information:")
for user in lieste:
    print(user)


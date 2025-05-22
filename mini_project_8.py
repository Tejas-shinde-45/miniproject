#EMPLOYEE MANAGEMENT SYSTEM
class Empoyee:
    def __init__(self,e_id,name,salary):
        self.e_id=e_id
        self.name=name
        self.salary=salary      
    
    def display_prof(self):
        return f"employee id is {self.e_id}\nname of the Empoyee is:{self.name}\nsalary of the Empoyee is :{self.salary}"

class Manager(Empoyee):    
    def __init__(self, e_id, name, salary,dept):
        super().__init__(e_id, name, salary)
        self.dept=dept
        self.lis=[]
    
    def display_prof(self):
        return super().display_prof()+f"\ndepartment is:{self.dept}"
    
    def add_employee(self):
        
        n=int(input("enter the number that how many employee you want:"))
        for i in range(n):
            id=int(input("enter the id of the employee:"))
            na=input("enter the name of the student:")
            sal=int(input("enter the salary of the employee:"))
            dept=input("enter the name of dept:")
            manager=Manager(id,na,sal,dept)
            self.lis.append(manager)
        return self.lis

    def display_manager(self):
        print(super().display_prof())
        print(self.dept)  


    def display_list(self):
        for i in self.lis:
            i.display_manager()


class Devloper(Empoyee):

    def __init__(self,e_id,name,salary,language):
        super().__init__(e_id,name,salary)
        self.language=language
    
    def display_prof(self):
        return super().display_prof() + f"\ncoding language name is :{self.language}"
    

m=Manager(2,"tejas",345,"HR")
m.add_employee()
m.display_list()
m.display_prof()

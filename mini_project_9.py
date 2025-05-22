# TODO LIST
import json
import os

class todo:
    def __init__(self,tno,task,tday):
        self.tno=tno
        self.task=task
        self.tday=tday
    
    def displaytask(self):
        print("------------------------")
        print("task id is:",self.tno)
        print("task name is:",self.task)
        print("task day is:",self.tday)
    

class todooperation():
    def __init__(self):
        self.lis=[]
    
    def add_task(self):
        tn=int(input("Enter how many task do you have today:"))
        for i in range(tn):
            tno=int(input("Enter no of task--"))
            task=str(input("Enter the name of task--"))
            tday=str(input("Enter the task day:--"))
        
            tas=todo(tno,task,tday)
            self.lis.append(tas) 
        return self.lis
    
    def view_taks(self):
        print("\n-------ToDo List------------")
        if not self.lis:
            print("no task added:")
        for i in self.lis:
            i.displaytask()
    
    def update_task(self):
        oldt=input("enter the old task:")
        taske=input("enter the second task:")
        flag=0
        for i in self.lis:
            if i.task==oldt:
                i.task=taske
                i.displaytask()
                flag=1
                break
        if flag==0:
            print("Task not found------")

    def delete_task(self):
        flagg=0
        delt=input("Enter task name which is want to delete:")
        for i in self.lis:
            if i.task==delt:
                flagg=1
                self.lis.remove(i)
                print("Task delete Successfully..")
                break

        if flagg==0:
            print("task not found-----")
    
        for i in self.lis:
            i.displaytask()

to=todooperation()
while True:

    print("____________Welcome To Todolist_____________")
    print("1,Add Task")
    print("2,View task")
    print("3,Update task")
    print("4,Delete task")
    print("5,Exit todo")

    ch=input("enter your choice")

    if ch=='1':
        to.add_task()
    elif ch=='2':
        to.view_taks()
    elif ch=='3':
        to.update_task()
    elif ch=='4':
        to.delete_task()
    elif ch=='5':
        print("Exiting ToDo System. Goodbye!")
        break
    else:
        print("Your choice is invalid")



















           
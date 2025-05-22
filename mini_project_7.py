class student:
    def __init__(self,name,rollnum,marks):
        self.name=name
        self.rollnum=rollnum
        self.marks=marks

    def display(self):
        print(f"student name is::{self.name}")
        print(f"student rollnum::{self.rollnum}")
        print(f"student marks::{self.marks}")
    

class Sms():
    def __init__(self):
        self.lis=[]
    #     super().__init__(name, rollnum, marks)

    def add_student(self):
        h=int(input("how many student you want to put int he list:"))
        for i in range(h):
            name=input("Name:")
            rollnum=int(input("Rollnum::"))
            marks=int(input("Marks::"))

            student_obj=student(name,rollnum,marks)
            self.lis.append(student_obj)
        return self.lis
    
    def view_student(self):
        for i in self.lis:
            i.display()

    def search_student(self):
        roll=int(input("Rollnumber for finding the:"))
        flag=0 # flag variable use only for checking and if certain condition met to the output.
        for i in self.lis:
            if i.rollnum==roll:
                print("rollnumber is valid:")
                i.display()
                flag=True
                break
        if not flag:
                print("student are not present in the list")

    def update_student(self):
        us=input("which student you want to update:")
        new=input("entre the new name of student:")
        flag=0
        for i in self.lis:
            if i.name==us:
                i.name=new
                i.display()
                flag = True
                break
s=Sms()
while True:
    # 1. Show menu
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student Marks")
    print("5. Exit")

    # 2. Take choice
    choice = input("Enter your choice (1-5): ")

    # 3. Process choice
    if choice == '1':
        s.add_student()
    elif choice == '2':
        s.view_student()
    elif choice == '3':
        s.search_student()
    elif choice == '4':
        s.update_student()
    elif choice == '5':
        print("Exiting Student Management System. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
import json
import os

def save_to_file(students, filename="students.json"):
    data = {}
    for rollno, student in students.items():
        data[rollno] = {
            "name": student.name,
            "rollno": student.rollno,
            "marks": student.marks
        }
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
    print("Data saved to file.")

def load_from_file(filename="students.json"):
    students = {}
    if os.path.exists(filename):
        with open(filename, "r") as f:
            data = json.load(f)
            for rollno_str, student_data in data.items():
                rollno = int(rollno_str)
                student = Grade_student(student_data["name"], rollno)
                student.marks = student_data["marks"]
                students[rollno] = student
        print("Data loaded from file.")
    return students
class Student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
        self.marks={}
    
    def add_result(self,subject,score):
        self.marks[subject]=score
    
    def update_marks(self, subject, score):
        if subject in self.marks:
            self.marks[subject] = score
            print(f"Updated {subject} to {score}.")
        else:
            print(f"{subject} not found in student's record.")
    
    def calculate_avg(self):
        if not self.marks:
            return 0
        total=sum(self.marks.values())    
        return total / len(self.marks)

    def display_report(self):
        print("\n--- Student Report ---")
        print("Name:", self.name)
        print("Roll No:", self.rollno)
        print("Marks:")
        for subject, score in self.marks.items():   # printing the values of the dictionaries using for loop....
            print(f"  {subject}: {score}")
        print("Average:", self.calculate_avg())
        print(self.marks)

class Grade_student(Student):
    def __init__(self, name, rollno):
        super().__init__(name, rollno)
    
        
    def assign_grade(self):
        avg=self.calculate_avg()
        if  avg>=90:
            return "A"
        elif 80 < avg <89:
            return "B"
        elif 70<avg <79:
            return "C"
        elif 60<avg <69:
             return "D"
        elif avg <59:
            return "F"
students={}
students = load_from_file()
# Main loop
while True:
    print("\n===== Student Report System =====")
    print("1. Add Student")
    print("2. Add/Update Marks")
    print("3. Search Student by Roll Number")
    print("4. Display All Reports")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter student name: ")
        rollno = int(input("Enter roll number: "))
        if rollno in students:
            print("Student already exists!")
        else:
            student = Grade_student(name, rollno)
            students[rollno] = student
            print("Student added successfully.")

    elif choice == '2':
        rollno = int(input("Enter roll number: "))
        if rollno in students:
            subject = input("Enter subject: ")
            score = int(input("Enter marks (0-100): "))
            students[rollno].add_result(subject, score)
            print("Marks added/updated.")
        else:
            print("Student not found.")

    elif choice == '3':
        rollno = int(input("Enter roll number to search: "))
        if rollno in students:
            students[rollno].display_report()
            print("Grade:", students[rollno].assign_grade())
        else:
            print("Student not found.")

    elif choice == '4':
        if not students:
            print("No students in record.")
        else:
            for student in students.values():
                student.display_report()
                print("Grade:", student.assign_grade())

    elif choice == '5':
        save_to_file(students)
        print("Exiting system. Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")

class Student:
    def __init__(self,name,ID,age,grade):
        self.name=name
        self.ID=ID
        self.age=age
        self.grade=grade
    def calculate_average(self,grade):
        total=sum(grade)
        average=total/len(grade)
        return average
    def is_passed(self,marks):
        average=self.calculate_average(marks)
        if average>=50:
            print(f"{self.name} has passed with an average of {average}.")
        else:
            print(f"{self.name} has failed with an average of {average}.")
    def display_info(self):
        print(f"Name: {self.name}, ID: {self.ID}, Age: {self.age}, Grade: {self.grade}")
students=[]
class studentSystem:
    def add_student(self,name,ID,age,grade):
        for student in students:
            if student.ID==ID and student.name==name:
                print("Student already exists.")
                return
        new_student=Student(name,ID,age,grade)
        students.append(new_student)
        print(f"Student {name} added successfully.")
    def find_student(self,ID):
        for student in students:
            if student.ID==ID:
                return student
        return "Student not found."
    def display_all_students(self):
        if not students:
            print("No students available.")
        else:
            for student in students:
                student.display_info()
def main():
    system=studentSystem()
    while True:
        print("1. Add Student")
        print("2. Find Student by ID")
        print("3. Display All Students")
        print("4. Calculate Average and Pass Status")
        print("5. Exit")
        choice=input("Enter your choice (1-5): ")
        if choice=='1':
            name=input("Enter student's name: ").capitalize()
            ID=input("Enter student's ID: ")
            age=input("Enter student's age: ")
            grade_input=input("Enter student's grades separated by commas: ")
            grade=[float(g) for g in grade_input.split(',')]
            system.add_student(name,ID,age,grade)
        elif choice=='2':
            ID=input("Enter student's ID to find: ")
            student=system.find_student(ID)
            if student!="Student not found.":
                student.display_info()
            else:
                print(student)
        elif choice=="3":
    
            system.display_all_students()
        elif choice=="4":
            ID=input("Enter student's ID: ")
            student=system.find_student(ID)
            if student!="Student not found.":
            
                student.is_passed(student.grade)
            else:
                print(student)
        elif choice=="5":
            print('Good bye!')
            break
main()
        

            
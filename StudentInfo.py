# This is a simple student information management system using file handling in Python.It connects to Student.txt file.
def add_student():
    ID=input("Create an ID for the student:")
    name=input("Student's name:")
    grade=input("Student's grade:")
    with open("Student.txt","a") as f:
        f.write(f" {ID} {name} {grade} {"\n"}")
        print("Student added")
def Search_Student():
    ID=input("Enter student's ID you want to search:")
    with open("Student.txt","r") as lines:
     
     for line in lines:
        data=line.strip().split()
        if data[0]==ID:
           print('Student found')
           print(f" Student's ID: {data[0]}; student's name: {data[1]}; Student's grade: {data[2]}")
           return
     print("Student not found")
def Display_All_Students():
   with open("Student.txt","r") as file:
        lines=file.readlines()
        for line in lines:
         print(line,end="")
def Detete_Student( ):
   ID=input("Enter student's ID you want to delete:")
   with open("Student.txt","r") as file:
         lines=file.readlines()
   remainning_students=[]
   found=False
   for line in lines:
      data=line.strip().split()
      if data[0]==ID:
         found=True
         
      else:
         remainning_students.append(line)    
   if found:
      with open("Student.txt","w") as file:
         file.writelines(remainning_students)
      print("Student deleted")
   else:
      print("Student not found")

def main():
   while True:
      print("\n My Students Storage")
      print("Type 1 to add student")
      print("Type 2 to search for a student")
      print("Type 3 to display all students")
      print("Type 4 to delete a student")
      print("Type 5 to quit")
      choice=input("Type 1-5:")
      if choice=="1":
         add_student()
      elif choice=="2":
         Search_Student()
      elif choice=="3":
         Display_All_Students()
      elif choice=="4":
         Detete_Student()
      elif choice=="5":
         print("You quit")
         break
main()
         



    



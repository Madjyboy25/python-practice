students_infos={}
def add_student(name, ID, age, grade):
    if name in students_infos:
        print(f"Student {name} already exists.")
        return
    else:
     students_infos[name] = {'ID': ID, 'age': age, 'grade': grade}
def add_student_note(name, note):
    if name in students_infos:
        # If the student doesn't have notes yet, create a list
        if 'note' not in students_infos[name]:
            students_infos[name]['note'] = []

        # Add the new note to the list
        students_infos[name]['note'].append(note)

        print(f"Note added to student {name}.")
    else:
        print(f"Student {name} not found.")

def get_student_report(name):
    if name in students_infos:
        info = students_infos[name]
        print(f"Student's name: {name}")
        print(f"Student's grade: {info['grade']}")
        print(f"Student's age: {info['age']}")

        if 'note' in info and info['note']:
            print("Student's notes:")
            for note in info['note']:
                print(f"- {note}")
        else:
            print("No notes available for this student.")
    else:
        print(f"Student {name} not found.")


def get_all_students():
    if not students_infos:
        print("No students available.")
    else:
        for name, info in students_infos.items():
            notes = info.get('note', 'No notes available')
            print(f"Name: {name}, Age: {info['age']}, Grade: {info['grade']}, Notes: {notes}")
def main():
    while True:
        print("1. Add Student")
        print("2. Add Note to Student")
        print("3. Get Student Report")
        print("4. Get All Students")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")
        if choice == '1':
            name = input("Enter student's name: ").capitalize()
            ID=input("Enter student's ID: ")
            age = input("Enter student's age: ")
            grade = input("Enter student's grade: ")
            add_student(name, ID, age, grade)
            print(f"Student {name} added.")
        elif choice == '2':
            name = input("Enter student's name to add note: ").capitalize()
            note=input("Enter subject and note. for example, math:40 :")

            add_student_note(name, note)
            
        elif choice == '3':
            name = input("Enter student's name to get report: ").capitalize()
            get_student_report(name)
        elif choice == '4':
            get_all_students()
        elif choice == '5':
            break
        else:
            print("Invalid choice, Please try again! Type a number between 1-5.")
main()
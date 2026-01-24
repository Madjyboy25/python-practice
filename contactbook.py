# This is a simple contact book management system using functions and dictionaries in Python.
contacts={}
def add_contact(name, phone, ID):
    if name and phone and ID  not in contacts:
        contacts[ID]={'name':name, 'phone':phone, 'ID':ID}
        print( f"{name} is added to the contact list!")
    else:
        print( f"{name} is in the contact list  already.")
def search_contact(name,ID):
    if ID in contacts:
        print(f"{name} is in the contact list and his/her phone number is {contacts[ID]['phone']} ")
    else:
        print(f"{name} is not found.")
def remove_contact(name,ID):
    if name and ID in contacts:
        contacts.pop(ID)
        print( f"{ name } is removed")
    else:
        print( f"{name} is not found")

def display_all_contacts():
    if contacts:
        for  value in contacts.values():
            print("Name:",value['name'])
            print("Phone number is:",value['phone'])
            print("ID:",value['ID'])
def display_choice():
    while True:
        print("\n Welcome to The Contact List")
        print("How can I help you today? See the option below!")
        options=["1-Add contact","2-Search Contact","3-Delete Contact","4-Display All Contacts","5-Exit"]
        for option in options:
            print(option)
        choices=input("Choose one option. Please type number only look at which number that correspond with your choice (1-5):")
        if choices=="1":
            name=input("Enter name:").capitalize()
            phone=input("Enter phone number:")
            ID=input("Create an ID:")
            add_contact(name,phone,ID)
        elif choices=="2":
            name=input("Enter name:").capitalize()
            ID=input("Enter ID:")
            search_contact(name,ID)
        elif choices=="3":
            name=input("Enter name: ").capitalize()
            ID=input("Enter ID:")
            remove_contact(name,ID)
        elif choices=="4":
            display_all_contacts()
        elif choices=="5":
            print("Bye see you next time!")
            break
        else:
            print("Invalid input. Please type a number 1-4.")
display_choice()
            
            

    
            




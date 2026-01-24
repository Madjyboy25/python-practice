# This a simple calculator using functions and error handling in Python.
def add(num1,num2):
    return num1+num2
def subtract(num1,num2):
    return num1-num2
def multiply(num1,num2):
    return num1*num2
def divide(num1,num2):
    try:
     div=num1/num2
    except:
       print("Error:You Cannot divide a number by zero")
def main():
   while True:
      print("\n Wecolme to The Simple Calculator")
      print("Press 1 to add")
      print("Press 2 to subtract")
      print("Press 3 to multiply")
      print("Press 4 to divide")
      print("Press 5 to quit")
      choice= input("Enter (1-5):")
      if choice=="1":
         num1=float(input("Enter first number:"))
         num2=float(input("Enter second number:"))
         print("Resut:",add(num1,num2))
      elif choice=="2":
         num1=float(input("Enter first number:"))
         num2=float(input("Enter second number:"))
         print("Result:",subtract(num1,num2))
      elif choice=="3":
         num1=float(input("Enter first number:"))
         num2=float(input("Enter second number:"))
         print("Result:",multiply(num1,num2))
      elif choice=="4":
         
         num1=float(input("Enter first number:"))
         num2=float(input("Enter second number:"))
         print("Result:",divide(num1,num2))
      elif choice=="5":
         print("Wish I have solved your operations")
         break
      else:
         print("Invalid option type a num 1-5!")
main()

         
        
          

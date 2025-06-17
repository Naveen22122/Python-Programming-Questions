24 python program to make a simple calculator.
.................................................

num1=float(input("enter the given num1:"))
num2=float(input("enter the given num2:"))
print("press 1 for addition \n press 2 for subraction \n press 3 for multiplication\n press 4 for division")
choice = int(input("enter your choice 1-4: "))
if choice==1:
    print("the sum of two numbers is:",num1+num2)
elif choice==2:
    print("the sub of two numbers is:",num1-num2)
elif choice==3:
    print("the mul of two numbers is:",num1*num2)
elif choice==4:
    print("the div of two numbers is:",num1%num2)

output:
        enter the given num1:12
        enter the given num2:12
        press 1 for addition 
         press 2 for subraction 
         press 3 for multiplication
         press 4 for division
        enter your choice 1-4: 1
        the sum of two numbers is: 24.0
        
        === Code Execution Successful ===

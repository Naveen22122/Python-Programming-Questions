09 python program to find the largest number among three numbers
........................................................................
num1=int(input("enter the given num1:"))
num2=int(input("enter the given num2:"))
num3=int(input("enter the given num3:"))
if (num1>num2) and (num1>num3):
    print(num1,"is the largest number among three numbers")
elif (num2>num1) and (num2>num3):
    print(num2,"is the largest number among three numbers")
else:
    print(num3,"is the largest number among three numbers")

output:
       enter the given num1:121
       enter the given num2:71
       enter the given num3:45
       121 is the largest number among three numbers

=== Code Execution Successful ===

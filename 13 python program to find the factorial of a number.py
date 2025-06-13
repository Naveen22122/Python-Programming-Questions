13 python program to find the factorial of a number
......................................................
(method1=using for loop)

num=int(input("enter the given num:"))
fact=1
if num<0:
    print("the factorial does not exists")
if num==0:
    print("the factorial of 0 is",1)
if num>0:
    for i in range(1,num+1):
        fact=fact*i
print("the factorial of the given number is",fact)

output:
       enter the given num:9
       the factorial of the given number is 362880
...............................................................
(method2-using recursion)

def fact(a):
    if a==0:
        return 1
    else:
        return a*fact(a-1)
num=int(input("enter the given number:"))
result=fact(num)
print("the factorial of the given number is",result)

output:
enter the given number:4
the factorial of the given number is 24

=== Code Execution Successful ===
..........................................................................

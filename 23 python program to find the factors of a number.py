23 python program to find the factors of a number.
....................................................
num=int(input("enter the given number:"))

for i in range(1,num+1):
    if num%i==0:
        print("the factors of num is ", i)

output:
        enter the given number:12
        the factors of num is  1
        the factors of num is  2
        the factors of num is  3
        the factors of num is  4
        the factors of num is  6
        the factors of num is  12
        
        === Code Execution Successful ===

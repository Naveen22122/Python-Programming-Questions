26 python program to display fabinacci sequence using recursion.
.................................................................
def fibo(num):
    if num<=1:
        return num
    else:
       return (num-1)+(num-2)
num=int(input("enter the given number:"))
if num<=0:
    print("enter the positive number")
else:
    for i in range(num):
        print(fibo(i))

output:
        enter the given number:5
        0
        1
        1
        3
        5
        
        === Code Execution Successful ===

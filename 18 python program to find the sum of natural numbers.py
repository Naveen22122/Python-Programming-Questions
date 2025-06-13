18 python program to find the sum of natural numbers
.......................................................
num=int(input("enter the given number:"))
if num<0:
    print("enter positive number")
else:
    sum=0
    while num>0:
        sum+=num
        num-=1
    print(sum)

output:
        enter the given number:5
        15
        
        === Code Execution Successful ===

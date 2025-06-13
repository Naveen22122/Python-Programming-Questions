17 python program to print all the armstrong numbers in an interval
.....................................................................
lower=int(input("enter the lower value of the number:"))
upper=int(input("enter the upper value of the number:"))

for num in range(lower,upper+1):
    sum=0
    order=len(str(num))
    temp=num
    while temp>0:
        digit=temp%10
        sum+=digit**order
        temp//=10
    if num==sum:
        print(num)

output:
        enter the lower value of the number:100
        enter the upper value of the number:1000
        153
        370
        371
        407
        
        === Code Execution Successful ===

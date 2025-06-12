11 python program to print all the prime numbers in an interval
...................................................................
lower=int(input("enter the lower value:"))
upper=int(input("enter the upper value:"))
for num in range(lower,upper+1):
    if num>1:
        for i in range(2,num):
            if num%i == 0:
                break
        else:
            print(num)

output: 
        enter the lower value:10
        enter the upper value:50
        11
        13
        17
        19
        23
        29
        31
        37
        41
        43
        47

=== Code Execution Successful ===

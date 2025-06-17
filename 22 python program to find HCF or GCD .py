22 python program to find HCF or GCD .
..........................................
def findHCF(x,y):
    if x>y:
        smaller=y
    else:
        smaller=x
    for i in range(1,smaller+1):
        if (x%i==0) and (y%i==0):
            HCF=i
    return HCF
x=20
y=30

print("the hcf of the given two numbers is:",findHCF(12,30))

output:
        the hcf of the given two numbers is: 6
        
        === Code Execution Successful ===

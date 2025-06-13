16 python program check given number is armstrong number or not
................................................................
num=int(input("enter the given number:"))
sum=0
temp=num
while temp>0:
    digit=temp%10
    cube=digit**3          {we dont need cube step instead sum+=digit**3}
    sum=sum+cube        
    temp//=10
if sum==num:
    print("it is an armstrong number")
else:
    print("it is not an armstrong number")

output:
        enter the given number:153
        it is an armstrong number
        enter the given number:163
        it is not an armstrong number
        
        === Code Execution Successful ===

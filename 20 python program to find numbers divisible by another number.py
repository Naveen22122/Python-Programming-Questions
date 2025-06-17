20 python program to find numbers divisible by another number.
..................................................................
#for loop codition
print("the numbers divisible by 13 is:")
for i in range(1,100):
    if i%13==0:
        print(i)
        
#using lambda function and filter function
l=[13,39,25,56,775,88,95]
result=list(filter(lambda x:x%13==0,l))
print("the numbers divisible by 13 is:",result)

output:
        #for loop output      
        the numbers divisible by 13 is:
        13
        26
        39
        52
        65
        78
        91
        #using lambda function and filter function output
        the numbers divisible by 13 is: [13, 39]
        
        === Code Execution Successful ===

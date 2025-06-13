15 python program to print the fabinacci sequence
...................................................
a=0
b=1
num=int(input("enter the given number to obtain fabinacci sequence:"))
if num==0:
    print(a)
if num==1:
    print(b)
else:
    for i in range (1,num+1):
        c=a+b
        a=b
        b=c
        print("the fabinacci sequence of a number is",c)

  output:
          enter the given number to obtain fabinacci sequence:7
          the fabinacci sequence of the number is 1
          the fabinacci sequence of the number is 2
          the fabinacci sequence of the number is 3
          the fabinacci sequence of the number is 5
          the fabinacci sequence of the number is 8
          the fabinacci sequence of the number is 13
          the fabinacci sequence of the number is 21
          
          === Code Execution Successful ===

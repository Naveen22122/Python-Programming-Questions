10 python program to check prime number
......................................................
num=int(input("enter the given number:"))
if num==1:
    print(num,"it is not a prime number")
if num>1:
    for i in range(2,num):
        if num%i == 0:
            print("it is not a prime number")
            break
    else:
        print("it is a prime number")

  output:  
          enter the given number:11
          it is a prime number
                 or
          enter the given number:8
          it is not a prime number
........................................................

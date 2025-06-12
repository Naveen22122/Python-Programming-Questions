1)python program to find the square root of the given number
...............................................................................    
(method1-Exponential operation)

num=81
num1=int(input("enter the given num1: "))
sr=num1**(1/2)
print("the square root of the given number is", sr)

output:  
      enter the given num1: 81
      the square root of the given number is 9.0
.................................................................................
    (method2-math module)

import math
num=int(input("enter the given number:"))
sr=math.sqrt(num)
print("the square root of the given number is", sr) 

output: 
      enter the given number:81
      the square root of the given number is 9.0

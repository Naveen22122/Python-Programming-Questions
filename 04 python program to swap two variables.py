04 python program to swap two variables
....................................................
(method1-using third variable)

x=20
y=30
temp=x
print("the temp variable is",temp)
x=y
print("the value of x is",x)
y=temp
print("the value of y is",y)

output:
      the temp variable is 20
      the value of x is 30
      the value of y is 20
......................................................
(method2=without using third variable)

x=20
y=30
x,y=y,x
print("the value of x is",x)
print("the value of y is",y)

output: 
      the value of x is 30
      the value of y is 20

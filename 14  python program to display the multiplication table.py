14  python program to display the multiplication table
.......................................................
(method1-for loop)

num=int(input("enter the given number:"))
for i in range(1,11):
    print(num,"x",i,"=",num*i)

output: 
       enter the given number:3
        3 x 1 = 3
        3 x 2 = 6
        3 x 3 = 9
        3 x 4 = 12
        3 x 5 = 15
        3 x 6 = 18
        3 x 7 = 21
        3 x 8 = 24
        3 x 9 = 27
        3 x 10 = 30
..........................................................
(method2-while loop)

  num=int(input("enter the given number:"))
i=1
while i<=10:
    print(num,"x",i,"=",num*i)
    i+=1

output:
      enter the given number:4
      4 x 1 = 4
      4 x 2 = 8
      4 x 3 = 12
      4 x 4 = 16
      4 x 5 = 20
      4 x 6 = 24
      4 x 7 = 28
      4 x 8 = 32
      4 x 9 = 36
      4 x 10 = 40
      
      === Code Execution Successful ===

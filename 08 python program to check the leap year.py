08 python program to check the leap year
............................................
year=int(input("enter the given year:"))
if (year%400==0) and (year%100==0):
    print(year,"is a leap year")
elif (year%4==0) and (year%100!=0):
    print(year,"is a leap year")
else:
    print(year,"is not a leap year")

output:
      enter the given year:2000
      2000 is a leap year  
             or
      enter the given year:2004
      2004 is a leap year
            or
      enter the given year:2006
      2006 is not a leap year
..................................................

25 python program to display the calendar.
...........................................
import calendar
year=int(input("enter the year:"))
month=int(input("enter the month:"))
calendar=calendar.month(year,month)
print(calendar)

output:
        enter the year:2002
        enter the month:10
            October 2002
        Mo Tu We Th Fr Sa Su
            1  2  3  4  5  6
         7  8  9 10 11 12 13
        14 15 16 17 18 19 20
        21 22 23 24 25 26 27
        28 29 30 31
        
        
        === Code Execution Successful ===

19 python program to display the power of 2 using anonymous function.
........................................................................
nterms=int(input("enter the number of terms:"))
result=list(map(lambda x:2**x, range(nterms+1)))
print(result)  # we can do upto this list function method
for i in range(nterms+1):
    print("the power 2 is raised for", i,"is",result[i])

output:
        enter the number of terms:5
        [1, 2, 4, 8, 16, 32]
        the power 2 is raised for 0 is 1
        the power 2 is raised for 1 is 2
        the power 2 is raised for 2 is 4
        the power 2 is raised for 3 is 8
        the power 2 is raised for 4 is 16
        the power 2 is raised for 5 is 32
        
        === Code Execution Successful ===
            
...........................................................

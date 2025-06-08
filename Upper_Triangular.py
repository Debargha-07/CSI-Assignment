row_no=int(input("Enter the number of rows :"))
for i in range(row_no):
    for j in range(i):
        print(" ",end="")
    for k in range(row_no-i):
        print("*",end="")    
    print()    
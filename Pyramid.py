row_no=int(input("Enter the number of rows :"))
for i in range(row_no):
    for j in range(row_no-i-1):
        print(" ",end="")
    for k in range(2*i+1):
        print("*",end="")
    print()        
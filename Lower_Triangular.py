row_no=int(input("Enter the number of rows :"))
for i in range(1,row_no+1):
    for j in range(i):
        print("*",end="")
    print()    
n=int(input("Enter the no: of lines: "))
for i in range(1,n+1):
    for j in range(1,n+1):
        if j >=i:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

for k in range(n - 1, 0, -1):
    for j in range(1, n + 1):
        if j >= k:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

        

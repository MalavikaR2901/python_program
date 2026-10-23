# n = int(input("Enter no: of rows: ")) #5
# for i in range (1,n+1):  #1 2 3
#     for j in range (n,0,-1):
#         if j>i:
#             print(" ",end=" ")
#         else:
#             print("*",end=" ")
#     print()

# n = int(input("Enter no: of rows: ")) #5
# for i in range (n,0,-1):  #1 2 3
#     for j in range (1,n+1):
#         if i<=j:
#             print(j,end=" ")
#         else:
#             print(" ",end=" ")
#     print()

n = int(input("Enter no: of rows: ")) #5
for i in range (n,0,-1):  #1 2 3
    for j in range (1,n+1):
        if i<=j:
            print(i,end=" ")
        else:
            print(" ",end=" ")
    print()
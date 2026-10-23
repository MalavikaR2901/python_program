#steps to take for these pattern problems
# - Check whether it is left oriented or right oriented
# - Check whether it is direct or inverted pattern
# - Find which value we need to put i or j


# n=int(input("Enter the count: "))
# for i in range(1,n+1): #1 2
#     for j in range(1,n+1): #1 2
#         if j>=i: #1 >= 1
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# n=int(input("Enter the count: "))
# for i in range(n,0,-1):
#     for j in range(n,0,-1):
#         if i>=j:
#             print(i,end=" ")
#     print()

n=int(input("Enter the number of lines: "))
for i in range(1,n+1):
    for j in range(n,0,-1):
        if j > i:
            print(" ",end=" ")
        else:
            print(j,end=" ")
    for k in range(2,i+1):
        print(k, end=" ")
    print(" ")
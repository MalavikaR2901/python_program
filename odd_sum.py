n = int(input("Enter a number: "))
count = 1
sum = 0

while count <= n:
    sum = sum + count
    count = count + 2

print("Sum of odd numbers is", sum)
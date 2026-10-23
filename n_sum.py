n = int(input("Enter a number: "))
count = 1
sum = 0

while count <= n:
    sum = sum + count
    count = count + 1

print("Sum of natural numbers is", sum)
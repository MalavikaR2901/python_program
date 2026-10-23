n = int(input("Enter a number: "))
count = 2
sum = 0

while count <= n:
    sum = sum + count
    count = count + 2

print("Sum of even numbers is", sum)
n = int(input("Enter the number: "))
count = 1
sum = 0
while count<= n:
    if n % count == 0:
        sum = sum + count
    count = count + 1

print("Sum of factors is", sum)
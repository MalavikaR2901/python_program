num = int(input("Enter the number: "))
sum_even = 0
while num > 0:
    digit = num % 10
    if digit % 2 == 0:
        sum_even += digit
    num = num // 10
print("Sum of even digits is ",sum_even)


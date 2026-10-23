num = int(input("Enter the number: "))
sum_odd = 0
while num > 0:
    digit = num % 10
    if digit % 2 != 0:
        sum_odd += digit
    num = num // 10
print("Sum of odd digits is ",sum_odd)


num = int(input("Enter the number: "))     #9
square = num * num     #9 * 9 = 81
sum_digit = 0  
while square > 0:   #81 > 0
    digit = square % 10    #digit = 81 % 10 = 1
    sum_digit += digit     #sum_digit = sum_digit + digit = 0 + 1
    square = square // 10  #to remove last digit, we use floor division method = 81 // 10 = 8. After this the digit send to while loop starting
if sum_digit == num: 
    print("Neon number")
else:
    print("Not a neon number")
n = int(input("Enter a number: "))   # let n = 20
count = 1   #starting from 1
while count <= n:      #1 < 20
    if n % count == 0:   #20 % 1 = 0
        print(count) 
        count = count + 1  #count = 1 + 1 = 2

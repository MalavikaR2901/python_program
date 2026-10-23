#fibonacci concept 
# take numbers 0 and 1 => 0 + 1 = 1
# form 0 1 1 => 1 + 1 = 2
#form 0 1 1 2 => 1 + 2 = 3
#form 0 1 1 2 3


n = int(input("Enter the number of terms: "))

a = 0
b = 1
count = 1

while count <= n:
    print(a)
    
    c = a + b
    a = b
    b = c
    
    count = count + 1
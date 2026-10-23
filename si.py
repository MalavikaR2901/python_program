pa = int(input("Enter principal amount: "))
if pa > 15000:
    rate = 0.15
else:
    rate = 0.20
n = 20
si = (pa * rate * n) / 100
print("Simple Interest is:", si)
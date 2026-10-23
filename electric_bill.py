U = int(input("Enter no: of units: "))

if U>=1 and U<=100:
    bill = U * 10
elif U>100 and U<=200:
    bill = U * 15
elif U>200 and U<=300:
    bill = U * 20
else:
    bill = U * 25 
print ("The electricity bill amount is:", bill)
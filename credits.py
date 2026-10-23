#WAP 
credit= int(input("Enter your credit score: "))
if credit <= 23:
    print("fresher")
elif credit >= 24 and credit <=53:
    print("fresher")
elif credit >= 54 and credit <= 83:
    print("sophomore")
else:
    print("senior")
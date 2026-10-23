age = int(input("Enter your age: "))
citizen = input("Are you a citizen? (yes/no): ").lower() == "yes"
if age >= 18:
    if citizen:
         print("You are eligible to vote.")
    else:
         print("You must be a citizen to vote.")
else:
    print("You are not old enough to vote.")
#Write a program that repeatedly asks the user for a password until the correct one (python123) is entered.
#Use else statement to print a success message when the loop completes.

pw = input("Enter the password: ")
correct_pw = "python123"
while pw != correct_pw:
    print("Password is incorrect")
    pw = input("Enter the password: ")
else:
    print("Password is correct")


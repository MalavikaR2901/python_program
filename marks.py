#Write a program to display grade of a student. (read marks for 3 subjects, Find total, percentage, then grade)

sub_1 = int(input("Enter the subject 1 mark: "))
sub_2 = int(input("Enter the subject 2 mark: "))
sub_3 = int(input("Enter the subject 3 mark: "))

total = sub_1 + sub_2 + sub_3

percentage = (total / 300 ) * 100

if percentage > 80:
    print("A grade")

elif percentage >= 60 and percentage < 80 :
    print("B grade")
else :
    print ("C grade")
       
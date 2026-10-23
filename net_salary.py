#Write a program to find net salary of an employee based on the following condition:
#If basic salary is less than 15000then hra = 15% of bs, da = 17% of bs pf = 19% of bs. If basic salary 
#is in between 15001 and 25000 then hra = 7% of bs, da = 9% of bs, pf = 10% of bs,otherwise hra = 5% of bs
# da = 7% of bs pf = 8% of bs

basic_salary = int (input("Enter the basic salary: "))
if basic_salary < 15000:
    hra = 0.15 * basic_salary
    da = 0.17 * basic_salary
    pf = 0.19 * basic_salary
elif basic_salary >= 15001 and basic_salary <= 25000:
    hra = 0.07 * basic_salary
    da = 0.09 * basic_salary
    pf = 0.10 * basic_salary
else:
    hra = 0.05 * basic_salary
    da = 0.07 * basic_salary
    pf = 0.08 * basic_salary

net_salary = (basic_salary + hra + da) - pf
print ("Net salary of an employee is ", net_salary)


































    
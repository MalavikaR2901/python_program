for i in "malavika":
    print(i)

for i in range (1,10):
    print(i)

for i in range(1,10,2):
    print(i)

for i in range (10):
    print(i)

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
     print(fruit)

name = "Python"
for letter in name:
    print (letter)

numbers = (1, 2, 3)
for num in numbers:
    print(num)

person = {"name": "Alice", "age":"25"}
for key, value in person.items():
    print(key,":", value)

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row in matrix:
    for number in row:
        print(number, end=" ")
    print()

n = int(input("enter the number: "))
for i in range(1,n+1):
    print(n)
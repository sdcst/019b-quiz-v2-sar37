"""
Write a program that uses a for loop.
Each iteration will ask the user to enter a name
Add the input to the provided list
"""
names = []

for i in range(5):
    n = input("enter a name")
    names.append(n)
    print(names)
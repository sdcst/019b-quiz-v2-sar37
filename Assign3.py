#!python3
"""
Write a program that sorts the values in this list and prints
the 3 highest numbers. You may use multiple print statements,
but you should try to incorporate a for loop and use 1 print
statement instead.
"""
numbers = [3,4,6,1,3,6,12,33,15,2,22,9,17]

for i in range(3):
    x = sorted(numbers)
print(x)

#numbers.sort(numbers)
    #a = a + 1
# Write a Python program that reads a list of numbers and finds the sum of all even numbers in the list using a for loop and if statement.
numbers: list[int] = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
total: int = 0

for i in numbers:
    total += (i if (i % 2 == 0) else 0)

print(total) 
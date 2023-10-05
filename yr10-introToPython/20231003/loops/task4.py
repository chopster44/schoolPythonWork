num: int = int(input("Enter a non-negative integer: "))

factorial: int = 1
i = 1

while i <= num:
    factorial *= i
    i += 1

print(f"Factorial of {num} is {factorial}")

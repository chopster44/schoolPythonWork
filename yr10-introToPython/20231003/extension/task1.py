n: int = int(input("Enter a number to start the Fibonacci sequence: "))

fib: list[int] = [0, 1]

while fib[-1] < n:
    fib.append(fib[-1] + fib[-2])

print(fib)

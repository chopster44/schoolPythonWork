num: int = 0
while num <= 0:
    num = int(input("Enter num1 positive integer: "))

num1: int = 0
num2: int = 1

if num == 1:
    print(num1)
else:
    print(num1)
    print(num2)
    for i in range(2, num):
        num3: int = num1 + num2
        print(num3)
        num1 = num2
        num2 = num3

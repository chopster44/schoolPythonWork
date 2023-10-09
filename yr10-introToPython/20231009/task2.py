startNum: int = int(input("Enter a number: "))
prevNum: int = startNum
for i in range(3):
    print(prevNum)
    prevNum = prevNum *startNum

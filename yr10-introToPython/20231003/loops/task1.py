from time import sleep
startNum: int=int(input("Start the countdown at: "))
while startNum > 0:
    print(startNum)
    startNum-=1
    sleep(1)
print("Blast off!")
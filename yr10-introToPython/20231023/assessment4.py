total: int = 0
for i in range(5):
    number: int = int(input("Enter a number: "))
    add: str = str(input("Do you want this number included? [Y/n] ")).lower()
    if add == "y":
        total += number
    else:
        continue
print(total)
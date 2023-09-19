age: int = int(input("What is your age? "))
salary: int = int(input("What is your salary? "))
if age >= 21:
    if salary >= 10000:
        print("You can rent a flat")
    elif 0 < salary < 1000:
        print("Not enough money, if you have a guarantor you can rent.")
        guarantorBool: str = str(
            input("Do you have a guarantor?[y/n] ")).lower()
        if guarantorBool == "y":
            print("You can rent a flat")
        else:
            print("No flat for you")
elif 16 < age < 21:
    if 0 < salary < 1000:
        print("Not old enough, if you have a guarantor you can rent.")
        guarantorBool: str = str(
            input("Do you have a guarantor?[y/n] ")).lower()
        if guarantorBool == "y":
            print("You can rent a flat")
        else:
            print("No flat for you")
else:
    print("Too young, no flat for you")

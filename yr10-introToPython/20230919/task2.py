holidayChoice: str = str(input("Do you want to go on holiday?[y/n]")).lower()
if holidayChoice == "y":
    passportChoice: str = str(input("Do you have a passport?[y/n]")).lower()
    if passportChoice == "y":
        print("You can go on holiday anywhere")
    elif passportChoice == "n":
        print("You can only go in the UK?")
else:
    print("No Holiday for you")

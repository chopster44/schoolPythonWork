print("You have tied balloons to your house")
flyAnswer: str = str(input("Will the house fly away?"))
if flyAnswer == "yes":
    print("You are in a far away land")
elif flyAnswer == "no":
    print("You don't have enough balloons")
    moreAnswer: str = str(input("Do you want to add more balloons?"))
    if moreAnswer == "yes":
        print("That's enough balloons....you have flown away!")
    else:
        print("Still not enough balloons")
else:
    print("Error! Answer should just been yes or no")

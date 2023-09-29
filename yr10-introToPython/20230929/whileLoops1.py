while True:
    puppies: str=str(input("Do you like puppies? ")).lower()
    if puppies == "no":
        print("Wrong answer")
    elif puppies == "yes":
        print("Right answer")
        break
    else:
        print("Error")

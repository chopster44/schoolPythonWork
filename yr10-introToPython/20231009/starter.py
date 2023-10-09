login: bool = False

while not login:
    password: str = str(input("Please enter your password"))
    if password == "dogs":
        print("Logged in")
        login=True
    else:
        print("Not logged in\n")
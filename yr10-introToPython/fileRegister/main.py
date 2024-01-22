file = open("./register.txt", "+r")

key: dict[str, str] = {
    "present": "/",
    "illness": "M",
    "trip": "T",
    "absent": "X"
}

content = file.read()

names = content.split("\n")[0].split(",")

register: list[str] = []


def doRegister():
    strOut: str = ""
    print(f"Welcome to the reigister\n You have {len(names)} Students in your class")
    print(f"\n Key: present '{key['present']}', illness '{key['illness']}', trip '{key['trip']}', absent '{key['absent']}'")

    for i in range(0, len(names) - 1, 1):
        status: str = str(input(f"{names[i]}: "))
        register.append(status)

    for i in register:
        strOut += f"{i},"

    strOut +="\n"

    while True:
        save: str = str(input("Save (s) or repeat (r) "))

        if save == "s":
            file.write(strOut)
            file.close(),
            break
        elif save == "r":
            doRegister()
            break
        else:
            pass

doRegister()

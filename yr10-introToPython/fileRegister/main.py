file = open("register.txt", "+r")

key: dict[str, str] = {
    "present": "/",
    "illness": "M",
    "trip": "T",
    "absent": "X"
}

content = file.read()

file.close()

names = content.split("\n")[0].split(",")

register: list[str] = []

print(f"Welcome to the reigister\n You have {len(names)} Students in your class 
      \n Key: present '{key['present']}', illness '{key['illness']}', trip '{key['trip']}', absent '{key['absent']}'")

for i in range(0, len(names), 1):
    status: str = str(input(f"{names[i]}: "))



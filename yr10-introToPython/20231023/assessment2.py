temp: int = int(input("What is the classroom temperature"))

if temp > 35:
    print("Too hot, school's out")
elif 30 < temp < 35:
    door: str = input("Does the classroom have a door? ")
    if door.lower() == "yes":
        print("Open the door")
    else:
        print("Too hot, have the lesson outside")
else:
    print("Temperature is fine, lessons continue as usual")
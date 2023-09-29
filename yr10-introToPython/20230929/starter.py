age: int = int(input("How old are you?"))
if age < 13:
    print("You cant drive tractors")
elif age <= 15:
    print("You can drive a low power tractor")
elif age == 16:
    print("You can have a provisional liscense")
elif age < 21:
    print("You can drive tractors less than 3.5 tonnes")
else:
    print("You can drive tractors")
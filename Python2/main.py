while True:
    distance = int(input("How far would you like to go? ")) 
    if distance > 0: break 
    else: print("Invalid distance, must be greater than 0")
passengers: int = int(input("How many passengers are you going to take? "))
print(f"Your total is £{(distance * 1.5) + (passengers * 2.0)}")
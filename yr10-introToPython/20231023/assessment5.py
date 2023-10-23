from random import randint

print("Welcome to dice game!\n")

while True:
    menu: str = input("Press Enter to roll the dice or type 'quit' to exit: ")
    if menu == "":
        print("[Pressed Enter]\n")
        dice1: int = randint(0,6) + 1
        dice2: int = randint(0,6) + 1
        print(f"You rolled a {dice1} and a {dice2}. The sum is {dice1 + dice2}. You {'win' if (dice1 + dice2) == 7 else 'loose'}")
    else:
        break

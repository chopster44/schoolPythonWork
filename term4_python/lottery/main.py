import random
print("Welcome to the lottery!")

choices: list = [];
while len(choices) < 5:
    choice: int = int(input("Enter a number between 1 and 20: "))
    if choice < 1 or choice > 20:
        print("You can only choose between 1 and 20.")
        continue
    choices.append(choice)

print("Okay! Time for the draw!")

rolls: list = [];
while len(rolls) < 5:
    roll: int = random.randint(1, 20)
    print(f"The lottery ball is: {roll}")
    rolls.append(roll)

correct: int = 0;
for choice in choices:
    if choice in rolls:
        correct += 1

print(f"You got {correct} correct! Well done and thanks for playing!")

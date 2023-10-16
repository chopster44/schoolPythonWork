from random import randint
# Generate a random number between 1 and 10
secret_number: int = randint(1, 10)

# Allow the user to guess the number
for attempts in range(3):
    guess: int = int(input("Guess the number (1-10): "))

    if guess == secret_number:
        print("Congratulations! You guessed the secret number.")
        break
    else:
        if guess > secret_number:
                print("Try a higher number.")
        elif guess < secret_number:
            print("Try a lower number.")
        else: 
            print(f"Out of attempts. The secret number was {secret_number}")

from random import randint
# Generate a random number between 1 and 10
secret_number: int = randint(1, 10)

attempt_taken: int = 0

# Allow the user to guess the number
for attempts in range(10):
    guess: int = int(input("Guess the number (1-10): "))
    attempt_taken += 1

    if guess == secret_number:
        print(f"Congratulations! You guessed the secret number. You took {attempt_taken} attempts")
        break
    else:
        if guess > secret_number:
            print("Try a higher number.")
        elif guess < secret_number:
            print("Try a lower number.")
        else: 
            print(f"Out of attempts. The secret number was {secret_number}")

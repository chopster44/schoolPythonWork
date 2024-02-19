from random import choice
print("Task 1: ");

destinations = ["Paris", "London", "Barcelona", "Berlin", "Libson"]
print(f"Why don't you go to {choice(destinations)}?")

print("Task 2: ")
vowels =  "aeiou"
vowel = choice(vowels)
if input("Enter a vowel: ") == vowel:
    print(f"Random vowel: {vowel}")
    print("The vowels matched!")
else:
    print(f"Random vowel: {vowel}")
    print("The vowels were not the same");
import random
# List of treats
treats = "Chocolate cake", "Fruit salad", "Ice cream", "Cookies", "Yogurt"

# Assume the user has eaten all their vegetables (you can modify this condition)
has_eaten_vegetables = input("Have you eaten all your vegtables?")

if has_eaten_vegetables=="yes":
    num = random.randint(0,len(treats))
    chosen_treat = treats[num]
    print("Congratulations! You've earned a " +chosen_treat+" for dessert.")
else:
    print("Remember to eat your vegetables first!")